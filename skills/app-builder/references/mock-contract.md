# モックデータ契約とAPI切り替えパターン

フェーズ1のモックデータを**Kuroco APIの実レスポンス形（契約）**で作るためのリファレンス。
この契約を守ると、フェーズ4は「クライアント層の実装差し替え + .env設定」だけで完了する。

## 原則

1. **モックはレスポンス全体の形を再現する**（`list` の配列だけ持たない。`pageInfo` も含める）
2. **UIはクライアント層のマッパーを通した「アプリ用の型」だけを見る**。`ext_col_01` のような
   生のフィールド名をUIコンポーネントに書かない（拡張項目の番号はバックエンド構築後に確定するため）
3. **フィールドの過不足はマッパーで吸収する**。実接続時に画面差分が出たら、直すのはマッパーだけ

## Kuroco APIレスポンス契約

> 外形（`{ list, pageInfo }` / `{ details }`）はモデル・オペレーションで決まる仕様で、サイトによって変わらない。
> 変わるのはカラム絞り込みと拡張項目の割当。フェーズ3の完了後、**Admin MCP の読み取りツールで**
> エンドポイント定義とコンテンツ定義を取得し、モック側を実物に合わせて訂正すること
> （マッパーで差分を隠さない）。ブラウザでの確認手順は取らない。

### 拡張項目のキー名は `ext_slug` で決める（付けない場合はサイト設定で2通りに分かれる）

`ext_slug` を設定しない場合、拡張項目のキー名は**サイト単位で `ext_1` 形式（連番）と `ext_col_01` 形式（ゼロ埋め2桁）に分かれる**。**推測してはいけない。** Admin MCP の `whoami` が `site.topics_ext_key_format` でそのサイトの命名を返すので、そこで確認する。

| `site.topics_ext_key_format` | キー名の例 |
|-----------------------------|-----------|
| `ext_<n>` | `ext_1`, `ext_2`, … |
| `ext_col_<nn>` | `ext_col_01`, `ext_col_02`, … |

**したがって、コンテンツ定義を作るときは必ず `ext_slug` を設定する。** スラッグを設定すればフロントAPIのキーはそのスラッグになり、この分岐そのものが起きない（フィールドを並べ替えても壊れない）。→ `/kuroco-content-structure`

- モックのキーは**そのエンドポイントの実レスポンス**に合わせる。フェーズ3の突き合わせで1項目ずつ確認する
- `ext_slug` が無い既存定義を相手にする場合は、`whoami` の `topics_ext_key_format` でサイトの命名を確認し、**どの番号がどの項目かは `topics-describe`（グループ単位の正）で確定させる**。どちらの形式であれUIには持ち込まない（→ 原則2）
- 4-4 の書き戻しで集約ファイルに入れるのは「実際のキー名 ↔ アプリ用フィールド名」の対応

### レスポンスに出てこない標準項目に注意

「標準機能で対応できる」ことと「その値がAPIレスポンスから読める」ことは別である。日付まわりは特に間違えやすい:

| 項目 | レスポンスに出るか | 使い方 |
|------|-----------------|--------|
| `ymd` | **出る** | コンテンツの日付。「掲載日」「公開日」として画面に出すのはこれ |
| `inst_ymdhi` / `update_ymdhi` | **出る** | 作成・更新日時（ISO8601） |
| `open_flg` | **出る** | 公開状態 |
| `open_type` / `open_sta_date` / `open_end_date` | **出ない**（実測で確認） | 予約公開・公開期間の**制御専用**。値を画面に表示することはできない |

- **予約公開の日付を画面に出したい場合は `ymd` を使う。** 拡張項目を別に作る必要はない
- `open_sta_date` は `open_type` が既定（`open`）のままだと**保存されない**。予約公開を設定するには `open_type: "sitei"` を併せて渡す
- 一般則として、**「制御に使う設定値」がレスポンスに出ると仮定しない。** モックに入れた項目が実レスポンスに存在するかは、フェーズ3の突き合わせで1項目ずつ確認する

### 一覧（Topics::list）

**成功レスポンスにも `errors` と `messages` が入る**（実測。空配列で返る）。モックにも必ず含めること — 省くと、実接続に切り替えた瞬間にこれらを参照するコードの挙動が変わる。

> **`if (raw.errors)` と書いてはいけない。** 成功時の値は `[]` で、JavaScript では空配列は truthy。
> 判定は `if (raw.errors?.length)` にする。

