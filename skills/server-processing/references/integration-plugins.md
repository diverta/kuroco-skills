# 外部サービス連携プラグイン

## 目次

- [sendmail](#sendmail) - メールを送信します。
- [slack_post_message](#slack_post_message) - Slackにメッセージを投稿します。
- [slack_get_message](#slack_get_message) - Slackから特定のメッセージを取得します。
- [slack_team_info](#slack_team_info) - Slackのチーム情報を取得します。
- [ai_completion](#ai_completion) - OpenAIを使用したAI補完（チャット）を行います。
- [ai_embeddings](#ai_embeddings) - OpenAIを使用してテキストのAI埋め込み（Embeddi...
- [twitter_post_message](#twitter_post_message) - Twitter（X）にツイートを投稿します。
- [github_deploy](#github_deploy) - GitHubデプロイを実行します。
- [gcloud_functions_token](#gcloud_functions_token) - Google Cloud Functionsトークンを取得し...
- [gcloud_pubsub_publish](#gcloud_pubsub_publish) - Google Cloud Pub/Subにメッセージを発行し...
- [googleanalytics](#googleanalytics) - Google Analyticsからデータを取得し、Topi...
- [purge_cdn_cache](#purge_cdn_cache) - CDNおよびイメージCDNのキャッシュをパージ（削除）します...
- [site_sync](#site_sync) - マルチサイト環境でサイト間の同期ジョブをキックします。
- [batch](#batch) - バッチ処理を登録・実行します。

---

## sendmail

メールを送信します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 送信結果を格納する変数名 |

### Return Value

`var` パラメータで指定した変数に送信結果が代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{sendmail var=result to="user@example.com" subject='testmail' contents="This is test." from="test@example.com" from_nm="Test Sender"}
{* メンバーIDで宛先を指定 *}
{sendmail var=result to_member_id="1,2,3" subject='Notice' contents="Hello members!"}
{* メールテンプレートを使用 *}
{sendmail var=result to=$email mail_template="notification" custom_var=$data}
{* SendGrid custom_args を指定（assign_array で事前に組み立てる）*}
{assign_array var="args" keys="campaign_id,order_ref" values="summer-2026,order-12345"}
{sendmail var=result to="user@example.com" subject="Hello" contents="Body" sg_custom_args=$args}
```

### Notes

- `mail_template` を使用する場合、`to`, `subject`, `contents` は省略可能です。`to_member_id`, `cc_member_id`, `bcc_member_id` を指定すると、メンバーのメールアドレスが自動的に取得されます。`sg_custom_args` はプラットフォーム予約済みキーを使用できません。

---

## slack_post_message

Slackにメッセージを投稿します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 結果を代入する変数名 |

### Return Value

`var` パラメータを指定した場合、API呼び出しの結果が変数に代入されます。

### Usage Example

```smarty
{* チャンネルにメッセージを投稿 *}
{slack_post_message channel="#general" text="Hello from Kuroco!"}
{* スレッドに返信 *}
{slack_post_message channel="#support" text="ありがとうございます" thread_ts="1234567890.123456"}
{* ダイレクトメッセージを送信 *}
{slack_post_message users="U1234567890" text="個別のお知らせです"}
{* Block Kit でリッチメッセージを送信 *}
{slack_post_message channel="#general" text="フォールバックテキスト" blocks='[{"type":"section","text":{"type":"mrkdwn","text":"*太字* のメッセージ"}}]'}
```

### Notes

- `channel` または `users` のどちらか一方は必須です。`text` パラメータは必須です。サイト設定でSlack連携が有効で、`slack_bot_token` が設定されている必要があります。

---

## slack_get_message

Slackから特定のメッセージを取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にメッセージの内容が代入されます。

### Usage Example

```smarty
{* 特定のメッセージを取得 *}
{slack_get_message var="message" channel="C1234567890" ts="1234567890.123456"}
{* 取得したメッセージを表示 *}
{if $message}
    <p>メッセージ: {$message.text}</p>
    <p>投稿者: {$message.user}</p>
{/if}
```

### Notes

- `channel` と `ts` の両方が必須です。サイト設定でSlack連携が有効で、`slack_bot_token` が設定されている必要があります。

---

## slack_team_info

Slackのチーム情報を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にチーム情報が代入されます。

### Usage Example

```smarty
{* チーム情報を取得 *}
{slack_team_info var="team" team="T1234567890"}
{* 取得した情報を表示 *}
{if $team}
    <h2>{$team.name}</h2>
    <p>ドメイン: {$team.domain}</p>
    <img src="{$team.icon.image_68}" alt="Team icon">
{/if}
```

### Notes

- `team` パラメータは必須です。サイト設定でSlack連携が有効で、`slack_bot_token` が設定されている必要があります。

---

## ai_completion

OpenAIを使用したAI補完（チャット）を行います。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にAIからの応答テキストが代入されます。エラー時や応答がない場合は空文字列が代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{ai_completion var='result' message='What is Kuroco?' model='gpt-4'}
{* 会話履歴を含める *}
{assign_array var='history' values=''}
{ai_completion var='result' message='Tell me more' messages=$history model='gpt-4'}
{* システムプロンプトを使用 *}
{ai_completion var='result' message='You are a helpful assistant.' role='system' model='gpt-4'}
```

### Notes

- サイト設定で `use_openai` が有効である必要があります
- `model` パラメータは必須で、COMPLETIONS_MODELSに定義されているモデルのみ使用可能です
- `message` パラメータが空の場合はエラーログが記録され、処理が終了します
- `messages` パラメータが文字列の場合、自動的にユーザーメッセージとして配列に変換されます
- バリデーションモード（`_rcms_validate`）の場合、実際のAPI呼び出しは実行されません

---

## ai_embeddings

OpenAIを使用してテキストのAI埋め込み（Embeddings）を作成・保存します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数に `true` が代入されます（成功時）。

### Usage Example

```smarty
{* 基本的な使用例 *}
{ai_embeddings var='result' text='This is sample text for embedding.' module_id=1 title='Sample'}
{* トピックスのコンテンツを埋め込む *}
{ai_embeddings var='result' text=$topics.subject module_id=$topics.topics_id title=$topics.subject slug=$topics.slug}
{* 複数言語対応 *}
{ai_embeddings var='result' text=$content module_id=100 lang='en' title='English Content'}
{* インデックスを指定して複数の埋め込みを保存 *}
{ai_embeddings var='result' text=$section1 module_id=100 index=0 title='Section 1'}
{ai_embeddings var='result' text=$section2 module_id=100 index=1 title='Section 2'}
```

### Notes

- サイト設定で `use_openai` が有効である必要があります
- `text` パラメータが空の場合はエラーログが記録され、処理が終了します
- テキストは自動的に正規化されます（改行や連続スペースの処理）
- 同じ `module_id`, `module_nm`, `lang`, `index` の組み合わせで既存データがある場合は更新されます
- 埋め込み処理はバッチジョブとして非同期で実行されます
- バリデーションモード（`_rcms_validate`）の場合、実際の処理は実行されません

---

## twitter_post_message

Twitter（X）にツイートを投稿します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 結果を代入する変数名 |

### Return Value

`var` パラメータを指定した場合、API呼び出しの結果がJSON形式の文字列として変数に代入されます。

### Usage Example

```smarty
{* 基本的な投稿 *}
{twitter_post_message text="新しい記事を公開しました！"}
{* 結果を取得して処理 *}
{twitter_post_message var="result" text="Hello from Kuroco!"}
```

### Notes

- `text` パラメータは必須です。サイト設定でTwitter連携が有効（`use_twitter=true`）で、`twitter_api_key`、`twitter_api_key_secret`、`twitter_token`、`twitter_token_secret` が設定されている必要があります。Twitter API v2 を使用します。

---

## github_deploy

GitHubデプロイを実行します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | 結果を代入する変数名 |

### Return Value

`var`パラメータで指定した変数にデプロイ結果が代入されます。

### Usage Example

```smarty
{github_deploy var="result"}
```

### Notes

- GitHubと連携したデプロイを実行します
- GitHub連携が設定されている必要があります

---

## gcloud_functions_token

Google Cloud Functionsトークンを取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | トークンを代入する変数名 |

### Return Value

`var`パラメータで指定した変数にGoogle Cloud Functionsトークンが代入されます。

### Usage Example

```smarty
{gcloud_functions_token var="token"}
```

### Notes

- Google Cloud Functionsの認証に使用するトークンを取得します
- Google Cloudが設定されている必要があります

---

## gcloud_pubsub_publish

Google Cloud Pub/Subにメッセージを発行します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | 結果を代入する変数名 |

### Return Value

`var`パラメータで指定した変数に発行結果が代入されます。

### Usage Example

```smarty
{gcloud_pubsub_publish topic="my-topic" message="Hello World" var="result"}
```

### Notes

- Google Cloud Pub/Subにメッセージを発行します
- Google Cloudが設定されている必要があります

---

## googleanalytics

Google Analyticsからデータを取得し、Topicsのカウンター拡張項目を更新します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 取得したデータを格納する変数名 |

### Return Value

`var`にページパスとPV数の連想配列が代入されます。

### Usage Example

```smarty
{* PVデータを取得して変数に格納 *}
{googleanalytics var='pv_data' startDate='-30 day'}
{* TopicsのPVカウンターを更新 *}
{googleanalytics
  topics_group_id=1
  update_column_slug='pv_count'
  startDate='-7 day'
  updated_topics_ids='updated_ids'
}
{* GA4でカスタムクエリを使用 *}
{googleanalytics var='data' queries=$custom_queries}
{* GA4で取得メトリクスと並び替えメトリクスを別々に指定 *}
{googleanalytics
  var='data'
  update_target_metric='engagedSessions'
  update_target_order_metric='screenPageViews'
}
```

### Notes

- Google Analytics APIの認証設定が必要です
- GA4とUniversal Analytics（GA3）の両方に対応しています
- `topics_group_id`と`update_column_slug`を指定するとTopicsのカウンター拡張項目を自動更新します

---

## purge_cdn_cache

CDNおよびイメージCDNのキャッシュをパージ（削除）します。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

なし

### Usage Example

```smarty
{* 特定のコンテンツ定義のキャッシュをパージ *}
{purge_cdn_cache module="topics" topics_group_id=123}
{* 全てのキャッシュをパージ *}
{purge_cdn_cache module="all"}
{* 特定のAPIエンドポイントのキャッシュをパージ *}
{purge_cdn_cache api_endpoint="/rcms-api/1/list"}
```

### Notes

- `module` または `api_endpoint` のどちらか一方は必須です。`module="all"` の場合は画像CDN、フロントCDN、CDN、エッジCDNのすべてがパージされます。

---

## site_sync

マルチサイト環境でサイト間の同期ジョブをキックします。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

なし

### Usage Example

```smarty
{* サイトキーを使用して同期 *}
{site_sync from_site_key="staging" to_site_key="production" sync_type=1}
{* サイトIDを使用して同期 *}
{site_sync from_site_id=10 to_site_id=20 sync_type=2}
{* フル同期（ファイルを含む） *}
{site_sync from_site_key="staging" to_site_key="production" sync_type=2}
```

### Notes

- 同期元と同期先が同じサイトの場合はエラーになります。過去6時間以内に同じ同期先への同期が実行されている場合は新しい同期は開始されません。

---

## batch

バッチ処理を登録・実行します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 新規作成されたバッチIDを格納する変数名 |

### Return Value

`var`パラメータで指定した変数に新規作成されたバッチIDが代入されます。

### Usage Example

```smarty
{* バッチIDで実行 *}
{batch batch_id=1234 ext_data=$ext_data}
{* スラッグで実行 *}
{batch name='sample_batch' ext_data=$ext_data var='new_batch_id'}
{* モジュールのデフォルトバッチを登録 *}
{batch module='topics' name='sync_counter' ext_data=$ext_data}
{* 実行日時を指定 *}
{batch name='scheduled_task' do_datetime='2024-12-01 09:00' ext_data=$data}
```

### Notes

- `batch_id`または`name`のいずれかは必須です
- `module`を指定すると1回のみ実行のバッチとして登録されます
- 同一テンプレート内での重複実行は防止されます

