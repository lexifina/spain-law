"""Spanish state law on a given day, read from this repository's history by the In-force trailers.

    python tools/eslaw.py on 2011-09-27 estatal/constitucion/1978/BOE-A-1978-31229/a135.md   # one block
    python tools/eslaw.py on 2011-09-27 estatal/constitucion/1978/BOE-A-1978-31229           # a whole norm, in order
    python tools/eslaw.py on 2011-09-27 estatal                                        # a folder: its entries
    python tools/eslaw.py 2011-09-27 estatal/constitucion/1978/BOE-A-1978-31229/a135.md      # "on" may be left out
    python tools/eslaw.py log estatal/constitucion/1978/BOE-A-1978-31229/a135.md             # in-force dates and authors

The version in force on a day is the last commit on main whose In-force trailer is on or before that day (commits
are in in-force order). It does not use `git log --before`, whose answer depends on the reader's time zone and on
the clamped pre-1970 commit dates. Standard library only.
"""
import re
import subprocess
import sys

DATE = re.compile(r"\d{4}-\d{2}-\d{2}$")


def git(*a: str) -> str:
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit(r.stderr.strip() or f"git {' '.join(a)} failed")
    return r.stdout


def commit_on(day: str, path: str) -> str:
    """The newest commit touching path whose In-force is on or before day."""
    out = git("log", "--first-parent", "--no-merges", "--format=%H %(trailers:key=In-force,valueonly,separator=)", "main", "--", path)
    for line in out.splitlines():
        sha, _, inf = line.partition(" ")
        inf = inf.strip()
        if inf and inf <= day:
            return sha
    return ""


def show(day: str, path: str) -> int:
    path = path.rstrip("/")
    sha = commit_on(day, path)
    if not sha:
        print(f"{path}: nothing in force on {day} in this record", file=sys.stderr)
        return 1
    kind = git("cat-file", "-t", f"{sha}:{path}").strip()
    if kind == "blob":
        sys.stdout.write(git("show", f"{sha}:{path}"))
        return 0
    names = [l.split("\t", 1)[1] for l in git("ls-tree", sha, path + "/").splitlines()]
    if f"{path}/README.md" in names:
        # A norm: its blocks in the BOE's order, as listed in its README on that day.
        readme = git("show", f"{sha}:{path}/README.md")
        sys.stdout.write(readme.split("## Bloques")[0].rstrip() + "\n")
        for f in re.findall(r"\]\(([^)]+\.md)\)$", readme, re.M):
            sys.stdout.write(f"\n<!-- {f} -->\n" + git("show", f"{sha}:{path}/{f}"))
        return 0
    sys.stdout.write(git("ls-tree", sha, path + "/"))
    return 0


def log(path: str) -> int:
    out = git("log", "--first-parent", "--format=%(trailers:key=In-force,valueonly,separator=)%x09%an", "main", "--", path)
    sys.stdout.write("\n".join(l for l in out.splitlines() if l.split("\t")[0]) + "\n")
    return 0


def main(argv) -> int:
    if len(argv) >= 3 and argv[0] == "on" and DATE.match(argv[1]):
        return show(argv[1], argv[2])
    if len(argv) >= 2 and DATE.match(argv[0]):
        return show(argv[0], argv[1])
    if len(argv) >= 2 and argv[0] == "log":
        return log(argv[1])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
