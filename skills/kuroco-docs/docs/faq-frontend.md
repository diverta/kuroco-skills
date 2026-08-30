# Kurocoドキュメント: FAQ / フロントエンド・KurocoFront

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- KurocoFrontの利用に制限事項はありますか（`are-there-any-restrictions-on-using-kurocofront`）
- KurocoFrontをProxy Serverを通して別のサーバーから使うにはどのようにすればよいですか？（`can-i-access-kurocofront-through-a-proxy-server`）
- GitHubを使用せずにKurocoFrontにデプロイできますか？（`can-i-deploy-kurocofront-without-using-github`）
- Kuroco Frontを使わずに自身のサーバーでサイトの表示をできますか？（`can-i-display-the-site-on-my-own-server-without-using-kuroco-front`）
- 時間指定でサイトをメンテナンス表示にできますか？（`can-i-schedule-site-to-display-maintenance-at-specific-time`）
- KurocoFront以外のホスティングサービスにWebhookを送信できますか？（`can-i-send-a-deploy-webhook-to-external-hosting-services`）
- 効果測定タグ(コンバージョンタグ)は利用できますか？（`can-i-use-conversion-tracking-tags`）
- GitHubアカウントを持っていなくてもKurocoを利用できますか？（`can-i-use-kuroco-without-a-github-account`）
- Nuxt.jsのSSGでページ内リンクされていないページを生成することはできますか？（`can-i-use-nuxt-js-ssg-to-generate-pages-that-are-not-linked-in-the-page`）
- Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？（`can-i-use-nuxt-js-ssg-to-reduce-api-calls`）
- GitHubサードパーティ製のアプリを利用して問題ないでしょうか？（`can-i-use-third-party-github-applications`）
- 静的ファイルをジェネレートしたい場合、Kurocoのインフラとは別のサーバーは必要になりますか？（`do-i-need-a-production-server-separate-from-kurocos-infrastructure-to-generate-static-files`）
- コンテンツ更新以外の任意のタイミングでGitHubActionsを使ったdeployを行うには？（`how-can-i-deploy-with-githubactions-at-any-time`）
- 画像のURL末尾にパラメータを付与してもキャッシュがクリアされません。画像のキャッシュクリアの方法を教えて下さい。（`how-do-i-clear-cached-images`）
- SSGにしています。コンテンツ更新後すぐにフロントに反映させるにはどうしたらいいですか？（`how-do-i-reflect-updated-ssg-contents-on-the-frontend`）
- Nuxt.jsでGoogleAnalytics4(GA4)をどのように設定すればいいですか？（`how-do-i-set-up-google-analytics-4-in-nuxtjs`）
- CDNにキャッシュされたレスポンスかどうかの確認方法を教えてください（`how-do-i-verify-responses-in-the-cdn-cache`）
- KurocoFrontでどのハッシュが利用されているかの確認方法を教えてください（`how-do-i-verify-the-hash-responses-used-by-kurocofront`）
- カスタムディメンションで設定されている数値の集計結果を確認する方法はありますか？（`how-to-generate-reports-using-custom-dimensions`）
- サイト内で利用している静的ファイル（画像、JS、CSSなど）はどこに配置するのが良いでしょうか？（`how-to-place-static-files`）
- デプロイしたサイトの表示を404に戻すことはできますか？（`is-it-possible-to-revert-the-deployed-site-to-display-a-404-error`）
- ページをリロードしたり、URLに直接アクセスすると 404 Not Found になります。（`reloading-the-page-or-accessing-it-directly-will-result-in-404-not-found`）
- 独自ドメインを設定しましたがサイトが表示できません。何を確認すれば良いでしょうか？（`setting-up-a-custom-domain`）
- kuroco_front.jsonとは何ですか？（`what-is-kuroco_front_json`）
- KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？（`what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront`）
- 画像を印刷できないときの対処方法を教えてください（`what-should-i-do-if-i-cant-print-an-image`）
- 特定のブラウザで画像が表示されないときの対処方法を教えてください（`what-should-i-do-if-images-are-not-displayed-in-certain-browsers`）


---

# KurocoFrontの利用に制限事項はありますか

> 元ページ: `faq/are-there-any-restrictions-on-using-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/are-there-any-restrictions-on-using-kurocofront/
> 概要: KurocoFrontにアップロードするファイルには制限事項があります。例えば、サーバーサイド側でのプログラムは動作しません。また、SSI、.htaccessは利用できません。

KurocoFrontにアップロードするファイルには制限事項があります。

## 制限事項
### サーバーサイド側でのプログラム
以下のような、サーバーサイド側でのプログラムは動作しません。
- PHP
- CGIcgi
- Perl
- Ruby

:::tip
KurocoのAPIはPHP等からリクエスト可能です。  
PHPを利用したい場合は、PHPが使えるレンタルサーバなどからKurocoのAPIをご利用ください。
:::

### その他
以下はご利用になれません。
- SSI(Server Side Include)
- .htaccess

## 拡張子の制限について
拡張子の制限事項はありません。

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [Kurocoにおける制限事項](/ja/docs/reference/limitations-in-kuroco/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [Kuroco Frontを使わずに自身のサーバーでサイトの表示をできますか？](/ja/docs/faq/can-i-display-the-site-on-my-own-server-without-using-kuroco-front/)


---

# KurocoFrontをProxy Serverを通して別のサーバーから使うにはどのようにすればよいですか？

> 元ページ: `faq/can-i-access-kurocofront-through-a-proxy-server` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-access-kurocofront-through-a-proxy-server/
> 概要: https://bar.example.com/foo/ で https://bar.g.kuroco-front.app/foo/ の表示をプロキシーを通して表示させる場合の設定は以下のようになります。

`https://bar.example.com/foo/`で`https://bar.g.kuroco-front.app/foo/`の表示をプロキシーを通して表示させる場合の設定は以下のようになります。

### nginxの場合
```
location /foo {
    proxy_pass https://bar.g.kuroco-front.app;
    proxy_redirect     https://bar.g.kuroco-front.app/foo https://bar.example.com/foo;
    proxy_set_header   Host bar.g.kuroco-front.app;
}
```

### Apache2.4のmod_proxyを利用する場合
```
ProxyRequests Off

ProxyPass /foo https://bar.g.kuroco-front.app/foo
ProxyPassReverse /foo https://bar.g.kuroco-front.app/foo
ProxyPreserveHost Off
```

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [Kuroco Frontを使わずに自身のサーバーでサイトの表示をできますか？](/ja/docs/faq/can-i-display-the-site-on-my-own-server-without-using-kuroco-front/)


---

# GitHubを使用せずにKurocoFrontにデプロイできますか？

> 元ページ: `faq/can-i-deploy-kurocofront-without-using-github` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/
> 概要: デプロイ用の全ファイルが圧縮されたZIPファイルのURLをKurocoに通知すると、そのZIPファイルをダウンロードしてKurocoFrontに展開できる機能があります。kuroco_front.jsonを含む静的ビルドされたファイル群をZIP圧縮し、AWSやKurocoFiles等に設置してWebhookを送信してください。

デプロイ用の全ファイルが圧縮されたZIPファイルのURLをKurocoに通知すると、そのZIPファイルをダウンロードしてKurocoFrontに展開できる機能があります。  

kuroco_front.jsonを含む静的ビルドされたファイル群をZIP圧縮し、AWSやKurocoFiles等に設置してWebhookを送信してください。

## デプロイ方法

```bash
#ご利用のサイトのAPIエンドポイントを指定 
endpoint="https://sitekey.g.kuroco.app" 

#アカウント管理で指定してあるKurocoFrontのドメイン 
domain="sitekey.g.kuroco-front.app" 

#フロントエンドドメインをSHA1でハッシュ化した40桁のハッシュ値 
hash="****************************************" 

#zipファイルのダウンロードURL 
storage_url="https://sitekey.g.kuroco-img.app/files/user/deploy_file/public.zip" 

#管理画面の[チャネル] -> [WEB] -> [KurocoFront設定]にあるtoken 
token="************************************" 

#以下のwebhookを送信する
curl -X POST "${endpoint}/direct/menu/github/" \
     -H 'Content-Type: application/json;charset=utf-8' \
     -H "X-Kuroco-Auth: token ${token}" \
     -d "{\"data\":{\"domain\":\"${domain}\", \"hash\":\"${hash}\",\"storage_url\":\"${storage_url}\"}}"
```

:::info
ZIPファイルはnpm run build、npm run generate等で作成したファイルを、展開直後にkuroco_front.jsonを含むファイル群が存在するように作成してください。
:::

