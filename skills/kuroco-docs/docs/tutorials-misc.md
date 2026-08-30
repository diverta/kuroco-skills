# Kurocoドキュメント: チュートリアル / その他

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Kurocoビギナーズガイド（`beginners-guide`）
- APIにアクセス元の国や都道府県を追加する（`how-to-add-region-data`）
- Kuroco利用料の最適化（`how-to-optimize-kuroco-usage-costs`）
- 本番環境のデータを検証環境に同期するボタンを設置する（`place-a-button-to-synchronize-production-data-with-the-validation-environment`）
- Kurocoを利用したプロジェクトの進行イメージ（`starting-a-project-on-kuroco`）


---

# Kurocoビギナーズガイド

> 元ページ: `tutorials/beginners-guide` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/beginners-guide/
> 概要: 本チュートリアルでは初めてKurocoを利用する方向けに、フリートライアル申込からNuxt.jsを利用したサイトの表示までの手順を説明します。

## はじめに
KurocoはAPIファーストのヘッドレスCMSであるため、フリートライアルに申し込んだだけではサイトの表示はされません。  
本チュートリアルでは初めてヘッドレスCMSのKurocoを利用する方向けに、フリートライアル申込からサイトの表示までの手順を説明します。

ここでは例として、サービスの紹介サイトを下記の構成で作成します。  

|項目   |サービス  |用途|
| :--- | :--- | :--- |
|バックエンド|[Kuroco](https://kuroco.app/ja/)|コンテンツ(画像やテキスト、メンバー情報等)を管理し、APIを作成します。|
|ホスティング|[KurocoFront](/ja/docs/about/kurocofront/)|GitHubで管理したコードをサーバーにビルドし、ユーザーがブラウザから表示できるようにします。|
|ソースコード管理|[GitHub](https://github.com/)|フロントエンドを表示するためのソースコードを管理します。|
|フロントエンド|[Nuxt.js](https://nuxtjs.org/ja/)|サイトを表示するフロントエンド部分のコードを記述します。|

今回はヘッドレスCMSの理解を目的としてトップページのみの作成としますが、慣れてきたらフォームやブログページ、多言語対応等、ドキュメントを見ながら追加してみてください。

## NuxtプロジェクトをKurocoFrontへデプロイする
### Kurocoのフリートライアル申込
早速、[Kurocoのフリートライアル](https://kuroco.app/ja/free_trial/) に申し込みます。  
リージョンを選択し、サイトキーはお好きな文字列を入力ください。  
ここではリージョンを「アジア(東京)」、サイトキーを「sample-service-site」としました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/87ee109095596f1174252d60583eb8e8.png)
登録したメールアドレスに、「Kurocoサイト登録が完了いたしました！」のメールが届きます。  
メールに記載されたURLをクリックするとKurocoのログイン画面が表示されるので、登録したメールアドレスとパスワードでログインします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/faa1039782ce49ac43efa0fbf71ba1fb.png)
ログインすると、Kuroco管理画面が表示されます。  
管理画面に[サイトを表示]のリンクがありますが、現時点ではクリックすると「404 Not Found (DEPLOYMENT NOT FOUND)」が表示されます。こちらはフロントエンドが作られていないためなので問題ありません。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/94892810d6231a4056868e7b1a7fc013.png)

Kurocoの管理画面は一旦このままで、次にフロントエンドの構築に進みます。 

### 事前準備
Nuxt.jsはnpxのコマンドを使ってインストールしていきます。  
ターミナルを開き、`npx -v`のコマンドでバージョンの確認ができますので、インストールされていない場合は[node.js](https://nodejs.org/ja/download/)をインストールしてください。  

また、[GitHub](https://github.com/)のアカウントが必要になるので、持っていない場合は登録ください。  

### Nuxt.jsインストール

:::info
本チュートリアルではNuxt.js のバージョン v2.15.8 を利用しています。
:::

準備ができたらプロジェクトを管理する任意のディレクトリで下記のコマンドを実行します。  
`sample-service-site`の部分はお好きな名前に変更してください。

```
npx nuxi@latest init sample-service-site
```

次に、複数の質問が聞かれるので回答します。 今回は下記のように入力しました。

```
Which package manager would you like to use?
npm
Initialize git repository?
Yes
```
全ての質問に回答するとsample-service-site ディレクトリが作成されますので、作成されたディレクトリに移動します。

```
cd sample-service-site
```

下記実行し、インストールしたNuxt.jsの表示を確認します。

```
npm run dev
```

ターミナルに表示されたURL `http://localhost:3000/` にアクセスすると、下記の画面が確認できます。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6cdb1560be6da8dcc2b5fef9632cd7a2.png)

以上でNuxt.jsのインストールとローカル環境での表示ができました。続いてこちらのページをweb上で表示できるようにしていきます。  

### GitHubリポジトリの準備
[GitHub](https://github.com/)にログインして、リポジトリを作成します。リポジトリの準備ができたら下記のコマンドを順に実行します。  

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/GitHubユーザー名/リポジトリ名.git
git push -u origin main
```

:::note
Nuxt.jsをインストールしたディレクトリのまま実行するように注意してください。  
:::

:::caution
`GitHubユーザー名/リポジトリ名.git`の部分はご自身のアカウントの情報を使用してください。
:::

こちらの手順でNuxt.jsをインストールしたフォルダをGit管理化して、リモートリポジトリにファイルをプッシュできました。 

### GitHubとKurocoの連携
続いてGitHubとKurocoを連携します。  
Kurocoの管理画面から[外部システム連携] -> [GitHub]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7553b3e477fd07848ee5a61724007648.png)

[GitHubリポジトリと接続する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/0962196e6c3f9d4592902a67fa7615f3.png)
GitHubへログインが求められますので、ログインをします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/214c1957e75be4de2ea7bc01d10499ab.png)
ログインするとGitHubの画面が表示されます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d42942104b7b668e7d80c44696db4429.png)
「Repository access」より先ほど作成したリポジトリを選択します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/afef17946cbde0c9d11433dcb08564a4.png)
:::tip
リポジトリ接続設定は後から変更が可能です。１つのアカウントで複数のKurocoを利用する場合は、KurocoのGitHub Appsは1つですので、ここで複数のリポジトリを選択することになります。  
:::

:::tip
接続できるリポジトリは管理者権限を持っているリポジトリのみになりますので、ご注意ください。  
:::

リポジトリを選択したら、「Save」をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1baf2798ac40f953e489b09040a5d1ce.png)
再度Kurocoへのログインを求められますので、ログインをします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/26486a7bc02153a291f73cb352f90284.png)
接続が完了すると、KurocoFrontの画面に遷移するので、プルダウンから対象のリポジトリを選択して[更新する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/10eff1221229bb98277274167f6dd729.png)
以上で、GitHubとKurocoの連携は完了です。

### デプロイ
GitHubで管理しているコードをKurocoFrontにデプロイすることで、`https://サイトキー.g.kuroco-front.app/`のURLでwebサイトの表示ができます。  

kuroco_front.json とYAMLファイル の2ファイルをNuxt.jsプロジェクトに追加します。  

|ファイル名   |保存するディレクトリ  |説明  |
| :--- | :--- | :--- |
|`kuroco_front.json`|`/public`|リダイレクトやBasic認証等の設定をするKurocoFrontを利用するために必要なJSONファイル|
|`build.yml`|`/.github/workflows`|GitHub Actionsのワークフロー設定を定義するためのファイル(YAMLファイル)|

それぞれファイルの中身は下記のようにします。

#### **/public/kuroco_front.json**
```json title="/public/kuroco_front.json"
{
    "rewrites": [
        {
          "source": ".*",
          "destination": "/index.html"
        }
      ],
    "redirects": [],
    "basic":[],
    "ip_restrictions":[]
}
```
Basic認証やIPアドレス制限等の設定は`kuroco_front.json`で行います。  

:::tip
Kuroco_front.jsonについての詳細は、FAQ -> [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/) をご参照ください。
:::

#### **/.github/workflows/build.yml**  
ファイルの中身はKurocoFront画面のリポジトリフィールドで、Frameworkを`nuxt3`に設定した内容をコピーして入力します。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/0d86d6f1f58a8c634a8bd5d63c010db1.png)

GitHubのブランチが`main`以外の場合や、独自ドメインを利用するような場合は、ビルドコマンドやブランチ名などを調整しますが、本チュートリアルの場合はこのまま使用できます。  

:::tip
YAMLファイルについての説明や、書き方については下記ドキュメントをご確認ください。<br/>- [GitHub Docs GitHub Actions について学ぶ](https://docs.github.com/ja/actions/learn-github-actions)<br/>- [GitHub Docs GitHub Actionsのワークフロー構文](https://docs.github.com/ja/actions/reference/workflow-syntax-for-github-actions)
:::

ファイルの追加ができたら、変更をGitHubにプッシュします。プッシュするとGitHubActionが実行され、ビルド&デプロイされます。  

ビルド&デプロイ完了後に、再度管理画面の[サイトを表示]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/94892810d6231a4056868e7b1a7fc013.png)

今度は「404 Not Found (DEPLOYMENT NOT FOUND)」ではなく、先ほどローカル環境で確認したNuxt.jsプロジェクトの初期の表示が確認できます。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6cdb1560be6da8dcc2b5fef9632cd7a2.png)
以上でNuxt.jsの最初のページをwebサイトで表示できました。  

Kurocoでコンテンツの追加をし、Nuxt.jsでコンテンツの表示やデザインの調整をすることでサイトの構築ができます。  

## Kurocoで管理したコンテンツを表示する
サイト構築の準備ができましたので、Kurocoでコンテンツの追加と、Nuxt.jsでKurocoのコンテンツの表示の作業をしていきます。  

### コンテンツの登録
まずはKurocoの管理画面でコンテンツを定義します。  
[コンテンツ定義]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a91b31af30504a5fb6755030220422f0.png)

