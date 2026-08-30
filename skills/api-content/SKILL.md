---
name: kuroco-api-content
metadata:
  author: Diverta inc.
  version: "1.5.1"
  lastUpdated: "2026-08-27"
description: KurocoのAPI設計とコンテンツ管理のベストプラクティス。エンドポイント設計、認証（Cookie・動的トークン・静的アクセストークン）、CORS、流量制限、キャッシュ、エラーハンドリング（401/403/429）、Topics APIによるコンテンツCRUD（list / details / insert / update / delete / bulk_upsert）、フィルタークエリ、ページネーション、多言語対応（langs_open_flg）、拡張項目（ext_col）、ファイルアップロード・CSVインポート、ECポイント（ECPoint）をカバー。API呼び出しの実装、ログインAPI・トークン認証、認証・権限エラーの解決、コンテンツの取得・作成・更新・削除・絞り込みの質問で使用。
---

# Kuroco API連携 & コンテンツ管理

Kuroco HeadlessCMSのAPI設計・実装およびコンテンツ管理に関するベストプラクティス。

**ドキュメント参照**: `/kuroco-docs` スキルを使用してKuroco公式ドキュメントを検索・参照できます。

## 目次

### Part 1: API連携パターン

- [エンドポイント設計](#エンドポイント設計)
- [セキュリティ設定](#セキュリティ設定)
- [キャッシュ戦略](#キャッシュ戦略)
- [流量制限](#流量制限)
- [API呼び出しパターン](#api呼び出しパターン)
- [エラーハンドリング](#エラーハンドリング)

### Part 2: コンテンツ管理パターン

- [コンテンツ構造](#コンテンツ構造)
- [拡張項目（カスタムフィールド）](#拡張項目カスタムフィールド)
- [Topics API オペレーション](#topics-api-オペレーション)
- [コンテンツCRUD操作](#コンテンツcrud操作)
- [フィルタークエリ](#フィルタークエリ) → 詳細は [references/filter-query.md](references/filter-query.md)
- [ファイル・CSV操作](#ファイルcsv操作) → 詳細は [references/file-operations.md](references/file-operations.md)
- [Admin MCPによる管理操作（コンテンツ）](#admin-mcpによる管理操作コンテンツ)

---

# Part 1: API連携パターン

## エンドポイント設計

### 基本構造

KurocoのAPIパスは以下の形式：
```
https://{サイトキー}.g.kuroco.app/rcms-api/{api_id}/{endpoint_path}
```

例：
```
https://example.g.kuroco.app/rcms-api/1/news
https://example.g.kuroco.app/rcms-api/1/member/login
```

### エンドポイント設定の主要項目

| 項目 | 説明 | 例 |
|------|------|-----|
| パス | エンドポイントのURL | `news`, `member/list` |
| モデル | 操作対象 | Topics, Member, InquiryForm |
| オペレーション | 操作種別 | list, details, insert, update, delete |
| キャッシュ | レスポンスキャッシュ期間 | 86400（1日） |
| 流量制限 | リクエスト数制限 | 100回/分 |
| 認証必須 | ログイン必須かどうか | true/false |

### 主要カテゴリとモデル

**認証（Authentication）**
| オペレーション | 説明 | メソッド |
|--------------|------|---------|
| `login_challenge` | ログイン | POST |
| `token` | アクセストークン取得 | POST |
| `logout` | ログアウト | POST |
| `profile` | ログインユーザー情報取得 | GET |
| `reminder` | パスワードリマインダー | POST |

**コンテンツ（Topics）**
| オペレーション | 説明 | メソッド |
|--------------|------|---------|
| `list` | 一覧取得 | GET |
| `details` | 詳細取得 | GET |
| `insert` | 新規追加 | POST |
| `update` | 更新 | POST |
| `delete` | 削除 | POST |
| `bulk_upsert` | 一括更新 | POST |

**メンバー（Member）**
| オペレーション | 説明 | メソッド |
|--------------|------|---------|
| `list` | メンバー一覧 | GET |
| `details` | メンバー詳細 | GET |
| `insert` | メンバー登録 | POST |
| `update` | メンバー更新 | POST |

**フォーム（InquiryMessage/InquiryForm）**
| オペレーション | 説明 | メソッド |
|--------------|------|---------|
| `send` | フォーム送信 | POST |
| `list` | 回答一覧 | GET |
| `details` | 回答詳細 | GET |

**ECポイント（ECPoint）**
| オペレーション | 説明 | メソッド |
|--------------|------|---------|
| `update` | ポイントの付与・消費 | POST |
| `history` | ポイント履歴・現在残高の取得 | GET |

## セキュリティ設定

> **詳細リファレンス**: セキュリティ設定の詳細は [references/security-settings.md](references/security-settings.md) を参照してください。
>
> **公式ドキュメント**: 詳細な公式情報は `../kuroco-docs/docs/management-api.md`（`api-security`） 等を参照してください。

### 認証方式

管理画面: [API] → [セキュリティ] で4種類から選択。

| 認証方式 | 用途 | ヘッダー |
|---------|------|---------|
| なし | 公開データ専用API（キャッシュと併用）。非公開データ・書き込み系には使わない | 不要 |
| 静的アクセストークン | サーバー間通信、公開API | `X-RCMS-API-ACCESS-TOKEN: {固定トークン}` |
| 動的アクセストークン | ログイン必須サイト（JWT） | `X-RCMS-API-ACCESS-TOKEN: {動的トークン}` |
| Cookie | ログイン必須Webサイト | `credentials: 'include'`（フロントエンド側） |

**トークン有効期限の事前通知**: 静的アクセストークン・特権付き静的トークン・KurocoFrontのトークンは、有効期限の30日前・7日前・1日前にアカウント設定のメールアドレスへ通知メールが送信される。

**注意**: APIのセキュリティ設定を変更すると、既存の発行済みトークンが無効化される（変更時に確認アラートが表示される）。稼働中のクライアントがある場合はトークンの再発行・差し替えを事前に計画すること。

#### 1. Cookie認証（Webアプリ推奨）

セッションベースの認証。`credentials: 'include'` が必須。

```javascript
// ログイン
const response = await fetch('https://example.g.kuroco.app/rcms-api/1/login', {
  method: 'POST',
  credentials: 'include',  // 必須
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
})

// レスポンス例
// {
//   "grant_token": "xxxxx",
//   "status": 0,
//   "member_id": 123
// }
```

**注意点**:
- サードパーティCookie問題（Safari等でブロックされる）
- APIドメインとフロントエンドを**同一ドメイン（サブドメイン違い）**に設定が必要（ファーストパーティCookie化）
  - 例: `api.example.com` と `www.example.com`
- Cookie認証APIが複数ある場合、各API間で認証状態が**共有される**

#### 2. トークン認証（モバイルアプリ推奨）

JWTベースの認証。ヘッダーにトークンを付与。

**取得フローは2段階**: まず `login`（`Login::login_challenge`）に email/password をPOSTして `grant_token` を取得し、次に `token`（`Login::token`）エンドポイントへ `grant_token` をPOSTして `access_token` / `refresh_token` に交換する。**`token` エンドポイントに email/password を直接送ることはできない**（受け付けるボディは初回発行時 `{ "grant_token": "..." }`、再発行時 `{ "refresh_token": "..." }` のみ）。

```javascript
// 1. ログインして grant_token を取得
const loginResponse = await fetch('https://example.g.kuroco.app/rcms-api/1/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
})
const { grant_token } = await loginResponse.json()

// 2. grant_token をアクセストークンに交換
const tokenResponse = await fetch('https://example.g.kuroco.app/rcms-api/1/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ grant_token })
})

const { access_token, refresh_token } = await tokenResponse.json()

// レスポンス例
// {
//   "access_token": {
//     "value": "eyJhbGciOiJS...",
//     "expiresAt": "2024-01-01T12:00:00+09:00"
//   },
//   "refresh_token": {
//     "value": "xxxxxx",
//     "expiresAt": "2024-01-08T12:00:00+09:00"
//   }
// }

// API呼び出し時
const response = await fetch('https://example.g.kuroco.app/rcms-api/1/news', {
  headers: {
    'X-RCMS-API-ACCESS-TOKEN': access_token.value
  }
})
```

**前提条件**: ユーザー1人以上、`login_challenge` + `token` エンドポイント必須。トークン認証APIが複数ある場合、各API間で認証状態は**共有されない**。

#### 3. StaticToken認証（サーバー間通信）

固定トークンによるAPIアクセス制限。

```javascript
const response = await fetch('https://example.g.kuroco.app/rcms-api/1/internal-api', {
  headers: {
    'X-RCMS-API-ACCESS-TOKEN': 'your-static-token-here'
  }
})
```

**設定場所**: 管理画面 → API → セキュリティ → StaticToken

**注意**: 静的トークンはフロントエンドに組み込まれるとユーザーに見える。流出時のトークン更新を想定した運用が必要。

### IPアドレス制限

管理画面: [API] → [セキュリティ] → [IPアドレス制限]

指定されたIPアドレスからのアクセスのみ許可します。

| 指定形式 | 例 | 説明 |
|---------|-----|------|
| 個別IP | `192.0.2.1` | 単一IPアドレス |
| CIDR | `192.0.2.0/24` | サブネット単位 |
| 範囲指定 | `192.0.2.1-192.0.2.2` | ハイフンによるIP範囲 |

**IPアドレスグループ**: 定数機能で `IPSETS_*` を定義し、`[[IPSETS_*]]` で参照可能（`../kuroco-docs/docs/faq-domain.md`（`is-it-possible-to-set-multiple-ip-addresses-at-once`） 参照）。

### CORS設定

管理画面: [API] → [セキュリティ] → [CORS]

| 項目 | 対応ヘッダー | 説明 |
|------|------------|------|
| CORS_ALLOW_ORIGINS | Access-Control-Allow-Origin | 許可オリジン（**ワイルドカード`*`は非推奨**） |
| CORS_ALLOW_METHODS | Access-Control-Allow-Methods | 許可HTTPメソッド |
| CORS_ALLOW_HEADERS | Access-Control-Allow-Headers | 許可リクエストヘッダー |
| CORS_MAX_AGE | Access-Control-Max-Age | プリフライトキャッシュ秒数 |
| CORS_ALLOW_CREDENTIALS | Access-Control-Allow-Credentials | Cookie送信の許可 |

**CSRF対策**: CORS + `Content-Type: application/json` でモダンブラウザでのCSRF攻撃を防御。ワイルドカードを使うと防御効果がなくなるため、必ず特定ドメインを指定すること。

**変更反映の遅延**: CORS設定変更後は `CORS_MAX_AGE` 分だけブラウザにキャッシュされる。即時反映にはブラウザキャッシュクリアまたは `CORS_MAX_AGE` を `0` に設定。

### APIリクエスト制限

| 制限タイプ | 説明 |
|----------|------|
| None | 制限なし |
| GroupAuth | ログインユーザーの**グループ権限**をチェックし、合致した場合のみ許可 |
| MemberCustomSearchAuth | ログインユーザーが**カスタムメンバーフィルター**の条件に合致する場合のみ許可 |

### 閲覧制限の優先順序

コンテンツ返却時の制限は以下の順序で評価されます（上位優先）:

1. **API → IPアドレス制限**（API全体）
2. **エンドポイント → APIリクエスト制限**（エンドポイント単位）
3. **コンテンツ定義 → APIリクエスト制限**
4. **コンテンツカテゴリ → APIリクエスト制限**
5. **個別コンテンツ → APIリクエスト制限**

### 後処理によるレスポンス制限

管理画面: [API] → エンドポイント → [後処理]

APIレスポンスから不要なフィールドを除外し、公開情報を制御:

| 処理タイプ | 説明 |
|----------|------|
| 出力許可リスト | 指定フィールドのみ返す（ホワイトリスト）。例: `list.subject`, `pageInfo` |
| 出力変換リスト | フィールドの削除・名称変更・変換関数の適用 |
| カスタム処理 | Smartyテンプレートでの独自ロジック |

**パフォーマンスTip**: 出力許可リストは他の処理の前に配置するとSQLレベルで効果あり。

### プラットフォームセキュリティ

Kurocoプラットフォームが提供するインフラレベルのセキュリティ:

- **通信**: HTTPS完全暗号化、TLS証明書自動管理
- **防御**: WAF、CDN、DDoS対策（オプションでFastly DDoS Protection）
- **認証連携**: SAML/OAuth外部ログイン、クライアント証明書（オプション）
- **監査**: アクセスログ、アプリケーションログ
- **認定**: ISMS (ISO 27001)、ISMSクラウド (ISO 27017)、プライバシーマーク
- **診断**: 毎日のコンテナ脆弱性スキャン、VADDY連携自動診断

### Admin MCPによる設定変更

APIのセキュリティ設定は管理画面だけでなく、**Admin MCP経由**でも操作可能です。接続・認証は `/kuroco-admin-mcp` スキルを参照してください。

## キャッシュ戦略

### 推奨設定

| ユースケース | キャッシュ期間 | 設定値 |
|------------|--------------|-------|
| 静的コンテンツ（ニュース等） | 1日 | 86400 |
| 更新頻度低いコンテンツ | 1週間 | 604800 |
| リアルタイム性が必要 | キャッシュなし | 0 |
| 認証が必要なAPI | キャッシュなし | 0 |

**重要**: コンテンツ・メンバー等のデータ更新時、キャッシュは自動クリアされます。**クリアされる範囲はデータの種類ごとに決まっている**ため、下記を把握しておくとキャッシュ期間を長めに設定しても安全かどうかを判断しやすい。

### Topicsのキャッシュクリア範囲

| 操作 | クリアされる範囲 |
|------|----------------|
| Topics（`insert` / `update` / `delete` / `accept` / `bulk_upsert` / `increment`） | 同じコンテンツ定義グループ（TopicsGroup）に紐づく全エンドポイント。**`Topics::details`のみ、更新されたコンテンツIDのキャッシュだけがクリアされる** |
| コンテンツカテゴリ（新規作成・更新・削除） | 同じコンテンツ定義グループに紐づく全エンドポイント。**`Topics::details`は対象外**（カテゴリの変更ではdetails側はクリアされない） |
| フォーム（`InquiryForm` の insert/update/delete、回答CSVアップロード） | 同じフォームIDに紐づく全エンドポイント |
| コメント（`Comment` の insert/update/delete） | モデルカテゴリ「アクティビティ」に紐づく全エンドポイント＋紐づけ先のコンテンツ定義グループに紐づくエンドポイント |
| お気に入り（`Favorite` の insert/delete） | 対象モデルカテゴリの全エンドポイント＋対象コンテンツのコンテンツ定義に紐づく`Topics::list`エンドポイント |
| メンバー（`Member` の insert/update） | モデルカテゴリ「メンバー」「認証」に紐づく全エンドポイント |
| マスタ（update/delete） | 同じマスタIDに紐づく全エンドポイント |

**上記以外の操作では自動クリアされない。** プロキシ経由・取り込み用のカスタムSmarty処理など、標準のTopics API以外の経路でデータを更新する場合は自動クリアの対象外なので、Smartyプラグイン `purge_cdn_cache` でクリア範囲・タイミングを明示的に指定する（例: `Favorite::insert`の後処理で`Topics::details`のキャッシュを削除）。急ぎクリアしたい場合はエンドポイント一覧の「キャッシュクリアする」ボタンで手動クリアもできる。

出典: `../kuroco-docs/docs/reference-api-1.md`（`cache-clear-operation`）

### キャッシュヘッダー

レスポンスヘッダーで確認可能：
```
Cache-Control: max-age=86400
```

## 流量制限

### 無料利用ユーザーの制限

決済情報未登録のユーザーには以下の制限があります。クレジットカード登録済み、または請求書払いのユーザーは対象外です。

| 対象 | 制限 |
|------|------|
| API送信 | 1時間あたり約1,000件 |
| バッチ処理 | 1時間あたり約100件 |

### レスポンスヘッダー

```
x-rcms-ratelimit-limit: 100      # 制限数
x-rcms-ratelimit-remaining: 95   # 残りリクエスト数
x-rcms-ratelimit-reset: 60       # リセットまでの秒数
```

### 429エラー時の対応

```javascript
const response = await fetch(url)

if (response.status === 429) {
  const resetTime = response.headers.get('x-rcms-ratelimit-reset')
  throw new Error(`流量制限超過。${resetTime}秒後に再試行してください`)
}
```

## API呼び出しパターン

### 一覧取得（ページネーション付き）

```javascript
async function fetchNewsList(page = 1, perPage = 10) {
  const params = new URLSearchParams({
    pageID: page,
    cnt: perPage
  })

  const response = await fetch(
    `https://example.g.kuroco.app/rcms-api/1/news?${params}`,
    { credentials: 'include' }
  )

  const data = await response.json()

  // レスポンス構造
  // {
  //   "list": [...],
  //   "pageInfo": {
  //     "totalCnt": 100,
  //     "perPage": 10,
  //     "totalPageCnt": 10,
  //     "pageNo": 1
  //   }
  // }

  return data
}
```

### フィルター検索

```javascript
// filter パラメータで検索
const params = new URLSearchParams({
  filter: 'subject contains "重要"',
  order_query: 'ymd=DESC'
})
// カテゴリでの絞り込みは contents_type を使う（category_id というフィールドは無い）
// 例: filter: 'contents_type = 1'

const response = await fetch(
  `https://example.g.kuroco.app/rcms-api/1/news?${params}`,
  { credentials: 'include' }
)
```

### 詳細取得

```javascript
async function fetchNewsDetail(topicsId) {
  const response = await fetch(
    `https://example.g.kuroco.app/rcms-api/1/newsdetail/${topicsId}`,
    { credentials: 'include' }
  )

  const data = await response.json()

  // レスポンス構造
  // {
  //   "details": {
  //     "topics_id": 1,
  //     "subject": "タイトル",
  //     "contents": "<p>本文</p>",
  //     ...
  //   }
  // }

  return data.details
}
```

### 多言語サイトでの公開状態の一括取得

Topics::list / Topics::details のエンドポイントで `langs_open_flg` パラメータを有効にすると、各コンテンツに全設定言語の公開状態を示す `langs_open_flg` オブジェクトが含まれます。言語ごとに個別のAPIリクエストを行わずに言語切替UIの表示制御が可能です。

```javascript
// レスポンス例
// {
//   "details": {
//     "topics_id": 1,
//     "langs_open_flg": { "en": 1, "ja": 0 },
//     ...
//   }
// }
```

### お気に入り日時の取得・並べ替え

Topics::list のエンドポイントで `get_last_favorite_ymdhi` パラメータを有効にすると、各コンテンツが最後にお気に入りされた日時（`last_favorite_ymdhi`）を取得できます。`last_favorite_ymdhi` での並べ替えにも対応しており、「人気順（最近お気に入りされた順）」の一覧表示が可能です。

### コンテンツ作成

```javascript
async function createNews(newsData) {
  const response = await fetch(
    'https://example.g.kuroco.app/rcms-api/1/news/insert',
    {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        subject: newsData.title,
        contents: newsData.body,
        ymd: newsData.date,
        open_flg: 1  // 1: 公開, 0: 非公開（topics_flg は「一覧に載せる/載せない」の別フラグ）
      })
    }
  )

  return response.json()
}
```

## エラーハンドリング

### 主要エラーコード

| コード | 説明 | 対応 |
|--------|------|------|
| 400 | リクエストエラー | リクエストパラメータを確認 |
| 401 | 認証エラー | ログイン状態・トークンを確認 |
| 403 | 権限エラー | APIの権限設定を確認 |
| 404 | リソース未存在 | パス・IDを確認 |
| 429 | 流量制限超過 | リトライまで待機 |
| 500 | サーバーエラー | Kurocoサポートに連絡 |

### エラーレスポンス例

```json
{
  "errors": [
    {
      "code": "authentication_error",
      "message": "ログインが必要です"
    }
  ]
}
```

### エラーハンドリング実装

```javascript
async function apiRequest(url, options = {}) {
  const response = await fetch(url, {
    credentials: 'include',
    ...options
  })

  if (!response.ok) {
    const errorData = await response.json()

    switch (response.status) {
      case 401:
        throw new Error('認証が必要です')
      case 403:
        throw new Error('アクセス権限がありません')
      case 429:
        throw new Error('リクエスト制限を超えました')
      default:
        throw new Error(errorData.errors?.[0]?.message || 'APIエラー')
    }
  }

  return response.json()
}
```

---

# Part 2: コンテンツ管理パターン

## コンテンツ構造

### 階層構造

```
コンテンツ定義（TopicsGroup）
├── カテゴリ（TopicsCategory）
│   └── コンテンツ（Topics）
└── 拡張項目（ext_col_01〜ext_col_XX）
```

### コンテンツ定義の設定

管理画面: [コンテンツ定義] → [新規作成]

| 項目 | 説明 |
|------|------|
| グループ名 | コンテンツ定義の名前 |
| 識別子 | ユニークなID（英数字） |
| 本文の入力方法 | WYSIWYG、マークダウン、HTML |
| 閲覧制限 | 全員/グループ制限/カスタム検索 |
| 編集制限 | 全員/グループ制限/カスタム検索 |
| 拡張項目 | カスタムフィールド。上限は`whoami`の`site.limits.topics_max_extension`（`{current, max}`）で確認する。`max`はJSONB形式サイトで999、レガシー形式サイトで99。`current`が`max`未満なら`admin_setting-update`で引き上げ可能（詳細: `/kuroco-admin-mcp`） |

## 拡張項目（カスタムフィールド）

> **キー名を推測しない。** 拡張項目のキー名は**サイト単位で `ext_1` 形式と `ext_col_01` 形式に分かれます**。
> Admin MCP に接続できる場合は `whoami` の `site.topics_ext_key_format` でそのサイトの命名を確認し、
> どの番号がどの項目かは `topics-describe`（グループ単位の正）で確定させてください（→ `/kuroco-admin-mcp`）。
> **`ext_slug` を設定した項目はスラッグがキーになる**ため、この分岐の影響を受けません。設定を推奨します。
> 以下の表は `ext_col_01` 形式のサイトでの例です。

| タイプ | 説明 | APIレスポンス例 |
|--------|------|----------------|
| テキスト | 1行テキスト | `"ext_col_01": "値"` |
| テキストエリア | 複数行テキスト | `"ext_col_02": "複数行\nテキスト"` |
| WYSIWYG | リッチテキスト | `"ext_col_03": "<p>HTML</p>"` |
| 数値 | 整数・小数 | `"ext_col_04": 100` |
| 日付 | 日付選択 | `"ext_col_05": "2024-01-01"` |
| 選択（単一） | ラジオボタン | `"ext_col_06": "選択肢1"` |
| 選択（複数） | チェックボックス | `"ext_col_07": ["選択肢1", "選択肢2"]` |
| ファイル/画像 | アップロード | `"ext_col_08": { "id": "xxx", "url": "https://...", "desc": "" }` |
| リンク | URLリンク | `"ext_col_10": { "url": "https://...", "title": "リンク名" }` |
| 関連コンテンツ | 他コンテンツ参照 | `"ext_col_11": { "topics_id": 123, "subject": "タイトル" }` |

## Topics API オペレーション

| オペレーション | 説明 | メソッド | パス例 |
|--------------|------|---------|-------|
| list | 一覧取得 | GET | `/news` |
| details | 詳細取得 | GET | `/newsdetail/{topics_id}` |
| insert | 新規追加 | POST | `/news/insert` |
| update | 更新 | POST | `/news/update/{topics_id}` |
| delete | 削除 | POST | `/news/delete/{topics_id}` |
| bulk_upsert | 一括更新 | POST | `/news/bulk` |

## コンテンツCRUD操作

### 一覧取得レスポンス

```json
{
  "list": [
    {
      "topics_id": 1,
      "subject": "タイトル",
      "contents": "本文（HTML）",
      "ymd": "2024-01-01",
      "open_flg": 1,
      "contents_type": 1,
      "contents_type_nm": "カテゴリ名",
      "ext_col_01": "拡張項目値",
      "tag": ["タグ1", "タグ2"]
    }
  ],
  "pageInfo": {
    "totalCnt": 100,
    "perPage": 10,
    "totalPageCnt": 10,
    "pageNo": 1
  }
}
```

### コンテンツ作成

```javascript
const response = await fetch('/rcms-api/1/news/insert', {
  method: 'POST',
  credentials: 'include',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    subject: 'タイトル',
    contents: '<p>本文</p>',
    ymd: '2024-01-01',
    open_flg: 1,                          // 1: 公開, 0: 非公開
    contents_type: 1,                     // カテゴリID（category_idというフィールドは無い）
    open_type: 'sitei',                   // 予約公開を使う場合は 'sitei' を明示（既定 'open' のままだと日時が保存されない）
    open_sta_date: '2024-12-01 00:00:00', // 公開開始日時
    open_end_date: '2024-12-31 23:59:59', // 公開終了日時
    tag: ['タグ1', 'タグ2'],
    ext_col_01: 'カスタム値'
  })
})
```

### コンテンツ更新

```javascript
const response = await fetch(`/rcms-api/1/news/update/${topicsId}`, {
  method: 'POST',
  credentials: 'include',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    subject: '更新タイトル',
    contents: '更新本文'
    // 更新したいフィールドのみ送信可能
  })
})
```

### コンテンツ削除

```javascript
await fetch(`/rcms-api/1/news/delete/${topicsId}`, {
  method: 'POST',
  credentials: 'include'
})
```

## フィルタークエリ

基本構文: `filter={field} {operator} {value}`

| 演算子 | 例 |
|--------|-----|
| `=`, `!=` | `filter=contents_type = 1` |
| `>`, `>=`, `<`, `<=` | `filter=ymd >= "2024-01-01"` |
| `contains`, `ncontains` | `filter=subject contains "キーワード"` |
| `in`, `nin` | `filter=contents_type in [1, 2, 3]` |

**文字列の値は二重引用符で囲む。** シングルクォートは引用符ごと値の一部として扱われ、
エラーにならず0件になる（値に空白を含む場合は構文エラー）。

**カテゴリのフィールド名は `contents_type`**（`category_id` というフィールドは存在しない）。

複合条件: `filter=(contents_type = 1 or contents_type = 2) and topics_flg = 1`

ソート: `order_query=ymd=DESC`（`{フィールド}={ASC|DESC}`。複数指定はカンマ区切り）

**詳細な使い方**: [references/filter-query.md](references/filter-query.md) を参照

## ファイル・CSV操作

### ファイルアップロード

```javascript
// 1. ファイルアップロード
const formData = new FormData()
formData.append('file', file)
const result = await fetch('/rcms-api/1/files/upload', {
  method: 'POST',
  credentials: 'include',
  body: formData
})
const { file_id } = await result.json()

// 2. コンテンツに紐付け
await fetch('/rcms-api/1/news/insert', {
  method: 'POST',
  credentials: 'include',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    subject: 'タイトル',
    ext_col_02: { file_id, desc: '説明' }
  })
})
```

**詳細（一括更新、カテゴリ、タグ、閲覧制限）**: [references/file-operations.md](references/file-operations.md) を参照

## Admin MCPによる管理操作（コンテンツ）

AIエージェント（Claude Desktop / claude.ai / Claude Code 等のMCPクライアント）から管理画面と同等のコンテンツ操作を行うには **Admin MCP（`/kuroco-admin-mcp` スキル）** を使用します。フロントエンドAPI（rcms-api）との違いに注意してください。

### フロントエンドAPI vs 管理操作（Admin MCP）

| 項目 | フロントエンドAPI（rcms-api） | 管理操作（Admin MCP） |
|------|---------------------------|-------------------|
| 対象 | エンドユーザー | 管理者・運用者 |
| 認証 | StaticToken / DynamicToken / Cookie | OAuth（Admin MCP） |
| エンドポイント | `/rcms-api/{api_id}/{path}` | Admin MCP ツール経由 |
| 利用場面 | フロントエンド実装 | データ一括操作、構造確認、設定変更 |

### 活用シーン

- **サイト構造の把握**: コンテンツ定義一覧・拡張項目の確認
- **データの一括確認・修正**: 管理画面GUIを経由せず効率的にデータ操作
- **スキーマ確認**: Admin MCP のスキーマ取得ツールでフィールド定義を取得

> **注意**: insert/update/deleteは必ずユーザーに確認してから実行すること。接続設定・ツールの詳細は `/kuroco-admin-mcp` スキル参照。

## ベストプラクティス

- **キャッシュ活用**: エンドポイント設定で `キャッシュ: 86400`（1日）を設定。更新時は自動クリア
- **ページネーション**: `pageID` と `cnt` パラメータで分割取得

---

## 関連スキル

- `/kuroco-frontend-integration` - Vite/Nuxt.js/Next.jsでのAPI呼び出しパターン、KurocoFrontデプロイ
- `/kuroco-server-processing` - Smartyプラグイン・構文リファレンス、Webhook・バッチ処理
- `/kuroco-admin-mcp` - Admin MCP経由の管理操作

## 関連ドキュメント

### スキル内リファレンス
- [references/security-settings.md](references/security-settings.md) - セキュリティ設定の詳細リファレンス
- [references/filter-query.md](references/filter-query.md) - フィルタークエリ詳細
- [references/file-operations.md](references/file-operations.md) - ファイル・CSV操作詳細

### Kuroco公式ドキュメント
- `../kuroco-docs/docs/management-api.md`（`api-security`） - APIセキュリティ設定（認証方式、IP制限）
- `../kuroco-docs/docs/management-api.md`（`api-list`） - API一覧・CORS設定
- `../kuroco-docs/docs/management-api.md`（`api-postprocessing`） - API後処理の設定
- `../kuroco-docs/docs/reference-api-2.md`（`endpoint-settings`） - エンドポイント設定項目一覧
- `../kuroco-docs/docs/reference-smarty-trigger-1.md`（`post-processing`） - 後処理の詳細リファレンス
- `../kuroco-docs/docs/tutorials-api-custom-1.md`（`configure-endpoint`） - エンドポイント設定方法
- `../kuroco-docs/docs/tutorials-auth-member-3.md`（`login`） - ログイン実装
- `../kuroco-docs/docs/tutorials-api-custom-1.md`（`restricting-api-access-with-statictoken`） - StaticToken認証
- `../kuroco-docs/docs/reference-api-1.md`（`api-cache`） - APIキャッシュ
- `../kuroco-docs/docs/reference-api-1.md`（`cache-clear-operation`） - APIキャッシュクリアのタイミングと範囲
- `../kuroco-docs/docs/reference-api-3.md`（`filter-query`） - フィルタークエリ
- `../kuroco-docs/docs/about.md`（`security`） - プラットフォームセキュリティ概要
- `../kuroco-docs/docs/faq-member.md`（`in-what-order-are-viewing-restrictions-applied`） - 閲覧制限の優先順序
- https://kuroco.app/ja/docs/faq/cors-and-content-type-prevent-csrf-attacks/ - CSRF対策
- `../kuroco-docs/docs/faq-api-error.md`（`the-api-returns-403-forbidden-even-though-no-restrictions-are-applied`） - 403エラーの解決
- `../kuroco-docs/docs/tutorials-content-1.md`（`adding-a-topics`） - コンテンツ定義作成
- `../kuroco-docs/docs/tutorials-content-1.md`（`bulk-upload-in-csv`） - CSVアップロード
- `../kuroco-docs/docs/management-content.md`（`content-structure-topics`） - コンテンツ構造
