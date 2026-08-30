# 調査に使う Admin MCP ツール リファレンス

正確な引数は各ツールの `inputSchema`（`tools/list`）が正。ここには
スキーマに現れない**返却値のフォーマット**と**制約**をまとめる。

---

## usage-get（module: `site`）

利用状況（費用・利用量）を取得する。

**引数**

| 引数 | 説明 |
|------|------|
| `ym` | 対象年月 `YYYY-MM`（省略時は当月） |
| `chart_begin_ym` / `chart_end_ym` | 月次系列の範囲 `YYYY-MM`（省略時は直近6ヶ月〜当月） |
| `encoding` | `utf8` / `sjis`（CSV 出力時のみ意味を持つ） |

CSV が必要なら `download: true` を付ける。`download.download_url` に一時ダウンロードリンクが返る（`encoding` が適用される）。

**site_id は指定できない。** MCP エンドポイントは接続中のサイトに束縛されている。
他環境（dev/stg）の数字が必要なら、その環境の Admin MCP に接続して取得する。

**返却**

| キー | 内容 |
|------|------|
| `cost_site` | 接続中サイトの `ym` 月の費目別コスト（`disp_nm` / `value`）。合計を含む。**機械可読なキーは持たない** |
| `cost_all_sites` | 親サイト配下の**全環境合計**。接続先が親サイトのときのみ返る |
| `cost_monthly` | 費目別の月次系列（`key` / `disp_nm` / `data[]`）。`data` は `chart_begin_ym` から順に並ぶ |
| `cost_daily` | 費目別の日次系列（同じ構造、`ym` の月） |
| `usage_list` | 日別の生カウント行＋末尾に合計行 |

`usage_list` / `cost_daily` は**当日を含まない**（前日まで）。`cost_site` / `cost_monthly` は
月の集計値なので、進行中の月は途中経過になる。

`usage_list` の主なカラム: `date` / `cached_api_count` / `api_count` / `api_traffic` /
`api_execution` / `admin_count` / `admin_execution_time` / `front_traffic` / `img_traffic` /
`mail_count` / `openai_unit` / `batch_execution_time` / `ai_agent_execution_time` /
`db_bytes` / `files_bytes` / `front_bytes` / `log_bytes` / `backup_bytes`。

費目キー（`cost_monthly[].key`）と利用状況項目の対応は `cost-model.md` を参照。

---

## api_analytics-list（module: `logs`）

API アクセスログを**エンドポイント単位に集計**して返す。傾向分析はまずこれを使う。

**引数**

