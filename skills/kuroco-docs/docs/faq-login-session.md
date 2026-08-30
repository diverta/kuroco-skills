# Kurocoドキュメント: FAQ / login-session

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- OAuthを使用したシングルサインオンはできますか（`can-I-use-single-sign-on-using-oauth`）
- SAML認証を使用したシングルサインオンを利用できますか（`can-I-use-single-sign-on-using-saml`）
- セッションの有効期限は変更できますか？（`can-i-change-the-session-timeout-duration`）
- ログインの有効期限を設定することはできますか（`can-i-set-a-login-expiration-date`）
- 静的アクセストークンの有効期限が切れる前に通知は届きますか？（`notification-before-static-access-token-expires`）
- オートログインの有効期間について教えてください（`what-is-the-validity-period-for-auto-logins`）


---

# OAuthを使用したシングルサインオンはできますか

> 元ページ: `faq/can-I-use-single-sign-on-using-oauth` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-I-use-single-sign-on-using-oauth/
> 概要: はい、KurocoはOAuthを使用したシングルサインオンの利用可能です。

はい、KurocoはOAuthを使用したシングルサインオンの利用可能です。

## 特徴

OAuth認証シングルサインオンの特徴は下記の通りです。

- シングルクリックログインとユーザー登録に対応しています。
- ユーザーアクセストークンの保存に対応します。
- 複数のSSOオプションを同時に有効にできます。
- SSOによる登録時のデフォルトのユーザー権限設定をサポートしています。
- コードを書くことなく、ユーザー情報を取得できます。
- SSOオプションを公開する前に、テストツールにて確認できます。
- GitHub、Facebook、Zoho、Microsoft、Chatwork、Atlassianなど、さまざまなサービスをサポートしています。


## サポート対象外

下記はサポート対象外となります。

- Identity Provider
- OAuth 2.0 JWT Profile.

:::tip
OAuthはシングルサインオンの一種です。SAMLの場合は[こちら](/ja/docs/faq/can-I-use-single-sign-on-using-saml/)を参照ください。
:::

## 関連ドキュメント
- [OAuth SP](/ja/docs/management/sso-oauth-sp/)
- [GitHubを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)
- [Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- [SSOによるログインをフロントエンドで利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)
- [SAML認証を使用したシングルサインオンを利用できますか](/ja/docs/faq/can-I-use-single-sign-on-using-saml/)


---

# SAML認証を使用したシングルサインオンを利用できますか

> 元ページ: `faq/can-I-use-single-sign-on-using-saml` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-I-use-single-sign-on-using-saml/
> 概要: はい、KurocoはSAML認証を使用したシングルサインオンを利用可能です。

はい、KurocoはSAML認証を使用したシングルサインオンを利用可能です。

## 特徴

SAML認証シングルサインオンの特徴は下記の通りです。

- ワンクリックでユーザー登録とログインができます。
- 設定ファイルを使って、簡単に設定・管理ができます。
- カスタム属性マッピング、ログイン状態フローなどの高度な設定をサポートします。
- Identity Providerとしてだけでなく、Service Providerとしても利用可能です。
- GoogleやSlackなど、多様なサードパーティサービスに対応しています。


## サポート対象外
下記はサポート対象外となります。
- ユーザーログアウトフロー
- ユーザー識別子管理プロトコル
- Identity Providerとして利用時のSAML 2.0 OASIS アサーション


:::info
SAMLはシングルサインオンの一種です。OAuthの場合は[こちら](/ja/docs/faq/can-I-use-single-sign-on-using-oauth/)を参照ください。
:::

## 関連ドキュメント
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [SAML IdP](/ja/docs/management/sso-saml-idp/)
- [Google Workspaceを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/)
- [Auth0を利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/)
- [GMOトラスト・ログインを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gmo-trust-login-to-implement-saml-based-sso/)
- [OAuthを使用したシングルサインオンはできますか](/ja/docs/faq/can-I-use-single-sign-on-using-oauth/)


---

# セッションの有効期限は変更できますか？

> 元ページ: `faq/can-i-change-the-session-timeout-duration` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-session-timeout-duration/
> 概要: 環境設定 -> 管理画面の「セッション有効期限」で変更できます。

[環境設定] -> [[管理画面](/ja/docs/management/management-screen/)]の「セッション有効期限」で変更できます。  


![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9f3f5b7f412f5c124a1dc0b0e64d77d5.png)
:::caution
「セッション有効期限」を変更すると、管理画面とAPIのセッション有効期限が同時に変更されますのでご注意ください。
:::

## 関連ドキュメント
- [管理画面](/ja/docs/management/management-screen/)
- [ログインの有効期限を設定することはできますか](/ja/docs/faq/can-i-set-a-login-expiration-date/)
- [オートログインの有効期間について教えてください](/ja/docs/faq/what-is-the-validity-period-for-auto-logins/)


---

# ログインの有効期限を設定することはできますか

> 元ページ: `faq/can-i-set-a-login-expiration-date` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-a-login-expiration-date/
> 概要: はい、可能です。メンバー毎にログインの有効期限を設定できます。

はい、可能です。メンバー毎にログインの有効期限を設定できます。

## ログインの有効期限設定方法
[メンバー管理] -> [メンバー]をクリックし、メンバー一覧画面を表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/702976f9920e36fdf69df964827b2cfa.png)

