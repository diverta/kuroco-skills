# Kurocoドキュメント: チュートリアル / フロントエンド・KurocoFront（1/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 多言語サイトを構築する（`building-a-multi-language-site`）
- GitHubからKurocoFrontへソースをデプロイする方法（`connect-to-github-with-kuroco-front`）
- KurocoでできるCore Web Vitalsへの対応の進め方（`core-web-vitals-with-kuroco`）
- コーポレートサンプルサイトをSSGにする（`corporate-sample-site-to-ssg`）
- 画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて（`difference-between-kurocofiles-and-kurocofront`）
- 会員制サンプルサイトの解説（`explanation-of-kuroco-sample-site`）
- figma-design-guide（`figma-design-guide`）
- コンテンツ一覧/詳細ページを作成する（`integrate-kuroco-with-nuxt`）
- プレビュー画面を構築する（`integrate-preview-page`）
- コーポレートサンプルサイトを利用する（`kuroco-corporate-sample-site`）
- メディアサンプルサイトを利用する（`kuroco-media-sample-site`）


---

# 多言語サイトを構築する

> 元ページ: `tutorials/building-a-multi-language-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/building-a-multi-language-site/
> 概要: Kurocoを利用したプロジェクトで、多言語に対応したサイトの構築方法について説明します。

Kurocoを利用したプロジェクトで、多言語に対応したサイトの構築方法について説明します。  
今回は例として[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)で作成した/news/のページを多言語対応します。

:::info
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、コンテンツ一覧のページが作成されていることを前提としています。
まだ構築していない場合は、下記のチュートリアルを参照してください。
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## 1. パッケージのインストール
ターミナルで対象のプロジェクトのディレクトリへ移動後、下記を実行します。  

**Nuxt2:**

nuxt-i18nをインストールします。 

```
npm i nuxt-i18n
```

**Nuxt3:**

@nuxtjs/i18nをインストールします。 

```
npx nuxi@latest module add i18n
```


## 2. localeファイルの作成
次にlocalesのフォルダを作成し、対応する言語毎のlocaleファイルをjson形式で保存します。  
今回は英語・日本語の言語に対応させるため、locales/en.json と、locales/ja.json のファイルを作成します。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/4ab99e8a6cb85c1b9d46e6c7155a9d6b.png)
localeファイルの中身はそれぞれ下記のように記述します。(項目は必要に応じて追加してください。)

```json title="/locales/en.json"
{
  "links": {
    "home": "Home",
    "news": "News",
    "en": "English",
    "ja": "Japanese"
  },
  "news": {
    "title": "front_kuroco_sample_support"
  }
}
```

```json title="/locales/ja.json"
{
  "links": {
    "home": "ホーム",
    "news": "お知らせ",
    "en": "英語",
    "ja": "日本語"
  },
  "news": {
    "title": "フロントKurocoサンプル"
  }
}
```
## 3. nuxt.config.js 修正
nuxt.config.jsの`modules`の項目に下記の記述を追加します。

**Nuxt2:**

```js title="nuxt.config.js"
modules: [
   [
      'nuxt-i18n',
      {
        strategy: 'prefix_and_default',
        // 切り替える言語を定義
        locales: [
          { code: 'ja', file: 'ja.json' },
          { code: 'en', file: 'en.json' },
        ],
        // デフォルトの言語を設定
        defaultLocale: 'ja',
        vueI18nLoader: true,
        lazy: true,
        // jsonファイルを保存したディレクトリを指定
        langDir: 'locales/',
      },
    ],
    ...
  ],
```

**Nuxt3:**

```js title="nuxt.config.js"
modules: [
    [
      "@nuxtjs/i18n",
      {
        strategy: "prefix_and_default",
        // Define the language options
        locales: [
          { code: "ja", file: "ja.json" },
          { code: "en", file: "en.json" },
        ],
        // Set the default language
        defaultLocale: "ja",
        vueI18nLoader: true,
        lazy: true,
        // Specify the directory for the JSON file
        langDir: "locales/",
      },
    ],
    ...
  ],
```


以上で多言語を利用する準備が整いました。  

## 4. 言語切り替えボタンの作成
続いて、言語切り替えボタンを作成します。  
コードは流用できるよう流用できるよう components フォルダに LanguageSwitcher.vue のファイルを作成し、こちらに記述します。  

`/components/LanguageSwitcher.vue`を下記のように作成します。  

```markup title="/components/LanguageSwitcher.vue"
<template>
  <div>
    <nuxt-link :to="switchLocalePath('en')">{{ $t('links.en') }}</nuxt-link>
    |
    <nuxt-link :to="switchLocalePath('ja')">{{ $t('links.ja') }}</nuxt-link>
  </div>
</template>

<script>
export default {};
</script>
``` 

また、`/pages/news/index.vue` の記述を次のように変更し、ボタンの確認をします。  
localeファイルで設定した文章は`{{ $t('news.title') }}`の記述で表示が可能です。  

```diff
 <template>
   <div>
-    <p>News list</p>
+    <LanguageSwitcher />
+
+    <h1 class="title">{{ $t('news.title') }}</h1>
     <div v-for="n in response.list" :key="n.slug">
       <nuxt-link :to="`/news/${n.topics_id}`">
         {{ n.ymd }} {{ n.subject }}
```

言語切り替えボタンの表示と、言語に応じたタイトルの表示が確認できました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/06f1d7f5e1cfe26416b8a4ad27d9faee.gif)

## 5. バックエンド部分(Kuroco)の多言語対応
次に[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)のチュートリアルで作成した`/news/`のページを多言語対応します。  

### 多言語設定を追加
Kuroco管理画面で[環境設定] -> [ローカライズ]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a94861a2f489c1c7a528d3d5ace4af1b.png)
多言語の設定が表示されるので、主言語、副言語を選択し、[利用する]にチェックを入れて[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4de7d307d273039830c2f377902980e5.png)

### 副言語のコンテンツを追加
次に副言語のコンテンツの追加をします。  
作成済みのコンテンツ定義「お知らせ」をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/2403b388d998d4dd25f7d01fafef73a0.png)
お知らせ一覧からコンテンツの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/27d25012588496557908eadf3f90d2ac.png)

ローカライズで多言語の設定をしているため、コンテンツ編集のページに設定した副言語のタブが表示されています。  
[英語]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6fd4552d008dd1d4e056f4ce8776570d.png)

英語版のコンテンツを入力し、[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ec0ffaaaa4da6c5eb1ea677a4911e87a.jpg)

同様に、それぞれのコンテンツで副言語の設定を追加します。  

### APIの言語毎でのレスポンスを確認する。
Swagger UIを使用して、副言語のレスポンスを確認します。  

「お知らせ一覧」と「お知らせ詳細」のエンドポイントを作成したAPIのページに遷移します。    
![Image from Gyazo](https://t.gyazo.com/teams/diverta/554777007d8f8c2017dbc487e89f38cf.png)

[Swagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ee0d42eac81896c83337bf6be06bfe0.png)

「お知らせ詳細」のエンドポイントの[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ca6e55b36a5ab45e8d54994f6682f02.png)

コンテンツのID(今回の場合は6)を入力して[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8dce93d3a7ed442fac44b1f2b043027.png)

主言語でのレスポンスが得られていることが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b6e11c5b701232e231b2c2c57072ce7.png)

次に`_lang`の設定に`en`を追加して[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/52b559e6116b9ac33fb81782df565bb0.png)

今度は副言語(en)でのレスポンスが得られていることが確認できました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bd9dd5112f747df6055f73b8233afc9.png)

Request URLを見てもわかるように、エンドポイント末尾に`?_lang=en`のパラメータを追加することで英語のデータを取得できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4d413bba7b5cf288ac8b034a576d38e2.jpg)

「お知らせ一覧」のエンドポイントも同様に副言語(en)でのレスポンスが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d705243c917da37ef7e3b344ff451963.png)

## 6. フロントエンドの修正
最後に、KurocoのAPIから得るレスポンスを、表示している言語に対応するよう記述を修正します。  

**Nuxt2:**

```markup reference title="/pages/news/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_i18n_list.vue
```

**Nuxt3:**

```markup reference title="/pages/news/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_i18n_list.vue
```


**Nuxt2:**

```markup reference title="/pages/news/_slug.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_i18n_details.vue
```

**Nuxt3:**

```markup reference title="/pages/news/[slug].vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_i18n_details.vue
```


:::caution
Request URLの部分(`/rcms-api/4/newsdetail/`)は自身のサイトのものに調整してください。  
:::

`http://localhost:3000/news`を確認すると、言語切り替えによって、Kurocoのコンテンツ部分についても表示言語が変わることを確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/236f2428cf0b6e5d5bf8086ab82625f3.gif)

以上で多言語サイトを構築する説明を終了します。

## 関連ドキュメント
- [ローカライズ](/ja/docs/management/localize/)
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [副言語について](/ja/docs/reference/secondary-language/)
- [APIでレスポンスされる言語の優先順位について](/ja/docs/reference/api-response-language-preference/)
- [多言語サイトを構築する際に気をつけることを教えてください](/ja/docs/faq/what-should-i-take-note-of-when-building-a-multilanguage-site/)


---

# GitHubからKurocoFrontへソースをデプロイする方法

> 元ページ: `tutorials/connect-to-github-with-kuroco-front` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/connect-to-github-with-kuroco-front/
> 概要: KurocoFrontへGitHubを利用したデプロイ方法を紹介します。

KurocoFrontへGitHubを利用したデプロイ方法を紹介します。 

## KurocoFrontへのデプロイ手順
### 1. リポジトリ準備

GitHubにてKurocoFrontへデプロイしたいリポジトリを準備します。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5ae8411ce2640c6f0c5b97576e29ee97.png)
:::info
前提条件として、静的なファイルしかホスティングできませんのでリポジトリにはNuxt.js等のJavaScriptフレームワークや、HTML/CSS/JSファイルや画像などのメディアファイルが登録されている必要があります。
上記画面はNuxt.jsのリポジトリを表示しております。
:::

### 2. KurocoFrontよりGitHubリポジトリと接続する
[外部システム連携] -> [GitHub] をクリックし、KurocoFrontを表示します。  
KurocoFrontより「GitHubリポジトリと接続する」をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/875b9ce003a701696e278a4454c49535.jpg)
GitHubへログインが求められますので、ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/214c1957e75be4de2ea7bc01d10499ab.png)
ログインするとGitHubの画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d42942104b7b668e7d80c44696db4429.png)
「Repository access」より接続するリポジトリを選択します。

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

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/296ac6fb71ddea36ace52dbe804fd126.png)
接続が完了すると、KurocoFrontの画面に遷移します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d4222c9238bbed8c3ad14461e29344ee.png)
以上でKurocoFrontとGitHubリポジトリの接続が完了となります。

### 3. kuroco_front.jsonを作成する
KurocoFrontを利用するために、`kuroco_front.json`をルートディレクトリに配置する必要があります。

:::tip
Nuxtの場合は下記kuroco_front.jsonを `/static` 配下に作成します。
:::