[追加]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fc79883afcc9ae8482db4aaa19c3d141.png)

コンテンツ定義編集画面でお好きな名前を入力し、コンテンツの項目を設定し、[追加する]をクリックします。  
今回は下記のように設定しています。

**全般**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0472bfa14e49982956e74a5334a2b17d.png)

**項目設定**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53f59bceba7ca013b29650576f9cc677.jpg)

:::tip
コンテンツのグループ化は項目のドラッグ&ドロップで実行します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57b1c28e7f863a65f8d50aab5a2fe723.gif)
:::

以上でコンテンツの内容を定義できましたので、次はコンテンツを追加していきます。  
[コンテンツ]->[事業紹介]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/65de8b0ed30f53f7b4081c91364f7bfb.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0cd90b2f672c396fe9e6fdc1290940a2.png)

先ほど定義したコンテンツの項目が表示されますので、画像やテキストなど、コンテンツを入力して[追加する]をクリックします。  
今回は下記のように登録しています。

<a href="https://diverta.gyazo.com/a5cf37e536c5660c8459acf3129e261a" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://t.gyazo.com/teams/diverta/a5cf37e536c5660c8459acf3129e261a.png" alt="Image from Gyazo"/></a>

追加したコンテンツ定義のID(7)とコンテンツのID(3)は後ほど利用するのでメモしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0a6fc1cf4c2d064978fd94fb09e4ab9.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f5e0abe859502f453307cf761de09d96.png)

### APIの登録
続いてAPIの登録をします。 
Kurocoの管理画面から[API]->[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8c4d0feec6c71fdd343c4a161415165.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/812f341dd9c83c52105da22bf18a5fa9.png)

タイトル、版、説明を入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d87d6fc076c17a1f908a63bca84f9646.png)

追加したAPIに遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6dda0a93616285f02f4af2bf22019b00.png)

続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/baa66dc6e3cda1184cfea62afce306c3.png)
[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
:::caution
APIのセキュリティにCookieを利用した状態で、今後もし独自ドメインを適用する場合は、フロントエンドドメインとAPIドメインを準備する必要があります。  
(WebブラウザによってはサードパーティーCookieが利用できず、ログインできない可能性があるため。)  
参考記事:[Google、ChromeでのサードパーティーCookie廃止を2023年まで延期）](https://www.itmedia.co.jp/news/articles/2106/25/news067.html)
:::

続いて、CORSの設定をします。   
[CORSを設定する] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/55acc9f3c6c67a40fef57c324d8ebc48.png)
CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000/`
- フロントエンドドメイン (ここでは`https://sample-service-site.g.kuroco-front.app/`)

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET
- POST
- OPTIONS

設定できたら[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/7be9be42bfd7df3edf2b7d2f25b56e93.png)
次に先ほど作成したコンテンツ「事業紹介」を取得するエンドポイントを作成します。  
[新しいエンドポイントの追加]をクリックします。    
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc5954932ba41cbeda755dbfb80add84.png)
下記のように設定し、[追加]をクリックします。

