"""The rebuttal step for citations of acts no longer in force (Spain), as triage.py does it for the other categories: for
each flag global-law's dead_ref_triage.py called a candidate defect, a second call gives the strongest argument that it is
not, and says whether the flag survives.

    (source llm_env.sh)  python -X utf8 dead_ref_rebut.py
Reads gl/vulnerabilities/scripts/findings/runref/dead_act_ref_triage.jsonl, writes findings/run/dead_act_ref_triage.jsonl
(the same records, with "rebut" added to each candidate_defect).
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.join(HERE, "gl", "vulnerabilities", "scripts")
sys.path.insert(0, os.path.join(SCR, "ingest"))
sys.path.insert(0, os.path.join(SCR, "triage"))
from llm import call  # noqa: E402
import triage as T  # noqa: E402

SRC = os.path.join(SCR, "findings", "runref", "dead_act_ref_triage.jsonl")
DST = os.path.join(SCR, "findings", "run", "dead_act_ref_triage.jsonl")
PIN = json.load(open(os.path.join(SCR, "pins.json"), encoding="utf-8"))["corpora"][0]["sha"]
GIT = os.path.join(SCR, "sources", "corpus", "spain-law.git")
recs = [json.loads(l) for l in open(SRC, encoding="utf-8")]


def work(rec):
    if rec["j"]["verdict"] != "candidate_defect" or rec.get("rebut"):
        return rec
    r = rec["row"]
    txt = subprocess.run(["git", "-C", GIT, "show", f"{PIN}:{r['path']}"], capture_output=True).stdout.decode("utf-8", "replace")[:6000]
    ev = (f"File: {r['path']} (a provision of Spanish state law in force, last rewritten {r['citing_last_change']} by "
          f"{r['citing_last_law']}).\nIt cites {r['cite']}: {r['cited_title']} ({r['cited_id']}), which BOE lists as no longer "
          f"in force (last change in the record {r['cited_last_change']}).\n\nTEXT OF THE CITING PROVISION:\n{txt}")
    rb = call(f"Another analyst claims this citation of an act no longer in force is a real defect. Give the strongest argument "
              f"that it is NOT (for example: a general clause of the replacing act says references to the old act are read as "
              f"references to the new one; the citation is historical or descriptive; the cited act still applies to earlier "
              f"cases; a different act with the same number is meant; the provision is spent), and rate how likely that "
              f"argument wins.\n\nEVIDENCE\n{ev}\n\nCLAIM\n{json.dumps(rec['j'], ensure_ascii=False)}",
              system=T.SYSTEM, schema=T.REBUT, provider="azure")
    rec["rebut"] = rb["json"]
    return rec


with ThreadPoolExecutor(12) as ex:
    recs = list(ex.map(work, recs))
with open(DST, "w", encoding="utf-8", newline="\n") as f:
    for rec in recs:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
cand = [r for r in recs if r["j"]["verdict"] == "candidate_defect"]
print(len(recs), "reviewed;", len(cand), "candidate defects;", sum(1 for r in cand if r["rebut"]["survives"]), "survive the rebuttal")
