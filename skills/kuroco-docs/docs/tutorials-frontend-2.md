# Kurocoドキュメント: チュートリアル / フロントエンド・KurocoFront（2/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 会員制サンプルサイトを利用する（`kuroco-sample-site`）
- KurocoFilesディレクトリとドメインの使い分けについて（`kurocofiles-directories-and-domains-usage`）
- 開発環境を作成する手順（`kurocofront-app-domain-for-front-end-staging-site`）
- サブサイトをプレビューサイトにする（`make-the-subsite-a-preview-site`）
- フロントエンドを一つのサーバにして、サイトキーを使ってバックエンドを切り替える（`one-server-for-front-end-and-switch-back-end-using-site-key`）
- 別サイトで使用しているドメインをKurocoに切り替える際の手順（`transferring-your-domain-from-another-site-to-kuroco`）
- KurocoFrontで独自ドメインを利用する手順（`using-a-custom-domain-name-on-kurocofront`）
- KurocoFrontで独自APIドメインを利用する手順（`using-your-own-api-domain-with-kurocofront`）


---

# 会員制サンプルサイトを利用する

> 元ページ: `tutorials/kuroco-sample-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kuroco-sample-site/
> 概要: Kurocoを試してみたいという方向けに、弊社がオープンソースで提供している会員制サンプルサイトを利用する方法を説明します。フロントエンドの構築やデプロイを行うことなくKurocoでサイト構築ができるので、お気軽にKurocoを試すことができます。

## 概要

Kurocoを試してみたいという方向けに、弊社がオープンソースで提供している会員制サンプルサイトを使用し、Kurocoを利用する方法を説明します。  
フロントエンドの構築やデプロイを行うことなくKurocoでサイト構築ができるので、お気軽にKurocoを試すことができます。  
3分程度の操作で会員制サイトを立ち上げることが出来ます。  
Kurocoで何ができるのか、どう動いているのかを理解するためにご利用ください。

### 作業の流れ
会員制サンプルサイトを利用してサイトを立ち上げる流れは以下の通りです。
- [Kurocoのアカウント登録](#kurocoのアカウント登録)
- [CORSの設定](#corsの設定)
- [会員制サンプルサイトの確認](#会員制サンプルサイトの確認)
- [コンテンツの追加](#利用例お知らせの追加)

### 前提条件
- この会員制サイトは、iOSのSafariでは動作しません。Google Chrome、Microsoft Edgeのご利用をお願いします。
- このドキュメントは東京リージョンでのご利用を想定しています。

## サイトを構築する
それではサイトの構築をはじめます。

### Kurocoのアカウント登録
Kurocoのアカウント登録します。[Free Trial](https://kuroco.app/ja/free_trial/)より必要項目を記入し「送信する」をクリックします。  
※リージョンは「アジア(東京)」を選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c725635780e4b1d6bb5a21cd497866d.png)

:::note
「サイトキー」「E-mail」「パスワード」は後ほど利用するので、メモをとっておいてください。
:::

登録したメールアドレスに登録完了のメールが届きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/826fd3623e1cddac5c65b9080dcda189.png)
メール内に記載されている管理画面URLをクリックし、ログインを行うとKuroco管理画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b9c1248f25b80cc6d9c2fccf89cfcc2.png)

### CORSの設定
API画面より、CORSの設定をします。
[API] -> [Default]をクリックし、「CORSを設定する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffc309c0ebcea53a7637c262a3805195.png)

CORS_ALLOW_ORIGINSの「Add Origin」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/26e7ba5a662bff8b195fe67020047f1f.png)
フィールドが追加されるので、`https://dev-nuxt-auth.g.kuroco-front.app` と記入し、「保存」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62379f134d531d518d4dbf43f8d54b9c.png)
以上でCORSの設定完了です。

### 会員制サンプルサイトの確認
次にサンプルサイトで動作するか確認をしてみます。

下記にアクセスします。

https://dev-nuxt-auth.g.kuroco-front.app/

ログイン画面が表示されるので、下記でログインします。
- Your sitekey：Kuroco登録時のサイトキー
- ID：kuroco登録時のE-mail
- Password：kuroco登録時のパスワード

全て記入し「Sign In」をクリックすると、ログイン後のトップページが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/af62c1c821486d525f33e202cb89413e.png)

以上で設定完了です。ご自身の会員制サイトが完成しました。  
フロントエンドはデモ用でKurocoFrontに用意されているものを利用していますが、バックエンドは今回、あなたが登録されたKurocoアカウントのものになるので、データはあなた独自のものになります。  

## 実際にサイトの更新などをしてみましょう

### コンテンツの確認

Kuroco管理画面より[コンテンツ] -> [Default]をクリックすると、テストデータが1件表示されています。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/795f6bd1017c4fa9d8e185acf8b81437.png)

こちらが、サイトトップページの「最新記事」に表示されているコンテンツです。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/76a30a5414e81b6bf23be5e238e16c06.png)

## 利用例：コンテンツの追加
Kurocoの管理画面より、[コンテンツ] -> [Default]より[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a4cda92b6368d5352a3e267db67b540.png)

記事追加ページより、必要項目を記入し「追加する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1fb1f542da28938ab7f3aceff8a14ecd.png)

記事を追加すると、サイトトップページの「最新記事」に追加した記事が表示されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9be2dd1d16d7385df2db6f7c0004b6ca.png)

## さいごに

以上でサイト構築と更新作業確認の完了です。  
先ほど登録したKurocoをバックエンドとしてあなた独自の会員制サイトが完成しました。  
フロントエンドのデプロイを行わずにKurocoが利用できるので、サンプルサイトとしてお気軽にご利用ください。

また、このチュートリアルでは、フロントエンドを簡易にするため共通のものを利用しています。  
下記のリポジトリからソースコードをcloneしてKurocoFrontにデプロイすると、デザインや機能などを自由にカスタマイズできるサイトも簡単に構築できます。

https://github.com/diverta/front_nuxt_auth