| 設定項目 | 設定 ||
| :--- | :--- | :--- |
|パス|service||
||有効/無効|有効|
|モデル|カテゴリー|コンテンツ|
||モデル|Topics|
||オペレーション|Details|
|ext_group|チェックを入れる||
|topics_group_id|作成したコンテンツ定義のグループID(7)||

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d44d94935a863cfecd69d3fa5e0cba50.jpg)

以上で、Kuroco側の設定は完了です。  
作成したエンドポイントにアクセスすると、エンドポイントからのレスポンスが確認できます。  
今回の場合は{topics_id}の部分にコンテンツのIDを入力して、下記のURLで確認ができます。  
`https://sample-service-site.g.kuroco.app/rcms-api/3/service/3`

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/efa03ca32459bf8ed0963a259ab35e72.png)
こちらのレスポンスを取得して表示するようにフロントエンドの記述を書くことでサイトを構築できます。  

:::tip
URLは管理画面URL(`sitekey.g.kuroco-mng.app`)やフロントエンドドメイン(`sitekey.g.kuroco-front.app`)ではなく、APIドメイン(`sitekey.g.kuroco.app`)になります。
:::

:::tip
APIレスポンスを確認する方法は下記のチュートリアルをご参照ください。<br/>- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
:::

### nuxt.config.tsファイルの調整
フロントエンドの具体的なページの記述を始める前に、KurocoのAPIドメインを登録します。  
また、KurocoFrontで静的にホスティングするために、サーバでの動的レンダリング機能をオフにしておきます。  

`nuxt.config.ts` の全文は下記のようになります。

```js title="nuxt.config.ts"
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  runtimeConfig: {
      // Public keys that are exposed to the client
      public: {
          apiBase: 'https://sample-service-site.g.kuroco.app'
      }
  },
})
```

### app.vueの調整
デフォルトではNuxt3のウェルカムページが表示されるように設定されているので、pagesディレクトリのページが表示されるようにapp.vueを以下のように更新します。

```markup title="app.vue"
<template>
  <div>
    <NuxtPage />
  </div>
</template>
```

### index.vueの調整
次に、フロントエンドの記述を調整します。pagesのディレクトリにindex.vueを以下の内容で作成してください。  

`<script>` `</script>`の部分で、エンドポイントからのレスポンスを得て、`<template>` `</template>`の部分でレスポンスの内容を表示するhtmlを記述しています。 

`/rcms-api/3/service/3`の部分はご自身のエンドポイントのURLに変更してください。  

```markup title="/pages/index.vue"
<template>
    <div>
        <img :src="response.details.ext_1.url" width="800">
        <div>{{ response.details.ext_2 }}</div>
        <div>{{ response.details.ext_3 }}</div>

        <div v-for="n in response.details.ext_4" :key="n.slag">
            <img :src="n.ext_4.url" width="400">
            <div>{{ n.ext_3 }}</div>
            <div>{{ n.ext_5 }}</div>
            <div>{{ n.ext_6 }}</div>
        </div>
    </div>
</template>

<script setup>
const config = useRuntimeConfig();

const { data: response } = await useFetch(
    `${config.public.apiBase}/rcms-api/3/service/3`,
    {
        credentials: 'include',
    }
);
</script>
```

ターミナルで`npm run dev`を実行し、
`http://localhost:3000/`にアクセスしてローカル環境で表示の確認をすると、下記のようにKurocoのコンテンツ表示が確認できます。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/2fd084ffcf40abe94d38248fa960a3b7.png)

:::tip
Kurocoをお申込みいただいたタイミングによっては、各項目のレスポンスが`ext_1`ではなく、`ext_col_01`となる場合があります。  
うまくいかない場合は Swagger UIでレスポンスをご確認ください。
:::

### デプロイ
ローカル環境での変更をGitHubにpushすると、フロントエンドドメインでの表示にも反映されます。

`/pages/index.vue`の変更をGitHubにpushします。  
デプロイが完了すると、下記のようにWebサイト上でも表示の確認ができます。 

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/69bbd996cd6047d41f607fcdefb0d746.jpg)

以上でKurocoのコンテンツの内容をAPIで出力・取得し、webサイト上に表示できました。  

## デザインを調整する
最後にwebサイトのデザインの部分を調整します。  
こちらは完全にフロントエンドでの作業になるので、普段利用しているCSSフレームワークを利用したり、外部のサービスと連携したり、ご自由に構築していただくことができます。  

本チュートリアルでは`index.vue` でスタイルの調整をして次のようにしました。  

```markup reference title="/pages/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/beginners-guide.vue
```

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/2a16294ccf428f758747337e22dc6791.png)
https://sample-service-site.g.kuroco-front.app/


## 参考
本チュートリアルではヘッドレスCMSの理解を目的として、トップページのみ作成をしました。  
以下のドキュメントを参考に是非他のページも作成してみてください。  