```json title="kuroco_front.json"
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

`kuroco_front.json`ではURLのリライト処理やBasic認証やIPアドレス制限の利用が可能です。Basic認証のパスワードはプレーンテキストになっております。リポジトリをpublicにする場合はご注意ください。  

参考: [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)  

### 4. `.github/workflows` にYAMLファイルを配置する  
KurocoFrontではGitHubアクションを利用するため、 `.github/workflows` にYAMLファイルを配置します。  

まずはKurocoFront画面のリポジトリフィールドの内容をコピーし、ビルドコマンドやブランチ名などを調整して `build.yml` を作成します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/dad5a689e0e8c160b7d7fd1de65bd09e.png)
次に作成した`build.yml`を`.github/workflows` 配下に配置し完了です。

参考:  
GitHub アクションを利用するため、YAMLファイルを作成しワークフローの定義を行なっております。
YAMLファイルについての説明や、書き方については下記ドキュメントをご確認ください。
- [GitHub Docs GitHub Actions について学ぶ](https://docs.github.com/ja/actions/learn-github-actions)
- [GitHub Docs GitHub Actionsのワークフロー構文](https://docs.github.com/ja/actions/reference/workflow-syntax-for-github-actions)

:::info
YAMLファイルに記載されているアクションのバージョンが古くなると、エラーが表示される可能性があります。  
自動でアクションのバージョンを更新する方法は、[GitHub Actionsワークフローのアクションを最新バージョンに保つ方法はありますか？](/ja/docs/faq/how-to-keep-github-actions-up-to-date/) をご確認ください。
:::

### 5. 実際にデプロイのGithubActionsを動かす  
作成した`build.yml`は、Github上にアップロードされ次第動作しますので、実際にGithubへ更新をpushして、GithubActionsが動作開始することを確認します。

以下のコマンドを実行して、Githubへ更新をpushしてください。
```sh
git add .
git commit -m "ops: provide kuroco deployment"
git push
```

Githubのリポジトリ画面へアクセスし、[Actions]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/39a7350cf279af2413129060d40edab1.png)

GithubActionsが動作開始していることが確認できます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffab5abcf0f34c6f64fc99119aeb98c4.png)

しばらく待機すると、GithubActionsの動作が完了していることが確認できます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bebbb2d5f64889833c37e3cbd7e4dfbb.png)

#### GithubActionsが完了しなかった場合

GithubActionsが何らかの理由でエラーとなり、デプロイが完了しなかった場合、失敗していることが表示されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/09c632162aff04a3decbf9740df9e26a.png)

また、メールで通知されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/716c8da642050b2974d8be5db1567fe6.png)

### 6. サイトを表示する  
[サイトを表示]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f0041c26480eec068c794e4bdd4b6ad4.png)
すると、デプロイされたサイトへ遷移します。問題なく画面が表示されればデプロイ完了です。

## KurocoFrontへプレビューデプロイする手順

KurocoFrontでは、通常のデプロイの他、プレビューとして一時的なデプロイをさせることができます。  

ある修正をGithubのPullRequestとして適用しようとする場合、ローカル上でしか動作確認ができないとき、レビュアーはそのPullRequestを自分のローカルにいちいちcheckout/ビルドして動作確認しなくてはならず、不便です。  
このため、そのPullRequestのソースコードが、一時的な仮URL上にビルド/デプロイでき(プレビューデプロイ)、誰でもPullRequestの成果物をブラウザで確認できるようになると便利です。

`build.yml`には、PullRequestに**特定のコメントが記載されたら**プレビューデプロイするようにあらかじめスクリプトが組み込まれています。  
上記通常のデプロイ手順を行なっている方は、ファイルの変更等は必要ありません。

### プレビューデプロイ手順

#### テスト用PullRequestの作成

動作確認用に、空ファイルを作成して、PullRequestします。
```sh
git checkout -b preview_deploy
touch test.txt
git add .
git commit -m "chore: tmp"
git push --set-upstream origin preview_deploy
```

Githubのリポジトリ画面へアクセスし、[Pull requests]、[New pull request]とクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/30e0f4ce522f56b17e53adeeb2a64c4c.png)

[compare: ***]をクリックし、[preview_deploy]を選択、[Create pull request]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c360322adfe36d1ff5c0f7e37d1d302.png)

[Create pull request]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d43216d2defda21b8b4eb0776562ed6.png)

PullRequestを作成できました。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/eb00d665a8bf98b5d5987ec1f61a7869.png)

#### プレビューデプロイする

PullRequest画面下部のコメント欄に、`/kuroco stage`と入力、[Comment]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb2301d837284c03d5662ba4040eac0f.png)

コメントがされたのを確認した後、[Actions]タブをクリックしてみると、GithubActionsが`/kuroco stage`のコメントに反応し、プレビューデプロイを開始していることが確認できます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e418ce8668741af1028ec8e5a1e6f571.png)

PullRequestの画面に戻り、しばらく後に画面更新をすると、仮URLのリンクと一緒にプレビューデプロイのコメントが追加されていることが確認できます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a0ac2f3728fd934658696bc8a959a2.png)

仮URLのリンクにアクセスして、PullRequestの内容がデプロイされていることを確認します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f652d02b27fc9120c4e9d3a6d69fa974.png)

:::tip
プレビューデプロイで発行される仮URL上から操作したとき、CORSエラーが発生する場合、ワイルドカードで仮URLからのアクセスを許可する指定をしてください。  
仮URLは`https://ハッシュ値-サイトキー.g.kuroco-front.app`の様に発行されるため、  
`https://*-サイトキー.g.kuroco-front.app`という指定をすることで、CORSエラーを回避できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/37dd46e77bc289ad77a83018e259866f.png)
:::

## ドメインについて
KurocoFrontのドメインですが、デフォルトでは `https://サイトキー.g.kuroco-front.app` のようになります。  
独自ドメインへの変更については [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)をご確認ください。

## うまくデプロイできない場合
KurocoFrontへうまくデプロイできない場合や、エラーが表示されてしまう場合は下記をご確認ください。

- 管理画面に[KurocoFrontログ](/ja/docs/management/front-log-list/)がありますので、そちらでログのご確認をお願いします。
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/) を参考に、設定の再確認をお願いします。

また、GitHub Actionsの設定が分からない場合は[サポートのSlack](/ja/docs/about/support/)へご連絡ください。サポートいたします。

## 関連ドキュメント
- [GitHub](/ja/docs/management/github/)
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)


---

# KurocoでできるCore Web Vitalsへの対応の進め方

> 元ページ: `tutorials/core-web-vitals-with-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/core-web-vitals-with-kuroco/

## Core Web Vitalsとは
GoogleがWebサイトの健全性を示す指標として Web Vitals というものがあります。  
Core Web Vitals とは Web Vitals の中でも特に重要なLCP、FID、CLSのことを示します。

### LCP (Largest Contentful Paint) とは
LCPとは、「最大視覚コンテンツの表示時間」つまり、「ページのメインとなる最も大きなコンテンツが表示されるまでの時間」を示す指標になります。表示されるまでの時間が2.5秒以内だと「良い」とされます。  
主に以下の要素が対象となります。

- `<img>` 要素
- `<svg>` 要素内の `<image>` 要素
- `<video>` 要素
- CSSの`url()`を介して読み込まれた背景画像
- テキストノードやその他のインラインレベルのテキスト要素の子要素を含むブロックレベル要素

### FID (First Input Delay) とは
FIDとは、「初回入力までの遅延時間」つまり、「ユーザーが最初にページを操作（リンクのクリック、ボタンのタップ、キーの押下など）を行った際の反応速度」を示す指標になります。  
その際、スクロールとズームイン・ズームアウトは操作の対象外となります。ページ操作時の反応速度が0.1秒以下だと「良い」とされます。

### CLS (Cumulative Layout Shift) とは
CLSとは、「累積レイアウト シフト数」つまり、「ページの表示中に発生したレイアウトのズレ」を示す指標になります。  
レイアウトのズレはページの操作や視覚的なUXの低下に繋がってしまいます。CLSのスコアが0.1以下だと「良い」とされます。  
よくあるものだと、画像の読み込みの度に他の要素がズレてしまったり、JavaScriptやCSSでコンテンツを非同期で読み込んで他の要素がズレてしまうといったものが該当します。

## SEOへの影響
Core Web Vitals はGoogle検索結果の評価に関わる[ページエクスペリエンスシグナル](https://developers.google.com/search/docs/advanced/experience/page-experience?hl=ja)へ追加されたため、Google検索結果のランキング（SEO）にも影響します。  
ページエクスペリエンスシグナルは他にも以下のようなものがあります。

- モバイルフレンドリーであるか
- HTTPSで配信されているか
- 煩わしいインタースティシャルがないか

## Core Web Vitals のスコアを計測するツール
[Core Web Vitals を測定するためのツール](https://web.dev/i18n/ja/vitals-tools/)には、Lighthouse、PageSpeed Insights、Search Consoleなどがあります。  

## Core Web Vitals のスコア改善について
### LCPスコア

LCPのスコアが低下する原因として以下が考えられます。

- サーバーの応答速度が遅い
- レンダリングを妨げるJavaScriptとCSSによる影響
- JavaScript、CSS、画像といったリソースファイルの読み込みが遅い
- クライアントサイドでのレンダリング

LCPのスコアを改善するには以下が有効です。

- サーバーの応答速度を改善する
- レンダリングを妨げるJavaScriptやCSSを削減する
- リソースファイルのサイズなどの読み込みを改善する
- 外部ファイルの読み込みの順番を改善する（`<link rel="preconnect">`の指定など）
- レンダリング方法を改善する

#### Kurocoで簡単にできるLCPのスコア改善
KurocoではCDNを利用しているため、JavaScript、CSS、画像といったリソースファイルを高速に配信できますので、「サーバーの応答速度」に関しては問題にはなりません。  
APIレスポンスもキャッシュ設定ができますので、適切にキャッシュの設定を実施してください。  
また、画像は次世代フォーマットであるwebpでの配信やURLパラメータベースのリサイズにも対応しています。  
適切にコーディングをしていただければ「リソースファイルのサイズなどの読み込みを改善する」は比較的容易に対応が可能です。  

### FIDスコア
主にFIDのスコアが低下する原因として以下が考えられます。

- JavaScriptやCSSファイルに必要のないコードが含まれており、サイズが肥大化している
- JavaScriptのロジックの問題で実行にかかる時間が遅い
- 広告やSNSボタンといったサードパーディのJavaScriptによる影響
- コーディングの問題やサイトの要件によりリクエスト数が多い

FIDのスコアを改善するには以下が有効です。

- 処理に時間のかかるJavaScriptのロジックを改善する
- 広告、SNSボタンといったサードパーティのJavaScriptを削減・非同期で読み込む
- リクエスト数を減らすなど読み込みの順番を調整して、リソースの読み込み待ち時間を少なくする

#### KurocoでできるFIDのスコア改善
KurocoはAPI中心設計のヘッドレスCMSのため、Nuxt.jsやNext.jsといったJavaScriptフレームワークと相性が良いです。  
また、ホスティング機能を持った[KurocoFront](/ja/docs/about/kurocofront/)を利用することで、CDNを利用した静的コンテンツを高速で配信できます。  
KurocoとJavaScriptフレームワークを利用することで、FIDスコアの良いサイトの構築を行えます。  
LCPとCLSの改善をするとFIDスコアも改善しますので、複雑なサイトでない限りFIDの調整は最後で構いません。

### CLSスコア
CLSのスコアが低下する原因として以下が考えられます。

- `<img>`や`<video>`要素にサイズが指定されていない
- 広告や`<ifame>`といった埋め込み要素にサイズが指定されていない
- コンテンツが動的に読み込まれている
- Webフォントの読み込み遅延によりFOUT（チラつき）が発生している

CLSのスコアを改善するには以下が有効です。

- `<img>`や`<video>`要素に`width`と`height`を指定する
- 広告、`<iframe>`、動的なコンテンツを読み込む場合はサイズを指定するか、CSSで予めスペースを確保する
- Webフォントの読み込みを最適化する（`<link rel=”preload”>`の指定など）

#### KurocoでできるCLSのスコア改善
Kurocoでは画像のURLにパラメータを付与することで動的変換を行えます。  
`<img>`要素のサイズ指定に併せて、画像のURLに`width`パラメータを指定することでサイズが固定された画像の配信が可能です。

また、以下のように`srcset`と画像のURLへの`width`パラメータを組み合わせることで、解像度の異なる画像を複数用意せずにレスポンシブへの対応も可能です。

```html
<picture>
  <source media="(max-width: 799px)" srcset="example.jpg?width=400" /><!-- ビューポートの横幅が799px以下のデバイスで表示 -->
  <source media="(min-width: 800px)" srcset="example.jpg?width=800" /><!-- ビューポートの横幅が800px以上のデバイスで表示 -->
  <img src="example.jpg" alt="サンプル画像" />