ご自身のフロントエンドとコンテンツを設定する方法については、以下をご確認ください。
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [チュートリアル：コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [管理画面マニュアル：コンテンツ](/ja/docs/management/content-structure-topics/)

ご不明点やご質問ありましたら[お問い合わせ](https://kuroco.zendesk.com/)よりご連絡ください。

## 関連ドキュメント
- [会員制サンプルサイトの解説](/ja/docs/tutorials/explanation-of-kuroco-sample-site/)
- [会員制サンプルサイトをコピーして、Kurocoで会員制サイトを構築する方法](/ja/docs/tutorials/building-a-membership-website-on-kuroco-from-the-sample-site-template/)
- [アカウント登録する](/ja/docs/tutorials/signup/)
- [会員制サンプルサイトで、開発環境と本番環境を分ける方法](/ja/docs/tutorials/separating-development-and-production-environments-for-your-sample-membership-site/)
- [API](/ja/docs/management/api-list/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)


---

# KurocoFilesディレクトリとドメインの使い分けについて

> 元ページ: `tutorials/kurocofiles-directories-and-domains-usage` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/
> 概要: KurocoFilesの3つのディレクトリ（通常、閲覧制限付き、メタデータ付き）と3つのドメイン（API、Files、管理画面）の使い分けについて詳しく解説します。

KurocoFilesでファイルを管理する際、適切なディレクトリとドメインを選択することで、セキュリティ、パフォーマンス、機能面で最適な運用が可能になります。本ドキュメントでは、3つのディレクトリタイプと3つのドメインタイプの特徴と使い分けについて詳しく解説します。

## KurocoFilesディレクトリの種類と使い分け

KurocoFilesには以下の3つのディレクトリタイプがあります。

### KurocoFiles
**用途**: インターネットユーザーに全公開する静的コンテンツ

**特徴**:
- 認証不要で誰でもアクセス可能な公開ファイル
- 最も高速なアクセスが可能

### KurocoFiles（閲覧制限付き）
**用途**: 認証が必要な静的コンテンツ

**特徴**:
- 認証されたユーザーのみアクセス可能
- グループ権限による細かいアクセス制御が可能
- セキュアなファイル配信

### KurocoFiles（メタデータ付き）
**用途**: クレジットや説明情報が必要なファイル

**特徴**:
- ファイルにクレジット情報と説明文を付与可能
- APIレスポンスにメタデータが含まれる
- ファイルマネージャーでファイル情報を管理

## ドメインの種類と使い分け

KurocoFilesのファイルは、以下の3つのドメインでアクセス可能です。

### APIドメイン
**ドメイン**: `kuroco.app`

**特徴**:
- APIでCookie認証をしている場合、そのクレデンシャルがそのまま利用可能
- 画像最適化機能が動作しない
- APIリクエストとしてカウントされる

### Filesドメイン
**ドメイン**: `kuroco-img.app`

**特徴**:
- APIのレスポンスに含まれるURLはこのドメインになる
- 認証が必要なファイルはAPIレスポンスに含まれるURLに`t=...`のトークンが付与される
- 画像最適化機能が動作する
- 最も一般的なファイルアクセス方法

### 管理画面ドメイン
**ドメイン**: `kuroco-mng.app`

**特徴**:
- 管理画面の認証がそのまま利用可能
- 画像最適化機能・キャッシュ機能が動作しない
- サイト管理者のファイル確認用途に最適

## ユースケース

- **ケース1: 管理画面プラグイン用ファイル**  
  管理画面ドメイン + KurocoFiles（閲覧制限付き）
  ```
  理由:
    - 公開したくないファイル → 閲覧制限付きディレクトリ
    - 管理画面での利用 → 管理画面ドメインで認証を活用
    - レスポンス速度よりもセキュリティを重視
  ```
  備考: 公開しても問題ない場合は、Filesドメイン + KurocoFiles（通常）の方がレスポンスが早い

- **ケース2: フロントエンド用の一般公開画像**  
  Filesドメイン + KurocoFiles（通常）
  ```
  理由:
    - 一般公開コンテンツ → 通常ディレクトリ
    - 画像最適化機能を活用 → Filesドメイン
    - 高速なアクセスが可能
  ```

- **ケース3: 会員限定の静的コンテンツ**  
  APIドメイン + KurocoFiles（閲覧制限付き）
  ```
  理由:
    - 認証が必要 → 閲覧制限付きディレクトリ
    - Cookie認証を活用 → APIドメイン
    - フロントエンドでの認証状態と連携
  ```
  備考: 認証が必要なファイルでもAPIレスポンスからURLを取得する場合は、URLにトークンが含まれるためFilesドメインをそのまま使用可能

- **ケース4: 著作権保護が必要な画像**  
  Filesドメイン + KurocoFiles（メタデータ付き）
  ```
  理由:
    - クレジット情報が必要 → メタデータ付きディレクトリ
    - 画像最適化を活用 → Filesドメイン
    - APIレスポンスでメタデータを取得可能
  ```

適切なディレクトリとドメインの組み合わせを選択することで、セキュリティ、パフォーマンス、機能面で最適なファイル管理が実現できます。用途に応じて最適な構成を選択してください。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)
- [ファイルにcreditとdescriptionのmeta情報を追加する](/ja/docs/tutorials/file-credit-and-description-information/)
- [Kurocoで利用するドメインの種類について教えてください](/ja/docs/faq/what-types-of-domains-does-kuroco-use/)


---

# 開発環境を作成する手順

> 元ページ: `tutorials/kurocofront-app-domain-for-front-end-staging-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/
> 概要: 独自ドメインの利用を開始すると、デフォルトで存在するhttps://サイトキー.g.kuroco-front.app をステージングサイト用のドメインとして利用できます。

## 概要
独自ドメインの利用を開始すると、デフォルトで存在する`https://サイトキー.g.kuroco-front.app`をステージングサイト用のドメインとして利用できます。  
本チュートリアルでは、GitHubのブランチを分けることで`https://サイトキー.g.kuroco-front.app`のドメインをフロントエンドのステージサイトとして利用する方法を紹介します。  
また、Kurocoのサブサイトを作成し、バックエンド及びフロントエンドが本番と異なる開発環境も作成します。  

### 学べること
本チュートリアルでは以下の手順でそれぞれの環境を作成します。    

- [ステージング環境の設定手順](#ステージング環境の設定手順)
- [開発環境の設定手順](#開発環境の設定手順)
- [ファイル構成の確認](#ファイル構成の確認)

### 前提条件
今回は下記の構成で実装します。  

|環境|ブランチ |ドメイン |用途|
| :--- | :--- | :--- | :--- |
|本番環境|main|`独自ドメイン`|公開用のサイト|
|ステージング環境|stg|`https://サイトキー.g.kuroco-front.app`| 本番とバックエンドは共通、フロントエンドが異なるデザイン修正などの事前確認用サイト|
|開発環境|dev|`独自ドメイン`| 本番とバックエンド及びフロントエンドが異なる、機能追加時の事前確認用サイト|

注: 今回はブランチ名を stg, devとしていますが、任意に変更して構いません。

また、本チュートリアルは[KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)及び、[KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)が完了し、独自ドメインでサイトの表示ができている状態を前提としています。

## ステージング環境の設定手順
### 1. stgブランチを作成する
本番サイトとステージング環境の表示はGitHubのブランチで分けます。  
対象のディレクトリに移動後、コマンドラインより下記実行します。  

```
git checkout -b stg
```

### 2. 環境変数設定ファイルの作成
サイトタイトルやメタ情報など開発環境と本番環境で異なる環境変数を使用する場合、環境毎に設定ファイルを作成して管理します。  

ここでは本番環境用とステージング環境用に以下のファイルを作成します。  
ステージング環境では本番環境とバックエンドが共通のため、同じAPIドメインになりますが、この後作成する開発環境では異なるドメインになるため、合わせて設定しておきます。  
YOUR_SITE_KEYの部分はご自身のサイトキーに置き換えてください。

env.production.js
```js 
module.exports = {
  API_BASE: 'https://YOUR_SITE_KEY.g.kuroco.app',
  SITE_TITLE: 'Kurocoサンプルサイト',
  META_TITLE: 'Kurocoサンプルサイト',
  SITE_DESCRIPTION: 'Kurocoビギナーズガイドを参考に作成したサンプルサイトです。',
  RSS_SITE_TITLE: 'Kurocoサンプル',
  RSS_SITE_DESCRIPTION: 'KurocoビギナーズガイドでKuroco利用を開始しましょう',
  ROBOTS: 'index',
}
```

env.staging.js
```js 
module.exports = {
  API_BASE: 'https://YOUR_SITE_KEY.g.kuroco.app',
  SITE_TITLE: '[ステージング]|Kurocoサンプルサイト',
  META_TITLE: '[ステージング]|Kurocoサンプルサイト',
  SITE_DESCRIPTION: '[ステージング]|Kurocoビギナーズガイドを参考に作成したサンプルサイトです。',
  RSS_SITE_TITLE: '[ステージング]|Kurocoサンプル',
  RSS_SITE_DESCRIPTION: '[ステージング]|KurocoビギナーズガイドでKuroco利用を開始しましょう',
  ROBOTS: 'noindex',
}
```

:::caution
ここで追加した環境変数設定ファイルはGithubリポジトリがパブリックな場合は外部から参照可能です。  
APIキーなどの機密情報は環境変数に設定せず、Githubシークレットに保存して、YAMLファイルで呼び出すように記述するなど対応してください。
:::

### 3. kuroco_front_stg.jsonを作成する
ステージング環境だけにBASIC認証をかけるために、ステージング環境用の`kuroco_front.json`を作成します。  

`/public` 配下の`kuroco_front.json`をコピーして、`kuroco_front_stg.json`を作成します。

以下のようにBasic認証を記述します。  

```json [kuroco_front_stg.json]
{
    "rewrites": [
        {
          "source": ".*",
          "destination": "/index.html"
        }
      ],
    "redirects": [],
    "basic":["user:pass"],
    "ip_restrictions":[]
}
```

### 4. nuxt.config.tsの修正
APIドメインを環境変数設定ファイルから読み込むため、nuxt.config.tsファイルを更新します。  
また、環境変数設定ファイルを読み込んでいることが分かりやすいようヘッダーのサイトタイトルも設定します。  

```js title="nuxt.config.ts"
const environment = process.env.APP_ENV;
const envSettings = require(`./env.${environment}.js`); 

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  runtimeConfig: {
      // Public keys that are exposed to the client
      public: {
          apiBase: envSettings.API_BASE
      }
  },
  app: {
    head: {
      title: envSettings.SITE_TITLE,
    },
  },
})

```

### 5. staging.ymlファイルを追加する
次に、stgブランチで変更をpushした際にGithub Actionsを動作させるためのYAMLファイルを追加します。  
Kuroco管理画面より[外部システム連携] -> [GitHub]をクリックし、「GitHub Actions workflow file ステージングサイト」のテキストエリア内をコピーします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b1c730611960bf6093cec97e57c8f2b.png)

コピーした内容で`.github/workflows/staging.yml`ファイルを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f1a772afd4075c52bbf329320436bdc7.png)

さらに`staging.yml`ファイルに以下の修正を加えます。

- Github Actionsの名前を変更する  
  1行目を以下に変更します。  
  `name: Build and deploy to Kuroco front(stg)`

- Github Actions実行のトリガーになるブランチを変更する  
  branches: の部分をstageからステージング環境用のブランチ名に修正します。  
  今回はstgに修正します。  

- envで環境の指定をする  
  `.github/workflows/staging.yml` の jobs:の直前に下記の記述を追加します。
  ```
  env:
    APP_ENV: staging
  ```

- ステージング環境用のkuroco_front.jsonを利用する  
  KurocoFrontを利用するためのJSONファイルは`kuroco_front.json`です。  
  そこで、`kuroco_front_stg.json`を`kuroco_front.json`にコピーする記述をYAMLファイルに追加することで、`staging.yml` が実行されたときのみ`kuroco_front_stg.json`を利用するように対応します。 
  `.github/workflows/staging.yml` の `- name: Use Node.js`の直前に下記の記述を追加します。(2箇所) 
  ```
  - name: Copy kuroco_front.json
    run:  cp public/kuroco_front_stg.json public/kuroco_front.json 
  ```

`staging.yml`ファイルは以下のようになります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/69c91d0f0710bf37be35edb746ff46e6.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/93381d32a15640e99bc8c8c4bdfe82f6.png)

修正が完了したらファイルを保存します。  

### 6. build.ymlファイルを更新する
環境変数からAPIドメインを読み込むように変更したので、本番環境用のbuild.ymlファイルにも環境変数を指定するコードを追加します。

- envで環境の指定をする  
  `.github/workflows/build.yml` の jobs:の直前に下記の記述を追加します。
  ```
  env:
    APP_ENV: production
  ```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53fce61e087e5fc469d1753f1b9e8d57.png)

