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
{secret var='github_token' key='GITHUB_TOKEN'}
{assign_array var=headers values=""}
{append var=headers value="Authorization: token `$github_token`"}
{append var=headers value='Accept: application/vnd.github.v3+json'}

{assign_array var=body values=""}
{append var=body index='event_type' value='kuroco-update'}

{api
  endpoint='https://api.github.com/repos/owner/repo/dispatches'
  method='POST'
  headers=$headers
  json_body=$body|@json_encode
  var='response'
  status_var='status'
}
```

## Slack通知

プラグイン名は **`slack_post_message`**（`slack_send` というプラグインは存在しない）。
事前にサイト設定でSlack連携を有効化し、`slack_bot_token` を設定しておく（Incoming Webhook URLは使わない）。

### 基本通知

```smarty
{slack_post_message
  channel="#general"
  text="新しいコンテンツが公開されました"
}
```

### 通知に情報を含める

パラメータは `channel` / `users` / `text` / `thread_ts` / `var` のみ（アタッチメント形式は非対応）。
必要な情報は `text` に組み立てて渡す。

```smarty
{capture assign="slack_text"}新規公開: {$topics.subject}
{$topics.contents|strip_tags|truncate:100}{/capture}

{slack_post_message
  channel="#notifications"
  text=$slack_text
}
```

## Chatwork通知

Chatwork専用のプラグインは無い。公式チュートリアル（`send-chatwork-notification-after-a-form-has-been-submitted`）のとおり、
`{api}` プラグインでChatwork APIを直接呼ぶ。APIトークンは `{secret}` に登録して読み出す。

```smarty
{secret var='chatwork_token' key='CHATWORK_API_TOKEN'}
{assign_array var=headers values=""}
{append var=headers value="X-ChatWorkToken: `$chatwork_token`"}
{append var=headers value='Content-Type: application/x-www-form-urlencoded'}

{api
  endpoint='https://api.chatwork.com/v2/rooms/{ルームID}/messages'
  method='POST'
  headers=$headers
  body="body=[info][title]お知らせ[/title]新しいコンテンツが公開されました[/info]"|@json_encode
  var='response'
  status_var='status'
}
```

## メール通知

プラグイン名は **`sendmail`**（`send_mail` ではない）。本文のパラメータ名は **`contents`**（`body` ではない）。

```smarty
{sendmail
  to="recipient@example.com"
  subject="【通知】新規コンテンツ公開"
  contents="新しいコンテンツが公開されました。

タイトル: {$topics.subject}
公開日: {$topics.ymd}

詳細はこちら: https://example.com/news/{$topics.topics_id}"
}
```

## SendGrid連携

管理画面: [外部システム連携] → [SendGrid]

`sendgrid_send` というプラグインは無い。SendGrid連携を有効にすると **`sendmail` がSendGrid経由で送信**される。
SendGridの `custom_args` を渡す場合は `sg_custom_args`（連想配列・最大5件）を使う。

```smarty
{assign_array var="args" keys="campaign_id" values="summer-2026"}
{sendmail
  to="recipient@example.com"
  subject="件名"
  contents="本文"
  from="sender@example.com"
  sg_custom_args=$args
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

前処理・後処理の制御は**予約変数への代入**で行う（`set_request_param` / `set_error` / `set_response_param` というプラグインは存在しない）。

### 前処理の例

参照用: `$meta`（エンドポイント情報）/ `$url` / `$body`（リクエストボディ）。
制御用: `$request`（メイン処理に渡す値の追加・上書き）/ `$errors`（エラー応答）/ `$http_code`。

```smarty
{* パラメータの加工: $request.キー名 への代入でメイン処理に渡す値を上書き *}
{assign_array var='request' values=''}
{assign var='request.param' value=$body.param|upper}

{* バリデーション: $errors に代入するとエラー応答になり、$http_code で上書きできる *}
{if !$body.required_field}
  {assign var='errors' value="必須項目が入力されていません"}
  {assign var='http_code' value=400}
{/if}
```

### 後処理の例

参照用: `$json`（メイン処理のオリジナル出力）。制御用: `$processed_json`（**必須**。レスポンスになるJSONを代入）/ `$errors` / `$http_code`。

```smarty
{* レスポンスの加工: $json を元に $processed_json を組み立てる *}
{assign var="processed_json" value=$json}
{assign var="processed_json.custom_field" value="追加データ"}

{* 条件に応じた通知 *}
{if $json.errors|@count == 0}
  {slack_post_message
    channel="#notifications"
    text="処理が完了しました"
  }
{/if}
```