</picture>
```

## 参考
このチュートリアルでは、Core Web Vitalsの一般的な概要を説明しました。Core Web Vitals についてさらに詳しく知るには、以下のリンクを参照してください。

**Web Vitals と Core Web Vitals**    
* [Web Vitalsについて - web.dev](https://web.dev/i18n/ja/vitals/)

**LCP (largest contentful paint)**    
* [Largest Contentful Paint (LCP) - web.dev](https://web.dev/i18n/ja/lcp/)
* [Largest Contentful Paint を最適化する - web.dev](https://web.dev/i18n/ja/optimize-lcp/)

**FID (first input delay)**    
* [FID (First Input Delay) - web.dev](https://web.dev/i18n/ja/fid/)
* [First Input Delay を最適化する - web.dev](https://web.dev/i18n/ja/optimize-fid/)

**CLS (cumulative layout shift)**    
* [Cumulative Layout Shift (CLS) - web.dev](https://web.dev/i18n/ja/cls/)
* [Cumulative Layout Shift を最適化する - web.dev](https://web.dev/i18n/ja/optimize-cls/)

**画像の動的変換**    
* [画像の動的変換について](/ja/docs/reference/api-convert-image/)

## 関連ドキュメント
- [Webサイトのパフォーマンス改善について](/ja/docs/tutorials/website-performance-tuning-with-kuroco/)
- [APIのキャッシュについて](/ja/docs/reference/api-cache/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# コーポレートサンプルサイトをSSGにする

> 元ページ: `tutorials/corporate-sample-site-to-ssg` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/corporate-sample-site-to-ssg/
> 概要: コーポレートサイトの会社概要やニュースのページなど、表示する内容をバックエンドから都度取得する必要のないページは、デプロイ時に予め生成しておくことで、APIリクエストの数を減らし、表示も高速にすることが可能です。本チュートリアルでは、コーポレートサンプルサイトの特定ページをSSGの構成に変更する手順を学びます。

## 概要
コーポレートサンプルサイトはサイト全体がCSRの構成になっています。  
これは、Kuroco管理画面での更新が即確認できる。ページ毎にクライアントサイドの処理かサーバーサイドの処理かを意識する必要が少ない。という利点があり、フロントエンドの構築にまだ馴染みがないユーザーにとって分かりやすい構成です。  

コーポレートサイトの会社概要やニュースのページなど、表示する内容をバックエンドから都度取得する必要のないページは、デプロイ時に予め生成しておくことで、APIリクエストの数を減らし、表示も高速にすることが可能です。

本チュートリアルでは、コーポレートサンプルサイトの特定ページをSSGの構成に変更する手順を学びます。

:::info
CSRとSSGの違いについて、詳しくは[Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)を参照してください。
:::

### 前提条件
このチュートリアルでは、コーポレートサンプルサイトの利用が可能な状態になっていることを前提とします。
まだの場合は以下のチュートリアルを実施してください。

:::info
[コーポレートサンプルサイトを利用する](/ja/docs/tutorials/kuroco-corporate-sample-site/)
:::

HTMLレンダリング方式の変更はフロントエンド側の作業で完結します。
不明点がある場合はNuxt.jsのドキュメントを参照してください。

:::info
https://nuxt.com/docs/guide/
:::

## レンダリング方式をSSGに変更する
### 対象ページに`<ClientOnly>`を追加する
デプロイ時はレンダリングをせず、クライアントサイドでのみ生成される箇所には`<ClientOnly>`を追加します。  
コーポレートサンプルサイトの場合、プレビューページなど、レンダリング方式に関わらずクライアントサイドでのみ生成される箇所については既に`<ClientOnly>`が明示的に追加されていますので、ここでは以下の2ファイルに`<ClientOnly>`を追加します。

- `/pages/ltd-news/detail/[slug].vue`

```diff
 <template>
+  <ClientOnly>
   <div>
     <UiPageHeader
       :path="[{ label: '会員限定コンテンツ', to: '/ltd-news/' }]"
```
```diff
       </template>
     </div>
   </div>
+  </ClientOnly>
 </template>

 <script setup>
```

- `/pages/mypage/edit/index.vue`

```diff
 <template>
+  <ClientOnly>
   <div>
     <UiPageHeader
       :path="[{ label: 'マイページ', to: '/mypage/' }]"
```
```diff
       </div>
     </section>
   </div>
+  </ClientOnly>
 </template>

 <script setup>
```

### SSGにするページのエンドポイントへのリクエストを調整する
エンドポイントからのデータを取得をサーバーサイドから実施するため、useFetchのserver: falseオプションを削除します。

例：`/pages/contact/index.vue`
```diff
 const { data: response } = await useFetch(
   `${config.public.kurocoApiDomain}/rcms-api/1/inquiry/1`,
   {
     credentials: "include",
-     server: false,
   }
 );
```

対象は8ファイル10箇所あります。

|ページ|エンドポイント|
|:--|:--|
|`/pages/index.vue` |/rcms-api/1/news/list<br/>/rcms-api/1/ltd-news/list|
|`/pages/company/index.vue`  |/rcms-api/1/content/details/company|
|`/pages/contact/index.vue`  |/rcms-api/1/inquiry/1 (GET)|
|`/pages/news/detail/[id].vue`  |/rcms-api/1/news/details/<br/>/rcms-api/1/master|
|`/pages/news/index.vue`  |/rcms-api/1/master|
|`/pages/preview/news.vue`  |/rcms-api/1/master|
|`/pages/privacy/index.vue`  |/rcms-api/1/content/details/privacy|
|`/pages/service/index.vue`  |/rcms-api/1/content/details/service|

### サイト全体をSSGの構成にする
`nuxt.config.ts` を編集して、アプリケーション全体のサーバーサイドレンダリングを有効にします。
`ssr: false`の部分を`ssr: true`に変更します。

```ts
import { defineNuxtConfig } from 'nuxt/config';

export default defineNuxtConfig({
  ssr: true, //サーバーサイドレンダリングを有効化
  runtimeConfig: {
    public: {
      kurocoApiDomain: 'https://**********.g.kuroco.app',
    },
  },
  app: {
    head: {
      title: 'front_nuxt_corporate',
  ・
  ・
  ・
```

ここまで実施したら`npm run dev`で表示の確認をします。
エラーが出る場合は修正漏れなどがないか再度確認してください。

### デプロイする
表示に問題が無ければ変更をプッシュしてデプロイします。  
ビルドが成功して表示が確認できたらレンダリング方式の変更は完了です。  

## バックエンドの変更の反映方法
SSGの構成になると企業情報のページなどはユーザーのアクセス時にAPIリクエストを送らなくなります。  
これにより、事前に生成したHTMLを表示するため高速になりますが、再ビルドを実施するまでKuroco管理画面での変更が反映されなくなります。

例えば、Kuroco管理画面から企業情報のコンテンツを更新しても、これだけではフロントエンド側の表示は更新されません。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9049f026693b8bf23439a3b600baba17.png)

コンテンツの更新をフロントエンド側に反映させるには、[GitHub](/ja/docs/management/github/)のページで[Githubの連携対象]のブランチが設定してある状態で、
コンテンツ更新時に[Github Actions ワークフロー]を有効にして更新してください。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c2e640cbbafee5e78bb49493745e2e1.png)

これにより、コンテンツ更新時にGitHub Actionsが実行され、フロントに反映されます。

:::info
[SSGにしています。コンテンツ更新後すぐにフロントに反映させるにはどうしたらいいですか？](/ja/docs/faq/how-do-i-reflect-updated-ssg-contents-on-the-frontend/)
:::

他には、変更を反映したいタイミングで[GitHub](/ja/docs/management/github/)ページの[Run Deployment]をクリックすることでもGitHub Actionsの実行が可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c709e49ba7327bf4f6c1a86bd796839.png)

## ニュースページのアーカイブの表示ついて
コーポレートサンプルサイトのニュースページに表示しているアーカイブは、事前にバッチ処理でコンテンツ数を集計し、マスタに保存した値をAPIで呼び出して利用しています。  

**フロント**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe5a45d0d0f0595204ed7cf46fffbbf6.png)

**マスタ**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c9adbb823b5a1f4d4d5e85db229244f4.png)

**バッチ処理**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad825c0c586c68fcd2aa2f67d0684448.png)

ユーザーのアクセス毎に、集計のためのAPIリクエストをする必要がないため、APIリクエストの数を削減できますが、コンテンツの更新やデプロイのタイミングによって、コンテンツ数の値がずれることがあります。  

アーカイブの作成については、以下の方法もありますのでコンテンツの更新頻度やキャッシュ戦略によって検討してください。
- ユーザーのアクセスがあったタイミングでAPIを利用して集計する。その際、エンドポイントはできる限りキャッシュされたリクエストになるよう調整する。
- アーカイブの集計をコンテンツの更新後のトリガーに設定する。

## 関連ドキュメント
- [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)
- [コーポレートサンプルサイトを利用する](/ja/docs/tutorials/kuroco-corporate-sample-site/)
- [コンテンツの更新時にGitHub Actionsを自動実行する](/ja/docs/tutorials/auto-run-github-with-contents-update/)


---

# 画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて

> 元ページ: `tutorials/difference-between-kurocofiles-and-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/

Kurocoで画像やファイルを保存する場合、下記２パターンがあります。

- **KurocoFiles**を利用する
- **KurocoFront**を利用する

本チュートリアルでは、それぞれの特徴と、利用シーンに応じた適切な配置場所を解説します。

## KurocoFilesについて
KurocoFilesは管理画面から更新ができるファイルアップロード機能です。  
KurocoFiles内にあるファイルは、Kuroco管理画面[ファイルマネージャー] -> [KurocoFiles]から確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b529aa294fa9a6507fbf7ffc59a41595.png)

## KurocoFrontについて
KurocoFrontは、CDNを利用した静的コンテンツホスティングサービスです。
GitHubと連携することで、ファイルをKurocoFrontに配置できます。

参考)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)

## KurocoFilesとKurocoFrontの使い分けについて
画像・ファイルを配置するのに、KurocoFilesとKurocoFrontのどちらを利用するのが良いかをご説明します。

### KurocoFilesをおすすめする場合
コンテンツに利用する画像等、定期的に更新するファイルはKurocoFilesを利用することをおすすめします。

### KurocoFrontをおすすめする場合 
HTMLやJS/CSSなどのサイトを構成するファイル群はKurocoFrontのassetとして利用することをおすすめします。

### 注意点
主なフロントエンドフレームワークはファイルパスにハッシュを付けてキャッシュクリアをしやすいような工夫がありますので、外部に連絡するURLなどにハッシュ付きでファイルを配置することは適切でありません。  
（フロントエンドフレームワークの配置フォルダなどの機能でハッシュを付けない配置の方法もあります）  
それぞれ扱える最大ファイルサイズ（KurocoFiles: 80MB KurocoFront: 30MB）があります。大容量ファイルを扱う場合には外部サービス連携のGCS/S3をご利用ください。   


なお、KurocoFiles、KurocoFront共に画像最適化機能がありますので、その点は特に考慮する必要ありません。  
参考) [画像の動的変換について](/ja/docs/reference/api-convert-image/)

## キャッシュのクリアの仕組み
### KurocoFilesの場合
ファイル更新時に該当フォルダのCDNキャッシュがクリアされます。

### KurocoFrontの場合
GitHubからコミットハッシュ毎に一括で更新をされ、一括でCDNキャッシュがクリアされます。

## コストについて
転送料のコストは同じです。  
ただし、**KurocoFront**に関してはファイルがコミットハッシュ毎に溜まっていきますのでストレージ料金が余計にかかります。  
また、**KurocoFront**はGitHub Actionsを利用してビルド・デプロイをしております。そのため、KurocoFrontで利用するファイル容量が多い場合には、GitHub側の料金もかかってくる場合がありますのでご注意ください。

## まとめ
以上がKurocoFilesとKurocoFrontの違いです。再度まとめると以下のようになります。

| 項目 | KurocoFiles | KurocoFront |
|:-------|:-------|:-------|
| おすすめ用途 | コンテンツに利用する画像等、定期的に更新するファイル | HTMLやJS/CSSなどのサイトを構成するファイル | 
| 管理している場所 | Kuroco管理画面 | GitHubリポジトリ |
| キャッシュのクリアタイミング | ファイル更新時 | GitHubからコミットハッシュ毎に一括で更新後 | 
| コスト | ストレージ・転送量のコスト | ストレージ・転送量のコストとGitHub Actionsコスト | 
| 最大ファイルサイズ | 80MB | 30MB | 

