# コンテンツ定義: 読み取りキーと仕様書の列の対応

SKILL.md の Step 3（収集）と Step 4（生成）で、コンテンツ定義のページを書くために
**どのツールのどのキーを、仕様書のどの列に落とすか**の対応表。

キー名から意味が読み取れず推測で埋められないため、ここだけは明示する。
往復運用（[apply-changes.md](apply-changes.md)）の精度は項目表の正確さに依存する。

---

## 1. どちらのツールを使うか

| 入口 | 使う条件 |
|------|---------|
| `topics-describe` | 項目表だけが要る定義。識別子・型・必須・選択肢・繰り返し上限まで揃う |
| `topics_group-get` | 下の「`topics-describe` が返さないもの」が要る定義。**`schema/contents/` に原本を残す方針なら全定義で必要**（`topics-describe` は入力スキーマであって定義そのものではない） |

**`topics-describe` が返さないものは4つ。**

| 返さないもの | これが要る場面 |
|------------|--------------|
| relation の参照先 `group_id` | ER図に関係を描くとき。**関係を持つ定義は実質 `topics_group-get` が要る** |
| `searchable` | 検索対象の指定を補足列に載せるとき |
| 項目グループの親子構造（`ext_parent_slug` / `ext_group_id`） | グループ単位で小見出しを立てて表を分けるとき |
| 定義レベル設定（`writer_groups` / `secure_level` / `need_application_groups` / `no_use_ymd` / `contents_type_cnt` 等） | 公開制御セクション（下の第4節） |

出典: Kuroco 本番テナント1件・7定義（12/14/16/17/19/20/22）での実測（2026-08-24、読み取りのみ）と
`nfs/lib/modules/topics/class/extension.php`（`maxItems` = `:3563` / `required` = `:3269` / json の `limits.schema` = `:3511-3512`）。

---

## 2. `topics-describe` から項目表を組む

`field_map.extension_fields` が項目ごとに以下を直接返す。

| 仕様書の列 | キー |
|-----------|------|
| 識別子 | `ext_slug` |
| 書き込みキー / APIレスポンスキー | `write_key` / `response_key` |
| 管理画面の列名 | `admin_column` |
| 型 | `ext_type`、および入力スキーマ側の `x-kuroco-type`（**文字列**で入る: `text` / `relation` / `csvtable` / `bool` / `number` …） |
| 繰り返し | `repeatable`、上限は入力スキーマの `maxItems` |

入力スキーマ側（各 write variant）から取るもの:

| 仕様書の列 | キー |
|-----------|------|
| 必須 | その variant の `required` 配列に識別子が入っているか |
| 選択肢 | `enum`（キー）と `enumNames`（表示ラベル）の対 |
| json 項目のスキーマ | 項目に設定された JSON Schema がそのまま入る |

**`x-kuroco-type` が型名を文字列で返すので、第3節の数値 → 型名の変換は要らない。**
数値の `type_N` を読むのは `topics_group-get` を使ったときだけ。

---

## 3. `topics_group-get` の `formData` から項目表を組む

`_N` は項目の連番。

| 仕様書の列 | `formData` のキー | 注意 |
|-----------|-----------------|------|
| 識別子 | `ext_slug_N`（空なら `ext_col_nm_N` = `ext_1` 等のスロット名） | **どちらも書かない行を作らない**——識別子が無い行は反映時に解決できない |
| 名称 | `title_N` | |
| 型 | `type_N` は**数値**（`0`=テキスト, `2`=セレクト, `35`=数値, `8`=日付, `9`=ファイル…） | 数値→型名は `/kuroco-content-structure` の Field Type Reference が正。数値のまま書かない。**この対応表があるのはコンテンツ定義の `ext_type` だけ。** フォーム（`inquiry` の `cols[].type`）など対応表が無いモジュールでは、値の内容から推定して型名を書き「（推定）」と付け、確定は手動確認リストに回す——数値をそのまま残すのは最後の手段 |
| 必須 | `limits_N.required`（`"1"` で必須。キー自体が無ければ任意） | `limits_N.searchable` は検索対象の指定。補足列に回す |
| 繰り返し | `ext_group_loop_N`（`1` は繰り返しなし、`20` なら最大20行） | |
| 項目グループ | グループ先頭の項目に `ext_parent_slug_N`（識別子）と `ext_parent_col_nm_N`（表示名）が入り、2件目以降のメンバーは `ext_group_id_N` = 先頭項目の `topics_group_ext_id_N` で連なる | グループ単位で小見出しを立てて表を分ける |
| 選択肢 | `options_N`（キー→ラベルの連想配列） | **`ext_option_N` の生文字列（`draft::default::下書き`）をそのまま書かない。** `::default::` は既定値マーカーでラベルの一部ではない。既定値は `default_value_N` |

---

## 4. 定義レベル設定 → 仕様書での言い換え

**設定の羅列ではなく意図を復元する。** 設定値は根拠として括弧で併記する（開発者向け詳細度のとき）。
いずれも `topics_group-get` にしか入らない（`topics-describe` では取れない）。

| 設定 | 仕様書での書き方 |
|------|----------------|
| `secure_level`（group_id のカンマ区切り） | 「閲覧できるのは {グループ名} のみ」。空なら「全体公開」 |
| `writer_groups` | 「登録・編集できるのは {グループ名}」 |
| `need_application_groups`（`"0"` 以外） | 「{グループ名} の更新は承認を経てから公開される」（→ workflow.md） |
| `my_topics_only_limit_groups`（`"0"` 以外） | 「{グループ名} は自分が登録したレコードしか扱えない」 |
| `non_public_flg=1` | 「公開APIには出さない内部向けの定義」 |
| `contents_type_cnt` | 「カテゴリを {n} 系統持つ」。`0` ならカテゴリ未使用としてセクションを削る |
| `data_limit`（`0` 以外） | 「レコード数を {n} 件に制限」 |
| `no_use_ymd=1` / `post_time_flg=1` | 「日付を使わない」/「時刻まで持つ」 |
