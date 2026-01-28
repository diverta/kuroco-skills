# フィルタークエリ詳細

## 基本構文

```
filter={field} {operator} {value}
```

## 演算子一覧

| 演算子 | 説明 | 例 |
|--------|------|-----|
| `=` | 等しい | `filter=category_id = 1` |
| `!=` | 等しくない | `filter=topics_flg != 0` |
| `>` | より大きい | `filter=topics_id > 100` |
| `>=` | 以上 | `filter=ymd >= '2024-01-01'` |
| `<` | より小さい | `filter=topics_id < 100` |
| `<=` | 以下 | `filter=ymd <= '2024-12-31'` |
| `contains` | 部分一致 | `filter=subject contains 'キーワード'` |
| `not_contains` | 部分一致しない | `filter=subject not_contains '除外'` |
| `in` | いずれかに一致 | `filter=category_id in [1, 2, 3]` |
| `not_in` | いずれにも一致しない | `filter=category_id not_in [1, 2]` |

## 複合条件

```javascript
// AND条件
const params = new URLSearchParams({
  filter: "category_id = 1 and ymd >= '2024-01-01'"
})

// OR条件
const params = new URLSearchParams({
  filter: "category_id = 1 or category_id = 2"
})

// 複合条件
const params = new URLSearchParams({
  filter: "(category_id = 1 or category_id = 2) and topics_flg = 1"
})
```

## ソート

```javascript
// 降順（新しい順）
const params = new URLSearchParams({
  order_by: 'ymd desc'
})

// 昇順
const params = new URLSearchParams({
  order_by: 'topics_id asc'
})

// 複数条件
const params = new URLSearchParams({
  order_by: 'category_id asc, ymd desc'
})
```

## ページネーション

```javascript
const params = new URLSearchParams({
  pageID: '2',    // ページ番号（1始まり）
  cnt: '20'       // 1ページあたりの件数
})

const response = await fetch(`/rcms-api/1/news?${params}`)
```

## 全件取得のページネーション実装

```javascript
async function fetchAllNews() {
  let allItems = []
  let page = 1
  let hasMore = true

  while (hasMore) {
    const response = await fetch(`/rcms-api/1/news?pageID=${page}&cnt=100`)
    const data = await response.json()

    allItems = [...allItems, ...data.list]
    hasMore = page < data.pageInfo.totalPageCnt
    page++
  }

  return allItems
}
```

## 検索機能の実装例

```javascript
async function searchNews(keyword, categoryId) {
  const filters = []

  if (keyword) {
    filters.push(`subject contains '${keyword}'`)
  }
  if (categoryId) {
    filters.push(`category_id = ${categoryId}`)
  }

  const params = new URLSearchParams({
    filter: filters.join(' and '),
    order_by: 'ymd desc'
  })

  const response = await fetch(`/rcms-api/1/news?${params}`)
  return response.json()
}
```
