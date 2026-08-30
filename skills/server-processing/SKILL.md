---
name: kuroco-server-processing
metadata:
  author: Diverta inc.
  version: "1.5.0"
  lastUpdated: "2026-08-27"
description: Kurocoのサーバーサイド処理リファレンスと外部連携の方式設計。Smartyテンプレートの構文と151プラグイン（api、api_internal、sendmail、slack_post_message、ai_completionなど）、バッチ処理による定期実行、スパイダー、Webhook、コンテンツ・フォーム更新時のトリガー処理、トリガーメールアドレス、Slack・Chatwork・SendGrid・GitHub Actions連携、外部システム連携方式（直接呼び出し／プロキシ／取り込み）の選定とシークレット・OAuthトークン管理・タイムアウト制約をカバー。Smarty構文やプラグインの使い方、定期実行・自動化・外部通知・カスタム処理の実装、LINE・Slack・Instagram等の外部APIとの連携方式やAPIキーの隠し方の相談で使用。
---

# Kuroco サーバーサイド処理

KurocoのSmartyテンプレートプラグインリファレンスおよびWebhook・バッチ処理パターン。

**ドキュメント参照**: `/kuroco-docs` スキルを使用してKuroco公式ドキュメントを検索・参照できます。

## 目次

### Part 1: Smartyプラグインリファレンス