- [KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [KurocoとNuxt.jsで、コンテンツ一覧ページにページネーションを実装する](/ja/docs/tutorials/splitting-the-contents-list-into-multiple-pages)
- [KurocoとNuxt.jsで、多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [KurocoとNuxt.jsで、プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)

## 関連ドキュメント
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# APIにアクセス元の国や都道府県を追加する

> 元ページ: `tutorials/how-to-add-region-data` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-add-region-data/

カスタム処理にあるSmartyの定数としてAPIのリクエスト元のユーザーの地理情報が取得できます。
 
## アクセス元として利用できるコード
```{$smarty.const.GEO_COUNTRY_CODE}``` ISO 3166-2に基づく国のコード。日本の場合はJPになります。  
```{$smarty.const.GEO_REGION}``` ISO 3166-2に基づくの区分コード。日本の場合は都道府県などの番号が入ります。例)東京都:13  
```{$smarty.const.GEO_CONN_SPEED}``` broadband, cable, dialup, mobileなどの接続環境のコードが入ります。  

## profileを返すAPIに地理情報を追加する

**1. カスタム処理に以下のコードを記述します** 
```
{assign_array var=processed_json values=""}
{assign var=processed_json value=$json}
{assign var=processed_json.geo_country_code value=$smarty.const.GEO_COUNTRY_CODE}
{assign var=processed_json.geo_region value=$smarty.const.GEO_REGION}
{assign var=processed_json.geo_conn_speed value=$smarty.const.GEO_CONN_SPEED}
```
$jsonは下記でセットすると、APIのPostProcessでの利用できるAPIの出力結果です。  
$processed_jsonは、PostProcessでの変換後の出力結果を投入できます。


**2. APIのPostProcessに上記のカスタム処理をセット** 

**3. API出力に例えば、以下のようにAPIのリクスト元の地理データが追加されます**  
```
{"name1":"加藤",
"name2":"ケンタ",
"member_id":96,
"group_ids":{"1":"管理者","110":"一般会員"},
"shash":"ca64ddf281bc0168626c2706fde81126",
"expiresAt":1628260083,
"geo_country_code":"JP",
"geo_region":"13",
"geo_conn_speed":"broadband"
}
```

## 注意
これらの地理データはIPアドレスベースで分類されていますが、正確性を保証するものではありません。あくまでも目安としてご利用ください。

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [API 後処理](/ja/docs/management/api-postprocessing/)
- [後処理](/ja/docs/reference/post-processing/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)
- [ユーザーのIPアドレスを取得できますか？](/ja/docs/faq/can-i-obtain-the-users-ip-address/)


---

# Kuroco利用料の最適化

> 元ページ: `tutorials/how-to-optimize-kuroco-usage-costs` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/
> 概要: Kuroco利用料が高くなった時に確認すべき項目と、APIリクエスト削減、キャッシュ比率向上、KurocoFront容量削減の具体的な方法について説明します。

Kuroco利用料が高くなった時に、効果的に費用を削減するための手順を説明します。以下の流れで対策を実施することで、利用料を最適化できます。

## 利用料を確認する

まず、現在の利用状況と費用内訳を確認します。

### 確認手順

1. [環境設定] -> [利用状況]をクリック  
2. 「管理サイト全体の費用」で項目別の費用を確認  
3. 「コストチャート」で費用の推移を確認  
  (定額契約の場合、コストチャートは表示されません。)
4. 「日別利用量」で詳細な利用状況を確認  

### 主要な費用項目

日別利用量では以下の項目毎に利用料が確認できます。  
それぞれの項目に対して、費用削減の例を紹介しますので、参考に調整をしてください。

- [キャッシュされたAPIリクエスト](#キャッシュ比率を上げる)
- [APIリクエスト](#apiリクエストを減らす)
- [API転送量](#api転送量を減らす)
- API追加処理時間
- [KurocoFront転送量](#kurocofront転送量を減らす)
- [KurocoFiles転送量](#kurocofiles転送量を減らす)
- メール
- AI処理ユニット
- バッチ処理時間
- [DBファイル容量](#dbファイル容量を減らす)
- [ファイル容量](#ファイル容量を減らす)
- [KurocoFrontファイル容量](#kurocofrontファイル容量を減らす)
- ログ容量
- [バックアップファイル容量](#バックアップファイル容量を減らす)

:::tip  
[オペレーション]->[ログ管理]で各ログを確認し、より詳細な分析が可能です。
:::

## Kuroco利用料の最適化を行う
### キャッシュ比率を上げる
キャッシュされたAPIリクエストは通常のAPIリクエストより安価なため、Kuroco利用料の削減にはキャッシュ比率の向上が重要です。

#### Cookie認証を静的アクセストークンに変更
セッションごとにキャッシュが作成されるCookieに対して、静的アクセストークンはトークン毎にキャッシュが作成されるため、セキュリティを静的アクセストークンに変更することでキャッシュ比率の改善が見込めます。  
認証が不要なエンドポイントは静的アクセストークンを利用することを検討してください。

- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)

:::caution
フロントエンド側の調整も必要になります。
:::

#### APIエンドポイントのキャッシュ設定
エンドポイントにキャッシュの設定をしていない場合は設定をお願いいたします。  
Kurocoでは1日や1週間といった設定をお勧めしておりますが、コンテンツが更新された際に自動でキャッシュがクリアされる仕組みがございますので、長く設定しても問題にはなりにくいです。

#### キャッシュの削除されないエンドポイントを作成する。
Kurocoではデータを最新に保つため、コンテンツの更新があった際に自動でキャッシュをクリアする仕組みがございます。

`Topics::list`の代わりに、キャッシュのクリアがされない`Api::request_api`のエンドポイントなどを利用することでキャッシュ比率の改善が可能な場合があります。

- [コンテンツカテゴリ毎にキャッシュがクリアされるリストのエンドポイントを作成する](/ja/docs/tutorials/create-an-endpoint-that-clears-the-cache-by-content-category/)

:::caution
キャッシュクリアのタイミングや範囲をご自身で設定する必要があることに注意してください。
:::

---
### APIリクエストを減らす
#### SSG（Static Site Generation）の活用
サイトのレンダリング方式をSSGにすると、APIを利用したデータの取得がデプロイ時のみになるため、一般的にはAPIのリクエスト数が減ることが多いです。

:::caution
クライアントサイドからリクエストを送るページはAPIリクエスト数の削減になりません。  
また、1日当たりのデプロイ回数やPV数によってはAPIリクエスト数が減らないこともございます。  
事前に試算することが重要です。  
:::

#### 内部API呼び出しの最適化

`{api_internal}`のSmartyプラグインはネットワーク経由のリクエストになるため、APIリクエスト数にカウントされます。
`direct=true`の設定をしたり、`{api_method}`のSmartyプラグインに置き換える事でAPIリクエスト数の削減が可能です。

- [カスタム処理で呼び出したAPIの利用料について教えてください](/ja/docs/faq/api-usage-fees-for-custom-processing/)

#### API呼び出しの最適化
ページ毎にリクエストを送ってデータの取得をしているAPIはフロントエンドのページ数が増えるとリクエスト数も増加します。  
ページ毎ではなく、事前にデータを取得してからページの生成をするように設計すると、APIリクエスト数を削減できる場合があります。

例えば、`Topics::details`のリクエスト数を減らすために`Topics::list`で取得するケースなどが考えられます。  
- [Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)

ただし、APIのリクエスト数を減らすために一度に大量のデータを取得すると、レスポンスに時間がかかり、コンピューティング費用がかかる場合があります。
APIレスポンスの件数は、1回あたり 20件から200件程度 にとどめることをお勧めします。
また、後処理で必要な項目を絞ることで、処理速度が向上する場合があります。その場合は、1,000件程度のデータを一括で取得することも選択肢となります。

#### 不要なAPIの削除
- フロントエンドから不要なAPI呼び出しがないか確認してください。

#### ファイルアクセス時のドメイン最適化
APIドメインでファイルにアクセスすると、APIリクエストとしてカウントされます。必要に応じて、Filesドメインへの置き換えをご検討ください。
- [KurocoFilesディレクトリとドメインの使い分けについて](/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/)

---
### API転送量を減らす
#### 後処理で出力許可リストを設定する
API転送量を減らすには、エンドポイントのレスポンスサイズを小さくする必要があります。
エンドポイントの後処理で出力許可リストを設定し、必要な項目のみレスポンスさせることは、レスポンス容量を減らし、API転送量の削減に効果があります。

- [出力許可リスト](/ja/docs/reference/post-processing/#出力許可リスト)

---
### KurocoFront転送量を減らす
#### 404ページの最適化
ボットやクローラーがURLを予想して巡回することで、存在しないURLにアクセスされることがありますが、
この場合でもKurocoFrontが404のページを表示するためにCDN転送量が発生します。  

`存在しないページへのアクセス数`×`404ページの容量`の分だけCDN転送量が発生することになりますので、
404を始めとしたエラーページはできるだけ軽量に設計すると、CDN転送量の削減になります。

---
### KurocoFiles転送量を減らす
#### 画像の動的変換で適切な画像サイズでCDNに記録する
動的変換の機能を利用すると、画像の大きさや品質などを動的に変更し、変更した内容でCDNキャッシュを残します。
適切な変換を行った画像に対してリクエスト・読込を行う事で、無駄に大きな画像のCDN読込を防止し、CDN転送量の削減を図ります。

- [画像の動的変換について](/ja/docs/reference/api-convert-image/)

---
### DBファイル容量を減らす
#### 更新履歴の削除
コンテンツ定義編集の詳細設定で、更新履歴を残さないを有効にすると、過去の更新履歴は削除され、以降の更新で更新履歴が残らなくなります。
更新履歴が不要な場合は有効にするとDBファイル容量の削減に効果があります。

:::caution  
削除された更新履歴は復元できません。  
:::

---
### ファイル容量を減らす
#### ファイルサイズの最適化
動的変換の機能で、画像の大きさや品質などを動的に変更して適切に利用していても、ファイル容量の項目には元ファイルの容量分の利用料が課金されます。  
元画像の容量が必要以上に大きい場合は、調整した画像をKurocoFilesに設置することでファイル容量の削減が可能です。

---
### KurocoFrontファイル容量を減らす
#### 90日以上前のファイル削除設定
KurocoFrontはコミットハッシュごとにファイルを保管しますので、古いファイルは自動で削除をする設定を有効化します。

1. [Kuroco Front] → [KurocoFront設定]  
2. 「90日以上前のファイルを削除する」を有効化  

#### 画像等をKurocoFilesに移動
KurocoFrontはデプロイのファイルを保管し、「90日以上前の履歴を削除する」の設定をしても90日間は削除されません。  
そのため、画像等の静的ファイルもデプロイのたびにKurocoFrontに溜まっていき、ストレージ料金が余計にかかります。

静的な画像やファイルはKurocoFilesを利用することで、KurocoFront容量の削減に効果があります。

- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/) 

---
### バックアップファイル容量を減らす
#### 不要なバックアップを削除する
[環境設定]->[[バックアップ](/ja/docs/management/backup/)]に不要なバックアップファイルがある場合は削除をしてください。
`{backup}`,`{backup_delete}`のSmartyプラグインで自動的にバックアップを追加・削除するバッチ処理を作成するのも有効です。


## 関連ドキュメント

- [利用状況](/ja/docs/management/usage/)  
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)  
- [Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)  
- [カスタム処理で呼び出したAPIの利用料について教えてください](/ja/docs/faq/api-usage-fees-for-custom-processing/)  
- [利用料金](https://kuroco.app/ja/pricing/)


---

# 本番環境のデータを検証環境に同期するボタンを設置する

> 元ページ: `tutorials/place-a-button-to-synchronize-production-data-with-the-validation-environment` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/place-a-button-to-synchronize-production-data-with-the-validation-environment/
> 概要: Kurocoはサイト同期の機能を持っており、メインサイトやサブサイト間でデータの同期が可能ですが、実行するには通常、メインサイトでサイト管理の更新権限が必要です。本チュートリアルでは、サブサイトのダッシュボードに「本番環境からの全同期を実行する」ボタンを設置して、メインサイトでサイト管理の更新権限を持たないメンバーでもワンクリックで最新のデータを同期する方法を説明します。

## 概要
Kurocoはサイト同期の機能を持っており、メインサイトやサブサイト間でデータの同期が可能ですが、実行するには通常、メインサイトでサイト管理の更新権限が必要です。  
作業者や制作担当者に大きな権限を与えたくない場合、メインサイト側に同期リクエストを受けるAPIを作成することによって、メインサイトでの権限を持たないメンバーでもデータを同期実行させることができます。  
また、サブサイト側のダッシュボードにウィジェットを用意すると、メインサイトにログインすることなく簡単に同期の実行をできるようになります。

本チュートリアルでは、サブサイトのダッシュボードに「本番環境からの全同期を実行する」ボタンを設置して、メインサイトでサイト管理の更新権限を持たないメンバーでもワンクリックで最新のデータを同期する方法を説明します。

### 学べること
以下の手順でメインサイトからの全同期を実行するボタンを設置します。
- [事前準備](#事前準備)
- [同期リクエストを受けるAPIを設定する](#同期リクエストを受けるapiを設定する)
- [同期を実行するカスタム処理を追加する](#同期を実行するカスタム処理を追加する)
- [ダッシュボードのウィジェットを追加する](#ダッシュボードのウィジェットを追加する)
- [サブサイトに同期する](#サブサイトに同期する)
- [動作を確認する](#動作の確認をする)

### 前提条件
[サイト一覧](/ja/docs/management/site-list/)でサブサイトが追加されていることを前提とします。

:::caution
サイト同期の方向を間違えるとメインサイトのデータを意図せず上書きしてしまう場合があります。
作業を進める前に[バックアップ](/ja/docs/management/backup/)を取得しておくことをお勧めします。
:::

## メインサイトの設定
### 事前準備
[同期項目一覧](/ja/docs/reference/sync-site-data/#同期項目一覧)にまとめた通り、全同期を実行すると、APIやカスタム処理、バッチ処理も同期されます。  

APIのCORS設定にメインサイトのURLだけを登録していると、同期後のサブサイトのCORSもメインサイトのURLだけになり、サブサイトのURLからのAPIリクエストを受け付けなくなります。  
そこで、全同期の実施後もサブサイトのURLからサブサイトのAPIへリクエストが送れるようCORS設定にサブサイトのURLも設定しておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/38a9752703b693f7c0ba5d560b71bc6f.png)

同様にカスタム処理やバッチ処理でサイトキーを含む管理画面URLやAPIドメインを直書きしている場合は、定数から取得して利用するように調整します。  

例：  
`{assign var=my_api_domain value="https://sitekey.g.kuroco.app"}`  
↓  
`{assign var=my_api_domain value=$smarty.const.ROOT_API_URL}`

### 同期リクエストを受けるAPIを設定する
同期用のAPIを作成します。  

#### APIの作成
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5577a5ea4237810a291a3654cb59df95.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Sync|
|版|1.0|
|ディスクリプション|Sync|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73c34adadc47bf2149fb6e70522d0fdf.png)

#### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/27ddd8db0440ffffed9a272b8fef1894.png)

セキュリティを[静的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c84a5a31f1e82c0ac13f230b6dbb1c1d.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4fab850dc0ce89a52c91161073b8d56e.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- サブサイトの管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/08813b7f761005f7ab35211f247764e4.png)

問題なければ [保存する] をクリックします。

#### 静的アクセストークンの発行
[Swagegr UI]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/969ff3fa5ae0c4e42ccb6db89d54b06b.png)

静的アクセストークンの有効期限を設定して[生成する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa1e7813514082f444e9952bdf380579.png)

静的アクセストークンが発行されるので値をメモします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f1de4001de6aa94dc226e5d3460a11a.png)

#### エンドポイントの作成
SyncのAPIから[新しいエンドポイントの追加]をクリックして以下のエンドポイントを作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c87d0a3ae3b483e2bef0d866c5e32f7.png)

|項目|設定内容|
| :--- | :--- |
|パス|sync_site|
|カテゴリー|API|
|モデル|Api|
|オペレーション|request_api_post|
|name|sync_site|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c8d4d489e9b5aa5a028cc929da088f11.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/20c2547ee21ac80eafe510549e00f652.png)

### 同期を実行するカスタム処理を追加する
リクエストを受け付けるエンドポイントの準備ができたら、同期を実行するカスタム処理を登録します。  

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

以下の動作となるカスタム処理を作成します。  
- site_syncという関数を呼んでサイト同期を行います。  
- 同期元サイトfrom_site_keyにはメインサイトのサイトキーを定数で指定します。  
- 同期先サイトto_site_keyはリクエスト変数から取得した値を利用するものとします。  
- 同期の種類 sync_type には全同期 2 を指定します。  
- 実行されたサイトキーと実行者の名前をログに残します。  

|項目|値|
|:--|:--|
|タイトル|sync_site|
|識別子|sync_site (request_api_postのエンドポイントに設定したnameと一致さてください。)|
|処理|以下の内容|

```smarty
{site_sync from_site_key=$smarty.const.SITE_KEY to_site_key=$smarty.request.to_site_key  sync_type='2'}
{logger msg1="全同期を実行しました" msg2=$smarty.request.to_site_key msg3=$smarty.request.name}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e4dad63cf56b572b0c3b02ab92ebdc82.png)

### ダッシュボードのウィジェットを追加する
次にダッシュボードのウィジェットの機能で同期を実行するためのボタンを表示します。  
[環境設定] -> [ダッシュボードのウィジェット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c792bbdad2221e3073a150fe243e15bf.png)

追加をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/207d9a78a141ce5667fbe8af1805ffb8.png)

以下のように設定します。  
サイトがメインサイト以外の場合に[本番環境からの全同期を実行する]のボタンを表示し、ボタンがクリックされると、サイトキーとユーザー名をメインサイトのエンドポイントにポストします。  
 
|項目|内容|
|:--|:--|
|名前|任意の名前|
|HTML|以下のコード|
|アクセス制限|無し|
|管理画面|通常版|
|公開設定|公開|

```smarty
{if $smarty.const.SITE_KEY != "YOUR_MAIN_SITE_SITEKEY"}
<form id="myForm" action="https://YOUR_MAIN_SITE_SITEKEY.g.kuroco.app/rcms-api/6/sync_site" method="POST">
    <input type="hidden" id="toURL" value="{$smarty.const.SITE_KEY}">
    <input type="hidden" id="member_NAME" value="{$smarty.session.name1}">
    <button type="button" onclick="submitForm()">本番環境からの全同期を実行する</button>
</form>

{literal}
<script>
    function submitForm() {
        var toURL = document.getElementById('toURL').value;  // hidden inputから値を取得
        var member_NAME = document.getElementById('member_NAME').value;  // hidden inputから値を取得
        var form = document.getElementById('myForm');
        var url = form.action;

        // POSTリクエスト用のオプションを設定
        var requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-RCMS-API-ACCESS-TOKEN': 'YOUR_STATIC_ACCESS_TOKEN'
            },
            body: JSON.stringify({
                to_site_key: toURL,
                name: member_NAME
            }),
        };

        fetch(url, requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                alert('同期を実行しました。反映までしばらく時間をおいて確認してください。');  // 成功時のアラート
            })
            .catch(error => {
                console.error('Fetch error:', error);
                alert('エラーが発生しました。');  // エラー時のアラート
            });
    }
</script>
{/literal}
{/if}
```

:::caution  
`YOUR_MAIN_SITE_SITEKEY`と`YOUR_STATIC_ACCESS_TOKEN`の部分はご自身のメインサイトのサイトキーと、メインサイトで発行した静的アクセストークンに置き換えてください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/679b637c39dbf0a055c76b070e31978e.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e8a3a7dbb21eebda298f8535f8d0b68.png)

入力ができたら[追加する]をクリックしてダッシュボードのウィジェットを追加します。  

以上で機能の設定は完了です。  
サブサイトにも反映し、動作の確認をします。  

## サブサイトに同期する
[環境設定] -> [サイト一覧]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d34e973cdd6985c77e9ee4bb8703410.png)

同期を実行するサブサイトの[編集]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6591837a85c90666da9b572f33f7afca.png)

以下のように設定して[更新する]をクリックします。

|項目|値|
|:--|:--|
|すぐに同期する|チェックを入れる|
|同期元サイトキー|メインサイトを指定する|
|アプリ同期/全同期|全同期を選択する|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0638a27478d676e77b581d08d5b93c11.png)

同期が反映されるまでしばらく時間をおき、追加したカスタム処理やダッシュボードのウィジェットがサブサイトで確認できたら完了です。

## 動作の確認をする
以下のポイントを確認して、想定通りの処理が実行されているか確認します。

- メインサイトには同期のボタンが表示されない  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/11776983e55f2bf252b4c6adb62ceea5.png)
- サブサイトには同期のボタンが表示される  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/f799a1c0090b35616d440dbbae9bc70e.png)
- 同期のボタンをクリックするとメインサイトに追加したコンテンツがサブサイトに同期される  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b34719ffd6b8ba97929559d162b736f.png)
- メインサイトのカスタムログを確認すると同期を実行したサイトキーとユーザー名が記録されている  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/58b90030cb3a1f748354dc0a0cfb7758.png)

以上で設定は完了です。  
メインサイトの最新データを作業担当者がサブサイトから同期できるようになりました。  

## 関連ドキュメント
- [同期項目一覧](/ja/docs/reference/sync-site-data/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/)


---

# Kurocoを利用したプロジェクトの進行イメージ

> 元ページ: `tutorials/starting-a-project-on-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/starting-a-project-on-kuroco/
> 概要: Kurocoを利用したプロジェクトの進行イメージについて説明します。今回は会員制社内ポータルサイトを構築する場合を想定し、実際にプロジェクトをどのように進めるのか、必要なツールは何か、それぞれの対応内容と役割は何かをまとめました。

本ドキュメントでは、Kurocoを利用したプロジェクトの進行イメージについて説明します。

今回は会員制社内ポータルサイトを構築する場合を想定し、実際にプロジェクトをどのように進めるのか、必要なツールは何か、それぞれの対応内容と役割は何かをまとめました。プロジェクトの進め方の流れの参考としてご利用ください。

:::caution
実際には案件によって仕様やプロジェクトメンバー、ツールが異なります。あくまでも参考としてご確認ください。
:::

## 案件概要

今回は、下記案件を想定しています。

### 開発するWebサイトの仕様

- 会員制社内ポータルサイト構築
- 新規ドメイン取得

### 利用するフレームワークについて

本プロジェクトで利用するフレームワークです。

|利用フレームワーク |概要 |
| :--- | :--- |
|Kuroco|バックエンドシステム|
|[Vuetify](https://vuetifyjs.com/ja/)|UIフレームワーク|
|[Figma](https://www.figma.com/)|Figma|

### 作業範囲と担当者

本プロジェクトの作業範囲と担当者です。

|No |フェーズ |作業範囲 |担当者 |
|:--- | :--- | :--- | :--- |
|1 |プロジェクト設計 |[要件定義・システム・UX設計](#1-要件定義・システム・ux設計)|プロジェクトマネージャー<br/>デザイナー|
|2 | |[画面・UI設計](#2-画面・ui設計)|プロジェクトマネージャー<br/>デザイナー|
|3 | |[データ構造・API設計(Kuroco)](#3-データ構造・api設計kuroco)|バックエンドエンジニア<br/>フロントエンドエンジニア|
|4 |デザイン |[UIデザイン](#4-uiデザイン)|デザイナー|
|5 | |[コーディング](#5-コーディング)|コーダー|
|6 |開発 |[マイクロサービス開発](#6-マイクロサービス開発)|バックエンドエンジニア|
|7 | |[API設定](#7-api設定)|バックエンドエンジニア<br/>フロントエンドエンジニア|
|8 | |[外部API連携](#8-外部api連携)|バックエンドエンジニア|
|9 | |[フロントエンド構築(含APIの呼び出し)](#9-フロントエンド構築含apiの呼び出し)|フロントエンドエンジニア|
|10 | |[環境構築](#10-環境構築)|バックエンドエンジニア|
|11 | |[データ移行](#11-データ移行)|バックエンドエンジニア|
|12 |テスト |[総合テスト](#12-総合テスト)|テスター|
|13 | |[動作検証(受入)](#13-動作検証受入)|顧客|
|14 |リリース |[リリース](#14-リリース)|プロジェクトマネージャー|
|15 |運用 |[サイト運用](#15-サイト運用)|プロジェクトマネージャー<br/>バックエンドエンジニア<br/>フロントエンドエンジニア|

:::tip
役割分担については、[[営業資料] -> [プロジェクト役割分担表]](/ja/docs/about/sales/#プロジェクト役割分担表)をご確認ください。
:::

### 管理ツール

プロジェクト管理やコミュニケーションツールとして、次のサービスを利用します。

ツールは複数に分散するほど管理が煩雑になり、見落としのリスクを高めます。そのため以下のツールに限定し管理しています。  

|ツール |用途 |概要 |
| :--- | :--- |:--- |
|[Googleスプレッドシート](https://www.google.com/intl/ja_jp/sheets/about/)|設計|ページ一覧、ページごとの期限、ステータス管理、Issue管理などに利用します。<br/>参考：[WBS・タスクリストのサンプル](https://docs.google.com/spreadsheets/d/1uWbBbQ96JFTFrEI5LyeDi54A9YjBY4nRZ_0Mie_GUsk/edit?usp=sharing)|
|[Backlog](https://backlog.com/ja/) |課題管理<br/>議事録共有 |課題管理やミーティング議事録として利用し、共有します。社内と社外向けをそれぞれ用意します。|
|[Slack](https://slack.com)|コミュニケーション|連絡コミュニケーションツールとして利用します。|
|[Google Meet](https://apps.google.com/intl/ja/meet/)|コミュニケーション|オンラインミーティングに利用します。|

### コミュニケーション計画

クライアント企業および社内でのミーティングを次のように設定します。

|項目 |概要 |参加者 |頻度 |
| :--- | :--- |:--- |:--- |
|キックオフ |プロジェクト開始時に開催します。 |全メンバー |１回。プロジェクト開始時 |
|定例ミーティング(クライアント) |クライアント企業との進捗管理ミーティングです。(※1) |フェーズ毎該当メンバー |週１回 |
|定例ミーティング(社内) |社内メンバー向けの進捗管理ミーティングです。 |社内メンバー |週1回 |
|運用レクチャー |クライアント向けの運用方法のレクチャーです。 |全メンバー |1回。運用フェーズ |

#### **※1. 定例ミーティングでの議題内容**
定例ミーティングの主な内容は次の通りです。

- 仕様の確認
  - 仕様に関する不明点の確認
  - Kurocoの実装方法の提案
- 進捗確認
  - スケジュール、作業状況確認、残課題の確認
  - 作業が遅れている場合は、疑問点や問題点について具体的に確認

## 1. 要件定義・システム・UX設計

要件定義・システム・UX設計は、次のような手順で行います。

### サイトマップ作成

Googleスプレッドシートを用いて、サイトマップを作成します。これを用いて、クライアント企業とページや機能の過不足を確認します。

### ページ単位での構成要素の定義

作成したサイトマップをベースに、各ページごとの構成要素を定義、確認します。ページをまたがって共通化できる部品があれば、グループ化して定義します。

### 動作環境の確定
サイトの実行動作環境についてクライアント企業と確認します。

## 2. 画面・UI設計

### ワイヤーフレーム制作

サイトマップ・ページ構成要素をもとに、Figmaを利用してワイヤーフレームを制作します。

## 3. データ構造・API設計(Kuroco)

### データ構造
Kuroco管理画面で設定するデータ構造を設計します。
- コンテンツ定義
- グループ設定
- メンバー項目定義

### 参考：
- [管理画面マニュアル -> コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [管理画面マニュアル -> グループ](/ja/docs/management/group/)
- [管理画面マニュアル -> メンバー](/ja/docs/management/member/)

### API設計

Kurocoを用いてAPI設計をします。まずページごとの構成要素に基づいて、必要なAPIを洗い出します。

洗い出したAPIはGoogleスプレッドシートにて、API一覧としてまとめます。また、GoogleスプレッドシートのPageListに、そのページで利用するAPIのエンドポイントを記載します。

この時、ワイヤーフレーム上に、どのAPIを利用するのか記述しておきます。これはフロントエンド担当者の役割です。また、API仕様の管理はバックエンド担当者の役割になります。

## 4. UIデザイン

Figmaで作成したワイヤーフレームは、そのままデザインにも利用します。

作成後、デザイン担当者とクライアント企業を含めてミーティングを行います。その際には、ページごとの要素や詳細な仕様について確認します。修正があった場合には、ミーティング時に修正した上で、その場で全員の確認と承認を得ます。

## 5. コーディング

本案件ではVuetifyを利用して、静的にコーデイングを行います。

なお、挙動を伴うコンポーネントは使わず、APIで処理する方が良いケースもあります。API設計時に、コーディング担当者とAPI設計者の間で情報共有しておくと良いでしょう。

## 6. マイクロサービス開発
デザインの承認が行われたら、開発フェーズに入ります。

### Kurocoサイト登録
[Free Trialページ](https://kuroco.app/ja/free_trial/)より、Kurocoサイトの登録をします。

### GitHubにて開発リポジトリ追加
GitHubに開発リポジトリを追加します。フロントエンドはGit管理をします。

参考: [GitHub Docs リポジトリを作成する](https://docs.github.com/ja/github/getting-started-with-github/quickstart/create-a-repo)

### KurocoFrontのホスティングとGit連携
KurocoFrontを利用し、KurocoとGitHubリポジトリを接続します。

参考: [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)

### Kuroco管理画面の設定をする
Kurocoの管理画面にて設定します。

#### **コンテンツ定義設定(拡張項目設定)**
[データ構造・API設計(Kuroco)](#3-データ構造・api設計kuroco)をもとにコンテンツ定義を設定します。

参考:
- [チュートリアル コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)<br/>
- [管理画面マニュアル コンテンツ定義](/ja/docs/management/content-structure-topics-group/)

#### **メンバー拡張項目設定**
グループの設定と会員メンバーの設定をします。

参考:
- [管理画面マニュアル メンバー拡張項目設定](/ja/docs/management/extra-information/)
- [チュートリアル グループを作成する](/ja/docs/tutorials/how-to-make-new-group/)

## 7. API設定
[API設計](#api設計)をもとにAPIの設定します。

参考:
- [チュートリアル API エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [管理画面マニュアル API API List](/ja/docs/management/api-list/)

## 8. 外部API連携
Kurocoは外部サービスとの連携も可能です。外部サービスと連携することで、機能の幅が広がります。

### SendGridの設定(メールの送信元として利用するメールアドレス)
問い合わせなど、Webサイトの送信（From）で利用するメールアドレスを独自ドメインにする場合には、SendGridの設定が必要です。  
SendGridのアカウントを取得し設定をお願いします。  
※ メールアドレスドメインが  `@kuroco-mail.app ` で良い場合は、SendGridの設定は不要です。

参考: [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)

### Google Analyticsの設定
Google Analyticsと連携することでサイト分析ができるようになります。

参考: [Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)

## 9. フロントエンド構築(含APIの呼び出し)
### API呼び出し
作成したAPIをフロントエンド側で呼び出します。

### APIを実行する
フロントエンドの開発に伴って、コンテンツをAPI経由で取得できるかテストしてください。
API実行の確認にはSwaggerの利用が可能です。

参考: [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)

## 10. 環境構築
リリースに向けての環境構築をします。今回はドメインの取得と適用をします。

なお、今回のプロジェクトは認証が伴うWebサイトの構築を想定しております。
その場合、フロントエンドドメインとAPIドメインを準備する必要があるので、２つのドメインを設定する前提で進めます。

WebブラウザによってはサードパーティーCookieの利用ができず、ログインできないエラーが発生する場合もあるためです。  
参考記事:[Google、ChromeでのサードパーティーCookie廃止を2023年まで延期](https://www.itmedia.co.jp/news/articles/2106/25/news067.html)

### ドメインの取得
下記２つのドメインを取得いただくようクライアントに依頼します。

|ドメイン |用途 |
| :--- | :--- |
|`www.CLIENT.app` |フロントエンドドメインとして利用します。 |
|`kuroco.CLIENT.app` |APIドメインとして利用します。 |

### ドメインの設定
KurocoFrontへ独自ドメインを適用します。ドメインの設定には下記作業が必要です。

- フロントエンドドメイン DNSの変更
- APIドメイン DNSの変更
- Kuroco管理画面にてドメインの設定

ドメインは下記ドキュメントを参考に設定してください。

参考: [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)

## 11. データ移行
Kuroco管理画面より、本番に必要なコンテンツ・ユーザーデータの登録をします。  
データ登録は登録フォームより登録、またはCSVファイルで一括登録が可能です。

参考: [CSVで記事を一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)

## 12. 総合テスト
### テストケースの作成
開発が進んできた段階で、テストケースを作成していきます。

### 社内検証の実施
テストケースに基づいて社内にて検証をします。    
不備があればタスク管理に登録・修正し、再検証をします。

## 13. 動作検証(受入)
### クライアント企業にて検証の実施
社内で総合テストが完了したらクライアント企業に検証を依頼します。  
開発環境にプロジェクトをデプロイし、外部からでも検証できる環境を用意します。
その際にはIPアドレスやBasic認証を用いてアクセス制限を行います。

クライアント企業からフィードバックを受け取ったら、その内容に基づいて修正対応を行います。

参考: [kuroco_front.jsonとは何ですか？ -> basic：Basic認証](/ja/docs/faq/what-is-kuroco_front_json/#basic：basic認証)

## 14. リリース

動作検証が完了したらいよいよリリースです。

### 認証解除
IPアドレス制限・Basic認証を解除します。

## 15. サイト運用
サイト公開と同時に運用フェーズが開始します。運用マニュアルを準備し、クライアント側で運用できるようサポートします。

## 関連ドキュメント
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
