# Smarty構文リファレンス

## 変数操作

```smarty
{* 変数の代入 *}
{assign var="variable_name" value="値"}
{assign var="number" value=100}
{assign var="date" value=$smarty.now|date_format:"%Y-%m-%d"}

{* 空配列の作成 *}
{assign var="array_name" value=$dataSet.emptyArray}

{* 配列への追加 *}
{append var="array_name" value="値"}
{append var="array_name" index="key" value="値"}

{* 連想配列の作成 *}
{assign var="obj" value=$dataSet.emptyArray}
{append var="obj" index="name" value="田中"}
{append var="obj" index="age" value=30}
```

## ループ処理

```smarty
{* 配列のループ *}
{foreach from=$array item="item" key="key" name="loop"}
  インデックス: {$smarty.foreach.loop.index}
  値: {$item}
  {if $smarty.foreach.loop.first}最初{/if}
  {if $smarty.foreach.loop.last}最後{/if}
{/foreach}

{* 回数指定ループ *}
{section name="i" start=0 loop=10}
  {$smarty.section.i.index}
{/section}
```

## 条件分岐

```smarty
{if $condition}
  条件が真
{elseif $other_condition}
  別の条件
{else}
  それ以外
{/if}

{* 比較演算子 *}
{if $value == "test"}等しい{/if}
{if $value != "test"}等しくない{/if}
{if $value > 10}より大きい{/if}
{if $value >= 10}以上{/if}
{if $value < 10}より小さい{/if}
{if $value <= 10}以下{/if}

{* 論理演算子 *}
{if $a && $b}AND{/if}
{if $a || $b}OR{/if}
{if !$a}NOT{/if}

{* 空チェック *}
{if $value}値がある{/if}
{if $value|@count > 0}配列に要素がある{/if}
```

## 文字列操作

```smarty
{* 連結 *}
{assign var="str" value=$str1|cat:$str2}
{assign var="str" value="Hello "|cat:$name}

{* 置換 *}
{$text|replace:"検索文字":"置換文字"}

{* 分割 *}
{assign var="parts" value=","|explode:$csv_line}

{* 結合 *}
{assign var="csv" value=","|implode:$array}

{* トリム *}
{$text|trim}

{* 大文字/小文字 *}
{$text|upper}
{$text|lower}

{* 長さ *}
{$text|strlen}

{* 部分文字列 *}
{$text|substr:0:10}
```

## 日付・時刻処理

```smarty
{* 現在日時 *}
{$smarty.now|date_format:"%Y-%m-%d"}
{$smarty.now|date_format:"%Y-%m-%d %H:%M:%S"}

{* 日付フォーマット変換 *}
{$date_string|strtotime|date_format:"%Y/%m/%d"}

{* 日付計算 *}
{assign var="tomorrow" value=$smarty.now+86400}
{assign var="yesterday" value=$smarty.now-86400}
{assign var="next_week" value=$smarty.now+604800}

{* 月初・月末 *}
{assign var="first_day" value="first day of this month"|strtotime|date_format:"%Y-%m-%d"}
{assign var="last_day" value="last day of this month"|strtotime|date_format:"%Y-%m-%d"}
```

## JSONデータの扱い

```smarty
{* JSONエンコード *}
{assign var="json_str" value=$array|@json_encode}

{* JSONデコード *}
{assign var="decoded" value=$json_str|json_decode:true}

{* オブジェクトのJSONエンコード *}
{assign var="obj" value=$dataSet.emptyArray}
{append var="obj" index="name" value="値"}
{$obj|@json_encode}
```

## ファイル出力

### 一時ファイルへの書き込み

```smarty
{* 新規作成 *}
{write_file var="tmp_path" value="ファイル内容"}

{* 追記モード *}
{write_file path=$tmp_path value="追記内容" is_append=1}

{* 改行付き *}
{write_file path=$tmp_path value=$line|cat:"\n" is_append=1}
```

### オンラインストレージへアップロード

```smarty
{assign var="tmp_abs_path" value=$smarty.const.TEMP_DIR2|cat:'/'|cat:$tmp_path}
{put_file path='/exports/output.csv' tmp_path=$tmp_abs_path}
```

## CSV出力の完全例

```smarty
{* ヘッダー行 *}
{assign var="csv_header" value="ID,タイトル,公開日,カテゴリ"}
{write_file var="tmp_path" value=$csv_header|cat:"\n"}

{* データ取得 *}
{assign var="queries" value=$dataSet.emptyArray}
{append var="queries" index="cnt" value=0}
{append var="queries" index="filter" value="topics_flg = 1"}
{append var="queries" index="order_by" value="ymd desc"}

{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  queries=$queries
  var='news_list'
}

{* データ行出力 *}
{foreach from=$news_list.list item="news"}
  {assign var="row" value=$dataSet.emptyArray}
  {append var="row" value=$news.topics_id}
  {append var="row" value=$news.subject|escapeCSV:false:"UTF-8"}
  {append var="row" value=$news.ymd}
  {append var="row" value=$news.category_nm|escapeCSV:false:"UTF-8"}
  {assign var="row_str" value=","|implode:$row}
  {write_file path=$tmp_path value=$row_str|cat:"\n" is_append=1}
{/foreach}

{* ファイル保存 *}
{assign var="filename" value="news_"|cat:$smarty.now|date_format:"%Y%m%d"|cat:".csv"}
{assign var="csv_path" value="/exports/"|cat:$filename}
{assign var="tmp_abs_path" value=$smarty.const.TEMP_DIR2|cat:'/'|cat:$tmp_path}
{put_file path=$csv_path tmp_path=$tmp_abs_path}

出力完了: {$csv_path}
出力件数: {$news_list.pageInfo.totalCnt}
```

## デバッグ方法

```smarty
{* デバッグ出力（テスト時のみ使用） *}
{$variable|@debug_print_var:0:1000}

{* 配列の内容を確認 *}
{$array|@print_r}

{* JSON形式で出力 *}
{$data|@json_encode}

{* バッチログに出力 *}
{log message="処理開始: {$smarty.now|date_format:'%Y-%m-%d %H:%M:%S'}"}
{log message="処理件数: {$count}"}
{log message="エラー: {$error_message}"}
```
