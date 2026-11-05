"""Check the built repository against the BOE data, version by version.

    python -X utf8 check_repo.py --repo ../../../spain-law --today 2026-10-28 [--procs 6] [--record]

For every block version in force on or before --today (cache/parsed.sqlite), including versions that changed nothing
and so have no commit of their own: the file at the last commit whose In-force is on or before the version's date
must equal the version's text byte for byte. Separately, the words of the version's XML (read from the cached
/texto answer, joined with spaces only at block-element boundaries) must equal the words of the file (parse.py
stores that comparison per version). Also: the files of main's head are exactly the blocks in force on --today.
Blobs are read through one long-lived `git cat-file --batch` per process.
"""
from __future__ import annotations

import argparse
import bisect
import json
import multiprocessing as mp
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import boe  # noqa: E402
PARSED = HERE / "cache" / "parsed.sqlite"


class Blobs:
    def __init__(self, repo: str) -> None:
        self.p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=repo, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def read(self, spec: str):
        self.p.stdin.write(spec.encode("utf-8") + b"\n")
        self.p.stdin.flush()
        head = self.p.stdout.readline().split()
        if len(head) < 3 or head[1] == b"missing":
            return None
        data = self.p.stdout.read(int(head[2]))
        self.p.stdout.read(1)
        return data.decode("utf-8")


def days_of(repo: str):
    out = subprocess.run(["git", "log", "--reverse", "--first-parent",
                          "--format=%H %(trailers:key=In-force,valueonly,separator=)", "main"],
                         cwd=repo, capture_output=True, text=True, check=True).stdout
    days, shas = [], []
    for line in out.splitlines():
        sha, _, d = line.partition(" ")
        d = d.strip()
        if d:
            if days and d < days[-1]:
                raise SystemExit(f"In-force goes backwards at {sha}: {d} after {days[-1]}")
            days.append(d)
            shas.append(sha)
    return days, shas


def check_shard(args):
    repo, today, laws, days, shas = args
    con = sqlite3.connect(PARSED)
    meta = {r[0]: r[1] for r in con.execute("select id, rslug from laws")}
    blobs = Blobs(repo)
    checked = bad = 0
    first_bad = []
    for law in laws:
        fn = {r[0]: r[1] for r in con.execute("select idx, fname from blocks where law=?", (law,))}
        for idx, date, text in con.execute("select idx, date, text from versions where law=? and date<=? order by idx, date", (law, today)):
            i = bisect.bisect_right(days, date) - 1
            path = f"{boe.law_dir(meta[law], law)}/{fn[idx]}.md"
            got = blobs.read(f"{shas[i]}:{path}") if i >= 0 else None
            checked += 1
            if got != text:
                bad += 1
                if len(first_bad) < 10:
                    first_bad.append(f"{path} {date}")
    return checked, bad, first_bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--today", required=True)
    ap.add_argument("--procs", type=int, default=6)
    ap.add_argument("--laws", default="")
    ap.add_argument("--record", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    con = sqlite3.connect(PARSED)
    only = [x for x in a.laws.split(",") if x]
    laws = [r[0] for r in con.execute("select id from laws where status=200 order by id") if not only or r[0] in only]
    days, shas = days_of(a.repo)
    shards = [laws[i::a.procs] for i in range(a.procs)]
    checked = bad = 0
    first_bad = []
    with mp.Pool(a.procs) as pool:
        for c, b, fb in pool.imap_unordered(check_shard, [(a.repo, a.today, s, days, shas) for s in shards]):
            checked += c
            bad += b
            first_bad += fb
    words_bad = con.execute("select count(*) from versions where date<=? and words_ok=0", (a.today,)).fetchone()[0]
    words_bad_ex = [f"{r[0]} block {r[1]} {r[2]}" for r in con.execute(
        "select law, idx, date from versions where date<=? and words_ok=0 limit 10", (a.today,))]
    # Head: exactly the blocks in force on --today.
    want = set()
    meta = {r[0]: r[1] for r in con.execute("select id, rslug from laws")}
    for law, fname in con.execute("select distinct v.law, b.fname from versions v join blocks b on b.law=v.law and b.idx=v.idx where v.date<=?", (a.today,)):
        if not only or law in only:
            want.add(f"{boe.law_dir(meta[law], law)}/{fname}.md")
    have = {p for p in subprocess.run(["git", "ls-tree", "-r", "--name-only", "main", "estatal/"], cwd=a.repo,
                                      capture_output=True, text=True, encoding="utf-8", check=True).stdout.splitlines()
            if not p.endswith("/README.md")}
    undated = con.execute("select count(*) from undated").fetchone()[0]
    same_day = con.execute("select count(*) from same_day").fetchone()[0]
    summary = (f"{checked:,} block versions checked on their dates, {bad} differ; {words_bad} differ word for word from "
               f"the XML; head files {len(have):,}, missing {len(want - have)}, extra {len(have - want)}")
    print(summary)
    for x in first_bad:
        print("DIFFERS", x)
    for x in words_bad_ex:
        print("WORDS", x)
    print(f"undated versions left out: {undated}; earlier same-day versions left out: {same_day}; {time.time() - t0:.0f} s")
    ok = not bad and not words_bad and want == have
    if a.record:
        p = HERE / "cache" / "verification.json"
        rec = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
        rec["check"] = {"summary": summary, "ok": ok, "checked": checked, "differ": bad, "words_differ": words_bad}
        rec["undated"] = undated
        rec["same_day"] = same_day
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
