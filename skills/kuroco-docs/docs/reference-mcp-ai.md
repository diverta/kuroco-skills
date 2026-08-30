# Kurocoドキュメント: リファレンス / MCP・AI

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Kuroco Skills リファレンス（`kuroco-skills-detail`）
- MCP クライアント設定リファレンス（`mcp-client-configuration`）
- 認証ヘッダーによる MCP クライアント設定リファレンス（`mcp-client-configuration-authentication-header`）
- MCP サーバ リファレンス（`mcp-server`）
- OAuth Authorization ServerのOpenID Connect対応（`oauth-authorization-server-openid-connect`）


---

# Kuroco Skills リファレンス

> 元ページ: `reference/kuroco-skills-detail` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/kuroco-skills-detail/
> 概要: Kuroco Skills に含まれる 11 個のスキルそれぞれの機能、対応するキーワード、提供される情報について詳しく説明します。

このページでは、[Kuroco Skills](/ja/docs/tutorials/kuroco-skills-overview/) に含まれる 11 個のスキルについて詳しく説明します。

## kuroco-docs - ドキュメント検索

Kuroco 公式ドキュメントの検索・参照を支援するスキルです。

### 機能

- パッケージに同梱された公式ドキュメントの横断検索
- 目的別クイックリファレンス（API、認証、フロントエンド、コンテンツ管理など）

### 使用例

```
「Kuroco のエンドポイント設定方法を知りたい」
「ログイン API の仕様を調べたい」
「フィルタークエリの書き方を教えて」
```

### 同梱ドキュメントの構成

公式ドキュメントの各ページは、カテゴリ単位の統合ファイルとして収録されています。1 つの統合ファイルに複数の公式ページが含まれ、各ページの見出し直下に元ページの slug と公式サイト URL が記載されています。

| ファイル | 内容 |
|---------|------|
| `INDEX.md` | 全ファイルの一覧と収録ページ数 |
| `tutorials-*.md` | チュートリアル（auth-member / frontend / content / api-custom / ai-mcp / ec / form-mail / integration / admin-customize / misc） |
| `reference-*.md` | リファレンス（api / content / smarty-trigger / mcp-ai / file / misc） |
| `management-*.md` | 管理画面ガイド（account / api / campaign / content / ec / integration / member / operation / misc） |
| `faq-*.md` | FAQ（content / frontend / api / api-error / admin / email-form / domain / file / login-session / password / smarty / tls / infrastructure / deploy / member / email / assessment / contracts / other） |
| `about.md` | Kuroco の概要、料金、制限事項、セキュリティ |
| `troubleshooting.md` | トラブルシューティング |

:::note
お知らせ・リリースノートは鮮度が重要なため同梱されていません。これらは公式サイト（https://kuroco.app/ja/docs/ ）を参照してください。
:::

---

## kuroco-app-builder - アプリ・サイトの構築ワークフロー

Kuroco で Web アプリ・サイトをゼロから構築する手順全体をオーケストレーションするスキルです。個別機能の実装は各専門スキルに委譲し、進め方（フェーズ設計）と橋渡しを担当します。

### 機能

- フロントエンド先行（モックファースト）の構築フロー
- 機能 → Kuroco 機能のマッピング表（コンテンツ定義、カテゴリ、メンバー、フォーム、お気に入り、コメント、EC など）
- 認証方式の決定基準（認証なし / Cookie 認証 / 動的アクセストークン / 静的アクセストークン）
- Admin MCP のスコープ事前確認（`whoami`）と、着手可否の判断
- モックデータを Kuroco API のレスポンス形（`{ list, pageInfo }` / `{ details }`）で作る契約と、実 API への差し替えパターン
- 進行チェックリストとアンチパターン集

### 使用例

```
「Kuroco でアプリを丸ごと作りたい」
「サイトを新規で構築して」
「ブログサイトを作りたい。まず動く画面を見せて」
「会員サイトをゼロから構築して」
```

### 対応するキーワード

`アプリ構築` `サイト構築` `プロトタイプ` `モックファースト` `フロントエンド先行` `コンテンツ定義` `TopicsGroup` `エンドポイント作成` `KurocoFront デプロイ` `whoami` `mcp:tools.all`

### 構築フェーズ

| フェーズ | 内容 |
|---------|------|
| フェーズ 0 | 要件ヒアリング、機能 → Kuroco 機能マッピング、認証方式の決定、Admin MCP のスコープ確認 |
| フェーズ 1 | モックデータでのフロントエンド構築と画面確定 |
| フェーズ 2 | コンテンツ定義・カテゴリ・サンプルデータの作成（Admin MCP） |
| フェーズ 3 | エンドポイント作成とセキュリティ設定 |
| フェーズ 4 | 実データ接続、認証・フォーム接続、デプロイ |

:::note
データモデルが確定している場合や画面が定型の場合は、バックエンド先行（フェーズ 2 → 3 → 1 → 4）に切り替えることもできます。
:::

---

## kuroco-api-content - API 連携 & コンテンツ管理

Kuroco API の設計・実装およびコンテンツ管理（CRUD 操作）に関するベストプラクティスを提供するスキルです。
旧 `kuroco-api-integration` と `kuroco-content-management` を統合したスキルです。

### 機能

**API 連携:**
- エンドポイント設計パターン（URL 構造、主要モデル、オペレーション）
- 認証方式（なし / 静的アクセストークン / 動的アクセストークン / Cookie）
- CORS 設定、キャッシュ戦略、流量制限
- エラーハンドリングパターン（401 / 403 / 429）

**コンテンツ管理:**
- コンテンツ構造（Topics / TopicsGroup / TopicsCategory）
- 拡張項目（カスタムフィールド）の設定・利用方法
- Topics API のオペレーション（list / details / insert / update / delete / bulk_upsert）
- フィルタークエリの構文と使い方、ページネーション
- 多言語対応（`langs_open_flg`）
- ファイルアップロード、CSV インポート/エクスポート
- EC ポイントの操作（ECPoint）

### 使用例

```
「Kuroco の API でログインを実装したい」
「トークン認証の使い方を教えて」
「CORS のエラーが出る。設定方法は？」
「Kuroco でコンテンツ定義を作りたい」
「記事の一覧を API で取得したい」
「フィルターで特定カテゴリの記事だけ取得したい」
```

### 対応するキーワード

`Kuroco API` `エンドポイント設定` `認証` `CORS` `Cookie認証` `動的アクセストークン` `静的アクセストークン` `JWT` `流量制限` `credentials include` `401エラー` `403エラー` `429エラー` `pageInfo` `ページネーション` `langs_open_flg` `コンテンツ定義` `Topics` `カテゴリ` `WYSIWYG` `ファイルアップロード` `CSVインポート` `ext_col` `filter` `order_query` `bulk_upsert` `topics_flg` `拡張項目` `ECPoint`

### 主な認証方式の比較

| 認証方式 | 推奨ユースケース | 特徴 |
|---------|----------------|------|
| なし | 開発・テスト用（本番非推奨） | ヘッダー不要 |
| 静的アクセストークン | サーバー間通信、公開 API | 固定トークンを `X-RCMS-API-ACCESS-TOKEN` ヘッダーに付与 |
| 動的アクセストークン | ログイン必須サイト（JWT） | ログインで取得したトークンを `X-RCMS-API-ACCESS-TOKEN` ヘッダーに付与 |
| Cookie | ログイン必須の Web サイト | セッションベース。`credentials: 'include'` が必須 |

### フィルタークエリの基本構文

| 演算子 | 例 |
|--------|-----|
| `=`, `!=` | `filter=category_id = 1` |
| `>`, `>=`, `<`, `<=` | `filter=ymd >= "2024-01-01"` |
| `contains`, `ncontains` | `filter=subject contains "キーワード"` |
| `in`, `nin` | `filter=category_id in [1, 2, 3]` |

:::note
文字列の値は二重引用符で囲みます。シングルクォートは引用符ごと値の一部として扱われるため、エラーにならず 0 件になります。
:::

---

## kuroco-frontend-integration - フロントエンド統合 & KurocoFront デプロイ

Kuroco と Vite / Nuxt.js / Next.js の統合パターンおよび KurocoFront へのデプロイを提供するスキルです。
旧 `kuroco-ai-deployment` の機能を統合しています。

