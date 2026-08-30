#!/usr/bin/env python3
"""スキル自動発動（トリガー）テストランナー。

skills/ 配下の各スキルを一時プロジェクトにインストールし、cases.json の
各質問をヘッドレスの `claude -p` で実行して、期待したスキルが自動発動
するかを検証する。詳細は README.md を参照。

usage:
  python3 run_tests.py                 # 全ケース実行
  python3 run_tests.py --only a19 c03  # 指定ケースのみ
  python3 run_tests.py --resume        # 前回の結果を残して未実行分のみ
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
WORK_DIR = os.path.join(HERE, ".work")
RESULTS_DIR = os.path.join(WORK_DIR, "results")

PARALLEL = 8
TIMEOUT_SEC = 300
MAX_TURNS = "2"

GROUP_NAMES = {
    "a": "api-content",
    "b": "app-builder",
    "s": "server-processing",
    "f": "frontend-integration",
    "d": "kuroco-docs",
    "m": "admin-mcp",
    "t": "content-structure（作成）",
    "c": "content-structure（設計）",
    "u": "auth-design",
    "e": "server-processing（外部連携設計）",
    "g": "security-audit",
    "p": "api-performance-review",
    "n": "対照（発動なし）",
}


def setup_workdir():
    """一時プロジェクトに全スキルをインストール（kuroco-docsの同梱docsは
    発動判定に不要かつ大きいため除外）。"""
    skills_dest = os.path.join(WORK_DIR, ".claude", "skills")
    shutil.rmtree(skills_dest, ignore_errors=True)
    os.makedirs(skills_dest)
    for name in sorted(os.listdir(SKILLS_DIR)):
        src = os.path.join(SKILLS_DIR, name)
        if not os.path.isdir(src):
            continue
        shutil.copytree(
            src,
            os.path.join(skills_dest, name),
            ignore=shutil.ignore_patterns("docs"),
        )


def run_case(case):
    out = os.path.join(RESULTS_DIR, f"{case['id']}.jsonl")
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return case["id"], "skipped"
    cmd = [
        "claude", "-p", case["prompt"],
        "--output-format", "stream-json", "--verbose",
        "--max-turns", MAX_TURNS,
        "--allowedTools", "Skill",
    ]
    with open(out, "w") as fo, open(out.replace(".jsonl", ".err"), "w") as fe:
        try:
            subprocess.run(cmd, stdout=fo, stderr=fe, cwd=WORK_DIR, timeout=TIMEOUT_SEC)
            return case["id"], "done"
        except subprocess.TimeoutExpired:
            return case["id"], "TIMEOUT"


def invoked_skills(case_id):
    """stream-jsonの出力からSkillツール呼び出しを抽出する。"""
    path = os.path.join(RESULTS_DIR, f"{case_id}.jsonl")
    skills = []
    if not os.path.exists(path):
        return skills
    for line in open(path):
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = ev.get("message")
        if not isinstance(msg, dict):
            # system/permission_denied などは message が文字列で来る
            continue
        for block in (msg.get("content") or []):
            if (
                isinstance(block, dict)
                and block.get("type") == "tool_use"
                and block.get("name") == "Skill"
            ):
                skills.append(block.get("input", {}).get("skill"))
    return skills


def normalize(skill):
    """`kuroco-skills:app-builder` のようなプラグイン名前空間付きの呼び出しを
    ディレクトリ名だけに揃える。テスト用プロジェクトにコピーしたスキルと、
    実行環境に導入済みのプラグイン版が同名で並ぶため、どちらで発動しても
    同じスキルとして扱う。"""
    return skill.rsplit(":", 1)[-1] if skill else skill


def report(cases):
    fails = []
    stats = defaultdict(lambda: [0, 0])
    for c in cases:
        skills = invoked_skills(c["id"])
        got = skills[0] if skills else None
        want = c["expect"]
        ok = (normalize(got) in {normalize(w) for w in want}) if want else (got is None)
        group = c["id"][0]
        stats[group][0] += ok
        stats[group][1] += 1
        if not ok:
            fails.append((c["id"], c["prompt"], want, got))

    total_ok = sum(v[0] for v in stats.values())
    total = sum(v[1] for v in stats.values())
    print(f"\n== 合計: {total_ok}/{total} ==")
    for g in GROUP_NAMES:
        if stats[g][1]:
            print(f"  {GROUP_NAMES[g]}: {stats[g][0]}/{stats[g][1]}")
    for g in sorted(set(stats) - set(GROUP_NAMES)):
        if stats[g][1]:
            print(f"  {g}*: {stats[g][0]}/{stats[g][1]}")
    for cid, prompt, want, got in fails:
        print(f"\n❌ [{cid}]「{prompt}」")
        print(f"    期待: {' or '.join(want) if want else '発動なし'} / 実際: {got or '発動なし'}")
    return not fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None, help="実行するケースID")
    ap.add_argument("--resume", action="store_true", help="既存の結果を残して未実行分のみ実行")
    args = ap.parse_args()

    cases = json.load(open(os.path.join(HERE, "cases.json")))
    if args.only:
        cases = [c for c in cases if c["id"] in set(args.only)]
    if not cases:
        sys.exit("対象ケースがありません")

    if not args.resume:
        shutil.rmtree(RESULTS_DIR, ignore_errors=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)
    setup_workdir()

    print(f"{len(cases)}ケースを{PARALLEL}並列で実行します（1ケースあたり30秒〜1分）")
    done = 0
    with ThreadPoolExecutor(max_workers=PARALLEL) as pool:
        futures = [pool.submit(run_case, c) for c in cases]
        for f in as_completed(futures):
            cid, status = f.result()
            done += 1
            print(f"[{done}/{len(cases)}] {cid}: {status}", flush=True)

    sys.exit(0 if report(cases) else 1)


main()
