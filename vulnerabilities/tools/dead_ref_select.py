"""Chooses the citations of acts no longer in force (Spain only, global-law's es_crossref.py) for global-law's own review of
that category (triage/dead_ref_triage.py): the 40 strongest, one per citing provision and cited act, ties on score broken
in a fixed order (md5 of the row), as triage.py does for the other categories.

    python -X utf8 dead_ref_select.py [N]   -> gl/vulnerabilities/scripts/findings/runref/ranked_dead_act_ref.parquet
then    python -X utf8 triage/dead_ref_triage.py runref --min 0     (in gl/vulnerabilities/scripts, with llm_env.sh sourced)
and     python -X utf8 dead_ref_rebut.py
"""
import os, sys
import duckdb

N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gl", "vulnerabilities", "scripts", "findings")
src = os.path.join(F, "run", "ranked_dead_act_ref.parquet").replace("\\", "/")
os.makedirs(os.path.join(F, "runref"), exist_ok=True)
dst = os.path.join(F, "runref", "ranked_dead_act_ref.parquet").replace("\\", "/")
duckdb.sql(f"""copy (
    with one as (select *, row_number() over (partition by path, cited_id order by score desc, line) k from '{src}')
    select * exclude (k) from one where k = 1
    order by score desc, md5(path || cited_id || cast(line as varchar)) limit {N}) to '{dst}' (format parquet)""")
print(duckdb.sql(f"select count(*), min(score) from '{dst}'").fetchall())