| 引数 | 説明 |
|------|------|
| `timestamp_start` / `timestamp_end` | **必須**。`YYYY-MM-DD HH:MM`（秒は内部で補完）。**1回の範囲は最大35日** |
| `filter` | フィルタ式（→ [フィルタ式の書き方](#フィルタ式の書き方)）。仮想カラム `keyword` が URL 検索にマッピングされている（`keyword contains "..."`） |
| `filters` | `{"filter": "...", "order": "..."}` を JSON 文字列にしたもの（`filter` + `sort` の代替） |
| `sort` | `hit` / `execution_time` / `execution_time_additional` / `body_size` |
| `desc` | `true` で降順 |
| `cnt`（既定100） / `pageID` | ページング。**`perPage` は宣言されておらず拒否される**（inputSchema が `additionalProperties: false` のため、未宣言の引数はエラーになる） |

`columns` は**無い**（列の絞り込みはできない）。
logs モジュールでは CSV ダウンロードとログ削除が MCP に公開されていない（CSV は管理画面から取得する）。

**返却行（グループ化: メソッド × api_id × api_uri_id × cache_status × status）**

| フィールド | 内容・フォーマット |
|-----------|------------------|
| `api_id` | **API タイトルに解決済み**（`/direct/` 系は `admin_mcp` / `admin_api` / `system`。Admin MCP 自身のリクエストも分離して見える） |
| `api_uri_id` | **`/rcms-api/{api_id}/{api_uri}` に解決済み**（`/direct/` 系はパス接頭辞） |
| `request` | HTTP メソッド |
| `cache_status` | `HIT` / `MISS` / `PASS`（生ログでは `ERROR` も記録される） |
| `status` | HTTP ステータス |
| `hit` | 件数 |
| `execution_time` | 平均実行時間。`"426 ms"` の文字列。**`cache_status = HIT` の行は `" - "`** |
| `execution_time_additional` | 300ms 超過分の合計 = コンピューティング課金の実体。同じく HIT 行は `" - "` |
| `body_size` | 平均レスポンスサイズ。`"15.61 KB"` の文字列 |

既定の並びは `hit desc, execution_time desc, body_size desc`。

**フィルタは生の値に対して効く。** 表示が API タイトルでも条件は `api_id = 3`、
サイズはバイト数で書く。使えるカラム: `api_id` / `request` / `api_uri_id` /
`cache_status` / `status` / `hit` / `execution_time` / `execution_time_additional` / `body_size`。

**MCP の BigQuery コストガード（12時間制限・レート制限）の対象外**。
`logs` モジュールのツールは原則ガードの対象だが、`api_analytics` は
実装の除外リストに明示的に載っている（集計なので期間を延ばしても結果セットが増えず、
12時間に絞ると意味を失うため）。生ログツールとの最大の違いはここ。

ただし**コントローラ側の 35日上限は効く**（`timestamp_end - timestamp_start` が
35日を超えるとエラー。開始が終了より後の場合もエラー）。

---

## api_log-list（module: `logs`）

API アクセスログの**生ログ**（1行 = 1リクエスト）。

**引数**

| 引数 | 説明 |
|------|------|
| `timestamp_start` / `timestamp_end` | **必須**。`YYYY-MM-DD HH:MM`。**直近12時間以内の範囲のみ** |
| `filter` / `filters` | api_analytics と同じ形式（→ [フィルタ式の書き方](#フィルタ式の書き方)）。仮想カラム `keyword` は URL 検索にマッピングされている |
| `sort` / `desc` | ソート可能: `timestamp`（既定 desc）・`execution_time`・`body_size`。`desc` は boolean / 文字列いずれも可 |
| `cnt`（既定100） / `pageID` | ページング。**`perPage` は存在しない。** `api_analytics-list` と同じで、ページ件数の引数は `cnt` だけ |
| `columns` | 返す列を絞る（ログ行は横に広いので必ず使う） |

**MCP 専用のコストガード**（管理画面には無い制限）が 2 段でかかる。`logs` モジュールの
ツールは `api_analytics` を除いてすべて対象（`front_log-list` / `img_log-list` /
`edge_log-list` 等も同じ）。

1. **12時間の遡り上限**: 判定対象は `timestamp_start` のみ。12時間より前を指定すると
   「指定可能な最古の時刻」を含むエラーが返る。`timestamp_start` は必須で、
   欠落・不正形式もエラー
2. **レート制限**: 5秒の固定スロットで**呼び出し元メンバー単位に1回**。
   同一スロット内の2回目以降がエラーになるため、連続呼び出しは間隔を空ける

35日上限（`timestamp_end - timestamp_start`）も効くが、12時間の方が先に効くため
実務上は意識しなくてよい。DELETE / CSV ダウンロードは MCP に公開されていない。

**主なカラム**

`timestamp` / `cache_status` / `request`(メソッド) / `status` / `response` /
`uri`(データセット上は `url`) / `client_ip` / `api_access_token`（先頭16文字に切詰め） /
`execution_time` / `body_size` / `request_referer` / `request_user_agent` /
`request_accept` / `geo_city` / `geo_region` / `geo_country_code` / `io_info` /
`request_id`（CDN側の識別子） / `rcms_request_id`（アプリ側の識別子）。

同系のログツール（同じ制約・同じ引数）:
`front_log-list`（KurocoFront アクセス）、`img_log-list`（画像配信）、
`edge_log-list`（KurocoEdge。Edge サービスを使っていないサイトでは参照先データセットが
空のため実質使えない）、`api_request_log-list`、`batch_log-list`、
`custom_log-list`、`rcms_log-list`、`admin_log-list`。

---

## api-list / api_uri-list（module: `rcms_api`）

エンドポイント定義とキャッシュ設定の確認。

```json
// tool: api-list（引数なし）
{}
```
```json
// tool: api_uri-list
{ "api_id": <対象APIのID> }
```

`api` リソースのツールは 1 MODE = 1 ツールで、**MODE はサーバー側で自動的に付与される**。
引数に `MODE` を書く必要はない（書いても無視される）。

返却の外形は次のとおり。注目するのは `uri_data` 側で、`uri_method`（メソッドのパラメータ定義）は
本スキルの調査には使わない:

```
{ "uri_list": [ { "uri_data": {...}, "uri_method": {...} }, ... ] }
```

キャッシュ設定と利用実績を持つのはこのツールだけ（`api-export_openapi` には含まれない）。
**何らかの理由で取得できなかった場合は、そのAPIのキャッシュ設定を「未確認」としてレポートに明記する。**
確認できなかったエンドポイントを黙って対象外にすると、「TTL未設定のエンドポイントは無い」と
読める結論になってしまう。

`uri_data` には**設定と直近8日間の実績が同居している**:

| フィールド | 内容 |
|-----------|------|
| `api_uri_id` / `api_uri` / `http_method` | エンドポイントの識別 |
| `model_classpath` / `model_method` | 例: `Topics` / `list` |
| `cache_settings` | **JSON 文字列**で、形が一定しない。「キャッシュ無効」の表現が複数ある: `"[]"`（空配列）/ `null`（更新系エンドポイントは設定欄自体が無い）/ `"{}"` / `{"maxage": 0}`（明示的に0）。**`maxage` キーの有無で分岐する前に、パースして4形すべてを「無効」として扱う**。有効なのは `maxage` が1以上のときだけ。`cache_by_group` も同じオブジェクト内 |
| `rate_settings` | `limit_req` / `limit_slot` |
| `api_count` | 直近8日間の非キャッシュリクエスト数。`"1,234hits"` 形式、実績なしは `"-"` |
| `cached_api_count` | 直近8日間のキャッシュ済みリクエスト数。同上 |
| `body_avg` | 直近8日間の平均レスポンスサイズ（`"15.61 KB"`） |
| `exec_avg` | 直近8日間の平均実行時間（`"426ms"`） |

`cached_api_count ÷ (api_count + cached_api_count)` がそのエンドポイントの
**直近8日間のキャッシュ比率**。管理画面「エンドポイント一覧」の
「7日間の利用状況」と同じ数字である。

**同じ `api` リソースの書き込み系ツール**（`api-upsert` / `api_uri-upsert` /
`api-delete` / `api_uri-delete` / `api-cdn_cache_purge` / `api-annotation_cache_purge`）は
接続スコープに `rcms_api` があれば見える。調査中に誤って呼ばないこと。

- `api-cdn_cache_purge` は `api_uri_id`（1件）/ `api_uri_ids`（複数）/ `all: true`（全エンドポイント）の
  **ちょうど 1 つ**を取る。選択子なしは 400（以前の「省略時は暗黙の全パージ」は廃止）
- `api-annotation_cache_purge` は annotation キャッシュの再構築に加えて
  **全 API エンドポイントの CDN キャッシュも破棄する**
- KurocoFront / KurocoEdge のキャッシュは別ツール（`kuroco_front-cdn_cache_purge` /
  `edge-cdn_cache_purge`。後者は KurocoEdge 利用サイトでしか `tools/list` に出ない）

- `api-upsert` は `security` / `cors`（`origins` / `methods` / `headers` /
  `exposeHeaders` / `maxAge` / `allowCredentials`）/ `ip_whitelist` を受け付ける
- **`api_uri-upsert` は `cache_settings` を受け付けない。** UPSERT_URI の inputSchema に
  そのプロパティが無く `additionalProperties: false` のため、渡すと
  「undeclared top-level argument」またはスキーマ検証エラーで**拒否される**
  （エラー文にも "must be changed in the Admin UI" と出る）。
  DB／コントローラ側は `cache_settings` を保存できるので、これは MCP 層の制限であり、
  **キャッシュ期間・`cache_by_group` の変更は管理画面で行う**
- **更新時に省略したフィールドは既存値が保持される**（更新系は部分更新）。
  他の目的で `api_uri-upsert` を呼んでも、既存の `cache_settings` / `rate_settings` が
  消えることはない

---

## フィルタ式の書き方

ログ系ツールの `filter` は Kuroco DSL（SQL の WHERE 相当）で、
コンテンツ API の filter と同じパーサを使う。

```
cache_status = "MISS"
status = 400 AND cache_status = "PASS"
body_size > 100000
uri contains "/rcms-api/2/"
request_user_agent contains "bot"
geo_country_code != "JP"
status IN [400,404,500]
```

- **文字列リテラルは二重引用符。シングルクォートは使えない**（パーサは二重引用符のみを
  文字列として扱い、`'MISS'` は引用符ごと1つの値として比較されるためヒットしない）。
  空白・記号を含まない値は無引用符でも通る
- **演算子の前後に半角スペースを置く**（`status = 400`。`status=400` は不可）
- 演算子: `=` `!=` `>` `>=` `<` `<=` / `contains` `ncontains` `icontains` `nicontains` /
  `startswith` `endswith`（各 `n` / `i` 派生あり）/ `IN [v1,v2]` `nin [v1,v2]` /
  `= null` `!= null`（**null は小文字**。大文字 `NULL` は文字列 `"NULL"` との比較になる）。`AND` / `OR` / 括弧で連結できる（小文字 `and` / `or` も可）
- カラム名は**短縮名**（`url` ではなく `uri`）
- **値は表示値ではなく生の値**（`status` は `200`。`"200 OK"` ではない。
  サイズはバイト数、時間はミリ秒、`api_id` は数値 ID）
- `filters` に JSON で渡す場合のキーは `filter` と `order`（`"timestamp DESC"` の形）。
  `{"列名": "値"}` 形式のオブジェクトは**サポートされない**
