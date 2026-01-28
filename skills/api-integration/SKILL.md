---
name: kuroco-api-integration
description: Kuroco API設計・実装のベストプラクティス。使用キーワード：「Kuroco API」「エンドポイント設定」「API設計」「認証」「CORS」「APIセキュリティ」「ログインAPI」「トークン認証」「Cookie認証」「JWT」「StaticToken」「X-RCMS-API-ACCESS-TOKEN」「rcms-api」「g.kuroco.app」「流量制限」「レート制限」「キャッシュ」「credentials include」「fetch」「axios」「HTTPリクエスト」「401エラー」「403エラー」「429エラー」「認証エラー」「権限エラー」「APIレスポンス」「pageInfo」「ページネーション」「アクセストークン」「リフレッシュトークン」「grant_token」。APIの設計、呼び出し、認証、エラー処理に関する質問で使用。
---

# Kuroco API連携パターン

Kuroco HeadlessCMSのAPI設計・実装に関するベストプラクティスを提供します。

**ドキュメント参照**: `/kuroco-docs` スキルを使用してKuroco公式ドキュメントを検索・参照できます。

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

## セキュリティ設定

### 認証方式

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
- APIドメインとフロントエンドを**同一ドメイン（サブドメイン違い）**に設定が必要
  - 例: `api.example.com` と `www.example.com`

#### 2. トークン認証（モバイルアプリ推奨）

JWTベースの認証。ヘッダーにトークンを付与。

```javascript
// トークン取得
const tokenResponse = await fetch('https://example.g.kuroco.app/rcms-api/1/token', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
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

### CORS設定

管理画面: [API] → [セキュリティ] → [CORS設定]

```
CORS_ALLOW_ORIGINS:
  - http://localhost:3000      # 開発環境
  - https://your-frontend.com   # 本番環境

CORS_ALLOW_METHODS:
  - GET
  - POST
  - PUT
  - DELETE
```

### APIリクエスト制限

| 制限タイプ | 説明 |
|----------|------|
| None | 制限なし |
| GroupAuth | グループ権限による制限 |
| MemberCustomSearchAuth | カスタム検索条件による制限 |

## キャッシュ戦略

### 推奨設定

| ユースケース | キャッシュ期間 | 設定値 |
|------------|--------------|-------|
| 静的コンテンツ（ニュース等） | 1日 | 86400 |
| 更新頻度低いコンテンツ | 1週間 | 604800 |
| リアルタイム性が必要 | キャッシュなし | 0 |
| 認証が必要なAPI | キャッシュなし | 0 |

**重要**: コンテンツ・メンバー等のデータ更新時、キャッシュは自動クリアされます。

### キャッシュヘッダー

レスポンスヘッダーで確認可能：
```
Cache-Control: max-age=86400
```

## 流量制限

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
  console.log(`流量制限超過。${resetTime}秒後に再試行してください`)
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
  order_by: 'ymd desc'
})

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
        topics_flg: 1  // 1: 公開, 0: 非公開
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
  try {
    const response = await fetch(url, {
      credentials: 'include',
      ...options
    })

    if (!response.ok) {
      const errorData = await response.json()

      switch (response.status) {
        case 401:
          // ログイン画面へリダイレクト
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
  } catch (error) {
    console.error('API Error:', error)
    throw error
  }
}
```

## 関連ドキュメント

詳細は以下のファイルを参照：
- `docs/tutorials/configure-endpoint.md` - エンドポイント設定方法
- `docs/tutorials/login.md` - ログイン実装
- `docs/tutorials/restricting-api-access-with-statictoken.md` - StaticToken認証
- `docs/reference/endpoint-settings.md` - エンドポイント設定項目一覧
- `docs/reference/api-cache.md` - APIキャッシュ
- `docs/reference/filter-query.md` - フィルタークエリ
- `docs/management/api-security.md` - APIセキュリティ設定