### 7. stgブランチでpushする
ここまでの変更をGithHubにpushします。 
GitHubの「Actions」タブをクリックすると、ビルドの状況が確認でき、staging.ymlの内容でビルドが実行されていることがわかります。
 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa3454a60eebf160b6d4c8612eb3e640.png)

ビルドが完了したら、Kuroco管理画面のロゴマークからステージング環境にアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c63163dc7bd81b9426d93fbab11a427.png)

ステージング環境にアクセスすると、Basic認証が求められることを確認できました。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b32d6297ab43b62ec31eea7b6c50e24f.png)

Kuroco管理画面の[サイトを表示]で本番環境にアクセスすると、Basic認証は求められませんので、stgブランチでの更新がステージング環境のみに反映されていることがわかります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb26204c17eb182418ecc4089b2e11c2.png)

### 8. stgブランチの変更をmainブランチにマージする
最後に以上の内容をmainブランチにマージします。

以上でステージング環境の設定が完了です。
以降、ステージング環境用のブランチ(今回の場合はstg)で変更した内容はステージング環境 (`https://サイトキー.g.kuroco-front.app`) に反映されます。

## 開発環境の設定手順
### 1. devブランチを作成する
本番サイトと開発環境の表示はGitHubのブランチで分けます。  
対象のディレクトリに移動後、コマンドラインより下記実行します。  

```
git checkout -b dev
```

### 2. サブサイトを追加する
次にバックエンドを開発環境と分けるため、Kurocoの管理画面からサブサイトを作成します。  

#### サブサイトの作成
[環境設定] -> [サイト一覧]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e62d36fc06738d5bd8bde2772e0d807.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1fc67dc7a135bc709f3bea4d6863a200.jpg)

下記のように設定して[追加する]をクリックします。  

|項目   |設定  |
| :--- | :--- | 
|コピー元のサイト名|本番環境のサイトを選択|
|サイト名|開発環境サイト|
|サイトキー|任意のサイトキー|
|メールアドレス|サイトの構築完了メールの送付先。管理者の初期パスワードもこのメールに記載されます。|
|会社名|貴社名|
|名前|ご自身のお名前|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fb7566e4555f76f294c78f982e967377.jpg)

#### GitHub連携
サブサイトが作成できたら、サブサイトとGithubを連携します。  
[外部システム連携] -> [GitHub]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7553b3e477fd07848ee5a61724007648.png)

[GitHubリポジトリと接続する]をクリックし、GitHubと連携します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0edf67511a9364e3d06138593c53de1f.png)

GitHubと連携ができたらリポジトリを本番環境と同じリポジトリに設定して[更新する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef0bd7f4ee9bbcb16410e4c9c977fde6.png)

### 3. 独自ドメイン、独自APIドメインを設定する
開発環境用の独自ドメインと独自APIドメインを設定します。  
[環境設定]->[独自ドメイン/TLS証明書]から開発環境用の独自ドメインと独自APIドメインを設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/152c78d6ccb15b3b41bca9b24b9908d1.png)

DNSの設定が反映され、全てOKの表示になったら完了です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ba473dd92f229f6244782a5f8fe29f19.jpg)

[環境設定]->[アカウント設定]からフロントエンドドメインとAPIドメインを変更します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/879979748f24cd6881e8ad5b68e60928.jpg)


### 4. 環境変数設定ファイルの作成
開発環境用の環境変数設定ファイルを以下のように作成します。  
YOUR_DEV_SITE_KEYの部分はご自身のサイトキーに置き換えてください。

env.development.js
```js 
module.exports = {
  API_BASE: 'https://YOUR_DEV_SITE_KEY.g.kuroco.app',
  SITE_TITLE: '[開発]|Kurocoサンプルサイト',
  META_TITLE: '[開発]|Kurocoサンプルサイト',
  SITE_DESCRIPTION: '[開発]|Kurocoビギナーズガイドを参考に作成したサンプルサイトです。',
  RSS_SITE_TITLE: '[開発]|Kurocoサンプル',
  RSS_SITE_DESCRIPTION: '[開発]|KurocoビギナーズガイドでKuroco利用を開始しましょう',
  ROBOTS: 'noindex',
}
```

### 5. kuroco_front_dev.jsonを作成する
開発環境だけにBASIC認証をかけるために、開発環境用の`kuroco_front.json`を作成します。  

`/public` 配下の`kuroco_front.json`をコピーして、`kuroco_front_dev.json`を作成します。

以下のようにBasic認証を記述します。  

```json [kuroco_front_dev.json]
{
    "rewrites": [
        {
          "source": ".*",
          "destination": "/index.html"
        }
      ],
    "redirects": [],
    "basic":["user:pass"],
    "ip_restrictions":[]
}
```

