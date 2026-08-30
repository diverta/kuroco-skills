# 使用例

SKILL.md の「よく使うプラグイン」を組み合わせた最小例。構文の詳細は [syntax.md](syntax.md)、各プラグインのパラメータはカテゴリ別リファレンスを参照。

## 目次

- [コンテンツ一覧をAPIで取得して表示](#コンテンツ一覧をapiで取得して表示)
- [フォーム送信後にSlack通知](#フォーム送信後にslack通知)
- [権限に応じた表示制御](#権限に応じた表示制御)
- [エラーハンドリング](#エラーハンドリング)
- [ページング分割](#ページング分割)

## コンテンツ一覧をAPIで取得して表示

```smarty
{assign var="queries" value=$dataSet.emptyArray}
{append var="queries" index="cnt" value=10}
{append var="queries" index="filter" value="topics_flg = 1"}

{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  queries=$queries
  var='result'
}

{foreach from=$result.list item="news"}
  <h2>{$news.subject|escape}</h2>
  <p>{$news.contents|truncate:200}</p>
  <time>{$news.ymd|date_format:"%Y年%m月%d日"}</time>
{/foreach}

{pager info=$result.pageInfo}
```

## フォーム送信後にSlack通知

```smarty
{sendmail
  var=mail_result
  to=$inquiry.email
  subject="お問い合わせありがとうございます"
  mail_template="inquiry_thanks"
}

{* サイト設定でSlack連携を有効化し slack_bot_token を設定しておく（webhook URLは使わない） *}
{slack_post_message
  channel="#inquiry"
  text="新規問い合わせ: {$inquiry.name}様 - {$inquiry.subject}"
}
```

## 権限に応じた表示制御

`target` は `"アクション:リソースパス"` 形式（アクションは `read` / `insert` / `update` / `delete`、`|` でOR指定）。

```smarty
{rcms_auth target="insert|update:/topics/"}
  <a href="/management/news/edit/">編集</a>
{/rcms_auth}

{rcms_auth target="delete:/topics/"}
  <button class="delete-btn">削除</button>
{/rcms_auth}
```

## エラーハンドリング

`errors` は空配列でも truthy にならないよう件数で判定する。ログは `{logger}`（msg1〜msg4、各1KB以内）。

```smarty
{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  var='response'
}

{* エラー配列は空でも truthy にならないよう件数で判定。ログは {logger}（msg1〜msg4、各1KB以内） *}
{if $response.errors|@count > 0}
  {slack_post_message channel="#alerts" text="エラー: {$response.errors|@json_encode}"}
  {logger msg1="batch-error" msg2=$response.errors|@json_encode}
{else}
  {logger msg1="batch-done" msg2="処理完了: {$response.pageInfo.totalCnt}件"}
{/if}
```

## ページング分割

大量データは `{while}` でページを回し、1回のバッチで扱う件数を絞る。

```smarty
{assign var="page" value=1}
{while true}
  {assign var="queries" value=$dataSet.emptyArray}
  {append var="queries" index="pageID" value=$page}
  {append var="queries" index="cnt" value=100}

  {api_internal endpoint='/rcms-api/1/news' method='GET' member_id=1 queries=$queries var='response'}

  {foreach from=$response.list item="item"}
    {* 処理 *}
  {/foreach}

  {if $page >= $response.pageInfo.totalPageCnt}{break}{/if}
  {assign var="page" value=$page+1}
{/while}
```
