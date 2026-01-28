# ファイル操作・CSVインポート

## ファイルアップロード

### 1. ファイルをアップロード

```javascript
async function uploadFile(file) {
  const formData = new FormData()
  formData.append('file', file)

  const response = await fetch('/rcms-api/1/files/upload', {
    method: 'POST',
    credentials: 'include',
    body: formData
  })

  const result = await response.json()
  return result.file_id
}
```

### 2. コンテンツに紐付け

```javascript
// アップロード後、file_idをコンテンツに紐付け
const fileId = await uploadFile(file)

await fetch('/rcms-api/1/news/insert', {
  method: 'POST',
  credentials: 'include',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    subject: 'タイトル',
    ext_col_02: {
      file_id: fileId,
      desc: 'ファイルの説明'
    }
  })
})
```

### 画像URL形式

```
https://{サイトキー}.g.kuroco-img.app/files/{ディレクトリ}/{ファイル名}
```

画像変換パラメータ:
```
?width=300&height=200&fit=cover
```

## CSVインポート/エクスポート

### 一括アップロード（bulk_upsert）

```javascript
async function bulkUpsert(items) {
  const response = await fetch('/rcms-api/1/news/bulk', {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      list: items.map(item => ({
        topics_id: item.id,  // 既存更新の場合
        subject: item.title,
        contents: item.body,
        ymd: item.date,
        topics_flg: 1
      }))
    })
  })

  return response.json()
}

// 使用例
await bulkUpsert([
  { title: 'タイトル1', body: '本文1', date: '2024-01-01' },
  { id: 123, title: '更新タイトル', body: '更新本文' }  // 既存更新
])
```

## カテゴリ管理

### カテゴリ一覧取得

```
パス: categories
カテゴリー: コンテンツ
モデル: TopicsCategory
オペレーション: list
topics_group_id: {グループID}
```

### レスポンス構造

```json
{
  "list": [
    {
      "topics_category_id": 1,
      "category_nm": "カテゴリ名",
      "parent_id": 0,
      "category_weight": 1,
      "child": [
        {
          "topics_category_id": 2,
          "category_nm": "子カテゴリ",
          "parent_id": 1
        }
      ]
    }
  ]
}
```

## タグ管理

### タグの設定

```javascript
// コンテンツ作成/更新時
{
  "subject": "タイトル",
  "tag": ["タグ1", "タグ2", "タグ3"]
}
```

### タグでフィルター

```javascript
const params = new URLSearchParams({
  filter: "tag contains 'タグ1'"
})
```

## 閲覧/編集制限

### 閲覧制限の種類

| 種類 | 説明 |
|------|------|
| 選択なし | 全員閲覧可能 |
| グループ制限 | 特定グループのメンバーのみ |
| メンバーカスタム検索 | 条件に合致するメンバーのみ |

### 制限適用の優先順位

1. コンテンツ定義の設定
2. カテゴリの設定
3. 個別コンテンツの設定