### 6. develop.ymlファイルを追加する
次に、devブランチで変更をpushした際にGithub Actionsを動作させるためのYAMLファイルを追加します。  
先ほど作成した開発環境用のKuroco管理画面より[外部システム連携] -> [GitHub]をクリックします。  
「GitHub Actions workflow file フロントエンドドメイン」のテキストエリア内をコピーします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/70307b849d208b5e30ea58be6a8467d1.jpg)

コピーした内容で`.github/workflows/develop.yml`ファイルを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/578beb7424ae8534b74254ff43a8db8e.png)

さらに`develop.yml`ファイルに以下の修正を加えます。

- Github Actionsの名前を変更する  
  1行目を以下に変更します。  
  `name: Build and deploy to Kuroco front(dev)`

- Github Actions実行のトリガーになるブランチを変更する  
  branches: の部分をmainから開発環境用のブランチ名に修正します。  
  今回はdevに修正します。  

- GitHubのシークレットを読み込む  
  `.github/workflows/develop.yml` の jobs:の直前に下記の記述を追加します。
  ```
  env:
    APP_ENV: development
  ```

- 開発環境用のkuroco_front.jsonを利用する  
  KurocoFrontを利用するためのJSONファイルは`kuroco_front.json`です。  
  そこで、`kuroco_front_dev.json`を`kuroco_front.json`にコピーする記述をYAMLファイルに追加することで、`develop.yml` が実行されたときのみ`kuroco_front_dev.json`を利用するように対応します。  
  `.github/workflows/develop.yml` の `- name: Use Node.js`の直前に下記の記述を追加します。(2箇所) 
  ```
  - name: Copy kuroco_front.json
    run:  cp public/kuroco_front_dev.json public/kuroco_front.json 
  ```

`develop.yml`ファイルは以下のようになります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/da2380bb621d72ca942189c93ea9ccd0.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ad5da28a106f53c2241511ad89e2af9.png)

修正が完了したらファイルを保存します。  

### 7. devブランチでpushする
ここまでの変更をGithHubにpushします。 
GitHubの「Actions」タブをクリックすると、ビルドの状況が確認でき、develop.ymlの内容でビルドが実行されていることがわかります。
 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/333e5c73b4458dc350895597292583a7.png)

ビルドが完了したら、Kuroco管理画面の[サイトを表示]から開発環境のサイトにアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb26204c17eb182418ecc4089b2e11c2.png)

BASIC認証以外は本番環境と同じ表示がされます。  

### 8. devブランチの変更をmainブランチ、stgブランチにマージする
以上の内容をmainブランチとstgブランチにマージします。

以上で開発環境の設定が完了です。 以降、開発環境用のブランチ(今回の場合はdev)と開発環境サイトの管理画面で変更した内容は開発環境サイト に反映されます。

### 開発環境と本番環境間でデータの同期をする
本番環境と開発環境でデータの差異が大きくなってしまった場合や、  
開発環境で更新したコンテンツや追加した処理などを一括で本番環境に反映したい場合、同期の機能が利用できます。  

[サイト一覧](/ja/docs/management/site-list/)から同期先になるサイトの[編集]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7eaba33d986387c87f08dcda4b5112aa.jpg)

同期の項目で同期元サイトキーを選択し、すぐに同期するにチェックを入れて更新します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f53c3dc7da9b645e9dfda27ae655775b.jpg)

「更新しました。」の表示がでたら同期は完了です。

:::danger
同期の方向を間違うと必要なデータがすべて上書きされてしまうため、  
必要に応じてバックアップを取っておくことをお勧めします。
:::

## ファイル構成の確認
ステージング環境及び、開発環境の準備が完了すると、どのブランチにも以下のファイルが存在する状態となります。  
うまくいかない場合はファイル構成が間違っていないかご確認ください。  

```
.github\workflows
  - build.yml
  - develop.yml
  - staging.yml
public
  - kuroco_front_dev.json
  - kuroco_front_stg.json
  - kuroco_front.json
env.production.js
env.staging.js
env.development.js
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/06161411c69a3cd7f683a8e2ce56fce4.png)

想定通りに設定ができている場合、各環境の表示を確認すると、以下のように環境に応じたサイトタイトルが表示されています。

- 本番環境
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/3613cc2bf46c3664bdcf18eb1b922216.png)
- ステージング環境
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/b21c5c124e495990bb43bff3429ccf6b.png)
- 開発環境
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5d8aea18543437add306740ebcf4b3e.png)

## 関連ドキュメント
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)


---

# サブサイトをプレビューサイトにする

> 元ページ: `tutorials/make-the-subsite-a-preview-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/make-the-subsite-a-preview-site/
> 概要: Kurocoで作成したサブサイトに同期元の設定をすることでプレビューサイトとして利用できます。設定をすると、同期元サイト(通常、本番サイト)で作成したコンテンツが自動的にプレビューサイトに送られ、プレビューサイトでデプロイした環境で表示の確認が可能です。

## 概要
Kurocoで作成したサブサイトに同期元の設定をすることでプレビューサイトとして利用できます。  
設定をすると、同期元サイト(通常、本番サイト)で作成したコンテンツが自動的にプレビューサイトに送られ、プレビューサイトでデプロイした環境で表示の確認が可能です。  

機能の概要図を以下に示します。  
挙動の特徴としては、同期元サイト(本番サイト)で承認ワークフローで申請したコンテンツが、プレビューサイトでは承認反映済みの状態で確認できる動作になります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d16809731b5d53c773520cf5a42fd210.png)

:::caution
- プレビューサイトではコンテンツの更新はしない想定になっています。  
  プレビューサイトでコンテンツの追加・更新を行った場合、コンテンツの更新はされますが、同期元サイトからの同期が発生した場合、同期元のデータで上書きされます。
- 同期元サイトからの同期が発生した場合は、プレビューサイトのトリガーは起動しません。
:::

本ドキュメントではKuroco上におけるプレビューサイトの設定とその動作を説明します。

### 前提条件
:::info
- サブサイトを作成していない場合は「[サイト一覧](/ja/docs/management/site-list/)」から追加してください。
- フロントエンドについては「[開発環境を作成する手順](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)」を参考に、同期元サイト、プレビューサイトそれぞれデプロイください。
:::

:::tip
Kurocoのプレビュー機能には、プレビューサイト機能のほかに以下があります。詳細はそれぞれのドキュメントをご参照ください。  
- プレビューのエンドポイント：[プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)
- プレビューデプロイ：[KurocoFrontへプレビューデプロイする手順](/ja/docs/tutorials/connect-to-github-with-kuroco-front/#kurocofrontへプレビューデプロイする手順)
:::

## プレビューサイトの設定方法
### 同期元サイトとプレビューサイトを全同期する
プレビューサイト機能で同期されるのはコンテンツのみです。タグIDやメンバーIDを揃えるために事前に全同期を実施します。

:::info
運用を進める中で差分が大きくなった場合は、本ステップを再度実施し、全体を同期してください。
:::

[環境設定] -> [サイト一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d34e973cdd6985c77e9ee4bb8703410.png)

プレビューサイトにするサブサイトの[編集]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/77328cc62de138047471d711be7ac058.png)

[すぐに同期する]を有効にし、同期元サイトと全同期を選択して[更新する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ac803801a1c8fff1b1f5cc0d30970fd.png)

### 同期元サイトの設定をする
全同期の完了後、プレビューサイト向けに[コンテンツ同期元サイトキー]を設定します。

再度、プレビューサイトにするサブサイトの[編集]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/77328cc62de138047471d711be7ac058.png)

コンテンツ同期元サイトキーに同期元になるサイトキーを設定して[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0cd590f25f7c0e7b03efabd0b2e56f0b.png)

以上でプレビューサイトの設定は完了です。

同期元サイトのコンテンツ編集画面で、公開設定に「プレビューサイトへ送る」が追加されていることを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/166044a0a3c74f8ff07249bd205dee49.png)

