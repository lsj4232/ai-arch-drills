"""Deep-ML 로컬 문제 뷰어·채점기.

문제 원본: _external/DML-OpenProblem/questions/<id>_<slug>/
  - description.md / example.json / starter_code.py / tests.json / learn.md

사용법:
  python tools/dml.py list [카테고리]        # 문제 목록 (id, 난이도, 제목)
  python tools/dml.py show <id>             # 문제 설명 + 예시 + 스타터 코드
  python tools/dml.py grade <id> <풀이.py>  # tests.json 전 케이스 채점
  python tools/dml.py learn <id>            # 해설(learn.md) 표시 — 정답 후에만 볼 것
"""
import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "_external" / "DML-OpenProblem" / "questions"


def find_problem(pid: str) -> Path:
    matches = [d for d in QUESTIONS.iterdir() if d.is_dir() and d.name.split("_")[0] == str(pid)]
    if not matches:
        sys.exit(f"문제 {pid} 없음 (questions/ 에서 미발견)")
    return matches[0]


def meta(d: Path) -> dict:
    f = d / "meta.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def cmd_list(category: str | None):
    rows = []
    for d in sorted(QUESTIONS.iterdir(), key=lambda p: int(p.name.split("_")[0]) if p.name.split("_")[0].isdigit() else 9999):
        if not d.is_dir():
            continue
        m = meta(d)
        cat = m.get("category", "?")
        if category and category.lower() not in cat.lower():
            continue
        rows.append((m.get("id", d.name.split("_")[0]), m.get("difficulty", "?"), cat, m.get("title", d.name)))
    for pid, diff, cat, title in rows:
        print(f"{pid:>4}  {diff:<7} {cat:<22} {title}")
    print(f"\n총 {len(rows)}문제")


def cmd_show(pid: str):
    d = find_problem(pid)
    m = meta(d)
    print(f"=== [{m.get('id')}] {m.get('title')} · {m.get('difficulty')} · {m.get('category')} ===\n")
    print((d / "description.md").read_text(encoding="utf-8").strip())
    ex = d / "example.json"
    if ex.exists():
        e = json.loads(ex.read_text(encoding="utf-8"))
        print(f"\n--- 예시 ---\ninput:    {e.get('input')}\noutput:   {e.get('output')}")
        if e.get("reasoning"):
            print(f"reasoning: {e['reasoning']}")
    sc = d / "starter_code.py"
    if sc.exists():
        print(f"\n--- 스타터 코드 ---\n{sc.read_text(encoding='utf-8').strip()}")


def cmd_grade(pid: str, solution_file: str):
    d = find_problem(pid)
    tests = json.loads((d / "tests.json").read_text(encoding="utf-8"))
    code = Path(solution_file).read_text(encoding="utf-8")
    ns: dict = {}
    exec(code, ns)  # 풀이 로드

    passed = 0
    for i, t in enumerate(tests, 1):
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                exec(t["test"], ns)
            got = buf.getvalue().strip()
        except Exception as e:
            got = f"<예외: {type(e).__name__}: {e}>"
        want = t["expected_output"].strip()
        ok = got == want
        passed += ok
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] case {i}: {t['test']}")
        if not ok:
            print(f"       expected: {want}\n       got:      {got}")
    print(f"\n{passed}/{len(tests)} 통과" + ("  🎉 정답!" if passed == len(tests) else ""))
    sys.exit(0 if passed == len(tests) else 1)


def cmd_learn(pid: str):
    d = find_problem(pid)
    f = d / "learn.md"
    print(f.read_text(encoding="utf-8") if f.exists() else "learn.md 없음")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
    elif args[0] == "list":
        cmd_list(args[1] if len(args) > 1 else None)
    elif args[0] == "show":
        cmd_show(args[1])
    elif args[0] == "grade":
        cmd_grade(args[1], args[2])
    elif args[0] == "learn":
        cmd_learn(args[1])
    else:
        print(__doc__)
