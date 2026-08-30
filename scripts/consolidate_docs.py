#!/usr/bin/env python3
"""kuroco-docs 同梱ドキュメントの統合(consolidate)スクリプト。

1ページ1ファイルの公式ドキュメントミラー(md/mdx)を、カテゴリ単位の
統合Markdownファイルに変換する。claude.ai のカスタムスキル上限
(zip 200ファイル)に収めつつ、Grepベースの検索性を維持するのが目的。

変換ルール:
- faq/          … frontmatter の subcategory ごとに `faq-<sub>.md` へ統合
- management/   … frontmatter の category (日本語) を CATEGORY_MAP で
                  スラッグ化し `management-<slug>.md` へ統合
- tutorials/    … ファイル名(slug)への正規表現ルール TUTORIAL_RULES で
                  テーマ分類し `tutorials-<theme>.md` へ統合
- reference/    … 同様に REFERENCE_RULES で `reference-<theme>.md` へ統合
- about/, troubleshooting/ … ディレクトリ全体を1ファイルへ統合
- information/, update/    … 時限性情報(お知らせ・リリースノート)のため除外
- PDF等のバイナリ、INDEX.md … 除外

統合ファイルが MAX_PART_BYTES を超える場合は `-1`, `-2` … に分割する。
各ページは `# タイトル` 見出し + 元ファイルパス + 公式URL付きで収録され、
ファイル冒頭に収録ページの目次が入る。INDEX.md も自動生成する。

再現手順(ドキュメント再同期時):
  1. 公式ドキュメントの1ページ1ファイル形式のソース一式を用意する
     (旧形式は本リポジトリのgit履歴 skills/kuroco-docs/docs/ にもある)
  2. python3 scripts/consolidate_docs.py \
       --source <raw-docs-dir> --output skills/kuroco-docs/docs --force \
       --map /tmp/docs-map.json
  3. 出力されたマッピング(--map)で他スキルからの参照パスを更新する

usage:
  python3 scripts/consolidate_docs.py --source <dir> --output <dir> [--force] [--map <file>]
"""
import argparse
import json
import os
import re
import shutil
import sys
from collections import defaultdict

MAX_PART_BYTES = 128 * 1024  # 1統合ファイルの目安上限(超えたら分割)
MIN_PAGES = 3                # これ未満の小グループは misc に併合

OFFICIAL_BASE = "https://kuroco.app/ja/docs"

SKIP_DIRS = {"information", "update"}
MERGE_WHOLE_DIRS = {"about", "troubleshooting"}

# management/ の frontmatter category(日本語) → ファイル名スラッグ
CATEGORY_MAP = {
    "EC": "ec",
    "オペレーション": "operation",
    "キャンペーン": "campaign",
    "メンバー管理": "member",
    "アカウント設定": "account",
    "外部システム連携": "integration",
    "コンテンツ": "content",
    "コンテンツ定義": "content",
    "API": "api",
    "環境設定": "settings",
    "Activity": "activity",
    "AI": "ai",
    "AI辞書": "ai",
    "ファイルマネージャー": "file",
    "KurocoFront": "kurocofront",
    "検索": "search",
    "WYSIWYG専用テンプレート": "wysiwyg",
}

# tutorials/ のslug分類ルール(上から順に最初にマッチしたテーマ)
TUTORIAL_RULES = [
    ("auth-member", r"login|signup|sso|saml|scim|two-step|password|passkey|"
                    r"one-time|auth0|azure-ad|oauth|member|regist|group"),
    ("ec", r"^ec-|stripe|paygent|purchase"),
    ("ai-mcp", r"\bai\b|^ai-|-ai-|mcp|kurocorag|deepl|translation|vector-search|"
               r"openai|claude|bedrock|kuroco-skills|kuroco-ai"),
    ("admin-customize", r"admin-panel|management-screen|dashboard|content-edit"),
    ("form-mail", r"form|inquiry|notif|slack|chatwork|email|mail|magazine|"
                  r"sendgrid|blastengine|mailchimp|recaptcha"),
    ("frontend", r"nuxt|next|front|ssg|preview|sample-site|figma|core-web-vitals|"
                 r"performance|multi-language|domain|kurocofiles"),
    ("content", r"topics|content|csv|bulk-upload|wordpress|wysiwyg|ckeditor|"
                r"workflow|category|master|json-field|comment|search|crawler|"
                r"thumb|pdf|scheduling"),
    ("integration", r"github|firebase|instagram|\bline\b|-line$|twillio|twilio|"
                    r"vimeo|google|analytics|teams|s3|vaddy|postman|twitter|"
                    r"openweathermap|har-file"),
    ("api-custom", r"api|endpoint|function|batch|smarty|statictoken|swagger|cache"),
]