## プレビューサイトの動作
- 同期元サイトで追加・更新・削除したコンテンツはプレビューサイトでも追加・更新・削除されます
- 同期元サイトで「プレビューサイトへ送る」を選択してコンテンツを追加・更新すると同期元サイトでは承認ワークフローに乗り、プレビューサイトでは公開状態で即時コンテンツが追加されます。承認時、コンテンツは公開になります。  
  ※ワークフローが利用できるようになっている必要があります。
- 同期元サイトで「プレビューサイトへ送る（非公開）」を選択してコンテンツを追加・更新すると同期元サイトでは承認ワークフローに乗り、プレビューサイトでは非公開状態で即時コンテンツが追加されます。承認時、コンテンツは非公開になります。  
  ※ワークフローが利用できるようになっている必要があります。
- プレビューサイトで表示の確認をしてOKであれば同期元サイトで承認するフローを想定しています。
- 承認中コンテンツに更新があった場合も、自動でプレビューサイトのコンテンツが更新されます。

## 制限事項
1. 同期されるのはコンテンツのみです。（タグやマスタは同期されません。）
2. 同期元サイトとプレビューサイトでメンバーIDが一致していない場合、コンテンツ所有者のmember_idがずれる可能性があります。
3. タグのIDが違う場合は、タグの紐づけがずれます。
4. CSVアップロードで追加・更新したコンテンツについてはプレビューサイトに同期されません。
5. 一覧画面からの公開状態・並び順を更新した場合はプレビューサイトに同期されません。
6. 途中保存はプレビューサイトに同期されません。
7. コンテンツカテゴリはプレビューサイトに同期されません。追加・更新が必要な場合は両方のサイトで更新してください。その際コンテンツカテゴリIDが同じになるように調整してください。
8. ファイルマネージャーはプレビューサイトに同期されません。
    - WYSIWYGで追加した画像は同期元の画像を参照します。
    - ファイル（ファイルマネージャーから）の項目のファイルは、同期元とプレビューサイトの両方に保存してください。
9. プレビューサイトではコンテンツの更新はしない想定になっています。  
  プレビューサイトでコンテンツの追加・更新を行った場合、コンテンツの更新はされますが、同期元サイトからの同期が発生した場合、同期元のデータで上書きされます。
10. GCS,Vimeo,S3はプレビューサイトに同期されません。

:::tip
制限事項の多くは、各IDが同期元サイトとプレビューサイトで異なる状態が影響します。
差分が大きくなった場合は「[同期](/ja/docs/reference/sync-site-data/)」を実行して、IDが揃うようにしてください。
:::

## 関連ドキュメント
- [開発環境を作成する手順](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)


---

# フロントエンドを一つのサーバにして、サイトキーを使ってバックエンドを切り替える

> 元ページ: `tutorials/one-server-for-front-end-and-switch-back-end-using-site-key` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/one-server-for-front-end-and-switch-back-end-using-site-key/
> 概要: 本チュートリアルでは企業コード（サイトキー）でバックエンドを切り替えるというB2Bアプリケーションの構築方法を説明します。

デザインは共通でコンテンツの内容がお客様によって違うような、B2BのサービスをKurocoを利用して構築する場合、フロントエンドを共通にして、バックエンドをお客様毎に切り替えるといった使い方が可能です。  
Kurocoのデモサイトで、パッケージにもなっている「シンプルな会員制サイト」はフロントエンドを共通にした利用方法となっています。  
サイトURL：https://dev-nuxt-auth.g.kuroco-front.app/  
Githubリポジトリ：https://github.com/diverta/front_nuxt_auth

本チュートリアルでは企業コード（サイトキー）でバックエンドを切り替えるというB2Bアプリケーションの構築方法を説明します。

:::info
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、下記のチュートリアルを実施済みであることを前提としています。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)  
[KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
:::

## メインサイトのコンテンツ登録をする
お客様から申し込みがあった場合に、コピーをしてお客様用の新たなバックエンド(サブサイト)を作成する運用を想定します。  
そこでまずはマスタとなるメインサイトのコンテンツを登録します。  
なお、本チュートリアルではメインサイトのサイトキーを`sample-b2b-service`、サブサイトのサイトキーを`sample-b2b-service-001`とします。    

### コンテンツの登録
まずはKurocoの管理画面でコンテンツを定義します。  
[コンテンツ定義]をクリックします。
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/e4c6ac4015bcc42eaaeb6f99764154fa.png)
[追加]をクリックします。
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/767d83ab8c249d8ed3c9efe9c6240f17.png)
コンテンツ定義編集画面でお好きな名前を入力し、コンテンツの項目を設定し、[追加する]をクリックします。  
今回は下記のように設定しています。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8ac6ce7e44b6c3ceeff8fc1ab9dfbcde.png)
次にコンテンツを追加します。  
[コンテンツ]->[ご契約者様専用コンテンツ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee1bc0a231cafb9b550814c5e1b371e0.png)
[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4d50e2fbfdd98405b6c84727787a768c.png)
先ほど定義したコンテンツの項目が表示されますので、コンテンツを入力して[追加する]をクリックします。  
今回は下記のように登録しています。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5ad27604ef491605a511187427a7061.png)
追加したコンテンツ定義のID(8)とコンテンツのID(4)は後ほど利用するのでメモしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/83a9ceb4499d6c47ab479e0292cbe8cd.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca5973728fec3d121134f8f133300412.png)
### APIの登録
続いてAPIの登録をします。  
Kurocoの管理画面から[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d2b16963c14af02eba7ed2dc396d548.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f8cc0a8eca5663fd901b43826421253.png)

タイトル、版、ディスクリプションを入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/76618ca32f7ce8bc82810fbff7c66a4a.png)
追加したAPIに遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6b8c367e494cf70fc6322a8d817077b.png)

続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a84d6737b31c7d4ead5dc2c92b168dc.png)

[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
続いて、CORSの設定をします。   
[CORSを設定する] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f5fe52c20c0ff874ec081151f8da7839.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000`
- フロントエンドドメイン (ここでは`https://sample-b2b-service.g.kuroco-front.app`)

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET
- POST
- OPTIONS

設定できたら[保存する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ec5e588193abeea1051125551462788.png)

次に先ほど作成したコンテンツ「ご契約者様専用コンテンツ」を取得するエンドポイントを作成します。  
[エンドポイントの追加]をクリックします。    
![Image from Gyazo](https://t.gyazo.com/teams/diverta/917c1f5cadcd9cb78fff20f375e2bda4.png)

下記のように設定し、[追加する]をクリックします。

| 設定項目 | 設定 ||
| :--- | :--- | :--- |
|パス|service_top||
||有効/無効|有効|
|モデル|カテゴリー|コンテンツ|
||モデル|Topics|
||オペレーション|Details|
|topics_group_id|作成したコンテンツ定義のグループID(8)||

![Image from Gyazo](https://t.gyazo.com/teams/diverta/374d1147197b685f7d7fbe68d95cd356.jpg)

以上で、Kuroco側の設定は完了です。  

## フロントエンドを作成する
### ご契約者様専用コンテンツのページを追加する
まずは先ほど作成したご契約者様専用コンテンツを表示するためのフロンエンド部分を作成します。  

pages のディレクトリに owners-page のフォルダを作成し、index.vue のファイルを作成します。  
 
```markup [/pages/owners-page/index.vue]
<template>
  <div>
    <h1>{{ response.details.ext_1}}</h1>
    <p>{{ response.details.ext_2}}</p>

  <button type="button" @click="logout">
  ログアウト
  </button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  middleware: 'auth',
  async asyncData({$axios}) {
    try {
      const response = await $axios.$get('/rcms-api/4/service_top/4')
      return { response }
    } catch (e) {
      console.log(e.message)
    }
  },
  methods: {
    ...mapActions(['logout'])
  }
}
</script>
```

### エンドポイントを叩くURLをログイン時に変更させる
続いて、エンドポイントを叩くURLをフロントエンドから変更できるように記述を調整します。  
`/pages/login/index.vue`と、`/store/index.js`のコードを次のように変更します。  

こちらでは`/store/index.js`の以下の記述で、入力されたsitekeyを元にリクエスト先のAPIを変更しています。 
```
this.$axios.defaults.baseURL = getters.hostname;
```

```markup [/pages/login/index.vue]
<template>
    <form @submit.prevent="login">
      <p v-if="loginStatus !== null" :style="{ color: resultMessageColor }">
        {{ resultMessage }}
      </p>

        <input v-model="sitekey" name="sitekey" type="sitekey" placeholder="sitekey">
        <input v-model="email" name="email" type="email" placeholder="email">
        <input
            v-model="password"
            name="password"
            type="password"
            placeholder="password"
        >
        <button type="submit">
            ログイン
        </button>

        <div>
            <nuxt-link to="/news/">
                ニュース一覧ページへ
            </nuxt-link>
        </div>
        <div>
            <nuxt-link to="/owners-page/">
                契約者専用ページへ
            </nuxt-link>
        </div>
    </form>
</template>

<script>
export default {
    data () {
        return {
            sitekey: '',
            email: '',
            password: '',
            loginStatus: null,
            resultMessage: null
        }
    },
    computed: {
        resultMessageColor () {
            switch (this.loginStatus) {
            case 'success':
                return 'green'
            case 'failure':
                return 'red'
            default:
                return ''
            }
        }
    },
    methods: {
        async login () {
            try {
                const payload = {
                    sitekey: this.sitekey,
                    loginInfo: {
                        email: this.email,
                        password: this.password
                    }
                }
                await this.$store.dispatch('login', payload)
                this.loginStatus = 'success'
                this.resultMessage = 'ログインに成功しました。'
            } catch (e) {
                this.loginStatus = 'failure'
                this.resultMessage = 'ログインに失敗しました。'
            }
        }
    }
}
</script>
```


```js [/store/index.js]
export const state = () => ({
    profile: null
})

export const getters = {
    authenticated (state) {
        return state.profile !== null
    },
    hostname () {
        try {
            const sitekey = localStorage.getItem('sitekey');
            if (sitekey === '' || sitekey === 'undefined' || sitekey === 'null') {
                throw new Error('unknown sitekey');
            }
            return `https://${sitekey}.g.kuroco.app`;
        } catch (e) {
            return false;
        }
    }
}