おすすめ用途を記載しておりますが、必ずこちらの運用をしなくてはいけないということではないので、サイト運用者と相談の上決定してください。  
ご不明点ございましたら[お問い合わせフォーム](https://kuroco.zendesk.com/)よりご連絡ください。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [KurocoFilesディレクトリとドメインの使い分けについて](/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [サイト内で利用している静的ファイル（画像、JS、CSSなど）はどこに配置するのが良いでしょうか？](/ja/docs/faq/how-to-place-static-files/)


---

# 会員制サンプルサイトの解説

> 元ページ: `tutorials/explanation-of-kuroco-sample-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/explanation-of-kuroco-sample-site/
> 概要: 本ページでは弊社がオープンソースで提供している会員制サンプルサイトをKuroco構築時のテンプレートとして利用している方向けに、サンプルサイトの構造や仕様について解説します。

本ページでは弊社がオープンソースで提供している会員制サンプルサイトをKuroco構築時のテンプレートとして利用している方向けに、サンプルサイトの構造や仕様について解説します。 

リポジトリ：https://github.com/diverta/front_nuxt_auth  
デモサイト：https://dev-nuxt-auth.g.kuroco-front.app/

## 利用しているAPIについて
会員制サンプルサイトに設定しているAPIについて解説します。  
ここでは各エンドポイントが果たす役割について解説しますので、具体的にどのようなパラメータが設定されているかは、フリートライアルから作成した自身のサイトをご確認ください。  

### 認証
|パス|モデル::オペレーション|説明|
|:--|:--|:--|
|`/rcms-api/1/login` |Login::login_challenge|ログインに使用します。<br/>こちらのエンドポイントに`email`, `password`をPOSTするとログイン処理が行われます。|
|`/rcms-api/1/logout` |Login::logout|ログアウトに使用します。<br/>こちらのエンドポイントにリクエストを送るとログアウト処理が行われます。|
|`/rcms-api/1/profile` |Login::profile|ログイン状態でリクエストを送ると、`name1`, `name2`の情報を返します。ログイン有無の確認に使用します。|
|`/rcms-api/1/reminder` |Login::reminder|パスワードリセットの機能に使用します。<br/>emailをPOSTすると、パスワードリマインダーメールが送付され、仮パスワードとトークンが発行されます。<br/>token, temp_pwd, login_pwd をPOSTするとパスワードが更新されます。|
|`/rcms-api/1/reset_password` |Login::reset_password|login_id, current_password, new_password をPOSTするとパスワードの更新ができるエンドポイントですが、会員制サンプルサイトのフロントでは使用していません。|

### コンテンツ
|パス|モデル::オペレーション|説明|
|:--|:--|:--|
|`/rcms-api/1/content/list`|Topics::list|コンテンツ定義ID=1のリストを取得するAPIです。<br/>クエリパラメータにカウント数やtopics_idを指定することで任意のデータを取り出します。|
|`/rcms-api/1/content/details/{topics_id}`|Topics::details|コンテンツの詳細を取得するAPIです。|
|`/rcms-api/1/content/category`|TopicsCategory::list|コンテンツ定義ID=1に登録されたカテゴリの一覧を取得するAPIです。|
|`/rcms-api/1/content/preview`|Topics::preview|コンテンツの保存前にプレビューを確認するためのAPIです。|
|`/rcms-api/1/content/update/{topics_id}`|Topics::update|コンテンツの更新をするAPIです。<br/>会員制サンプルサイトのフロントエンドでは使用していません。|

### メンバー

|パス|モデル::オペレーション|説明|
|:--|:--|:--|
|`/rcms-api/1/member/{member_id}`|Member::details|メンバー情報の詳細を取得するAPIです。<br/>取得できるメンバー情報はグループID=104(user)のものに限定され、ID=104(user)からのリクエストは制限されています。<br/>会員制サンプルサイトのフロントエンドではlistのAPIで代用しているため使用していません。|
|`/rcms-api/1/member/list`|Member::list|グループID=104(user)のメンバー一覧を取得するAPIです。<br/>取得する件数は1000件までとなっており、ID=104(user)からのリクエストは制限されています。|
|`/rcms-api/1/member/update`|Member::update|メンバー情報を更新するAPIです。<br/>自身の情報のみ更新できるように制限されています。|
|`/rcms-api/1/member/register`|Member::insert|メンバーの追加を行うAPIです。<br/>こちらのAPIで追加されたメンバーはグループID=104(user)のグループに所属した状態で登録されます。|
|`/rcms-api/1/member/settings`|MemberForm::details|登録できるメンバー情報の構造をレスポンスします。<br/>会員制サンプルサイトのフロントエンドでは使用していません。|
|`/rcms-api/1/member/me`|Member::details|自身のメンバー情報の詳細を取得するAPIです。<br/>自分以外のメンバー情報は取得できないように制限されています。|

### お気に入り
|パス|モデル::オペレーション|説明|
|:--|:--|:--|
|`/rcms-api/1/favorite/list`|Favorite::list|お気に入りのリストを取得するAPIです。<br/>`module_id`, `module_type`をクエリパラメータに設定してリクエストを送ることで、対象メンバーがお気に入りにしたコンテンツを取得します。|
|`/rcms-api/1/favorite/register `|Favorite::insert|お気に入りを追加するAPIです。<br/>`module_id`, `module_type`をPOSTすると[アクティビティ]->[お気に入り]にお気に入りが追加されます。|
|`/rcms-api/1/favorite/delete`|Favorite::delete|お気に入りを削除するAPIです。<br/>`module_id`, `module_type`をPOSTすると[アクティビティ]->[お気に入り]からお気に入りが削除されます。|

### フォーム
|パス|モデル::オペレーション|説明|
|:--|:--|:--|
|`/rcms-api/1/inquiry/{inquiry_id}`|InquiryForm::details|フォームの詳細を取得するAPIです。<br/>フォームの項目表示に使用します。|
|`/rcms-api/1/inquiry/1`|InquiryMessage::send|フォームの回答を送付するAPIです。<br/>フォームの入力項目をPOSTすると[チャネル] -> [WEB] -> [フォーム]のフォームID=1に回答が追加されます。|

### ファイル
|パス|モデル::オペレーション|説明|
|:--|:--|:--|
|`/rcms-api/1/upload`|Files::upload|ファイルをアップロードし、Kurocoの一時領域にファイルを格納するAPIです。<br/>フォームからファイルをアップロードする際に使用します。|

## フロントエンドと動作の仕様について
### 全般
- i18nで多言語対応しているため、テキストは`{{ $t('top.latest_articles') }}`のような記述で、/locales に設定されたテキストを取得・表示します。
- 処理の完了・エラーの際の表示は`nuxt-snackbar`のプラグインを利用しています。

### TOPページ(/) 
#### 対象ファイル  
https://github.com/diverta/front_nuxt_auth/blob/main/pages/index.vue

#### 動作の説明 
- `<Login v-if="!authUser.member_id" />`の記述により、未ログイン状態の場合は /components/Login.vue を表示します。
- /components/Login.vue でのログイン処理の際に`setSitekey()`で、APIのリクエスト先変更しています。  
  これにより、フロントエンドを共通に、バックエンド(Kuroco管理画面)を各サイトキーで切り替える動作を実現します。

- ログイン状態の場合はナビゲーション、コンテンツリスト、お気に入りリストを表示します。
- スライダー部分はVuetifyのv-carouselを利用しています。
- コンテンツのグリッド表示はコンポーネント化されており、`<TopicsGrid :topics="topicsList" />`で /components/topics/Grid.vue を呼び出し、表示しています。
- お気に入りのリスト表示はコンポーネント化されており、`<TopicsList :topics="favouriteList" />`で /components/topics/List.vue を呼び出し、表示しています。

### /topics_list
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/blob/main/pages/topics_list.vue

#### 動作の説明
- カテゴリの一覧とコンテンツの一覧を取得して表示します。
- コンテンツのグリッド表示はコンポーネント化されており、`<TopicsGrid :topics="topics" />`で /components/topics/Grid.vue を呼び出し、表示しています。
- ページネーションはVuetifyのv-paginationを利用しています。

### /topics_detail/{topics_id}
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/blob/main/pages/topics_detail/[slug].vue

#### 動作の説明
- URLからコンテンツのIDを取得し、対応するKurocoのコンテンツを表示します。
<!--
URLが/topics_detail/preview/ の場合はpreviewエンドポイントにリクエストを送り、公開前のコンテンツ情報を表示します。 
-->
- 星マークをクリックすると、/rcms-api/1/favorite/register のエンドポイントに`module_id` をpostし、お気に入り登録をします。
- お気に利登録済みのコンテンツで星マークをクリックすると、/rcms-api/1/favorite/delete のエンドポイントに`module_id` をpostし、お気に入り登録を削除します。

### /favourite
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/blob/main/pages/favourite.vue

#### 動作の説明
- アクセスすると、/rcms-api/1/favorite/list のエンドポイントでお気に入りされた`topics_id`のリストを取得します。
- その後 /rcms-api/1/content/list のエンドポイントに`topics_id`のリストをクエリパラメータで付与してリクエストを送り、お気に入りの一覧を取得しています。
- お気に入りのリスト表示はコンポーネント化されており、`<TopicsList :topics="topics" />`で /components/topics/List.vue を呼び出し、表示しています。
- フロントエンドのテーブルとページネーションは、Vuetifyのv-data-tableを利用しています。

### /member
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/blob/main/pages/member/index.vue

#### 動作の説明
- /rcms-api/1/member/list のエンドポイントで、メンバーのリストを取得して表示しています。
- 表示されるメンバーはUserのグループに所属するメンバーのみです。
- メンバーの一覧を表示できるのはAdministratorもしくはEditorのメンバーのみです。  
  フロントから登録したメンバー(User)では表示できません。
- 画面上部にある絞込みの動作はVuetifyのv-autocompleteを使用して、フロントエンド側で対応しています。
- ページネーションはVuetifyのv-paginationを利用しています。

### /member/detail/{member_id}
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/tree/main/pages/member/detail/[slug].vue

#### 動作の説明
- /rcms-api/1/member/list のエンドポイントに、URLから取得したメンバーIDをクエリパラメータで付与してメンバー詳細の情報を表示しています。


### /profile
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/blob/main/pages/profile/index.vue

#### 動作の説明
- /rcms-api/1/member/me のエンドポイントで取得した自身のprofile情報を表示します。

### /profile/edit
#### 対象ファイル
https://github.com/diverta/front_nuxt_auth/blob/main/pages/profile/edit/index.vue

#### 動作の説明
- /rcms-api/1/member/me のエンドポイントで取得した自身のprofile情報を表示します。
- submitをクリックすると /rcms-api/1/member/update のエンドポイントに入力したデータをpostします。
- フォームの表示は Formkit を利用しています。

### /inquiry
#### 対象ファイル
対象ファイル：https://github.com/diverta/front_nuxt_auth/blob/main/pages/inquiry.vue

#### 動作の説明
- /rcms-api/1/inquiry/1 のエンドポイントで取得したフォーム項目を表示します。
- フォームの表示はFormkitを利用しています。
- Submitをクリックすると、/rcms-api/1/inquiry/1 のエンドポイントにデータをPOSTします。
- 入力した内容はフォームID=1の回答に保存されます。

### /signup
#### 対象ファイル
対象ファイル：https://github.com/diverta/front_nuxt_auth/blob/main/pages/signup.vue

#### 動作の説明
- フォームの表示はFormkitを利用しています。
- Submitをクリックすると、/rcms-api/1/member/register のエンドポイントにデータをPOSTし、会員登録が完了します。
- ここから登録したメンバーはUserのグループに所属します。

### /reminder
#### 対象ファイル
対象ファイル：https://github.com/diverta/front_nuxt_auth/blob/main/pages/reminder.vue

#### 動作の説明
- Reset my passwordをクリックすると、/rcms-api/1/reminder に`email`をpostし、パスワードリセットのメールを送付します。
- パスワードリセットのメールには`login/reset_password`のメールひな形が使用され、reminderのAPIが発行したトークン情報を含みます。
- reminderのAPIが発行したトークン情報をクエリパラメータにセットした状態でアクセスすると、仮パスワードと新パスワードの入力欄を表示します。
- SUBMITをクリックすると /rcms-api/1/reminder のエンドポイントに`login_pwd`、`temp_pwd`、`token`をpostし、パスワードの更新が完了します。


## 利用しているプラグインについて
会員制サンプルサイトでは、いくつかのプラグインを使用して、フロントエンドの構築をしてます。  
主に使用しているプラグインを以下に紹介しますので、プラグイン部分の記述や仕様については各ドキュメントを参照してください。  

|プラグイン名|公式ドキュメント|
|:--|:--|
|nuxtjs/i18n|https://i18n.nuxtjs.org/|
|Vuetify|https://vuetifyjs.com/getting-started/installation/|
|Formkit|https://formkit.com/|
|Nuxt Snackbar|https://nuxt.com/modules/snackbar|

## 関連ドキュメント
各機能の実装方法については各チュートリアルを準備しています。  
チュートリアルではシンプルなコードで機能の実装方法を紹介していますので是非ご確認ください。
- [会員制サンプルサイトをコピーして、Kurocoで会員制サイトを構築する方法](/ja/docs/tutorials/building-a-membership-website-on-kuroco-from-the-sample-site-template/)
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [KurocoとNuxt.jsで、多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)
- [パスワードリマインダー/パスワードリセットを設定する](/ja/docs/tutorials/how-to-use-password-reminder/)
- [フロントエンドを一つのサーバにして、サイトキーを使ってバックエンドを切り替える](/ja/docs/tutorials/one-server-for-front-end-and-switch-back-end-using-site-key/)


---

# figma-design-guide

> 元ページ: `tutorials/figma-design-guide` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/figma-design-guide/

# Figma デザイン設計 ガイドライン

:::caution 注意
実際には案件によって必要とされる仕様や要求内容は異なります。最終的には案件毎に確認をするようにしてください。
:::

**コンポーネントベース設計（Next.js / React 対応）**

| 項目 | 内容 |
|------|------|
| 件名 | Figma デザイン設計（コンポーネントベース） |
| 対象フレームワーク | Next.js（React）[案件ごとに設定する] |
| スタイリング | プレーン CSS / Tailwind CSS |
| 想定担当者 | UI デザイナー / デザインシステム担当者 |

---

## 1. 依頼背景と目的

本案件では、フロントエンドフレームワークとして Next.js（React）を採用しています。実装工程を円滑に進めるため、デザイン段階からコンポーネントベースの思想を取り入れた Figma 設計を推奨します。

デザインデータがコードへスムーズに変換できるよう、以下のルールおよびガイドラインに沿って設計してください。

---

## 2. Figma 設計の基本方針

### 2-1. コンポーネントベースの粒度設計

コンポーネントベースで設計し、粒度を意識して整理してください。

**Step 1 — Styles の定義**

コンポーネントを作成する前に、Figma の Styles または Variables として以下を定義してください。

- **Color Style**: Primary / Secondary / Semantic / Neutral 等のカラー
- **Text Style**: Font Family・Size・Weight・Line Height の組み合わせ
- **Effect Style**: Shadow（elevation レベルに対応）

**Step 2 — Components の構成**

Styles を参照する形でコンポーネントを作成し、以下の分類で整理してください（分類名はチームの共通言語として機能することを優先します）。

- **Primitives（最小部品）**: アイコン、バッジ、ラベルなど、それ以上分割できない最小コンポーネント
- **Components（部品）**: ボタン、入力フィールド、カード、モーダルなど、見た目と振る舞いが固定された再利用部品
- **Patterns（構造）**: ヘッダー、フォームレイアウト、一覧ページなど、Components を組み合わせた柔軟なレイアウトガイドライン

> ※ コンポーネント名は英語で命名し、React コンポーネント名（PascalCase）に対応する名称を付けてください（例: `PrimaryButton`、`CardItem`）。分類名はチームの共通言語として機能することを優先し、厳格な階層ルールへの縛りより「見ればわかる命名」を重視してください。

### 2-2. Auto Layout の徹底

実装時のレスポンシブ対応を見据え、すべてのコンポーネントは Auto Layout を使用して設計してください。

- 横方向・縦方向どちらの伸縮が想定されるかを明示してください
- Padding・Gap・Min/Max Width の値は CSS 実装で使用できるよう `px` 単位で統一してください
- コンテンツが増減する場合を考慮した伸縮設定（Fill / Hug / Fixed）を適切に使い分けてください
- 各要素の制約（Constraints）を適切に設定してください（親フレームのリサイズ時の振る舞いに対応）

### 2-3. Variants の設定

状態変化や種別のあるコンポーネントは、Variants を使って一元管理してください。

Variants のプロパティ名は camelCase で、内容が一目でわかる適切な名称を設定してください（例: `state`、`size`、`variant` など）。

- ボタン: `state=default` / `state=hover` / `state=disabled` / `state=loading`
- フォーム入力: `state=default` / `state=focus` / `state=error` / `state=disabled`
- サイズバリエーション: `size=small` / `size=medium` / `size=large` など

> ※ Variants の名称は、CSS の data 属性（`data-state="hover"` 等）や aria 属性に対応できる命名にしてください。プロパティ名・値ともに camelCase で統一してください（例: `state=default`、`size=medium`）。

### 2-4. コンポーネントプロパティの設定

Variants 以外のコンポーネントプロパティも積極的に活用してください。

- **Boolean プロパティ**: パーツの表示・非表示を制御するフラグ（例: `showIcon`、`hasLabel`）
- **Text プロパティ**: ラベルや説明文など、差し替え可能なテキストを定義（例: `label`、`placeholder`）
- **Instance swap プロパティ**: アイコンや内部コンポーネントを差し替え可能にする（例: `icon`、`leadingElement`）
- **Slot プロパティ**: 子コンテンツを差し込める領域を定義する（例: `prefix`、`suffix`、`children`）

> ※ プロパティ名は camelCase で命名し、React の Props 名と対応させてください。

### 2-5. レイヤー命名規則

Figma の自動命名（`Frame 42`、`Group 7` 等）は使用しないでください。レイヤー名はコードのコンポーネント名・変数名と対応できるよう、以下の規則で命名してください。

- コンポーネント名は PascalCase（例: `PrimaryButton`、`CardItem`）
- プロパティ名は camelCase（例: `variant`、`isDisabled`、`showIcon`）
- レイアウト用フレームは役割がわかる名称（例: `layout/container`、`section/hero`）
- アイコンは `icon/` プレフィックス ＋ PascalCase で統一（例: `icon/ArrowRight`、`icon/CheckCircle`）

> ※ AI ツールやコード生成ツールはレイヤー名を識別の基準とするため、意味のある命名はコード品質に直結します。

### 2-6. 仕様注釈

デザインだけでは伝わりにくい仕様・挙動・意図は、該当フレームやコンポーネントの近くにテキストで注釈を記載してください。実装者が見ればすぐわかる位置に置いてください。

> ※ Figma のコメント機能は一時的なメモや確認・フィードバックのやりとりにのみ使用してください。仕様の説明にはコメントではなく、キャンバス上のテキストで記載してください。コメントは対応完了後に解決済みとしてください。

---

## 3. デザイントークンの定義

CSS カスタムプロパティ（CSS Variables）への変換を前提に、以下のデザイントークンを Figma の Styles または Variables として定義してください。

### 3-1. カラートークン

- Primary / Secondary / Accent カラーとそれぞれの段階値（100〜900）
- Semantic カラー: `success` / `warning` / `error` / `info`
- Neutral / Gray スケール
- 背景色・テキスト色・ボーダー色

### 3-2. タイポグラフィトークン

- Font Family（Web フォント名を明示）
- Font Size
- Font Weight
- Line Height / Letter Spacing

### 3-3. スペーシングトークン

スペーシングスケールを定義する場合は、4px または 8px ベースを推奨します（例: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px）。

### 3-4. その他のトークン

- Border Radius（`sm` / `md` / `lg` / `full`）
- Shadow（elevation レベルに対応）
- Z-index スケール（必要に応じて）

### 3-5. トークンの命名規則とエクスポート形式

CSS Variables や実装ツールへの変換精度を高めるため、以下の規則に沿って命名・エクスポートしてください。

**命名規則**: `/` 区切りで `{category}/{group}/{name}` の形式を基本とします。Figma の Style パネルでも `/` がグループ区切りとして機能するため、Style 名とトークン名を統一してください。

```
color/primary/default
color/primary/hover
color/semantic/error
typography/body/md
spacing/md
radius/lg
shadow/elevation/1
```

**エクスポート形式**: Tokens Studio 等のプラグインを使用し、JSON 形式でエクスポートできる状態にしてください。Style Dictionary や CSS Variables への変換を前提とした構造で定義をお願いします。

---

## 4. 状態の設計

実装では data 属性または aria 属性を用いて状態管理を行います。デザイン上の状態変化は以下の方針で Figma に反映してください。

- インタラクティブな UI は必ず全状態のデザインを提供してください
  - 例: ボタン → `state=default` / `state=hover` / `state=active` / `state=disabled` / `state=loading`
  - 例: アコーディオン → `state=closed` / `state=open`
  - 例: モーダル → `state=hidden` / `state=visible`
- アニメーションやトランジションが想定される箇所には、遷移前後のフレームを両方用意し、備考にトランジション秒数・イージングを記載してください
- エラー状態・空状態（データなし）・ローディング状態のデザインも必ず含めてください

---

## 5. レイアウトとレスポンシブ設計

### 5-1. ブレークポイント

以下のブレークポイントに対応するデザインを納品してください（変更がある場合は事前にご相談ください）。

| 名称 | 画面幅 | 備考 |
|------|--------|------|
| Mobile (sm) | 〜 767px | スマートフォン縦表示 |
| Tablet (md) | 768px 〜 1199px | タブレット / 横表示 |
| Desktop (lg) | 1200px 〜 | PC 標準 |

### 5-2. グリッドシステム

- 各ブレークポイントで使用するカラム数・ガター幅・マージン幅を Figma の Grid 設定として明示してください
- コンテンツ最大幅（Max Width）を指定してください

---

## 6. Figma ファイル構成

Figma ファイルは以下のページ構成で整理してください。

| ページ名 | 内容 |
|----------|------|
| Cover | ファイル概要・更新履歴 |
| Design Tokens | Styles / Variables の定義一覧（必要に応じて） |
| Components | 全コンポーネントのライブラリ（Primitives → Components → Patterns の順） |
| Pages | 各ページのデザイン（PC / SP 両対応） |
| Prototypes | 主要なインタラクション・フローのプロトタイプ（必要な場合） |

> ※ コンポーネントのページでは、各コンポーネントの Description 欄に以下の形式で Props と用途を記載してください。AI ツールやコード生成ツールはこの欄を参照してコードを生成するため、省略しないようにお願いします。
>
> ```
> Component: PrimaryButton
> 用途: 主要アクション用のボタン。フォーム送信・確認操作などに使用。
> Props:
>   - variant: primary | secondary | ghost
>   - size: sm | md | lg
>   - disabled: boolean
>   - loading: boolean
> ```

---

## 7. 納品・やり取りのルール

### 7-1. 共有方法

- Figma のファイル共有リンク（編集権限）を実装担当者へ共有してください
- 共有先アドレスは別途ご連絡します
- コンポーネントのマスターが別ファイルに存在する場合は、そのファイルも実装担当者が閲覧・アクセスできるよう共有してください

### 7-2. レビュー・フィードバック

- フィードバックは Figma のコメント機能を使用します
- 修正対応は原則 [案件ごとに設定する] 営業日以内での反映をお願いします
- 大幅な仕様変更が生じる場合は事前に[案件ごとに設定する]にてご相談ください

### 7-3. エクスポート・アセット

- 画像アセット（アイコン・イラスト等）は SVG または PNG（2x）形式でエクスポート可能な状態にしてください
- フォントは Google Fonts または Web フォントで代替可能なものを使用するか、ライセンスを明示してください

### 7-4. 禁止事項・注意事項

- コンポーネントのフラット化（Flatten）は避け、レイヤー構造を維持してください
- Third-party プラグイン固有の機能に依存したデザインは、実装への影響がある場合があるため事前確認をお願いします

---

## 8. 連絡先・担当者

| 項目 | 内容 |
|------|------|
| 実装担当者 | （担当者名・部署を記入） |
| 連絡方法 | （メール / Slack / チャットツール等を記入） |
| デザイン確認フロー | Figma コメント → 担当者確認 → 承認 |
| 質問・相談 | 作業開始前に不明点は必ずご確認ください |

---

以上

## 関連ドキュメント
- [Kurocoを利用したプロジェクトの進行イメージ](/ja/docs/tutorials/starting-a-project-on-kuroco/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# コンテンツ一覧/詳細ページを作成する

> 元ページ: `tutorials/integrate-kuroco-with-nuxt` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrate-kuroco-with-nuxt/
> 概要: Kurocoを利用したプロジェクトで、コンテンツ定義「お知らせ」の一覧と詳細画面を表示させる方法を解説します。本チュートリアルではフロントエンドのコードとして、Nuxt.jsとNext.jsを紹介します

Kurocoを利用したプロジェクトで、コンテンツ定義「お知らせ」の一覧と詳細画面を表示させる方法を解説します。  
本チュートリアルではフロントエンドのコードとして、Nuxt.jsとNext.jsを紹介します。  

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
Next.js: v13.4.12 (Using App Router)
:::

:::info
このページはKurocoでのプロジェクトが構築済みであることを前提としています。    
まだ構築していない場合は、下記のチュートリアルを参照してください。  
Nuxt.js：[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
:::

## Kurocoの設定
### コンテンツの作成
まずはKuroco管理画面でコンテンツを作成します。  
[コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)ページを参考に、コンテンツ定義「お知らせ」を作成してください。 

「本文の入力方法」はWYSIWYGをチェックしてください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4805adb8844b1fea28e104622b4c01eb.png)
:::tip
作成した/利用するコンテンツの閲覧制限/編集制限は、「選択なし」を設定してください。  
閲覧制限/編集制限については、[こちら](/ja/docs/management/content-structure-topics-group/#詳細設定)を参考にしてください。
:::

次に、作成したコンテンツ定義「お知らせ」より、コンテンツを作成してください。  
今回は下記のように作成しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae67e6f93d596b60bc7a63b6170185d7.png)
以上でコンテンツ作成は完了です。  

### API基本設定を行う
続いてAPIの登録をします。  
Kurocoの管理画面から[API]->[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4d7ef47c9d0738cd5098b94292fce296.png)
[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef2bcacd07dd7f3cd0c40c84c172adc7.png)
タイトル、版、ディスクリプションを入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a2e698ab7eb8c30fe9a36d8a0261197.png)
追加したAPIに遷移しますので、続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d04bb87a4ba10a6c4b880eebcbd5bb86.png)
[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
注意)  
Cookieをセキュリティ用のトークンとして利用する場合、APIドメインとフロントエンドのドメインが違うとサードパティクッキーの問題があり、Safari等で認証が効きません。  
フロントエンドとAPIドメインをサブドメイン違いで設定をする必要があるので、[独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)でAPIドメインを設定し、[アカウント設定](/ja/docs/management/account/)からAPIドメインを変更ください。  
（Chromeでは正常に動作しますので、開発やテストの段階ではまずChromeで構築していただくことをお勧めします。）

### CORS設定を行う
[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/50afffbe729d7ba6f16fab9b68a0bd9a.png)
CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000/`
- フロントエンドドメイン

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET  
- POST

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5d8e6972c8e08cd8b9cd271f3568f72.png)
問題なければ [保存する] をクリックします。