# reference/ のslug分類ルール
REFERENCE_RULES = [
    ("smarty-trigger", r"smarty|trigger|variables|constant|pre-processing|"
                       r"post-processing|mail-variables|batch"),
    ("mcp-ai", r"mcp|oauth|kuroco-skills"),
    ("ec", r"^ec-"),
    ("api", r"api|endpoint|filter|cache|error|swagger|auto-login"),
    ("content", r"content|column|wysiwyg|search|json|object|secondary-language|"
                r"order-by|form-field"),
    ("file", r"file|gcs|backup"),
]

# INDEX.md 表示用の日本語ラベル
GROUP_LABELS = {
    "auth-member": "認証・会員",
    "ec": "EC・決済",
    "ai-mcp": "AI・MCP",
    "admin-customize": "管理画面カスタマイズ",
    "form-mail": "フォーム・メール通知",
    "frontend": "フロントエンド・KurocoFront",
    "content": "コンテンツ管理",
    "integration": "外部サービス連携",
    "api-custom": "API・カスタム処理",
    "smarty-trigger": "Smarty・トリガー・バッチ",
    "mcp-ai": "MCP・AI",
    "api": "API",
    "file": "ファイル",
    "operation": "オペレーション",
    "campaign": "キャンペーン",
    "member": "メンバー管理",
    "account": "アカウント設定",
    "settings": "環境設定",
    "activity": "Activity",
    "ai": "AI",
    "kurocofront": "KurocoFront",
    "search": "検索",
    "wysiwyg": "WYSIWYG",
    "misc": "その他",
}

DIR_LABELS = {
    "tutorials": "チュートリアル",
    "management": "管理画面",
    "reference": "リファレンス",
    "faq": "FAQ",
    "about": "Kurocoについて",
    "troubleshooting": "トラブルシューティング",
}


def parse_frontmatter(text):
    """frontmatter(dict)と本文を返す。値は1行のみ対応の簡易パーサ。"""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return fm, text[m.end():]


def strip_mdx(body):
    """コードフェンス外の MDX 構文(import文・JSXコンポーネント)を除去する。

    - `import ... from '@site/...'` / '@theme/...' の行を削除
    - <StructuredDataFaqs .../> ブロックを削除(frontmatterと重複のため)
    - <Tabs>/<TabItem label="X"> は `**X:**` の見出し行に変換
    """
    out = []
    in_fence = False
    skip_until_close = None  # 'selfclose' → '/>' まで、'gt' → '>' まで読み飛ばし
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if skip_until_close:
            if (skip_until_close == "selfclose" and stripped.endswith("/>")) or \
               (skip_until_close == "gt" and stripped.endswith(">")):
                skip_until_close = None
            continue
        if re.match(r"^import\s.+from\s+['\"]@(site|theme)/", stripped):
            continue
        if stripped.startswith("<StructuredDataFaqs"):
            if not stripped.endswith("/>"):
                skip_until_close = "selfclose"
            continue
        if stripped.startswith("<Tabs"):
            if not stripped.endswith(">"):
                skip_until_close = "gt"
            continue
        if stripped in ("</Tabs>", "</TabItem>"):
            continue
        m = re.match(r"^<TabItem\b([^>]*)>?", stripped)
        if m:
            label = re.search(r'label="([^"]+)"', m.group(1)) or \
                    re.search(r'value="([^"]+)"', m.group(1))
            out.append(f"**{label.group(1)}:**" if label else "")
            if not stripped.endswith(">"):
                skip_until_close = "gt"
            continue
        out.append(line)
    # 3行以上の連続空行を圧縮
    text = "\n".join(out)
    return re.sub(r"\n{4,}", "\n\n\n", text).strip() + "\n"


def classify(dirname, slug, fm):
    """ページの所属グループ(ファイル名スラッグ)を決める。"""
    if dirname in MERGE_WHOLE_DIRS:
        return None  # ディレクトリ全体で1ファイル
    if dirname == "faq":
        return fm.get("subcategory") or fm.get("category") or "other"
    if dirname == "management":
        cat = fm.get("category", "")
        if cat in CATEGORY_MAP:
            return CATEGORY_MAP[cat]
        if cat:
            print(f"  [warn] management: 未知のcategory {cat!r} ({slug}) → misc",
                  file=sys.stderr)
        return "misc"
    rules = TUTORIAL_RULES if dirname == "tutorials" else REFERENCE_RULES
    for theme, pattern in rules:
        if re.search(pattern, slug):
            return theme
    return "misc"


def render_page(dirname, slug, fm, body):
    title = fm.get("title") or slug
    desc = fm.get("description", "")
    lines = [f"# {title}", ""]
    src = f"`{dirname}/{slug}` ｜ 公式ページ: {OFFICIAL_BASE}/{dirname}/{slug}/"
    lines.append(f"> 元ページ: {src}")
    if desc:
        lines.append(f"> 概要: {desc}")
    lines.append("")
    lines.append(strip_mdx(body))
    return title, "\n".join(lines)