export const mutations = {
    setProfile (state, { profile }) {
        state.profile = profile
    },
}

export const actions = {
    async login ({ commit, getters }, payload) {
        localStorage.setItem('sitekey', payload.sitekey);
        this.$axios.defaults.baseURL = getters.hostname;

        await this.$axios.$post('/rcms-api/3/login', payload.loginInfo)
        const profileRes = await this.$axios.$get('/rcms-api/3/profile', { withCredentials: true })
        commit('setProfile', { profile: profileRes.data })        
    },

    async logout ({ commit }) {
        try {
            await this.$axios.$post('/rcms-api/3/logout')
        } catch {
             /** No Process */
             /** エラーが返却されてきた場合は、結果的にログアウトできているものとみなし、これを無視します。 */
            }
            commit('setProfile', { profile: null })

            this.$router.push('/login')
        },

    async restoreLoginState ({ commit, dispatch, getters }) {
        if (!getters.hostname) {
            await dispatch('logout')
            throw new Error('need to login')
        }
        try {
            this.$axios.defaults.baseURL = getters.hostname;
            const profileRes = await this.$axios.$get('/rcms-api/3/profile', { withCredentials: true })
            commit('setProfile', { profile: profileRes.data });
        } catch {
            await dispatch('logout')
            throw new Error('need to login')
        }
    }
}
```

以上でフロントエンドの準備は完了です。  

## ユーザー用のバックエンドを作成する
### サブサイトの追加をする
Kurocoの管理画面から契約者用のバックエンド(サブサイト)を作成します。  
[サイト一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8dd81949f357649b61481f5ec54ca32.png)
[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0dfd2d8d25e6b263c7a2bc2451782195.png)
下記のように設定して[追加する]をクリックします。  

|項目   |設定  |
| :--- | :--- | 
|コピー元のサイト名|コピー元となるサイトを選択します。(ここではsample-b2b-service)|
|サイト名|株式会社ディバータ様サイト|
|サイトキー|sample-b2b-service-001|
|URL|フロントエンド共有にチェックを入れて、`https://sample-b2b-service.g.kuroco-front.app`を選択します。|
|メールアドレス|サイトの構築完了メールの送付先。管理者の初期パスワードもこのメールに記載されます。|
|会社名|株式会社ディバータ|
|名前|DIVERTA TARO|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/51e58c5b9e20e1a5b1431860bd6601dc.png)
### サブサイトのコンテンツを調整する
サブサイトの追加が完了したら、サブサイトのコンテンツを調整します。  
メインサイトのサイト一覧に追加したサブサイトが表示されるので、[管理画面]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d206487f62ebcb84ac8462c5568893a8.png)
サブサイトにログインします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bebc2905d765b44c5a9355bf2b46006.png) 
サブサイトのご契約者様専用コンテンツをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bcd82afaf879d30c344697c64281802.jpg)
コンテンツ一覧から[契約者ページトップ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/23f9ccd2fd3f0dc516c56486618beaa5.png)
コンテンツの内容を対象のユーザー向けに調整して[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/02b71c22800c17963f5381bc8b4a2a3a.png)
### サブサイトのAPIを確認する
サブサイトの追加時にフロントエンド共有へチェックを入れていると、設定したフロントエンドのURLが自動的にアカウント設定と、APIのCORS設定に追加されます。  
CORS設定の確認をするため、サブサイトのAPIから[B2Bサービスページ]のAPIをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6a593dc2829488355c0d0313ca92c5a5.png)
[CORSを設定する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3446b36ed523f5abf463c22a5bd028c8.png)
CORS_ALLOW_ORIGINSにフロントエンド共有で選択したフロントエンドURLが追加されていることを確認できました。    
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c776251d0afa78f9c744493828351e11.png)
以上で設定が完了となりますので、フロントエンドから動作の確認をしてみます。  

## サイトキーによって表示が変わることを確認する
作成したサイトにアクセスし、入力するsitekeyによって表示されるコンテンツが変わることを確認します。  

サイトキー=sample-b2b-service：  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/63791a491d9b40a5f716faecd30cadd6.gif)

サイトキー=sample-b2b-service-001：  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c623348fb8f50cca142dc1efaa5d6f2.gif)

以上で、フロントエンドを共通にして、バックエンドをお客様毎に切り替える機能を構築できました。  
このように追加したお客様専用ページに、メール送信の機能や、コンテンツの投稿機能、コメント機能などを実装することで、B2B向けサービスをKurocoで構築できます。  

今回は管理画面からコンテンツの内容を調整しましたが、APIを利用してユーザー自身でコンテンツの追加・更新ができるように実装できます。  
また、サイトの追加自体をAPI利用により実行も可能です。

:::tip
サブサイトのKuroco利用料金はメインサイトにまとめて請求されます。  
:::

## 関連ドキュメント
- [サイト一覧](/ja/docs/management/site-list/)
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [Kurocoに登録したコンテンツを複数のサイトから利用できますか](/ja/docs/faq/can-the-content-registered-in-kuroco-be-used-from-multiple-sites/)
- [スーパーユーザーはサブサイトにもログインできますか？](/ja/docs/faq/can-superuser-also-log-in-to-sub-sites/)


---

# 別サイトで使用しているドメインをKurocoに切り替える際の手順

