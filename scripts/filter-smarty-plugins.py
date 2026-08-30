#!/usr/bin/env python3
"""公開ドキュメントに載っていない Smarty プラグインを server-processing/references から除く。

generate_docs.php は nfs/lib/smarty/plugins 配下を再帰的に読むため、管理画面専用・内部用の
プラグインも references に混ざる。ドキュメントサイトに一度も現れない名前は利用者が使えない
前提なので、生成後にこのスクリプトで落とす。

usage:
  scripts/filter-smarty-plugins.py                      # scripts/smarty-public-plugins.txt を使う
  scripts/filter-smarty-plugins.py --docs-repo PATH     # ドキュメントサイトから許可リストを再計算して保存
"""
import argparse, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REFS = os.path.join(REPO, 'skills/server-processing/references')
ALLOW_FILE = os.path.join(HERE, 'smarty-public-plugins.txt')
MANUAL_MARKER = '# --- manual: ドキュメント未整備でも公開扱いと判断したもの。--docs-repo で再計算しても残す ---'
CATEGORY_FILES = ['api-plugins.md', 'string-plugins.md', 'array-plugins.md', 'form-plugins.md',
                  'auth-plugins.md', 'integration-plugins.md', 'file-plugins.md', 'vue-plugins.md']


def docs_text(docs_repo):
    parts = []
    for pattern in ('docs/**/*.md*', 'i18n/ja/docusaurus-plugin-content-docs/current/**/*.md*'):
        for p in glob.glob(os.path.join(docs_repo, pattern), recursive=True):
            if '/information/' in p or '/update/' in p:
                continue
            with open(p, encoding='utf-8', errors='ignore') as f:
                parts.append(f.read())
    return "\n".join(parts)


def documented(name, docs):
    n = re.escape(name)
    if re.search(r'^## +' + n + r'\s*$', docs, flags=re.M):
        return True
    if re.search(r'\{' + n + r'[\s}]', docs) or re.search(r'\|@?' + n + r'(?=[:}|\s])', docs):
        return True
    if re.search(r'`' + n + r'`', docs):
        return True
    return '_' in name and re.search(r'\b' + n + r'\b', docs) is not None


def generated_names():
    with open(os.path.join(REFS, 'all-plugins.md'), encoding='utf-8') as f:
        return sorted(set(re.findall(r'^\| ([A-Za-z_0-9]+) \|', f.read(), flags=re.M)))


def manual_section():
    if not os.path.exists(ALLOW_FILE):
        return []
    with open(ALLOW_FILE, encoding='utf-8') as f:
        lines = f.read().split('\n')
    if MANUAL_MARKER not in lines:
        return []
    return [l.strip() for l in lines[lines.index(MANUAL_MARKER) + 1:] if l.strip() and not l.startswith('#')]


def load_allow():
    with open(ALLOW_FILE, encoding='utf-8') as f:
        return {l.strip() for l in f if l.strip() and not l.startswith('#')}


def filter_file(path, allow):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    # 目次・索引の行
    lines = [l for l in text.split('\n')
             if not (re.match(r'^- \[([A-Za-z_0-9]+)\]\(#', l) and re.match(r'^- \[([A-Za-z_0-9]+)\]\(#', l).group(1) not in allow)
             and not (re.match(r'^\| ([A-Za-z_0-9]+) \|', l) and re.match(r'^\| ([A-Za-z_0-9]+) \|', l).group(1) not in allow)]
    text = '\n'.join(lines)
    # 本文セクション: "## name" から次の "## " または末尾まで（直前の --- 区切りも一緒に）
    out, skip = [], False
    for block in re.split(r'(?=^## )', text, flags=re.M):
        m = re.match(r'^## ([A-Za-z_0-9]+)\s*$', block.split('\n', 1)[0])
        if m and m.group(1) not in allow:
            continue
        out.append(block)
    text = ''.join(out)
    text = re.sub(r'(\n---\n\s*)+(?=\n---\n|\Z)', '\n', text)  # 連続した区切りを潰す
    text = re.sub(r'\n{3,}', '\n\n', text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--docs-repo', help='front_kuroco_document_site のパス。指定すると許可リストを再計算して保存する')
    args = ap.parse_args()
    names = generated_names()
    if args.docs_repo:
        docs = docs_text(args.docs_repo)
        allow = sorted(n for n in names if documented(n, docs))
        manual = manual_section()
        with open(ALLOW_FILE, 'w', encoding='utf-8') as f:
            f.write('# ドキュメントサイトに現れる Smarty プラグイン名（scripts/filter-smarty-plugins.py --docs-repo で再生成）\n')
            f.write('\n'.join(allow) + '\n')
            f.write(MANUAL_MARKER + '\n' + '\n'.join(manual) + ('\n' if manual else ''))
        print(f'allowlist saved: {len(allow)} documented + {len(manual)} manual -> {ALLOW_FILE}')
    allow = load_allow()
    dropped = [n for n in names if n not in allow]
    for fn in CATEGORY_FILES + ['all-plugins.md']:
        filter_file(os.path.join(REFS, fn), allow)
    kept = [n for n in names if n in allow]
    p = os.path.join(REFS, 'all-plugins.md')
    with open(p, encoding='utf-8') as f:
        t = f.read()
    t = re.sub(r'全\d+個', f'全{len(kept)}個', t)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f'kept {len(kept)} / dropped {len(dropped)}: {" ".join(dropped)}')


if __name__ == '__main__':
    main()
