# Kurocoドキュメント: リファレンス / API（3/3）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- APIエラーレスポンス（`error`）
- Filter検索のパラメータ（`filter-query`）
- 関連しているデータを条件にしたfilter機能（`r-filter`）
- APIを使ったファイルのアップロードについて（`uploading-files-using-the-api`）


---

# APIエラーレスポンス

> 元ページ: `reference/error` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/error/
> 概要: コンテンツ定義に設定できるバリデーションのエラー一覧です。レスポンスに含まれる code、message、field の内容についても説明します。

## 概要

コンテンツ定義に設定できるバリデーションのエラーの一覧をまとめます。
各レスポンスには `code`、`message`、`field`の項目が含まれています。
- code: エラー種別コードを意味する文字列（例：リクエストパラメータが無効な場合は`invalid`が入ります）
- message: Kuroco標準のエラーメッセージ
- field: エラーが発生したリクエストパラメータ、総合的なエラーの場合は出力されません

:::note
本リファレンスには、コンテンツ定義に設定されたバリデーションのエラーを記載しています。リクエストに問題がある場合は、別のエラーが発生します。
:::

## バリデーションエラー一覧

### 共通

|Condition|HTTP Status|Code|Message(ja)|Message(en)|
|----|----|----|----|----|
|必須チェック|400|required|[項目名]は必須項目です。|[item name] is required|

### タイトル

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（E-mail）|400|invalid|subject|タイトルが不正です。 メールアドレス形式で入力してください。|*Invalid Title. Please enter in a E-mail format.*|
|入力制限（電話番号）|400|invalid|subject|タイトルが不正です。 電話番号形式で入力してください。|*Invalid Title Please enter in a Contact number format.*|
|入力制限（郵便番号）|400|invalid|subject|タイトルが不正です。 郵便番号形式で入力してください。|*Invalid Title. Please enter in a ZIP code format.*|
|入力制限（URL）|400|invalid|subject|タイトルが不正です。 URL形式で入力してください。|*Invalid Title. Please enter in a URL format.*|
|入力制限（数値）|400|invalid|subject|タイトルが不正です。 数値形式で入力してください。|*Invalid Title. Please enter in a Numeric value format.*|
|入力制限（正規表現）|400|invalid|subject|タイトルが不正です。 |*Invalid Title*|
|入力制限（最小文字数）|400|invalid|subject|タイトルはx文字以上で入力してください。|*Title should be X characters or more.*|
|入力制限（最大文字数）|400|invalid|subject|タイトルはx文字以内で入力してください。|*Please input Title within X characters.*|

### テキスト

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（E-mail）|400|invalid|ext_x|[項目名]が不正です。 メールアドレス形式で入力してください。|*Invalid [item name] Please enter in a E-mail format.*|
|入力制限（電話番号）|400|invalid|ext_x|[項目名]が不正です。 電話番号形式で入力してください。|*Invalid [item name] Please enter in a Contact number format.*|
|入力制限（郵便番号）|400|invalid|ext_x|[項目名]が不正です。 郵便番号形式で入力してください。|*Invalid [item name]. Please enter in a ZIP code format.*|
|入力制限（URL）|400|invalid|ext_x|[項目名]が不正です。 URL形式で入力してください。|*Invalid [item name]. Please enter in a URL format.*|
|入力制限（数値）|400|invalid|ext_x|[項目名]が不正です。 数値形式で入力してください。|*Invalid [item name]. Please enter in a Numeric value format.*|
|入力制限（正規表現）|400|invalid|ext_x|[項目名]が不正です。 |*Invalid [item name]*|
|入力制限（最小文字数）|400|invalid|ext_x|[項目名]の文字数が不正です。|*Invalid The Number of characters of [item name]*|
|入力制限（最大文字数）|400|invalid|ext_x|[項目名]の文字数が不正です。|*Invalid The Number of characters of [item name]*|

### テキストエリア

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（最小文字数）|400|invalid|ext_x|[項目名]の文字数が不正です。|*Invalid The Number of characters of [item name]*|
|入力制限（最大文字数）|400|invalid|ext_x|[項目名]の文字数が不正です。|*Invalid The Number of characters of [item name]*|

### 画像(KurocoFilesにアップロード)

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（拡張子）|400|invalid|ext_x|[項目名][ファイル名]が不正です。|Invalid [item name] [File name]|
|入力制限（ファイル容量制限）|400|invalid|ext_x|[項目名]容量オーバーのためファイルはアップロードできませんでした。|[item name] Could not upload: the file size is too big|

