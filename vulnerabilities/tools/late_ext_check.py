"""Hand-check helper: for each empty-period flag that survived the rebuttal, the lines of the extending commit's diff that
hold the old or the new date (Spanish or numeric forms).

    python -X utf8 late_ext_check.py        (run in the workspace folder, next to gl/)
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "gl", "vulnerabilities", "scripts")
G = os.path.join(S, "sources", "corpus", "spain-law.git")
PIN = json.load(open(os.path.join(S, "pins.json"), encoding="utf-8"))["corpora"][0]["sha"]
MON = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()


def forms(d):
    y, m, dd = d.split("-"); m, dd = int(m), int(dd)
    return [f"{dd} de {MON[m-1]} de {y}", f"{dd} de {MON[m-1]} del {y}", f"{dd}/{m}/{y}", f"{dd:02d}/{m:02d}/{y}", f"{dd}-{m}-{y}", d]


def git(*a):
    return subprocess.run(["git", "--git-dir", G, *a], capture_output=True).stdout.decode("utf-8", "replace")


seen = set()
for x in map(json.loads, open(os.path.join(S, "findings", "run", "late_extension_triage.jsonl"), encoding="utf-8")):
    if not (x.get("rebut") or {}).get("survives"):
        continue
    r = x["row"]; k = (r["path"], r["old_until"], r["new_until"], r["law"])
    if k in seen:
        continue
    seen.add(k)
    c = [l.split()[0] for l in git("log", "--format=%h %an", PIN, "--", r["path"]).splitlines() if l.split(" ", 1)[1] == r["law"]]
    hits = []
    for cc in c:
        d = git("diff", "-U0", "--word-diff", f"{cc}^", cc, "--", r["path"])
        for line in d.splitlines():
            if not ("{+" in line or "[-" in line):
                continue
            # the full date, or a word-diff that changes only part of it ("31 de diciembre de [-2025-]{+2026+}")
            yo, yn = r["old_until"][:4], r["new_until"][:4]
            part = f"[-{yo}-]{{+{yn}+}}" in line or (f"[-{forms(r['old_until'])[0]}" in line)
            if part or any(f in line for f in forms(r["old_until"]) + forms(r["new_until"])):
                i = max(line.find(f"[-{yo}"), line.find(forms(r["old_until"])[0]), line.find(forms(r["new_until"])[0]), 0)
                hits.append(f"{cc} ..." + line.strip()[max(0, i - 250):i + 150])
    title = git("show", f"{PIN}:{r['path'].rsplit('/', 1)[0]}/README.md").splitlines()[:1]
    print(f"## {r['path']} {title[0][2:110] if title else ''}\n   {r['old_until']} -> {r['new_until']} by {r['law']} in force {r['extended_in_force']} ({r['gap_days']} d)")
    for h in hits[:4]:
        print("     ", h)
    if not hits:
        print("      (no diff line holds either date)")
