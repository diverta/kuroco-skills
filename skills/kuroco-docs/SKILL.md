---
name: kuroco-docs
metadata:
  author: Diverta inc.
  version: "2.2.2"
  lastUpdated: "2026-08-27"
description: Kuroco公式ドキュメント（チュートリアル・リファレンス・管理画面ガイド・FAQ）をスキル同梱のファイルから検索・参照する。Kurocoの機能の使い方、設定方法、仕様、トラブルシューティングのほか、「Kurocoに〜という機能・資料はあるか」という有無の確認など、公式ドキュメントに基づく正確な情報が必要なときに使用。
---

# Kurocoドキュメント検索ガイド

このSkillはKuroco公式ドキュメントの検索・参照を支援します。

## ドキュメントの場所と形式

ドキュメントはこのスキルに同梱されています。場所は次のとおり:

この `SKILL.md` と同じディレクトリにある `docs/` を使用します。以下の例では、このスキルのディレクトリを基準にした相対パスとして `docs/` と表記します。クライアント固有の環境変数や、リポジトリ内の固定パスには依存しないでください。

同梱ドキュメントは配布時点のスナップショットです。**記載が古い可能性がある場合や、同梱ドキュメントに該当項目が見つからない場合は、公式サイト（https://kuroco.app/ja/docs/ ）を確認してください。** スキルパッケージを更新すると同梱ドキュメントも最新になります（更新手順は導入方法によって異なるため、リポジトリの README を参照）。

公式ドキュメントの各ページは**カテゴリ単位の統合ファイル**として収録されています。

- 1つの統合ファイルに複数の公式ページが入っており、各ページは `# タイトル` 見出しで始まる
- ページ見出しの直下に元ページのslugと公式サイトURL（`https://kuroco.app/ja/docs/...`）がある
- 各ファイルの冒頭に「収録ページ」の目次がある
- サイズの大きい分類は `-1.md`, `-2.md` のように分割されている（Globで `tutorials-auth-member*.md` のように検索）

## ファイル構成

| ファイル | 内容 |
|---------|------|
| `INDEX.md` | 全ファイルの一覧と収録ページ数 |
| `tutorials-*.md` | チュートリアル（auth-member / frontend / content / api-custom / ai-mcp / ec / form-mail / integration / admin-customize / misc） |
| `reference-*.md` | リファレンス（api / content / smarty-trigger / mcp-ai / file / misc） |
| `management-*.md` | 管理画面ガイド（account / api / campaign / content / ec / integration / member / operation / misc） |
| `faq-*.md` | FAQ（content / frontend / api / api-error / admin / email-form / domain / file / login-session / password / smarty / tls / infrastructure / deploy / member / email / assessment / contracts / other） |
| `about.md` | Kurocoの概要・料金・制限事項・セキュリティ |
| `troubleshooting.md` | トラブルシューティング |

お知らせ・リリースノートは鮮度が重要なため同梱していません。必要な場合は公式サイト（https://kuroco.app/ja/docs/ ）を参照してください。

## 検索方法

### 方法1: Grepでキーワード検索（推奨）

全文検索ツール（Grep 相当）で docs/ 全体を横断検索し、ヒットしたファイルの該当行付近をファイル読み取りツール（Read 相当。開始行を指定できるもの）で読んでください。検索ツールが無い環境では `grep -rn` をシェルで実行しても同じことができます。

```
# キーワードで検索（ファイル特定）
Grep: pattern="エンドポイント" path="docs/"

# 行番号付きで内容を確認 → その行から Read で該当セクションを読む
Grep: pattern="フィルタークエリ" path="docs/" output_mode="content" -n=true

# 元ページのslugがわかっている場合（各ページ見出し直下に slug が記載されている）
Grep: pattern="how-to-use-batch" path="docs/"

# ファイル名で分類を絞る
Grep: pattern="ログイン" path="docs/" glob="tutorials-*.md"
```

統合ファイルは大きいため、**全文Readせず、Grepの行番号 → Read（offset/limit指定）**で必要なセクションのみ読むのが効率的です。ページの区切りは `# ` 見出しです。

### 方法2: INDEX.mdでファイル一覧を確認

```bash
cat docs/INDEX.md
```

どの統合ファイルに何ページ収録されているかの一覧が確認できます。各統合ファイルの冒頭には収録ページの目次（タイトルとslug）があります。

## 目的別クイックリファレンス

| 目的 | 参照先 |
|------|--------|
| API・エンドポイント設定 | `reference-api*.md`（endpoint-settings, filter-query, api-cache）、`tutorials-api-custom*.md`（configure-endpoint） |
| 認証・ログイン・会員登録 | `tutorials-auth-member*.md`（login, signup, 二段階認証, SSO/SAML） |
| フロントエンド統合（Nuxt/Next, SSG） | `tutorials-frontend*.md`（integrate-kuroco-with-nuxt, beginners-guide, corporate-sample-site-to-ssg） |
| コンテンツ管理・CSV一括登録 | `tutorials-content*.md`（adding-a-topics, bulk-upload-in-csv）、`management-content*.md` |
| バッチ処理・トリガー・Smarty | `reference-smarty-trigger*.md`（smarty-plugin, trigger-variables）、`tutorials-api-custom*.md`（how-to-use-batch） |
| 外部サービス連携（Slack/SendGrid/Firebase等） | `tutorials-integration*.md`、`tutorials-form-mail*.md`、`management-integration*.md` |
| EC・決済（Stripe/Paygent） | `tutorials-ec*.md`、`management-ec*.md` |
| MCP・AI機能（Kuroco RAG等） | `tutorials-ai-mcp*.md`、`reference-mcp-ai*.md` |
| エラー・トラブル解決 | `faq-*.md`、`troubleshooting.md`、`reference-api*.md`（error） |
| 料金・制限事項・インフラ | `about.md`、`faq-contracts.md`、`faq-infrastructure.md` |

## 検索のコツ

1. **日本語キーワード**: `エンドポイント`, `ログイン`, `コンテンツ`
2. **英語キーワード**: `Topics`, `Member`, `API`, `CORS`
3. **機能名・slug**: `batch`, `webhook`, `trigger`, `smarty`, `filter-query`
4. **分類を絞る**: `tutorials-*`（実装方法）、`reference-*`（仕様）、`management-*`（管理画面）、`faq-*`（Q&A）
5. **回答に公式URLを添える**: 各ページ見出し直下の「公式ページ」URLを引用する

## ドキュメント更新

ドキュメントはプラグインのアップデートと一緒に更新されます。

```
/plugin marketplace update diverta-kuroco-skills
```

統合ファイルの再生成手順（メンテナ向け）は `scripts/consolidate_docs.py` のdocstringを参照してください。
