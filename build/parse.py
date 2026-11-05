"""Parse the cached BOE XML into cache/parsed.sqlite: laws, blocks and the block versions the history uses.

    python -X utf8 parse.py [--ambito Estatal] [--procs 8]

Per block, versions are kept in the order the BOE gives them. A version without a real fecha_vigencia is not dated and
cannot be placed in time: it is recorded in `undated` and left out. Where a block has two or more versions with the
same fecha_vigencia, the last one in the BOE's order is the text in force that day; the others are recorded in
`same_day` and left out (one version per block per date).
"""
from __future__ import annotations

import argparse
import gzip
import json
import multiprocessing as mp
import re
import sqlite3
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import boe  # noqa: E402
from fetch import API, connect, get, norms  # noqa: E402

RESERVED = {"con", "prn", "aux", "nul", "readme", *(f"com{i}" for i in range(10)), *(f"lpt{i}" for i in range(10))}


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "otro"


def filenames(ids):
    """Block ids -> file names: safe characters, no Windows device names, unique without regard to case."""
    out, seen = [], set()
    for i in ids:
        f = re.sub(r"[^A-Za-z0-9._-]+", "-", i).strip(".-") or "bloque"
        if f.lower() in RESERVED:
            f = "_" + f
        base, n = f, 2
        while f.lower() in seen:
            f = f"{base}-{n}"
            n += 1
        seen.add(f.lower())
        out.append(f)
    return out


def refs_of(x, kind):
    """(kind, reference) for every dict with an id_norma under 'anterior' or 'posterior', whatever the nesting
    (the JSON gives a list where there are several and a bare object where there is one)."""
    if isinstance(x, list):
        for y in x:
            yield from refs_of(y, kind)
    elif isinstance(x, dict):
        if "id_norma" in x and kind:
            yield kind, x
            return
        for k, v in x.items():
            yield from refs_of(v, k if k in ("anterior", "posterior") else kind)


def parse_one(ident: str):
    con = sqlite3.connect(HERE / "cache" / "boe.sqlite", timeout=60)
    got = get(con, f"{API}/id/{ident}/texto")
    con.close()
    if not got or got[0] != 200:
        return ident, (got[0] if got else None), [], [], [], []
    root = ET.fromstring(got[1])
    blocks, versions, undated, same_day = [], [], [], []
    bl = list(root.iter("bloque"))
    names = filenames([b.get("id") or f"bloque{i}" for i, b in enumerate(bl)])
    for idx, (b, fname) in enumerate(zip(bl, names)):
        blocks.append((ident, idx, b.get("id") or "", b.get("tipo") or "", b.get("titulo") or "", fname))
        kept = {}
        for vi, v in enumerate(b.findall("version")):
            d = boe.date(v.get("fecha_vigencia"))
            row = (ident, idx, vi, d, v.get("id_norma") or "", boe.date(v.get("fecha_publicacion")))
            if not d or d < "1800-01-01":
                # No date, the BOE's "99999999" (a date not yet fixed), or an impossible one (0998-01-01 for a
                # 1997 norm): left out and listed, never repaired.
                undated.append(row + (v.get("fecha_vigencia") or "",))
                continue
            text = boe.render(v)
            words_ok = boe.words_of_file(text) == boe.words_of_xml(v)
            if d in kept:
                same_day.append(kept[d][:6])
            kept[d] = row + (text, int(words_ok))
        versions += list(kept.values())
    return ident, 200, blocks, versions, undated, same_day


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ambito", default="Estatal")
    ap.add_argument("--procs", type=int, default=8)
    a = ap.parse_args()
    con = connect()
    data = norms(con, a.ambito)
    allnorms = norms(con, "")
    out_path = HERE / "cache" / "parsed.sqlite"
    if out_path.exists():
        out_path.unlink()
    out = sqlite3.connect(out_path, isolation_level=None)
    out.execute("pragma journal_mode=off")
    out.execute("pragma synchronous=off")
    out.executescript("""
        create table laws (id text primary key, ambito text, rango text, rslug text, titulo text, fdisp text, fpub text,
                           fvig text, fact text, agotada text, estado text, status int);
        create table blocks (law text, idx int, block text, tipo text, titulo text, fname text, primary key (law, idx));
        create table versions (law text, idx int, vi int, date text, norma text, fpub text, text text, words_ok int);
        create table undated (law text, idx int, vi int, date text, norma text, fpub text, raw text);
        create table same_day (law text, idx int, vi int, date text, norma text, fpub text);
        create table titles (norma text primary key, titulo text, src text);
    """)
    for d in data:
        out.execute("insert into laws values (?,?,?,?,?,?,?,?,?,?,?,?)", (
            d["identificador"], d["ambito"]["texto"], d["rango"]["texto"], slug(d["rango"]["texto"]), d["titulo"],
            boe.date(d.get("fecha_disposicion")), boe.date(d.get("fecha_publicacion")), boe.date(d.get("fecha_vigencia")),
            d.get("fecha_actualizacion") or "", d.get("vigencia_agotada") or "", d["estado_consolidacion"]["texto"], None))
    # Titles of norms: the consolidated list first, then the BOE's own analysis of each law ("..., por Ley 2/2020, de ...").
    for d in allnorms:
        out.execute("insert or replace into titles values (?,?,?)", (d["identificador"], d["titulo"], "list"))
    for d in data:
        got = get(con, f"{API}/id/{d['identificador']}/analisis")
        if not got or got[0] != 200:
            continue
        try:
            js = json.loads(got[1])["data"]
        except Exception:
            continue
        for kind, r in refs_of(js, ""):
            t = r.get("texto") or ""
            if not r.get("id_norma") or not t:
                continue
            if kind == "posterior":
                m = re.search(r"(?:^|,\s*)por\s+(?:el |la |los |las )?((?:(?!,\s*por\s).)+)$", t)
                if m:
                    out.execute("insert or ignore into titles values (?,?,?)", (r["id_norma"], m.group(1).strip(), "analisis"))
            elif kind == "anterior":
                out.execute("insert or ignore into titles values (?,?,?)", (r["id_norma"], t.strip(), "analisis"))
    t0 = time.time()
    n = 0
    out.execute("begin")
    with mp.Pool(a.procs) as pool:
        for ident, status, blocks, versions, undated, same_day in pool.imap_unordered(
                parse_one, sorted(d["identificador"] for d in data), chunksize=4):
            out.execute("update laws set status=? where id=?", (status, ident))
            out.executemany("insert into blocks values (?,?,?,?,?,?)", blocks)
            out.executemany("insert into versions values (?,?,?,?,?,?,?,?)", versions)
            out.executemany("insert into undated values (?,?,?,?,?,?,?)", undated)
            out.executemany("insert into same_day values (?,?,?,?,?,?)", same_day)
            n += 1
            if n % 500 == 0:
                print(f"{n}/{len(data)} laws parsed, {time.time() - t0:.0f} s", flush=True)
    out.execute("commit")
    out.execute("create index v_date on versions (date, norma, law, idx)")
    out.execute("create index v_law on versions (law, idx, date)")
    c = {k: out.execute(f"select count(*) from {k}").fetchone()[0] for k in ("laws", "blocks", "versions", "undated", "same_day")}
    bad = out.execute("select count(*) from versions where words_ok=0").fetchone()[0]
    print(f"parsed in {time.time() - t0:.0f} s: {c}; versions whose words differ from the XML: {bad}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
