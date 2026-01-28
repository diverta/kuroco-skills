# 外部サービス連携

## GitHub Actions連携

コンテンツ更新時にGitHub Actionsを自動実行。

### GitHub側の設定

```yaml
name: Deploy
on:
  workflow_dispatch:
  repository_dispatch:
    types: [kuroco-update]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build
```

### Kuroco側（トリガー）

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

## Slack通知

### 基本通知

```smarty
{assign var="message" value=$dataSet.emptyArray}
{append var="message" index="text" value="新しいコンテンツが公開されました"}

{slack_send
  webhook_url="https://hooks.slack.com/services/xxx/yyy/zzz"
  body=$message|@json_encode
}
```

### リッチ通知（アタッチメント）

```smarty
{assign var="attachment" value=$dataSet.emptyArray}
{append var="attachment" index="color" value="#36a64f"}
{append var="attachment" index="title" value=$topics.subject}
{append var="attachment" index="text" value=$topics.contents|strip_tags|truncate:100}

{assign var="attachments" value=$dataSet.emptyArray}
{append var="attachments" value=$attachment}

{assign var="message" value=$dataSet.emptyArray}
{append var="message" index="attachments" value=$attachments}

{slack_send
  webhook_url="https://hooks.slack.com/services/xxx/yyy/zzz"
  body=$message|@json_encode
}
```

## Chatwork通知

```smarty
{chatwork_send
  room_id="ルームID"
  api_token="APIトークン"
  message="[info][title]お知らせ[/title]新しいコンテンツが公開されました[/info]"
}
```

## メール通知

```smarty
{send_mail
  to="recipient@example.com"
  subject="【通知】新規コンテンツ公開"
  body="新しいコンテンツが公開されました。

タイトル: {$topics.subject}
公開日: {$topics.ymd}

詳細はこちら: https://example.com/news/{$topics.topics_id}"
}
```

## SendGrid連携

管理画面: [外部システム連携] → [SendGrid]

```smarty
{sendgrid_send
  to="recipient@example.com"
  subject="件名"
  body="本文"
  from="sender@example.com"
}
```

## Webhook呼び出し

### Batch Webhookエンドポイント

外部からバッチ処理を呼び出すためのエンドポイント。

エンドポイント設定:
```
パス: batch/webhook
カテゴリー: バッチ処理
モデル: Batch
オペレーション: webhook
```

### Webhook URL形式

```
POST https://{サイトキー}.g.kuroco.app/rcms-api/{api_id}/batch/webhook
Content-Type: application/json

{
  "batch_id": "バッチの識別子"
}
```

### GitHub Actionsからの呼び出し例

```yaml
name: Trigger Kuroco Batch
on:
  workflow_dispatch:

jobs:
  trigger:
    runs-on: ubuntu-latest
    steps:
      - name: Call Kuroco Webhook
        run: |
          curl -X POST \
            -H "Content-Type: application/json" \
            -H "X-RCMS-API-ACCESS-TOKEN: ${{ secrets.KUROCO_TOKEN }}" \
            -d '{"batch_id": "csv_export"}' \
            https://example.g.kuroco.app/rcms-api/1/batch/webhook
```

## カスタム処理（Function）

管理画面: [API] → [カスタム処理]

### 処理タイプ

| タイプ | 実行タイミング | 用途 |
|--------|--------------|------|
| 前処理 | APIメイン処理の前 | リクエスト検証、パラメータ加工 |
| 後処理 | APIメイン処理の後 | レスポンス加工、通知送信 |
| 独自API | 完全カスタム | 外部API連携、複雑なロジック |

### 前処理の例

```smarty
{* リクエストパラメータの取得 *}
{assign var="request" value=$smarty.request}

{* パラメータの加工 *}
{assign var="modified_value" value=$request.param|upper}
{set_request_param key="param" value=$modified_value}

{* バリデーション *}
{if !$request.required_field}
  {set_error code=400 message="必須項目が入力されていません"}
{/if}
```

### 後処理の例

```smarty
{* レスポンスの加工 *}
{assign var="response" value=$api_response}

{* カスタムフィールドを追加 *}
{set_response_param key="custom_field" value="追加データ"}

{* 条件に応じた通知 *}
{if $response.status == "success"}
  {slack_send
    webhook_url="..."
    text="処理が完了しました"
  }
{/if}
```