### ファイル(KurocoFilesにアップロード)

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（拡張子）|400|invalid|ext_x|[項目名][ファイル名]が不正です。|Invalid [item name] [File name]|
|入力制限（ファイル容量制限）|400|invalid|ext_x|[項目名]容量オーバーのためファイルはアップロードできませんでした。|[item name] Could not upload: the file size is too big|

### ファイル(GSCにアップロード)

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（拡張子）|400|invalid|ext_x|[項目名][ファイル名]が不正です。|Invalid [item name] [File name]|

### ファイル(S3にアップロード)

|Condition|HTTP Status|Code|Field|Message(ja)|Message(en)|
|----|----|----|----|----|----|
|入力制限（拡張子）|400|invalid|ext_x|[項目名][ファイル名]が不正です。|Invalid [item name] [File name]|

## エラーレンスポンスサンプル

コンテンツ追加APIでsubjectが空文字、もしくは未指定だった場合のエラーのレスポンスサンプルは下記になります。

```json
{
  "errors": [
    {
      "code": "invalid",
      "message": "タイトルは必須項目です。",
      "field": "subject"
    }
  ],
  "x-rcms-request-id": "280496b2-8b45-4a9a-8a21-678feb77e2ff"
}
```

- 特定の項目に対するエラーの場合は `field` に対象項目が含まれています。

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [APIのエラーメッセージ一覧はありますか？](/ja/docs/faq/where-can-i-find-a-list-of-api-error-messages/)
- [APIが動かないです。どうしたらよいですか？](/ja/docs/faq/what-should-i-do-if-the-api-is-not-working/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)


---

# Filter検索のパラメータ

> 元ページ: `reference/filter-query` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/filter-query/

ここでは検索機能を利用する方法を解説します。

## 基本

検索はFilter queryという機能を利用します。Filter queryはSQLに似た記述で検索条件を指定できます。

たとえばtimestampというフィールドについて、2021年06月01日から6月30日までのデータを検索する場合には次のように指定します。

```
?filter=%28timestamp+%3E%3D+%222021-06-01+00%3A00%22+AND+timestamp+%3C%3D+%222021-06-30+23%3A59%22%29
```

この `filter` パラメータは次のような内容をURLエンコードしたものです。

```
?filter=(timestamp >= "2021-06-01 00:00" AND timestamp <= "2021-06-30 23:59")
```

## filterパラメータについて

filterパラメータは基本的に次のような形で構成されます。

`(カラム) (オペレータ) (値)`