```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1,
      "subject": "タイトル",
      "contents": "<p>本文HTML</p>",
      "ymd": "2026-08-01",
      "contents_type": 1,
      "contents_type_nm": "カテゴリ名",
      "recipe_note": "拡張項目の値（ext_slug = recipe_note を設定した場合）",
      "main_image": { "url": "https://.../image.jpg", "desc": "画像説明" }
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

### 詳細（Topics::details）

```json
{
  "details": {
    "topics_id": 1,
    "subject": "タイトル",
    "contents": "<p>本文HTML</p>",
    "ymd": "2026-08-01",
    "recipe_note": "拡張項目の値（ext_slug = recipe_note）"
  }
}
```

### 拡張項目のAPIレスポンス形（型別）

キー名は `ext_slug` に設定した値になる（下表は例）。**見るべきは値の形**で、キー名は自分で決められる。

| フィールド型 | レスポンス例 |
|-------------|-------------|
| text / textarea / wysiwyg | `"lead_text": "値"` |
| number | `"price": 100` |
| date | `"published_on": "2026-08-01"` |
| select（単一） | `"category_key": { "key": "選択肢キー", "label": "表示ラベル" }` ——**文字列ではなくオブジェクト**。画面に出すのは `label`、`filter` に渡すのは `key` |
| checkbox（複数） | `"tags": ["a", "b"]` |
| image / file | `"main_image": { "id": "...", "url": "https://...", "desc": "", "url_org": "https://..." }` |
| link | `"external_link": { "url": "https://...", "title": "リンク名" }` |
| relation | `"related_article": { "topics_id": 123, "subject": "参照先タイトル" }` ——**既定はid＋ラベル相当のみ**。参照先の他項目まで画面に出すなら、別途その定義を取得するかエンドポイントの後処理が必要 |
| 繰り返し（単項目に繰り返しを設定） | `"repeat_texts": ["text1", "text2"]` ——値が配列になる。途中の削除は前方に詰められ、空要素は含まれない |
| グループ化（`ext_group` 有効） | `"photos": { "photo": { "id": "...", "url": "..." }, "caption": "説明" }` ——グループが1オブジェクトにまとまる。キー名はグループのslug |
| 繰り返し＋グループ化（`ext_group` 有効） | `"items": [ { "name": "品名", "qty": 2 }, { "name": "品名2", "qty": 1 } ]` ——**明細を繰り返しフィールドグループで持つ場合の形。モックはこの形で作る** |

**作成者（コンテンツ所有者）の属性は既定では返らない。** 「誰が出した依頼か」「投稿者名」を画面に出すなら、`Topics::list` / `details` の **`add_owner_info_cols`**（取得したい所有者属性を指定。例: `email,nickname`）を有効にする。会員に紐づく属性を出す場合は `add_member_info_cols`。**要件側で頻出する「作成者・更新者・所属」は、日付項目と同じく「出る／出ない」を先に確認してからモックのキーを決める**（後から足すとマッパーと画面の両方を直すことになる）。

**グループ化した項目のレスポンス形は、エンドポイントの `ext_group` パラメータの有無で変わる。** 有効なら上表のとおりオブジェクト／オブジェクト配列にまとまり、無効なら項目ごとに分かれて返る（繰り返し＋グループで無効の場合は項目ごとの配列になり、空要素も含まれて配列長が揃う）。**モックを作る前に、そのエンドポイントで `ext_group` を有効にするかを決めて統一する**（詳細は `/kuroco-docs` の `reference-content-1.md`「グループ化・繰り返しを行ったコンテンツ項目の制御」）。

### 認証（Authentication）

```json
// POST /login （Cookie認証: credentials: 'include' が必須）
{ "grant_token": "...", "status": 0, "member_id": 123 }

// GET /profile （ログイン状態確認。未ログインは 401/403）
{ "member_id": 123, "email": "user@example.com", "name1": "姓", "name2": "名" }
```

**動的アクセストークン認証の場合**（クロスドメインSPAで推奨）: `login` で取得した `grant_token` を
`token` エンドポイントにPOSTして `access_token`（+ `refresh_token`）を取得し、以降のリクエストに
`X-RCMS-API-ACCESS-TOKEN: {access_token}` ヘッダーを付与する（`credentials: 'include'` は不要）。
モック時は認証ヘッダーの有無を無視してよいが、クライアント層にはヘッダー付与の分岐を最初から入れておく。

### お気に入り（Favorite）・コメント（Comment）・フォーム（InquiryMessage）

```json
// GET /favorites （Favorite::list。module_id = topics_id）
{ "list": [ { "module_type": "topics", "module_id": 1 } ], "pageInfo": { "totalCnt": 2 } }

// POST /favorites/insert  body: { "module_type": "topics", "module_id": 1 }
// POST /comments/insert   body: { "module_type": "topics", "module_id": 1, "comment": "..." }
// POST /form/send         body: フォーム項目（フォーム定義に依存）
```

### エラーレスポンス

```json
{ "errors": [ { "code": "...", "message": "エラーメッセージ" } ], "x-rcms-request-id": "..." }
```

主要コード: 401（未認証）/ 403（権限・CORS）/ 404 / 429（流量制限）。
モックにも「0件」「エラー」のフィクスチャを1つずつ用意すると、実接続前に空状態・エラー表示を確認できる。

## 実装パターン: Vite + Vue 3（SPA・シンプルなアプリの既定）

```
src/lib/kuroco/types.ts      # アプリ用の型（Article等）
src/lib/kuroco/mappers.ts    # 生レスポンス → アプリ用の型
src/lib/kuroco/client.ts     # 切り替えの入口（これだけをUIから使う）
src/lib/kuroco/mock/articles.ts  # Kurocoレスポンス形のフィクスチャ
```

```typescript
// src/lib/kuroco/client.ts — モック/実APIの切り替え
const USE_MOCK = import.meta.env.VITE_USE_MOCK === 'true'
const API_BASE = import.meta.env.VITE_KUROCO_API_BASE ?? ''