### エンドポイントを設定する

次に先ほど作成したコンテンツ「お知らせ」を取得するエンドポイントを作成します。  
今回は、「お知らせ一覧」と「お知らせ詳細」の２つのエンドポイントを作成します。

まずはお知らせ一覧のエンドポイントを作成します。  
[新しいエンドポイントの追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f0109322da45dd0e95744b5e95ac235.png)
下記記載します。
- パス：news
- カテゴリー：コンテンツ
- モデル：Topics
- オペレーション：list

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6eb9c78fc92400a1a27f11b09e6d521d.png)
また、基本設定にある「topics_group_id」にコンテンツ定義「お知らせ」のグループIDを入力してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8d81395bb2f4b2591a6e49e42194ba1.jpg)
参考) グループIDはコンテンツ定義一覧画面より確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2943721f7311f069b683ab3a6589217.png)
全て入力したら、画面上部または下部の「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62be9272f7d5dbb96c64556db6c85cbd.png)
以上で「お知らせ一覧」のエンドポイント作成完了です。

次に「お知らせ詳細」のエンドポイントを作成します。
一覧の時と同様に、[新しいエンドポイントの追加] をクリックし、下記記載します。

- パス：newsdetail
- カテゴリー：コンテンツ
- モデル：Topics
- オペレーション：details
- topics_group_id：任意のグループID

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef073b308ed5ba13eb3217c650731229.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1225101529053e46760eedfe1808624b.png)
全て入力したら「追加する」をクリックします。