メンバー一覧画面より、有効期限を設定したいメンバーの名前をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b80331fd4aeca8b1d55a974210db1999.png)

クリックするとメンバー編集画面が表示されるので、[ID情報]タブの「ログイン許可の有効期限」より、メンバーにいつまでログインを許可するかの指定ができます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d83548244650f72421692a63d1e479b9.png)

「ログイン許可の有効期限」に「2021/03/31」と入力した場合、2021/04/01からはログインできなくなります。

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [期限付き一時メンバー](/ja/docs/management/temporary-member/)
- [ログインパスワードに有効期限を設定することはできますか？](/ja/docs/faq/can-i-set-an-expiration-date-for-login-passwords/)
- [セッションの有効期限は変更できますか？](/ja/docs/faq/can-i-change-the-session-timeout-duration/)
- [オートログインの有効期間について教えてください](/ja/docs/faq/what-is-the-validity-period-for-auto-logins/)


---

# 静的アクセストークンの有効期限が切れる前に通知は届きますか？

> 元ページ: `faq/notification-before-static-access-token-expires` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/notification-before-static-access-token-expires/
> 概要: はい。有効期限の30日前・7日前・1日前にあたる日に、アカウント設定に登録されたメールアドレス宛へ事前通知メールが届きます。

はい。届きます。

次のトークンについて、有効期限が近づくと、有効期限日の **30日前・7日前・1日前** にあたる日に、それぞれ1回ずつ事前通知メールが送信されます。

- [静的アクセストークン](/ja/docs/management/api-security/#静的アクセストークン)
- [特権付き静的トークン](/ja/docs/management/api-security/#特権付き静的トークン)
- [KurocoFrontのトークン](/ja/docs/management/kuroco-front-settings/)（KurocoにWebhookを送信してデプロイする際に使用するトークン）

対象となるのは、有効なAPIに設定されたトークンです。判定は有効期限の日付を基準に行われます。

## 通知先

通知メールは、[アカウント設定](/ja/docs/management/account/)に登録されている「メールアドレス」宛に送信されます。通知を受け取るには、アカウント設定にメールアドレスが登録されている必要があります。

## 有効期限が切れた場合

有効期限が切れると、該当トークンによるAPIアクセスができなくなります。通知を受け取ったら、必要に応じてトークンを再発行してください。静的アクセストークンは、流出時やフロントエンドに組み込む場合を想定し、トークンの更新（再発行）を前提としたシステム構成にすることが推奨されています。

## 関連ドキュメント

- [APIのセキュリティ設定 -> 静的アクセストークン](/ja/docs/management/api-security/#静的アクセストークン)
- [APIのセキュリティ設定 -> 特権付き静的トークン](/ja/docs/management/api-security/#特権付き静的トークン)
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [アカウント設定](/ja/docs/management/account/)
- [Smartyプラグイン -> api_token](/ja/docs/reference/smarty-plugin/#api_token)


---

# オートログインの有効期間について教えてください

> 元ページ: `faq/what-is-the-validity-period-for-auto-logins` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-the-validity-period-for-auto-logins/
> 概要: オートログインの有効期間は、ログイン画面で 「次回から自動的にログインする」にチェックがある状態でログインをした日時から計算されます。

オートログインの有効期間は、ログイン画面で **「次回から自動的にログインする」にチェックがある状態でログインをした日時** から計算されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/897f01229f82bf74a10521dafd8a1f67.png)
## オートログインの設定箇所
オートログインの期間は、管理画面より設定できます。

管理画面より、[環境設定]->[管理画面]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8971314fe7b7c03799a8a3052749a73c.png)

「オートログイン有効期間」にて有効期間を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2d925df9a7dc9c40363465d159f95bc.png)

## オートログインの注意事項
ご利用の際は下記ご注意ください。また、あくまでも便利機能としてご利用くださいますようお願いいたします。

- オートログインで再度ログインをした場合、有効期間は延長されません。  
- デバイスやブラウザ、環境の設定などによって挙動は左右されます。  
  オートログインの有効期限内に、ブラウザ側でCookieが削除されることもあります。そのため、何かの動作を保証するような利用方法は避けてご利用ください。
- 外部ドメインから遷移してきた場合には、ログイン画面を必ず挟みます。  
  CookieのSameSite属性がStrictになっているためです。

## 関連ドキュメント
- [管理画面](/ja/docs/management/management-screen/)
- [自動ログイントークン管理](/ja/docs/management/autologin-token-list/)
- [ログインの有効期限を設定することはできますか](/ja/docs/faq/can-i-set-a-login-expiration-date/)
- [セッションの有効期限は変更できますか？](/ja/docs/faq/can-i-change-the-session-timeout-duration/)
- [ログイン履歴の記録ロジックに関して教えてください](/ja/docs/faq/what-is-the-logic-behind-the-login-history/)