export async function fetchArticles(page = 1) {
  const raw = USE_MOCK
    ? (await import('./mock/articles')).articleList
    : await fetch(
        `${API_BASE}/rcms-api/1/articles?pageID=${page}&cnt=10`,
        { credentials: 'include' }  // トークン認証なら headers: { 'X-RCMS-API-ACCESS-TOKEN': token } に置き換え
      ).then(r => r.json())
  return { articles: raw.list.map(toArticle), pageInfo: raw.pageInfo }
}
```

```bash
# .env — フェーズ1
VITE_USE_MOCK=true
# .env — フェーズ4（切り替えはこの2行の変更のみ）
VITE_USE_MOCK=false
VITE_KUROCO_API_BASE=https://{site_key}.g.kuroco.app
```

開発時にCookie認証を使う場合は `vite.config.ts` の `server.proxy` でAPIを同一オリジンに見せると
ブラウザのCookie制限を受けない。デプロイは `vite build` → `dist/` を KurocoFront へ
（SPA用 `kuroco_front.json` の rewrites 設定は `/kuroco-frontend-integration` 参照）。

## 実装パターン: Nuxt 3

```
composables/useKurocoApi.ts   # 切り替えの入口（これだけをUIから使う）
lib/kuroco/types.ts           # アプリ用の型（Article等）
lib/kuroco/mappers.ts         # 生レスポンス → アプリ用の型
lib/kuroco/mock/articles.ts   # Kurocoレスポンス形のフィクスチャ
```

```typescript
// lib/kuroco/types.ts — UIが使う型（Kurocoの生フィールド名を出さない）
export interface Article {
  id: number
  title: string
  body: string
  date: string
  imageUrl: string | null
}

// lib/kuroco/mappers.ts — 拡張項目の対応はここに集約
export const toArticle = (raw: any): Article => ({
  id: raw.topics_id,
  title: raw.subject,
  body: raw.contents,
  date: raw.ymd,
  // コンテンツ定義で ext_slug（ここでは main_image）を設定しておき、スラッグで受ける。
  // ext_slug 未設定の既存定義を相手にする場合のみ位置依存のキーになるので、
  // whoami の site.topics_ext_key_format で形式を確認し、番号は topics-describe で確定させる。
  imageUrl: raw.main_image?.url ?? null,
})

// composables/useKurocoApi.ts — モック/実APIの切り替え
export const useArticles = (page = 1) => {
  const config = useRuntimeConfig()
  return useAsyncData(`articles-${page}`, async () => {
    const raw = config.public.useMock
      ? await import('~/lib/kuroco/mock/articles').then(m => m.articleList)
      : await $fetch<any>(`${config.public.kurocoApiBase}/rcms-api/1/articles`, {
          params: { pageID: page, cnt: 10 },
          credentials: 'include',
        })
    return { articles: raw.list.map(toArticle), pageInfo: raw.pageInfo }
  })
}
```

```bash
# .env — フェーズ1
NUXT_PUBLIC_USE_MOCK=true
# .env — フェーズ4（切り替えはこの2行の変更のみ）
NUXT_PUBLIC_USE_MOCK=false
NUXT_PUBLIC_KUROCO_API_BASE=https://{site_key}.g.kuroco.app
```

## 実装パターン: Next.js

```typescript
// lib/kuroco/client.ts
const USE_MOCK = process.env.NEXT_PUBLIC_USE_MOCK === 'true'
const API_BASE = process.env.NEXT_PUBLIC_KUROCO_API_BASE ?? ''

export async function fetchArticles(page = 1) {
  const raw = USE_MOCK
    ? (await import('./mock/articles')).articleList
    : await fetch(
        `${API_BASE}/rcms-api/1/articles?pageID=${page}&cnt=10`,
        { credentials: 'include' }
      ).then(r => r.json())
  return { articles: raw.list.map(toArticle), pageInfo: raw.pageInfo }
}
```

## フェーズ4: 切り替え手順と検証

1. `.env` を実API設定に変更（上記）
2. フェーズ2で**モックと同じ内容のサンプルコンテンツを投入してある**ので、全画面でモック時と同じ表示になることを確認する
3. 差分が出たら **Admin MCP で取得したエンドポイント定義・コンテンツ定義**とモックを比較し、**モック側を実物に合わせて訂正**する（マッパーで吸収して隠さない）
   - 典型例: 拡張項目の番号ずれ（`ext_col_01` → `ext_col_02`）、画像フィールドがオブジェクトだった、カテゴリが `contents_type_nm` で返る
4. CORSエラー（403 / ブラウザのCORSエラー）が出たら `/kuroco-api-content` のCORS設定を確認（オリジン許可、Cookie認証なら `Allow-Credentials: true`）
5. 確認後、モックのフィクスチャは削除せず残してよい（開発・テスト用に `USE_MOCK=true` で引き続き使える）