- [よく使うプラグイン](#よく使うプラグイン)
- プラグイン種別（関数・修飾子・ブロック）→ [references/syntax.md](references/syntax.md#プラグイン種別)
- [カテゴリ別リファレンス](#カテゴリ別リファレンス)
- 使用例（一覧表示・Slack通知・権限表示・エラー処理・ページング）→ [references/examples.md](references/examples.md)
- [Smarty構文リファレンス](references/syntax.md) - 基本構文、制御構造、組み込み変数

### Part 2: Webhook・バッチ処理パターン

- [バッチ処理](#バッチ処理)
- [内部API呼び出し](#内部api呼び出し)
- [外部システム連携の方式設計](#外部システム連携の方式設計) → 深掘りは [references/integration-design.md](references/integration-design.md)
- [外部API呼び出し](#外部api呼び出し)
- [トリガー処理](#トリガー処理)
- Webhook（受信エンドポイント・URL 形式）→ [references/integrations.md](references/integrations.md#webhook呼び出し)
- [外部サービス連携](#外部サービス連携) → 詳細は [references/integrations.md](references/integrations.md)

---

# Part 1: Smartyプラグインリファレンス

KurocoのSmartyテンプレートで使用可能な全プラグインの完全リファレンス。

## よく使うプラグイン

### 変数・データ操作

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `assign` | 変数代入 | `{assign var="name" value="値"}` |
| `append` | 配列追加 | `{append var="arr" value="値"}` |
| `json_decode` | JSONパース | `{$json\|json_decode:true}` |
| `rcms_json_encode` | JSONエンコード | `{$arr\|@rcms_json_encode}` |

### API・データ取得

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `api_internal` | 内部API呼び出し | `{api_internal endpoint='/rcms-api/1/news' var='result'}` |
| `api_method` | エンドポイントを作らずモデルのオペレーションを直接実行（GETのみ） | `{api_method var='result' model='Topics' method='list' ...}` |
| `assign_tag_list` | タグ一覧取得 | `{assign_tag_list var='tags'}` |

→ 詳細: [references/api-plugins.md](references/api-plugins.md)

### 文字列処理

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `escape` | エスケープ | `{$html\|escape}` |
| `truncate` | 文字列切り詰め | `{$text\|truncate:100:"..."}` |
| `mb_truncate` | マルチバイト対応 | `{$text\|mb_truncate:50}` |
| `date_format` | 日付フォーマット | `{$date\|date_format:"%Y-%m-%d"}` |
| `translate` | 翻訳 | `{$key\|translate}` |
| `nl2br` | 改行をBRに | `{$text\|nl2br}` |
| `replace` | 文字列置換 | `{$text\|replace:"a":"b"}` |

→ 詳細: [references/string-plugins.md](references/string-plugins.md)

### フォーム・UI

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `fileupload` | ファイルアップロード | `{fileupload id="photo" hidden_nm="photo_url" url=$upload_url}{/fileupload}` |
| `inquiry_input` | フォーム入力 | `{inquiry_input col="name" ...}` |
| `pager` | ページネーション | `{pager info=$pageInfo}` |

→ 詳細: [references/form-plugins.md](references/form-plugins.md)

### 認証・権限

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `rcms_auth` | 権限制御ブロック | `{rcms_auth target="read:/topics/"}...{/rcms_auth}` |
| `login` | ログイン処理 | `{login ...}` |
| `logout` | ログアウト処理 | `{logout ...}` |

→ 詳細: [references/auth-plugins.md](references/auth-plugins.md)

### 外部サービス連携

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `sendmail` | メール送信 | `{sendmail to=$email subject="件名" contents="本文"}` |
| `slack_post_message` | Slack通知 | `{slack_post_message channel="#general" text="..."}` |
| `ai_completion` | AI呼び出し | `{ai_completion var='result' message=$prompt model='gpt-4'}` |
| `github_deploy` | GitHubデプロイ | `{github_deploy ...}` |

→ 詳細: [references/integration-plugins.md](references/integration-plugins.md)

### ファイル操作

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `write_file` | ファイル書き込み | `{write_file var="path" value="内容"}` |
| `put_file` | ストレージアップロード | `{put_file path="/files/..." tmp_path=$tmp}` |
| `read_file` | ファイルを1行ずつ読み込み（ブロック） | `{read_file name="log" path="/files/user/..." row="line"}{$line}{/read_file}` |
| `read_dir` | ディレクトリ読み込み | `{read_dir name="files" path="/files/user/..." file_var='file'}...{/read_dir}` |

→ 詳細: [references/file-plugins.md](references/file-plugins.md)

### Vue.js連携

| プラグイン | 説明 | 例 |
|-----------|------|-----|
| `rcms_vue_component` | Vueコンポーネント | `{rcms_vue_component config="rcms-mng" name="..."}` |
| `head_include` | headに追加 | `{head_include file="..."}` |

→ 詳細: [references/vue-plugins.md](references/vue-plugins.md)

## カテゴリ別リファレンス

| カテゴリ | ファイル | 主なプラグイン |
|---------|---------|---------------|
| **構文リファレンス** | [syntax.md](references/syntax.md) | **基本構文、制御構造、組み込み変数、ベストプラクティス** |
| API・データ取得 | [api-plugins.md](references/api-plugins.md) | api_internal, api_method, assign_tag_list |
| 文字列処理 | [string-plugins.md](references/string-plugins.md) | escape, truncate, date_format, translate |
| 配列操作 | [array-plugins.md](references/array-plugins.md) | count, in_array, implode, explode, sort系 |
| フォーム・UI | [form-plugins.md](references/form-plugins.md) | fileupload, inquiry_input, pager, html_* |
| 認証・権限 | [auth-plugins.md](references/auth-plugins.md) | rcms_auth, login, logout |
| 外部連携 | [integration-plugins.md](references/integration-plugins.md) | sendmail, slack_*, ai_completion |
| ファイル操作 | [file-plugins.md](references/file-plugins.md) | write_file, put_file, read_file, read_dir |
| Vue.js連携 | [vue-plugins.md](references/vue-plugins.md) | rcms_vue_component, head_include |
| 全プラグイン | [all-plugins.md](references/all-plugins.md) | 全151プラグイン一覧 |

# Part 2: Webhook・バッチ処理パターン

Kuroco HeadlessCMSでのWebhook、バッチ処理、外部連携に関するベストプラクティス。

> **Smarty構文について**: バッチ処理・トリガーはSmartyテンプレートで記述します。構文やプラグインの詳細は上記 Part 1 を参照してください。

## バッチ処理

### 概要

バッチ処理は一定時間ごとに自動実行される処理。

**実行頻度の選択肢:**
| 頻度 | 用途 |
|------|------|
| 15分毎 | 頻繁な同期が必要な場合 |
| 30分毎 | 準リアルタイム処理 |
| 1時間毎 | 定期的な集計・更新 |
| 毎日（指定時刻） | 日次レポート、バックアップ |

> **無料利用ユーザーの実行制限**: カード決済を選択していてカード未登録のサイトは、**バッチの起動（登録）が1時間あたり100回まで**に制限される。数えるのはバッチの起動回数で、バッチ内で発行するリクエスト数ではない（外部への `{api}` 送信は別枠で1,000回/時）。カード登録済み・請求書払いなら制限なし。
>
> **1回のバッチの実行時間上限は既定4時間、Smarty バッチは6時間**——超えるとタイムアウト失敗になる。大量データはこの枠に収めるより、後述の「タイムアウト対策」のとおりページング分割して1回を短く保つ。

### ユースケース

- 外部システムへのCSV生成・連携
- 外部システムからのデータ取り込み
- ログ集計・統計データ算出
- 定期的なメール配信
- GitHub Actions連携（デプロイトリガー）

### バッチ処理の作成

管理画面: [オペレーション] → [バッチ処理] → [追加]

| 項目 | 説明 | 例 |
|------|------|-----|
| タイトル | バッチの名前 | CSV出力バッチ |
| 識別子 | ユニークな識別子（英数字） | csv_export |
| 実行頻度 | 実行間隔 | 毎日 03:00 |
| 実行内容 | Smarty構文で記述 | 下記参照 |

## 内部API呼び出し

### 基本構文

```smarty
{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  queries=$queries
  var='response'
}
```

### コンテンツ一覧取得

```smarty
{assign var="queries" value=$dataSet.emptyArray}
{append var="queries" index="cnt" value=0}
{append var="queries" index="filter" value="topics_flg = 1"}

{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  queries=$queries
  var='news_list'
}

{foreach from=$news_list.list item="news"}
  ID: {$news.topics_id}, タイトル: {$news.subject}
{/foreach}
```

### コンテンツ作成

POSTのリクエストボディも `queries` で渡す（`body` というパラメータは存在しない）。

```smarty
{assign var="body" value=$dataSet.emptyArray}
{append var="body" index="subject" value="タイトル"}
{append var="body" index="contents" value="本文"}
{append var="body" index="open_flg" value=1}

{api_internal
  endpoint='/rcms-api/1/news/insert'
  method='POST'
  member_id=1
  queries=$body
  var='result'
}
```

更新（`/update/{topics_id}`）も同じ形で、変更するキーだけを `queries` に載せる。拡張項目は `ext_slug` 名（未設定なら `ext_1` / `ext_col_01` 形式）をキーにする——キー名の確認と `bulk_upsert` は `/kuroco-api-content` を参照。

## 外部システム連携の方式設計

外部システムと繋ぐ前に、3パターンのどれで繋ぐかを決める（選定基準は `/kuroco-app-builder` の 0-4 と共通）。

| パターン | 構成 | 向くケース |
|---------|------|-----------|
| 直接呼び出し | フロントエンドが外部APIを直接呼ぶ。Kurocoは関与しない | 外部API側がCORS許可済み・鍵をフロントに置いてよい・リアルタイム性最優先 |
| プロキシ（Kuroco経由） | カスタムエンドポイントのSmartyテンプレートから **`{api}`** プラグインで外部APIを呼び、結果を返す | 鍵を隠したい、認証/CORS/レート制限をKuroco側に一本化したい、レスポンスを加工したい |
| 取り込み | 事前に外部データをTopics/CSVテーブルへ取り込み、標準のTopics APIで提供する | 更新頻度が低い、Kurocoの標準機能（検索・キャッシュ・多言語）に外部データも乗せたい |

判断基準:
- **鍵を秘匿する必要があるか** → あるならプロキシか取り込み。直接呼び出しはフロントの JS から鍵が読めるため、非公開の鍵には使えない
- **リアルタイム性が必要か** → 必要ならプロキシ、許容できるなら取り込み
- **Kuroco の標準機能（検索・カテゴリ・キャッシュ・多言語）に外部データも乗せたいか** → 乗せたいなら取り込み
- **スパイダーは構造化 API のポーリングには向かない**（Web ページ・ファイルの巡回取り込み用で、巡回自体が課金対象のリクエストになる）。構造化 API を定期取得するなら取り込みでもバッチ処理＋`{api}` を使う
- **外部への通知送信（Slack / LINE / SMS / メール）は3パターンの外**。トリガー処理から連携プラグインを呼ぶか、トリガーメールアドレスに送るだけで済む（→ [外部サービス連携](#外部サービス連携)）

相手がREST APIなら `{api}` で「繋がるかどうか」に詰まることはまず無い。設計の重心は **(1) 秘密情報の置き場所（`{secret}`）** と **(2) トークンのライフサイクル管理** に置く。選んだ後の確認事項——`{api}` の制約（1ファイル/回、timeout 既定30秒・最大3600秒。カスタムエンドポイント自体は30秒で打ち切られる）、バッチ／スパイダー／Webhook の向き不向き、OAuth トークンを都度取得（JIT）するか保護された Topics レコードに保存するか、Instagram の長期トークンが60日で失効するといった実例の落とし穴、設計成果物テンプレート——は **[references/integration-design.md](references/integration-design.md)** にまとめている。プロキシ・取り込みを選んだら実装前に読む（構文だけが要るなら次節へ進んでよい）。プロキシで結果をフロントに返す書き方は [プロキシエンドポイントの返却](#プロキシエンドポイントの返却カスタム処理)。

## 外部API呼び出し

外部APIの呼び出しには **`{api}`** プラグインを使う（`{api_internal}`はKuroco自身のAPIを呼ぶ別プラグインなので混同しない。`api_request`という名前のプラグインは存在しない）。

### 基本構文

```smarty
{api
  endpoint='https://api.example.com/endpoint'
  method='GET'
  headers=$headers
  var='response'
  status_var='status'
}
```

### POSTリクエスト例（JSON）

`headers`は`'Key: value'`形式の文字列を並べた配列で指定する。JSONボディは`json_body`に渡す。

```smarty
{secret var='api_key' key='EXAMPLE_API_KEY'}
{assign_array var=headers values=""}
{append var=headers value='Content-Type: application/json'}
{append var=headers value="Authorization: Bearer `$api_key`"}

{assign_array var=body values=""}
{append var=body index='message' value='Hello'}

{api
  endpoint='https://api.example.com/post'
  method='POST'
  headers=$headers
  json_body=$body|@json_encode
  json_var='response'
  status_var='status'
}
```

### 非JSON（例: CSV）を送る場合

`body`属性を使う。JSON以外の内容でも、マルチバイト文字をエスケープするため`|@json_encode`を通す必要がある。Content-Typeヘッダーは`text/***`形式で明示する。

```smarty
{assign_array var=headers values=""}
{append var=headers value='Content-Type: text/csv'}
{assign var=csv value="ID,NAME,PRICE\n1,apple,150\n2,orange,200"}

{api
  endpoint='https://api.example.com/upload'
  method='PUT'
  headers=$headers
  body=$csv|@json_encode
  var='response'
  status_var='status'
}
```

### 主なパラメータ

| パラメータ | 内容 |
|---|---|
| `endpoint` | 呼び出し先URL（必須） |
| `query` / `queries` | クエリ文字列 / クエリパラメータ配列（URL に直接書いてもよい） |
| `method` | `GET`/`POST`/`PUT`/`PATCH`/`DELETE`/`PURGE`/`HEAD` |
| `headers` | `'Key: value'`形式の文字列配列 |
| `json_body` / `body` | JSON / 非JSONのリクエストボディ |
| `files` | 送信ファイル。**1回の呼び出しで送れるのは1ファイルのみ**（配列の2件目以降は無視される） |
| `var` / `json_var` | レスポンス格納変数。**JSON を返す API には `json_var` を使う**（デコード済みの配列で受け取れる。`var` は生文字列） |
| `status_var` | 成否（0/1） |
| `http_code_var` / `resp_header_var` | HTTP ステータスコード / レスポンスヘッダーの格納変数 |
| `timeout` | タイムアウト秒数。**既定 30、指定できるのは 1〜3600**（範囲外はエラー）。遅い外部 API なら明示的に伸ばすか、取り込み（バッチ）に倒す |
| `cache_time` | キャッシュ時間（分）。相手 API への往復を減らす。Kuroco 側エンドポイントのキャッシュ（Kuroco の API リクエスト課金を減らす）とは目的が別で、併用できる |
| `sslcert` / `sslkey` / `cainfo` | mTLS用の証明書・鍵・CA情報。値は**証明書そのものではなくシークレットのキー名** |

外部APIキーなど秘匿すべき値は**`{secret}`プラグイン**（[環境設定]→[シークレット]で事前に登録）で読み出す。`$smarty.const.*`（サイト定数）は非秘匿の設定値向けで、APIキー等の秘匿情報には使わない。

```smarty
{secret var='api_key' key='EXAMPLE_API_KEY'}
{assign_array var=headers values=""}
{append var=headers value="Authorization: Bearer `$api_key`"}
{api
  endpoint='https://api.example.com/endpoint'
  headers=$headers
  var='response'
}
```

### プロキシエンドポイントの返却（カスタム処理）

`request_api` / `request_api_post` のカスタムエンドポイントは、既定では**テンプレートで assign した `data` 変数を `{"data": …}` の形で返す**。**1リクエストの PHP 実行時間は30秒**（API エントリの `set_time_limit(30)`）なので、プロキシで `{api}` を呼ぶときは `timeout` を30未満（例: 10）にする——既定の30秒のままだと外部待ちの途中で先にエンドポイント側が打ち切られる。任意の形の JSON をそのまま返したいときはエンドポイント設定の **`show_contents`** を有効にし、テンプレートが JSON 文字列を出力する（出力が空なら `[]`、不正な JSON なら `Contents JSON error`）。リクエストパラメータは `$smarty.request.*`（GET/POST 共通）や `$smarty.post.*` で受け、外部 URL に埋める前に検証する。

```smarty
{assign var=city value=$smarty.request.city|default:"tokyo"}
{secret var='weather_key' key='WEATHER_API_KEY'}
{assign_array var=headers values=""}
{append var=headers value="X-Api-Key: `$weather_key`"}

{api
  endpoint="https://api.weather.example/today?city=`$city`"
  method='GET'
  headers=$headers
  json_var='forecast'
  status_var='ok'
  timeout=10
  cache_time=30
}

{if $ok == 1}
  {assign var='data' value=$forecast}
{else}
  {logger msg1="weather-proxy-error" msg2="city=`$city`"}
  {assign_array var=err values=""}
  {append var=err index='error' value='weather_unavailable'}
  {assign var='data' value=$err}
{/if}
{* 既定はこれで {"data": …} が返る。show_contents を有効にした場合は代わりに {$data|@rcms_json_encode} を出力する *}
```

## トリガー処理

### コンテンツ更新時のトリガー

管理画面: [コンテンツ定義] → [トリガー設定]

**利用可能なイベント:**
| イベント | タイミング |
|---------|----------|
| 作成時 | コンテンツ新規作成後 |
| 更新時 | コンテンツ更新後 |
| 削除時 | コンテンツ削除後 |
| 公開時 | 公開ステータス変更時 |
| プレビューサイト送信後 | プレビューサイト（ステージサイト）への送信処理完了後 |

**利用可能な変数:**
```smarty
{$topics.topics_id}      {* コンテンツID *}
{$topics.subject}        {* タイトル *}
{$topics.contents}       {* 本文 *}
{$topics.ymd}            {* 公開日 *}
{$topics.ext_col_01}     {* 拡張項目 *}
```

### フォーム送信時のトリガー

管理画面: [フォーム] → [トリガー設定]

```smarty
{$inquiry.inquiry_id}    {* 回答ID *}
{$inquiry.name}          {* 名前 *}
{$inquiry.email}         {* メールアドレス *}
{$inquiry.message}       {* メッセージ *}
```

## 外部サービス連携

**詳細な連携パターン**: [references/integrations.md](references/integrations.md)（GitHub Actions / Slack / Chatwork / メール / SendGrid / Webhook / カスタム処理）。LINE・SMS・X はトリガーメールアドレスのみで、references に追加情報は無い

### トリガーメールアドレス（メール送信を契機とした連携）

メールの送信先に専用アドレスを指定すると、メール送信を契機に外部サービスへの送信やバッチ処理・AIエージェントの起動ができます。契機になるメールは、トリガー処理の `{sendmail}`、フォームの自動返信・管理者通知メールの宛先、メルマガのいずれでもよい——**コードを書かずに済む宛先設定を先に検討する**。

**前提**: 各宛先は対象チャネルの連携設定が有効になっている必要がある（LINE は [チャネル]→[メッセージング]→[LINE] にトリガーメールアドレスが表示される。Slack はサイト設定の Slack 連携）。ローカル部（@より前）は Slack=チャンネルID または #チャンネル名、LINE=送信先の LINE ユーザーID（公式アカウントの友だち追加 Webhook か LINE ログイン（OAuth SSO）で取得して会員に保存しておく——`kuroco-docs` の LINE 連携チュートリアル）、SMS=電話番号。送れるのはメール本文のテキスト（LINE は `[emoji:…]` 記法の絵文字も可）。

| 宛先アドレス | 動作 |
|-------------|------|
| `{channel}@slack.r-cms.jp` | Slack送信 |
| `{twitter_id}@tweets.twitter.r-cms.jp` | X（Twitter）投稿 |
| `{batch_id}@batch.r-cms.jp` | バッチ処理の起動 |
| `{ai_agent_id}@agent.r-cms.jp` | AIエージェントの起動 |
| `{LINE ID}@text.line.r-cms.jp` | LINE送信 |
| `{tel}@twilio.r-cms.jp` | テキストメッセージ（SMS）送信（Twilio） |

### Slack通知

プラグイン名は `slack_post_message`（`slack_send` というプラグインは存在しない）。webhook URLではなく、サイト設定のSlack連携（`slack_bot_token`）を使う。

```smarty
{slack_post_message
  channel="#general"
  text="通知メッセージ"
}
```

### メール通知

本文のパラメータ名は `contents`（`body` ではない）。

```smarty
{sendmail
  to="recipient@example.com"
  subject="件名"
  contents="本文"
}
```

### GitHub Actions連携

```smarty
{secret var='github_token' key='GITHUB_TOKEN'}
{assign_array var=headers values=""}
{append var=headers value="Authorization: token `$github_token`"}
{append var=headers value='Accept: application/vnd.github.v3+json'}

{assign_array var=body values=""}
{append var=body index='event_type' value='kuroco-update'}

{api
  endpoint='https://api.github.com/repos/owner/repo/dispatches'
  method='POST'
  headers=$headers
  json_body=$body|@json_encode
  var='response'
  status_var='status'
}
```

## ベストプラクティス

- **実行時間**: システム負荷の低い時間帯（深夜・早朝）に設定し、大量データは1日1回・ページング分割で処理する（`{while}` でページを回す例: [references/examples.md](references/examples.md#ページング分割)）
- **エラーハンドリング**: `errors` は空でも truthy にならないよう `|@count > 0` で判定し、`{logger}`（msg1〜msg4、各1KB以内）と `slack_post_message` で通知する（例: [references/examples.md](references/examples.md#エラーハンドリング)）
- **途中終了のタグは無い。** 失敗時に「以降を実行しない」は、書き込み部分を `{if $status == 1}…{/if}`（または `errors|@count == 0`）で囲んで表現する
- **動的なエンドポイントパス**はバッククォートで補間する。`{id}` のような波かっこをそのまま書くと Smarty タグとして解釈される

```smarty
{api_internal endpoint="/rcms-api/3/product/update/`$row.topics_id`" method='POST' member_id=1 queries=$body var='res' status_var='ok'}
```

## 関連スキル

- `/kuroco-api-content` - API設計・認証パターン、コンテンツCRUD操作
- `/kuroco-admin-mcp` - Admin MCP経由の管理操作

## 関連ドキュメント

- `../kuroco-docs/docs/tutorials-api-custom-1.md`（`how-to-use-batch`） - バッチ処理の使い方
- `../kuroco-docs/docs/tutorials-content-1.md`（`auto-run-github-with-contents-update`） - GitHub Actions連携
- `../kuroco-docs/docs/tutorials-form-mail-1.md`（`send-slack-notification-after-a-form-has-been-submitted`） - Slack通知
- `../kuroco-docs/docs/reference-smarty-trigger-3.md`（`trigger-variables`） - トリガー変数
