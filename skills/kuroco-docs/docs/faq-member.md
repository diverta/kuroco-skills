# Kurocoドキュメント: FAQ / メンバー管理

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- profile APIの役割について（`about-profile-api`）
- ユーザーのIPアドレスを取得できますか？（`can-i-obtain-the-users-ip-address`）
- Basic認証は利用できますか？（`can-i-use-basic-authentication`）
- ステージサイトにだけBasic認証をかけられますか？（`can-i-use-basic-authentication-only-on-the-staging-site`）
- APIリクエスト制限の優先順位について教えてください（`in-what-order-are-viewing-restrictions-applied`）


---

# profile APIの役割について

> 元ページ: `faq/about-profile-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/about-profile-api/
> 概要: profile APIは会員制サイトでログインしているかどうかのチェックをするのに利用できるAPIとなっております

profile APIは会員制サイトでログインしているかどうかのチェックをするのに利用できるAPIとなっております。
全てのページでこのAPIをコールしていただいてご利用ください。
このため、会員制サイトを作成する場合には必須のAPIとなります。

また、ログインしている場合はログインユーザーの情報取得にもprofile APIが利用できます。

## 関連ドキュメント
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [アカウント情報の表示・更新・削除画面を構築する](/ja/docs/tutorials/setting-up-the-display-update-delete-screen-for-account-information/)
- [ログインユーザーの情報でAPIのレスポンスを動的に変更する](/ja/docs/tutorials/change-the-api-response-with-the-logged-in-users-information/)
- [会員制サンプルサイトを利用する](/ja/docs/tutorials/kuroco-sample-site/)


---

# ユーザーのIPアドレスを取得できますか？

> 元ページ: `faq/can-i-obtain-the-users-ip-address` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-obtain-the-users-ip-address/
> 概要: カスタム処理で{$smarty.server.REMOTE_ADDR}を使用し、エンドポイントに紐づけると、APIリクエストを送ったユーザーのIPアドレスが取得できます。

可能です。  
カスタム処理で`{$smarty.server.REMOTE_ADDR}`を使用し、エンドポイントに紐づけると、APIリクエストを送ったユーザーのIPアドレスが取得できます。

例えば、エンドポイントの[後処理](/ja/docs/reference/post-processing/)に設定して、レスポンスに`ip_address`の項目を追加するカスタム処理は以下になります。

```
{append var='json' value=$smarty.server.REMOTE_ADDR index='ip_address'}
{assign var='processed_json' value=$json}
```

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [APIにアクセス元の国や都道府県を追加する](/ja/docs/tutorials/how-to-add-region-data/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [後処理](/ja/docs/reference/post-processing/)
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)


---

# Basic認証は利用できますか？

> 元ページ: `faq/can-i-use-basic-authentication` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-basic-authentication/
> 概要: はい、Basic認証の利用可能です。kuroco_front.jsonファイルでBasic認証を設定します。

はい、Basic認証の利用可能です。kuroco_front.jsonファイルでBasic認証を設定します。

Basic認証を利用する場合、kuroco_front.jsonに下記を追記してください。

```json [kuroco_front.json]
{
    "basic":["kuroco:kuroco"],
}
```

フロント画面でサイトにアクセスすると、Basic認証がかかります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d97ce43675561ee728b757dde15043c2.png)

:::info
kuroco_front.json については、[kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)をご確認ください。
:::

なお、管理画面にはBasic認証の設定はできません。  
しかしながら、「管理画面のアクセス制限」機能をご利用いただくことで、IPアドレスにて管理画面のアクセス制御を行うことができます。

管理画面より[環境設定] -> [管理画面]に移動し、「管理画面のアクセス制限(IPアドレス)」フィールドにIPアドレスを記入してください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c5234bf12a75e2b2b96045b2f7ddc729.png)
:::info
管理画面については、[管理画面マニュアル] -> [[管理画面]](/ja/docs/management/management-screen/)をご確認ください。
:::

## 関連ドキュメント
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [ステージサイトにだけBasic認証をかけられますか？](/ja/docs/faq/can-i-use-basic-authentication-only-on-the-staging-site/)
- [管理画面](/ja/docs/management/management-screen/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# ステージサイトにだけBasic認証をかけられますか？

> 元ページ: `faq/can-i-use-basic-authentication-only-on-the-staging-site` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-basic-authentication-only-on-the-staging-site/
> 概要: ステージサイトにだけBasic認証をかける場合は、ステージサイト用のkuroco_front.jsonを作成し、"basic"項目に記載してください。

ステージサイトにだけBasic認証をかける場合は、ステージサイト用のkuroco_front.jsonを作成し、"basic"項目に記載してください。

```JSON [kuroco_front.json]
 "basic":[
        "user:pass"
 ],
```

- user：ユーザー名  
- pass：パスワード

ステージサイトにアクセスすると、Basic認証が求められます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b32d6297ab43b62ec31eea7b6c50e24f.png)
:::info
参考：[kuroco_front.jsonとは何ですか？ -> basic：Basic認証](/ja/docs/faq/what-is-kuroco_front_json/#basic：basic認証)
:::

ステージサイトの利用方法は下記のチュートリアルを参考にしてください。

:::info
参考：[独自ドメイン登録後、kuroco-front.appのドメインをフロントエンドのステージサイトとして利用する](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)
:::

## 関連ドキュメント
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [Basic認証は利用できますか？](/ja/docs/faq/can-i-use-basic-authentication/)
- [開発環境を作成する手順](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)


---

# APIリクエスト制限の優先順位について教えてください

> 元ページ: `faq/in-what-order-are-viewing-restrictions-applied` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/in-what-order-are-viewing-restrictions-applied/
> 概要: あるコンテンツ定義のコンテンツを返すAPIのレスポンス時にAPIリクエスト制限の優先順位は以下のようになります。

あるコンテンツ定義のコンテンツを返すAPIのレスポンス時にAPIリクエスト制限の優先順位は以下のようになります。 
## APIリクエスト制限の優先順位  

1.[API](/ja/docs/management/api-list/) -> [セキュリティ]の「IPアドレス制限」  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/73a19d739d2b7438d4b22186ff646622.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/26e373a35186093c3ca231ee871d6b17.png)

2.[API](/ja/docs/management/api-list/) -> [エンドポイントの設定]の[APIリクエスト制限]	
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c7591441946c6ed2b1c8093ff5fc6be.png)	
	
3.[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)の「APIリクエスト制限」  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4f32a35232561d983016ba26a3b5baf6.png)
	
4.[コンテンツカテゴリ](/ja/docs/management/content-structure-topics-category/)の「APIリクエスト制限」 	
![Image from Gyazo](https://t.gyazo.com/teams/diverta/77ecc3401869259208e2528fccf60294.png)
	
5.[コンテンツ](/ja/docs/management/content-structure-topics/)の「APIリクエスト制限」  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/865edc3d539eac28e1c499766a8a8c90.png)

## 関連ドキュメント
- [API](/ja/docs/management/api-list/)
- [API セキュリティ](/ja/docs/management/api-security/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツカテゴリ](/ja/docs/management/content-structure-topics-category/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [制限をかけていないのにAPIから403 forbidden が返ってきます](/ja/docs/faq/the-api-returns-403-forbidden-even-though-no-restrictions-are-applied/)