- カラムはデータで定義したものを指定します。上記例では `timestamp` になります。
- オペレータはカラムと値をつなぐものです。たとえば `=` や `>=` などになります（[後述](#オペレータについて)）。
- 値は検索条件値になります。文字列や数字が利用できます。

### 値の書き方

:::caution 文字列は二重引用符で囲みます
シングルクォートは文字列の囲み文字として扱われません。`subject contains 'キーワード'` と書くと
引用符も値の一部として比較されるため、**エラーにならないまま検索結果が0件**になります
（値に半角スペースを含む場合は構文エラーになります）。
:::

```text
subject contains "キーワード"     ← 正しい
subject contains 'キーワード'     ← 誤り（0件になります）
```

- 半角スペースや特殊文字を含まず、日付や数値など他の型として解釈されない値は、引用符なしでも文字列として指定できます（`slug = news`）。詳細は[値について](#値について)の文字列の行を参照してください。
- 値の中で二重引用符そのものを使う場合は `\"`、バックスラッシュ自体を使う場合は `\\` とエスケープします（[エスケープについて](#エスケープについて)を参照）。引用符を2つ重ねる書き方（`""`）はエスケープとして扱われません。
- `contains` のような単語のオペレータは、前後に半角スペースが必要です。`=` などの記号のオペレータはスペースなしでも指定できます（`topics_flg=1`）。
- NULL の判定は**小文字**の `null` を使います（`ext_col_01 = null` / `ext_col_01 != null`）。
  大文字の `NULL` は `"NULL"` という文字列との比較になります。
- 空文字の判定（`ext_col_01 = ""`）は、値が NULL の場合も一致対象に含みます。反対に `ext_col_01 != ""` は、値が NULL の場合を一致対象に含みません。
- 配列の末尾にカンマを残すと構文エラーになります（`in [1, 2, ]` は不可）。
- 値の型ごとのフォーマットは[値について](#値について)を参照してください。

### 相対日付モードについて

今日や昨日、何時間前といった相対的に日時を扱って検索するモードを用意しています。基本形は次のようになります。

`(カラム) (オペレータ):relatively (値)`

カラムやオペレータについては、通常のfilterパラメータと同じです（一部利用できないオペレータがあります）。たとえば次のように検索することで、今日のデータだけを取得できます。

`timestamp >=:relatively "today"`

指定できるオペレータと値については[相対日付モードで指定できるオペレータと値](#相対日付モードで指定できるオペレータと値)を参照してください。

### オペレータについて

Filter queryで利用できるオペレータは次の通りです。

| オペレータ | 意味 | 例 | 備考 |
|-----------|-----------|-----------|-----------|
| =         | `カラム` が `値` である | topics_id = 1 | `=` の代わりに `eq` も利用可能です |
| !=        | `カラム` が `値` ではない | ext_col_01 != "" | `!=` の代わりに `ne` も利用可能です |
| <         | `カラム` が `値` より小さい | inst_ymdhi < "2020-08-01" | `<` の代わりに `lt` も利用可能です |
| <=        | `カラム` が `値` 以下である | inst_ymdhi <= "2020-08-01" | `<=` の代わりに `lte` も利用可能です |
| >         | `カラム` が `値` より大きい | topics_group_id > 2 | `>` の代わりに `gt` も利用可能です |
| >=        | `カラム` が `値` 以上である | topics_group_id >= 2 | `>=` の代わりに `gte` も利用可能です |
| in        | `カラム` に `値` のいずれかが含まれる | ext_col_01 in ["A", "B", "C"]  | 値は配列である必要があります |
| nin       | `カラム` に `値` のいずれも含まれない | ext_col_01 nin ["A", "B", "C"] | 値は配列である必要があります |
| all       | `カラム` に `値` すべてが含まれる | secure_level all [1, 2] | 値は配列である必要があります |
| nall      | `カラム` に `値` すべてが含まれない | secure_level nall [1, 2] | 値は配列である必要があります |
| contains  | `カラム` に `値` が含まれる        | subject contains "foo" | 大文字小文字を区別します |
| icontains | `カラム` に `値` が含まれる        | subject icontains "foo" | 大文字小文字を区別しません |
| ncontains | `カラム` に `値` が含まれない      | subject ncontains "bar" | 大文字小文字を区別します |
| nicontains | `カラム` に `値` が含まれない    | subject nicontains "bar" | 大文字小文字を区別しません |
| startswith | `カラム` が `値` ではじまる       | subject startswith "foo" | 大文字小文字を区別します |
| istartswith | `カラム` が `値` ではじまる      | subject istartswith "foo" | 大文字小文字を区別しません |
| nstartswith | `カラム` が `値` ではじまらない  | subject nstartswith "foo" | 大文字小文字を区別します |
| nistartswith | `カラム` が `値` ではじまらない  | subject nistartswith "foo" | 大文字小文字を区別しません |
| endswith    | `カラム` が `値` で終わる       | subject endswith "foo"      | 大文字小文字を区別します |
| iendswith   | `カラム` が `値` で終わる       | subject iendswith "foo"      | 大文字小文字を区別しません |
| nendswith    | `カラム` が `値` で終わらない   | subject nendswith "foo"      | 大文字小文字を区別します |
| niendswith   | `カラム` が `値` で終わらない   | subject niendswith "foo"      | 大文字小文字を区別しません |

:::caution 否定形のオペレータ名
否定形は `n` を先頭に付けた名前です（`ncontains` / `nin` / `nstartswith` など）。
`not_contains` や `not_in` というオペレータは存在せず、指定するとエラーになります。
:::

### オペレータの連結について

複数の条件を指定する場合には `AND` と `OR` が利用できます。

| オペレータ | 意味 | 例 |
|-----------|-----------|-----------|
| AND | `条件1` と `条件2` にマッチする | topics_id eq 1 AND subject eq foo |
| OR  | `条件1` と `条件2` のいずれかにマッチする | topics_id eq 1 OR subject eq foo |

### 他の記法

他に括弧などの記法が用意されています。

| オペレータ | 意味 | 例 |
|-----------|-----------|-----------|
| ()        | 条件の優先順位付け | topics_id eq 1 AND (subject eq foo OR subject eq bar) |
| []        | 値の配列化        | topics_id in [1, 2, 3] |
| ,         | 値の配列区切り文字 | topics_id in [1, 2, 3] |

### 値について

| 種類 | フォーマット |  例 | 備考 |
|------|------|------|------|
| 整数 | `%d`   | topics_id eq 1 |               |
| 数値 | `%f`   | topics_id > 1.00 |              |
| 日付 | `"Y-m-d"` | inst_ymdhi < "2020-08-01" |          |
| 時間 | `"H:m:s"`<br />`"H:m"` | post_time > "12:30:00"<br />"H:m" post_time > "12:30"|           |
| 日時 | `"Y-m-d H:i"`<br />`"Y-m-d H:i:s"`<br />`"Y-m-d H:i:s O"` | update_ymdhi < "2020-08-01 12:00"<br />update_ymdhi < "2020-08-01 12:00:00"<br />update_ymdhi < "2020-08-01 12:00:00 +0900" |           |
| 日付 + 時間 | `"Y/m/d H:i:s"`       |  ymd_time > "2021/09/30 12:30:00" |コンテンツ定義の「投稿時間も設定する」フィールドで、「有効にする」にチェックが入っている場合のみ利用できます。<br/>参考:[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#項目説明-1) |
| 空文字 | `""`   |  ext_col_01 eq "" |           |
| 空配列| `:empty`   |  ext_col_01 eq :empty | 複数選択で選択なしをフィルタする場合はこちらをご利用ください。<br/>タグで選択なしをフィルタする場合は[:R()検索](/ja/docs/reference/r-filter/#topicslistのapiでタグが設定されていないコンテンツを取得)をご利用ください。|
| 文字列 | `"%s"`<br />`%s`       |  subject eq "TITLE"<br />subject eq TITLE |ダブルクオート `"` で囲んだ場合は日付/時刻/日時を除いて文字列として扱われます。<br />ダブルクオートがない場合、他の型と一致せず、かつ空白や特殊文字がない場合は文字列として扱われます。 |

### 相対日付モードで指定できるオペレータと値

#### 相対日付モードで指定できるオペレータ

相対日付モードで指定できるオペレータは次の通りです。

| オペレータ | 意味 | 例 |
|-----------|-----------|-----------|
| =:relatively | 値に一致する    | timestamp =:relatively "today" |
| !=:relatively | 値に一致しない | timestamp !=:relatively "today" |
| >:relatively | 値より大きい    | timestamp >:relatively "-9 hours" |
| >=:relatively | 値以上         | timestamp >=:relatively "-10 hours" |
| <:relatively | 値より小さい    | timestamp <:relatively "1 week" |
| <=:relatively | 値以下         | timestamp <=:relatively "last Monday" |

#### 相対日付モードで指定できる値

相対日付モードは[PHPのstrtotime関数](https://www.php.net/manual/ja/function.strtotime.php)互換となっています。strtotime関数で利用できる指定方式が指定可能です。

利用できる書式は次の通りです（[PHP: 相対的な書式 - Manual](https://www.php.net/manual/ja/datetime.formats.relative.php)からの転載です）。

| シンボル | 書式 |
|---------|---------|
| dayname | 'sunday' \| 'monday' \| 'tuesday' \| 'wednesday' \| 'thursday' \| 'friday' \| 'saturday' \| 'sun' \| 'mon' \| 'tue' \| 'wed' \| 'thu' \| 'fri' \| 'sat' |
| daytext | 'weekday' \| 'weekdays' |
| number  | [+-]?[0-9]+ |
| ordinal | 'first' \| 'second' \| 'third' \| 'fourth' \| 'fifth' \| 'sixth' \| 'seventh' \| 'eighth' \| 'ninth' \| 'tenth' \| 'eleventh' \| 'twelfth' \| 'next' \| 'last' \| 'previous' \| 'this' |
| reltext | 'next' \| 'last' \| 'previous' \| 'this' |
| space   | [ \t]+ |
| unit    | (('sec' \| 'second' \| 'min' \| 'minute' \| 'hour' \| 'day' \| 'fortnight' \| 'forthnight' \| 'month' \| 'year') 's'?) \| 'weeks' \| daytext |

入力例は次の通りです。

| 書式 | 説明 | 例 |
|------|------|------|
| 'yesterday' | 昨日の00:00:00 | "yesterday 14:00" |
| 'midnight' | 時刻を00:00:00にします |   |
| 'today' | 時刻を00:00:00にします |   |
| 'now' | 今 |   |
| 'noon' | 時刻を12:00:00にします | "yesterday noon" |
| 'tomorrow' | 明日の00:00:00 |   |
| 'back of' hour | 指定された時の15分後 | "back of 7pm", "back of 15" |
| 'front of' hour | 指定された時の15分前 | "front of 5am", "front of 23" |
| 'first day of' | 現在月の最初の日にします。 この書式に続けて月名を指定する使いかたが最適です。 | "first day of January 2008" |
| 'last day of' | 現在月の最後の日にします。 この書式に続いて月名を指定する使いかたが最適です。 | "last day of next month" |
| ordinal space dayname space 'of' | 現在月のx番目の曜日を計算します。 | "first sat of July 2008" |
| 'last' space dayname space 'of' | 現在月の 最後の 曜日を計算します。 | "last sat of July 2008" |
| number space? (unit \| 'week') | 値を数値で指定するような、相対的な時間指定を処理します。 | "+5 weeks", "12 day", "-7 weekdays" |
| ordinal space unit | 値を英単語で指定するような、相対的な時間指定を処理します。 | "fifth day", "second month" |
| 'ago' | 直前に指定された相対的な時間指定について、正負反転します。 | "2 days ago", "8 days ago 14:00", "2 months 5 days ago", "2 months ago 5 days", "2 days ago" |
| dayname | 現在からみて次にやってくる、指定された曜日にします。 | "Monday" |
| reltext space 'week' | 特別な書式 "weekday + last/this/next week" を処理します。 | "Monday next week" |

### エスケープについて

Filter クエリ内では、特定の文字をそのまま検索条件として利用するために  
**エスケープ処理** が必要になります。  
特に **ダブルクオート (`"`)** と **バックスラッシュ (`\`)** は、クエリ構文に影響するため注意してください。

#### 文字列指定時のルール

- 文字列は原則として **ダブルクオート `"` で囲みます**
- 値の中にダブルクオートを含めたい場合は `\"` としてエスケープします
- バックスラッシュ自体を 1 文字として扱う場合は `\\` と記述します

#### エスケープが必要な文字

| 文字 | 用途 | エスケープ方法 | 記述例 |
|------|------|----------------|--------|
| `"`  | 文字列の区切り | `\"` | `subject eq "He said \"Hello\""` |
| `\`  | エスケープ文字 | `\\` | `path eq "C:\\data\\file.txt"` |


### `:File()`検索
画像の有無を元に検索を実行します。

検索の対象となる項目は以下の通りです。
- 画像(Kurocofilesにアップロード)
- ファイル(Kurocofilesにアップロード)
- ファイル(GCSにアップロード)
- ファイル(S3にアップロード)

Filterの指定例
- ext_1にファイルが存在する：`:File(exists(ext_1))`
- ext_1にファイルが存在しない：`:File(nexists(ext_1))`

:::caution
:File()による検索はコンテンツの拡張項目が`ext_1`のサイトで有効になっています。  
拡張項目のレスポンスが`ext_col_01`の形式のサイトでは動作しませんのでご注意ください。
:::

### `:R()`検索
関連情報に紐づけられたコンテンツやタグの情報を条件に検索を実行できます。  
詳しい使い方は以下を参考にしてください。

:::info
- [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)
:::

### `:D()`検索
地図の項目を基に、指定した位置からの距離を条件に検索できます。
詳しい使い方は以下を参考にしてください。

:::info
- [位置情報による並び替え](/ja/docs/reference/order-by-location/#filterクエリとの併用)
:::

## order_queryパラメータについて

order_query パラメータは、結果の並び順を指定するために使用します。  
このパラメータは、エンドポイントのパラメータまたはクエリパラメータとして、`フィールド名=(昇順 or 降順)` の形式で指定してください。

###  昇順

昇順（最初が小さいデータ、徐々に大きくなる）はASCになります。  
例：`/rcms-api/1/topics?order_query=topics_id=ASC`

###  降順

降順（最初が大きいデータ、徐々に小さくなる）はDESCになります。  
例：`/rcms-api/1/topics?order_query=topics_id=DESC`

## その他のパラメータについて

その他、検索実行時に指定できるパラメータは次の通りです。

| パラメータ名 | 意味 | 例 |
|-------------|-------------|-------------|
| pageID      | 何ページ目を返すかの指定 | pageID=1 |
| perPage     | 1ページあたりの結果件数 | perPage=20 |
| filter_lang | 絞り込みに利用する言語  | filter_lang=en |
| _lang       | レスポンスするコンテンツの言語 | _lang=en  |

## 関連ドキュメント
- [検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)
- [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)
- [Kurocoのキーワード検索の種類](/ja/docs/reference/keyword-search-types/)
- [APIのレスポンスをコンテンツカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-content-category/)
- [APIのレスポンスをタグカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-tag-category/)


---

# 関連しているデータを条件にしたfilter機能

> 元ページ: `reference/r-filter` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/r-filter/
> 概要: ここではfilter機能で、関連しているデータを条件にして検索をする方法を紹介します。`:R(%module_name%:q|%filter_query%|)`の形式でフィルターを作成することで、関連情報に対する絞り込み条件を指定できるほか、キーワードとタグを組み合わせて検索するなど、柔軟な検索ができます。

ここではfilter機能で、関連しているデータを条件にして検索をする方法を紹介します。  
`:R(%module_name%:q|%filter_query%|)`の形式でフィルターを作成することで、  
関連情報に対する絞り込み条件を指定できるほか、キーワードとタグを組み合わせて検索するなど、柔軟な検索ができます。

:::info
:R()検索は主言語に対してのみ実行可能です。多言語設定を有効にしていても紐づくコンテンツは主言語が元になりますのでご注意ください。
:::

## 設定方法
### 事前準備
関連情報に対する絞り込みを行うためには、まず`filter_request_allow_list`で利用を許可するモジュールを設定します。  
以下の形式で`filter_request_allow_list`を記述します。  

`:q|%module_name%:[%column_name1%,%column_name2%]`

例：`:q|topics:[topics_group_id,subject]`  
-> サブクエリに topics_group_id, subject の指定を許可。

コンテンツの拡張項目をサブクエリに指定する場合は、コンテンツ定義IDも指定してください。

例：`:q|topics[topics_group_id=10]:[ext_1,relation]`  
-> サブクエリにコンテンツの拡張項目 ext_1, relation の指定を許可。

また、`:q|tag:[:ALL]`のようにサブクエリを`:ALL`で指定も可能です。  
指定できるサブクエリは[利用できる項目](#利用できる項目)を参照してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0c8768a58aae9ed73ad790be0719e63a.png)

#### 絞り込み条件の変化
Topics, Tag, Inquiryは、allow_listの設定内容に応じてデフォルトの絞り込み条件が変化します。  
- Topics, Tag  
    - allow_listにopen_flgを含まない場合、公開状態のコンテンツ/タグのみが検索対象になります。  
    - allow_listにopen_flg(または:ALL)を含む場合、非公開のコンテンツ/タグも含めて検索対象になります。
- Inquiry
    - allow_listにstatusを含まない場合、運用中のフォームのみが検索対象になります。
    - allow_listにstatus(または:ALL)を含む場合、休止中のフォームも含めて検索対象になります。


### フィルター指定例
#### Tag::listのAPIでtopics_group_id=1 のコンテンツに紐付くタグを取得
`filter`: `:R(topics:q|topics_group_id eq 1|)`  
`filter_request_allow_list`: `:q|topics:[topics_group_id]`  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a228332196dc900e20b4f18e6a1bcbbf.png)

#### Topics::listのAPIでtag_id=50 のタグに紐付くコンテンツを取得
`filter`: `:R(tag:q|tag_id in [50]|)`  
`filter_request_allow_list`: `:q|tag:[tag_id]`  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab3ff88f6033bb89ee29b550cf81842c.jpg)

#### Topics::listのAPIでキーワードとタグでAND検索
`filter`: `search_keyword contains "テスト" AND :R(tag:q|tag_id in [50]|)`  
`filter_request_allow_list`:`[search_keyword,:q|tag:[tag_id]]`  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/52454de0102cab6d1842238a10808784.jpg)

#### Topics::listのAPIで特定のタグ内でOR検索をし、それぞれをAND検索する
`filter`: `:R(tag:q|tag_id in [7,8,9]|) AND :R(tag:q|tag_id in [5,6]|)`  
`filter_request_allow_list`: `:q|tag:[tag_id]` 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9e3d5407acc69992bf2e948f91f36db3.jpg)

#### Topics::listのAPIでタグが設定されていないコンテンツを取得
`filter`: `:R(tag:empty)`

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acf8be256a14e699dc221c3221dc6476.png)

#### Tag::listのAPIで、topics_group_id=1,2、ext_1="val"、checkbox="1" のコンテンツに紐付くタグを取得

:::caution
サブクエリに拡張項目(ext_X)を指定する場合はコンテンツ定義IDも指定してください。
:::

`filter`: `:R(topics[topics_group_id=1,2]:q|ext_1 = "val" AND checkbox = "1"|)`  
`filter_request_allow_list`: `:q|topics[topics_group_id=1,2]:[ext_1,ext_2,text,checkbox]` 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8f173bb70eb9a0a16891479caf08cd1.png)

#### 注意事項
関連したコンテンツの拡張項目で絞込みを行う場合、コンテンツ定義IDは`topics_group_id=1`の指定の他、`1`のように省略して書くことができますが、allow_listとfilterで[]内に指定するパラメータを一致させる必要があります。

- 動作するパターン
  - filter_request_allow_list: topics[`topics_group_id=1`]
  - filter: topics[`topics_group_id=1`]
- 動作しないパターン(1)
  - filter_request_allow_list: topics[`topics_group_id=1`]
  - filter: topics[`1`]
- 動作しないパターン(2)
  - filter_request_allow_list: topics[`1,2`]
  - filter: topics[`2,1`]

## 利用できる項目
利用できる`module_name`とそのサブクエリ(`column_name`)は以下となります。  

### Topics
`topics_id`  
`topics_group_id`  
`contents_type`  
`subject`  
`open_flg`  
`topics_flg`  
`regular_flg`  
`inst_ymdhi`  
`update_ymdhi`  
`ext_x(slug)`  

 ### Member
`member_id`  
`group_ids`  
`inst_ymdhi`  
`update_ymdhi`  

 ### Inquiry
`inquiry_id`  
`inquiry_name`  
`status`  
`inst_ymdhi`  
`update_ymdhi`  

 ### Tag
`tag_id`  
`tag_nm`  
`open_flg`  
`inst_ymdhi`  
`update_ymdhi`  
`tag_category_id`  
`ext_col_01`  
`ext_col_02`  
`ext_col_03`  
`ext_col_04`  
`ext_col_05`  
`ext_col_06`  
`ext_col_07`  
`ext_col_08`  
`ext_col_09`  
`ext_col_10`  

## 関連ドキュメント
- [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
- [APIのレスポンスをタグカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-tag-category/)
- [APIのレスポンスをコンテンツカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-content-category/)
- [関連情報選択で選択したコンテンツの全情報をレスポンスに追加するにはどうしたら良いですか？](/ja/docs/faq/add-all-information-on-the-content-selected-in-the-relational-data-selection-to-the-response/)


---

# APIを使ったファイルのアップロードについて

> 元ページ: `reference/uploading-files-using-the-api` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/uploading-files-using-the-api/
> 概要: APIを利用してファイルをアップロードする方法は、コンテンツやメンバーなどに紐づける方法と、ファイルマネージャーに直接アップロードする方法の2つがあります。

## 概要
APIを利用してファイルをアップロードする方法は、用途に応じて以下の2つがあります。

- **コンテンツに紐づけてアップロードする**: `Files::upload`のエンドポイントを利用して一時領域にファイルをアップロードし、取得した`file_id`をコンテンツ更新等の各エンドポイントにPOSTします。
- **ファイルマネージャーに直接アップロードする**: `FileManager::upload`のエンドポイントを利用して、ファイルマネージャーの指定ディレクトリにファイルを直接アップロードします。

## コンテンツに紐づけてアップロードする

コンテンツ、フォーム、メンバーなどにAPIを利用してファイルをアップロードする場合、`Files::upload`のエンドポイントを利用して、ファイルをKurocoの一時領域にアップロードし、応答として返される`file_id`を各エンドポイントにPOSTしてコンテンツを更新します。

SwaggerUIで動作の確認をすると、以下の手順になります。

### 画像(KurocoFilesにアップロード)
画像(KurocoFilesにアップロード)(コンテンツ)や、アップロードファイル(メンバー)の場合は以下のように`Files::upload`で取得した`file_id`をエンドポイントにPOSTします。

1. Files::uploadのエンドポイントにファイルをアップロードする。  
  `Files::upload`のエンドポイントを開くと、[ファイルを選択]のボタンが表示されるので、アップロードするファイルを選択します。  

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/4bc477a16c196a73f921f38a1f66eeb6.png)

  :::tip
  ファイル送信時のリクエストヘッダには'Content-Type': 'multipart/form-data'を指定します。
  :::

2. レスポンスから`file_id`を確認する  
  ファイルの一時領域へのアップロードが成功すると、`file_id`を含むレスポンスが表示されます。  

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/5abfaf930bc6a331be7c0d7ef99083ca.png)

3. `file_id`をコンテンツを更新するエンドポイントにPOSTする  
  更新・追加したいコンテンツを操作するエンドポイントに対して、`file_id`を指定してリクエストを送ります。   

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/dfea1d5badaf69fdb605de19702bcdd9.png)

4. リクエストが成功したことを確認する  
  レスポンスとコンテンツを確認します。

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/392768bb3b877d18b0fd9460152a40ad.jpg)


フロントエンドでの具体的なコードの例は関連ドキュメントを参照してください。

### WYSIWYG

WYSIWYGの拡張項目の場合は`Files::upload`で取得した`file_id`をHTMLの`src`属性に指定すると、画像がファイルマネージャーの`/files/user/topics_img/`配下のディレクトリに保存されて更新されます。

1. Files::uploadのエンドポイントにファイルをアップロードする。  
  `Files::upload`のエンドポイントを開くと、[ファイルを選択]のボタンが表示されるので、アップロードするファイルを選択します。  

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/4bc477a16c196a73f921f38a1f66eeb6.png)

2. レスポンスから`file_id`を確認する  
  ファイルの一時領域へのアップロードが成功すると、`file_id`を含むレスポンスが表示されます。  

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/f99b6e0c79647c928fee6e4132482274.png)

3. HTML要素の`src`属性に一時パスを入力したHTMLを準備する

  `<img src=\"INPUT_TEMPORARY_PATH_HERE\">`のように`src`属性に`Files::upload`のエンドポイントから取得した`file_id`を指定したHTMLを準備します。  
  次のようになります。
  ```
  <figure class=\"image\"><img style=\"aspect-ratio:2000/1334;\" src=\"files/temp/75a0d4626ac4bab6d4ec6f8969233fd493db2f7093b67cf92a782f8814e37530.png\" width=\"2000\" height=\"1334\"></figure>
  ```

  :::tip
  HTMLに含まれる`"`は`\`でエスケープしてください。
  :::

4. `src`属性に`file_id`を含むHTMLをエンドポイントにPOSTする  
  更新・追加したいコンテンツを操作するエンドポイントに対して、`src`属性に`file_id`を含むHTMLをPOSTします。   

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/3105068b3e7ae098e57b27fe6766ecd9.png)

5. リクエストが成功したことを確認する  
  レスポンスとコンテンツを確認します。

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a4b664d3577f40e2c3af6e81da5dcb1.png)

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/8623013b6775dc9d29c0a01adc918814.png)

仕様:
- HTML要素には`src`属性が含まれている必要があります。
- アップロードストレージにはKurocoFiles、S3、GCSが利用可能です。
- WYSIWYGへのAPIを使ったファイルアップロードは画像ファイル(`jpeg`,`jpg`,`gif`,`png`,`bmp`,`webp`,`avif`,`svg`)のみが許可されています。
- 一度のリクエストで複数の一時ファイルパスを使用することが可能です。
- 一度のリクエストで同じ一時ファイルパスを複数回使用することが可能です。例えば、以下のようにリクエストすると、WYSIWYGの項目に同じ画像が2つ追加されます。
  ```
  `<figure class=\"image1\"><img src=\"TEMPORARY_PATH\"></figure><figure class=\"image2\"><img src=\"TEMPORARY_PATH\"></figure>`
  ```
- 複数のAPIリクエストで同じ一時ファイルパスを使用することが可能です。
- WYSIWYIGへのAPIを利用した画像アップロードは追加項目の名称が`ext_x`のサイトで動作します。追加項目の名称が`ext_col_x`のサイトでは動作しません。

## ファイルマネージャーに直接アップロードする

コンテンツに紐づけず、ファイルマネージャーの指定ディレクトリにファイルを直接アップロードする場合は、`FileManager::upload`のエンドポイントを利用します。

`Files::upload`との違いは以下の通りです。

| | Files::upload | FileManager::upload |
|:--|:--|:--|
| 用途 | コンテンツ・フォーム・メンバーにファイルを紐づける | ファイルマネージャーにファイルを直接配置する |
| アップロード先 | 一時領域（`files/temp/`） | ファイルマネージャーの指定ディレクトリ |
| レスポンス | `file_id`（一時ファイルパス） | `url`（アップロード先のファイルURL） |
| ファイルの利用方法 | `file_id`を他のエンドポイントにPOSTして紐づける | アップロード完了後すぐにURLでアクセス可能 |

以下の手順でアップロードが可能です。

1. `FileManager::upload`のエンドポイントにファイルをアップロードする。  
  `FileManager::upload`のエンドポイントを開き、アップロードするファイルを選択します。

2. レスポンスからアップロード先のURLを確認する。  
  アップロードが成功すると、ファイルの`url`を含むレスポンスが返されます。

:::tip
ファイル送信時のリクエストヘッダには'Content-Type': 'multipart/form-data'を指定します。
:::

:::info
`FileManager::upload`を利用するには、APIを実行するメンバーに「ファイル」の「更新」権限が必要です。
:::

## 関連ドキュメント
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/#ファイルの入力項目を追加する)
- [フロントエンドからファイルをアップロードしてコンテンツに関連づけるにはどうしたらよいですか？](/ja/docs/faq/how-do-i-upload-image-and-manage-it/)
- [コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？](/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/)
- [ファイルマネージャー](/ja/docs/management/file-manager/)