以上でKurocoの設定が完了です。


## フロントエンドの実装

実際にKurocoで作成したコンテンツをフロントエンドで表示します。

### ファイル作成

フロントエンドのフレームワークをインストールしたディレクトリに、下記構造にてファイル作成します。  
今回は`/news/`、`/news/slug`のディレクトリ名でページが表示できるようにファイルを作成しました。

**Nuxt2:**

```
pages
 - news
   - _slug.vue
   - index.vue 
```

**Nuxt3:**

```
pages
 - news
   - [slug].vue
   - index.vue 
```

**Next.js:**

```
app
 - news
   - [slug]
     - page.jsx
   - page.jsx
```


### 一覧ページの作成
一覧ページは以下のように記載します。

**Nuxt2:**

```markup reference title="/pages/news/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_list.vue
```

**Nuxt3:**

```markup reference title="/pages/news/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_list.vue
```

**Next.js:**

```jsx reference title="/app/news/page.jsx"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nextjs/news_list.jsx
```


注意) 
`/rcms-api/4/news`の箇所は、Kuroco管理画面に記載のパスをご記入ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2ae827a91b1617876dc4724deff9ae9.png)
上記保存し、`http://localhost:3000/news`にアクセスすると下記のような画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6876536ed2faee86e4771dc28732cea.png)

### 詳細ページの作成
詳細ページは以下のように記載します。  

**Nuxt.2:**

```markup reference title="/pages/news/_slug.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_details.vue
```

**Nuxt3:**

```markup reference title="/pages/news/[slug].vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_details.vue
```

**Next.js:**

```jsx reference title="/app/news/[slug]/page.jsx"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nextjs/news_details.jsx
```


注意) `/rcms-api/4/newsdetail/` の箇所は、Kuroco管理画面に記載のパスをご記入ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/87fc99efae91526e9ce8814cbd22e05b.png)
上記保存し、お知らせ一覧画面のタイトルをクリック、すると下記のように詳細画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ffe471b014934535d6536a330947a70.png)
## まとめ
以上でKurocoでお知らせ一覧/詳細ページを実装する説明を終わります。うまく表示されましたでしょうか。  
このリファレンスでは下記のことが学べます。

- KurocoのAPI設定
- Nuxt.js/Next.jsでKurocoコンテンツの表示

こちらを応用し、ご自身のサイトを構築してみて下さい。

## 関連ドキュメント
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [コンテンツ一覧ページにページネーションを実装する](/ja/docs/tutorials/splitting-the-contents-list-into-multiple-pages/)
- [API](/ja/docs/management/api-list/)


---

# プレビュー画面を構築する

> 元ページ: `tutorials/integrate-preview-page` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrate-preview-page/
> 概要: Kurocoを利用したプロジェクトで、プレビューの利用方法を紹介します。本チュートリアルではフロントエンドのコードとして、Nuxt.jsとNext.jsの2種類を紹介します。

Kurocoを利用したプロジェクトで、プレビューの利用方法を紹介します。  
本チュートリアルではフロントエンドのコードとして、Nuxt.jsとNext.jsの2種類を紹介します。

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
Next.js: v13.4.12 (Using App Router)
:::

:::info
このページはKurocoでのプロジェクトが構築済みであることを前提としています。    
まだ構築していない場合は、下記のチュートリアルを参照してください。  
Nuxt.js：[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
:::

## プレビューとは

コンテンツのプレビューを行う機能です。

コンテンツを作成/編集する際に、
コンテンツの内容を更新することなく、
ひとまずWEBページ上での作成/編集後の画面を確認したいときに便利な機能です。

[コンテンツ編集](/ja/docs/management/content-structure-topics/)の[プレビューを確認する]ボタンでプレビューでき、
[更新する/途中保存する]ボタンによるコンテンツの変更をしていない場合でも、
即時で編集している内容をプレビューできます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/75499043371ee8cf6273a1dfd4abf99f.jpg)
この機能は初期状態では動作せず、
各種設定とフロントエンド側のコーディングが必要となります。

この記事では、Kurocoのプレビューをフロントエンドで表示するための手順を紹介します。

## プレビューする画面のURLを設定する

[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)
画面の[プレビューの対象とするページのURL]に、
プレビューする画面のURLを設定します。

ここでは`http://localhost:3000/news_preview`画面へリンクするように設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdfa79d59a963ac623ee13567c9893c0.png)

下記のうちどちらかのURLが
`プレビューを確認する`ボタンのリンク先に設定されます。
- 相対パスを指定された場合は、[フロントエンドドメイン] + 相対パス のURL
- プロトコルを含んだURLが指定された場合は、そのURL

リンクには、
新規に生成されたワンタイムトークンを含んだ
URLクエリパラメータが付加されます。

`${URL}?preview_token=aaaAAA000999&validUntil=1234567890`

### 絶対パス、相対パスについて

画像の例では絶対パスを指定していますが、
相対パスを指定した場合
例えば[フロントエンドドメイン]が下記の画像の通りで  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/02b31850268804b0710212658308d01c.png)  
`プレビューの対象とするページのURL`が下記の画像のとき  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/df197dd33d942ee9190b805d339d713b.png)  
リンク先のURLは
`https://kuroco-dev.web.app/sub/feed/preview/?preview_token=aaaAAA000999&validUntil=1234567890`
となります。

[フロントエンドドメイン]は、[アカウント設定](/ja/docs/management/account/)で確認/変更ができます。

### 設定の確認

実際にプレビューボタンのリンク先が設定したURLとなっているかを確認します。

[コンテンツ編集](/ja/docs/management/content-structure-topics/)画面の、
[プレビューを確認する]ボタンをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/690836d6c1381d127ee689e3a3a2c690.jpg)

`http://localhost:3000/news_preview?preview_token=...`
となっていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71eaa489156347b700299f6032c0e122.png)

## プレビュー用のAPIを作成する
### API基本設定を行う
続いてAPIの登録をします。  
Kurocoの管理画面から[API]->[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5a0c3aacbb47a0e6c9fb95819d14622.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa425815fa52294d9cac473ad30f8128.png)

タイトル、版、ディスクリプションを入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/47504529d5421cba9a97fabfc37529b6.png)

追加したAPIに遷移しますので、続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae15c4586461b9fa56be21f86e4a84f3.png)

[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
注意)  
Cookieをセキュリティ用のトークンとして利用する場合、APIドメインとフロントエンドのドメインが違うとサードパティクッキーの問題があり、Safari等で認証が効きません。  
フロントエンドとAPIドメインをサブドメイン違いで設定をする必要があるので、[独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)でAPIドメインを設定し、[アカウント設定](/ja/docs/management/account/)からAPIドメインを変更ください。  
（Chromeでは正常に動作しますので、開発やテストの段階ではまずChromeで構築していただくことをお勧めします。）

### CORS設定を行う
[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb98a278523926012fce2b3cffded320.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000/`
- フロントエンドドメイン

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6fab130c21608aa66875a721a0c13cd5.png)

問題なければ [保存する] をクリックします。

### エンドポイントを設定する
以下の内容で、プレビュー用のコンテンツデータを取得するエンドポイントを作成します。

:::tip
ワンタイムトークンが発行されるため、APIリクエスト制限はNoneを指定してください。  
topics_group_idには、ご自身のコンテンツ定義のIDを記入してください。
:::

| 設定項目 | 設定 | |
| :--- | :--- | :--- |
| パス | **news/preview** ||
| | 有効/無効 | 有効 |
| モデル | カテゴリー | コンテンツ |
| | モデル | Topics |
| | オペレーション | preview |
| 認証 | **None** ||
| topics_group_id | **10** |  |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1a44cd6d1d2afa1f591251750cc5ef7.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/640f812fb9c69847e35b057ea21ef483.png)

## フロントエンドの追加をする

プレビューを表示するためのページを追加します。 
今回はnews_previewのディレクトリ名でページが表示できるように以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/news_preview/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_preview.vue
```

**Nuxt3:**

```markup reference title="/pages/news_preview/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_preview.vue
```

**Next.js:**

```jsx reference title="/app/news_preview/page.jsx"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nextjs/news_preview.jsx
```


:::caution
`/rcms-api/6/news/preview`の部分はご自身のエンドポイントのURLに変更してください。  
:::

最後に動作の確認をします。  
[プレビューを確認する]ボタンをクリックすることで、
保存前の編集中コンテンツを取得できるようになりました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/63c49a4bff9cb5df720a2b96179796b9.gif)

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [サブサイトをプレビューサイトにする](/ja/docs/tutorials/make-the-subsite-a-preview-site/)
- [Kurocofrontでプレビュー用のページを出力できますか？](/ja/docs/faq/can-i-output-a-preview-page-with-kurocofront/)
- [プレビュートークンの有効期限を変更できますか](/ja/docs/faq/can-i-change-the-expiration-date-of-the-preview-token/)