> 元ページ: `tutorials/transferring-your-domain-from-another-site-to-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/transferring-your-domain-from-another-site-to-kuroco/

現在別のサイトで使用している使用しているドメインを、Kurocoで作成したサイトに切り替える手順を説明します。

## ドメイン切り替え手順
### 1. Kurocofrontで独自ドメインを登録する

[環境設定] -> [独自ドメイン/TLS証明書]をクリックし、「独自ドメイン」のテキストフィールドに利用するドメインを入力します。

:::tip
最後尾にスラッシュやディレクトリなどは必要ありません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44b6ce3e459e41ca43678a833a55a826.png)

入力後、「追加する」ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/528ce38cba2754e3b78d186c588b4837.png)

### 2. CNAMEレコードを設定する。
独自ドメインを追加すると、DNSレコードの確認ができるようになります。  
KurocoFrontの画面より、「ドメイン所有権の確認」のDNSレコードを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2411600ab988807b49eca22c46378d18.png)

表示されている内容に従い、CNAMEの設定をしてください。

:::danger
このステップではまだ「ドメインを利用する為のDNSレコード」は設定しません。  
「ドメイン所有権の確認」のDNSレコードのみ設定してください。
:::

参考) DNSレコードの設定は取得したドメイン会社により異なります。詳細な設定方法は取得したドメイン会社にてご確認ください。
- [お名前.com Navi ネームサーバー/DNSについて](https://www.onamae.com/guide/p/70)
- [Google Domainsヘルプ ドメイン ネームサーバーの管理](https://support.google.com/domains/answer/3290309?hl=ja)

### 3. アカウント設定でフロントエンドドメインを変更する
フロントエンドドメインを独自ドメインに変更します。  
[環境設定] -> [アカウント設定]をクリックし、アカウント設定画面を表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/305d23c42fea6e17ba789407fa9fdd74.png)

「フロントエンドドメイン」に設定した独自ドメインが表示されるので、チェックを入れ「更新する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b8af1de9171b110601abf68645b8de9.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cab5b76eda4ff4cdc2118aca85f004f.png)

なお、現時点では「ドメインを利用する為のDNSレコード」を変更していないため、独自ドメインはまだKurocoで作成したサイトの表示にはなりません。独自ドメインにアクセスしても、元のサイトにアクセスされます。

### 4. 独自APIドメインを登録する(必要な方のみ)

:::tip
こちらは下記に該当する方のみ対応が必要となります。  
[API] -> [セキュリティ]でCookieを利用している  
上記に該当しない場合は、[5. CORSに独自ドメインを追加する](#5-corsに独自ドメインを追加する)まで進んでください。
:::

---
次に独自APIドメインを登録します。  

[環境設定] -> [独自ドメイン/TLS証明書]より「独自ドメイン」のテキストフィールドに利用するドメインを入力します。

:::tip
最後尾にスラッシュやディレクトリなどは必要ありません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/328db4c19a7b8cbe76a549a01597ad8d.png)

また、独自APIドメインは、独自ドメインとサブドメイン違いで設定する必要がありますのでご注意ください。  

例)  
- 独自ドメイン：`https://www.example.com`
- APIドメイン：`https://api.example.com`

独自APIドメインを登録すると、DNSレコードが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/315f1b83b987783ce37f42edb91a8cc6.png)

表示されている内容に従い、CNAMEまたはAレコードの設定をしてください。

設定変更後、APIドメインを変更します。
[環境設定] -> [アカウント設定]をクリックし、アカウント設定画面を表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a31068a1ee6b74b9f4c17911363b517.png)

「APIドメイン」より、設定したAPIドメインにチェックを入れ、「更新する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/98511da63d88255b7ac1e800dfb103ee.png)

### 5. CORSに独自ドメインを追加する
APIのCORS設定に独自ドメインを追加します。
[API]よりご利用のAPIを選択し、「CORSを設定する」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ae5ac217eb9ee29f1dfd5656c2322fe7.png)
[CORS_ALLOW_ORIGINS]より、「Add Origin」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b8eaf84945f48b74ae372ddd47060c28.png)
するとテキストフィールドが追加されます。  
テキストフィールドに独自ドメインを入力し、「Save」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f6ce21e057f8e97490ec7fe9b39867c3.png)
以上でCORSの設定完了です。

### 6. ドメインを直接記述しているファイルを修正する
連携しているGitHubのリポジトリのファイルにドメインを直接記述している場合、ファイルを修正します。  

**GitHub Actions用YAMLファイル**  
GitHub Actions連携のYAMLファイル内にはドメインが記載されますので、独自ドメイン設定後はファイルを修正してください。

[外部システム連携] -> [GitHub]をクリックし、「リポジトリ」よりYAMLファイルをコピーしてご利用ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/78420b89898335775930b8793dd28789.png)

:::info
[GitHubからKurocoFrontへソースをデプロイする方法 4. .github/workflows にYAMLファイルを配置する](/ja/docs/tutorials/connect-to-github-with-kuroco-front/#4-githubworkflows-にyamlファイルを配置する)
:::

**.envファイル**  
.envファイルにルートドメインやAPIドメインを直接記述している場合は修正してください。

### 7. hostsファイルを修正し、DNS変更前にサイトの表示を確認する
DNSを切り替える前にサイトの表示を確認したい場合、hostsファイルを変更することによって確認が可能です。  
必須の作業ではありませんが、DNS変更の前に表示の確認が必要な場合は下記を参考にしてください。

hostsファイルに記載するAレコードは、[環境設定] -> [独自ドメイン/TLS証明書]の「ドメインを利用する為のDNSレコード(CNAMEが利用できない場合)」をご確認ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/972a8d6a8359e3fae9d4a7a2f2b9977a.png)

なお、上記画面ではAレコードが4件表示されますが、hostsには1件のみ記載すれば確認可能となります。

```hosts title="hosts"
151.101.XX.XXX www.example.com
```

:::caution
表示の確認後、hostsの設定は必ず元に戻してください。
:::

:::tip
サイトがうまく表示されない場合は下記をご確認ください。  
- [独自ドメインを設定しましたがサイトが表示できません。何を確認すれば良いでしょうか？](/ja/docs/faq/setting-up-a-custom-domain/)
:::

### 8. ドメインを利用する為のDNSレコードを設定する
最後にDNSレコードを変更します。  
[環境設定] -> [独自ドメイン/TLS証明書]をクリックし、「ドメインを利用する為のDNSレコード(推奨)」または「ドメインを利用する為のDNSレコード(CNAMEが利用できない場合)」を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c8267ffd6320515407bae03986ac9d4.png)

表示されている内容に従い、CNAMEまたはAレコードの設定をしてください。 