:::tip
Windowsのコマンドプロンプトからcurlを送信する場合は、シングルクォーテーション(`'`)をダブルクォーテーション(`"`)に変換してください。  
また、バックスラッシュ(`\`)がエスケープ文字として扱われるため、改行の`\`は`^`に変換しててください。
:::

Kurocoへのリクエストが成功すると、`deploy requested!` のレスポンスがあります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e40b69986a7964cffbb02b4bbb8e0b6a.png)

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)


---

# Kuroco Frontを使わずに自身のサーバーでサイトの表示をできますか？

> 元ページ: `faq/can-i-display-the-site-on-my-own-server-without-using-kuroco-front` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-display-the-site-on-my-own-server-without-using-kuroco-front/
> 概要: 利用できます。Kuroco は API のみを提供していますので、アプリケーションをホスティングするサーバーはお好きなものをご使用いただけます。

Kuroco は Headless CMS であるため、アプリケーションのホスティングサーバーはご自由にお選びいただけます。
なお、表示方法はサーバーごとに異なるため、ご利用の環境に合わせて設定してください。

ホスティングサービスの例:
- [Vercel](https://vercel.com/docs/deployments/overview)
- [Cloudflare Pages](https://www.cloudflare.com/ja-jp/developer-platform/products/pages/)
- [Netlify](https://docs.netlify.com/site-deploys/overview/)
- [Azure Static Web Apps](https://azure.microsoft.com/ja-jp/products/app-service/static/)
- [AWS Amplify](https://aws.amazon.com/jp/amplify/)

また、レンタルサーバーでのホスティングも可能です。
レンタルサーバー上で動作するアプリケーションから Kuroco の API を呼び出し、ページを表示することができます。
ただし、他のホスティングサービスと比較すると、CI/CD ツールとの連携において追加の工数が発生する場合があります。

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [KurocoFront以外のホスティングサービスにWebhookを送信できますか？](/ja/docs/faq/can-i-send-a-deploy-webhook-to-external-hosting-services/)
- [KurocoFrontの利用に制限事項はありますか](/ja/docs/faq/are-there-any-restrictions-on-using-kurocofront/)
- [静的ファイルをジェネレートしたい場合、Kurocoのインフラとは別のサーバーは必要になりますか？](/ja/docs/faq/do-i-need-a-production-server-separate-from-kurocos-infrastructure-to-generate-static-files/)


---

# 時間指定でサイトをメンテナンス表示にできますか？

> 元ページ: `faq/can-i-schedule-site-to-display-maintenance-at-specific-time` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-schedule-site-to-display-maintenance-at-specific-time/
> 概要: メンテナンス用の静的ファイルを設置して、時間指定でデプロイリクエストを送ることで対応できます。デプロイリクエストはKurocoのバッチ処理で実行することもできます。

メンテナンス用の静的ファイルを設置して、時間指定でデプロイリクエストを送ることで対応できます。

:::note
時間指定が不要で、IPアドレス制限をかける時間帯にフロントエンド更新の作業ができる場合、メンテナンスモードの表示には`kuroco_front.json`の設定を利用することもできます。詳細は[特定のIPアドレス以外はメンテナンスページを表示したいです](/ja/docs/faq/how-to-display-maintenance-page-except-for-specific-ip-addresses/)を参照してください。
:::

:::tip
メンテナンス表示のスケジュール設定やパス単位でのアクセス制限など、より高度な制御が必要な場合は[KurocoEdge](https://kurocoedge.com/ja/)の利用もご検討ください。KurocoEdgeではスケジュール設定によるメンテナンスページの表示切替が可能です。
:::

以下では、KurocoFrontのデプロイ機能を使って対応する方法を紹介します。

## 事前準備

### 1. デプロイ用ZIPファイルの作成

メンテナンスページ用のHTMLファイルと`kuroco_front.json`を含むZIPファイルを作成します。

```
maintenance_deploy.zip
├── index.html   (メンテナンスページ)
└── kuroco_front.json
```

### 2. ZIPファイルの設置

作成したZIPファイルをKurocoFiles等にアップロードします。

### 3. デプロイに必要な情報の確認

「[GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)」を参考に、以下の情報を確認してください。

- APIエンドポイント（例: `https://sitekey.g.kuroco.app`）
- KurocoFrontのドメイン（例: `sitekey.g.kuroco-front.app`）
- フロントエンドドメインのSHA1ハッシュ値
- ZIPファイルのダウンロードURL
- KurocoFront設定のtoken

## デプロイリクエストの送信

指定の日時に、以下のようなcurlコマンドでデプロイリクエストを送信します。

```bash
endpoint="https://sitekey.g.kuroco.app"
domain="sitekey.g.kuroco-front.app"
hash="****************************************"
storage_url="https://sitekey.g.kuroco-img.app/files/user/deploy_file/maintenance_deploy.zip"
token="************************************"

curl -X POST "${endpoint}/direct/menu/github/" \
     -H 'Content-Type: application/json;charset=utf-8' \
     -H "X-Kuroco-Auth: token ${token}" \
     -d "{\"data\":{\"domain\":\"${domain}\", \"hash\":\"${hash}\",\"storage_url\":\"${storage_url}\"}}"
```

:::tip
サイトを復元する場合は、GitHub Actionsを実行して連携されたGitHubの成果物をデプロイしてください。
また、通常の成果物のZIPファイルを別途用意し、同様のデプロイリクエストを送信する方法でも構いません。
:::

## Kurocoのバッチ処理でデプロイリクエストを実行する場合

デプロイリクエストをKurocoのバッチ処理で実行することもできます。バッチ処理を作成し、実行タイミングを「毎日」に設定して、`date`のSmartyプラグインで日時を判定することで、指定の日時にデプロイを自動実行できます。

### 特定の日付にメンテナンス表示にする例

```smarty
{* 指定日付以外はスキップ *}
{date var='today' time='now' format='Y-m-d'}
{if $today != '2026-03-15'}
    {return}
{/if}

{* 変数の設定 *}
{assign var="endpoint" value="https://sitekey.g.kuroco.app"}
{assign var="domain" value="sitekey.g.kuroco-front.app"}
{rcms_hash var='hash' data='domain' algo='SHA1'}
{assign var="storage_url" value="https://sitekey.g.kuroco-img.app/files/user/deploy_file/maintenance_deploy.zip"}
{assign var="token" value="****************************************************************"}

{* ヘッダーの設定 *}
{assign_array var="headers" values=""}
{append var="headers" value="Content-Type: application/json;charset=utf-8"}
{append var="headers" value="X-Kuroco-Auth: token `$token`"}

{* リクエストボディの設定 *}
{assign_array var="body" values=""}
{assign_array var="body.data" values=""}
{assign var="body.data.domain" value=$domain}
{assign var="body.data.hash" value=$hash}
{assign var="body.data.storage_url" value=$storage_url}

{* APIリクエスト実行 *}
{api
  endpoint="`$endpoint`/direct/menu/github/"
  method="POST"
  headers=$headers
  body=$body
  var="response"
  status_var="status"
}
```

:::info
バッチ処理の実行タイミングの詳細な設定方法については「[バッチ処理の実行を指定の日時や週次に設定できますか？](/ja/docs/faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly/)」を参照してください。
:::

## 関連ドキュメント
- [バッチ処理の実行を指定の日時や週次に設定できますか？](/ja/docs/faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly/)
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)
- [特定のIPアドレス以外はメンテナンスページを表示したいです](/ja/docs/faq/how-to-display-maintenance-page-except-for-specific-ip-addresses/)
- [管理画面マニュアル: バッチ一覧](/ja/docs/management/batch/)
- [KurocoEdge](https://kurocoedge.com/ja/)


---

# KurocoFront以外のホスティングサービスにWebhookを送信できますか？

> 元ページ: `faq/can-i-send-a-deploy-webhook-to-external-hosting-services` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-send-a-deploy-webhook-to-external-hosting-services/
> 概要: 可能です。`{api}`のSmartyプラグインを使用して、外部サービスにリクエストを送信してください

可能です。  
[`{api}`](/ja/docs/reference/smarty-plugin/#api)のSmartyプラグインを使用して、外部サービスにリクエストを送信してください。
Webhookの送信先URLやリクエスト内容はカスタム処理で記述し、送信のタイミングは希望するトリガーを設定して調整します。

これにより、KurocoFront以外のサービスでホスティングしている場合でも、コンテンツ更新後などの任意のタイミングで自動的にビルドを実行できます。

## コンテンツの更新後のトリガーでWebhookを送る方法

### リクエストの内容を調整する
例えば、VercelにDeploy Hookを送る場合はカスタム処理に以下のコードを書きます。  
endpointのURLは[Vercelのドキュメント](https://vercel.com/docs/deploy-hooks)を参考にVercel側で発行してください。

```smarty
{api
    endpoint='https://api.vercel.com/v1/integrations/deploy/prj_******************'
    method="POST"
    var=response
    status_var=status
}

{logger msg1="vercel deploy" msg2=$response}
```

### Webhookの送信タイミングを設定する
追加したカスタム処理に[コンテンツの更新後]のトリガーを設定します。  
名称横のボックスに`1`を入力するとコンテンツ定義ID=1のコンテンツがトリガーの対象になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0ab88b9bfa01546bae7168354c889f2.png)

これにより対象のコンテンツが更新されるとVercelにDeploy Hookが送信され、自動でビルドが開始します。

:::tip
利用できるトリガーの一覧は以下を参照してください。
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
:::

## Githubのデプロイリクエスト時のトリガーでWebhookを送る方法

「[Githubのデプロイリクエスト時](/ja/docs/reference/trigger-variables/#githubのデプロイリクエスト時)」のトリガーは、KurocoからGitHub ActionsへのWebhook時に動作します。  
こちらのトリガーを利用して、デフォルトのGitHub Actionsへのリクエストを任意のホスティングサービスに書き換える事で、KurocoFront以外のホスティングサービスを利用している場合でも、
コンテンツ編集画面のGithub Actionsワークフローの設定でデプロイの有無を制御できるようになります。

例えば、以下のようにカスタム処理を設定すると、デフォルトのGitHub Actionsへのリクエストをキャンセルし、Vercelへのデプロイフック送信ができます。  
endpointのURLは[Vercelのドキュメント](https://vercel.com/docs/deploy-hooks)を参考にVercel側で発行してください。

```smarty
{api
    endpoint='https://api.vercel.com/v1/integrations/deploy/prj_******************'
    method="POST"
    var=response
    status_var=status
}

{logger msg1="vercel deploy" msg2=$response}
{assign var='cancel_github_deploy_request' value=true}
```

## 代表的なホスティングサービス

他のホスティングサービスを利用する場合も、同様にWebhookを送信する任意の処理を設定してください。

| ホスティングサービス       | 機能名称             | 公式ドキュメントリンク |
|----------------------------|----------------------|-------------------------|
| **Vercel**                 | Deploy Hook          | [公式ドキュメント](https://vercel.com/docs/deploy-hooks) |
| **Netlify**                | Build Hook           | [公式ドキュメント](https://docs.netlify.com/configure-builds/build-hooks/) |
| **Cloudflare Pages**       | Deploy Hook          | [公式ドキュメント](https://developers.cloudflare.com/pages/configuration/deploy-hooks/) |
| **GitHub Pages**           | Webhook              | [公式ドキュメント](https://docs.github.com/ja/webhooks/using-webhooks/creating-webhooks) |
| **Firebase Hosting**       | REST API             | [公式ドキュメント](https://firebase.google.com/docs/hosting/api-deploy) |
| **AWS Amplify**            | Incoming Webhook     | [公式ドキュメント](https://docs.aws.amazon.com/ja_jp/amplify/latest/userguide/create-incoming-webhook.html) |

:::tip
ホスティングサービスへのデプロイを目的としたWebhookだけでなく、Slack、Chatwork、Discordなど任意のサービスへの通知にも利用できます。
:::

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [お問い合わせの受信通知をChatworkで送信する](/ja/docs/tutorials/send-chatwork-notification-after-a-form-has-been-submitted/)


---

# 効果測定タグ(コンバージョンタグ)は利用できますか？

> 元ページ: `faq/can-i-use-conversion-tracking-tags` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-conversion-tracking-tags/
> 概要: フォームの[基本設定]で、効果測定タグ(コンバージョンタグ)を設置し、フロントエンドで利用できます。

## 効果測定タグの設定方法

キャンペーン管理画面の以下の手順で効果測定タグ(コンバージョンタグ)を設定できます：

1. [チャネル] > [WEB] > [フォーム] を開く  
2. 対象フォームの [基本設定] を選択  
3. 「フォーム完了タグ」項目に、設置したいタグ（例：トラッキングコードやカスタムHTMLなど）を入力  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ece2c0197ea2d9d88e5d339fc548c3b.png)

## タグの動作について

設定された「フォーム完了タグ」は、InquiryMessage::send のエンドポイントを利用した場合のレスポンスに含まれるようになります。  
フロントエンド側でタグを取得・利用してください。

## 関連ドキュメント
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [Nuxt.jsでGoogleAnalytics4(GA4)をどのように設定すればいいですか？](/ja/docs/faq/how-do-i-set-up-google-analytics-4-in-nuxtjs/)


---

# GitHubアカウントを持っていなくてもKurocoを利用できますか？

> 元ページ: `faq/can-i-use-kuroco-without-a-github-account` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-kuroco-without-a-github-account/
> 概要: ご利用いただけます。運用サポートをご契約いただくと、ディバータのGitHubリポジトリをご利用いただけます。GitHubを使わずにデプロイする方法もありますが、コードを管理する場所自体は必要です。

ご利用いただけます。運用サポートをご契約いただくと、ディバータのGitHubリポジトリをご利用いただけます。

GitHubを使わずにデプロイする方法もありますが、コードを管理する場所自体は必要です。

:::info
GitHubを使わないデプロイ方法については、[GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)をご覧ください。
:::

特別なご指定がない場合、基本的にはGitHubでコードを管理いただくことになります。

## コードを管理する方法

- お客様でリポジトリを作成し、制作を依頼する
- 制作会社様にリポジトリを管理いただき、サイトを作成いただく
- ディバータのリポジトリを利用する（[利用条件はこちら](/ja/docs/faq/is-it-possible-to-use-a-diverta-managed-github-repository/)）

## 関連ドキュメント

- [Diverta管理のGitHubリポジトリを使用することは可能ですか？](/ja/docs/faq/is-it-possible-to-use-a-diverta-managed-github-repository/)
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)
- [有償サポート](/ja/docs/about/paid-support/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# Nuxt.jsのSSGでページ内リンクされていないページを生成することはできますか？

> 元ページ: `faq/can-i-use-nuxt-js-ssg-to-generate-pages-that-are-not-linked-in-the-page` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-nuxt-js-ssg-to-generate-pages-that-are-not-linked-in-the-page/
> 概要: nuxt.config.js の generate プロパティに routes のオプションを設定することでページ内リンクされていないページを生成することが可能です。

nuxt.config.js の generate プロパティに routes オプションを設定することで、generateした際にページ内リンクされていないページを生成できます。

```js [nuxt.config.js]
generate: {
    routes: [
        '/example/', 
        '/example2/',
        '/example3/test.html',
    ]
}
```
### APIから記事一覧を取得
サイト内に非同期で記事を表示している要素（「もっと見る」を押下すると記事を非同期で表示など）がある場合、generate でその記事のページは生成されないため、routes に生成したいページのディレクトリを設定する必要があります。  
以下はKurocoのAPIから記事一覧のデータを取得し、routes にページのディレクトリを設定する例になります。

```js [nuxt.config.js]
generate: {
    /**
     * APIから記事一覧を取得し、その記事のtopics_idごとにページを作成する例です。
     * まずKurocoからデータ取得、その後`{ route: 'URL' }`というオブジェクトの配列を返すようにすると、
     * サーバ上でのgenerate時に上記全てのデータを静的生成するようになります。
     */ 
    routes: async (callback) => {
        try {
            const topicsListResponse = await
            axios.get('https://xxxxxx.a.kuroco.app/rcms-api/1/topics/list') // APIのエンドポイントが入ります
            const routes = topicsListResponse.data.list.map((item) => {
                return {
                    route: `/topics/${item.topics_id}/`,
                }
            })
            callback(null, routes);
        } catch(e) {
            callback(e, routes);
        }
    },
}
```

### APIから一度に取得する記事の件数が多い場合
APIから一度に取得する記事一覧の件数が500件以上といった膨大な件数の場合、APIへの負荷が高くなってしまい、502エラーが返ってきてしまう場合があります。  
その場合、APIから取得する記事一覧の件数を制限し、繰り返し取得することでAPIへの負荷を削減できます。  
以下はAPIから記事一覧を100件ずつ取得する例になります。

```js [nuxt.config.js]
generate: {
    /**
     * APIから記事一覧を100件(cnt)ずつ取得することでAPIへの負荷を軽減する例です。
     * @note 別の方法として、`cnt: 0`を指定することで記事の全件が取得できますが、記事件数が膨大に存在する場合ビルドに極端に時間がかかる場合がありますのでご注意ください。
     */
    routes: async () => {
        const cnt = 100;
        const fetchAllTopics = async (pageID = 1) => {
            const response = await axios.get('https://xxxxxx.a.kuroco.app/rcms-api/1/topics/list', {
                params: {
                    cnt,
                    pageID,
                }
            });
            const { list, pageInfo } = response.data;
            return pageInfo.totalPageCnt > pageID
                ? [...list, ...(await fetchAllTopics(pageID + 1))]
                : list;
        };
        const topicsList = await fetchAllTopics();
        return topicsList.map((item) => ({
            route: `/topics/${item.topics_id}/`,
        }));
    }
},
```

:::info
[routesについて - Nuxt公式ドキュメント](https://nuxtjs.org/ja/docs/configuration-glossary/configuration-generate/#routes)
:::

## 関連ドキュメント
- [コーポレートサンプルサイトをSSGにする](/ja/docs/tutorials/corporate-sample-site-to-ssg/)
- [Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)
- [SSGにしています。コンテンツ更新後すぐにフロントに反映させるにはどうしたらいいですか？](/ja/docs/faq/how-do-i-reflect-updated-ssg-contents-on-the-frontend/)
- [静的ファイルをジェネレートしたい場合、Kurocoのインフラとは別のサーバーは必要になりますか？](/ja/docs/faq/do-i-need-a-production-server-separate-from-kurocos-infrastructure-to-generate-static-files/)


---

# Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？

> 元ページ: `faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/
> 概要: 事前に一覧の全データをローカルに保存しておくことで、ページ内リンクされていないページを生成することが可能です。

## Nuxt 3でAPIコール回数を削減する方法

### 概要

Nuxt 3でSSG（静的サイト生成）を使用する際、多数のページを生成するとAPIリクエストが増加し、ビルド時間やコストに影響することがあります。この記事では、**事前にデータを一括取得**することで、APIコール回数を効率的に削減する方法を紹介します。

### この方法が役立つケース

- 記事一覧と詳細ページなど、多数のページを生成する場合
- APIコール回数に制限がある場合
- ビルド時間を短縮したい場合
- サーバー負荷を軽減したい場合

### 解決方法

通常のSSGでは、各ページの生成時にAPIリクエストが発生します。例えば、100記事の詳細ページを生成する場合、100回のAPIリクエストが必要になります。

しかし、**プリフェッチ方式**を使用すると、最初に一括でデータを取得し、そのデータを使って各ページを生成できます。これにより、APIリクエスト回数を大幅に削減できます。

## 実装手順

### 1. プリフェッチの基本設定

まず、APIからデータを事前に取得するための環境を構築します。

```bash
# プリフェッチ用のディレクトリとファイルを作成
mkdir -p prefetch/data
touch prefetch/index.js

# .gitignoreにデータディレクトリを追加
echo "prefetch/data" >> .gitignore
```

### 2. プリフェッチスクリプトの作成 (prefetch/index.js)

次に、APIからデータを取得して保存するスクリプトを作成します。以下のコードを `prefetch/index.js` ファイルに保存します。

```javascript
// prefetch/index.js
import fs from 'fs/promises';
import path from 'path';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

// 環境変数の読み込み
dotenv.config();
const ROOT_URL = process.env.NUXT_PUBLIC_API_BASE;

// ファイルパスの設定
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const EXPORT_PATH = path.join(__dirname, 'data');

// 取得対象のAPIエンドポイント一覧
const ALL_LIST_ENDPOINTS = ['/rcms-api/1/example/list'];

// エクスポート先ディレクトリの作成
const createExportPath = async () => {
    try {
        await fs.access(EXPORT_PATH);
    } catch (error) {
        await fs.mkdir(EXPORT_PATH, { recursive: true });
    }
};

// APIデータを取得する関数
async function kurocoAPIAll(endpoint) {
    // 最初のページを取得
    const initialData = await fetch(`${ROOT_URL}${endpoint}`).then(res => res.json());
    const { list, pageInfo } = initialData;
    const totalPageCnt = pageInfo.totalPageCnt;
    
    // 2ページ目以降を並列で取得
    const promises = [];
    for (let i = 2; i <= totalPageCnt; i++) {
        promises.push(
            fetch(`${ROOT_URL}${endpoint}?pageID=${i}`).then(res => res.json())
        );
    }
    
    const allData = await Promise.all(promises);
    const allList = allData.map((data) => data.list).flat();
    
    // 全てのデータを結合
    return [...list, ...allList];
}

// メイン処理
(async () => {
    console.log('データのプリフェッチを開始します');
    
    await createExportPath();
    
    // 全てのエンドポイントからデータを取得して保存
    for (const endpoint of ALL_LIST_ENDPOINTS) {
        const data = await kurocoAPIAll(endpoint);
        const fileName = endpoint.replaceAll('/', '_');
        const filePath = path.join(EXPORT_PATH, `all${fileName}.json`);
        
        await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
        console.log(`データを保存しました: ${filePath}`);
    }
    
    console.log('全てのデータのプリフェッチが完了しました');
})();
```

### 3. package.jsonにスクリプトを追加

プリフェッチを簡単に実行できるようにするため、package.jsonにスクリプトを追加します。

```json
"scripts": {
    "prefetch": "node prefetch/index.js"
}
```

### 4. 一覧ページの実装

プリフェッチしたデータを使用して、一覧ページを実装します。

```markup title="pages/ssg_list/index.vue"
<template>
    <ul>
        <li v-for="item in listJSON" :key="item.topics_id">
            <NuxtLink :to="`/ssg_list/${item.topics_id}`">{{ item.subject }}</NuxtLink>
        </li>
    </ul>
</template>

<script lang="ts" setup>
// プリフェッチしたJSONファイルを読み込む
const { data: listJSON } = await useAsyncData('filteredList', async () => {
    const fullListJSON = await import('~/prefetch/data/all_rcms-api_1_example_list.json')
        .then((m) => m.default);
    
    // 必要なプロパティのみを抽出（データ量削減）
    return fullListJSON.map((item: any) => ({
        topics_id: item.topics_id,
        subject: item.subject
    }));
});
</script>
```

### 5. 詳細ページの実装

同様に、詳細ページもプリフェッチしたデータを使用して実装します。

```markup title="pages/ssg_list/[topics_id].vue"
<template>
    <template v-if="item">
        <h1>
            <span>{{ item.subject }}</span>
        </h1>
        <section v-if="item.content">
            <div v-for="(content, idx) in item.content" :key="idx" 
                 v-html="content.content_wysiwyg"></div>
        </section>
    </template>

    <NuxtLink to="/ssg_list">戻る</NuxtLink>
</template>

<script lang="ts" setup>
const { topics_id } = useRoute().params;

// プリフェッチしたJSONファイルから該当データを検索
const { data: item } = await useAsyncData(`filteredList-${topics_id}`, async () => {
    const fullListJSON = await import('~/prefetch/data/all_rcms-api_1_example_list.json')
        .then((m) => m.default);
    
    // IDに一致するアイテムを検索
    return fullListJSON
        .map((item: any) => ({
            topics_id: item.topics_id,
            subject: item.subject,
            content: item.content
        }))
        .find((item) => `${item.topics_id}` === topics_id);
});

// アイテムが見つからない場合は404エラーを表示
if (!item) {
    throw createError({
        statusCode: 404,
        statusMessage: 'Not Found'
    });
}
</script>
```

### 6. SSGの実行

最後に、プリフェッチとSSGを実行します。

```bash
# データのプリフェッチを実行
npm run prefetch

# 静的サイトを生成
npm run generate
```

:::info
想定通りの静的ファイル生成が確認できたらYAMLファイルを調整してnpm run generate の前にnpm run prefetchを実行するステップを追加してください。(KurocoFrontでデプロイする場合)
:::

## メリットと注意点

### メリット

1. **APIコール削減**: 多数のページを生成する場合でも、APIコール回数を大幅に削減できます
2. **高速な表示**: 事前に生成されたHTMLとJSONを使用するため、ページ表示が高速です
3. **SEO対策**: 静的HTMLが生成されるため、検索エンジンのクローラーに適しています
4. **コスト削減**: APIコール回数の削減により、APIサービスの利用料金を削減できます

### 注意点

1. **データの鮮度**: プリフェッチしたデータは静的なため、最新の情報を反映するには定期的に再ビルドする必要があります
2. **ビルド時間**: データ量が多い場合、プリフェッチとビルドに時間がかかる場合があります
3. **動的コンテンツ**: ユーザー固有のデータなど、完全に動的なコンテンツには適していません

## まとめ

Nuxt 3のSSGでAPIコール回数を削減するには、**プリフェッチ方式**が効果的です。この方法を使うことで、多数のページを効率的に生成しながら、APIコール回数を最小限に抑えることができます。特に大規模なサイトや、APIコール回数に制限がある場合に有効な手法です。

## 関連ドキュメント
- [Nuxt.jsのSSGでページ内リンクされていないページを生成することはできますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-generate-pages-that-are-not-linked-in-the-page/)
- [コーポレートサンプルサイトをSSGにする](/ja/docs/tutorials/corporate-sample-site-to-ssg/)
- [Kuroco利用料の最適化](/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/)
- [SSGにしています。コンテンツ更新後すぐにフロントに反映させるにはどうしたらいいですか？](/ja/docs/faq/how-do-i-reflect-updated-ssg-contents-on-the-frontend/)


---

# GitHubサードパーティ製のアプリを利用して問題ないでしょうか？

> 元ページ: `faq/can-i-use-third-party-github-applications` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-third-party-github-applications/
> 概要: GitHubサードパーティーアプリを利用することは問題ございません。注意点として、利用元のアプリが削除や修正されることもあります。また、サードパーティ製のアプリの安全性などは弊社で確認はできませんので、公開されているソースコードをご確認ください。

GitHubサードパーティーアプリを利用することは問題ございません。  
注意点として、利用元のアプリが削除や修正されることもあります。また、サードパーティ製のアプリの安全性などは弊社で確認はできませんので、公開されているソースコードをご確認ください。  

[GitHub Marketplace](https://github.com/marketplace?type=actions)でVerified creatorとなっているユーザーが作成したものをお勧めいたします。  

また、不意にアプリが削除や修正されることもあります。その場合に動作不良を起こす可能性も考慮すると、以下の対策もご検討ください。
- バージョン指定をして実行する
- ご自身のリポジトリ側にforkする
- プライベートアクションを作成する

## 関連ドキュメント
- [GitHub](/ja/docs/management/github/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [GitHub Actionsワークフローのアクションを最新バージョンに保つ方法はありますか？](/ja/docs/faq/how-to-keep-github-actions-up-to-date/)
- [Diverta管理のGitHubリポジトリを使用することは可能ですか？](/ja/docs/faq/is-it-possible-to-use-a-diverta-managed-github-repository/)


---

# 静的ファイルをジェネレートしたい場合、Kurocoのインフラとは別のサーバーは必要になりますか？

> 元ページ: `faq/do-i-need-a-production-server-separate-from-kurocos-infrastructure-to-generate-static-files` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/do-i-need-a-production-server-separate-from-kurocos-infrastructure-to-generate-static-files/
> 概要: KurocoFrontという、CDNを利用した静的コンテンツホスティングサービスを用意しております。そのため、KurocoFrontを利用することで、静的ファイルもKurocoで配信可能です。

Kurocoでは、**KurocoFront**というCDNを利用した静的コンテンツホスティングサービスを用意しております。KurocoFrontを利用することで、静的ファイルもKurocoで配信可能です。

KurocoFrontについては下記ドキュメントをご参照ください。
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- チュートリアル -> [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)

KurocoFrontはGitHub Actionsを利用する前提になっており、ビルドもGitHub Actionsを利用いただくことになります。

## その他、フロントエンド側のサーバーについて
静的ファイルは別サーバーに配置したいという場合は、[Netlify](https://www.netlify.com/)、[Amplify](https://aws.amazon.com/jp/amplify/)、[Firebase Hosting](https://firebase.google.com/docs/hosting?hl=ja)などのサービスから、一般的なレンタルサーバーまで、ご利用いただくものに特に制限はございません。

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [Kuroco Frontを使わずに自身のサーバーでサイトの表示をできますか？](/ja/docs/faq/can-i-display-the-site-on-my-own-server-without-using-kuroco-front/)
- [KurocoFrontの利用に制限事項はありますか](/ja/docs/faq/are-there-any-restrictions-on-using-kurocofront/)


---

# コンテンツ更新以外の任意のタイミングでGitHubActionsを使ったdeployを行うには？

> 元ページ: `faq/how-can-i-deploy-with-githubactions-at-any-time` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-deploy-with-githubactions-at-any-time/
> 概要: 任意のタイミングでdeployを行いたい場合は、カスタム処理やバッチで{github_deploy result_var='res'}の記述を実行するとGitHubActionsを実行できます。

[コンテンツ編集](/ja/docs/management/content-structure-topics/)で、  
`GitHub` > `Workflow` > `連携する`  
を選択してGitHubActionsを利用したdeployを行うのではなく任意のタイミングで  
deployを行いたい場合は、GitHubActionsを実行するSmartyプラグインを利用するか、管理画面の[Run Deployment]ボタンをクリックします。

## Smartyプラグインを利用する方法

[カスタム処理](/ja/docs/management/function/)や[バッチ](/ja/docs/management/batch/)で下記の記述をするとGitHubActionsを実行できます。

```
{github_deploy result_var='res'}
```

### 使用例
- バッチ処理で定期的にdeployを行う
- API経由で処理が行われた場合にPost-processでdeployを行う
- トリガーを利用して管理画面の特定の動作時にdeployを行う
- カスタム処理と紐づいたAPIエンドポイントを作成し、ダッシュボードのウィジェットでdeployボタンを作成する

## Run Deploymentボタン

[外部システム連携] -> [[GitHub](/ja/docs/management/github/)]のページで、[Run Deployment]ボタンをクリックするとGitHubActionsを実行できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/54762eda572d0c886303d9e383de125c.png)

## 関連ドキュメント
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [前処理](/ja/docs/reference/pre-processing/)
- [後処理](/ja/docs/reference/post-processing/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)


---

# 画像のURL末尾にパラメータを付与してもキャッシュがクリアされません。画像のキャッシュクリアの方法を教えて下さい。

> 元ページ: `faq/how-do-i-clear-cached-images` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-clear-cached-images/
> 概要: KurocoFilesは、画像ファイルに特定のQueryStringを追加することで画像を動的に変換する機能をもっています。そのため、URL末尾にキャッシュクリアを目的としたパラメータを付与してもキャッシュクリアはされません。

KurocoFilesは、画像ファイルに特定のQueryStringを追加することで画像を動的に変換する機能([画像の動的変換について](/ja/docs/reference/api-convert-image/))をもっています。  
そのため、URL末尾にキャッシュクリアを目的としたパラメータを付与してもキャッシュクリアはされません。

キャッシュクリアをしたい場合、画像URLの1階層目に`v=[数字10桁]`が表記されますので、こちらを利用してキャッシュのコントロールが可能です。  

参考：キャッシュコントロールの記述例  
`https://example.kuroco-img.app/v=1234567890/files/topics/example.png`

APIでKurocoFilesのパスをレスポンスする場合には、自動的にフォルダの1階層目にこのパラメータを付与するようになっておりますので、APIのレスポンスの場合はそちらをそのままご利用ください。  

:::info
キャッシュのクリアについては、下記も併せてご確認ください。  
FAQ -> [KurocoFilesのキャッシュはいつクリアされますか？](/ja/docs/faq/when-are-cached-kurocofiles-cleared/)
:::

## 関連ドキュメント
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [APIキャッシュクリアのタイミングと範囲](/ja/docs/reference/cache-clear-operation/)
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)
- [KurocoFilesのキャッシュはいつクリアされますか？](/ja/docs/faq/when-are-cached-kurocofiles-cleared/)


---

# SSGにしています。コンテンツ更新後すぐにフロントに反映させるにはどうしたらいいですか？

> 元ページ: `faq/how-do-i-reflect-updated-ssg-contents-on-the-frontend` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-reflect-updated-ssg-contents-on-the-frontend/
> 概要: 記事編集画面のGitHubの項目のWorkflow で、「連携する」を選択してコンテンツを更新してください。連携したGitHubでGitHub actionsが実行され、フロントに反映されます。

[記事編集画面のGitHubの項目](/ja/docs/management/content-structure-topics/#github)のGithub Actions ワークフローで、「有効」を選択してコンテンツを更新してください。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/63868cbb53adf046b7981f99c970c91d.png)
連携したGitHubでGitHub actionsが実行され、フロントに反映されます。

GitHub actionsが実行される対象のブランチは[GitHub](/ja/docs/management/github/)のページで連携対象として選択したブランチになります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b55e50c68d2022478e8b270a8016a8f9.png)

## 関連ドキュメント
- [GitHub](/ja/docs/management/github/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [コンテンツの更新時にGitHub Actionsを自動実行する](/ja/docs/tutorials/auto-run-github-with-contents-update/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [コンテンツ更新以外の任意のタイミングでGitHubActionsを使ったdeployを行うには？](/ja/docs/faq/how-can-i-deploy-with-githubactions-at-any-time/)


---

# Nuxt.jsでGoogleAnalytics4(GA4)をどのように設定すればいいですか？

> 元ページ: `faq/how-do-i-set-up-google-analytics-4-in-nuxtjs` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-set-up-google-analytics-4-in-nuxtjs/
> 概要: nuxtjs/google-gtagやnuxtjs/gtmを使う方法があります。詳しくはGoogle Analytics連携方法のドキュメントを参照してください。

`@nuxtjs/google-gtag`を利用します。

## @nuxtjs/google-gtagを利用する方法
### @nuxtjs/google-gtagをインストールする
プロジェクトにGoogle Analytics用のモジュール `@nuxtjs/google-gtag` をインストールします。  
下記実行します。

```
npm install --save @nuxtjs/google-gtag
```

### nuxt.config.jsにモジュール追加
nuxt.config.jsにGoogle Analyticsの設定をします。  
nuxt.config.jsを開き、下記追記します。

```js title="nuxt.config.js"
  modules: [
    '@nuxtjs/google-gtag'
  ],
  'google-gtag': {
    id: "G-XXXXXXX",
    debug: false
  },
```

:::caution
G-XXXXXXXには、ご自身のトラッキング IDを入力してください。
:::

## 参考

他にも、`@nuxtjs/gtm`を使う方法でも対応可能です。  
詳しくは[Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)のドキュメントを参照してください。

## 関連ドキュメント
- [Google Analytics](/ja/docs/management/google-analytics/)
- [Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)
- [GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法](/ja/docs/tutorials/how-to-implement-ranking-with-google-analytics/)
- [効果測定タグ(コンバージョンタグ)は利用できますか？](/ja/docs/faq/can-i-use-conversion-tracking-tags/)


---

# CDNにキャッシュされたレスポンスかどうかの確認方法を教えてください

> 元ページ: `faq/how-do-i-verify-responses-in-the-cdn-cache` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-verify-responses-in-the-cdn-cache/
> 概要: HARファイルやDeveloper toolsでHTTPレスポンスを確認します。

HARファイルやDeveloper toolsでHTTPレスポンスを確認します。  
以下のように「age」に表示されている数字が、キャッシュされてからの秒数です。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fd6cd7c98dfbf404bba79736745639cb.png)
### 例
上記キャプチャのように age が `63696` の場合は「17時間31分36秒前にキャッシュされたレスポンス」となります。

:::info
HARファイルの生成方法は下記リンクをご参照ください。  
[HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
:::

## 関連ドキュメント
- [APIのキャッシュについて](/ja/docs/reference/api-cache/)
- [APIキャッシュクリアのタイミングと範囲](/ja/docs/reference/cache-clear-operation/)
- [HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
- [KurocoFilesのキャッシュはいつクリアされますか？](/ja/docs/faq/when-are-cached-kurocofiles-cleared/)


---

# KurocoFrontでどのハッシュが利用されているかの確認方法を教えてください

> 元ページ: `faq/how-do-i-verify-the-hash-responses-used-by-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-verify-the-hash-responses-used-by-kurocofront/
> 概要: HARファイルやDeveloper toolsでHTTPレスポンスを確認します。

HARファイルやDeveloper toolsでHTTPレスポンスを確認します。  
KurocoFrontでは、レスポンスヘッダーにデプロイ情報が含まれています。

### レスポンスヘッダー一覧

| ヘッダー名 | 説明 |
| --- | --- |
| x-rcms-hash | GitHubのコミットハッシュ |
| x-rcms-deploy | Kurocoのデプロイごとに付与されるハッシュ |
| x-rcms-domain | KurocoFrontのドメイン名 |

以下のように「x-rcms-hash」に表示されている文字列が、利用されているハッシュの最初の7文字です。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5f87738a9fd9b0bfa2999ec8b88ef4d4.png)
### 例
`x-rcms-hash` が 51632bf の場合は、GitHubで51632bfのハッシュ値を探してみてください。表示されているページはそのコミットを利用したものになっています。

`x-rcms-deploy` の値はKurocoのデプロイごとに付与されるハッシュです。この値が変わっている場合、新しいデプロイが反映されていることを確認できます。

:::info
HARファイルの生成方法は下記リンクをご参照ください。  
[HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
:::

## 関連ドキュメント
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)
- [HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)


---

# カスタムディメンションで設定されている数値の集計結果を確認する方法はありますか？

> 元ページ: `faq/how-to-generate-reports-using-custom-dimensions` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-generate-reports-using-custom-dimensions/
> 概要: GoogleAnalyticsのレポート画面のセカンダリディメンションで、カスタムディメンションを選択することで集計結果にカスタムディメンションの値を利用できます。

GoogleAnalyticsのレポート画面のセカンダリディメンションで、カスタムディメンションを選択することで集計結果にカスタムディメンションの値を利用できます。  

また、下記のようにカスタムレポートを利用することで、個別の記事のIDなどで絞り込んだレポートも作成可能です。

「新しいカスタムレポート」をクリックすると作成画面に遷移します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8a22921edfc30eabcf066cdd7ce00f68.png)
フィルタで絞り込むことができます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/062953db410a34db17fb54a5c398c4ea.png)
:::caution
Google側の仕様変更により、実際の画面とキャプチャの見た目が違う場合もあります。
:::

## 関連ドキュメント
- [Google Analytics](/ja/docs/management/google-analytics/)
- [Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)
- [GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法](/ja/docs/tutorials/how-to-implement-ranking-with-google-analytics/)
- [Nuxt.jsでGoogleAnalytics4(GA4)をどのように設定すればいいですか？](/ja/docs/faq/how-do-i-set-up-google-analytics-4-in-nuxtjs/)


---

# サイト内で利用している静的ファイル（画像、JS、CSSなど）はどこに配置するのが良いでしょうか？

> 元ページ: `faq/how-to-place-static-files` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-place-static-files/
> 概要: Kurocoでサイト運用をする場合、静的ファイルの配置場所としてKurocoFrontとKurocoFilesの2つが存在します。それぞれの利用用途、メリットデメリットについて説明します。

Kurocoでサイト運用をする場合、静的ファイルの配置場所として下記2つが存在します。
- ソースファイル内に配置する(例：Nuxt.jsの場合はstaticディレクトリ)
- KurocoFilesに配置する

それぞれのおすすめの利用用途ついて説明します。

## ソースファイル内に配置をおすすめする場合
- サイトのデザインに利用しているファイル（画像、CSS、JSなど）

## KurocoFilesをおすすめする場合
- 運用で利用するような更新頻度の高いファイル
- ファイルサイズが大きい場合(例：画像だけで30MBを超える)

### KurocoFiles利用のメリット
ファイルサイズの大きいファイルをKurocoFilesに配置することでソースファイル全体のファイルサイズを削減できます。  
ソースファイルのサイズが少なくなると、GitHub ActionsでのBuild&Deployの時間が短縮されます。  

### KurocoFiles利用のデメリット
デメリットとして、KurocoFilesにバージョン管理の機能はないため、CSSやJSをKurocoFilesにアップする場合、それらのファイルはバージョン管理できなくなってしまいます。  

:::tip
より詳細な使い分け方法については、[画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)も併せてご確認ください。
:::

:::info
KurocoFront、KurocoFilesについては下記ドキュメントをご確認ください。  
-[KurocoFrontについて](/ja/docs/about/kurocofront/)  
-[ファイルマネージャー](/ja/docs/management/file-manager/)
:::

## 関連ドキュメント
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [KurocoFilesディレクトリとドメインの使い分けについて](/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [GitHub Actionsのビルド&デプロイに時間がかかってしまいます。解決方法はありますか？](/ja/docs/faq/how-to-reduce-artifact-file-sizes/)


---

# デプロイしたサイトの表示を404に戻すことはできますか？

> 元ページ: `faq/is-it-possible-to-revert-the-deployed-site-to-display-a-404-error` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-revert-the-deployed-site-to-display-a-404-error/
> 概要: index.html やその他の実際のHTMLファイルを配置せず、kuroco_front.json のみが存在する構成でファイルをデプロイすると404の表示にできます。

index.html やその他の実際のHTMLファイルを配置せず、kuroco_front.json のみが存在する構成でファイルをデプロイすると404の表示にできます。

## 対応例

例えば、以下のような状態のZIPファイルを作成します。

```
my_project.zip
└── kuroco_front.json
```

このZIPファイルをKurocoFiles等に設置して、「[GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)」を参考にCurlでデプロイリクエストを送信します。


## 関連ドキュメント
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)


---

# ページをリロードしたり、URLに直接アクセスすると 404 Not Found になります。

> 元ページ: `faq/reloading-the-page-or-accessing-it-directly-will-result-in-404-not-found` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/reloading-the-page-or-accessing-it-directly-will-result-in-404-not-found/
> 概要: SPAの構成の場合、動的に作成したページをリロードしたりURLに直接アクセスすると、index.htmlのファイルが見つからないため404 Not Found になります。「SSGの構成にする」「URLリライトを設定する」のいずれかで解消できます。

SPAの構成の場合、動的に作成したページをリロードしたりURLに直接アクセスすると、index.htmlのファイルが見つからないため404 Not Found になります。  
下記いずれかの方法で解消できますのでお試しください。  

## SSGの構成にする
SSGの構成で利用する場合、サーバー側であらかじめコンテンツを生成するため、本事象は発生しません。 
Nuxt.jsの場合は`nuxt.config.js`で`ssr: true,`を設定ください。

SPAとSSGの違いについては[Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)を参照ください。  

## URLリライトを設定する
SPAの構成で利用する場合は、KurocoFrontでURLリライトの設定をしてください。
`Kuroco_front.js`に下記の記述を設定すると解消されます。

```js [Kuroco_front.js]
    "rewrites": [
        {
          "source": ".*",
          "destination": "/index.html"
        }
    ],
```

Kuroco_front.js の詳細については[kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)を参照ください。  

## 関連ドキュメント
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)
- [コーポレートサンプルサイトをSSGにする](/ja/docs/tutorials/corporate-sample-site-to-ssg/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# 独自ドメインを設定しましたがサイトが表示できません。何を確認すれば良いでしょうか？

> 元ページ: `faq/setting-up-a-custom-domain` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/setting-up-a-custom-domain/
> 概要: 独自ドメインを設定したにもかかわらず、サイトが表示できない/エラーとなる場合は下記をご確認ください。

独自ドメインを設定したにもかかわらず、サイトが表示できない/エラーとなる場合は下記をご確認ください。

## 独自ドメイン/TLS証明書の確認
独自ドメインが適切に設定されているかの確認をお願いします。  
[KurocoFront] -> [独自ドメイン/TLS証明書]より、独自ドメインが「OK」になっているか確認してください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fe59452282070580f70635b1e126de7b.png)
こちらが「認証中」になっている場合は、うまく設定ができていない可能性がございます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f4e81deaae4dd964e6c95d364596929b.png)
その場合、[KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)を参考に設定をお願いします。

## GitHub連携の確認
GitHubとの連携がうまくできているかの確認をお願いします。  
[外部システム連携] -> [GitHub]より下記2点をご確認ください。

- リポジトリ：対象のリポジトリが選択されているか
- GitHubの連携対象：対象ブランチが選択されているか

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/7eaa310c8459d6bfc0daeae2ce70d3cb.png)
GitHubとの連携ができていない場合は [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)を参考に連携してください。

## kuroco_front.jsonが作成されているかの確認
KurocoFrontを利用するためには、Kuroco_front.jsonファイルを適切な場所に配置する必要があります。Kuroco_front.jsonが作成されているかをご確認ください。

Kuroco_front.jsonについては、[kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)を参考にしてください。

## .github/workflows 配下のYAMLファイル内容確認
KurocoFrontにてビルドするために、.github/workslows ディレクトリ配下にYAMLファイルを作成する必要があります。  
YAMLファイルの内容は、[外部システム連携] -> [GitHub]ページの[リポジトリ] -> [GitHub Actions workflow file フロントエンド ドメイン]に表示されている内容を記載してください。  
YAMLファイル内に独自ドメインなども記載されていますので、リポジトリのコピーやドメインの変更をされている場合などはそちらもご確認ください。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/4342bb0927ec2710b5d6ccab27e961ff.png)
.github/workflows 配下のYAMLファイルについては、[GitHubからKurocoFrontへソースをデプロイする方法 デプロイ手順](/ja/docs/tutorials/connect-to-github-with-kuroco-front/#デプロイ手順)の「4. .github/workflows にYAMLファイルを配置する」をご参考にしてください。

## 上記で解決しない場合
上記の対応方法で解決しない場合は [お問い合わせフォーム](https://kuroco.zendesk.com/hc/ja)よりお問い合わせください。

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [GitHub](/ja/docs/management/github/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [独自ドメインの変更方法を教えてください。](/ja/docs/faq/how-do-i-change-my-domain-name/)


---

# kuroco_front.jsonとは何ですか？

> 元ページ: `faq/what-is-kuroco_front_json` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-kuroco_front_json/
> 概要: kuroco_front.jsonとは、KurocoFrontoを利用するために必要なJSONファイルです。Kuroco_front.jsonを利用することで、リダイレクト設定やBasic認証設定、エラーページの設定が可能となります。

kuroco_front.jsonとは、KurocoFrontを利用するために必要なJSONファイルです。  
Kuroco_front.jsonを利用することで、リダイレクト設定やBasic認証設定、エラーページの設定が可能となります。

## 配置場所

KurocoFrontを利用する際は、ビルド後の出力ディレクトリのルート(公開ディレクトリの直下)にkuroco_front.jsonを配置してください。ただし、このファイルは公開されません。

:::tip
例えば、Nuxt.jsやNext.jsの場合は以下のディレクトリに配置します。  
Nuxt2:`/static`  
Nuxt3:`/public`  
Next.js:`/public`  
:::

## 設定できるキー一覧

kuroco_front.jsonで設定できるキーは以下の8個です。

|キー|説明|
|:-------|:-------|
|`rewrites`|URLリライトの設定|
|`redirects`|リダイレクトの設定|
|`redirects_by_ie`|IEでのアクセス時にリダイレクト|
|`basic`|Basic認証|
|`ip_restrictions`|IPアドレス制限|
|`ip_restricted_maintenance`|IPアドレス制限付きメンテナンスページ|
|`error_page`|エラーページの設定|
|`stale_while_revalidate`|キャッシュが更新されるまでCDNから期限切れのコンテンツを配信する期限|

:::caution
上記以外のキーを記述してもエラーにはならず、無視されます。他のホスティングサービスの設定キーやキー名のタイポは動作しないため注意してください。  
また、値の型が想定と異なる場合（例：`stale_while_revalidate`をJSONの数値で記述した場合）も、その設定は無視されます。
:::

## サンプルコード

```json [kuroco_front.json]
{
    "rewrites": [
        {
          "source": ".*",
          "destination": "/index.html"
        }
    ],
    "redirects": [
        {
          "source": "^/old_path/",
          "destination": "/new_path/"
        },
        {
          "source": "^/old_articles/([^/]+?)/",
          "destination": "/new_articles/$1/"
        },
        {
          "source": "^/old_articles2/([^/]+?)/",
          "destination": "status:404"
        },
        {
          "source": "^/articles2/([^/]+?)/",
          "destination": "status:302:/temp_articles2/$1/"
        }
    ],
    "redirects_by_ie": [
        {
          "source": ".*",
          "destination": "/ie/"
        }
    ],
    "basic":[
        "user:pass",
        "user2:pass2"
    ],
    "ip_restrictions":[
        "111.111.111.111/32",
        "222.222.222.222/32"
    ],
    "ip_restricted_maintenance":[
        "111.111.111.111/32",
        "222.222.222.222/32"
    ],
    "stale_while_revalidate":"86400",
    "error_page": {
        "status404":"/404.html",
        "status401":"/401.html",
        "status_ip_503":"/ip_503.html"
    }
}

```
## kuroco_front.jsonの役割
上記サンプルコードの役割を詳しく解説します。

### rewrites：URLリライトの設定
```json
"rewrites": [
        {
          "source": ".*",
          "destination": "/index.html"
        }
    ],
```

|項目|説明|設定例|
|:-------|:-------|:-------|
|source|URLリライト対象URIを正規表現で記述します。|.*|
|destination|リライト先を記述します。 |/index.html|

".*"の時のみ、ファイルの存在がない場合有効になります。  
複数設定可能です。  
上から順番にチェックをします。  

### redirects：リダイレクトの設定
```json
"redirects": [
        {
          "source": "/old_path/",
          "destination": "/new_path/"
        }
    ],
```

|項目|説明|設定例|
|:-------|:-------|:-------|
|source|リダイレクト対象URIを正規表現で記述します。`()`でキャプチャグループを指定できます。|^/old_articles/([^/]+?)/|
|destination|リダイレクト先を記述します。`$1`などでsourceのキャプチャグループを参照できます。何も指定しない場合は301リダイレクトになります。status:302:を先頭にセットすると302リダイレクトになります。status:404をセットすると404エラーになる特別な挙動が設定可能です。 |/new_articles/$1/|
 
".*"の時のみ、ファイルの存在がしない時のみ動作する挙動になります。  
複数設定可能です。  
上から順番にチェックをします。  
リダイレクト時はQueryStringを保持してリダイレクトします。destinationにもQueryStringは指定できますが、sourceの指定にQueryStringは利用できません。  

#### キャプチャグループの利用

sourceの正規表現に`()`で指定したキャプチャグループは、destinationで`$1`、`$2`…の順に参照できます。リダイレクト元URLの一部をリダイレクト先に引き継ぎたい場合に利用します。

```json
"redirects": [
    {
        "source": "^/old_articles/([^/]+?)/",
        "destination": "/new_articles/$1/"
    }
],
```

上記の場合、アクセスされたURLに応じて次のようにリダイレクトされます。

|アクセスされたURL|リダイレクト先|
|:-------|:-------|
|/old_articles/123/|/new_articles/123/|
|/old_articles/abc/|/new_articles/abc/|

`()`は複数指定でき、左から順に`$1`、`$2`…に対応します。  

### redirects_by_ie：IEでのアクセス時にリダイレクト
```json
"redirects_by_ie": [
    {
        "source": ".*",
        "destination": "/ie/"
    }
],
```

|項目|説明|設定例|
|:-------|:-------|:-------|
|source|リダイレクト対象URIを正規表現で記述します。|.*|
|destination|リダイレクト先を記述します。 |/ie/|

UserAgentにMSIEかTridentが文字列として含まれている場合のみ有効になるリダイレクトです。ファイルの存在確認はしません。  
複数設定可能です。
上から順番にチェックをします。  

### basic：Basic認証
```json
"basic":[
    "user:pass",
    "user2:pass2"
],
```

IDとパスワードのセットを:で結合してセットします。  
（上記の場合、「ID：user、パスワード：pass」または「ID：user2、パスワード：pass2」となります。） 

:::caution
プレーンにパスワードを記述しますので、扱いに気をつけてください。   
:::

複数設定可能です。


### ip_restrictions：IPアドレス制限
```json
"ip_restrictions":[
     "111.111.111.111/32",
     "222.222.222.222/32"
],
```

IPアドレスをセットします。スラッシュ表記でサブネットマスクも利用可能です。  
複数設定可能です。

### ip_restricted_maintenance：IPアドレス制限付きメンテナンスページ
```json
"ip_restricted_maintenance":[
     "111.111.111.111/32",
     "222.222.222.222/32"
],
```

特定のIPアドレス以外はメンテナンスページを表示します。  
IPアドレスをセットします。スラッシュ表記でサブネットマスクも利用可能です。  
複数設定可能です。

### stale_while_revalidate：キャッシュが更新されるまでCDNから期限切れのコンテンツを配信する期限
```json
"stale_while_revalidate":"86400",
```

Cache-Controlヘッダーにstale_while_revalidateを追加して、CDN側で失効済みコンテンツ配信を可能にします。  
`stale_while_revalidateに86400`をセットすると、CDNのキャッシュがクリアされてもコンテンツを1日間（86400秒）保持し、キャッシュクリア後1回目のアクセスでは失効済みコンテンツを配信します。  
この間にキャッシュの再作成することでキャッシュがない時のレスポンス遅延を防ぎます。  
HTTPレスポンスが200の時だけ有効になります。

:::caution
値は数字の文字列（`"86400"`）で記述します。JSONの数値（`86400`）で記述した場合は無視されます。
:::

### error_page：エラーページの設定
```json
"error_page": {
    "status404":"/404.html",
    "status401":"/401.html",
    "status_ip_503":"/ip_503.html"
},
```

|項目|説明|設定例|
|:-------|:-------|:-------|
|status404|404エラー時にレスポンスするHTMLファイルのパスを記述します。|/404.html|
|status403|403エラー時にレスポンスするHTMLファイルのパスを記述します。|/403.html|
|status401|401エラー時にレスポンスするHTMLファイルのパスを記述します。|/401.html|
|status_ip_503|IPアドレス付きメンテナンスページ表示時にレスポンスするHTMLファイルのパスを記述します。|/ip_503.html|

パスは`/`始まり（デプロイルートからの絶対パス）で記述します。`/`始まりでないパスは無視されます。

## 補足
- kuroco_front.jsonが見つからない、JSON形式が間違っていると「404 Not Found (CONFIG FILE NOT FOUND)」になります。
- IPアドレス制限での認証に失敗すると、「403 Forbidden」、またはerror_pageでセットした内容となります。  
- 閲覧制限はKurocoのID・PWDでの認証になるため、認証に失敗すると、「Authentication required」、またはerror_pageでセットした内容となります。
- 同一リポジトリ内でブランチ毎にkuroco_front.jsonの内容を切り替えたい場合はGitHubActionsのビルドファイルで切り替えることが出来ます。  
具体的な運用ケースとしては開発環境のみBasic認証を設定したい場合に利用出来ます。  

実際の設定例は[GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/#githubactions%E7%94%A8build%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E4%BF%AE%E6%AD%A3)を参照してください。

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [ページをリロードしたり、URLに直接アクセスすると 404 Not Found になります。](/ja/docs/faq/reloading-the-page-or-accessing-it-directly-will-result-in-404-not-found/)
- [Basic認証は利用できますか？](/ja/docs/faq/can-i-use-basic-authentication/)
- [特定のIPアドレス以外はメンテナンスページを表示したいです](/ja/docs/faq/how-to-display-maintenance-page-except-for-specific-ip-addresses/)


---

# KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？

> 元ページ: `faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/
> 概要: KurocoFrontへのファイルの反映は、基本的にGitHub Actionsを利用します。KurocoFrontへのファイルの反映がされない理由として、主に想定されるパターンは以下になります。

KurocoFrontへのファイルの反映は、基本的にGitHub Actionsを利用します。 

:::info
まだデプロイの作業を実施していない場合は[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)を参考にデプロイをしてください。  
:::

KurocoFrontへのファイルの反映がされない理由として、主に想定されるパターンは以下になります。  

- [GitHub Actionsでの.github/workflows配下のYAMLファイルの記述が間違っている](#github-actionsでのgithubworkflows配下のyamlファイルの記述が間違っている場合)
- [公開ディレクトリのルートにkuroco_front.jsonが存在しない](#公開ディレクトリのルートにkuroco_frontjsonが存在しない場合)
- [GitHub Actionsでのビルドに失敗している](#github-actionsでのビルドに失敗している場合)
- [GitHub Actionsでのビルドやデプロイプロセスで時間がかかっている](#github-actionsでのビルドやkurocofrontへのデプロイプロセスで時間がかかっている場合)
- [デプロイするファイルが重くて、デプロイする処理でエラーになっている](#デプロイするファイルが重くて、デプロイする処理でエラーになっている)
- [CDNのキャッシュが正常にクリアされていない](#cdnのキャッシュが正常にクリアされていない)

## GitHub Actionsでの.github/workflows配下のYAMLファイルの記述が間違っている場合
[GitHub](/ja/docs/management/github/)のページにある.github/workflows配下のYAMLファイルのサンプルの内容と現在の設定の比較・確認をしてください。  

## 公開ディレクトリのルートにkuroco_front.jsonが存在しない場合
[kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)を参考に公開ディレクトリのルートにkuroco_front.jsonを設置してください。  
リポジトリのルートではなく、distなどの出力フォルダのルートに配置されるように設定をしてください。

実際に公開ディレクトリのルートにkuroco_front.jsonがあるかはGitHub ActionsのArtifactsのZipファイルをダウンロードして解凍してご確認いただくことができます。  

## GitHub Actionsでのビルドに失敗している場合
GitHub Actionsの実行ログを確認して、問題点を発見してください。  
ビルド後の成果物をArtifactsのところからダウンロードして確認していただいて、想定されたビルド成果物かどうかのチェックもお願いいたします。  

:::info
GitHub Actionsの実行ログの確認方法は、[GitHub docs -> ワークフロー実行ログを使用する](https://docs.github.com/ja/actions/managing-workflow-runs/using-workflow-run-logs)をご確認ください。
:::

## GitHub ActionsでのビルドやKurocoFrontへのデプロイプロセスで時間がかかっている場合
GitHub Actionsの実行履歴からGitHub Actionsの実行時間を確認してください。KurocoFrontへのデプロイプロセスはArtifactsのサイズによりますが、30秒〜数分程度が想定されます。  

:::info
GitHub Actionsの実行履歴は、[GitHub docs -> ワークフロー実行の履歴を表示する](https://docs.github.com/ja/actions/managing-workflow-runs/viewing-workflow-run-history)をご確認ください。
:::

## デプロイするファイルが重くて、デプロイする処理でエラーになっている
KurocoFrontへのデプロイプロセスではGitHub ActionsのArtifactsを利用しています。  
300MBを超えるArtifactsだとGitHubからのダウンロードスピードの関係でエラーになる場合があります。
現在は、エラーログ等で確認できるようになっておりません。  

GitHub Actionsのプロセス終了後10分以内にデプロイが確認できない場合、Artifactsのダウンロードに失敗している可能性が高いです。
`Re-run jobs`で再実行してください。   

:::info
[GitHub docs -> ワークフローの成果物をダウンロードする](https://docs.github.com/ja/actions/managing-workflow-runs/downloading-workflow-artifacts)
:::

## CDNのキャッシュが正常にクリアされていない
KurocoFrontで利用しているコミットハッシュを確認できますので、どのコミットハッシュのArtifactsがデプロイされているか確認をお願いします。

:::info
[KurocoFrontでどのハッシュが利用されているかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-the-hash-responses-used-by-kurocofront/)
:::

:::info
[CDNにキャッシュされたレスポンスかどうかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-responses-in-the-cdn-cache/)
:::

## 関連ドキュメント
- [GitHub](/ja/docs/management/github/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [KurocoFrontでどのハッシュが利用されているかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-the-hash-responses-used-by-kurocofront/)
- [CDNにキャッシュされたレスポンスかどうかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-responses-in-the-cdn-cache/)
- [GitHub Actionsのビルド&デプロイに時間がかかってしまいます。解決方法はありますか？](/ja/docs/faq/how-to-reduce-artifact-file-sizes/)


---

# 画像を印刷できないときの対処方法を教えてください

> 元ページ: `faq/what-should-i-do-if-i-cant-print-an-image` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-should-i-do-if-i-cant-print-an-image/
> 概要: 画像にメタデータが残っていると印刷できないことがあります。メタデータを除いた画像をセットしてから、再度印刷をお試しください。

画像にメタデータが残っていると印刷できないことがあります。  
メタデータを除いた画像をセットしてから、再度印刷をお試しください。  
なお、メタデータが付与される・されないは、撮影機器などで異なる可能性がありますのでご注意ください。

## Adobe PhotoShopでメタデータを除く方法
### 手順
1. Photoshopで画像を開く
2. メニューで[ファイル] -> [書き出し] -> [Web用に保存]を選択する
3. メタデータを「なし」にして保存する

### 注意点
- PhotoShop側の仕様変更で、手順や方法が異なる場合あります。
- その他の画像編集ソフトでの操作方法は、Googleなどの検索エンジンでお調べください。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [特定のブラウザで画像が表示されないときの対処方法を教えてください](/ja/docs/faq/what-should-i-do-if-images-are-not-displayed-in-certain-browsers/)


---

# 特定のブラウザで画像が表示されないときの対処方法を教えてください

> 元ページ: `faq/what-should-i-do-if-images-are-not-displayed-in-certain-browsers` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-should-i-do-if-images-are-not-displayed-in-certain-browsers/
> 概要: デスクトップやウィンドウ画面で拡張子を書き換えただけの画像は、ブラウザで表示されない場合があります。画像の拡張子が正しいか、変更している場合は正しく変更できているかをご確認ください。

デスクトップやウィンドウ画面で拡張子を書き換えただけの画像は、ブラウザで表示されない場合があります。  
画像の拡張子が正しいか、変更している場合は正しく変更できているかをご確認ください。  

正しく拡張子を変更していても表示されない場合は、お調べしますので、下記２点を添えて[問い合わせフォーム](https://kuroco.zendesk.com/hc/ja)からお問い合わせください。

- 表示される想定の画面URL
- 対象の画像

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [ファイルマネージャーで利用できるファイルの種類](/ja/docs/reference/what-file-formats-does-the-file-manager-support/)
- [画像を印刷できないときの対処方法を教えてください](/ja/docs/faq/what-should-i-do-if-i-cant-print-an-image/)
- [画像のURL末尾にパラメータを付与してもキャッシュがクリアされません。画像のキャッシュクリアの方法を教えて下さい。](/ja/docs/faq/how-do-i-clear-cached-images/)
