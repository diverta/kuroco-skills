# フィルタークエリ詳細

公式リファレンス: [Filter検索のパラメータ](https://kuroco.app/ja/docs/reference/filter-query/)

## 基本構文

```
filter={field} {operator} {value}
```

## 値の書き方（重要）

- **文字列の値は二重引用符で囲む。** `subject contains "キーワード"`
- **シングルクォートは使えない。** `subject contains 'キーワード'` は引用符が値の一部として
  扱われ、**エラーにならないまま0件**になる（値に空白を含む場合は構文エラー）
- 空白・記号を含まない値は引用符なしでも通る（`topics_flg = 1`、`slug = news`）
- 演算子の前後には半角スペースを入れる。`contains` などの語形演算子ではスペースが必須
- `and` / `or` は大文字小文字どちらでもよい

## 演算子一覧

| 演算子 | 説明 | 例 | 別名 |
|--------|------|-----|------|
| `=` | 等しい | `filter=contents_type = 1` | `eq` |
| `!=` | 等しくない | `filter=topics_flg != 0` | `ne` |
| `>` | より大きい | `filter=topics_id > 100` | `gt` |
| `>=` | 以上 | `filter=ymd >= "2024-01-01"` | `gte` |
| `<` | より小さい | `filter=topics_id < 100` | `lt` |
| `<=` | 以下 | `filter=ymd <= "2024-12-31"` | `lte` |
| `contains` | 部分一致（大文字小文字を区別） | `filter=subject contains "キーワード"` | — |
| `icontains` | 部分一致（区別しない） | `filter=subject icontains "keyword"` | — |
| `ncontains` | 部分一致しない（区別する） | `filter=subject ncontains "除外"` | — |
| `nicontains` | 部分一致しない（区別しない） | `filter=subject nicontains "exclude"` | — |
| `startswith` / `endswith` | 前方／後方一致 | `filter=subject startswith "【重要】"` | `i` / `n` / `ni` 派生あり |
| `in` | いずれかに一致 | `filter=contents_type in [1, 2, 3]` | — |
| `nin` | いずれにも一致しない | `filter=contents_type nin [1, 2]` | — |
| `all` | すべて含む（複数値カラム向け） | `filter=secure_level all [1, 2]` | — |
| `nall` | すべて含まない（複数値カラム向け） | `filter=secure_level nall [1, 2]` | — |
| `= null` | NULL である | `filter=ext_col_01 = null` | `!= null` で NOT NULL |

**`not_contains` / `not_in` という演算子は存在しない**（`Invalid operator` になる）。
否定形は `n` 接頭辞（`ncontains` / `nin`）。

- `null` は**小文字**で書く。`= null` → `IS NULL`、`!= null` → `IS NOT NULL`。
  大文字の `NULL` は `"NULL"` という文字列との比較になる
- `= ""`（空文字）は NULL も一致対象に含む
- `all` / `nall` は複数値を持つカラム向け。単一値のカラムに使うと
  `Invalid operator for the specified column` になる
- 配列の末尾にカンマを残すと構文エラーになる（`in [1, 2, ]` は不可）
- 値の中で `"` を使う場合は `\"` とエスケープする（`subject = "He said \"Hello\""`）。
  バックスラッシュ自体は `\\`。**引用符を2つ重ねる書き方（`""`）はエスケープにならず構文エラー**

## 複合条件

カテゴリのフィールド名は **`contents_type`**（`category_id` というフィールドは存在しない）。

```javascript
// AND条件
const params = new URLSearchParams({
  filter: 'contents_type = 1 and ymd >= "2024-01-01"'
})

// OR条件
const params = new URLSearchParams({
  filter: 'contents_type = 1 or contents_type = 2'
})

// 複合条件
const params = new URLSearchParams({
  filter: '(contents_type = 1 or contents_type = 2) and topics_flg = 1'
})
```

JavaScript では、フィルタ式の外側をシングルクォート（またはバッククォート）にして、
**値の二重引用符をそのまま式の中に残す**のが安全。

## 相対日付モード

`{field} {operator}:relatively {value}` の形式で、今日・昨日などの相対指定ができる。

```javascript
const params = new URLSearchParams({
  filter: 'ymd >=:relatively "today"'
})
```

指定できる値は公式リファレンスの
[相対日付モードで指定できるオペレータと値](https://kuroco.app/ja/docs/reference/filter-query/) を参照。

## ソート（order_query）

パラメータ名は **`order_query`**（`order_by` ではない）。
値は `{フィールド}={ASC|DESC}` の形式で、複数指定はカンマ区切り。

```javascript
// 降順（新しい順）
const params = new URLSearchParams({
  order_query: 'ymd=DESC'
})

// 昇順
const params = new URLSearchParams({
  order_query: 'topics_id=ASC'
})

// 複数条件
const params = new URLSearchParams({
  order_query: 'contents_type=ASC, ymd=DESC'
})
```

`ymd desc` のようなスペース区切りの書き方は形式チェックで拒否される。

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
    // 値は二重引用符で囲み、値の中の " と \ はエスケープする
    const escaped = keyword.replace(/\\/g, '\\\\').replace(/"/g, '\\"')
    filters.push(`subject contains "${escaped}"`)
  }
  if (categoryId) {
    filters.push(`contents_type = ${categoryId}`)
  }

  const params = new URLSearchParams({
    filter: filters.join(' and '),
    order_query: 'ymd=DESC'
  })

  const response = await fetch(`/rcms-api/1/news?${params}`)
  return response.json()
}
```