参考) DNSレコードの設定は取得したドメイン会社により異なります。詳細な設定方法は取得したドメイン会社にてご確認ください。
- [お名前.com Navi ネームサーバー/DNSについて](https://www.onamae.com/guide/p/70)
- [Google Domainsヘルプ ドメイン ネームサーバーの管理](https://support.google.com/domains/answer/3290309?hl=ja)

DNSが反映されると、独自ドメインにアクセスでKurocoのサイトが表示されるようになります。左サイドバーの「サイトを表示」をクリックすると、独自ドメインが適応されたサイトを表示します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9912852dc2324076b459e8757ebc84a.png)

## 関連ドキュメント
独自ドメイン、KurocoFrontに関するドキュメントです。併せてご確認ください。

- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [独自ドメインを設定しましたがサイトが表示できません。何を確認すれば良いでしょうか？](/ja/docs/faq/setting-up-a-custom-domain/)


---

# KurocoFrontで独自ドメインを利用する手順

> 元ページ: `tutorials/using-a-custom-domain-name-on-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/
> 概要: KurocoFrontへ独自ドメインを適用する方法を紹介します。独自ドメインを適用するには、そのドメインに対してDNSレコードを設定する権限が必要になります。

KurocoFrontへ独自ドメインを適用する方法を紹介します。    
独自ドメインを適用するには、そのドメインに対してDNSレコードを設定する権限が必要になります。
また、TLS証明書の設定までが必須でTLS証明書の持ち込みはできません。

## 独自ドメイン利用手順

### 1. 独自ドメインを入力
[環境設定] -> [独自ドメイン/TLS証明書]をクリックし、「独自ドメイン」のテキストフィールドに利用するドメインを入力します。

:::tip
最後尾にスラッシュやディレクトリなどは必要ありません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4993b3f8ef0f8ea33601325a398c0eb5.png)

入力後、「追加する」ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/528ce38cba2754e3b78d186c588b4837.png)

:::danger 要注意
独自ドメインは一度追加すると変更ができません。間違って入力してしまった場合は、サポート宛にご連絡をお願いいたします。    
[フォームより問い合わせをする](https://kuroco.zendesk.com/)
:::

暫くすると、以下のように設定するべきDNSレコードが表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fbe71e7ba9c3ed5c6aa8328be7548901.png)

### 2. DNSレコードの設定
次にDNSレコードの設定をします。  
表示されている内容に従い、CNAME、Aレコードを設定してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fbe71e7ba9c3ed5c6aa8328be7548901.png)

参考) DNSレコードの設定は取得したドメイン会社により異なります。詳細な設定方法は取得したドメイン会社にてご確認ください。
- [お名前.com Navi ネームサーバー/DNSについて](https://www.onamae.com/guide/p/70)
- [Google Domainsヘルプ ドメイン ネームサーバーの管理](https://support.google.com/domains/answer/3290309?hl=ja)

DNSレコードをセットすると以下のようにOKが表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8dfa4107bf5a906d6054b5b6e0c8f67.png)

:::tip
DNSレコードの反映およびステータスの更新には時間がかかることがあります。OKが表示されない場合は、時間を置いてから「リロードする」ボタンを押して確認してください。
:::

:::info
独自ドメイン/TLS証明書 の ドメイン所有権の確認 は、dns.google.com を利用してDNSレコードの確認を行っています。  
下記の画面から DNSレコードのキャッシュのクリアが出来るので、お急ぎの場合はこちらをお試しいただくと早く更新されることがあります。  
https://developers.google.com/speed/public-dns/cache?hl=ja  

Doman Name:`_acme-challenge.CUSTOM_DOMAIN`  
RR Type:`CNAME`
:::

### 3. フロントエンドドメインの変更
次にフロントエンドドメインを独自ドメインに変更します。  
[環境設定] -> [アカウント設定]をクリックし、アカウント設定画面を表示します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/305d23c42fea6e17ba789407fa9fdd74.png)

「フロントエンドドメイン」に設定した独自ドメインが表示されるので、チェックを入れ「更新する」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b8af1de9171b110601abf68645b8de9.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cab5b76eda4ff4cdc2118aca85f004f.png)

これで独自ドメインが利用できるようになりました。
左サイドバーの[サイトを表示]をクリックすると独自ドメインが適応されたサイトを表示します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/642009338d99503898995fe8eed1a3d0.png)

:::tip
TLS証明書がCDNに反映し終わるまで、10数分程度かかる場合があります。
:::

### 4. YAMLファイルの修正
KurocoFrontを利用していてYAMLファイルを作成している場合、YAMLファイルの修正が必要となります。

[外部システム連携] -> [GitHub]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7553b3e477fd07848ee5a61724007648.png)

「リポジトリ」の「GitHub Actions workflow file フロントエンド ドメイン」の内容を確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c19058aac0fedbaadbfb88ba3b33111.png)

webhookの箇所にドメインの記載箇所があり、こちらが独自ドメインに変更されています。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50586339002aa7388d138b3f4cd4faf4.png)

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/2a2851760e638026dd43512683c53a7f.png)
ご自分のYAMLファイル内のdomainの箇所を、設定した独自ドメインに修正してください。  
なお、YAMLファイル内にdomainの指定設定は２箇所あります。２箇所修正をお願いします。

:::tip
KurocoFrontの設定方法は、[GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)を参考に設定してください。
:::

## 関連ドキュメント
独自ドメイン設定がうまくできない場合、下記をご確認ください。

- [独自ドメインを設定しましたがサイトが表示できません。何を確認すれば良いでしょうか？](/ja/docs/faq/setting-up-a-custom-domain/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)

独自APIドメインの設定方法は下記をご確認ください。
- [KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)

wwwなしからのリダイレクト設定は下記をご確認ください。
- [独自ドメインでwwwなしでもサイト表示できますか？](/ja/docs/faq/can-i-display-my-site-on-custom-domain-without-www/)


---

# KurocoFrontで独自APIドメインを利用する手順

> 元ページ: `tutorials/using-your-own-api-domain-with-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/
> 概要: KurocoFrontへ独自APIドメインを適用する方法を紹介します。APIドメインを適用するには、そのドメインに対してDNSレコードを設定する権限が必要になります。

KurocoFrontへ独自APIドメインを適用する方法を紹介します。    
独自APIドメインを適用するには、そのドメインに対してDNSレコードを設定する権限が必要になります。

## APIドメイン利用手順

### 1. APIドメインを入力
[環境設定] -> [独自ドメイン/TLS証明書]をクリックし、「独自APIドメイン」のテキストフィールドに利用するドメインを入力します。

:::tip
最後尾にスラッシュやディレクトリなどは必要ありません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/328db4c19a7b8cbe76a549a01597ad8d.png)

入力後、「追加する」ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ebfe4afe6e24be9a3e754de158712ae.png)

:::danger 要注意
独自APIドメインは一度追加すると変更ができません。間違って入力してしまった場合は、サポート宛にご連絡をお願いいたします。    
[フォームより問い合わせをする](https://kuroco.zendesk.com/)
:::

暫くすると、以下のように設定するべきDNSレコードが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/559e84909a8e528acb16a971f3cd600f.png)

### 2. DNSレコードの設定
次にDNSレコードの設定をします。表示されている内容に従い、CNAME/Aレコードを設定してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7e335a3fb53ff463986c9ee8d070d8fc.png)

:::tip
DNSレコードの設定は取得したドメイン会社により異なります。詳細な設定方法は取得したドメイン会社にてご確認ください。  
-[お名前.com Navi ネームサーバー/DNSについて](https://www.onamae.com/guide/p/70)  
-[Google Domainsヘルプ ドメイン ネームサーバーの管理](https://support.google.com/domains/answer/3290309?hl=ja)  
:::

DNSレコードをセットすると、ドメイン所有権の確認にOKが表示され、しばらく時間がたつとTLS証明書が発行されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dcda60ce31fe04ed64c9145d356185d6.png)

:::tip
DNSレコードの反映およびステータスの更新には時間がかかることがあります。OKが表示されない場合は、時間を置いてから「リロードする」ボタンを押して確認してください。
:::

:::info
独自ドメイン/TLS証明書 の ドメイン所有権の確認 は、dns.google.com を利用してDNSレコードの確認を行っています。  
下記の画面から DNSレコードのキャッシュのクリアが出来るので、お急ぎの場合はこちらをお試しいただくと早く更新されることがあります。  
https://developers.google.com/speed/public-dns/cache?hl=ja  

Doman Name:`_acme-challenge.api.CUSTOM_API_DOMAIN`  
RR Type:`CNAME`
:::

### 3. APIドメインの変更
TLS証明書が発行されたら、APIドメインを先ほど設定した独自ドメインに変更します。  

:::caution
デフォルトのAPIドメイン(`kuroco.app`)は使用できなくなります。既に公開済みのサイトでAPIドメインを変更する場合は、リクエスト先の変更とタイミングを合わせて実施ください。
:::

[環境設定] -> [アカウント設定]をクリックし、アカウント設定画面を表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/170770ebee636e370c9ad40e4df3482f.png)

「APIドメイン」に設定した独自APIドメインが表示されるので、チェックを入れ「更新する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/98511da63d88255b7ac1e800dfb103ee.png)

これで独自APIドメインが利用できるようになりました。

### 4. APIドメインの記述箇所の変更
フロントエンドなどで、デフォルトのAPIドメインの記述がある場合は、独自APIドメインに変更します。  
APIドメインの記述箇所は実装によりますが、以下に記述されている場合が多いので参考にしてください。  

- GitHubシークレット
- .envファイル
- vueファイル

## 関連ドキュメント
独自ドメインの設定方法は下記をご確認ください。
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
