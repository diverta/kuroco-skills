---
name: kuroco-content-management
description: Kurocoコンテンツ管理（CRUD操作）のベストプラクティス。使用キーワード：「コンテンツ定義」「記事管理」「Topics」「TopicsGroup」「カテゴリ」「WYSIWYG」「ファイルアップロード」「CSVインポート」「コンテンツAPI」「拡張項目」「ext_col」「topics_id」「subject」「contents」「ymd」「topics_flg」「フィルター」「filter」「order_by」「一覧取得」「詳細取得」「list」「details」「insert」「update」「delete」「bulk_upsert」「一括更新」「タグ」「tag」「予約投稿」「open_ymd」「close_ymd」「公開設定」「閲覧制限」「関連コンテンツ」「pageID」「cnt」。コンテンツの作成・取得・更新・削除・フィルタリングに関する質問で使用。
---

# Kuroco コンテンツ管理パターン

Kuroco HeadlessCMSでのコンテンツ管理（作成・取得・更新・削除）に関するベストプラクティス。

**ドキュメント参照**: 詳細は `${CLAUDE_PLUGIN_ROOT}/docs/` を参照。同期が必要な場合は `/kuroco-docs` スキルを使用。

## 目次

- [コンテンツ構造](#コンテンツ構造)
- [拡張項目（カスタムフィールド）](#拡張項目カスタムフィールド)
- [Topics API オペレーション](#topics-api-オペレーション)
- [コンテンツCRUD操作](#コンテンツcrud操作)
- [フィルタークエリ](#フィルタークエリ) → 詳細は [references/filter-query.md](references/filter-query.md)
- [ファイル・CSV操作](#ファイルcsv操作) → 詳細は [references/file-operations.md](references/file-operations.md)

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
| 拡張項目 | カスタムフィールド（最大99個） |

## 拡張項目（カスタムフィールド）

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
      "topics_flg": 1,
      "category_id": 1,
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
    topics_flg: 1,           // 1: 公開, 0: 非公開
    category_id: 1,
    open_ymd: '2024-12-01',  // 予約公開開始日
    close_ymd: '2024-12-31', // 公開終了日
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
| `=`, `!=` | `filter=category_id = 1` |
| `>`, `>=`, `<`, `<=` | `filter=ymd >= '2024-01-01'` |
| `contains` | `filter=subject contains 'キーワード'` |
| `in`, `not_in` | `filter=category_id in [1, 2, 3]` |

複合条件: `filter=(category_id = 1 or category_id = 2) and topics_flg = 1`

ソート: `order_by=ymd desc`

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

## ベストプラクティス

- **キャッシュ活用**: エンドポイント設定で `キャッシュ: 86400`（1日）を設定。更新時は自動クリア
- **ページネーション**: `pageID` と `cnt` パラメータで分割取得

## 関連ドキュメント

- `docs/tutorials/adding-a-topics.md` - コンテンツ定義作成
- `docs/tutorials/bulk-upload-in-csv.md` - CSVアップロード
- `docs/management/content-structure-topics.md` - コンテンツ構造
- `docs/reference/filter-query.md` - フィルタークエリ詳細
