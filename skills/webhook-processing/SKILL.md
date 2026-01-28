---
name: kuroco-webhook-processing
description: Kuroco Webhook・バッチ処理・自動化のベストプラクティス。使用キーワード：「Webhook」「バッチ処理」「定期実行」「スケジュール実行」「cron」「15分毎」「1時間毎」「外部連携」「GitHub Actions」「repository_dispatch」「workflow_dispatch」「Slack通知」「slack_send」「Chatwork」「chatwork_send」「メール通知」「send_mail」「SendGrid」「sendgrid_send」「自動処理」「Smarty」「Smarty構文」「assign」「foreach」「if」「api_internal」「api_request」「外部API」「トリガー」「前処理」「後処理」「Function」「カスタム処理」「CSV出力」「write_file」「put_file」「json_encode」「date_format」「topics変数」「inquiry変数」。定期実行、外部通知、Smartyテンプレート、トリガー処理に関する質問で使用。
---

# Kuroco Webhook・バッチ処理パターン

Kuroco HeadlessCMSでのWebhook、バッチ処理、外部連携に関するベストプラクティス。

**ドキュメント参照**: 詳細は `${CLAUDE_PLUGIN_ROOT}/docs/` を参照。同期が必要な場合は `/kuroco-docs` スキルを使用。

## 目次

