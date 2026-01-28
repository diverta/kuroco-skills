---
name: sync-docs
description: Kurocoドキュメントをダウンロードしてdocs/フォルダに全展開します。1ヶ月以上更新していない場合や、docs/フォルダが空の場合に実行してください。
---

# Kurocoドキュメント同期コマンド

Kuroco公式ドキュメントをZIPファイルからダウンロードし、`docs/` フォルダに展開します。
Claude CodeのGrepやReadツールで横断検索が可能になります。

## いつ実行するか

- `docs/` フォルダが空または存在しない場合
- `.last_sync` ファイルの日時が1ヶ月以上前の場合
- ドキュメントが更新された可能性がある場合

## ダウンロード元

```
https://rcms.g.kuroco-img.app/files/user/skills/current.zip
```

## 実行方法

```bash
bash ${CLAUDE_PLUGIN_ROOT}/scripts/sync-docs.sh
```

## 処理内容

1. ZIPファイルをダウンロード（リトライ機能付き）
2. ZIPファイルの検証
3. `docs/` フォルダをクリア
4. ドキュメントを展開
5. `INDEX.md` を自動生成（目的別リファレンス、ディレクトリ構造、ファイル一覧）
6. `.last_sync` に同期日時を記録

## 展開先

```
docs/
├── INDEX.md            # 自動生成されるインデックス
├── .last_sync          # 同期日時（Unixタイムスタンプ）
├── tutorials/          # チュートリアル（実装手順、サンプルコード）
├── reference/          # リファレンス（API設定、Smartyプラグイン）
├── management/         # 管理画面ガイド
├── faq/                # FAQ
├── about/              # Kurocoについて
├── troubleshooting/    # トラブルシューティング
├── update/             # アップデート情報
└── information/        # お知らせ
```

## 同期後の確認

```bash
# ファイル数を確認
find docs/ -name "*.md" | wc -l

# INDEX.mdを確認
cat docs/INDEX.md

# 同期日時を確認
cat docs/.last_sync
```

## 検索方法

### Claude Codeツール（推奨）

```
# キーワードで検索
Grep: pattern="エンドポイント" path="docs/"

# ファイル一覧
Glob: pattern="**/*.md" path="docs/"
```

### Bash

```bash
# キーワードで全文検索
grep -rl 'エンドポイント' docs/

# ファイル名のみ表示
grep -rl 'login' docs/

# 特定ディレクトリ内を検索
grep -r 'CORS' docs/tutorials/

# 大文字小文字を区別しない
grep -ri 'api' docs/reference/
```

## 使い方

1. `/sync-docs` または上記コマンドでドキュメントを同期
2. `docs/INDEX.md` で目的のファイルを探す
3. GrepまたはGlobでキーワード検索
4. Readツールで該当ファイルを読む

## トラブルシューティング

### ダウンロードに失敗する場合

- インターネット接続を確認
- ZIPファイルのURLが有効か確認
- プロキシ設定を確認

### ZIPが解凍できない場合

- ファイルが破損している可能性あり
- 再度ダウンロードを試行

## 更新頻度

- **推奨**: 1ヶ月に1回
- **自動チェック**: 各Skillが `.last_sync` を確認し、1ヶ月以上経過している場合は再同期を促します
