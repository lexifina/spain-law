"""Write Spain's consolidated state legislation as a git history, streamed into git fast-import.

    python -X utf8 build.py --repo NEW_DIR --today 2026-10-28 --docs-date 2026-10-28 [--laws ID,ID] [--no-docs]
    python -X utf8 build.py --repo DIR --verify-rebuild     # build again into a temporary folder; heads must match

Input: cache/parsed.sqlite (parse.py). Layout: `estatal/<rango>/<BOE id>/<block>.md`, one file per block (article,
heading, preamble, annex ...) of each norm, with one paragraph per line, plus a README.md per norm listing its blocks
in the BOE's order.

Commits, oldest first: one per amending norm (id_norma) per in-force date (fecha_vigencia) of the block versions it
wrote, authored by that norm (`BOE-A-2015-7391 (Ley 15/2015, de 2 de julio)` <boe-a-2015-7391@boe.invalid>), dated
noon Europe/Madrid that day. After the last commit of a day every block equals the BOE's version for that day. A
version the BOE gives no norm for is committed by the publisher, labelled. A version that changes nothing gets no commit.
Versions in force after --today are left out (there is no future branch). Dates before 1970 are clamped to
1970-01-01T00:00:01Z onwards, one second apart; In-force: keeps the real date.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

HERE = Path(__file__).resolve().parent
PARSED = HERE / "cache" / "parsed.sqlite"
COMMITTER = "Lexifina <spain-law@lexifina.com>"
PUBLISHER = ("Agencia Estatal Boletin Oficial del Estado (BOE)", "publisher@boe.invalid")
ROOT = "estatal"


def madrid_noon(date: str) -> str:
    """Noon in Madrid as a git date: CET (+0100), CEST (+0200) from the last Sunday of March to the last Sunday of
    October (start <= day < end), the EU rule, applied to every year from 1970."""
    y, m, d = map(int, date.split("-"))
    day = dt.date(y, m, d)

    def last_sunday(month: int) -> dt.date:
        last = dt.date(y, month, 31)
        return last - dt.timedelta(days=(last.weekday() + 1) % 7)

    summer = last_sunday(3) <= day < last_sunday(10)
    stamp = dt.datetime(y, m, d, 10 if summer else 11, 0, tzinfo=dt.timezone.utc)
    return f"{int(stamp.timestamp())} {'+0200' if summer else '+0100'}"


class Clock:
    def __init__(self) -> None:
        self.clamped = 0

    def stamp(self, date: str) -> str:
        if date < "1970-01-01":
            self.clamped += 1
            return f"{self.clamped} +0000"
        return madrid_noon(date)


def natural(norma: str):
    m = re.fullmatch(r"([A-Z]+-[A-Za-z]+)-(\d{4})-(\d+)", norma)
    return (0, m.group(1), int(m.group(2)), int(m.group(3)), norma) if m else (1, "", 0, 0, norma)


def short_title(t: str) -> str:
    """'Ley 15/2015, de 2 de julio, de la Jurisdiccion Voluntaria.' -> 'Ley 15/2015, de 2 de julio'."""
    t = re.sub(r"\s+", " ", t or "").strip().rstrip(".")
    m = re.match(r"^(.{0,80}?\d+/\d{4},? de \d{1,2} de [a-záéíóú]+(?: de \d{4})?)", t, re.I)
    if m:
        return m.group(1)
    return t if len(t) <= 100 else t[:99].rstrip() + "…"


def shorten(s: str, n: int = 72) -> str:
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def git_name(s: str) -> str:
    return re.sub(r"[<>\n\r]", "", s)[:200]


def law_dir(meta: Dict) -> str:
    import boe
    return boe.law_dir(meta["rslug"], meta["id"])


def law_readme(meta: Dict, blocks: List[Tuple], present) -> str:
    lines = [f"# {meta['titulo']}", "",
             f"- Identificador: {meta['id']}",
             f"- Rango: {meta['rango']}",
             *( [f"- Fecha de disposición: {meta['fdisp']}"] if meta["fdisp"] else []),
             *( [f"- Publicación: {meta['fpub']}"] if meta["fpub"] else []),
             f"- Texto consolidado: https://www.boe.es/buscar/act.php?id={meta['id']}",
             "",
             "Texto consolidado de carácter meramente informativo. Basado en datos de la Agencia Estatal Boletín "
             "Oficial del Estado (https://www.boe.es). Solo tienen carácter oficial y auténtico los textos publicados "
             "en el diario oficial «Boletín Oficial del Estado».",
             "",
             "## Bloques", ""]
    for idx, block, tipo, titulo, fname in blocks:
        if idx in present:
            lines.append(f"- [{(titulo or block).replace('[', '(').replace(']', ')')}]({fname}.md)")
    return "\n".join(lines) + "\n"


def load(con: sqlite3.Connection, only: List[str]):
    laws = {}
    for r in con.execute("select id, rango, rslug, titulo, fdisp, fpub, fvig, fact, agotada, estado, status from laws"):
        if only and r[0] not in only:
            continue
        laws[r[0]] = dict(zip(("id", "rango", "rslug", "titulo", "fdisp", "fpub", "fvig", "fact", "agotada", "estado", "status"), r))
    blocks: Dict[str, List[Tuple]] = defaultdict(list)
    for law, idx, block, tipo, titulo, fname in con.execute("select law, idx, block, tipo, titulo, fname from blocks order by law, idx"):
        if law in laws:
            blocks[law].append((idx, block, tipo, titulo, fname))
    titles = {r[0]: (r[1], r[2]) for r in con.execute("select norma, titulo, src from titles")}
    return laws, blocks, titles


VALID = re.compile(r"[A-Z]+-[A-Za-z]+-\d{4}-\d+")


def valid(norma: str) -> bool:
    """A BOE identifier. The data also has 'BOE-A-0-0' (48 versions) and typos such as 'BOE-A-201-9739': those are
    credited to no norm, never repaired."""
    return bool(VALID.fullmatch(norma or ""))


def author_of(norma: str, titles) -> Tuple[str, str]:
    if not valid(norma):
        return PUBLISHER
    t = titles.get(norma)
    name = f"{norma} ({short_title(t[0])})" if t else norma
    return git_name(name), re.sub(r"[^a-z0-9]+", "-", norma.lower()).strip("-") + "@boe.invalid"


def write(repo: Path, today: str, docs_date: str, only: List[str], docs: Dict[str, str]) -> Dict:
    if repo.exists() and any(repo.iterdir()):
        raise SystemExit(f"{repo} is not empty; the history is written into a new, empty directory")
    repo.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repo, check=True)
    subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=repo, check=True)
    con = sqlite3.connect(PARSED)
    laws, blocks, titles = load(con, only)
    fname = {(law, b[0]): b[4] for law, bl in blocks.items() for b in bl}
    cur: Dict[Tuple[str, int], bytes] = {}
    present: Dict[str, set] = defaultdict(set)
    clock = Clock()
    fi = subprocess.Popen(["git", "fast-import", "--quiet", "--done"], cwd=repo, stdin=subprocess.PIPE)
    out = fi.stdin
    stats = defaultdict(int)
    mark = 0
    t0 = time.time()

    def emit(author: Tuple[str, str], when: str, message: str, files: Dict[str, str]) -> None:
        nonlocal mark
        mark += 1
        msg = message.encode("utf-8")
        out.write(f"commit refs/heads/main\nmark :{mark}\n".encode())
        out.write(f"author {author[0]} <{author[1]}> {when}\ncommitter {COMMITTER} {when}\n".encode("utf-8"))
        out.write(f"data {len(msg)}\n".encode() + msg + b"\n")
        if mark > 1:
            out.write(f"from :{mark - 1}\n".encode())
        for path in sorted(files):
            data = files[path].encode("utf-8")
            out.write(f"M 100644 inline {path}\ndata {len(data)}\n".encode() + data + b"\n")

    dates = [r[0] for r in con.execute("select distinct date from versions where date <= ? order by date", (today,))]
    stats["future_versions"] = con.execute("select count(*) from versions where date > ?", (today,)).fetchone()[0]
    for n_day, date in enumerate(dates):
        rows = con.execute("select norma, law, idx, fpub, text from versions where date=?", (date,)).fetchall()
        groups: Dict[str, List[Tuple]] = defaultdict(list)
        for norma, law, idx, fpub, text in rows:
            if law in laws:
                groups[norma].append((law, idx, fpub, text))
        for norma in sorted(groups, key=natural):
            files: Dict[str, str] = {}
            changed: Dict[str, List[int]] = defaultdict(list)
            new_laws: List[str] = []
            fpubs = defaultdict(int)
            for law, idx, fpub, text in sorted(groups[norma], key=lambda r: (r[0], r[1])):
                stats["versions"] += 1
                h = hashlib.blake2b(text.encode("utf-8"), digest_size=16).digest()
                if cur.get((law, idx)) == h:
                    stats["versions_unchanged"] += 1
                    continue
                cur[(law, idx)] = h
                if not present[law]:
                    new_laws.append(law)
                d = law_dir(laws[law])
                files[f"{d}/{fname[(law, idx)]}.md"] = text
                changed[law].append(idx)
                if fpub:
                    fpubs[fpub] += 1
            if not files:
                stats["groups_without_change"] += 1
                continue
            for law in changed:
                before = set(present[law])
                present[law].update(changed[law])
                if present[law] != before:
                    files[f"{law_dir(laws[law])}/README.md"] = law_readme(laws[law], blocks[law], present[law])
            author = author_of(norma, titles)
            subject, body = describe(norma, date, changed, new_laws, laws, blocks, titles, fpubs)
            when = clock.stamp(date)
            if date < "1970-01-01":
                body = body.replace("\n\nIn-force:", "\n\nGit cannot store dates before 1970: this commit is dated "
                                    f"1970-01-01T00:00:00Z plus {clock.clamped} s, in order. The real date is In-force.\n\nIn-force:", 1)
            emit(author, when, subject + "\n\n" + body, files)
            stats["commits"] += 1
            stats["publisher_commits" if not valid(norma) else "law_commits"] += 1
            stats["files_written"] += len(files)
        if n_day % 2000 == 0:
            print(f"{date}: {n_day}/{len(dates)} days, {stats['commits']} commits, {time.time() - t0:.0f} s", flush=True)
    if mark:
        out.write(f"reset refs/heads/law-head\nfrom :{mark}\n\n".encode())
    stats["laws_written"] = sum(1 for l in present if present[l])
    stats["clamped"] = clock.clamped
    stats["last_in_force"] = dates[-1] if dates else ""
    stats["first_in_force"] = dates[0] if dates else ""
    if docs:
        emit(("Lexifina", "spain-law@lexifina.com"), madrid_noon(docs_date),
             "README, REPRODUCE, corpus.json and tools: how the history is read, built and checked\n", docs)
    out.write(b"done\n")
    out.close()
    if fi.wait():
        raise SystemExit("git fast-import failed")
    # Timings are printed, never stored: build-stats.json feeds REPRODUCE.md, which must not change between rebuilds.
    print(f"fast-import {time.time() - t0:.0f} s", flush=True)
    return dict(stats)


def describe(norma, date, changed, new_laws, laws, blocks, titles, fpubs) -> Tuple[str, str]:
    who = short_title(titles[norma][0]) if norma in titles and valid(norma) else (norma if valid(norma) else "BOE")
    lawlist = sorted(changed)
    if len(lawlist) == 1:
        law = lawlist[0]
        tgt = short_title(laws[law]["titulo"])
        if law in new_laws:
            subject = f"{who}: texto inicial" if norma == law else f"{who}: {tgt}, primer texto"
        else:
            subject = f"{who}: {tgt} ({len(changed[law])})"
    else:
        subject = f"{who}: {len(lawlist)} normas ({sum(len(v) for v in changed.values())})"
    lines = []
    if norma in titles and valid(norma):
        lines += [titles[norma][0].strip(), ""]
    if not norma:
        lines += ["The BOE gives no amending norm for these versions; committed by the publisher, labelled.", ""]
    elif not valid(norma):
        lines += [f"The BOE gives id_norma \"{norma}\" for these versions, which is not a BOE identifier; they are "
                  "credited to no norm and committed by the publisher, labelled. The identifier is not corrected.", ""]
    lines.append(f"In force from {date}:")
    bname = {(l, b[0]): (b[3] or b[1]) for l in lawlist for b in blocks[l]}
    for law in lawlist[:300]:
        idxs = sorted(changed[law])
        label = ", ".join(bname[(law, i)] for i in idxs[:40]) + (f" ... (+{len(idxs) - 40})" if len(idxs) > 40 else "")
        lines.append(f"- {laws[law]['titulo'][:200]} ({law}): {label}")
        if law in new_laws:
            lines.append(f"  First text of this norm in the BOE consolidated record (in force {date}"
                         + (f"; dated {laws[law]['fdisp']}" if laws[law]["fdisp"] else "")
                         + (f", published {laws[law]['fpub']}" if laws[law]["fpub"] else "") + ").")
        lines.append(f"  https://www.boe.es/buscar/act.php?id={law}")
    if len(lawlist) > 300:
        lines.append(f"... and {len(lawlist) - 300} more norms")
    trailers = [f"In-force: {date}"]
    if fpubs:
        trailers.append(f"Published: {sorted(fpubs, key=lambda k: (-fpubs[k], k))[0]}")
    if norma and not valid(norma):
        trailers.append(f"Explained-by: none (id_norma {norma} is not a valid BOE identifier)")
    elif norma:
        trailers.append(f"Norma: {norma}")
        if norma in laws and laws[norma]["fdisp"]:
            trailers.append(f"Enacted: {laws[norma]['fdisp']}")
        trailers.append(f"Source: https://www.boe.es/buscar/doc.php?id={norma}")
    else:
        trailers.append("Explained-by: none (no id_norma in the BOE data)")
    trailers.append(f"Laws-changed: {len(lawlist)}")
    return shorten(subject), "\n".join(lines) + "\n\n" + "\n".join(trailers) + "\n"


def checkout(repo: Path) -> None:
    subprocess.run(["git", "-c", "checkout.workers=8", "-c", "checkout.thresholdForParallelism=100", "-c", "core.fscache=true", "checkout", "-q", "-f", "main"], cwd=repo, check=True)


def head(repo: Path, ref: str = "main") -> str:
    return subprocess.run(["git", "rev-parse", ref], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--today", default="2026-10-28", help="the data's retrieval day: versions in force after it are left out")
    ap.add_argument("--docs-date", default=None, help="the day of the data, dating the documentation commit")
    ap.add_argument("--laws", default="")
    ap.add_argument("--no-docs", action="store_true")
    ap.add_argument("--no-checkout", action="store_true")
    ap.add_argument("--verify-rebuild", action="store_true")
    ap.add_argument("--record", action="store_true", help="with --verify-rebuild: write the result to cache/verification.json")
    a = ap.parse_args()
    only = [x for x in a.laws.split(",") if x]
    repo = Path(a.repo)
    if a.verify_rebuild:
        want, want_law = head(repo), head(repo, "law-head")
        with tempfile.TemporaryDirectory(dir=HERE / "cache") as tmp:
            r = subprocess.run([sys.executable, "-X", "utf8", __file__, "--repo", str(Path(tmp) / "r"), "--today", a.today,
                                "--docs-date", a.docs_date or a.today, "--no-checkout"] + (["--laws", a.laws] if a.laws else [])
                               + (["--no-docs"] if a.no_docs else []), check=True)
            got, got_law = head(Path(tmp) / "r"), head(Path(tmp) / "r", "law-head")
            shutil.rmtree(Path(tmp) / "r", ignore_errors=True)
        summary = (f"law-head {got_law} vs {want_law}: {'IDENTICAL' if got_law == want_law else 'DIFFERENT'}; "
                   f"main {got} vs {want}: {'IDENTICAL' if got == want else 'DIFFERENT'}")
        print(summary)
        if a.record:
            # Recorded for the next build's REPRODUCE.md. The law history (law-head) must match; main differs only if
            # this file changed since the compared build, as it does when results are first recorded.
            p = HERE / "cache" / "verification.json"
            rec = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
            rec["rebuild"] = {"summary": f"a second build from the same data gave the identical law history (law-head {got_law[:12]}, "
                                         f"{'same' if got_law == want_law else 'DIFFERENT'} hash for all law commits)",
                              "ok": got_law == want_law}
            p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        return 0 if got == want else 1
    if not a.docs_date and not a.no_docs:
        raise SystemExit("--docs-date is required (the day of the data), or pass --no-docs")
    docs = {}
    if not a.no_docs:
        import reproduce
        docs = reproduce.docs(a.today, a.docs_date, only)
    stats = write(repo, a.today, a.docs_date or a.today, only, docs)
    print(json.dumps(stats, sort_keys=True))
    (HERE / "cache" / "build-stats.json").write_text(json.dumps(stats, sort_keys=True, indent=1) + "\n", encoding="utf-8")
    if not a.no_checkout:
        t = time.time()
        checkout(repo)
        print(f"checkout {time.time() - t:.0f} s")
    print("main", head(repo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