---

# コーポレートサンプルサイトを利用する

> 元ページ: `tutorials/kuroco-corporate-sample-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kuroco-corporate-sample-site/
> 概要: コーポレートサンプルサイトを利用する

Kuroco構築時のテンプレートとして利用できる**コーポレートサンプルサイトを公開**しました。

コーポレートサンプルサイトには、一般的なコーポレートサイトで使われる内容のコンテンツ表示に加えて、ログイン機能もテンプレートに含まれています。    
  
Kurocoでプロジェクトをはじめる際のテンプレートとしてご利用ください。

## デモサイト

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e28bb1f6d8f2930b54205016f8739cd4.jpg)

デモサイトURL：https://dev-nuxt-corporate.g.kuroco-front.app/  
リポジトリ：https://github.com/diverta/front_nuxt_corporate

### 機能一覧

- コンテンツ管理
  - 記事一覧
  - 記事詳細
  - プレビュー
  - マスタの表示(アーカイブに利用)
  - フィルタ(日付)
- 問い合わせフォーム
  - 回答項目の動的表示
  - フォーム送信
- 会員機能
  - 登録・退会
  - ログイン・ログアウト
  - 会員情報の更新
  - パスワードリマインダー
  - 会員クラスによるコンテンツの出し分け
  - 非ログインユーザーにも会員限定コンテンツの一部を表示
  - 会員クラス変更の依頼を自動処理  
    ※デモ用に追加されています。<br/>　設定を外して、手動処理 or Stripeと連携した有料会員機能としてご利用いただけます。

### コンセプト
本サンプルサイトは以下のコンセプトで作られています。
- 機能紹介を目的とした制作事例のショーケースではなく、あくまでユーザーが編集して使うための"テンプレート"サイト
- ユーザーで編集できることが必須のため、利便性よりも読みやすいコードを優先する
- プラグイン等はできる限り入れず、欲しいプラグインはユーザー側で追加する
- CSSフレームワークはユーザーが使い慣れたものを適用できるように、テンプレート側では使わない

## 前提条件

プロジェクト開始前に、準備事項を記載します。

:::info
本プロジェクトはNuxt3を利用しています。ご自身の環境でNuxtが利用できるようにあらかじめご対応をお願いいたします。  
参考: [NuxtJS インストール 前提条件](https://nuxt.com/docs/getting-started/installation#prerequisites)
:::

:::info
プロジェクトをデプロイするためGitHubにソースをpushします。あらかじめGitHubのアカウント作成をお願いします。  
参考: [GitHub Docs クイックスタート](https://docs.github.com/ja/github/getting-started-with-github/quickstart)
:::

## バックエンドの準備をする
### Kurocoの登録
まずはKurocoのアカウント登録します。[無料トライアル](https://kuroco.app/ja/free_trial/)より必要項目を記入し、「登録する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a80b767e116713164250606ff2b4ca58.png)

:::caution
コーポレートサンプルサイトはサブサイトで運用します。  
メインサイトとサブサイトで別々のサイトキーになるのでそれぞれ準備してください。

無料トライアルから登録するサイトキーはメインサイトのものになります。
:::

登録したメールアドレスに登録完了のメールが届きます。メール内に記載されている管理画面URLをクリックし、ログインを行うと下記画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a370334b8d179ad7d55cf6b62756802.png)

### サブサイトの追加
サイト一覧からコーポレートサンプルサイト用のサブサイトを追加します。  

:::info
メインサイトのデフォルトは会員制サンプルサイト用の設定になっています。メインサイトのフロントエンドは未使用で構いません。  
お支払い用のクレジットカードはメインサイトで登録し、サブサイトの利用料を含めた費用がメインサイトに請求されます。  
:::

[環境設定] -> [サイト一覧]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e62d36fc06738d5bd8bde2772e0d807.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2275c30e4535ce3d720c21ccd054af4.png)

コピー元のサイト名を`[Template]Nuxt Corporete(Default)`に設定し、必須項目を入力して[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/10bd183ae1f78d734eb48b1e94da4f85.png)

サブサイトの登録完了のメールが届いたらログインをしてコンテンツを確認します。  

:::note
以降、Kuroco管理画面の説明はすべてサブサイトのものになります。
:::

### CORSの設定
API画面より、CORSを設定します。
[API] -> [Default]をクリックし、「CORSを設定する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4de3b09b0972d5ed0b7ebef45817c7f8.png)

CORS_ALLOW_ORIGINSの「Add Origin」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/88f828d364b4bca60cfae2883f65a08d.png)

フィールドが追加されるので、`http://localhost:3000`を追加し「保存する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/468ab5e5c4cc677ed1eefa81595e3f8d.png)

以上でCORSの設定完了です。

## フロントエンドの準備をする
### コーポレートサンプルサイトのリポジトリをcloneする

[GitHubのリポジトリ](https://github.com/diverta/front_nuxt_corporate)よりソースコードをご自身のローカルディレクトリにcloneします。ターミナルで下記実行します。

```
git clone https://github.com/diverta/front_nuxt_corporate.git
```

clone後、front_nuxt_corporateディレクトリに移動し、プロジェクトのインストールをします。

```
cd front_nuxt_corporate
npm install
```


続いて、nuxt.config.tsを開き、のruntimeconfigのkurocoApiDomainを自身のサイトのAPIドメインに変更します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d457b5b9b69e9820cf280f6334baad3.png)

:::tip
APIドメインはアカウント設定もしくは、エンドポイント一覧のページで確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9735780170101683329a3ce6195c4eff.png)
:::

準備ができたら以下をコマンドラインで実行し、ローカルでの表示を確認します。  

```
npm run dev
```

`http://localhost:3000` にアクセスするとサイトが表示されます。


### GitHubにリポジトリを作成しファイルをpushする

次に、先ほどcloneしたリポジトリをご自身のリポジトリにpushします。  
GitHubにログインし、[Repositories] -> [New]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/77864b81ba1d3d0f46cd49aa456b83dd.png)

リポジトリ作成画面が表示されるので、必要事項を記入し「Create repository」をクリックします。  
（今回は「Repository name」に「kuroco_front_nuxt_corporate」と記入しました。）

![Image from Gyazo](https://t.gyazo.com/teams/diverta/35f920071b0308c091e5368e16637ebf.png)

以上でリポジトリが完成しました。

それでは、先ほどcloneしたファイルをこちらのリポジトリにpushします。
現在はclone元の `https://github.com/diverta/front_nuxt_corporate.git`に紐づいているので、こちらを先ほど作成したリポジトリに変更します。

コマンドラインより下記実行します。

```
git remote set-url origin https://github.com/GitHubアカウント/kuroco_front_nuxt_corporate.git
```

注：
下記２点はご自身のアカウントに合わせて変更してください。  
- GitHubアカウント：ご自身のGitHubアカウント名  
- kuroco_front_nuxt_corporate：先ほど作成したリポジトリ名  

これでリモートリポジトリが変更されました。念の為コマンドラインで下記実行します。

```
git remote -v
```

すると、設定したリポジトリに変更されていることが確認できます。

```
origin  https://github.com/GitHubアカウント/kuroco_front_nuxt_corporate.git (fetch)
origin  https://github.com/GitHubアカウント/kuroco_front_nuxt_corporate.git (push)
```

それではファイルを作成したGitHubリポジトリにpushします。
下記実行してください。

```
git push -u origin main
```

GitHubのリポジトリを確認すると、ファイルがpushされていることが確認できます。

:::tip
注: pushでエラーになる場合の対応方法  
今回のサンプルサイトでは、ファイルにGitHubActions用のymlファイルが含まれます。  
そのため、GitHubの設定によってはエラー表示される可能性がございます。エラーが表示された場合は、[FAQ -> GitHubリポジトリにpushした際、エラーが表示されます。エラー解決方法を教えてください。](/ja/docs/faq/i-get-an-error-message-when-i-push-to-the-github-repository/)を参考に対応をお願いします。  
:::

以上でフロントエンドの準備は完了です。次に、ご自分のKurocoと接続する方法を説明します。

## KurocoとGitHubを連携してデプロイする
### KurocoFrontの設定
KurocoFrontを利用し、Kurocoと先程cloneしたGitHubリポジトリを連携します。

[外部システム連携] -> [GitHub] をクリックし、KurocoFrontを表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7553b3e477fd07848ee5a61724007648.png)
「GitHubリポジトリと接続する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e41debef535542ae805cda392baec9a7.png)
GitHubへログインが求められますので、ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/214c1957e75be4de2ea7bc01d10499ab.png)
ログインするとGitHubの画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d42942104b7b668e7d80c44696db4429.png)
「Repository access」より接続するリポジトリを選択します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/afef17946cbde0c9d11433dcb08564a4.png)
:::tip
リポジトリ接続設定は後から変更が可能です。１つのアカウントで複数のKurocoを利用する場合は、KurocoのGitHub Appsは1つですので、ここで複数のリポジトリを選択することになります。
:::

:::tip 
接続できるリポジトリは管理者権限を持っているリポジトリのみになりますので、ご注意ください。
:::

リポジトリを選択したら、「Save」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2495975946bf105a99c9ebccf9e267b.png)

再度Kurocoへのログインを求められますので、ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4d89886433dac6ad24ebcc40cdc7ce90.png)

接続が完了すると、KurocoFrontの画面に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/20469ed06d8b1171c8ec9e6a69a491d5.png)

「リポジトリ」でcloneしたリポジトリを選択し、「更新する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9809e851b07526aa3a82cff0bd8c7bdf.png)

「GitHubの連携対象」で下記選択し、「更新する」をクリックします。
- ワークフロー：Build and deploy
- 対象ブランチ：main

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4f83cba449c17a35d055bfb1b3df594e.png)

以上でKurocoFrontの設定が完了です。

### build.ymlファイル修正
/.github/workflow/build.yml ファイルを修正します。  
[外部システム連携] -> [GitHub]にアクセスし、Frameworkをnuxt3に設定して、「リポジトリ」のテキストエリア内をコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/044a64e252e181fc475a4d4d5aecba1b.png)

/.github/workflow/build.yml を開き、コピーした内容で上書きします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d44909461561c2260e90696208ae5ad.png)

ファイルの更新ができたら、変更をGitHubにプッシュします。GitHubActionが実行され、ビルド&デプロイが正常終了したら完了です。  

### 表示の確認 
Kuroco管理画面より、「サイトを表示」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/72216a3afc86e1b59c4548b4a1bba828.png)

すると、front_nuxt_corporate をクローンしたサイトが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e28bb1f6d8f2930b54205016f8739cd4.jpg)

## ご質問や不具合連絡について

以上でコーポレートサンプルサイトの使用準備は完了です。  