def pack_parts(pages, base_name, label):
    """ページ列をサイズ上限で分割し [(filename, content)] を返す。"""
    parts = []
    cur, cur_size = [], 0
    for page in pages:
        size = len(page["text"].encode("utf-8"))
        if cur and cur_size + size > MAX_PART_BYTES:
            parts.append(cur)
            cur, cur_size = [], 0
        cur.append(page)
        cur_size += size
    if cur:
        parts.append(cur)

    results = []
    for i, part in enumerate(parts, 1):
        fname = f"{base_name}.md" if len(parts) == 1 else f"{base_name}-{i}.md"
        suffix = f"（{i}/{len(parts)}）" if len(parts) > 1 else ""
        header = [f"# Kurocoドキュメント: {label}{suffix}", ""]
        header.append("収録ページ一覧。目的のページは Grep でタイトルまたは "
                      "slug を検索し、該当行から Read してください。")
        header.append("")
        header.append("## 収録ページ")
        header.append("")
        for page in part:
            header.append(f"- {page['title']}（`{page['slug']}`）")
        header.append("")
        body = "\n\n---\n\n".join(p["text"] for p in part)
        results.append((fname, "\n".join(header) + "\n\n---\n\n" + body, part))
    return results


def build_index(entries):
    lines = [
        "# Kurocoドキュメント インデックス",
        "",
        "公式ドキュメントをカテゴリ単位の統合ファイルとして収録しています。",
        "各ファイルの冒頭に収録ページの目次があります。",
        "キーワード検索には Grep（`pattern=\"キーワード\" path=docs/`）を使い、",
        "ヒットした行番号から Read（offset指定）で該当セクションを読んでください。",
        "",
        "| ファイル | 分類 | 収録ページ数 |",
        "|----------|------|-------------|",
    ]
    for fname, label, count in entries:
        lines.append(f"| `{fname}` | {label} | {count} |")
    lines += [
        "",
        "情報の鮮度が重要なもの（お知らせ・リリースノート）は同梱していません。",
        "公式サイト https://kuroco.app/ja/docs/ を参照してください。",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--source", required=True, help="1ページ1ファイル形式のdocsディレクトリ")
    ap.add_argument("--output", required=True, help="統合ファイルの出力先")
    ap.add_argument("--force", action="store_true", help="出力先を削除して作り直す")
    ap.add_argument("--map", help="旧パス→新ファイルのマッピングJSONの出力先")
    args = ap.parse_args()

    if os.path.exists(args.output) and os.listdir(args.output):
        if not args.force:
            ap.error(f"{args.output} は空ではありません。--force で上書きしてください")
        shutil.rmtree(args.output)
    os.makedirs(args.output, exist_ok=True)

    groups = defaultdict(list)  # (dirname, group) -> [page]
    path_map = {}
    skipped = []

    for dirname in sorted(os.listdir(args.source)):
        src_dir = os.path.join(args.source, dirname)
        if not os.path.isdir(src_dir):
            continue
        if dirname in SKIP_DIRS:
            skipped.append(dirname)
            continue
        for fn in sorted(os.listdir(src_dir)):
            if not fn.endswith((".md", ".mdx")):
                continue
            slug = re.sub(r"\.(md|mdx)$", "", fn)
            text = open(os.path.join(src_dir, fn), encoding="utf-8").read()
            fm, body = parse_frontmatter(text)
            group = classify(dirname, slug, fm)
            title, rendered = render_page(dirname, slug, fm, body)
            groups[(dirname, group)].append(
                {"slug": slug, "title": title, "text": rendered,
                 "old": f"{dirname}/{fn}"})

    # 小さすぎるグループは misc へ併合(ディレクトリ全体統合は対象外)
    for (dirname, group) in list(groups.keys()):
        if group in (None, "misc"):
            continue
        if len(groups[(dirname, group)]) < MIN_PAGES:
            groups[(dirname, "misc")].extend(groups.pop((dirname, group)))

    index_entries = []
    total_files = 0
    for (dirname, group), pages in sorted(groups.items(),
                                          key=lambda kv: (kv[0][0], kv[0][1] or "")):
        pages.sort(key=lambda p: p["slug"])
        base = dirname if group is None else f"{dirname}-{group}"
        label = DIR_LABELS.get(dirname, dirname)
        if group is not None:
            label += " / " + GROUP_LABELS.get(group, group)
        for fname, content, part_pages in pack_parts(pages, base, label):
            with open(os.path.join(args.output, fname), "w", encoding="utf-8") as f:
                f.write(content)
            total_files += 1
            index_entries.append((fname, label, len(part_pages)))
            for p in part_pages:
                path_map[p["old"]] = fname
        print(f"{base}: {len(pages)}ページ")

    with open(os.path.join(args.output, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(build_index(index_entries))
    total_files += 1

    if args.map:
        with open(args.map, "w", encoding="utf-8") as f:
            json.dump(path_map, f, ensure_ascii=False, indent=1)

    print(f"\n出力: {total_files}ファイル / 除外ディレクトリ: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