実践的なチュートリアルは [Kuroco サンプルサイトチュートリアル](https://kuroco.app/ja/docs/tutorials/kuroco-sample-site/) を参照してください。

### 機能

**フロントエンド統合:**
- Vite + Vue 3 / Nuxt 3 / Nuxt 2 / Next.js（App Router / Pages Router）の統合パターン
- 環境変数設定、プロジェクト構成例
- 認証実装（ログイン / ログアウト / ログイン状態確認 / 会員登録）
- SPA / SSG / SSR 設定
- KurocoPages との連携
- サードパーティ Cookie 問題への対応、XSS 対策

**KurocoFront デプロイ:**
- `kuroco_front.json` の設定
- GitHub リポジトリ連携によるデプロイ
- Admin MCP からの直接デプロイ（zip アップロード → `kuroco_front-deploy` → `kuroco_front-history` で反映確認）
- プレビューデプロイ（`is_preview`）/ 本番デプロイ、上書き時の注意点

### 使用例

```
「Nuxt3 で Kuroco のコンテンツを表示したい」
「Next.js で Kuroco の認証を実装したい」
「SSG で静的サイトを生成したい」
「Safari でログインできない（Cookie の問題）」
「Kuroco のサイトを KurocoFront にデプロイしたい」
「プレビュー環境にデプロイして確認したい」
```

### 対応するキーワード

`Vite` `Nuxt3` `Next.js` `App Router` `SPA` `SSG` `SSR` `useAsyncData` `$fetch` `composable` `useAuth` `KurocoPages` `credentials include` `サードパーティCookie` `XSS` `KurocoFront` `kuroco_front.json` `GitHub連携` `kuroco_front-deploy` `kuroco_front-history` `artifact_url` `stage_url` `is_preview` `CI/CD`

### フレームワーク別の推奨

| フレームワーク | 推奨ユースケース |
|--------------|----------------|
| Vite + Vue 3 | シンプルな SPA（SEO 不要のアプリ・ツール類） |
| Nuxt.js 3.x | SEO が必要なコンテンツサイト（SSG で静的 HTML 生成、推奨） |
| Nuxt.js 2.x | 既存 Vue プロジェクト |
| Next.js 13+（App Router） | 新規 React プロジェクト |
| Next.js（Pages Router） | 既存 React プロジェクト |

### デプロイ方法

| 方法 | 内容 |
|------|------|
| GitHub 連携 | 管理画面 [KurocoFront] → GitHub リポジトリ連携。push 時に GitHub Actions でビルドし、成果物をデプロイ |
| Admin MCP からの直接デプロイ | ビルド成果物の zip をアップロードし、`kuroco_front-deploy` でデプロイ（非同期）。`kuroco_front-history` で反映を確認 |

:::caution 上書きについて
1 つのドメインで公開されるのは現行デプロイ 1 つだけで、新しいデプロイは既存の公開内容を置き換えます。本番反映前に `is_preview: true` でのプレビューデプロイによる確認を推奨します。
:::

---

## kuroco-server-processing - Smarty プラグイン & バッチ処理

Kuroco の Smarty テンプレートの完全リファレンスおよびバッチ処理・Webhook・トリガーを使った自動化パターンを提供するスキルです。
旧 `kuroco-smarty-plugins` と `kuroco-webhook-processing` を統合したスキルです。

### 機能

**Smarty プラグインリファレンス:**
- 210 個のプラグインの完全なリファレンス
- カテゴリ別索引（API / 文字列 / 配列 / フォーム / 認証 / 外部連携 / ファイル / Vue.js）
- Smarty 基本構文（変数代入、ループ、条件分岐、修飾子）
- セキュリティ設定（IF_FUNCS / MODIFIER_FUNCS）

**バッチ処理 & Webhook:**
- バッチ処理の設定方法と実行頻度
- 内部 API 呼び出し（`api_internal`）
- 外部 API 呼び出し（`api`）
- トリガー処理（コンテンツ更新時 / フォーム送信時）、トリガーメールアドレス
- 外部サービス連携（Slack / Chatwork / SendGrid / メール / GitHub Actions）

**外部システム連携方式の設計:**
- 3 パターン（直接呼び出し / プロキシ / 取り込み）の使い分けと判断基準（認証情報の秘匿、リアルタイム性、Kuroco の標準機能に乗せるか、スパイダーとバッチの向き不向き）
- プロキシパターンの実装制約（`api` プラグイン: 1 回の呼び出しで送信できるファイルは 1 件、`timeout` は既定 30 秒・最大 3600 秒）、カスタムエンドポイントからの結果の返却
- `secret` プラグインによる秘密情報の管理、OAuth トークンのライフサイクル（都度取得 / 保護された Topics レコードへの保存）、連携先ごとの落とし穴（Instagram、Twilio、LINE、Slack など）
- 外部への通知送信（Slack / LINE / SMS）はトリガー処理とトリガーメールアドレスで行う（3 パターンの外）

### 使用例

```
「Smarty で記事一覧を取得して表示したい」
「sendmail プラグインの使い方を教えて」
「Smarty で JSON をパースする方法は？」
「バッチ処理で毎日 CSV を生成したい」
「コンテンツ更新時に Slack に通知を送りたい」
「GitHub Actions でデプロイをトリガーしたい」
「外部 API と連携したい。API キーをどこに置くべきか」
「Instagram の投稿を定期的に取り込みたい」
```

### 対応するキーワード

`Smartyプラグイン` `Smarty関数` `Smarty修飾子` `assign` `foreach` `escape` `date_format` `api_internal` `sendmail` `slack_post_message` `ai_completion` `write_file` `バッチ処理` `Webhook` `定期実行` `cron` `Slack通知` `Chatwork` `SendGrid` `GitHub Actions` `api` `トリガー` `トリガーメールアドレス` `カスタム処理` `外部連携` `直接呼び出し` `プロキシ` `取り込み` `secret` `シークレット` `スパイダー` `OAuth` `リフレッシュトークン` `mTLS`

### カテゴリ別リファレンス

| カテゴリ | 主なプラグイン |
|---------|---------------|
| API・データ取得 | `api_internal`, `assign_topics_list`, `assign_tag_list` |
| 文字列処理 | `escape`, `truncate`, `date_format`, `translate` |
| 配列操作 | `count`, `in_array`, `implode`, `explode` |
| フォーム・UI | `fileupload`, `inquiry_input`, `pager` |
| 認証・権限 | `rcms_auth`, `login`, `logout` |
| 外部連携 | `sendmail`, `slack_post_message`, `ai_completion` |
| ファイル操作 | `write_file`, `put_file`, `read_file` |
| Vue.js 連携 | `rcms_vue_component`, `head_include` |

### バッチ処理の実行頻度

| 頻度 | 用途 |
|------|------|
| 15 分毎 | 頻繁な同期が必要な場合 |
| 30 分毎 | 準リアルタイム処理 |
| 1 時間毎 | 定期的な集計・更新 |
| 毎日（指定時刻） | 日次レポート、バックアップ |

### 3 つの連携パターン

| パターン | 構成 | 向くケース |
|---------|------|-----------|
| 直接呼び出し | フロントエンドが外部 API を直接呼ぶ。Kuroco は関与しない | 外部 API 側が CORS を許可しており、認証情報をフロントに置いてよい場合 |
| プロキシ（Kuroco 経由） | カスタムエンドポイントの Smarty テンプレートから `api` プラグインで外部 API を呼び、結果を返す | 認証情報を隠したい、認証・CORS・流量制限を Kuroco 側に一本化したい、レスポンスを加工したい場合 |
| 取り込み | 外部データを事前に Topics / CSV テーブルへ取り込み、標準の Topics API で提供する | 更新頻度が低い、Kuroco の標準機能（検索・キャッシュ・多言語）に外部データも乗せたい場合 |

:::caution 秘密情報の置き場所
API キーや Webhook の秘密 URL など、攻撃に使われうる値は `secret` プラグイン（[環境設定] → [シークレット]に事前登録）で読み出します。サイト定数（`$smarty.const.*`）は非秘匿の設定値向けであり、秘匿情報の置き場所にはしません。
:::

:::note
スパイダーは Web ページやファイルの巡回・取り込みを行う機能で、構造化された外部 API の定期取得には向きません。巡回自体が課金対象の API リクエストを発生させます。構造化データの定期取得はバッチ処理から `api` プラグインで取得し、`api_internal` で Topics へ登録する構成にします。
:::

---

## kuroco-admin-mcp - Admin MCP 接続 & 管理操作

Admin MCP（管理 MCP サーバ）への接続設定と、MCP ツールによる管理操作を支援するスキルです。
AI エージェントから Kuroco の管理操作を行う場合の推奨手段です。

### 機能

- モジュールスコープ付きエンドポイント URL の組み立て方（`/x/all`、`/x/all/readonly`、`/x/topics_group_5` など）
- 3 つの認証方式（OAuth 2.0 認可コードフロー / 特権静的トークン / 管理セッション）と CIMD の利用
- OAuth スコープの権限レベル設計（`mcp:tools.read` / `mcp:tools.write` / `mcp:tools.all` / `mcp:admin` の 4 レベル、リソース単位スコープ）
- `whoami` による実効権限の事前確認
- Claude Code・Claude（Web / Desktop）・ChatGPT・Codex CLI からの接続設定
- ツールの命名規則（`{リソース}-{動詞}`）と利用フロー、ファイルアップロード（ステージング → 参照渡し）
- 「ツールが見えない」「audience 不一致」「エンドポイント作成だけ権限エラー」などのトラブルシューティング

### 使用例

```
「Claude Desktop から Kuroco を操作したい」
「Admin MCP に接続したい」
「MCP のツールが表示されない原因を知りたい」
「読み取り専用で MCP を使いたい」
```

### 対応するキーワード

`Admin MCP` `MCP サーバ` `MCP 接続` `OAuth` `CIMD` `Issuer URL` `mcp:admin` `mcp:tools.all` `mcp:tools.write` `mcp:tools.read` `whoami` `スコープ` `tools/list` `特権静的トークン`

### スコープの権限レベル

| スコープ | できること |
|---------|-----------|
| `mcp:tools.read` | 全モジュールの読み取りのみ（書き込み不可） |
| `mcp:tools.write` | `topics` / `csvtable` / `tag` / `comment` 等の登録・更新。削除は不可で、`rcms_api` `member` `group` `batch` は含まれない |
| `mcp:tools.all` | 全モジュール・全操作（下記の例外を除く） |
| `mcp:admin` | 制約なし。スーパーユーザーのみ承認可能 |

`mcp:tools.write` は単独では選べず、`mcp:tools.read` とセットで付与されます。`mcp:tools.all` でも、権限グループと汎用 Smarty バッチの作成・変更・削除、メンバーへのスーパーユーザーグループ付与、特権付き静的トークンの発行はできません。

:::note
API 定義・エンドポイントの作成には `mcp:tools.all` 以上が必要です。コンテンツ定義の作成は `mcp:tools.write` で進むため、エンドポイント作成の手前で初めて失敗します。着手前に `whoami` で `permissions.connection.scope` を確認してください。
:::

### 前提条件

- 対象サイトの管理メンバーアカウント（OAuth 認可フローで管理画面のログイン・同意を経由するため）
- 接続元 IP を限定する場合は、[環境設定] → [管理画面] の「Admin MCP のアクセス制限(IP アドレス)」の設定

:::caution 課金対象
Admin MCP（`/direct/rcms_api/admin_mcp/`）へのリクエストは、通常の API リクエストと同様に**リクエストごとの課金対象**です。
:::

---

## kuroco-content-structure - コンテンツ構造の設計と作成

コンテンツ定義（TopicsGroup）を、設計判断から Admin MCP ツール `topics_group-create` による作成まで一貫して扱うスキルです。Part 1 で設計（定義の分割、マスタデータ、分類、`ext_slug`）を確定し、Part 2 でペイロードを組み立てて作成し、読み戻しで検証します。設計相談だけの依頼は Part 1 で終了します。

### 機能

**Part 1 — 設計判断:**
- コンテンツ定義を分割するかどうかの判断（拡張項目数の上限、コンテンツの性質の違い）
- 検索・一覧表示・外部連携に使わない付随項目を JSON 項目にまとめる判断
- マスタデータの表現方法の選択（CSV テーブル / 別コンテンツ定義 + リレーション）
- 分類の持ち方の選択（カテゴリ / タグ / リレーション）
- `ext_slug` の命名方針と予約語
- 定義レベルの設定（本文の持ち方、閲覧・編集制限、承認、自分の投稿のみ）まで含む設計成果物テンプレート

**Part 2 — Admin MCP での作成:**
- `topics_group-create` の手順と定義レベルのパラメータ（`content_input_type`、`secure_level`、`writer_groups`、`need_application_groups`、`my_topics_only_limit_groups`）
- `topics_group-describe` と照合したフィールドタイプのリファレンス（テキスト、WYSIWYG、選択、チェックボックス、画像、ファイル、関連、日付、JSON、CSV テーブル、ブロックエディタなど）、フィールドグループ・繰り返し項目
- 書き込み後に `topics_group-get` で必ず読み戻して検証する手順
- 既存定義への項目追加（`topics_group-update`。部分更新で `fields` は追加のみ、削除はしない）

### 使用例

```
「都道府県マスタは CSV テーブルとリレーションのどちらで持つべき？」
「カテゴリとタグのどちらを使うべきか」
「コンテンツ定義を新しく作りたい」
「既存のお知らせ定義に添付 PDF の項目を追加して」
```

### 対応するキーワード

`コンテンツ構造` `コンテンツ定義` `TopicsGroup` `マスタデータ` `CSV テーブル` `csvtable` `relation` `カテゴリ` `タグ` `JSON 項目` `ext_slug` `拡張項目` `フィールドタイプ` `フィールドグループ` `繰り返し項目` `topics_group-create` `topics_group-update` `topics_group-describe`

### マスタデータの表現方法

| 観点 | CSV テーブル + `csvtable` / `csvtable_checkbox` | 別コンテンツ定義 + `relation` |
|------|------------------------------------------------|------------------------------|
| マスタの実体 | CSV テーブル（コンテンツ定義とは別のリソース） | 通常のコンテンツ定義 |
| 呼び出し側の API レスポンス | キーのみ。値は `Master::list` を別途呼んで結合する | id + ラベルがインラインで返る |
| マスタ側の拡張項目・カテゴリ・公開制御 | 持てない | 持てる |
| マスタ自身の属性での絞り込み | 不可 | 可能（`:R()` 検索。主言語に対してのみ実行可能） |
| 向くケース | 都道府県・業種一覧など、静的で単純なキー / 値の対応 | マスタを管理画面で編集する、属性を持つ、絞り込みに使う |

:::note
`relation` 型のレスポンスに含まれるのは、既定では id とラベルのみです。関連先コンテンツの全項目を返すには、エンドポイントの後処理にカスタム処理を追加する必要があります。
:::

---

---

## kuroco-auth-design - 認証・会員設計

会員認証と権限まわりの設計判断を行うスキルです。実装コードは `kuroco-frontend-integration`、既存設定の点検は `kuroco-security-audit` が担当します。

### 機能

- API 認証方式の選択（認証なし / Cookie 認証 / 動的アクセストークン / 静的アクセストークン）
- 会員グループ設計（モジュールごとの権限の組み合わせ、権限昇格経路の回避）
- 登録フローの選択（即時登録 / 招待 / 仮登録）
- コンテンツアクセス制限のスコープ（グループ制限 / カスタム検索 / 自分の投稿のみ）と、認証方式と権限をセットで設定する必要性
- パスワードポリシー・2 要素認証（管理画面向けと会員ログイン向けの切り分け）
- 代理ログインの要否
- エンタープライズ SSO（OAuth SP / SAML SP / IDaaS SP）・SCIM プロビジョニングを見据えた設計

### 使用例

```
「会員機能を設計したい」
「会員グループをどう分ければいいか」
「登録フローをどうするか」
「あとから SSO を繋げられるようにしたい」
```

### 対応するキーワード

`会員認証` `会員グループ` `登録フロー` `仮登録` `招待` `閲覧制限` `編集制限` `パスワードポリシー` `2 要素認証` `代理ログイン` `SSO` `OAuth SP` `SAML SP` `IDaaS SP` `SCIM`

### ID 連携の種類

| 仕組み | 役割 |
|--------|------|
| OAuth SP | Kuroco がクライアントとなり、外部 IdP で OAuth 認証による SSO ログインを行う |
| SAML SP | Kuroco がサービスプロバイダとなり、外部 IdP と SAML 認証で SSO ログインを行う |
| IDaaS SP | CIAM（消費者向け ID 管理）サービスと連携して SSO ログインを行う |
| SCIM SP | ログインではなく、外部 IdP からの会員情報の自動同期（作成・更新・無効化） |

同時に有効にできる SCIM SP は 1 サイトにつき 1 つです。

:::note
本スキルが扱うのはサイトの会員の認証・権限です。AI エージェント自身が Kuroco の管理操作を行うための OAuth スコープ（`mcp:admin` など）は `kuroco-admin-mcp` の対象です。
:::

---

## kuroco-api-performance-review - API パフォーマンス & コストレビュー

Admin MCP の読み取り系ツールで API のパフォーマンスと利用料を調査し、キャッシュ設定を中心とした改善提案をまとめるスキルです。

### 機能

- 費目別のコスト内訳と推移の把握（利用状況）
- エンドポイント別の集計分析（リクエスト数、キャッシュヒット / ミス、平均実行時間、平均レスポンスサイズ）
- キャッシュ設定と直近実績の突き合わせ（キャッシュ期間が未設定なのか、設定済みでも当たっていないのかの切り分け）
- 生ログによる裏取り（クローラー比率、リファラー別のリクエスト数、エラーの常態化）
- 症状別の調査レシピと、費用対効果順の対策整理

### 使用例

```
「Kuroco の利用料が増えた原因を調べたい」
「キャッシュヒット率が低いエンドポイントを洗い出したい」
「API リクエスト課金の内訳を分析して」
「レスポンスが遅いエンドポイントを特定して」
```

### 対応するキーワード

`利用料` `コスト` `従量課金` `API リクエスト` `キャッシュされた API リクエスト` `キャッシュヒット率` `MISS` `PASS` `API 解析` `キャッシュ設定` `maxage` `CDN 転送量` `実行時間` `クローラー`

### 前提条件

- Admin MCP への接続（調査のみであれば読み取り専用の権限レベルで足ります）
- 費用の分析には利用状況を参照できる権限

---

## kuroco-security-audit - セキュリティ設定チェック

Admin MCP の読み取り系ツールのみでセキュリティ設定を収集し、チェックリストに照らしてリスクを診断・報告する**読み取り専用**のスキルです。設定の変更は行いません。

### 機能

- API のセキュリティ方式・CORS・IP アドレス制限の点検
- ログイン / パスワードポリシー、2 要素認証（ワンタイムパスワード）の設定確認
- 権限グループとスーパーユーザーの棚卸し
- 静的アクセストークン・シークレットの棚卸し
- 監査ログの有効性確認と、MCP で取得できない項目の手動確認リスト化

### 使用例

```
「セキュリティ設定に問題がないか確認したい」
「CORS と IP 制限の設定を点検して」
「権限グループとスーパーユーザーを棚卸ししたい」
「静的アクセストークンの棚卸しをして」
```

### 対応するキーワード

`セキュリティチェック` `セキュリティ監査` `セキュリティ診断` `CORS` `IP 制限` `アクセス制限` `権限` `スーパーユーザー` `2 要素認証` `ワンタイムパスワード` `パスワードポリシー` `静的アクセストークン` `監査ログ`

:::info 脆弱性スキャンとの違い
本スキルは管理画面で設定できる項目の**設定値レビュー**を行うもので、脆弱性スキャンやペネトレーションテストは対象外です。
:::

---

## kuroco-spec-writer - 仕様書生成

Admin MCP の読み取り系ツールのみでサイトの実設定を収集し、Markdown + Mermaid の仕様書（現況仕様書）を生成する**読み取り専用**のスキルです。設定の変更は行いません。

### 機能

- コンテンツ定義の項目表と ER 図、API エンドポイント一覧、認証・会員グループ、承認フロー、カスタム処理・バッチ、フォームの生成
- そのサイトで実際に使われているモジュールの判定（CSV テーブル、サイト定数、メールテンプレートなど）と章の追加
- 1 定義 = 1 ページの分割出力と、ファイル名・図のノード名に使うページキーの採番
- 生成に使用した読み取りツール名の出典記載
- 付属スクリプトによる PDF + zip への変換
- 生成した仕様書をユーザーが編集し、その差分をサイトへ反映する往復運用（書き込み自体は `kuroco-admin-mcp` に委譲）

### 使用例

```
「サイトの仕様書を作って」
「コンテンツ定義を一覧化して ER 図も作って」
「引き継ぎ資料を PDF でほしい」
「編集した仕様書の内容をサイトに反映して」
```

### 対応するキーワード

`仕様書` `設計書` `現況仕様書` `as-built` `ドキュメント化` `ER 図` `Mermaid` `PDF` `引き継ぎ資料` `納品ドキュメント`

### 出力構造

```
spec/
├── README.md              # 目次・サイト概要・全体構成図
├── contents/              # コンテンツ定義（一覧表 + ER 図、1 定義 = 1 ページ）
├── functions/             # カスタム処理・バッチ（1 処理 = 1 ページ）
├── api.md                 # API エンドポイント一覧
├── auth.md                # 認証・会員グループ
├── workflow.md            # 承認フロー（使用している場合のみ）
├── forms.md               # フォーム（使用している場合のみ）
└── {module}.md            # 上記以外で使われているモジュールの一覧
```

### 前提条件

- Admin MCP への接続。書き込み系ツールが一覧に出ないため、`/readonly` を付けたスコープ URL を推奨します
- 仕様書は横断的にモジュールを参照するため、スコープは `all` が適切な場合が多いです

:::info セキュリティ監査との違い
本スキルは実設定を仕様書として書き起こすスキルです。セキュリティ観点のリスク判定は `kuroco-security-audit` が担当します。
:::

---

## 関連ドキュメント

- [Kuroco Skills の使い方](/ja/docs/tutorials/kuroco-skills-overview/) - インストール方法と基本的な使い方
- [Kuroco Skills GitHub リポジトリ](https://github.com/diverta/kuroco-skills)


---

# MCP クライアント設定リファレンス

> 元ページ: `reference/mcp-client-configuration` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/mcp-client-configuration/
> 概要: Kuroco の MCP エンドポイントを主要な MCP クライアントへ接続するための設定手順です。

このページでは、**OAuth 2.0** を使って MCP クライアントを Kuroco に接続する方法を説明します。

設定は次の 3 ステップで完了します。

1. [対応クライアント](#対応クライアント)の表で、使用するクライアントの対応状況を確認します。クライアント名のリンクから、そのクライアントの設定手順へ直接移動できます。
2. [Kuroco 側の設定](#kuroco-側の設定)を行います。ほとんどの場合、デフォルトの認可サーバーで CIMD を有効化するだけで済みます。
3. 各クライアントの設定手順に従って Kuroco に接続します。

リクエストヘッダー（`X-RCMS-API-ACCESS-TOKEN`）による認証にも対応していますが — [認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/) を参照してください — OAuth の利用を推奨します。

OAuth 接続を設定する前に、Kuroco 管理画面に表示される **発行元 (Issuer) URL** を確認します。Issuer URL は認可サーバーを識別する URL です。MCP クライアントに **Issuer URL** または **OAuth Issuer** の入力欄がある場合は、この URL を入力します。確認場所と URL の例は[発行元 (Issuer) URL を確認する](#発行元-issuer-url-を確認する)を参照してください。

## 対応クライアント

クライアント名のリンクから、各クライアントの設定手順へ移動できます。

### チャットベースのクライアント

| クライアント | OAuth サポート | CIMD | クライアントの手動登録 | ヘッダー認証 |
|--------|---------------|------|------------------------------|------------|
| [Jan](#jan) | ❌ | ❌ | ❌ | ✅ |
| [Claude（Web / Desktop / Mobile）](#claudeweb--desktop--mobile) | ✅ | ✅ | ✅ | ❌ |
| [ChatGPT（Developer mode）](#chatgpt-appsdeveloper-mode) | ✅ | ✅ | ✅ | ❌ |
| [Slackbot](#slackbot) | ✅ | ❌ | ✅ | ❌ |

### コーディングアシスタント

| クライアント | OAuth サポート | CIMD | クライアントの手動登録 | ヘッダー認証 |
|--------|---------------|------|------------------------------|------------|
| [Claude Code](#claude-code) | ✅ | ✅ | ✅ | ✅ |
| [Codex CLI](#codex-cli) | ✅ | ✅ | ✅ | ✅ |
| [Cursor](#cursor) | ✅ | ❌ | ✅ | ✅ |
| [GitHub Copilot Chat（VS Code）](#github-copilot-chatvs-code) | ✅ | ✅ | ✅ | ✅ |
| [GitHub Copilot coding agent](#github-copilot-coding-agent) | ❌ | ❌ | ❌ | ✅ |

### カスタム実装

| クライアント | OAuth サポート | CIMD | クライアントの手動登録 | ヘッダー認証 |
|--------|---------------|------|------------------------------|------------|
| [Python / TypeScript / その他のカスタム MCP クライアント](#python--typescript--その他) | ✅ | クライアントの実装に依存 | ✅ | ✅ |

**補足:**
- CIMD は IETF のドラフト仕様（`draft-ietf-oauth-client-id-metadata-document`）です。各クライアントでの対応は最近始まったばかりで変化し続けているため、本番環境で利用する前に各ベンダーの最新ドキュメントで再確認してください。
- 「クライアントの手動登録」とは、ユーザーが事前登録済みの `client_id`／`client_secret` を設定できることを指します。この選択肢がないクライアントは、CIMD または RFC 7591 DCR に対応した認可サーバーに対してのみ OAuth を利用できます。
- 「ヘッダー認証」とは、リクエストヘッダー（`X-RCMS-API-ACCESS-TOKEN`）にアクセストークンを設定して認証できることを指します。設定手順は [認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/) を参照してください。

## Kuroco の OAuth クライアント登録サポート

MCP クライアントが Kuroco に対して認可コードフローを開始するには、事前に `client_id`（コンフィデンシャルクライアントの場合は `client_secret` も）が必要です。Kuroco では、これを取得する方法を 2 通り用意しています。

1. **CIMD（クライアント ID メタデータドキュメント）** — `client_id` 自体が HTTPS の URL であり、そのクライアントを説明する小さな JSON ドキュメント（`redirect_uris`、`client_name` など）を返します。Kuroco は初回利用時にこのドキュメントを取得・検証するため、クライアントごとの管理画面操作は不要です。Claude、Claude Code、ChatGPT、Codex CLI、GitHub Copilot Chat はこの方式を利用します。**CIMD は MCP のクライアント登録方式として現在デフォルトかつ推奨の方式です** — [MCP の認可仕様](https://modelcontextprotocol.io/specification/draft/basic/authorization/client-registration#dynamic-client-registration) の最新ドラフトでは、旧来の動的クライアント登録（DCR）は非推奨と明記されています。
2. **クライアントの手動登録** — 管理者が Kuroco 管理画面でクライアントを事前登録し、発行された `client_id`（該当する場合は `client_secret` も）を MCP クライアントの設定担当者に渡します。CIMD に対応していないクライアント（例：Cursor）や、クライアントを明示的に管理したい場合に利用します。

Kuroco は OAuth の動的クライアント登録（RFC 7591 の `POST /register` フロー）を**実装していません**。これは上記の非推奨化に沿った対応です。RFC 7591 の DCR のみに対応し、手動設定の手段を持たないクライアントは、Kuroco に対して OAuth を完了できません。

## リソース識別子とスコープ付きエンドポイント

Kuroco は MCP の要件に従い、クライアントが RFC 8707 の `resource` パラメータとして **MCP サーバーの正規 URI** を送ることと、サーバーが自身向けに発行されたトークンのみを受け付けることを前提としています。つまり、**クライアントに設定した MCP サーバー URL がリソース識別子であり、トークンはその URL に紐付きます。**

これが特に重要になるのは、URL にエンドポイントのスコープ指定セグメントを持つ **Admin MCP** です。

```text
https://your_site_key.g.kuroco.app/direct/rcms_api/admin_mcp/x/all
https://your_site_key.g.kuroco.app/direct/rcms_api/admin_mcp/x/topics_group_1,member/readonly
```

これらの URL はそれぞれ**別個の OAuth リソース**です。`x/topics_group_1,member/readonly` で取得したトークンを `x/all` に対して使うと `401` で拒否されるため、URL を絞ることは実際に認可範囲を絞ることになります（ツール一覧のフィルタにとどまりません）。実務上の注意点は次のとおりです。

- 付与したい**スコープ付き URL そのもの**をクライアントに設定してください。ベースとなる `/direct/rcms_api/admin_mcp/` は MCP エンドポイントではなく `400` を返します（スコープ指定は必須です）。
- リソース／オーディエンスを明示的に設定する項目があるクライアント（Codex の `oauth_resource`、独自 SDK クライアント等）では、同じスコープ付き URL を設定するか、未設定にしてディスカバリに任せてください。
- スコープを変更すると URL が変わるため、クライアントは再認可が必要になり、新しいトークンを受け取ります。
- スコープ付き URL ごとに専用の Protected Resource Metadata ドキュメントが配信されます（例：`/.well-known/oauth-protected-resource/direct/rcms_api/admin_mcp/x/all`）。サーバー URL からメタデータ URL を導出するクライアントはそのまま解決でき、`401` チャレンジの `resource_metadata` を読むクライアントも同じ URL に到達します。

コンテンツ API MCP でも同じ原則が適用されます。リソース識別子は MCP サーバー URL です。

```text
https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp
```

Protected Resource Metadata ドキュメントもこの URL に対応する `/.well-known/oauth-protected-resource/rcms-api/{api_id}/mcp` で配信されるため、`401` チャレンジの `resource_metadata` を読むクライアントと、設定済みの MCP サーバー URL からメタデータ URL を導出するクライアントは同じ URL に到達します。リソース／オーディエンスを明示的に設定する項目があるクライアントでは、この MCP サーバー URL を設定するか、未設定にしてディスカバリに任せてください。同じ API の REST エンドポイント（`/rcms-api/{api_id}`）は別の OAuth リソースであり、MCP 用に取得したトークンでは呼び出せません。

## Kuroco 側の設定

OAuth ログインは、セキュリティが **動的アクセストークン** または **Cookie** に設定されている API で発生します。セキュリティが **静的アクセストークン**・**特権付き静的トークン** の API は OAuth ではなく、`X-RCMS-API-ACCESS-TOKEN` ヘッダーによるトークン認証を使用します（[認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/) を参照）。公開エンドポイント（セキュリティ = `なし`）の場合、MCP サーバーをクライアントに追加する手順自体は同じですが、認証するものがないため OAuth ログインの手順は発生しません。

:::caution
公開エンドポイントの使用は推奨しません。認証が不要なため URL が知られれば誰でも API にアクセスでき、リクエストの発信元も追跡できません。公開エンドポイントを使用する場合は、読み取り専用のエンドポイントに限定し、公開しても問題のないデータのみを対象にしてください。書き込みエンドポイントを認証なしで公開することは避けてください。
:::

Kuroco の OAuth は、トークンを発行する **認可サーバー** と、その配下に任意で作成する 1 つ以上の **登録済みクライアント** を中心に構成されています。最初に発行元 (Issuer) URL を確認し、続いて 2 通りの方法から設定方法を選択します。

### 発行元 (Issuer) URL を確認する

OAuth 接続では、Kuroco 管理画面に表示される **発行元 (Issuer) URL** が認可サーバーを識別する URL です。URL は次の形式です。

```text
https://your_site_key.g.kuroco-mng.app/direct/login/oauth_idp/{idpid}
```

この URL は形式を示す例です。URL を手動で組み立てず、OAuth Authorization Server 編集画面（`/management/external/memberregist_sso_oauth_idp_edit/`）に表示される値をそのまま使用します。Admin MCP の場合は、Admin MCP 設定画面（`/management/rcms_api/admin_mcp_info/`）でも確認できます。

MCP クライアントに **Issuer URL** または **OAuth Issuer** の入力欄がある場合は、この URL を入力します。入力欄がなく OAuth の自動検出に対応しているクライアントでは、MCP サーバー URL を登録すると認可サーバーの情報が検出されます。その場合も、検出された認可サーバーが意図した接続先かを、管理画面の **発行元 (Issuer) URL** と照合します。

**MCP サーバー URL** または **Server URL** の入力を求められた場合は、Issuer URL ではなく、利用する MCP サーバーの URL を入力します。MCP サーバー URL の形式は [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/) を参照してください。

**Client ID** または **Client Secret** の入力を求められた場合は、[クライアントを手動登録する方法](#クライアントを手動登録する方法)を利用する場合のみ、OAuth Authorization Server クライアントの保存時に発行された値を入力します。CIMD を利用する場合は入力しません。

### CIMD（クライアント ID メタデータドキュメント）を使う方法

Kuroco では、初めて必要になったタイミングで **Admin MCP (default)**（管理系 MCP エンドポイント用）と **Kuroco MCP API (default)**（`/rcms-api/{api_id}/mcp` で公開されるコンテンツ API 用）という 2 つのデフォルト認可サーバーが自動的に作成されます。ほとんどの場合は、これらのデフォルト認可サーバーのどちらかを編集し、CIMD が未有効であれば有効化するだけで済みます。新しいカスタム認可サーバーの作成は、コンテンツ API ごとに異なるスコープ／グラントタイプで個別の認可サーバーを用意したい場合など、より高度な構成が必要な場合にのみ必要です。

#### デフォルトの認可サーバーを使う

管理画面で **外部システム連携 > ID連携 > OAuth Authorization Server** を開きます。

公開したいエンドポイントに対応するデフォルトの認可サーバー（**Admin MCP (default)** または **Kuroco MCP API (default)**）を開き、**クライアント ID メタデータドキュメント（URL クライアント ID）** が未有効であれば有効化します。

#### 新しいカスタム認可サーバーを作成する

同じ一覧画面から **追加** をクリックし、以下を設定します。

| 項目 | 説明 |
|-------|-------------|
| **名前** | この認可サーバーを識別するための自由入力ラベルです。 |
| **用途** | この認可サーバーが保護する対象です。`API`（`/rcms-api/{api_id}/mcp` で公開されるコンテンツ API）、`Management`、`AdminMCP`（管理系 MCP エンドポイント、`/direct/rcms_api/admin_mcp/...`）から選択します。**作成後は変更できません。** `Management`／`AdminMCP` について、サイト全体で有効化できる認可サーバーはそれぞれ 1 つのみです。 |
| **クライアント ID メタデータドキュメント（URL クライアント ID）** | **これが CIMD の有効／無効を切り替えるスイッチです。** 有効にすると、クライアントはメタデータ URL 自体を `client_id` として認証できるようになります（例：Claude Code、ChatGPT）。 |
| **対応するグラントタイプ** | `authorization_code`、`refresh_token`、`client_credentials` のうち、クライアントに必要なものを選択します。 |
| **許可するスコープ** | この用途向けのスコープカタログです。`AdminMCP` の場合、個々のスコープはチェックボックスとして表示されません。代わりに、後述するクライアントごとの単一の権限レベル選択（**読み取り専用**／**読み書き**／**全権限**）に応じて、保存時にスコープが自動的に割り当てられます（読み取り専用 = `mcp:tools.read`、読み書き = `mcp:tools.read` + `mcp:tools.write`、全権限 = `mcp:admin`。ツール一覧取得用の `mcp:tools.list` はいずれのレベルでも自動的に付与されます）。 |
| **アクセストークン有効期間** / **リフレッシュトークン有効期間** / **認可コード有効期間** | トークンの有効期間を秒単位で指定します（デフォルト：3600 / 2592000 / 60）。 |

**用途** は作成時に選択する必要があり、後から変更できません。

作成後、`API` 用途の認可サーバーは API 構成一覧（`/management/rcms_api/api_list/`）から特定のコンテンツ API に割り当てられます。対象 API の **MCP設定** タブを開き、**OAuth Authorization Server** のドロップダウンから選択してください。

対象の認可サーバーで CIMD を有効化すれば、CIMD に対応したクライアント側では追加の設定は不要です。そのまま各クライアントの **CIMD** の節に進んでください。

:::note CIMD クライアントは管理画面のクライアント一覧に追加されません
CIMD で接続するクライアントは、認可のたびにクライアント自身のメタデータ文書から解決されるため、Kuroco 側にクライアントとして登録されず、管理画面のクライアント一覧にも表示されません。認可サーバーで CIMD を有効化すると、サイト管理者がクライアントを個別に登録しなくても、利用者が各自のログインと同意画面での承認だけで接続できるようになります。接続できる範囲は、ログインした本人の権限と、トークンに紐付くリソース（MCP サーバー URL）・スコープに制限されます。

クライアントを 1 件ずつ登録・管理したい場合は、CIMD を有効化せず [クライアントを手動登録する方法](#クライアントを手動登録する方法) を利用してください。
:::

### クライアントを手動登録する方法

以下の各クライアントの **クライアントの手動登録** の節で client_id／secret を直接設定するよう案内されている場合（例：**Cursor**）に利用します。

対象の認可サーバーの配下にある **外部システム連携 > ID連携 > OAuth Authorization Server > クライアント** を開きます。

以下を設定します。

| 項目 | 説明 |
|-------|-------------|
| **クライアント名** | 自由入力のラベルです（例：「Cursor」）。 |
| **トークンエンドポイント認証方式** | PKCE を使うパブリッククライアント（デスクトップアプリなど、Cursor に推奨）の場合は `none`、シークレットを保持できるコンフィデンシャルクライアントの場合は `client_secret_basic` または `client_secret_post` を選択します。 |
| **リダイレクト URI** | 同意後に MCP クライアントがリダイレクトする、正確なコールバック URL を 1 行に 1 つずつ指定します。この値は MCP クライアント側で固定されているため、そのクライアントのドキュメントや設定画面で正しい値を確認してください。`authorization_code` を選択したグラントタイプに含める場合は必須です。 |
| **対応するグラントタイプ** | 通常は `authorization_code` + `refresh_token` です。`client_credentials` を使う場合は、`none` 以外の認証方式と、紐付けるサービスメンバーが必要です。 |
| **許可するスコープ** | 用途のスコープカタログと、親の認可サーバーの **許可するスコープ** の積集合から選択します。`AdminMCP` の認可サーバーの場合、これは個別のスコープ選択ではなく、単一の権限レベル選択（**読み取り専用** / **読み書き** / **全権限**）になります。 |
| **有効** | クライアントを有効化します。 |

保存すると、Kuroco が **クライアント ID** を自動生成します。**トークンエンドポイント認証方式** が `none` 以外の場合は **クライアントシークレット** も生成され、**その場で一度だけ** 表示されます。以降は再表示できないため、すぐに控えてください。紛失した場合は編集画面の「シークレットを再生成」を使用します。

発行された **クライアント ID**（該当する場合は **クライアントシークレット** も）と、認可サーバーのメタデータ URL に記載されたトークン／認可エンドポイントを、MCP クライアントの設定担当者に渡してください。

#### 認可サーバーのメタデータ URL

OAuth Authorization Server 編集画面（`/management/external/memberregist_sso_oauth_idp_edit/`）には、認可サーバー固有の **メタデータ URL** が表示されます。「Authorization URL」や「Token URL」の入力を求められた場合は、メタデータ URL の JSON ドキュメントに記載された `authorization_endpoint` と `token_endpoint` の値を入力します。このドキュメントには、`issuer`、対応するグラントタイプ、スコープも記載されています。

## client_credentials でトークンを取得する

CI や常駐サービスなど、ブラウザでの対話的な認可を実行できない環境向けのグラントです。ユーザーの同意画面を経由せず、クライアント自身の資格情報でアクセストークンを取得します。

### クライアント側の対応状況

主要な MCP クライアントは、いずれも `client_credentials` グラント自体を実行する機能を持ちません。トークンの取得は利用者側（スクリプトや CI のジョブ）で行い、クライアントには取得済みのアクセストークンを `Authorization: Bearer` ヘッダーとして設定します。クライアントから見ると、これは固定のリクエストヘッダーであり、トークンの更新や再取得は行われません。

| クライアント | `client_credentials` の実行 | 取得済みトークンの受け渡し |
|------|:---:|------|
| Claude Code | ✕ | ○ `--header "Authorization: Bearer ..."`（`.mcp.json` の値は `${VAR}` 形式の環境変数展開に対応） |
| OpenAI Responses API の MCP ツール | ✕ | ○ ツール定義の `authorization` にトークンを指定 |
| ChatGPT / OpenAI Playground のコネクタ | ✕ | ✕ |
| GitHub Copilot coding agent | ✕ | ○ `headers` に Bearer ヘッダーを指定 |

:::note
対話的に利用するクライアントで `client_credentials` を使う場合、トークンの自動更新は行われません（後述のとおりリフレッシュトークンは発行されません）。有効期限が切れたら取得し直してヘッダーを設定し直す必要があるため、常用する用途には向きません。対話的なクライアントでは `authorization_code` を利用してください。
:::

### Kuroco 側の設定

`client_credentials` を使うクライアントは、CIMD ではなく[クライアントを手動登録する方法](#クライアントを手動登録する方法)で登録します（CIMD のクライアントはシークレットを持たないため利用できません）。次の条件をすべて満たす必要があります。

| 設定箇所 | 必要な値 |
|------|------|
| 認可サーバーの **対応するグラントタイプ** | `client_credentials` を含める |
| クライアントの **対応するグラントタイプ** | `client_credentials` を含める |
| クライアントの **トークンエンドポイント認証方式** | `client_secret_basic` または `client_secret_post`（`none` は不可） |
| クライアントの **サービスメンバー** | トークンの主体となるメンバーを指定する |
| クライアントの **対象リソース**（`AdminMCP` の場合） | 接続するスコープ付き URL を完全一致で指定する（必須） |
| クライアントの **対象APIのMCPサーバ**（`API` の場合） | 接続する MCP サーバーを選択する |

### トークンを取得する

トークンエンドポイントの URL は、認可サーバーのメタデータドキュメントの `token_endpoint` を参照してください（[認可サーバーのメタデータ URL](#認可サーバーのメタデータ-url)）。

```bash
curl -s -X POST "https://your_site_key.g.kuroco.app/direct/login/oauth_idp/{idp_id}/token" \
  -u "{client_id}:{client_secret}" \
  -d "grant_type=client_credentials" \
  -d "resource=https://your_site_key.g.kuroco.app/direct/rcms_api/admin_mcp/x/all"
```

- `resource`（RFC 8707）は必須です。クライアントの **対象リソース** と完全に一致する値を指定します。
- `-u` は `client_secret_basic` の場合の指定です。`client_secret_post` の場合は `-d "client_id=..." -d "client_secret=..."` を使用します。
- `scope` は省略できます。省略した場合はクライアントに設定された権限レベル（`AdminMCP` の場合は **読み取り専用** / **読み書き** / **全権限**）に応じたスコープが付与されます。

:::caution
`client_credentials` ではリフレッシュトークンは発行されません。アクセストークンの有効期限（認可サーバーの **アクセストークン有効期間**、デフォルト 3600 秒）が切れた場合は、同じリクエストでトークンを取得し直してください。
:::

主なエラーレスポンス:

| `error` | 主な原因 |
|------|------|
| `unauthorized_client` | 認可サーバーまたはクライアントの **対応するグラントタイプ** に `client_credentials` が含まれていない／**トークンエンドポイント認証方式** が `none` になっている |
| `invalid_client` | クライアントに **サービスメンバー** が設定されていない／クライアント認証に失敗している |
| `invalid_target` | `resource` パラメータを送っていない／クライアントの **対象リソース** と一致しない |
| `invalid_scope` | 要求したスコープが認可サーバーまたはクライアントの許可範囲を超えている |

### クライアントに設定する

取得したアクセストークンを `Authorization: Bearer` ヘッダーとして渡します。Claude Code の例:

```bash
export KUROCO_MCP_TOKEN="取得したアクセストークン"

claude mcp add --transport http kuroco-admin \
  https://your_site_key.g.kuroco.app/direct/rcms_api/admin_mcp/x/all \
  --header "Authorization: Bearer ${KUROCO_MCP_TOKEN}"
```

MCP サーバーの URL は、トークン取得時に指定した `resource` と同じ URL にしてください。異なる URL を指定すると、トークンのオーディエンスが一致せず `401` で拒否されます。

:::note
これは OAuth の Bearer トークンを渡す方法であり、`X-RCMS-API-ACCESS-TOKEN` ヘッダーによる[認証ヘッダー](/ja/docs/reference/mcp-client-configuration-authentication-header/)の方式とは異なります。静的アクセストークン・特権付き静的トークンによるヘッダー認証はコンテンツ API の MCP サーバー（`/rcms-api/{api_id}/mcp`）専用で、Admin MCP では利用できません。
:::

## チャットベースのクライアント

### Jan

Jan はヘッダー認証で Kuroco に接続できます。MCP 連携はサーバー URL と静的なヘッダー／環境変数の設定に対応しており、[認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/) の設定方法を利用してください。なお、OAuth の認可コードフロー、CIMD、クライアントの手動登録はいずれもサポートしていません。

### Claude（Web / Desktop / Mobile）

#### CIMD

対象の Kuroco の認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化した上で、以下を行います。

1. **Settings > Connectors** を開きます。
2. **Add custom connector** をクリックします。
3. リモート MCP URL（例：`https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp`）を入力します。
4. **Connect** をクリックすると、Kuroco の認可サーバーに対する OAuth 同意画面がブラウザで開きます。追加の設定は不要です。

#### クライアントの手動登録

クライアントの手動登録を利用する場合は、Claude のコネクタのコールバックに一致するリダイレクト URI を指定して Kuroco にクライアントを登録し（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）、以下を行います。

1. **Settings > Connectors** を開きます。
2. **Add custom connector** をクリックします。
3. リモート MCP URL を入力します。
4. **Advanced settings** を展開し、Kuroco が発行した `client_id`／`client_secret` を入力します。
5. **Connect** をクリックして OAuth 同意フローを完了します。

OAuth 認証を利用した Kuroco コネクタの登録手順は [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/) を参照してください。

公式ドキュメント:
- [Building custom connectors: authentication](https://claude.com/docs/connectors/building/authentication)
- [Getting started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

### ChatGPT Apps（Developer mode）

#### CIMD

対象の Kuroco の認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化した上で、以下を行います。

1. ワークスペース／ユーザーロールで Developer mode を有効化します。
2. **Apps > Create** を開きます。
3. MCP エンドポイントを入力すると、追加の設定なしに接続が完了します。

#### クライアントの手動登録

クライアントの手動登録を利用する場合は、Kuroco にクライアントを登録し（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）、以下を行います。

1. ワークスペース／ユーザーロールで Developer mode を有効化します。
2. **Apps > Create** を開きます。
3. MCP エンドポイントを入力します。
4. プロンプトが表示されたら、手動登録した `client_id`／`client_secret` を入力します。

公式ドキュメント:
- [Developer mode, and MCP apps in ChatGPT (beta)](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta)

### Slackbot

Slackbot は CIMD に対応していません。OAuth で Kuroco に接続する唯一の方法は、クライアントの手動登録です。

#### CIMD

Slackbot では未対応です。

#### クライアントの手動登録

以下の設定で Kuroco にクライアントを登録します（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）。
- **リダイレクト URI**: `https://oauth2.slack.com/external/auth/callback`
- **トークンエンドポイント認証方式**: `client_secret_post`

続いて、Slack 側で以下を行います。

1. [api.slack.com/apps](https://api.slack.com/apps) で Slack アプリを新規作成します。
2. アプリ設定の **MCP Servers** セクションを開き、**Add MCP Server** をクリックします。
3. **Name** と Kuroco MCP エンドポイントの **URL** を入力し、**Auth** に **Manual OAuth** を設定します。
4. Kuroco が発行した **Client ID** と **Client Secret** を入力します。**Authorization URL** と **Token request URL** は認可サーバーのメタデータ URL から取得します。**Use PKCE (Proof Key for Code Exchange)** を有効化し、残りの項目は空欄のままにします。

追加が完了すると、Slack の任意の会話で Slackbot から MCP サーバーのツールを利用できるようになります。

## コーディングアシスタント

### Claude Code

#### CIMD

対象の Kuroco の認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化します。Claude Code は CIMD 対応を自動検出し、自身がホストするクライアントメタデータドキュメント（`https://claude.ai/oauth/claude-code-client-metadata`）を利用するため、Kuroco 側での追加設定は不要です。

```bash
claude mcp add --transport http kuroco https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp
claude mcp login kuroco
```

#### クライアントの手動登録

クライアントの手動登録を利用する場合は、Kuroco にクライアントを登録し（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）、発行された資格情報を直接指定します。

```bash
claude mcp add --transport http kuroco https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp \
  --client-id "your-client-id" --client-secret "your-client-secret"
claude mcp login kuroco
```

公式ドキュメント:
- [Claude Code MCP](https://docs.claude.com/en/docs/claude-code/mcp)

### Codex CLI

Codex CLI は CIMD とクライアントの手動登録の両方に対応しています。Kuroco 側で CIMD を有効化していれば、管理画面でのクライアント登録なしに接続できます。

#### CIMD

対象の Kuroco の認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化します（[CIMD（クライアント ID メタデータドキュメント）を使う方法](#cimdクライアント-id-メタデータドキュメントを使う方法) を参照）。

```bash
codex mcp add kuroco --url https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp
codex mcp login kuroco
```

Codex は、認可サーバーが `client_id_metadata_document_supported: true` を広告している場合に CIMD を自動的に選択します。登録方式を明示的に指定する場合は、`codex mcp login` に `--oauth-client-registration` を付けます（既定値は `auto`）。

```bash
codex mcp login kuroco --oauth-client-registration cimd
```

:::note
`--oauth-client-registration` は Codex CLI のバージョンによっては利用できません。`codex mcp login --help` に表示されない場合は、オプションを付けずに自動選択に任せてください。
:::

次の場合は CIMD が使われないため、下記の「クライアントの手動登録」が必要です。

- Kuroco の認可サーバーで CIMD を有効化していない場合。Codex は DCR にフォールバックしますが、Kuroco は RFC 7591 の DCR を実装していないため接続できません。
- `config.toml` の `[mcp_servers.<name>.oauth]` に `client_id` を設定している場合。設定済みの OAuth クライアント ID が常に優先され、クライアント登録は行われません。CIMD を使う場合は `client_id` を設定しないでください。

#### クライアントの手動登録

CIMD を有効化できない場合や、クライアントを明示的に管理したい場合に利用します。Codex CLI には `client_secret` を設定する手段がないため、Kuroco 側では PKCE を利用する**パブリッククライアント**として登録します。

Kuroco でクライアントを登録します（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）。設定値は次のとおりです。

- **Token Endpoint Auth Method**: `none` — Codex は client_secret を保存できず、PKCE で認証します。
- **リダイレクトURI**: Codex は `http://127.0.0.1:{ポート}/callback/{サーバー固有ID}` 形式のループバックリダイレクト URI を生成します。ポートはログインごとにランダムですが、Kuroco はループバックのリダイレクト URI をポート無視で照合し（RFC 8252）、パス部分は MCP サーバー URL ごとに固定なので、URI の登録は一度だけで済みます。正確な値を確認するには、下記の `config.toml` 設定を済ませたうえで `codex mcp login kuroco` を一度実行します。初回は Kuroco のエラーページ（「redirect_uri does not match a registered URI」）で止まるので、ブラウザのアドレスバーに表示されている認可 URL の `redirect_uri` クエリパラメータをコピーし、クライアントのリダイレクト URI として登録してから再度ログインしてください。

次に `~/.codex/config.toml` を設定します。

```toml
[mcp_servers.kuroco]
url = "https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp"

[mcp_servers.kuroco.oauth]
client_id = "your-oauth-client-id"
```

ログインします。

```bash
codex mcp login kuroco
```

任意項目の `scopes` と `oauth_resource` は通常は省略できます。省略した場合、Kuroco はクライアントに許可されたスコープと認可サーバーのデフォルトリソースを適用します。`oauth_resource` を設定する場合は `url` と同じ URL を指定してください（MCP サーバー URL がリソース識別子です。[リソース識別子とスコープ付きエンドポイント](#リソース識別子とスコープ付きエンドポイント) を参照）。

公式ドキュメント:
- [Model Context Protocol – Codex](https://learn.chatgpt.com/docs/extend/mcp)

### Cursor

Cursor はデフォルトで RFC 7591 の DCR を実行しますが、Kuroco はこれを実装しておらず、CIMD にも対応していません。OAuth で Kuroco に接続する唯一の方法は、クライアントの手動登録です。

#### CIMD

Cursor では未対応です。

#### クライアントの手動登録

Cursor の固定コールバック URL を `redirect_uris` に設定して、Kuroco にクライアントを登録します（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）。
- Web: `https://www.cursor.com/agents/mcp/oauth/callback`
- Desktop: `cursor://anysphere.cursor-mcp/oauth/callback`

続いて `mcp.json` を直接設定します。

```json
{
  "mcpServers": {
    "kuroco": {
      "url": "https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp",
      "auth": {
        "CLIENT_ID": "your-oauth-client-id",
        "CLIENT_SECRET": "your-oauth-client-secret",
        "scopes": ["your", "selected", "scopes"]
      }
    }
  }
}
```

公式ドキュメント:
- [Cursor MCP docs](https://docs.cursor.com/context/mcp)

### GitHub Copilot Chat（VS Code）

VS Code の MCP クライアントは、まず CIMD を試み、次に DCR（Kuroco は未対応）を試み、どちらも利用できない場合に `client_id`／`client_secret` の手動入力を求めます。

#### CIMD

対象の Kuroco の認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化します。サーバー URL のみを設定します。

```json
{
  "servers": {
    "kuroco": {
      "type": "http",
      "url": "https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp"
    }
  }
}
```

`oauth` ブロックは不要です — Kuroco からの `401` と `WWW-Authenticate` レスポンスをきっかけにネゴシエーションが開始されます。

#### クライアントの手動登録

クライアントの手動登録を利用する場合は、Kuroco にクライアントを登録します（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）。VS Code はサーバー追加時に `client_id`／`client_secret` の入力を対話的に求めます。保存済みの資格情報はその後 **Accounts メニュー > Manage Trusted MCP Servers** から管理できます。

公式ドキュメント:
- [Using MCP with GitHub Copilot](https://docs.github.com/copilot/how-tos/context/model-context-protocol)
- [VS Code MCP configuration reference](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration)

### GitHub Copilot coding agent

coding agent はリモート MCP サーバーに対する OAuth をサポートしていません — GitHub のドキュメントにも明記されており、CIMD・クライアントの手動登録のいずれも対象外です。代わりに `COPILOT_MCP_` プレフィックス付きのリポジトリシークレットと、静的な Bearer ヘッダーを使用します。

```json
{
  "mcpServers": {
    "kuroco": {
      "type": "http",
      "url": "https://your_site_key.g.kuroco.app/rcms-api/{api_id}/mcp",
      "headers": {
        "Authorization": "Bearer $COPILOT_MCP_KUROCO_TOKEN"
      }
    }
  }
}
```

この方式を使うには、対象 API のセキュリティを OAuth ではなく **静的アクセストークン** または **特権付き静的トークン**（[認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/) を参照）に設定する必要があります。

公式ドキュメント:
- [Extending Copilot coding agent with MCP](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp)

## カスタム実装

### Python / TypeScript / その他

公式の MCP SDK が提供する OAuth クライアントのサポートを利用してください（多くの SDK が PKCE 付き認可コードフローを実装しており、任意の `client_id` を指定できます）。

#### CIMD

クライアントが CIMD に対応している場合は、HTTPS の URL に小さな JSON ドキュメントをホストし、その URL を `client_id` として使用します。対象の Kuroco の認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化してください。

#### クライアントの手動登録

クライアントの手動登録を利用する場合は、Kuroco にクライアントを登録し（[クライアントを手動登録する方法](#クライアントを手動登録する方法) を参照）、発行された `client_id`／`client_secret` と、認可サーバーのメタデータ URL に記載された認可／トークンエンドポイントをクライアントに設定してください。

Kuroco は RFC 7591 の DCR を実装していないため、`POST /register` に依存するカスタムクライアントは Kuroco に対して動作しません。

## 関連ドキュメント
- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)
- [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/)
- [静的アクセストークンによるAPIアクセス制限の方法](/ja/docs/tutorials/restricting-api-access-with-statictoken/)
- [API セキュリティ](/ja/docs/management/api-security/)


---

# 認証ヘッダーによる MCP クライアント設定リファレンス

> 元ページ: `reference/mcp-client-configuration-authentication-header` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/mcp-client-configuration-authentication-header/
> 概要: 認証ヘッダーを使って Kuroco の MCP エンドポイントを主要な MCP クライアントへ接続するための設定手順です。

**OAuth 2.0 は、MCP クライアントを Kuroco に接続する際のデフォルトかつ推奨の認証方式です** — 主要なリファレンスは [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) を参照してください。

このページでは、リクエストヘッダー（`X-RCMS-API-ACCESS-TOKEN`）による認証方法のみを取り上げます。OAuth を利用できないクライアントの場合や、あえてアクセストークンをヘッダーに設定して認証したい場合に利用できます。

以下の例に登場する `https://your-kuroco-domain.com/rcms-api/{api_id}/mcp` は、実際の Kuroco MCP エンドポイントに置き換えてください。

:::caution
このページの方式は、コンテンツ API の MCP サーバー（`/rcms-api/{api_id}/mcp`）専用です。Admin MCP サーバー（`/direct/rcms_api/admin_mcp/`）は `X-RCMS-API-ACCESS-TOKEN` ヘッダーによる認証を受け付けません。静的アクセストークン・特権付き静的トークンでは接続できず、OAuth のアクセストークン（Bearer）または管理セッションのみが利用できます。詳細は [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/#admin-mcp-サーバ) を参照してください。
:::

実装全体のチュートリアルは以下を参照してください。
[Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)。

## 対応クライアント

### チャットベースのクライアント

| クライアント | MCP サポート | Kuroco に接続可能 | 実装タイプ | ヘッダー認証のサポート |
|--------|-------------|-------------------|-------------------|----------------------|
| Jan | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| Claude Desktop | ✅ | ✅ | 完全（読み取り/書き込み） | ❌ |
| ChatGPT（Developer mode） | ✅ | ✅ | 完全（読み取り/書き込み） | ❌ |

### コーディングアシスタント

| クライアント | MCP サポート | Kuroco に接続可能 | 実装タイプ | ヘッダー認証のサポート |
|--------|-------------|-------------------|-------------------|----------------------|
| Claude Code | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| Codex CLI | ✅ | ✅ | 完全（読み取り/書き込み） | ✅（`config.toml` 経由） |
| Cursor | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| Zed | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| GitHub Copilot Chat（VS Code） | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| GitHub Copilot coding agent | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |

### カスタム実装

| クライアント | MCP サポート | Kuroco に接続可能 | 実装タイプ | ヘッダー認証のサポート |
|--------|-------------|-------------------|-------------------|----------------------|
| Python MCP Server | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| TypeScript MCP Server | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |
| その他のカスタムクライアント | ✅ | ✅ | 完全（読み取り/書き込み） | ✅ |

**実装タイプ:**
- **完全（読み取り/書き込み）**: データ取得と変更の両方に対応した完全な MCP サポート
- **ローカルのみ**: リモート MCP 非対応

**補足:**
- この方法には、クライアントがカスタムヘッダーを設定できる必要があります。**ヘッダー認証のサポート** が ❌ のクライアントは本ページの方法を利用できません — 代わりに [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)（OAuth）を利用してください。OAuth にも対応していないクライアントについては、[公開エンドポイント](#公開エンドポイント) を参照してください。

## MCP 接続に利用する Kuroco API のセキュリティ

**ヘッダー認証のサポート** が ✅ のクライアントは、アクセストークンで保護されたエンドポイントに接続でき、読み取り・書き込み操作が可能になります。セキュリティには特権付き静的トークンの使用を推奨します。

認証を設定するには：
1. セキュリティを特権付き静的トークンに設定した Kuroco API の Swagger UI を開きます。
2. ページ右上の **Generate** をクリックし、必要な情報を入力してトークンを生成します。
3. 生成されたトークンを MCP クライアントの設定でリクエストヘッダーに指定します。

ヘッダー名は `X-RCMS-API-ACCESS-TOKEN` です。具体的な設定方法は以下の各クライアントの設定手順を参照してください。

## 公開エンドポイント

ヘッダー認証にも OAuth にも対応していないクライアントは、API のセキュリティが **なし** に設定された Kuroco の MCP エンドポイントにのみ接続できます。

:::caution
公開エンドポイントの使用は推奨しません。認証が不要なため URL が知られれば誰でも API にアクセスでき、リクエストの発信元も追跡できません。公開エンドポイントを使用する場合は、読み取り専用のエンドポイントに限定し、公開しても問題のないデータのみを対象にしてください。書き込みエンドポイントを認証なしで公開することは避けてください。
:::

## チャットベースのクライアント

### Jan

Jan は **Settings -> MCP Servers** から MCP サーバーを設定できます。

公式ドキュメント:
- [Using MCP in Jan](https://www.jan.ai/docs/desktop/mcp)

### Claude（Web / Desktop / Mobile）

Claude と Claude Desktop はヘッダー認証に対応していないため、この方法は利用できません。代わりに [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)（OAuth）を利用してください。

### ChatGPT Apps（Developer mode）

ChatGPT はヘッダー認証に対応していないため、この方法は利用できません。代わりに [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)（OAuth）を利用してください。

## コーディングアシスタント

### Claude Code

ヘッダーを指定してサーバーを追加します（`--header` は URL の**後ろ**に指定する必要があります）。

```bash
claude mcp add --transport http kuroco https://your-kuroco-domain.com/rcms-api/{api_id}/mcp --header "X-RCMS-API-ACCESS-TOKEN: your-token"
```

プロジェクトスコープで共有する場合:

```bash
claude mcp add --scope project --transport http kuroco https://your-kuroco-domain.com/rcms-api/{api_id}/mcp --header "X-RCMS-API-ACCESS-TOKEN: your-token"
```

公式ドキュメント:
- [Claude Code MCP](https://docs.claude.com/en/docs/claude-code/mcp)

### Codex CLI

`codex mcp add` の CLI にはカスタムヘッダーオプションがないため、サーバー追加後に `~/.codex/config.toml` を編集してヘッダーを設定します。

```toml
[mcp_servers.kuroco]
url = "https://your-kuroco-domain.com/rcms-api/{api_id}/mcp"
enabled = true

[mcp_servers.kuroco.http_headers]
"X-RCMS-API-ACCESS-TOKEN" = "your-token"
```

環境変数からトークンを読み込む場合は `env_http_headers` を使用します:

```toml
[mcp_servers.kuroco]
url = "https://your-kuroco-domain.com/rcms-api/{api_id}/mcp"
enabled = true

[mcp_servers.kuroco.env_http_headers]
"X-RCMS-API-ACCESS-TOKEN" = "KUROCO_MCP_TOKEN"
```

```bash
export KUROCO_MCP_TOKEN="your-token"
```

公式ドキュメント:
- [Model Context Protocol – Codex](https://developers.openai.com/codex/mcp)

### Cursor

`mcp.json` にアクセストークンをヘッダーとして設定します。

```json
{
  "mcpServers": {
    "kuroco": {
      "url": "https://your-kuroco-domain.com/rcms-api/{api_id}/mcp",
      "headers": {
        "X-RCMS-API-ACCESS-TOKEN": "your-token"
      }
    }
  }
}
```

公式ドキュメント:
- [Cursor MCP docs](https://docs.cursor.com/context/mcp)

### Zed

`settings.json` にアクセストークンをヘッダーとして設定します。

```json
{
  "context_servers": {
    "kuroco": {
      "url": "https://your-kuroco-domain.com/rcms-api/{api_id}/mcp",
      "headers": {
        "X-RCMS-API-ACCESS-TOKEN": "your-token"
      }
    }
  }
}
```

公式ドキュメント:
- [Zed MCP docs](https://zed.dev/docs/ai/mcp)

### GitHub Copilot Chat（VS Code）

VS Code の MCP 設定（`mcp.json`）で、アクセストークンをヘッダーとして指定します。

```json
{
  "servers": {
    "kuroco": {
      "type": "http",
      "url": "https://your-kuroco-domain.com/rcms-api/{api_id}/mcp",
      "headers": {
        "X-RCMS-API-ACCESS-TOKEN": "your-token"
      }
    }
  }
}
```

公式ドキュメント:
- [Using MCP with GitHub Copilot](https://docs.github.com/copilot/how-tos/context/model-context-protocol)
- [VS Code MCP configuration reference](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration)

### GitHub Copilot coding agent

Copilot coding agent はリポジトリ設定で MCP ツールを利用できます。トークンは `COPILOT_MCP_` プレフィックス付きのリポジトリシークレットに保存し、ヘッダーとして渡します。

```json
{
  "mcpServers": {
    "kuroco": {
      "type": "http",
      "url": "https://your-kuroco-domain.com/rcms-api/{api_id}/mcp",
      "headers": {
        "X-RCMS-API-ACCESS-TOKEN": "$COPILOT_MCP_KUROCO_TOKEN"
      }
    }
  }
}
```

公式ドキュメント:
- [MCP and Copilot coding agent](https://docs.github.com/en/copilot/concepts/coding-agent/mcp-and-coding-agent)
- [Extending Copilot coding agent with MCP](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp)

## カスタム実装

### Python / TypeScript / その他

- Python: 公式の MCP Python SDK で HTTP サーバーを公開し、そのエンドポイントを MCP クライアントに登録します。
- TypeScript: HTTP トランスポート対応の MCP SDK でサーバーを公開し、そのエンドポイントを MCP クライアントに登録します。
- その他の言語: HTTP MCP サーバーを実装し、クライアントから `https://your-kuroco-domain.com/rcms-api/{api_id}/mcp` を参照させます。


---

# MCP サーバ リファレンス

> 元ページ: `reference/mcp-server` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/mcp-server/
> 概要: Kuroco が提供する 2 種類の MCP サーバ（クライアント API MCP サーバ / Admin MCP サーバ）のエンドポイント、認証方式、ツール構成をまとめたリファレンスです。

Kuroco は Model Context Protocol (MCP) のサーバを 2 系統提供しています。このページでは、それぞれのエンドポイントと認証方式、ツールの構成をまとめます。

| サーバ | エンドポイント | 用途 |
|------|--------------|------|
| クライアント API MCP サーバ | `/rcms-api/{id}/mcp` | Client API のエンドポイントを MCP ツールとして公開します。 |
| Admin MCP サーバ | `/direct/rcms_api/admin_mcp/` | Admin API と同等の管理操作を MCP ツールとして公開します。 |

MCP クライアント側（Claude Code、Claude Desktop、Cursor など）の設定方法は [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) を参照してください。

## クライアント API MCP サーバ

API 単位で提供される MCP サーバです（例: `https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp`）。エンドポイントごとに MCP 設定（ツール名 / 入力データ定義 / ステータス）を有効化すると、そのエンドポイントが MCP ツールとして公開されます。

設定手順の詳細は [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) を参照してください。

### 認証

接続方法は API のセキュリティ設定に従います。

| API のセキュリティ | 接続方法 |
|------------------|---------|
| None | MCP サーバの URL のみで接続できます（認証なし）。 |
| 静的トークン / 特権付き静的トークン | `X-RCMS-API-ACCESS-TOKEN` ヘッダーにトークンを設定します。ヘッダー認証に対応したクライアントが必要です。 |
| 動的アクセストークン / Cookie | OAuth 認証で接続します（OAuth Authorization Server、用途 = API）。Claude.ai のコネクタ機能などが対応しています。 |

動的アクセストークン / Cookie の場合、このMCPサーバのリソース識別子（RFC 8707 の `resource`）は MCP サーバの URL です。アクセストークンはこの識別子に拘束されます。

```
{API ドメイン}/rcms-api/{id}/mcp
```

`401` レスポンスには RFC 6750 準拠の `WWW-Authenticate` チャレンジが含まれ、`resource_metadata` で次のメタデータ文書（RFC 9728 Protected Resource Metadata）を案内します。MCP サーバの URL からメタデータ文書の URL を導出するクライアントも、同じ URL に到達します。

```
{API ドメイン}/.well-known/oauth-protected-resource/rcms-api/{id}/mcp
```

認証不要の公開エンドポイントで、MCP クライアントは事前認証なしで Authorization Server を発見できます。`/rcms-api/{id}/mcp?MODE=protected_resource_metadata` 経由でも到達可能です。

:::note
同じ API の REST エンドポイント（`/rcms-api/{id}`）は別の OAuth リソースです。MCP サーバ用に取得したトークンで REST を呼び出すことはできません（逆も同様です）。
:::

:::caution
認証なしの公開エンドポイントは本番運用では推奨されません。詳細は [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/#mcp-接続に利用する-kuroco-api-のセキュリティ) を参照してください。
:::

OAuth 認証を利用した Claude.ai コネクタの登録手順は [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/) を参照してください。

## Admin MCP サーバ

Admin API と同等の管理操作を、JSON-RPC 2.0 ベースの **MCP サーバ** として `/direct/rcms_api/admin_mcp/` から提供しています。MCP 対応クライアントは、後述するモジュールスコープ付き URL（例: `/direct/rcms_api/admin_mcp/x/all`）を登録するだけで利用できます。

### 認証

認証方式は、リクエストに含まれる資格情報によって切り替わります。

| 資格情報 | 方式 | 補足 |
|------|------|------|
| Bearer トークン（`Authorization` ヘッダ） | OAuth アクセストークン | OAuth Authorization Server（用途 = AdminMCP）が発行するアクセストークンのみを受け付けます。トークンは RFC 8707 準拠で、アクセス先のスコープ付き URL（`/x/...`）に audience 拘束されます。OAuth の認可フローを対話的に実行できない CI や無人エージェントには `client_credentials` グラントを利用します。 |
| Bearer トークンなし（管理画面ドメインからのアクセス） | 管理セッション Cookie | 管理画面と同じログインセッションを利用します。 |

`401` レスポンスには RFC 6750 準拠の `WWW-Authenticate` チャレンジが含まれ、`resource_metadata` でアクセスしたスコープ付き URL に対応するメタデータ文書（RFC 9728 Protected Resource Metadata）を案内します。

```
/.well-known/oauth-protected-resource/direct/rcms_api/admin_mcp/x/all
```

メタデータ文書はスコープ付き URL ごとに配信されます（上記は `/x/all` の例）。認証不要の公開エンドポイントで、MCP クライアントは事前認証なしで Authorization Server を発見できます。`?MODE=protected_resource_metadata` 経由でも到達可能です。

#### OAuth スコープ

アクセストークンには、実行できる操作の種別を表すスコープを付与します。「どのモジュールを操作できるか」はスコープではなく、トークンの audience（`/x/...` のバンドル URL）で決まります。

| スコープ | 実行できる操作 |
|---------|--------------|
| `mcp:tools.read` | 参照系ツールの実行と `tools/list` |
| `mcp:tools.write` | 更新系ツールの実行と `tools/list`（参照系も実行できます） |
| `mcp:admin` | すべてのツールの実行。トークンを発行するツールはこのスコープでのみ利用できます。 |
| `mcp:tools.list` | `tools/list` のみ（ツールは実行できません） |

- `401` の `WWW-Authenticate` チャレンジには、アクセス先のバンドルに必要なスコープが含まれます。`/readonly` のバンドルでは更新系のスコープを要求しません。
- スコープが不足している場合は `403`、`WWW-Authenticate` の `error="insufficient_scope"`、および JSON-RPC のエラーを返します。
- `mcp:admin` を持たないトークンは、上記のいずれかのスコープが少なくとも 1 つ必要です。`openid` のみのトークンはどのツールにも到達しません。
- 管理セッション Cookie での接続は、スコープによる制限を受けません（管理者の権限に従います）。

### IP アドレスによるアクセス制限

Admin MCP エンドポイントは、管理画面や KurocoFiles の IP アドレス制限の対象外です（送信元 IP アドレスが一定しないクラウド型の MCP クライアントに対応するため）。ネットワークで接続元を限定する場合は、Admin MCP 専用の許可 IP リストを有効にします。

設定箇所は [環境設定] -> [管理画面] の「Admin MCPのアクセス制限(IPアドレス)」です。[有効にする]にチェックを入れ、許可する IP アドレスを 1 行に 1 つ入力します。CIDR 表記、`#コメント`、`[[IPSETS_*]]` 定数を利用できます。設定手順は [管理画面](/ja/docs/management/management-screen/) を参照してください。

適用範囲と挙動は次のとおりです。

| 項目 | 内容 |
|------|------|
| 対象 | Admin MCP エンドポイント（`/direct/rcms_api/admin_mcp/`、モジュールスコープ付き URL と `?MODE=tools` を含む）、およびファイルアップロード用エンドポイント（`/direct/rcms_api/mcp_upload/`）。 |
| 対象の認証経路 | Bearer トークン（OAuth アクセストークン）と管理セッション Cookie の両方。 |
| 対象外 | `?MODE=protected_resource_metadata`（RFC 9728 のメタデータ配信）。認証不要の公開エンドポイントのまま維持されます。 |
| 判定タイミング | 認証よりも前に判定されます。許可されない IP アドレスからのリクエストは、トークンの正否にかかわらず `403` を返します。 |
| 拒否時のレスポンス | `403` と JSON-RPC のエラーボディ（`Access from this IP address is not allowed.`）。 |
| 無効時の挙動 | [有効にする]が OFF の場合、またはリストが空（コメント行のみの場合を含む）の場合は制限しません。既定では制限なしです。 |
| 定数の展開結果が空の場合 | 許可 IP が 1 件も得られないため、すべてのリクエストを拒否します（未定義の `[[IPSETS_*]]` を指定した場合など）。 |

:::note 管理画面の IP アドレス制限との関係
「管理画面のアクセス制限(IPアドレス)」は Admin MCP エンドポイントには適用されません。ただし、OAuth の認可コードフロー（`authorization_code`）と管理セッション Cookie の利用では、途中で管理画面のログイン・同意画面を経由するため、その画面が「管理画面のアクセス制限(IPアドレス)」の対象になります。<br/>
`client_credentials` によるトークン取得、リフレッシュトークンによる更新、および発行済みトークンでの Admin MCP 呼び出しは、「管理画面のアクセス制限(IPアドレス)」の対象外です。これらも含めて接続元を限定する場合に「Admin MCPのアクセス制限(IPアドレス)」を利用します。
:::

:::caution
この制限は、管理画面内の AI エージェント機能（[AIエージェントアシスト](/ja/docs/management/ai-agent-assist/) など）による Admin MCP へのアクセスにも適用されます。リストに含まれていない IP アドレスから管理画面を利用している管理者は、自分の IP アドレスを追加するまで、これらの機能を利用できません。<br/>
[環境設定] -> [管理画面] の画面自体はこの制限の対象外のため、設定の変更・解除は引き続き可能です。
:::

### モジュールスコープ付き MCP サーバ

`/admin_mcp/` 以降のパスセグメントで、1 つの MCP サーバ（=1 認証情報）に複数の管理モジュールをバンドルできます。GitHub MCP の `/x/<csv>/readonly` パターンに準拠しています。

```
POST /direct/rcms_api/admin_mcp/x/all                                # 全ツール
POST /direct/rcms_api/admin_mcp/x/topics_group_1,topics_group_5,member,services
POST /direct/rcms_api/admin_mcp/x/topics_group_1,topics_group_5/readonly
POST /direct/rcms_api/admin_mcp/x/topics_group                       # グループ定義 CRUD
```

:::caution
スコープ指定（`/x/...`）は必須です。ベース URL（`/direct/rcms_api/admin_mcp/`）への直接のリクエストは `400` で拒否されます。全ツールを利用する場合も `/x/all` を明示してください。
:::

認識される CSV エントリ（AI エージェント設定の「公開モジュール」と同じ識別子）:

| エントリ | 意味 |
|---------|------|
| `topics_group_<N>` | `topics_group_id = N` にスコープした topics レコード操作。各ツールの `topics_group_id` 引数は enum として制約され、許可外グループへの呼び出しは拒否されます。 |
| `topics` | グループ制約なしの同等表現。discovery 専用で、ツール呼び出しは拒否されます。 |
| `topics_group` | グループ定義の管理（`t_topics_group` の CRUD）。 |
| `services` | サービスモデル（Email、Slack など）。 |
| `<mt>` | その他任意の管理モジュール（`member`、`ec`、`batch` など）。 |
| サブモジュール | 1 つのモジュールの一部のコントローラだけを公開する識別子（`site_management_plugin`）。アクセス範囲だけが変わり、ツール名は `<mt>` 指定時と同じです。 |

モジュール指定時の挙動:

- 更新系の操作は、操作ごとに個別のツールになります（追加 / 更新 / 削除など）
- レコードが 1 件も無いモジュールでは、参照系のツールが表示されません（追加のツールのみが表示されます）

パスに `/readonly` を付与すると、書き込み系ツールはリストから除外されます。

### モジュール一覧（REST）

スコープ指定（`/x/...`）なしのベース URL で利用できます（認証は必要です）。

```
GET /direct/rcms_api/admin_mcp/?MODE=tools
```

レスポンス:

```json
{
  "modules": [
    {"module": "topics",   "type": "topics",     "tool_count": 8, "label": "...", "description": "..."},
    {"module": "member",   "type": "controller", "tool_count": 5, "label": "...", "description": "..."},
    {"module": "services", "type": "service",    "tool_count": 4, "label": "...", "description": "..."}
  ]
}
```

`type` は `topics`（topics レコード操作）、`topics_group_admin`（グループ定義管理）、`controller`（一般の管理モジュール）、`service`（サービスモデル）のいずれかです。各エントリにはモジュールの表示名（`label`）と説明（`description`）が含まれ、`topics` のエントリには選択可能なグループの一覧（`groups`）も含まれます。

### MCP プロトコル

HTTP POST + JSON-RPC 2.0。`initialize` で交渉するプロトコルバージョンは `2025-11-25` / `2025-06-18` / `2025-03-26` に対応しています。

サポートメソッド:

| メソッド | 説明 |
|---------|------|
| `initialize` | ハンドシェイク・プロトコルバージョン交渉 |
| `notifications/initialized` | クライアント準備完了通知 |
| `ping` | 接続確認 |
| `tools/list` | 利用可能な管理ツール一覧（モジュールスコープ反映） |
| `tools/call` | 名前指定で管理ツールを実行 |
| `prompts/list` | 空の一覧を返します（プロンプトは提供していません） |
| `resources/list` | 空の一覧を返します（リソースは提供していません） |

ツール名は `{resource}-{verb}` の形式です。リソースは操作対象のレコード種別を表し、モジュール名とは一致しないことがあります（例: `site` モジュールには `kuroco_front`、`usage`、`const` などのリソースが含まれます）。ハイフンはリソースと動詞の区切りとして 1 つだけ使われ、リソース名の中の区切りはアンダースコアのままです（`topics_group-create`）。

| 動詞 | 操作 | 例 |
|------|------|-----|
| `-list` | 一覧・検索 | `topics-list` |
| `-get` | ID 指定で 1 件取得 | `topics-get` |
| `-create` | 追加 | `topics-create` |
| `-update` | 更新（1 件、または `ids` / `filter` で複数件） | `topics-update` |
| `-delete` | 削除（同上） | `topics-delete` |
| `-validate` | 保存せず入力チェックのみ実行 | `topics-validate` |
| `-import` | CSV や行データの取り込み | `topics-import` |
| `-export` | ダウンロード | `topics-export` |
| その他の管理操作 | 管理操作の名称がそのまま動詞になります | `topics-accept` |
| サービスメソッド | `{service}-{method}` | `email-send` |

固定名のツールが 2 つあります。`topics-describe`（コンテンツ定義の構造を返します）と `files-create_upload`（[ファイルのアップロード](#ファイルのアップロード)を参照）です。

対象件数（1 件 / 複数）や実行方法（同期 / ジョブ）はツール名ではなく引数で指定します。このため一括処理は専用のツール名（`bulk_delete` など）を持ちません。`{resource}-delete` / `{resource}-update` では引数で対象（`ids` または `filter`）を選択し、ガードとして `dry_run` / `expected_cnt` を指定できます。ジョブ実行に対応するツールでは `async` 引数で同期実行とジョブ実行を切り替えます（`{resource}-import` など）。

実際のツール一覧はモジュールが公開するコントローラに依存します。スコープ URL に対して JSON-RPC の `tools/list` を発行して列挙してください。

呼び出し例:

```http
POST /direct/rcms_api/admin_mcp/x/topics_group_1
Authorization: Bearer <token>
Content-Type: application/json

{"jsonrpc":"2.0","method":"tools/call",
 "params":{"name":"topics-create",
           "arguments":{"subject":"Hello","topics_group_id":1}},
 "id":3}
```

### ファイルのアップロード

コンテンツの画像・ファイル項目に大きなファイルを設定する場合は、`files-create_upload` ツールでアップロード先を発行し、本文とは別にアップロードします。小さなファイルは `data:` URI としてそのまま値に渡すこともできます。

1. `files-create_upload` を呼び出すと、不透明な参照（`file_ref`、`kuroco-file:` で始まる文字列）とアップロード先（`upload.method` = `PUT`、`upload.url`）が返ります。
2. `upload.url` にファイルのバイト列を `PUT` します。`upload.url` が `307` を返す場合は、`GET` でリダイレクト先（`Location`）を解決してから、その URL に `PUT` してください。リダイレクトする URL 自体への `PUT` はエッジで `405` になります。
3. `topics-create` / `topics-update` の画像・ファイル項目の値に `file_ref` を渡します（`{"file_id": "kuroco-file:...", "desc": "キャプション"}` の形式も利用できます）。

アップロード先は環境によって異なります。S3 の一時バケットが構成されている場合は S3 の presigned URL（短縮 URL の場合は上記の `307` 解決が必要）、構成されていない場合は Kuroco の以下のエンドポイントです。参照はアカウントに紐づき、有効期限があります。

```
PUT /direct/rcms_api/mcp_upload/<token>
```

:::note
`files-create_upload` は、コンテンツのレコード操作ツールを含むバンドルにのみ表示されます。`/readonly` のバンドルでは表示されません。
:::

### OpenAPI 定義の取得

`api-export_openapi` ツールで、エンドポイント定義を OpenAPI 形式（OpenAPI 3.1.0）で取得できます。管理画面の [OpenAPIエクスポート](/ja/docs/management/api-list/#openapiエクスポートする)と同じ内容を、Swagger UI やブラウザを経由せずに取得できます。

読み取り系のツールのため、`mcp:tools.read` スコープと `/readonly` のバンドルでも実行できます。`rcms_api` モジュールを含むバンドルで公開されます。

| パラメータ | 型 | 必須 | 内容 |
|---------|-----|-----|------|
| `api_id` | integer | 必須 | 対象 API の ID |
| `format` | string | 任意 | 出力形式。`json`（既定）または `yaml`。 |

戻り値は `format` と `openapi_data` を含みます。`format` が `json` の場合、`openapi_data` は構造化されたオブジェクトです。`yaml` の場合は文字列です。存在しない `api_id` を指定した場合はエラーを返します。

呼び出し例:

```http
POST /direct/rcms_api/admin_mcp/x/rcms_api/readonly
Authorization: Bearer <token>
Content-Type: application/json

{"jsonrpc":"2.0","method":"tools/call",
 "params":{"name":"api-export_openapi",
           "arguments":{"api_id":1,"format":"json"}},
 "id":4}
```

### 制限事項

MCP クライアントは 1 つの指示を複数のツール呼び出しに展開し、それらを並列で送信することがあります。管理操作 1 件はレコード保存に加えて検索インデックス更新・キャッシュパージ・トリガー処理を伴うため、並列送信をそのまま受け付けると同一インスタンスで配信している公開サイトまで遅くなります。これを防ぐために、以下の上限が設けられています。

いずれの上限も認証方式（OAuth アクセストークン／管理画面のセッションクッキー）にかかわらず適用されるため、[AIエージェントアシスト](/ja/docs/management/ai-agent-assist/) など管理画面内から Admin MCP を利用する機能も対象です。

#### 書き込みリクエストのレート制限

| 項目 | 内容 |
|------|------|
| 上限 | 2 秒あたり 8 リクエスト（サイト単位） |
| 対象 | 書き込み系ツールの `tools/call`。Admin API（`/direct/rcms_api/admin_api/`）の書き込みリクエストと共通の枠で数えます。 |
| 対象外 | 読み取り系ツールの `tools/call`、および `initialize` / `tools/list` / `ping` などのメソッド。接続直後のツール一覧取得や参照系の呼び出しは、この書き込みレート制限では数えません（Kuroco 全体の[同時接続数の制限](/ja/docs/reference/limitations-in-kuroco/#同時接続数)は別途適用されます）。 |
| 超過時の応答 | HTTP `429` と `Retry-After` ヘッダ、および JSON-RPC エラー。エラーメッセージにも再試行可能になるまでの秒数が含まれます。 |
| 対処 | 書き込みを並列化せず 1 件ずつ送信します。同種の更新をまとめる場合は、`{mt}-delete` / `{mt}-update` に `ids` または `filter` を指定して 1 回の呼び出しで処理します。 |

:::caution
判定は「その 2 秒間に受け付けた書き込みリクエスト数」で行われます。数件の書き込みを並列で送る程度であれば通りますが、9 件目以降は `429` になります（平均すると 1 秒あたり 4 リクエストが上限です）。`429` を受け取ったクライアントは `Retry-After` に従って再試行してください（待ち時間は最大 2 秒です）。
:::

#### 一括操作の 1 リクエスト上限

| 項目 | 内容 |
|------|------|
| 同期実行 | 1 回の呼び出しで 200 件まで |
| 非同期実行（`async=true` でジョブとして登録） | 1 ジョブで 100,000 件まで |
| 超過時 | エラーを返します。同期実行で 200 件を超える場合は `async=true` の指定、または呼び出しの分割が必要です。 |

CSV ファイルの取り込みも同じ件数で判定され、上限を超えるファイルは 1 行も取り込まずにエラーになります。

#### 処理時間の通知

1 回のツール呼び出しに 1,000ms を超える時間がかかった場合、ツール実行結果に処理時間と対処の指針が追記されます。エラーではありませんが、書き込みの並列送信を控える、取得する項目や件数を絞るなどの対処を検討してください。

#### ログ参照ツールの上限

| 項目 | 内容 |
|------|------|
| 参照可能な期間 | 直近 12 時間（`timestamp_start` は必須で、12 時間より前を指定するとエラー） |
| 呼び出し間隔 | 管理ユーザー単位で 5 秒に 1 回 |

**API 解析（`api_analytics-list`）はこの上限の対象外です。** エンドポイント単位に集計した結果を返すため、
期間を延ばしても応答の行数が増えないためです。代わりに 1 回の指定範囲は最大 35 日で、
`timestamp_end` と `timestamp_start` の差が 35 日を超えるとエラーになります。

長期間の傾向を調べる場合は、生ログのツール（`api_log-list` など）ではなく API 解析を利用してください。
生ログのツールは、集計では説明できない挙動を個別のリクエスト単位で確認する用途に向いています。

#### MCP から変更できない設定

エンドポイントのキャッシュ設定（キャッシュ期間など）は Admin MCP のツールでは変更できません。
`api_uri-upsert` のスキーマに該当のパラメータが含まれていないため、指定するとエラーになります。
キャッシュ期間の変更は[管理画面のエンドポイント設定](/ja/docs/reference/api-cache/#キャッシュ期間の設定方法)から行ってください。

:::caution 課金対象
Admin MCP（`/direct/rcms_api/admin_mcp/`）へのリクエストは、通常の API リクエストと同様に**リクエストごとの課金対象**です。意図しない書き込みトラフィックを抑えるには、モジュールスコープ付き URL と `/readonly` の活用を推奨します。
:::

:::note Client CLI
Client API に CLI ベースでアクセスする場合は、別途 Client CLI（`kuroco-client`）も利用可能です。
詳細は [Kuroco AI アーキテクチャ](/ja/docs/tutorials/kuroco-skills-overview/#kuroco-ai-アーキテクチャ) を参照してください。
:::

## MCP 動作改善フィードバック

クライアント API MCP サーバと Admin MCP サーバの initialize レスポンス（instructions）には、AI クライアントが MCP ツール自体の不具合・改善要望を Kuroco 開発チームへ報告するための送信手順が含まれます。ツールの説明が分かりにくい、入力スキーマが実際の挙動と一致しない、想定外のエラーが発生した、といった問題を AI クライアントが作業中に検知した場合、Kuroco が用意した専用のフィードバック API へ報告します。報告は Kuroco 開発チームに届き、MCP の改善に利用されます。

報告に含まれる項目は次のとおりです。

| 項目 | 内容 |
|------|------|
| 件名（必須） | 問題・要望の要約 |
| 詳細（必須） | 現在の挙動、期待する挙動、再現手順 |
| 対象 MCP ツール名 | 例: `topics-list` |
| 利用クライアント | 例: Claude Code |
| 利用モデル | 例: claude-fable-5 |
| メールアドレス | 返信を希望する場合のみ |

instructions には、AI クライアントに対する次の制約が明記されています。

- 報告を送信する前に、必ず報告内容をユーザーに提示して承認を得ること。サイレントに送信してはならない
- メールアドレスは、ユーザーが返信を希望して共有に同意した場合のみ送信すること
- それ以外のユーザーのデータや秘密情報を報告に含めないこと

### 有効/無効の切り替え

デフォルトは有効です。次のいずれかの画面で切り替えられます。

- [環境設定] -> [サイト管理]（`/management/site/site_edit/`）の「MCP動作改善フィードバック」チェックボックス
- Admin MCP 設定画面（`/management/rcms_api/admin_mcp_info/`）の「MCP動作改善フィードバック」カードの切り替えボタン

無効にすると、両 MCP サーバの instructions からフィードバック送信手順が除外されます。

## 関連ドキュメント

- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) - クライアント API MCP サーバの設定手順
- [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) - クライアント別の接続設定
- [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/) - OAuth 認証での接続手順
- [Kuroco Skills リファレンス](/ja/docs/reference/kuroco-skills-detail/) - Kuroco Skills 各スキルの詳細


---

# OAuth Authorization ServerのOpenID Connect対応

> 元ページ: `reference/oauth-authorization-server-openid-connect` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/oauth-authorization-server-openid-connect/

OAuth Authorization Serverでサインイン用スコープ（`openid` / `profile` / `email`）を許可すると、この認可サーバーはOpenID Connectの認可サーバーとして、メンバーのサインイン情報（claim）をクライアントに連携します。付与されたスコープに`openid`が含まれる場合にのみ、id_tokenの発行とuserinfoエンドポイントでのclaim取得が有効になります。

OAuth Authorization Serverの設定方法は[OAuth Authorization Server](/ja/docs/management/sso-oauth-idp/)を参照してください。

## 基本情報

| 項目 | 内容 |
| :--- | :--- |
| 種別 | OpenID Connect（id_token / userinfo / JWKS） |
| 対象 | OAuth Authorization Server（用途が`API` / `Management` / `AdminMCP`のいずれか） |
| 利用場面 | OAuthクライアントがメンバーのサインイン情報（claim）を取得する場合 |

## メタデータ

OAuth Authorization Serverの編集画面の[メタデータURL]にアクセスすると、この認可サーバーの設定情報（Authorization Server Metadata）がJSON形式で返されます。`issuer`・`authorization_endpoint`・`token_endpoint`などOAuth 2.0の基本的な項目に加えて、次の項目が含まれます。

- `jwks_uri`：JWKSエンドポイントのURL
- `userinfo_endpoint`：userinfoエンドポイントのURL（発行可能なスコープに`openid`が含まれる場合）
- `subject_types_supported`
- `id_token_signing_alg_values_supported`（`RS256`）
- `claims_supported`

以降のJWKS・userinfoの各エンドポイントのURLは、このレスポンスから確認できます。

## SSOで利用する認可リクエスト <VersionLabel version="BETA" /> {#ssoで利用する認可リクエスト}

同一組織で管理するサービス間のSSOでは、OAuth Authorization Server クライアントで[信頼済みクライアント]を有効にすると、Kurocoのログインセッションを利用して同意画面を省略できます。[信頼済みクライアント]の設定方法は[OAuth Authorization Server クライアントの編集](/ja/docs/management/sso-oauth-idp/#oauth-authorization-server-クライアントの編集)を参照してください。

認可エンドポイントのURLは、メタデータの`authorization_endpoint`で確認できます。ログイン画面や同意画面を表示せずに認可できるか確認する場合は、`prompt=none`を指定します。挙動が変わる`prompt`の値は、メタデータの`prompt_values_supported`で確認できます。

```http
GET {authorization_endpoint}?response_type=code&client_id={client_id}&redirect_uri=https%3A%2F%2Fclient.example%2Fcallback&scope=openid+profile+email&state={state}&nonce={nonce}&code_challenge={code_challenge}&code_challenge_method=S256&prompt=none
```

`scope`内のスコープは空白または`+`で区切り、`prompt`など別のパラメータとは`&`で区切ります。

### `prompt`による挙動

| `prompt` | ログインセッションなし | ログイン済み・信頼済みクライアント | ログイン済み・その他のクライアント |
| :--- | :--- | :--- | :--- |
| 指定なし | ログイン画面を表示します。 | 同意画面を表示せず、認可コードを発行します。 | 同意画面を表示します。 |
| `none` | 画面を表示せず、`login_required`を返します。 | 同意画面を表示せず、認可コードを発行します。 | 画面を表示せず、`consent_required`を返します。 |
| `consent` / `login` / `select_account` / その他の値 | ログイン後に同意画面を表示します。 | 同意画面を表示します。 | 同意画面を表示します。 |

`none`以外の値は、ユーザーの操作を要求するものとして扱われるため、信頼済みクライアントでも同意画面を表示します。メタデータの`prompt_values_supported`で公開しているのは`none`と`consent`のみで、`prompt=login`でログイン済みユーザーの再認証は行わず、`prompt=select_account`でアカウント選択画面は表示しません。

`prompt=none`は他の値と同時に指定できません。`none consent`のように組み合わせた場合は`invalid_request`を返します。また、ログイン済みのアカウントが認可の対象外の場合は`access_denied`を返します。

:::caution
[信頼済みクライアント]は、自社・同一組織で管理するクライアントにのみ使用してください。同意画面は省略されますが、リダイレクトURI、スコープ、リソース、PKCEなどの検証は通常どおり行われます。
:::

## id_token

トークンエンドポイントは、認可コード・リフレッシュトークン・クライアント認証情報などをアクセストークンに交換するためのエンドポイントです（URLはメタデータの`token_endpoint`で確認できます）。付与されたスコープに`openid`が含まれる場合、このエンドポイントのレスポンスに、アクセストークンに加えてRS256で署名されたid_token（JWT）が含まれます。

id_tokenには、常に`iss`（発行元）・`sub`（メンバーID）・`aud`（クライアントID）・`iat`・`exp`が含まれ、認可リクエストで`nonce`が指定された場合は`nonce`も含まれます。認証時刻を特定できる場合は`auth_time`も含まれます。[信頼済みクライアント]が既存のログインセッションを利用して同意画面を省略した場合、`auth_time`は含まれません。`profile`・`email`スコープに応じて追加されるclaimは、[スコープとclaimの対応](#スコープとclaimの対応)を参照してください。

## JWKSエンドポイント

id_tokenの署名を検証するための公開鍵を、JWK Set形式（RFC 7517）で配信します。エンドポイントのURLはメタデータの`jwks_uri`で確認できます。署名鍵は認可サーバーごとに管理され、初回アクセス時に生成されます。

## userinfoエンドポイント

アクセストークンを用いて、メンバーのclaimを取得できます。

| 項目 | 内容 |
| :--- | :--- |
| メソッド | `GET` / `POST` |
| 認証 | `Authorization: Bearer <access_token>`ヘッダーで認証します（クエリパラメータでのアクセストークン指定には対応していません）。 |
| レスポンス | 付与されたスコープに応じたclaim（必ず`sub`を含む）をJSON形式で返します。 |

エンドポイントのURLは、メタデータの`userinfo_endpoint`で確認できます。

## スコープとclaimの対応

付与されたスコープに応じて、id_tokenおよびuserinfoで返されるclaimが決まります。

| スコープ | claim | 取得元 |
| :--- | :--- | :--- |
| `openid` | `sub` | メンバーID |
| `profile` | `name` | 氏名（姓 + 名） |
| `profile` | `family_name` | 姓 |
| `profile` | `given_name` | 名 |
| `profile` | `preferred_username` | ログインID |
| `profile` | `updated_at` | メンバー情報の更新日時（Unixタイム） |
| `email` | `email` | メールアドレス |
| `email` | `email_verified` | 常に`true`（Kurocoはメールアドレスの検証フローを持たないため、固定値です） |

## 同意画面での共有情報

`openid`を含むスコープが要求された場合、同意画面には、クライアントに共有されるサインイン情報（claimの実際の値）が「共有される情報」として表示されます。スコープ名だけでなく、実際に連携されるメンバー情報を確認したうえで許可できます。

<!-- TODO: スクリーンショット: 同意画面の「共有される情報」セクション -->

## 関連ドキュメント

- [OAuth Authorization Server](/ja/docs/management/sso-oauth-idp/)