ご不明点やご質問ありましたら[お問い合わせ](https://kuroco.zendesk.com/)よりご連絡ください。  
また、コードの不具合等ありましたら[リポジトリ](https://github.com/diverta/front_nuxt_corporate)よりissueまたはPRをお願いします。

## 関連ドキュメント
- [コーポレートサンプルサイトをSSGにする](/ja/docs/tutorials/corporate-sample-site-to-ssg/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [会員制サンプルサイトを利用する](/ja/docs/tutorials/kuroco-sample-site/)
- [メディアサンプルサイトを利用する](/ja/docs/tutorials/kuroco-media-sample-site/)
- [サイト一覧](/ja/docs/management/site-list/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)


---

# メディアサンプルサイトを利用する

> 元ページ: `tutorials/kuroco-media-sample-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kuroco-media-sample-site/
> 概要: メディアサンプルサイトを利用する

Kuroco構築時のテンプレートとして利用できる**メディアサンプルサイトを公開**しました。

メディアサンプルサイトには、一般的なメディアサイトで使われる内容のコンテンツ表示に加えて、ログイン機能もテンプレートに含まれています。    
  
Kurocoでプロジェクトをはじめる際のテンプレートとしてご利用ください。

## デモサイト

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2cd369a6adce3d7c8c0b311a20c75fea.jpg)

デモサイトURL：https://dev-next-media.g.kuroco-front.app/  
リポジトリ：https://github.com/diverta/front_next_media

### 機能一覧

- コンテンツ管理
  - 記事一覧
  - 記事詳細
  - ランキング表示
  - 特集記事
  <!--- プレビュー-->
  - カテゴリ検索
  - タグ検索
  - キーワード検索
- 問い合わせフォーム
  - 回答項目の動的表示
  - フォーム送信
- 会員機能
  - 登録・退会
  - ログイン・ログアウト
  - 会員情報の更新
  - パスワードリマインダー
  - 会員限定記事
  - お気に入り

### コンセプト
本サンプルサイトは以下のコンセプトで作られています。
- Next.jsのAppルーターを使用した実装例として提示する
- ユーザーが編集して使うためのテンプレートサイトであるが、ある程度フロントエンドフレームワークの利用に慣れたユーザーを対象とする
- プラグイン等はできる限り入れず、欲しいプラグインはユーザー側で追加する
- CSSフレームワークはユーザーが使い慣れたものを適用できるように、テンプレート側では使わない

## 前提条件

プロジェクト開始前に、準備事項を記載します。

:::info
本プロジェクトはNext.jsを利用しています。ご自身の環境でNextが利用できるようにあらかじめご対応をお願いいたします。  
参考: [Next.js インストール](https://nextjs.org/docs/getting-started/installation)
:::

:::info
プロジェクトをデプロイするためGitHubにソースをpushします。あらかじめGitHubのアカウント作成をお願いします。  
参考: [GitHub Docs クイックスタート](https://docs.github.com/ja/github/getting-started-with-github/quickstart)
:::

## バックエンドの準備をする
### Kurocoの登録
まずはKurocoのアカウント登録します。[無料トライアル](https://kuroco.app/ja/free_trial/)より必要項目を記入し、「登録する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a80b767e116713164250606ff2b4ca58.png)

:::caution
メディアサンプルサイトはサブサイトで運用します。  
メインサイトとサブサイトで別々のサイトキーになるのでそれぞれ準備してください。

無料トライアルから登録するサイトキーはメインサイトのものになります。
:::

登録したメールアドレスに登録完了のメールが届きます。メール内に記載されている管理画面URLをクリックし、ログインを行うと下記画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a370334b8d179ad7d55cf6b62756802.png)

### サブサイトの追加
サイト一覧からメディアサンプルサイト用のサブサイトを追加します。  

:::info
メインサイトのデフォルトは会員制サンプルサイト用の設定になっています。メインサイトのフロントエンドは未使用で構いません。  
お支払い用のクレジットカードはメインサイトで登録し、サブサイトの利用料を含めた費用がメインサイトに請求されます。  
:::

[環境設定] -> [サイト一覧]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e62d36fc06738d5bd8bde2772e0d807.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2275c30e4535ce3d720c21ccd054af4.png)

コピー元のサイト名を`[Template]Next Media(Default)`に設定し、必須項目を入力して[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e45ad95c7c3b91bd0484fb4a57986cdd.png)

サブサイトの登録完了のメールが届いたらログインをしてコンテンツを確認します。  

:::note
以降、Kuroco管理画面の説明はすべてサブサイトのものになります。
:::

### CORSの設定
API画面より、CORSを設定します。
[API] -> [Default]をクリックし、「CORSを設定する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4de3b09b0972d5ed0b7ebef45817c7f8.png)

CORS_ALLOW_ORIGINSの「Add Origin」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/88f828d364b4bca60cfae2883f65a08d.png)

フィールドが追加されるので、`http://localhost:3000`を追加し「保存する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/468ab5e5c4cc677ed1eefa81595e3f8d.png)

以上でCORSの設定完了です。

## フロントエンドの準備をする
### メディアサンプルサイトのリポジトリをcloneする

[GitHubのリポジトリ](https://github.com/diverta/front_next_media)よりソースコードをご自身のローカルディレクトリにcloneします。ターミナルで下記実行します。

```
git clone https://github.com/diverta/front_next_media.git
```

clone後、front_next_mediaディレクトリに移動し、プロジェクトのインストールをします。

```
cd front_next_media
npm install
```


続いて、.envファイルを開き、NEXT_PUBLIC_BASE_URLを自身のサイトのAPIドメインに変更します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4f11c948de7bc7c98711c2cd076a0a33.jpg)

:::tip
APIドメインはアカウント設定もしくは、エンドポイント一覧のページで確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1ef33e4c5272798ad24dea7fbe6c4acf.png)
:::

準備ができたら以下をコマンドラインで実行し、ローカルでの表示を確認します。  

```
npm run dev
```

`http://localhost:3000` にアクセスするとサイトが表示されます。


### GitHubにリポジトリを作成しファイルをpushする

次に、先ほどcloneしたリポジトリをご自身のリポジトリにpushします。  
GitHubにログインし、[Repositories] -> [New]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/77864b81ba1d3d0f46cd49aa456b83dd.png)

リポジトリ作成画面が表示されるので、必要事項を記入し「Create repository」をクリックします。  
（今回は「Repository name」に「kuroco_front_next_media」と記入しました。）

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e22bbd381e9fe1b2fc33a7b7e5dce509.png)

以上でリポジトリが完成しました。

それでは、先ほどcloneしたファイルをこちらのリポジトリにpushします。
現在はclone元の `https://github.com/diverta/front_next_media.git`に紐づいているので、こちらを先ほど作成したリポジトリに変更します。

コマンドラインより下記実行します。

```
git remote set-url origin https://github.com/GitHubアカウント/kuroco_front_next_media.git
```

注：
下記２点はご自身のアカウントに合わせて変更してください。  
- GitHubアカウント：ご自身のGitHubアカウント名  
- kuroco_front_next_media：先ほど作成したリポジトリ名  

これでリモートリポジトリが変更されました。念の為コマンドラインで下記実行します。

```
git remote -v
```

すると、設定したリポジトリに変更されていることが確認できます。

```
origin  https://github.com/GitHubアカウント/kuroco_front_next_media.git (fetch)
origin  https://github.com/GitHubアカウント/kuroco_front_next_media.git (push)
```

それではファイルを作成したGitHubリポジトリにpushします。
下記実行してください。

```
git push -u origin main
```

GitHubのリポジトリを確認すると、ファイルがpushされていることが確認できます。

:::tip
注: pushでエラーになる場合の対応方法  
今回のサンプルサイトでは、ファイルにGitHubActions用のymlファイルが含まれます。  
そのため、GitHubの設定によってはエラー表示される可能性がございます。エラーが表示された場合は、[FAQ -> GitHubリポジトリにpushした際、エラーが表示されます。エラー解決方法を教えてください。](/ja/docs/faq/i-get-an-error-message-when-i-push-to-the-github-repository/)を参考に対応をお願いします。  
:::

以上でフロントエンドの準備は完了です。次に、ご自分のKurocoと接続する方法を説明します。

## KurocoとGitHubを連携してデプロイする
### KurocoFrontの設定
KurocoFrontを利用し、Kurocoと先程cloneしたGitHubリポジトリを連携します。

[外部システム連携] -> [GitHub] をクリックし、KurocoFrontを表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7553b3e477fd07848ee5a61724007648.png)
「GitHubリポジトリと接続する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e41debef535542ae805cda392baec9a7.png)
GitHubへログインが求められますので、ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/214c1957e75be4de2ea7bc01d10499ab.png)
ログインするとGitHubの画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d42942104b7b668e7d80c44696db4429.png)
「Repository access」より接続するリポジトリを選択します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/afef17946cbde0c9d11433dcb08564a4.png)
:::tip
リポジトリ接続設定は後から変更が可能です。１つのアカウントで複数のKurocoを利用する場合は、KurocoのGitHub Appsは1つですので、ここで複数のリポジトリを選択することになります。
:::

:::tip 
接続できるリポジトリは管理者権限を持っているリポジトリのみになりますので、ご注意ください。
:::

リポジトリを選択したら、「Save」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2495975946bf105a99c9ebccf9e267b.png)

再度Kurocoへのログインを求められますので、ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4d89886433dac6ad24ebcc40cdc7ce90.png)

接続が完了すると、KurocoFrontの画面に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/20469ed06d8b1171c8ec9e6a69a491d5.png)

「リポジトリ」でcloneしたリポジトリを選択し、「更新する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1ade800fb58a8d2ff5764fcce4ab7f4f.png)

「GitHubの連携対象」で下記選択し、「更新する」をクリックします。
- ワークフロー：Build and deploy
- 対象ブランチ：main

![Image from Gyazo](https://t.gyazo.com/teams/diverta/58540e6b239f1e7a6eaeda5c523acd3f.png)

以上でKurocoFrontの設定が完了です。

### build.ymlファイル修正
/.github/workflow/build.yml ファイルを修正します。  
[外部システム連携] -> [GitHub]にアクセスし、Frameworkをnextに設定して、「リポジトリ」のテキストエリア内をコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e613775632e46a9a6436e12b78be302.png)

/.github/workflow/build.yml を開き、コピーした内容で上書きします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3827d2d89b67ff31acf01ef200037c62.png)

ファイルの更新ができたら、変更をGitHubにプッシュします。GitHubActionが実行され、ビルド&デプロイが正常終了したら完了です。  

### 表示の確認 
Kuroco管理画面より、「サイトを表示」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/72216a3afc86e1b59c4548b4a1bba828.png)

すると、front_next_media をクローンしたサイトが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2cd369a6adce3d7c8c0b311a20c75fea.jpg)

## コンテンツを追加する
メディアサンプルサイトでは、サイトトップの記事一覧と、記事詳細がSSGの構成で作られています。  
これは、デプロイ時にAPIリクエストを送り、最新の記事を取得している事を意味します。

ユーザーのアクセス時には事前に取得したコンテンツを表示できるため、APIリクエスト数の低減とパフォーマンスの向上が可能ですが、Kuroco側でコンテンツの追加・更新をしても、再デプロイを実施しないと追加したコンテンツは表示されません。  

Kurocoではコンテンツの追加・更新に連動してGitHub Actionsを実行し、デプロイを実施する機能をもっていますので、こちらを有効にしてコンテンツを追加します。  

コンテンツ一覧から[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/800c75b5da4b48f124435f609661c424.png)

任意のコンテンツを入力したら[Github Actions ワークフロー]を有効にしてコンテンツを追加します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff4991ee751737910a5a35fce4b37a6e.png)

:::tip
コンテンツ毎に設定が記憶されますので、2回目以降はデフォルトで有効にチェックが入った状態になります。
::: 

コンテンツの追加と同時にGitHub Actionsが実行されることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c2149a1953d1e274ee53cc38cc8e49e4.png)

デプロイが完了するとフロントエンドにも表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/08670f76d7f222a3822e800558a9e06e.png)

フロントエンドを構築する際にはコンテンツが頻繁に変わらない、かつSEOが重要なページはSSG、リアルタイムでのデータ更新が必要なページやユーザーによって表示されるコンテンツが異なるページはCSRにするなど、プロジェクトの要件に応じてSSGとCSRを適切に併用してください。

## ご質問や不具合連絡について

以上でメディアサンプルサイトの使用準備は完了です。  

ご不明点やご質問ありましたら[お問い合わせ](https://kuroco.zendesk.com/)よりご連絡ください。  
また、コードの不具合等ありましたら[リポジトリ](https://github.com/diverta/front_next_media)よりissueまたはPRをお願いします。

## 関連ドキュメント
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [コーポレートサンプルサイトを利用する](/ja/docs/tutorials/kuroco-corporate-sample-site/)
- [会員制サンプルサイトを利用する](/ja/docs/tutorials/kuroco-sample-site/)
- [サイト一覧](/ja/docs/management/site-list/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