- [バッチ処理](#バッチ処理)
- [Smarty構文の基本](#smarty構文の基本) → 詳細は [references/smarty.md](references/smarty.md)
- [内部API呼び出し](#内部api呼び出し)
- [外部API呼び出し](#外部api呼び出し)
- [トリガー処理](#トリガー処理)
- [外部サービス連携](#外部サービス連携) → 詳細は [references/integrations.md](references/integrations.md)

## バッチ処理

### 概要

バッチ処理は一定時間ごとに自動実行される処理。

**実行頻度の選択肢:**
| 頻度 | 用途 |
|------|------|
| 15分毎 | 頻繁な同期が必要な場合 |
| 30分毎 | 準リアルタイム処理 |
| 1時間毎 | 定期的な集計・更新 |
| 毎日（指定時刻） | 日次レポート、バックアップ |

### ユースケース

- 外部システムへのCSV生成・連携
- 外部システムからのデータ取り込み
- ログ集計・統計データ算出
- 定期的なメール配信
- GitHub Actions連携（デプロイトリガー）

### バッチ処理の作成

管理画面: [オペレーション] → [バッチ処理] → [追加]

| 項目 | 説明 | 例 |
|------|------|-----|
| タイトル | バッチの名前 | CSV出力バッチ |
| 識別子 | ユニークな識別子（英数字） | csv_export |
| 実行頻度 | 実行間隔 | 毎日 03:00 |
| 実行内容 | Smarty構文で記述 | 下記参照 |

## Smarty構文の基本

**詳細な構文リファレンス**: [references/smarty.md](references/smarty.md) を参照

### 変数操作

```smarty
{assign var="name" value="値"}
{assign var="array" value=$dataSet.emptyArray}
{append var="array" index="key" value="値"}
```

### 条件分岐

```smarty
{if $condition}
  処理
{elseif $other}
  別の処理
{else}
  それ以外
{/if}
```

### ループ

```smarty
{foreach from=$array item="item" key="key"}
  {$item}
{/foreach}
```

## 内部API呼び出し

### 基本構文

```smarty
{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  queries=$queries
  var='response'
}
```

### コンテンツ一覧取得

```smarty
{assign var="queries" value=$dataSet.emptyArray}
{append var="queries" index="cnt" value=0}
{append var="queries" index="filter" value="topics_flg = 1"}

{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  queries=$queries
  var='news_list'
}

{foreach from=$news_list.list item="news"}
  ID: {$news.topics_id}, タイトル: {$news.subject}
{/foreach}
```

### コンテンツ作成

```smarty
{assign var="body" value=$dataSet.emptyArray}
{append var="body" index="subject" value="タイトル"}
{append var="body" index="contents" value="本文"}
{append var="body" index="topics_flg" value=1}

{api_internal
  endpoint='/rcms-api/1/news/insert'
  method='POST'
  member_id=1
  body=$body
  var='result'
}
```

## 外部API呼び出し

### 基本構文

```smarty
{api_request
  url='https://api.example.com/endpoint'
  method='GET'
  headers=$headers
  body=$body
  var='response'
}
```

### POSTリクエスト例

```smarty
{assign var="headers" value=$dataSet.emptyArray}
{append var="headers" index="Content-Type" value="application/json"}
{append var="headers" index="Authorization" value="Bearer YOUR_API_KEY"}

{assign var="body" value=$dataSet.emptyArray}
{append var="body" index="message" value="Hello"}

{api_request
  url='https://api.example.com/post'
  method='POST'
  headers=$headers
  body=$body|@json_encode
  var='response'
}
```

## トリガー処理

### コンテンツ更新時のトリガー

管理画面: [コンテンツ定義] → [トリガー設定]

**利用可能なイベント:**
| イベント | タイミング |
|---------|----------|
| 作成時 | コンテンツ新規作成後 |
| 更新時 | コンテンツ更新後 |
| 削除時 | コンテンツ削除後 |
| 公開時 | 公開ステータス変更時 |

**利用可能な変数:**
```smarty
{$topics.topics_id}      {* コンテンツID *}
{$topics.subject}        {* タイトル *}
{$topics.contents}       {* 本文 *}
{$topics.ymd}            {* 公開日 *}
{$topics.ext_col_01}     {* 拡張項目 *}
```

### フォーム送信時のトリガー

管理画面: [フォーム] → [トリガー設定]

```smarty
{$inquiry.inquiry_id}    {* 回答ID *}
{$inquiry.name}          {* 名前 *}
{$inquiry.email}         {* メールアドレス *}
{$inquiry.message}       {* メッセージ *}
```

## 外部サービス連携

**詳細な連携パターン**: [references/integrations.md](references/integrations.md) を参照

### Slack通知

```smarty
{assign var="message" value=$dataSet.emptyArray}
{append var="message" index="text" value="通知メッセージ"}

{slack_send
  webhook_url="https://hooks.slack.com/services/xxx/yyy/zzz"
  body=$message|@json_encode
}
```

### メール通知

```smarty
{send_mail
  to="recipient@example.com"
  subject="件名"
  body="本文"
}
```

### GitHub Actions連携

```smarty
{assign var="headers" value=$dataSet.emptyArray}
{append var="headers" index="Authorization" value="token YOUR_GITHUB_TOKEN"}
{append var="headers" index="Accept" value="application/vnd.github.v3+json"}

{assign var="body" value=$dataSet.emptyArray}
{append var="body" index="event_type" value="kuroco-update"}

{api_request
  url='https://api.github.com/repos/owner/repo/dispatches'
  method='POST'
  headers=$headers
  body=$body|@json_encode
  var='response'
}
```

## ベストプラクティス

### 負荷を考慮した実行時間

- システム負荷の低い時間帯（深夜・早朝）に設定
- 大量データ処理は1日1回に制限
- ページネーションを使用して分割処理

### エラーハンドリング

```smarty
{api_internal
  endpoint='/rcms-api/1/news'
  method='GET'
  member_id=1
  var='response'
}

{if $response.errors}
  {slack_send webhook_url="..." text="エラー: {$response.errors|@json_encode}"}
  {log message="エラー: {$response.errors|@json_encode}"}
{else}
  {log message="処理完了: {$response.pageInfo.totalCnt}件"}
{/if}
```

### タイムアウト対策

大量データは分割処理:

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

## 関連ドキュメント

- `docs/tutorials/how-to-use-batch.md` - バッチ処理の使い方
- `docs/tutorials/auto-run-github-with-contents-update.md` - GitHub Actions連携
- `docs/tutorials/send-slack-notification-after-a-form-has-been-submitted.md` - Slack通知
- `docs/reference/smarty-plugin.md` - Smartyプラグイン
- `docs/reference/trigger-variables.md` - トリガー変数
