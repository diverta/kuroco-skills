# Kurocoドキュメント: チュートリアル / 認証・会員（1/4）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 同じグループのメンバーが作成したコンテンツのみ表示・編集を可能にする（`allow-only-the-display-and-editing-of-content-created-by-same-group-members`）
- 会員制サンプルサイトをコピーして、Kurocoで会員制サイトを構築する方法（`building-a-membership-website-on-kuroco-from-the-sample-site-template`）
- メンバー登録時にドメインによって所属グループを変更する（`change-the-default-group-for-member-registration-depending-on-the-domain`）
- メンバーを追加する（`how-to-add-new-member`）
- フォーム送信によりメンバー登録されるユーザーのメンバー情報にフォームの回答内容を設定する（`how-to-implement-original-function-into-the-member-info-when-form-send-with-member-regist`）
- メンバーを招待する（`how-to-invite-new-member`）
- 社内ネットワークからアクセスした場合のみスーパーユーザーとなるグループを作成する（`how-to-make-new-group`）
- 配信の購読者を登録する（`how-to-register-subscribers-on-magazine`）
- パスワードリマインダー/パスワードリセットを設定する（`how-to-use-password-reminder`）
- 代理ログイン機能の使い方（`how-to-use-proxy-login`）
- Microsoftを利用してOAuth認証によるSSOを実装する（`implement-login-with-microsoft`）
- 一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する（`implement-reminder-and-automatic-deletion-of-members`）
- GitHubを利用してOAuth認証によるSSOを実装する（`implementing-oauth-sp-based-sso`）
- SSOによるログインをフロントエンドで利用する（`implementing-oauth-sp-based-sso-front`）


---

# 同じグループのメンバーが作成したコンテンツのみ表示・編集を可能にする

> 元ページ: `tutorials/allow-only-the-display-and-editing-of-content-created-by-same-group-members` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/allow-only-the-display-and-editing-of-content-created-by-same-group-members/
> 概要: コンテンツ定義の編集権限設定で閲覧・編集可能なグループを制限することができますが、「自分と同じグループ」のような動的な設定の場合はトリガーを使ったカスタム処理で実装します。本チュートリアルではコンテンツの表示（管理画面）のトリガーを使用して、同じグループのメンバーが作成したコンテンツのみ表示・編集が可能となる制限をコンテンツ定義に設定します。

## 概要
コンテンツ定義の編集権限設定で閲覧・編集可能なグループを制限することができますが、
「自分と同じグループ」のような動的な設定の場合はトリガーを使ったカスタム処理で実装します。

本チュートリアルでは[コンテンツの表示（管理画面）](/ja/docs/reference/trigger-variables/#コンテンツの表示管理画面)のトリガーを使用して、同じグループのメンバーが作成したコンテンツのみ表示・編集が可能となる制限をコンテンツ定義に設定します。

### 学べること
以下の手順で、同じグループのメンバーが作成したコンテンツのみ表示・編集が可能となる制限を設定します。

- [カスタム処理を設定する](#カスタム処理を設定する)
- [動作を確認する](#動作を確認する)


## カスタム処理を設定する

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

以下のカスタム処理を設定します。 

|項目|値|
|:--|:--|
|タイトル|fiter_members_of_the_same_group|
|識別子|fiter_members_of_the_same_group|
|トリガ|コンテンツの表示（管理画面）/対象のコンテンツ定義IDを指定|
|処理|以下の内容|

```smarty reference title="fiter_members_of_the_same_group"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/trigger/fiter_members_of_the_same_group.txt
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cbe022b063b6d0adf919036ac49f245.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

## 動作を確認する
動作の確認をするため、検証用のメンバーとグループを以下のように準備します。  

|メンバー|グループ|
|:--|:--|
|Diverta Hanako|Tester|
|Diverta Jiro|Editor|
|Diverta Taro|Editor|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bd54ba4deeb968800cc1cd7fe3fe915.png)

次に、それぞれのメンバーでログインをして、コンテンツを1つずつ作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aafb0bb9871b3897a0f5c38c257f911b.png)

:::info
コンテンツの表示（管理画面）のトリガーは「スーパーユーザー」以外でログインしている場合に実行されるため、スーパーユーザーからは全てのコンテンツが確認できます。
:::

最後にそれぞれのメンバーでログインをして、一覧に表示されるコンテンツを確認します。  
同じグループのメンバーが作成したコンテンツだけが表示されることが分かります。

**Diverta Hanakoでログイン**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/332a4a07a44b5b179f856a4f369cc8eb.png)

**Diverta Jiroでログイン**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7db9012cda539deae44393ea47997b37.png)

**Diverta Taroでログイン**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/13ae4b2fc1795f1afe53653064ee30d2.png)

:::caution
上記のサンプルコードの場合、
- Aさんは、`幹部` グループと `社内釣り愛好会` グループに所属
- Bさんは、`平社員` グループと `社内釣り愛好会 `グループに所属
- Aさんが`トップシークレット文書` を作成する

とすると、Bさんは `トップシークレット文書` を編集可能になります。

１人のメンバーは1グループのみに所属する運用にする。カスタム処理内に例外の処理を追加する。などプロジェクトに合わせて調整してください。
:::

:::tip
さらに、[コンテンツのバリデーション前](/ja/docs/reference/trigger-variables/#コンテンツのバリデーション前)のトリガーを追加することで、同じグループのメンバーが作成したコンテンツだけ表示されるが、編集はできないといった実装も可能です。
:::

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# 会員制サンプルサイトをコピーして、Kurocoで会員制サイトを構築する方法

> 元ページ: `tutorials/building-a-membership-website-on-kuroco-from-the-sample-site-template` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/building-a-membership-website-on-kuroco-from-the-sample-site-template/
> 概要: Kuroco構築時のテンプレートとして利用できる会員制サンプルサイトをオープンソース化しました。本プロジェクトをコピーすることで、簡易的な会員制サイトを構築することができます。Kurocoでプロジェクトをはじめる際のテンプレートとしてご利用ください。

Kuroco構築時のテンプレートとして利用できる**会員制サンプルサイトをオープンソース化**しました。

本プロジェクトをコピーすることで、簡易的な会員制サイトを構築できます。Kurocoでプロジェクトをはじめる際のテンプレートとしてご利用ください。

リポジトリ：https://github.com/diverta/front_nuxt_auth

## デモサイト
今回構築するサイトのデモサイトは、下記より動作確認できます。

https://dev-nuxt-auth.g.kuroco-front.app/

## 前提条件

プロジェクト開始前に、準備事項を記載します。

### Nuxtを利用します

本プロジェクトはNuxtを利用しています。ご自身の環境でNuxtが利用できるようにあらかじめご対応をお願いいたします。

:::info
参考: [NuxtJS Prerequisites](https://nuxt.com/docs/getting-started/installation#prerequisites)
:::

### GitHubを利用します

プロジェクトをデプロイするためGitHubにソースをpushします。あらかじめGitHubのアカウント作成をお願いします。

:::info
参考: [GitHub Docs クイックスタート](https://docs.github.com/ja/github/getting-started-with-github/quickstart)
:::

## サイトを構築する
それではサイトの構築をはじめます。

### 会員制サイトサンプルリポジトリをcloneする

[GitHubのリポジトリ](https://github.com/diverta/front_nuxt_auth)よりソースコードをご自身のローカルディレクトリにcloneします。ターミナルで下記実行します。

```
git clone https://github.com/diverta/front_nuxt_auth.git
```

clone後、front_nuxt_authディレクトリに移動し、プロジェクトのインストール・実行します。

```
cd front_nuxt_auth
npm install
npm run dev
```

`http://localhost:3000` にアクセスするとログイン画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4ccca26427689829fbadc4351618e348.png)
### GitHubにリポジトリを作成しファイルをpushする

次に、先ほどcloneしたリポジトリをご自身のリポジトリにpushします。  
GitHubにログインし、[Repositories] -> [New]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/77864b81ba1d3d0f46cd49aa456b83dd.png)
リポジトリ作成画面が表示されるので、必要事項を記入し「Create repository」をクリックします。  
（今回は「Repository name」に「kuroco_front_nuxt_auth」と記入しました。）

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4cfa87a561bbcd23aac699ac6a462969.png)
以上でリポジトリが完成しました。

それでは、先ほどcloneしたファイルをこちらのリポジトリにpushします。
現在はclone元の `https://github.com/diverta/front_nuxt_auth.git`に紐づいているので、こちらを先ほど作成したリポジトリに変更します。

コマンドラインより下記実行します。

```
git remote set-url origin https://github.com/GitHubアカウント/kuroco_front_nuxt_auth.git
```
注：
下記２点はご自身のアカウントに合わせて変更してください。  
- GitHubアカウント：ご自身のGitHubアカウント名  
- kuroco_front_nuxt_auth：先ほど作成したリポジトリ名  

これでリモートリポジトリが変更されました。念の為コマンドラインで下記実行します。

```
git remote -v
```

すると、設定したリポジトリに変更されていることが確認できます。

```
origin  https://github.com/GitHubアカウント/kuroco_front_nuxt_auth.git (fetch)
origin  https://github.com/GitHubアカウント/kuroco_front_nuxt_auth.git (push)
```

それではファイルを作成したGitHubリポジトリにpushします。
下記実行してください。

```
git push -u origin main
```

GitHubのリポジトリを確認すると、ファイルがpushされていることが確認できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0b35802a4969603bbb8f8277e83db8c7.png)
以上でフロントエンドの準備は完了です。次に、ご自分のKurocoと接続する方法を記載します。

:::tip
注: pushでエラーになる場合の対応方法  
今回のサンプルサイトでは、ファイルにGitHubActions用のymlファイルが含まれます。  
そのため、GitHubの設定によってはエラー表示される可能性がございます。エラーが表示された場合は、[FAQ -> GitHubリポジトリにpushした際、エラーが表示されます。エラー解決方法を教えてください。](/ja/docs/faq/i-get-an-error-message-when-i-push-to-the-github-repository/)を参考に対応をお願いします。  
:::

### Kurocoの登録
次にKurocoのアカウント登録します。[Free Trial](https://kuroco.app/ja/free_trial/)より必要項目を記入し、「送信する」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f0b35156d68f35e64d1f9f6d3679806e.jpg)
登録したメールアドレスに登録完了のメールが届きます。メール内に記載されている管理画面URLをクリックし、ログインを行うと下記画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a370334b8d179ad7d55cf6b62756802.png)
### CORSの設定
API画面より、CORSを設定します。
[API] -> [Default]をクリックし、「CORSを設定する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4de3b09b0972d5ed0b7ebef45817c7f8.png)

CORS_ALLOW_ORIGINSの「Add Origin」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/88f828d364b4bca60cfae2883f65a08d.png)
フィールドが追加されるので、下記２つを追加し「保存する」をクリックします。

- `フロントエンドドメイン`
- `http://localhost:3000` 

:::tip 
`フロントエンドドメイン`は、[環境設定] -> [アカウント設定]より確認できます。  
（参考: [管理画面マニュアル アカウント設定](/ja/docs/management/account/)）  
独自ドメインを利用しない場合、フロントエンドドメインは`https://サイトキー.g.kuroco-front.app`となります。
`https://サイトキー.g.kuroco-front.app`はすでにCORS_ALLOW_ORIGINSに登録されているので、追加で登録する必要はありません。
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d71252ed9b91d272f7ddbef131d07fa1.png)
以上でCORSの設定完了です。

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

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1baf2798ac40f953e489b09040a5d1ce.png)
再度Kurocoへのログインを求められますので、ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4d89886433dac6ad24ebcc40cdc7ce90.png)
接続が完了すると、KurocoFrontの画面に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f036a90da0c9c28942e775330b12ae91.png)
「リポジトリ」でcloneしたリポジトリを選択し、「更新する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d7824e17e00e7f479b4ada293cde1948.png)
「GitHubの連携対象」で下記選択し、「更新する」をクリックします。
- ワークフロー：Build and deploy
- 対象ブランチ：main

![Image from Gyazo](https://t.gyazo.com/teams/diverta/732762647b502b764dd8a15b90e027f0.png)
以上でKurocoFrontの設定が完了です。

### build.ymlファイル修正
/.github/workflow/build.yml ファイルを修正します。  
[外部システム連携] -> [GitHub]をクリックし、「リポジトリ」のテキストエリア内をコピーします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/53bf0aa8fc530571879dfecda6062eba.png)
/.github/workflow/build.yml を開き、コピーした内容で上書きします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6f5d150f5418e49c22fb2d5264b02a21.png)
ファイルを保存し、GitHubにpushします。すると、GitHub Actionsが実行されます。

GitHubの「Actions」タブをクリックし、ビルドの状況を確認できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c5cf18a799e97703eae9ec35e9aae8bd.png)
ビルドが成功するとデプロイ完了です。

### 画面確認 
Kuroco管理画面より、「サイトを表示」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/72216a3afc86e1b59c4548b4a1bba828.png)
すると、front_nuxt_auth をクローンしたサイトが表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5acd1dcd3cf287b9c0ef00014e0cae80.png)
下記でログインします。
- Your sitekey：あなたのsitekey
- ID：kuroco登録時のメールアドレス
- Password：kuroco登録時のパスワード

全て記入し「Sign In」をクリックすると、ログイン後のトップページが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fc1850f8dac95cafa43d515ede9a06af.png)

:::caution
「アジア(東京)」以外のリージョンをお使いの場合はAPIドメインが異なりますので、該当箇所を探して調整してください。  
例：`.g.kuroco.app` -> `.g3.kuroco.app`
:::

## 利用例

### コンテンツの追加

Kurocoの管理画面より、[コンテンツ] -> [Default]より「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7195e22863cc482c85e4fef568d41387.png)
コンテンツ追加ページより、必要項目を記入し「追加する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a95e389752ba7ef1392bddee3a51887.png)
コンテンツを追加すると、一覧にも追加されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/13f510e3289e705f291e43bdd1a54fb7.png)
## 参考：サイト概要

### 機能一覧

本プロジェクトのサイト概要を記載します。

- ログイン/ログアウト
- 会員登録
- パスワードリマインダー
- 記事一覧表示
- 記事詳細表示
- お気に入り機能
- メンバー一覧表示
- メンバー詳細表示
- 自分のプロフィール編集
- お問い合わせフォーム

### 利用フレームワーク

本プロジェクトで利用している技術・フレームワークです。

- [Nuxt.js](https://nuxt.com/)
- [Vuetify](https://vuetifyjs.com/) 


## ご質問や不具合連絡について

以上で会員制サイトサンプルコピー方法の説明を終わります。  

ご不明点やご質問ありましたら[お問い合わせ](https://kuroco.zendesk.com/)よりご連絡ください。  
また、コードの不具合等ありましたら[リポジトリ](https://github.com/diverta/front_nuxt_auth)よりissueまたはPRをお願いします。

## 関連ドキュメント
- [会員制サンプルサイトを利用する](/ja/docs/tutorials/kuroco-sample-site/)
- [会員制サンプルサイトの解説](/ja/docs/tutorials/explanation-of-kuroco-sample-site/)
- [会員制サンプルサイトで、開発環境と本番環境を分ける方法](/ja/docs/tutorials/separating-development-and-production-environments-for-your-sample-membership-site/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [front_nuxt_authのテンプレートを利用したいのですが、参考ドキュメントはありますか？](/ja/docs/faq/can-i-verify-the-front-nuxt-auth-template/)
- [GitHubリポジトリにpushした際にエラーが表示されます。エラー解決方法を教えてください。](/ja/docs/faq/i-get-an-error-message-when-i-push-to-the-github-repository/)


---

# メンバー登録時にドメインによって所属グループを変更する

> 元ページ: `tutorials/change-the-default-group-for-member-registration-depending-on-the-domain` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/change-the-default-group-for-member-registration-depending-on-the-domain/
> 概要: Member::insert のエンドポイントはセキュリティ上、default_group_id をフロントエンドから変更できません。そこで複数のエンドポイントを作成し、カスタム処理を利用して、ドメインによって利用するエンドポイントを振り分けることで機能を実装します。

## 概要
メンバー登録時にドメインによって所属グループを変更する機能の実装方法を説明します。
Member::insert のエンドポイントはセキュリティ上、`default_group_id`をフロントエンドから変更できません。  
そこで複数のエンドポイントを作成し、カスタム処理を利用して、ドメインによって利用するエンドポイントを振り分けることで機能を実装します。

### 学べること
以下の手順でドメインによって所属グループを変更する機能を実装します。
- [APIの設定](#apiの設定)
- [カスタム処理の作成](#カスタム処理の作成)
- [動作確認](#動作確認)

### 前提条件
このチュートリアルでは、エンドポイント及びカスタム処理の作成とSwagger UI を利用した動作の確認までを行います。  
また、所属させるグループは事前に作成済みとします。

フロントエンドへの実装は[KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)を参考に対応をお願いします。

## APIの設定
### APIの作成
Kuroco内部でのみ利用するエンドポイントはAPIを分けておくことをお勧めします。  
そこで、まずは内部利用のためのAPIを新規で作成します。  
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c341acced8d685e67ec1da1e85abac.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Internal|
|版|1.0|
|ディスクリプション|内部処理用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c04c600fc74102913e9e668ae5cca0e.png)

### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bc5cb1beb28c74ede6aeca89715a647.png)

セキュリティを[動的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62aaa225db5d12ee84ccc6d5a52411fe.png)

セキュリティを[動的アクセストークン]に設定後、`Login::token`のエンドポイントが無い場合、利用をお勧めされますが、内部利用のみの場合は無視して構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb1efe099bdae8f1c0481037416a5d9.png)

### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74cd7a36fd926dbc20b04812553072c7.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2bc3744fe6a2ab042456fa8c635195c.png)

問題なければ [保存する] をクリックします。  

### エンドポイントの作成
次にエンドポイントを作成します。  
今回は`default_group_id`が異なる2つの`Member::insert`エンドポイントと、カスタム処理を呼び出すための`Api::request_api_post`エンドポイントを作成します。  

まずは`Member::insert`エンドポイントです。  
こちらはKuroco内部から呼び出して利用するため、InternalのAPIから[新しいエンドポイントの追加]をクリックして作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

以下の2つを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|member/insert/a|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|insert|
|default_group_id|所属するグループID(101)|
|login_ok_flg|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3042367419a44c8467410b22a22412b4.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68d2e9407d33ebf03ab4bcfb56a4266.png)

|項目|設定内容|
| :--- | :--- |
|パス|member/insert/a|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|insert|
|default_group_id|所属するグループID(102)|
|login_ok_flg|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa4a72af32e2c51dfff1becd15de79b4.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/feba7daca1586426cd5cf4e574963034.png)

次に`Api::request_api_post`エンドポイントです。  
こちらはフロントエンドから利用できるAPIに作成します。今回はDefaultのAPIを利用します。
DefaultのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21831b02823d8ec43ef328ba8c998ad7.png)

|項目|設定内容|
| :--- | :--- |
|パス|member/insert|
|カテゴリー|API|
|モデル|Api|
|オペレーション|request_api_post|
|name|member_insert<br/>(後で設定するカスタム処理の識別子と一致させます。)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/184e8c1517a103ce778e17c69a959175.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ed53bda05a934cb2c2647ef9d8d3274.png)

以上で利用する3つのエンドが作成できました。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8f9f2e59391bbe1e4a1afc3f799d0833.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c5973bd9f5bb0a0e9f6853d293eb5b6.jpg)

## カスタム処理の作成
続いて、ドメインによってリクエストを送るエンドポイントを振り分けるカスタム処理を作成します。  
[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad5047e75ef8f43759d6a9580b6dc871.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|ドメインによって登録先を変える|
|識別子|member_insert <br/>(Api::request_apiエンドポイントのnameと一致させてください。)|
|処理|以下のコードを入力します。|

```smarty
{* POSTされたメールアドレスのドメインで登録先を変える。 *}
{* リクエスト ボディ *}
{assign_array var='body'            values=''}
{assign       var='body'    value=$smarty.post}

{* ドメインが@example.com以外の場合 *}
{if $smarty.post.email|strpos:'@example.com' === false}
    {api_internal
        var='response'
        status_var='status'
        endpoint='/rcms-api/4/member/insert/a'
        method='POST'
        queries=$body
        member_id='1'
    }
{* ドメインが@example.comの場合 *}
{else}
    {api_internal
        var='response'
        status_var='status'
        endpoint='/rcms-api/4/member/insert/b'
        method='POST'
        queries=$body
        member_id='1'
    }
{/if}

{assign var=data value=$response}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a677414e6939a8e807015cd9221fd34.jpg)

設定ができたら[追加する]をクリックしてカスタム処理を追加します。

## 動作確認
最後に動作の確認をします。  
DefaultのAPIの[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c770e6f045b3783f004fe3f4fed8af8.png)

作成したエンドポイントの[Try it out]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/265ef85d681791193973b180d2b26a66.png)

Request bodyに以下を入力して[Execute]をクリックします。  

```json
{
  "email": "example@example.com",
  "name1":"Diverta",
  "name2":"Taro",
  "login_pwd":"********"
}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f14c4d82b8d5bf1f5bc44cde8415fa02.png)

"新規追加しました"のメッセージとメンバーIDの表示を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed8eb913c2ab700a34e391027ff64c60.png)


続いて、Request bodyに以下を入力して[Execute]をクリックします。  

```json
{
  "email": "test@test.com",
  "name1":"Diverta",
  "name2":"Jiro",
  "login_pwd":"********"
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a28874e9dceb3638262e290625cc7b72.png)

"新規追加しました"のメッセージとメンバーIDの表示を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8151b10336eaf5efdc3ee8b567babcc.png)

メンバー一覧ページで登録されたメンバーを確認すると、Diverta Taro と Diverta Jiro で所属するグループが異なることを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd3b555b7e4b741c94241919e0e53f89.png)

以上でメンバー登録時にドメインによって所属グループを変更する機能の実装ができました。

## 関連ドキュメント
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)


---

# メンバーを追加する

> 元ページ: `tutorials/how-to-add-new-member` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-add-new-member/

「メンバー」の機能で、サイトの管理者が新しいメンバーを追加します。

## メンバーを追加する
**1. メンバー一覧画面にアクセスする**  
[メンバー管理] -> [メンバー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f4a541e9b644117906ff37ccb0ad13a9.png)

**2. [追加]をクリックする**  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8609aa28b92c97fb688e508b20eba4ff.png)

**3. メンバー情報を入力する**  
各入力項目の説明は[メンバー編集](/ja/docs/management/member/)を参照ください。  
下記の項目は必ず入力してください。
- [ID情報]タブ：「名前」 
- [ID情報]タブ：「メールアドレス」または「ログインID」
- [ID情報]タブ：「ログインパスワード」  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b68225a1ffae174305cde3d6bc1a888.png)

**4. [追加する]をクリックする**  
「新規追加しました。」のメッセージが表示され、新しいメンバーが追加されます。  
以上で作業は完了です。

## 注意
サイトに何らかのアクセス制限をかけている場合は、ID情報の「所属グループ」の設定に特にご注意ください。  
「所属グループ」は[初期グループ設定](/ja/docs/management/default-group-settings/)で設定したグループがデフォルトで追加されており、[>>編集する]をクリックすると追加・削除が可能です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b5db50e1a9399f91bc3e2d6867e24d50.png)

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [初期グループ設定](/ja/docs/management/default-group-settings/)
- [メンバーアップロード](/ja/docs/management/member-upload/)
- [メンバーを招待する](/ja/docs/tutorials/how-to-invite-new-member/)
- [管理画面からメンバー登録した際にメールでパスワードを通知できますか？](/ja/docs/faq/how-can-i-send-a-registration-email-with-pw-information/)


---

# フォーム送信によりメンバー登録されるユーザーのメンバー情報にフォームの回答内容を設定する

> 元ページ: `tutorials/how-to-implement-original-function-into-the-member-info-when-form-send-with-member-regist` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-original-function-into-the-member-info-when-form-send-with-member-regist/
> 概要: このチュートリアルでは、カスタム処理を利用することで、自動で登録されるユーザーのメンバー情報にフォームの回答データを追加で設定する方法を紹介します。

## 概要  
フォーム基本設定で自動ユーザ登録にチェックを入れると、フォームの回答を送付したメールアドレスを自動でユーザー登録できます。  
このチュートリアルでは、カスタム処理を利用することで、自動で登録されるユーザーのメンバー情報にフォームの回答データを追加で設定する方法を紹介します。

### 学べること
以下の手順で機能の設定をする流れを学びます。

- [カスタム処理で利用するAPIを設定する](#カスタム処理で利用するapiを設定する)
- [カスタム処理を作成する](#カスタム処理を作成する)
- [APIのポストプロセスに作成したカスタム処理を設定](#apiのポストプロセスに作成したカスタム処理を設定)
- [Swaggerを利用して動作確認を行う](#swaggerを利用して動作確認を行う)

### 前提条件
このチュートリアルでは、下記のチュートリアルを参考にフォーム送信と同時にメンバー情報を登録する機能が設定されていることを前提とします。  

- [フォームの回答を送付したユーザー向けに配信メッセージを送付する](/ja/docs/tutorials/sending-notification-messages-to-users-who-submitted-form-responses/)

## カスタム処理で利用するAPIを設定する
次に、カスタム処理で利用する下記のAPIを設定します。

### 内部処理用のAPI設定
Kuroco内部でのみ利用するエンドポイントはAPIを分けておくことをお勧めします。  
そこで、まずは内部利用のためのAPIを新規で作成します。  
既に追加済みの場合は次のステップに進んで構いません。  

#### APIの作成
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c341acced8d685e67ec1da1e85abac.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Internal|
|版|1.0|
|ディスクリプション|内部処理用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c04c600fc74102913e9e668ae5cca0e.png)

#### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bc5cb1beb28c74ede6aeca89715a647.png)

セキュリティを[動的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62aaa225db5d12ee84ccc6d5a52411fe.png)

セキュリティを[動的アクセストークン]に設定後、`Login::token`のエンドポイントが無い場合、利用をお勧めされますが、内部利用のみの場合は無視して構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb1efe099bdae8f1c0481037416a5d9.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74cd7a36fd926dbc20b04812553072c7.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2bc3744fe6a2ab042456fa8c635195c.png)

問題なければ [保存する] をクリックします。  

### 内部処理用のAPIエンドポイントの作成
作成したAPIの設定に実際に利用するAPIのエンドポイントを追加します。
このチュートリアルでは下記の2つのエンドポイントの設定をします。
- フォーム回答情報 詳細取得API
- メンバー更新API

#### フォーム回答情報 詳細取得APIの作成
[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4ecb0650afb6e2abce191a26bb06194.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|inquiry_details|
|カテゴリー|フォーム|
|モデル|InaquiryMessage|
|オペレーション|details|
|GroupAuth|管理者<br/>内部処理用のAPIグループにしているのでフロントから呼ばれることはありませんが、念のためアクセス制限を付けておきます。|
|inquiry_id|「事前準備」で作成したフォームのIDを指定します。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb2130ab2b8efb4d43ca6300a6e8cae8.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

#### メンバー更新APIの作成
[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4ecb0650afb6e2abce191a26bb06194.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|self-member-update|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|update|
|self_only|チェック|

※あくまでも最低限の設定です、実際のサイトに合わせて`allowed_group_ids`、`use_columns`などを設定してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57474f2480e86321ca01949d8c7fbb6f.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

## カスタム処理を作成する
それではカスタム処理を作成します。

### 1. カスタム処理の一覧画面を表示する  
メニューの[オペレーション] -> [カスタム処理] をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a1004b72758bacc6481434dc2645ec6.png)

### 2. カスタム処理の編集画面を表示する 
カスタム処理一覧画面の右上の [追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53e29eae5f0cd2604103b10eff66583d.png)
すると、カスタム処理編集画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/389245a9b05ffacb0c1cb2065b969463.jpg)

### 3. タイトル・識別子を記入する
それではカスタム処理を作成していきます。  
まずはタイトルと識別子に記入します。今回は下記のように記入します。

- タイトル：お問い合わせ時メンバー登録データ連係
- 識別子：member-register-when-inquiry-send

:::tip
タイトル・識別子は他のカスタム処理と重複できません。
実装対象のエンドポイント名など、他と重複しない内容で記入してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e369af2ac8c160ef2cc182f57abb3c8.png)

#### カスタム処理
フォームメッセージの内容を元に登録されたメンバー情報を更新する処理を下記のように記入します。  

```smarty
{assign var=update_member_flg value=1}

{*新規メンバー登録のデータを対象にしたいので未ログインの場合にのみ処理を行う(ログイン済みの場合は既にメンバー登録されている)*}
{if $smarty.session.member_id}
    {assign var=update_member_flg value=0}
{/if}

{*既に登録済みメンバーが存在した場合はプリプロセスに判定処理を追加し以下の部分のコメントアウトを解除して下さい*}
{*}
{assign_session var=exist_member_flg key='exist_member_flg'}
{if $exist_member_flg}
    {assign var=update_member_flg value=0}
{/if}
{*}

{if $update_member_flg}
    {*お問い合わせデータからメンバーID取得*}
    {assign var=inquiry_bn_id value=$json.id}
    {api_internal endpoint='/rcms-api/2/inquiry_details/'|cat:$inquiry_bn_id member_id=1 method='GET' var=inquiry_response status_var=status}
    {if $status==1}
        {assign var=member_id value=$inquiry_response.details.member_id}
        {if $member_id}
            {*問い合わせ情報取得*}
            {assign var=tel value=$inquiry_response.details.ext_01}
            {assign var=address value=$inquiry_response.details.ext_03}
            {assign var=sex value=$inquiry_response.details.ext_04.key}{*選択形式の場合はkeyを連携する*}
            {assign var=birth value=$inquiry_response.details.ext_05}

            {*メンバー情報更新*}
            {assign_array var=queries values=''}
            {assign var=queries.tel value=$tel}
            {assign var=queries.address1 value=$address}
            {assign var=queries.ex_sex value=$sex}
            {assign var=queries.ex_date value=$birth}
            {api_internal endpoint='/rcms-api/2/self-member-update' method='POST' member_id=$member_id queries=$queries var=member_response status_var=status}
            {if $status==1}
                {*処理成功*}
            {else}
                {*エラー処理*}
                {logger msg1='member-register-when-inquiry-send' msg2='Cannot set member ext data' msg3=$queries msg4=$member_response}
            {/if}
        {else}
            {*エラー処理、標準処理でメンバー登録に失敗しているケース*}
            {logger msg1='member-register-when-inquiry-send' msg2='Cannot get member_id from inquiry details' msg3=$inquiry_response}
        {/if}
    {else}
        {*エラー処理*}
        {logger msg1='member-register-when-inquiry-send' msg2='Cannot get inquiry details' msg3=$inquiry_response}
    {/if}
{/if}
{$json|@json_encode}
```

**メンバー項目に設定されるフォーム項目の内容**  
上記のカスタム処理では下記のフォーム設定 / メンバー設定を対応させています。

それぞれの設定は「[フォーム項目設定](/ja/docs/management/form-field-settings/)」、「[メンバーの拡張項目設定](/ja/docs/management/extra-information/)」で実施してください。  

| フォーム項目 | フォームキー名 | メンバー項目 | メンバーキー名 | 型 | 備考 | 
| --- | --- | --- | --- | --- | --- |
| name | name | 姓<br/>名 | name1<br/>name2 | テキスト | 標準のメンバー登録処理で設定されるので連携時には設定しない |
| email | email | メールアドレス | email | テキスト | 標準のメンバー登録処理で設定されるので連携時には設定しない |
| tel | ext_01 | 電話番号 | tel | テキスト | |
| address | ext_03 | 住所1 | address1 | テキスト | |
| sex | ext_04 | 拡張-性別 | ex_sex | 選択項目 | 選択肢はフォーム・メンバー共通で下記を設定<br/>1::male<br/>2::female<br/>3::other |
| birth | ext_05 | 拡張-生年月日 | ex_date | 日付フォーマット | |

#### フォーム項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e0025dd210c95ccef7c8f37b209a5b1.png)

#### メンバー項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b43c6f352ef5fe924f230142b213165.png)


### 4. カスタム処理を保存する 
処理の記述が完了したら、[追加する] ボタンをクリックして保存します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b3b74abddfc8775f8ab73958631a975.png)
### 5. 新規登録時のみフォームデータとメンバー項目の連係を行いたい場合
フォーム送信処理でメンバーを新規登録する処理は、既存メンバーにEmailアドレスが存在しない場合のみ行っています。

その為、もし既に登録済みのメンバーがいる場合にはフォームの内容で連携処理を行いたくない場合は下記の処理をプリプロセスで行い、ポストプロセスに記載している下記のコメント処理を行って下さい。

#### ポストプロセスの該当コメント
```smarty
{*既に登録済みメンバーが存在した場合はプリプロセスに判定処理を追加し以下の部分のコメントアウトを解除して下さい*}
{*}
{assign_session var=exist_member_flg key='exist_member_flg'}
{if $exist_member_flg}
    {assign var=update_member_flg value=0}
{/if}
{*}
```

#### プリプロセスで既に登録済みメンバーが存在するかチェックする為のオリジナル処理
```smarty
{assign_session key='exist_member_flg' value=0}
{if $smarty.request.email}
    {*emailでメンバー情報をfilter*}
    {assign var=email value=$smarty.request.email}

    {assign_array var=method_params values=''}
    {assign var=method_params.filter value='email='|cat:$email}
    {api_method var=list model="Member" method="list" method_params=$method_params}
    {if $list.list|@count > 0}
        {*存在する場合は新規登録しないので更新処理も行わない*}
        {assign_session key='exist_member_flg' value=1}
    {/if}
{/if}
```


以上でカスタム処理の完成です。

## APIのポストプロセスに作成したカスタム処理を設定
APIの一覧画面から「事前準備」で作成したフォーム送信のエンドポイントにポストプロセスを設定する。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a87610be9e87a96ec8f877864a359a25.png)

## Swaggerを利用して動作確認を行う
1. Swaggerから下記のサンプルデータでInquiryMessage:sendのAPIを呼び出す
2. 追加されたメンバー情報に送信したものと同じ内容のデータが入っていることを確認する

#### サンプルデータ
```json
{
  "name": "test user",
  "email": "email@example.com",
  "ext_01": "09022223333",
  "ext_03": "東京都世田谷区",
  "ext_04": "1",
  "ext_05": "1980-10-21",
  "body": "Example Message",
  "inquiry_category_id": 8
}
```
※`inquiry_category_id`は環境によって値の変更、もしくは送信しないで問題ありません。

#### 登録後メンバー情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee9e69768786f5821ddd970057a4155b.png)


以上です。

## 関連ドキュメント
- [フォームの回答を送付したユーザー向けに配信メッセージを送付する](/ja/docs/tutorials/how-to-implement-original-function-into-the-member-info-when-form-send-with-member-regist/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# メンバーを招待する

> 元ページ: `tutorials/how-to-invite-new-member` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-invite-new-member/

サイトへの新規メンバー登録を、相手のメールアドレスに招待メールを送る形で行います。  
所属するグループは招待する側が設定し、メンバー情報は招待メールを受け取ったメンバー自身が登録します。

## メンバーを招待する方法
**1. メンバー一覧画面にアクセスする**  
[メンバー管理] -> [メンバー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/702976f9920e36fdf69df964827b2cfa.png)

**2. 招待メールの作成画面を開く**  
[招待]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/93970143dbdafed0141234d30aa71415.png)

:::tip
「現在の設定では会員招待画面にはアクセスできません。」のメッセージが表示される場合は、新規メンバーの招待が許可されていないので、[新規メンバー登録条件](/ja/docs/management/registration-conditions/)のページで、新規メンバーの招待を許可するよう設定ください。
:::

**3. 招待状を送る**  
「招待したい人のメールアドレスを入力してください。」にメールアドレスを入力してください。複数名を招待したい場合は１行につき１名分のメールアドレスを入力します。  
「登録グループ」を選択して[次へ]をクリックしてください。  
参考) [招待する](/ja/docs/management/member-invite/)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f3ca84cc82a893429d8bc563c516eca6.png)

[送信する]をクリックすると設定したメールアドレス宛に招待メールが送付されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6a808a26ba7946cb04eaeae15674b2ff.png)

**4. 招待状からメンバー登録をする**  
招待状が届いたら、メール本文内にあるURLをクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3102f0a9706d128b5ea2eda2140e3122.png)
会員登録ページに遷移しますので、必要項目を入力し、[登録する]ボタンをクリックすると、メンバー登録が完了します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/05fdb2bc6bf3b7a10d8babd40a99db0a.png)
## 招待メールの編集方法
招待メールの内容はメッセージひな形で編集できます。  
**1. メッセージひな形一覧にアクセスする**  
[オペレーション] -> [メッセージひな形]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/be3fdd5c65007a98fd554828930f3384.png)

**2. デフォルト以外のメッセージひな形を表示する**  
カスタマイズしているメッセージひな形だけを表示したい場合は、[デフォルト以外]にチェックを入れて[検索]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/eeea4be60ea40a1b7f39199e8572f048.png)

**3. 招待メールのメッセージひな形を編集する**  
メッセージひな形の一覧から、識別子が「memberregist/invite」のメッセージひな形を探して、[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6dbcec2b3bd7d8486219385ec780ec86.png)

[メッセージひな形](/ja/docs/management/email-template/#メッセージひな形)を参考に内容を編集し、[更新する]をクリックしたら招待メールの編集は完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4d3d89f9e0a5ab0c63c817399a562f5.jpg)

## 関連ドキュメント
- [メンバー招待](/ja/docs/management/member-invite/)
- [新規メンバー登録条件](/ja/docs/management/registration-conditions/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)


---

# 社内ネットワークからアクセスした場合のみスーパーユーザーとなるグループを作成する

> 元ページ: `tutorials/how-to-make-new-group` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-make-new-group/
> 概要: 「グループ」にIPアドレス制限を設定すると、設定したIPアドレスからアクセスした場合にのみ権限が付与されるグループを作成できます。ここでは例として、社内ネットワークからアクセスした場合にのみ、スーパーユーザーとして振る舞うグループを作成します。

「グループ」にIPアドレス制限を設定すると、設定したIPアドレスからアクセスした場合にのみ権限が付与されるグループを作成できます。  
ここでは例として、社内ネットワークからアクセスした場合にのみ、スーパーユーザーとして振る舞うグループを作成します。

## グループを追加する
**1. グループ一覧画面にアクセスする**  
[メンバー管理] -> [グループ] をクリックし、グループ一覧画面にアクセスします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bca18f239cc2a408e3a8b8461f0220ec.png)

**2. [追加]をクリックする**  
画面右上の[追加]をクリックし、グループ追加画面にアクセスします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3197ce93c7d47ea91346b6bae042c7fb.png)

**3. グループ基本設定を入力する**  
[グループ基本設定](/ja/docs/management/group/)を参考にグループ基本設定を入力します。
ここでは例として、下記のように設定します。
- 名前: 管理者権限(社内NWのみ有効)
- ユーザー種別: スーパーユーザー
- IPアドレス制限: 許可するIPアドレスを入力

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b747568bb6d799974f29b778becec73a.png)

入力が完了したら[追加する]をクリックし、グループの追加は完了です。  
次にグループに所属するメンバーを設定します。

## メンバーの所属グループを変更する
**1. メンバー編集画面を開く**  
[メンバー編集](/ja/docs/management/member/)を参考にメンバー編集画面へアクセスします。

**2. 所属グループを設定する**  
[ID情報]タブの所属グループでプルダウンリストを開きます。  
ここでは「編集権限」と「管理者権限(社内NWのみ有効)」を選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/20ceed80dbec6cfd94b7dea0cef72380.png)

画面下部の [更新する]をクリックで設定完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ede52bd4c3fadd19862e3742e3361152.png)

このユーザーの場合は、社内ネットワークからログインした際は「編集権限」と「管理者権限(社内NWのみ有効)」の権限が適用され、その他のIPアドレスからログインした際は「編集権限」のみ権限が適用されます。

## 関連ドキュメント
- [グループ](/ja/docs/management/group/)
- [メンバー](/ja/docs/management/member/)
- [メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)
- [複数のIPアドレスをまとめて設定できますか？](/ja/docs/faq/is-it-possible-to-set-multiple-ip-addresses-at-once/)


---

# 配信の購読者を登録する

> 元ページ: `tutorials/how-to-register-subscribers-on-magazine` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-register-subscribers-on-magazine/
> 概要: 配信の購読者を登録する方法を説明します。購読者は配信毎に設定され、配信送付の際のあて先に利用します。

ここでは配信の購読者を登録する方法を説明します。
購読者は配信毎に設定され、配信送付の際のあて先に利用します。

## 配信の購読者を登録する方法
### 購読者のページにへアクセスする 
[チャネル] -> [一括配信] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

購読者の登録をしたい配信のタイトルをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2229dfa74261bed02bd1ee064ed6a33.png)

「購読者」タブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/20db58f0909005a069db019afaa1c6a3.png)

### 購読者を登録する
購読者の登録方法は下記2通りあります。
- 1件ずつ購読者を登録する
- CSVアップロードで購読者を一括登録する
それぞれ説明します。

#### 1件ずつ購読者を登録する方法
「メールアドレス」もしくは「メンバーID」を入力し、 「追加する」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1211c8993810e626efff60eb8726e2c7.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/358323a6935b67a444e03c2f1a2249a6.png)

「登録しました。」のメッセージが表示され、購読者でメールアドレスが追加されたことを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f07a12dde54ff9c2d8c2fd11737abfa.png)

#### CSVアップロードで購読者を一括登録する方法
**CSVファイルを準備する**  
購読者のページで、右上の[その他]をクリックし、[ダウンロード]をクリックしてCSVファイルをダウンロードします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c8e92a5572334620eede572755f8df5a.png)

購読者として登録したい「email」もしくは「メンバーID」を入力したら準備完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bba2ed0aa3b46698e14cbb405a594a52.png)

**CSVファイルをアップロードする**  
購読者のページで、右上の[その他]をクリックし、[アップロード]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/18a2bae4b606ca6124001029e8cd2be4.png)

アップロード種別とファイルを選択し、[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/897df3ee02756425576f106f8b90c0e4.png)

「更新しました。」のメッセージが表示され、購読者のアップロードが完了します。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/823088a6a2c3a3bdd13db5cd15e7bddb.png)

**追加した登録者を確認する。**  
購読者のページに戻り追加した購読者の確認をします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6288afeb30407c2f67be67d0da040b74.png)

以上で購読者の登録は完了です。

## 関連ドキュメント
- [配信 購読者一覧](/ja/docs/management/notification-subscribers/)
- [配信一覧](/ja/docs/management/notification-list/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)
- [配信購読者の登録・停止フォームを作成する](/ja/docs/tutorials/implement-a-magazine-subscription-unsubscription-form/)
- [複数のメールマガジンを一度に登録・解除するページを作成する](/ja/docs/tutorials/create-a-page-to-subscribe-and-unsubscribe-to-multiple-magazines-at-once/)


---

# パスワードリマインダー/パスワードリセットを設定する

> 元ページ: `tutorials/how-to-use-password-reminder` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-password-reminder/

会員登録サイトでは、ユーザーが登録したパスワードを忘れた際、パスワードを再発行するためのリマインダー機能が必要になります。  
メールに記載されたパスワード変更ページ用URLからユーザー自身が変更できます。また、ユーザー自身でパスワード情報を変更する機能も必要になります。

本チュートリアルでは、パスワードリマインダーとパスワードリセットを実行するエンドポイントを作成する方法を記載します。  

## パスワードリマインダーの設定
ユーザーがパスワードを忘れてしまった際に、パスワード再発行をするためのリマインダーメールを送信できます。

### 1. パスワードリマインダー用のエンドポイントを作成する
パスワードリマインダー用のエンドポイントを作成します。
[API]より対象のAPIを選択し、API管理画面より [新しいエンドポイントの追加] をクリックます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3575edd6842b897a0891f2e915d44ae.png)  

今回は下記設定にてエンドポイントを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/565e1cc6858e00451d26ca962e2ffd61.png)

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | repass |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | 認証 |
|  | モデル | Login |
|  | オペレーション | reminder |
| password_reset_page_url | /repass |  |

設定後、[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f06404de41248b0aaf971f11565b95e1.png)

### 2. パスワードリマインダーメール送信する
次に、作成したエンドポイントの実装内容をSwagger UIを利用して確認します。  
API画面より、[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acbad196996fa49f8cb397ee57043779.png)

Swagger UI画面が表示されるので、先ほど作成したエンドポイントをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d62ec56f7f80af1e9195e3ca29d788aa.png)

[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ba216b7de303e59ba77fc7a8d2f5571.png)

テキストエリアのメールアドレスに、サイトに登録されているユーザーのメールアドレスを記入し、[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1464d538679778e8bd0fa7152fdc1732.png)

レスポンスコード:200でデータがレスポンスされることを確認できました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7e4d0eb85c6f864ffc116aa2593583ac.png)

メールも送信されていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b07b1b76adf93e66f772e9f5ba1710a9.png)

パスワード再設定時に利用するので、パスワード設定画面の「?token=」以降の文字と、仮パスワードはコピーしておいてください。

なお、ユーザー登録されていないメールアドレスを記入すると、エラーが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7dab5d28d96c82cd2970ba6546b6f7a7.png)

### 3. パスワード再設定を行う  
次に、メールで送られてきた内容をもとにパスワード再設定します。
同じSwagger UI画面の「Request body」を下記のように修正します。

```
{
    "token": "*****",
    "temp_pwd": "*****",
    "login_pwd": "*****"
}
```

| 項目 | 値           | 
| :------- | :------------- |
| token | メールに記載されているtoken<br />(「?token=」以降の文字) |
| temp_pwd | メールに記載されている仮パスワード |
| login_pwd | 新パスワード |

記載したら[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa65855f7a1ea1ca7ae006d7fdc5cd2f.png)

レスポンスコード:200でデータがレスポンスされることを確認できました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/af7bae6c389007412a264c0333002a06.png)

以上でパスワードリマインダーの設定と、Swagger UIでの確認、パスワード再設定方法を完了します。

## パスワードリセットの設定
ユーザーにてパスワード再設定をする際に利用します。

### 1. パスワードリセット用のエンドポイントを作成する
パスワードリセット用のエンドポイントを作成します。
[API]より対象のAPIを選択し、API管理画面より [新しいエンドポイントの追加] をクリックます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3575edd6842b897a0891f2e915d44ae.png)

今回は下記設定にてエンドポイントを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62d05754844045eb715300048cdb3dc7.png)

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | password_reset |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | 認証 |
|  | モデル | Login |
|  | オペレーション | reset_password |

設定後、[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad15d4972392d881404908019c296dcc.png)

### 2. パスワードリセットを行う
次に、作成したエンドポイントを利用してパスワードリセットを実行します。今回はSwagger UIを利用して確認します。  
API画面より、[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acbad196996fa49f8cb397ee57043779.png)

Swagger UI画面が表示されるので、先ほど作成したエンドポイントをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/06d7c30173c98dd172f121698d7638b1.png)

[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/36389f644e6e00ef3a8ee4b0a85bf97b.png)

テキストエリアに下記記入します。

| 項目 | 値           | 
| :------- | :------------- |
| login_id | ユーザーのメールアドレス |
| current_password | 現在のパスワード |
| new_password | 新しいパスワード |

記入したら、[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/afac4aa4f1b1c11347f3fa0db92d0ff8.png)

レスポンスコード:200でデータがレスポンスされることを確認できました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ef4ed11be3b7c4b51f7c34184469ef2.png)

なお、ユーザー登録されていないメールアドレスを記入すると、エラーが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57169d719b97a84526d0a16c757e5387.png)

以上でパスワードリセットの設定と、Swagger UIでの確認方法を完了します。

## 関連ドキュメント
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [reCAPTCHAを利用したパスワードリマインダーを作成する](/ja/docs/tutorials/using-recaptcha-for-password-reminders/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [メッセージひな形](/ja/docs/management/email-template/)


---

# 代理ログイン機能の使い方

> 元ページ: `tutorials/how-to-use-proxy-login` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-proxy-login/
> 概要: Kurocoの代理ログイン機能を使って、管理者が別のメンバーとしてログインする方法を説明します。設定方法やユースケース、注意点を含めたチュートリアルです。

Kurocoの代理ログイン機能を使うと、特定のメンバーが別のメンバーのアカウントに代わりにログインできます。
本チュートリアルでは、代理ログインの設定方法と利用手順について説明します。

## 代理ログインとは

代理ログインは、特定の権限を持つメンバーが、別のメンバーのアカウントに代理でログインできる機能です。
主に以下のような場面で活用できます。

- メンバーがログインできない場合のサポート対応
- メンバーの画面表示やデータの確認
- メンバーに代わってコンテンツの操作や設定変更を行う
- 複数グループに所属するユーザーが、グループごとにアカウントを切り替えて利用する

:::caution
代理ログインの**設定**（メンバー編集画面での代理ログイン許可の付与）には、編集ユーザーまたはスーパーユーザー権限が必要です。
:::

## 前提条件

- 代理ログインの**設定**を行うには、編集ユーザーまたはスーパーユーザー権限を持つメンバーであること
- 代理ログインの**利用**は、管理画面へのアクセス権限がないメンバーでも可能（`Login/alias_login` エンドポイント経由）

## 設定手順

### ステップ1: メンバー編集画面を開く

1. Kuroco管理画面にログインします。
2. [メンバー管理] -> [メンバー]をクリックします。
3. メンバー一覧から、代理ログインを**される側**（ログイン先）のメンバーの名前をクリックして編集画面を開きます。

### ステップ2: 代理ログイン許可を設定する

メンバー編集画面のID情報セクションにある「代理ログイン許可」フィールドを見つけます。

|項目|説明|
| :--- | :--- |
|代理ログイン許可|代理ログインを許可するメンバーIDを入力し、自分の代わりにログインできる人を設定できます。|

1. 「代理ログイン許可」フィールドに、代理ログインを**する側**（管理者側）のメンバーIDを入力します。
2. 複数のメンバーに代理ログインを許可する場合は、それぞれのメンバーIDを入力します。
3. [更新する]をクリックして設定を保存します。

:::tip
メンバーIDは、メンバー一覧画面の「ID」列で確認できます。
:::

### ステップ3: 代理ログインを実行する

代理ログインの実行方法は、管理画面からの実行とAPIからの実行の2通りがあります。

#### 管理画面から実行する場合

管理画面へのログイン権限を持つメンバーは、管理画面から代理ログインを実行できます。

1. 代理ログインを許可されたメンバーで管理画面にログインします。
2. 画面上部に表示されるメンバーのアイコンをクリックします。
3. 「代理ログイン」を開き、ログインしたいメンバー名をクリックします。
4. 対象メンバーとしてログインした状態になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d573c16dfa087b7388cbad6f4ea92a04.png)

:::info
管理画面の「Login as」ドロップダウンには、管理画面へのログイン権限を持つメンバーのみが表示されます。
:::

#### APIから実行する場合

管理画面へのアクセス権限がないメンバーでも、`Login/alias_login` エンドポイントを使用して代理ログインを実行できます。
フロントエンドから代理ログインを実装する場合は、この方法を使用します。

:::info
代理ログイン中は、対象メンバーの権限でフロントエンドやAPIにアクセスすることになります。メンバーのプロフィール情報やコンテンツの閲覧権限などが、対象メンバーのものとして適用されます。
:::

:::tip
ログイン中のメンバーがどのメンバーIDで代理ログインできるかは、`basic_info`のパラメータに`aliaslogin_target`を設定した`Login::profile`のエンドポイントで確認可能です。
:::

## 設定例

### 例1: 管理者がカスタマーサポートとして利用する

カスタマーサポート担当者（メンバーID: 1）が、一般メンバー（メンバーID: 100）のアカウントに代理ログインする場合：

1. メンバーID: 100の編集画面を開きます。
2. 「代理ログイン許可」フィールドにメンバーID `1` を入力します。
3. [更新する]をクリックして保存します。

これにより、メンバーID: 1でログインした管理者が、メンバーID: 100として代理ログインできるようになります。

### 例2: 複数の管理者に代理ログインを許可する

複数のサポート担当者（メンバーID: 1, 2, 3）に代理ログインを許可する場合：

1. 対象メンバーの編集画面を開きます。
2. 「代理ログイン許可」フィールドにメンバーID `1`, `2`, `3` をそれぞれ入力します。
3. [更新する]をクリックして保存します。

## 注意事項

- **設定には編集ユーザー以上の権限が必要**: 代理ログインの設定（代理ログイン許可の付与）には、編集ユーザーまたはスーパーユーザー権限が必要です。
- **利用は管理画面権限不要**: 代理ログインの利用（実行）は、管理画面へのアクセス権限がないメンバーでもAPIエンドポイント（`Login/alias_login`）経由で可能です。
- **操作の責任**: 代理ログイン中に行った操作は、操作ログ等に記録されます。代理ログインの利用は必要最小限にとどめてください。
- **セキュリティの考慮**: 代理ログインの許可は、信頼できるメンバーのみに付与してください。不要になった代理ログイン許可は速やかに削除してください。
- **ログイン許可が必要**: 代理ログインの対象メンバーの「ログインの許可」が有効になっている必要があります。

## 関連ドキュメント

- [メンバー](/ja/docs/management/member/)
- [メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)


---

# Microsoftを利用してOAuth認証によるSSOを実装する

> 元ページ: `tutorials/implement-login-with-microsoft` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implement-login-with-microsoft/
> 概要: KurocoをOAuthサービスプロバイダーとして使用し、Microsoftを利用したSSOを実装する（Microsoft AzureおよびMicrosoft Entra）

KurocoをOAuthサービスプロバイダーとして使用し、Microsoftを利用したSSOを実装する方法について説明します。

:::info
本チュートリアルは、任意のMicrosoftユーザーがKurocoにログイン/登録できるようにする、OAuth認証を利用した実装を説明するものです。  
Active Directory B2Cを使用したユーザーフロー制御SSOについては、[IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する](/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)を参照してください。
:::

:::caution
OAuth認証では、IdP（アイデンティティプロバイダー）側の任意の組織のアカウントでログインが可能になります。そのため、**管理画面へのログインにSSOを利用する場合は、組織単位でのアクセス制御が可能な[SAML認証](/ja/docs/management/sso-saml-sp/)の利用を推奨します。**

本チュートリアルでは動作確認を容易にするため、ターゲットドメインを管理画面に設定していますが、実運用で管理画面へのSSOログインを実装する場合はSAML認証をご検討ください。

OAuth SSOはフロントエンドでの利用に適しています。フロントエンドで利用する場合は、本チュートリアルでのOAuth SP設定に加えて、[フロントエンドでSSOログインを利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)を参照し、アクセストークンの発行方法を実装してください。
:::

## 前提条件
Microsoftアカウントを所持していることが前提となります。

## Kuroco管理画面でSP設定を追加
まず、Kurocoの管理画面でOAuth SP設定を追加します。

**1. SSO OAuth SP設定ページにアクセスする**  
[OAuth SP一覧](/docs/management/sso-oauth-sp/)に遷移し、[Add]ボタンをクリックして新しいサービスプロバイダーを追加します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a15eaa8703e8c9e70e613234146d47b5.png)

**2. SP設定を追加する**  
SSO OAuth SP編集ページで以下を入力し、[追加]ボタンをクリックします。

| 項目 | 値 |
| :-- | :--- |
| OAuth SPの名称  | 任意の名前。これは内部参照用であり、Microsoft側と一致する必要はありません。 |
| 有効   | チェックを外す |
| ターゲットドメイン | ユースケースに応じてAPIアクセス用または管理パネルへのログインを許可するためのものです。このチュートリアルでは管理画面を設定します。 |
| タイプ | Microsoft IDを選択。 |
| ユーザーの自動登録 | 新規アカウントを許可するかどうかに応じてチェックボックスを選択します。このチュートリアルではチェックします。|
| 登録時に設定するグループ | 登録時に割り当てられるユーザーグループ。このチュートリアルでは、Administratorを設定します。|

:::warning
新規メンバーに管理者グループを使用すると、意図しないメンバーがサインアップして管理者権限を得るリスクがあります。実際の運用時には、新規ユーザー登録を無効にするか、より制限された権限のグループを選択することをお勧めします。
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4c0c5f94cfd82ffb420311a7e5ef5ca7.jpg)

**2. ログインURLをコピーする**  
設定の追加後、追加したサービスプロバイダー名をクリックして、SSO OAuth SP編集画面を開き、ログインURLをコピーします。このURLはMicrosoftポータルでの設定に利用します。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1819949ff0a19fc621f878686bb4cb28.png)

## Microsoftポータル設定
次に、[Microsoft Azureポータル](https://portal.azure.com/)または[Microsoft Entraポータル](https://entra.microsoft.com/)でOAuthアプリ登録と設定を行います。  
- 画面はMicrosoftの仕様によって変更される場合があります。

**1. OAuthアプリケーション設定ページにアクセスする**  

**Azureポータル:**

Azureポータルでは、クイックアクセスもしくは検索からMicrosoft Entra External ID（ポータル上では[Azure AD B2C]と表示される場合があります）をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bbaf68059cb6562b91a6ad188de39441.png)
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/95975fba6824d3d443c3cceb25fa324a.png)

**Entraポータル:**

Entraポータルでは、サイドメニューもしくは検索から[アプリの登録]を選択します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a28d8dd047411130a9cb21f603a9735f.png)
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/092b59604e082e3402cb4668b5e17c9e.png)


**2. 新しいアプリケーションを作成する**  

**Azureポータル:**

Azureポータルでは、アプリ登録をクリックしてから、新規登録をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c9399def755f32134f1f05b3b6df8933.png)
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7e3504e8ae54330fae81c0520ff24f66.png)

**Entraポータル:**

Entraポータルでは、新規登録をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b5310075ea0a522138d6a954d82a121c.png)


**3. アプリケーション設定を入力する**  
これ以降のステップは、Microsoft AzureポータルとMicrosoft Entraポータルで同じです。  
そのため、このチュートリアルでは、これ以降はMicrosoft Azureポータルのキャプチャで説明します。

設定に以下を入力して[登録]ボタンをクリックします。

| 項目 | 値 |
| :-- | :-- |
| 名前 | 任意の名前。これはMicrosoftポータル内での内部参照用であり、Kurocoと一致する必要はありません。 |
| サポートされるアカウントの種類  | このアプリケーションを使用するユーザーの種類に応じて選択します。このチュートリアルでは、すべてを許可します。 |
| リダイレクトURI (ドロップダウン) | Webを選択 |
| リダイレクトURI (テキストフィールド) | KurocoのSSO OAuth SP編集画面からコピーしたログインURLを貼り付け |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b061d66590dceef62a6c977640a79aae.png)

**3. アプリケーション（クライアント）IDをコピーする**  
登録が成功した後、ダッシュボードからアプリケーション (クライアント) IDをコピーします。これは、KurocoのOAuth SP編集画面に設定します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5c25b839faf9ecce12fd1b629a868e0f.png)

**4. クライアントシークレットを作成する**  
[証明書とシークレット]をクリックしてから、[新しいクライアントシークレット]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/951b9e951c6494ec456428a42c7f4ab1.png)

**5. シークレットの説明と有効期限を更新する**  
説明を入力し、有効期限を選択します。

:::caution
シークレットの有効期限が切れた後は、新しいシークレットを発行し、KurocoのOAuth SP編集画面に設定する必要があります。
:::

データを入力した後、[追加]をクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cefd1fc35bbc4fd40a2969e931d381f9.png)

**6. シークレット値をコピーする**  
クライアントシークレットの登録に成功した後、ダッシュボードからシークレット値をコピーします。これは、KurocoのOAuth SP編集画面に設定します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0f21e6cd8c8da7e5a5d474e1dc67b1e0.png)

以上で、Microsoftダッシュボードでのステップは完了です。

## Kuroco OAuth SP編集の設定
Microsoft OAuthアプリからコピーしたクライアントIDとクライアントシークレットをKuroco管理画面のOAuth SP編集画面に入力し、[更新]をクリックします。

| 項目 | 値 |
| :-- | :-- |
|有効|チェックを入れる|
| クライアントID (Client ID)   | ステップ4でコピーした[アプリケーション（クライアント）ID]の値 |
| クライアントの秘密鍵 (Client Secret) | ステップ6でコピーした[シークレット]の値 |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2b1057476f3be207afafe15c2bd9bab6.png)

## 使用方法
作成されたOAuth SP画面を確認します。
SSO OAuth SPリスト画面で作成したSP設定の[ログインOAuth SP名]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e2b09e7c779b70a117e50eb901e73317.png)

[ログインURL]が表示されるので、 シークレットモードでURLを開きます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f8cad4364277c24880ff46848f3e8e93.png)


または、タイプが管理パネルに設定されているので、管理パネルのログイン画面に移動し、外部ログインSSOの[外部アカウントでログイン]リストからSPを選択します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d89e4b42b497ab0c4b970e5d9d031dda.png)

Microsoftログイン画面に遷移し、SSOが使用できます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0d4b4b2c9e8ec77c12d09b2b8aac3910.png)

アプリを通じて初めてログインする新規アカウントの場合、権限を求められます。  
追加情報の登録が必要な場合は、カスタムのタイプを使用し、希望のスコープを追加することも可能です。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8f5432990cbb637a092ce44596cb0f98.png)

## 関連ドキュメント
- [OAuth SP](/ja/docs/management/sso-oauth-sp/)
- [SSOによるログインをフロントエンドで利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)
- [IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)
- [Microsoft Entra IDを使用してSCIMプロビジョニングを実装する](/ja/docs/tutorials/implementing-scim-provisioning-with-microsoft-entra-id/)
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [OAuthを使用したシングルサインオンはできますか](/ja/docs/faq/can-I-use-single-sign-on-using-oauth/)


---

# 一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する

> 元ページ: `tutorials/implement-reminder-and-automatic-deletion-of-members` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implement-reminder-and-automatic-deletion-of-members/
> 概要: バッチ処理を利用して、一定期間ログインの無いメンバーに対してリマインド送付と自動退会の機能を実装します。また、ログインがあった場合に有効期限を伸ばす機能は「ログイン後処理」をトリガーにしたカスタム処理で実装します。

## 概要
バッチ処理を利用して、一定期間ログインの無いメンバーに対してリマインド送付と自動退会の機能を実装します。  
また、ログインがあった場合に有効期限を伸ばす機能は「ログイン後処理」をトリガーにしたカスタム処理で実装します。

### 学べること
以下の手順で一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装します。
- [事前準備](#事前準備)
- [リマインド機能の実装](#リマインド機能の実装)
- [自動退会機能の実装](#自動退会機能の実装)
- [ログイン後にログイン許可の有効期限を延ばす機能の実装](#ログイン後にログイン許可の有効期限を延ばす機能の実装)

### 前提条件
動作確認に利用するメンバー及びグループは適宜追加することとします。  

## 事前準備
### メンバーにログイン許可の有効期限を設定
ログイン許可の有効期限は、後で設定するカスタム処理で自動的に追加されますが、動作の確認のためまずは手動で設定します。  
[メンバー管理] -> [メンバー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9233a93df746e9dd8d780f6b1c0c368.png)

メンバー一覧のページでテーブル右上の歯車マークから、表示項目設定を開き、「ログイン許可期限」の表示を追加しておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8cd347e117d972fa93bc7699c4fc40f2.png)

メンバー一覧から設定をするメンバーの名前をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc5f95c0c215d81884e6d94362c8596a.png)

ログイン許可の有効期限を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88c15699cae8ae8473c698d0cf90155d.png)

「メルマガ拒否フラグ」のチェックが外れていることを確認します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/617428680855a4f9339cd5688e4268c9.png)

同様に動作確認用のメンバーにログイン許可期限を設定して、以下のようにしました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3f162f67c0f1d707e31a202ed64ffed.png)

### 内部処理用のAPI作成
Kuroco内部でのみ利用するエンドポイントはAPIを分けておくことをお勧めします。  
そこで、まずは内部利用のためのAPIを新規で作成します。  
既に追加済みの場合は次のステップに進んで構いません。  

#### APIの作成
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c341acced8d685e67ec1da1e85abac.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Internal|
|版|1.0|
|ディスクリプション|内部処理用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c04c600fc74102913e9e668ae5cca0e.png)

#### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bc5cb1beb28c74ede6aeca89715a647.png)

セキュリティを[動的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62aaa225db5d12ee84ccc6d5a52411fe.png)

セキュリティを[動的アクセストークン]に設定後、`Login::token`のエンドポイントが無い場合、利用をお勧めされますが、内部利用のみの場合は無視して構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb1efe099bdae8f1c0481037416a5d9.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74cd7a36fd926dbc20b04812553072c7.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2bc3744fe6a2ab042456fa8c635195c.png)

問題なければ [保存する] をクリックします。  

## リマインド機能の実装
リマインド機能は以下の流れで動作をさせます。
- バッチ処理で毎日06:00に、エンドポイントにリクエストを送る。
- エンドポイントは設定された配信IDに、メッセージひな形の識別子とカスタムメンバーフィルターIDの情報を送る。
- 配信はメッセージひな形の内容をカスタムメンバーフィルター宛に送信する。

### カスタムメンバーフィルターの作成
リマインド送付の対象者はカスタムメンバーフィルターで設定します。    
[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b8b8332df9870a7bdcec7b5474cf562.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0403ee2fe9d2f335ee495c8a6060f71c.png)

以下のフィルタを作成します。  
管理者およびDeveloperのメンバーを除いて、有効期限が30日前の場合と、7日を切っている場合をリマインド送付の対象者とします。

|項目|設定|
|:--|:--|
|タイトル|ログイン許可有効期限のリマインド送付対象者|
|絞り込み条件|以下の通り|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ebfb7f7f271d120aed7954fe16c72e4b.jpg)

[結果を閲覧する]をクリックして、想定通りのメンバーがヒットするか確認します。  
複数の条件がある場合はテストメンバーのログイン許可有効期限を手動で変更しながら確認してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f36b104a2261171c2e85c3a106f795f.png)

問題なければ[追加する]をクリックしてカスタムメンバーフィルターを追加します。  
作成したカスタムメンバーフィルターのIDは後ほど利用するのでメモをしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2f663c1d4ffb324452d1fe428f29f90.png)

### 配信の作成
リマインドメールの送付は配信の機能を利用します。  
[チャネル] -> [一括配信] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1118c911e95b78fe2423d6bf66e2e916.png)

以下の内容を設定します。  

|項目|設定|
|:-|:--|
|タイトル|ログイン許可有効期限のリマインド|
|メール送信元（From）|`noreply@kuroco-mail.app`|
|その他の設定|デフォルトのまま|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c068495bb9453be9a1f4a1d7da6318d1.png)

- バッチ処理実行時に設定するので、あて先も設定なしで構いません。
- fromのメールアドレスを変更したい場合は[SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)を参考にSendgridと連携してください。

設定ができたら[追加する]をクリックして配信を追加し、配信IDをメモしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7e76584f39b7de5cb5f16234b06dd6fa.png)

### メッセージひな形の作成
リマインドメールの文面はメッセージひな形を利用して作成します。  
[オペレーション] -> [メッセージひな形]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1248d218b3a9b24a8c292f17a355801e.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1b2f6a592700bcb6f48b83f38c4b5f3.png)

以下のように設定します。  

|項目|設定内容|
| :--- | :--- |
|テンプレート|ログイン許可有効期限のリマインド文言|
|識別子|expiration_remind_template|
|本文|以下の内容|

```html
%name1% %name2% 様<br>
<br>
ログインの有効期限は%login_ok_ymd%までとなっております。<br>
有効期限までに再度ログインしてください。
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0e6a154ae40bd9d21202cc47298019e.png)

設定ができたら[追加する]をクリックしてメッセージひな形を追加します。  

### カスタム処理の作成
配信では`%name1%`、`%name2%`と記入すると、あて先のメンバーの名前を表示できますが、`%login_ok_ymd%`などデフォルトで利用できない項目や、複雑な処理を追加したい場合はカスタム処理を利用します。

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a0256fcb7617a95ab332d2943923d08.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|配信の差し込み|
|識別子|magazine_substitution|
|これを使ったコンポーネント|トリガー：配信の差し込み<br/>値：利用する配信ID(2)|
|処理|以下のコードを入力します。|

```smarty
{assign_array var=substitutions values=''}
{assign var=substitutions.name1 value=$member_info.name1}
{assign var=substitutions.name2 value=$member_info.name2}
{assign var=substitutions.login_ok_ymd value=$member_info.login_ok_ymd|date_format:'%Y年%m月%d日'}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b9803c7238755a55c5c6a98d33f07457.png)

設定ができたら[追加する]をクリックしてカスタム処理を追加します。  

### エンドポイントの作成
次にエンドポイントを作成します。  
InternalのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|expiration_remind|
|カテゴリー|配信|
|モデル|Magazine|
|オペレーション|send|
|destination_id|カスタムメンバーフィルターのID(1)|
|mail_type|1|
|mail_template_name|メッセージひな形の識別子(expiration_remind_template)|
|subject|ログインの有効期限を確認してください|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1409dcc31ea8eedcc288126a9a61d674.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/eeb9ff4e0707a53e9f772c380dc438b8.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。  

### バッチ処理の作成
リマインド機能はバッチ処理で作成し、日次で対象者の確認及びリマインドメールの送付をします。  
[オペレーション] -> [バッチ処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbbe745e3943541e470fb5c0dc66969f.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/82e14b4bc626dd8d97c97d7ac082842f.png)

以下のように設定します。  

|項目|設定内容|
| :--- | :--- |
|テンプレート|ログイン許可有効期限のリマインド送付|
|識別子|send_remind_mail|
|バッチ|毎日 06:00|
|処理|以下のコード|

```smarty
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/4/expiration_remind/2'
    method='POST'
    member_id='1'
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/035e368c5c0f3d65facfad7b19663cf0.png)

入力ができたら[追加する]をクリックしてバッチ処理を追加します。 

### 動作確認
最後に、[すぐに実行する]をクリックして動作の確認をします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2fe8f8fea48e2e06c35789a8779bba56.png)

正しく設定ができていれば以下のようにリマインドメールが届きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/78fd353e75e571932929e51a47d72f9e.png)

## 自動退会機能の実装
自動退会機能はバッチ処理で作成し、日次で対象メンバーの有無を確認し、対象メンバーが存在する場合はMember::deleteのエンドポイントを利用して削除をします。

### カスタムメンバーフィルターの作成
自動退会の対象者はカスタムメンバーフィルターで設定します。  
[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b8b8332df9870a7bdcec7b5474cf562.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b13c7749146d2497ad376630d6452df5.png)

以下のフィルタを作成します。

|項目|設定|
|:--|:--|
|タイトル|自動退会処理の対象者|
|絞り込み条件|以下の通り|
  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/15766cabc5beb6b641b273154c189531.jpg)

フィルター結果の確認をして、問題なければ[追加する]をクリックしてカスタムメンバーフィルターを追加します。

作成したカスタムメンバーフィルターのIDは後ほど利用するのでメモをしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2996b6d6aa5b68ece252a48b5f3a73d4.png)

### エンドポイントの作成
削除対象のメンバーリストを返すエンドポイントと、メンバーを削除するためのエンドポイントの2つを作成します。  
InternalのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

#### delete_member_listエンドポイント
以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|delete_member_list|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|list|
|custom_search_id|カスタムメンバーフィルターのID(2)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6c1e7bb05ec9d3a402be4f0d45f031b.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/47cb9c22b7e045bd9bf85153025d27ad.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。  

#### expired_member_deleteエンドポイント
同様にメンバーを削除するための以下のエンドポイントを作成します。  

|項目|設定内容|
| :--- | :--- |
|パス|expired_member_delete|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|delete|
|allowed_group_ids|削除対象となるメンバーが所属するグループを設定します。(101,102)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbc9f086776368cac3824c42f70855fe.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/da75abe728e98a6f00892180ab8bc553.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。  

### バッチ処理の作成
続いてバッチ処理を作成します。  
[オペレーション] -> [バッチ処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbbe745e3943541e470fb5c0dc66969f.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/664166e4272e9a9381421bce387098fd.png)

以下のように設定します。  

|項目|設定内容|
| :--- | :--- |
|タイトル|有効期限切れメンバーの削除|
|識別子|delete_expired_member|
|バッチ|毎日 05:00|
|処理|以下のコード|

```smarty
{*対象メンバーの取得*}
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/4/delete_member_list'
    method='GET'
    member_id='1'
}

{*対象メンバーの削除*}
{foreach from=$response.list item=n}
    {assign var='target' value="/rcms-api/4/expired_member_delete/`$n.member_id`"}
    {* member_id=1 -> admin user *}
    {api_internal
        var='response'
        status_var='status'
        endpoint=$target
        method='POST'
        member_id='1'
    }
    {logger msg1="`$n.name1``$n.name2`(member_id=`$n.member_id`)を削除します。" msg2=$response}
{/foreach}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75cc361961bb8ef5c734b89e2bd0ec43.png)

入力ができたら[追加する]をクリックしてバッチ処理を追加します。 

### 動作確認
最後に、[すぐに実行する]をクリックして動作の確認をします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/54c198478e7a4aba17f6db0288119869.png)

正しく設定ができていれば以下のようにカスタムログにログが残り、メンバーが削除されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6804f92660cc1cadab674955496835e.png)


## ログイン後にログイン許可の有効期限を延ばす機能の実装
最後に、ログイン後にログイン許可の有効期限を自動で延ばす機能を実装します。  
こちらはメンバーのログイン後をトリガーにカスタム処理を実行し、Member::updateのエンドポントで`login_ok_ymd`を更新します。

### エンドポイントの作成
InternalのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|member/update_login_ok_ymd|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|update|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dcf0a24ead3ca0e254e5c28db37d021c.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a77be43d3c52d08a5e271b056473797.png)

### カスタム処理の作成
[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cf05595e31dd0f905466ec2a09bb835.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|ログインしたらログイン許可期間を延ばす|
|識別子|update_login_permission_date|
|これを使ったコンポーネント|トリガー：ログイン後処理<br/>値：0|
|処理|以下のコード|


```smarty
{assign_member_detail assign_group_flg=1 var='member_detail' member_id=$member_id}

{* add extending 1y *}
{assign_array var="payload" keys="login_ok_ymd" values="1 year"|strtotime|date_format:"Y-m-d"}

{if
    "1"|rcms_in_array:$member_detail.arrGroup_id ||
    "2"|rcms_in_array:$member_detail.arrGroup_id
}
  {* skip execution when the user supposed to be administrator *}
{else}
    {* member_id=1 -> admin user *}
    {api_internal
        var='response'
        status_var='status'
        endpoint='/rcms-api/4/member/update_login_ok_ymd'
        method='POST'
        queries=$payload
        member_id=$member_id
    }
    {logger msg1="`$member_detail.name1``$member_detail.name2`(member_id=`$member_id`)のlogin_ok_ymdを更新します。" msg2=$response}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d1add74a2d4b4145627237afca37adc.png)

### 動作確認
最後に、動作確認のため、対象のメンバーでログインをします。  

正しく設定ができていれば以下のようにカスタムログにログが残り、メンバーのログイン許可の有効期限が更新されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bac4f40cea4593e148bf19e805cc5439.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/861b3aa62feb7bedbf5bdb881617faea.png)

以上で、一定期間ログインの無いメンバーへのリマインドおよび自動退会機能の実装ができました。  

## 関連ドキュメント
- [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)
- [カスタム処理に利用できる変数一覧](/ja/docs/reference/trigger-variables/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [カスタム処理でデバッグを目的としたログを出力できますか？](/ja/docs/faq/can-the-original-process-output-logs-for-debugging-purposes/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)


---

# GitHubを利用してOAuth認証によるSSOを実装する

> 元ページ: `tutorials/implementing-oauth-sp-based-sso` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-oauth-sp-based-sso/
> 概要: KurocoはOAuth SPの機能を持っており、SSOの実装が可能です。また、プリセットとしていくつかの外部サービスをご用意しており、対応したサービスの場合は簡単に設定ができます。本チュートリアルでは、OAuth認証によるSSOを実装する例としてGitHubでのログインを実装します。

## 概要
KurocoはOAuth SPの機能を持っており、SSOの実装が可能です。
また、プリセットとしていくつかの外部サービスをご用意しており、対応したサービスの場合は簡単に設定ができます。

本チュートリアルでは、OAuth認証によるSSOを実装する例として下記条件でのログインを実装します。  

- Kuroco管理画面に対してログインする
- GitHubのOAuthを利用する
- GitHubと同じEmailのメンバーでKurocoにログインする

:::caution
OAuth認証では、IdP（アイデンティティプロバイダー）側の任意の組織のアカウントでログインが可能になります。そのため、**管理画面へのログインにSSOを利用する場合は、組織単位でのアクセス制御が可能な[SAML認証](/ja/docs/management/sso-saml-sp/)の利用を推奨します。**

本チュートリアルでは動作確認を容易にするため、ターゲットドメインを管理画面に設定していますが、実運用で管理画面へのSSOログインを実装する場合はSAML認証をご検討ください。

OAuth SSOはフロントエンドでの利用に適しています。フロントエンドで利用する場合は、本チュートリアルでのOAuth SP設定に加えて、[フロントエンドでSSOログインを利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)を参照し、アクセストークンの発行方法を実装してください。
:::

### 学べること
以下の手順でOauth SPによるSSOの実装を学びます。

- [Kurocoの設定](#kurocoの設定)
  - [OAuth SP設定を追加する](#oauth-sp設定を追加する)
- [GitHubの設定](#githubの設定)
  - [OAuth Appsを追加する](#oauth-appsを追加する)
  - [秘密鍵を生成する](#秘密鍵を生成する)
- [KurocoのOAuth SP設定を更新する](#kurocoのoauth-sp設定を更新する)
- [利用方法](#利用方法)

### 前提条件
:::info
GitHub側の仕様の変更により、Client ID、Client secretsの取得方法は本チュートリアルと異なる場合がございます。詳細はGitHubで最新情報をご確認ください。  
:::

## Kurocoの設定
### OAuth SP設定を追加する
[外部システム連携] -> [ID連携] -> [OAuth SP]をクリックします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/73eb838e1113048df534ea34be2b9b34.png)
[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa509003cbad6d80b36a622488e8d68e.png)

OAuth SP編集画面が表示されますので、下記を入力して[追加する]をクリックします。  

|項目   |設定内容  |
| :--- | :--- |
|OAuth SPの名称|お好きな名前|
|ターゲットドメイン|管理画面|
|タイプ|GitHub|
|自動ユーザー登録|チェックを入れない|
|Emailを利用せずメンバー拡張項目にIDを格納してリンクする|チェックを入れない|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/333e97ef6f93e653502f9ae72accaac1.jpg)

追加されたOAuth SPの編集画面から、ログインURLをメモしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1d6a3d8ec027909c3f7eb1995bab700.png)

## GitHubの設定
### OAuth Appsを追加する
次にGitHub側の設定をします。  
[GitHubのOAuth Appsの設定ページ](https://github.com/settings/developers)にアクセスし、[New OAuth App]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/dc6b88cb76b1f39583d00088d3fc3e70.png)
下記の内容を入力して[Register application]をクリックします。  

|項目   |設定内容  |
| :--- | :--- |
|Application name|お好きな名前|
|Homepage URL|サイトのURL|
|Authorization callback URL|[OAuth SP設定を追加する](#oauth-sp設定を追加する)でメモしたログインURL|

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/30d1d4adf17e669d67fa16d0826876ab.png)

### 秘密鍵を生成する
追加されたOAuth Appsのページから[Generate a new client secret]をクリックします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a828b511ec0345f67ab4d4ea32f02a7d.png)

Client IDと、生成されたClient secretsをメモしておきます。  
ページを遷移すると、Client secretsは再度表示できません。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/179d95544175f6877b8bca47f016009b.png)

## KurocoのOAuth SP設定を更新する
GitHubの設定が完了したら、再度Kurocoの設定に戻ります。  
[外部システム連携] -> [ID連携] -> [OAuth SP]をクリックします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/73eb838e1113048df534ea34be2b9b34.png)

[OAuth SP設定を追加する](#oauth-sp設定を追加する)で追加したOAuth SPの名称をクリックします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/caf1dc02c31f8dc8403a44c297c54afa.png)

[秘密鍵を生成する](#秘密鍵を生成する)で取得したクライアントの秘密鍵 (Client Secret)と、クライアントID (Client ID)を入力し、[有効]にチェックを入れて[更新する]をクリックします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b88e8facb4a666afd788e11f13a39817.png)

以上で、SSO OAuth SPの設定は完了です。  

## 利用方法
ターゲットドメインを管理画面に設定していると、SP設定の追加後、自動でログインページに「外部アカウントでログイン」の項目が追加されます。  
リンクをクリックすると、GitHubのログイン画面に遷移します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3858a548ccfdc986c2a56ef71d4f3d9f.png)

また、SSO OAuth SP編集画面のログインURLを使って独自のログインページを作ることも可能です。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04194089ff9f1be7f98a3c325433da2d.png)

## 参考
### クライアントIDと秘密鍵の入手先
タイプの設定で選択できる主要なアイデンティティプロバイダのクライアントIDと秘密鍵の入手先を下記に示します。  
GitHub以外のIdPでSSOを実装する場合は参考にして下さい。    

| IdP | URL | クライアントID, 秘密鍵の名称 |
| :--- | :--- | :--- |
|GitHub|https://github.com/settings/developers|Client ID, Client secrets|
|Google|https://console.cloud.google.com/apis/credentials|クライアント ID, クライアント シークレット|
|Facebook|https://developers.facebook.com/apps|アプリID, app secret|
|LINE|https://developers.line.biz/console/|チャネルID, チャネルシークレット|

### カスタムについて
タイプの選択肢にないサービスについても、カスタムのタイプを利用してOAuth認証によるSSOを実装可能です。  
まず接続しようとしているアイデンティティプロバイダがOAuth 2.0の仕様をサポートしていることを確認してください。
もしサポートしている場合はアイデンティティプロバイダのドキュメントを確認し、[SSO OAuth SP](/ja/docs/management/sso-oauth-sp/)で設定をします。

また、SSO OAuth SP編集画面の[テスト]をクリックすると、設定が正しいかどうかをテストできます。これにより、アイデンティティプロバイダから返されるレスポンスを確認し、それに応じて構成パラメーターの設定が可能です。  

<a href="https://diverta.gyazo.com/29042cc196b3e5fed6608be0c76425b5" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://t.gyazo.com/teams/diverta/29042cc196b3e5fed6608be0c76425b5.png" alt="Image from Gyazo" /></a>

:::tip
保存されていないデータはテストできません。テストを実行する前に、まず設定データを更新する必要があります。
:::

## 関連ドキュメント
- [OAuth SP](/ja/docs/management/sso-oauth-sp/)
- [SSOによるログインをフロントエンドで利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)
- [Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- [SPAでのSSO認証フローを実装する](/ja/docs/tutorials/implementing-sso-login-flow-in-spa/)
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [OAuthを使用したシングルサインオンはできますか](/ja/docs/faq/can-I-use-single-sign-on-using-oauth/)


---

# SSOによるログインをフロントエンドで利用する

> 元ページ: `tutorials/implementing-oauth-sp-based-sso-front` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/
> 概要: Kurocoでは、OAuth連携やSAML連携によるSSOの実装が可能です。対応するサービスの場合は簡単に設定ができます。また、いくつかの外部サービスをプリセットとして用意しており、本チュートリアルでは、GitHubでのログインを例としてOAuth認証によるSSOを実装します。

## 概要
KurocoはOAuth連携やSAML連携機能を持っており、それらに対応するサービスとのSSO(Single Sign-On)の実装が可能です。
いくつかの外部サービスについてはプリセットとして設定をご用意しておりますので、より簡単に設定できます。

本チュートリアルでは、SSOログインをフロントエンドで利用するため、grant_tokenとアクセストークンの生成方法について説明します。  
SSOはGitHubとのOAuth認証を例として説明しますが、IDaaS SP、SAML SPについてもトークンの生成手順はここで説明するOAuthと基本的には同じになります。

### 学べること
以下の手順でOauth SPによるSSOの実装を学びます。

- [概要](#概要)
  - [学べること](#学べること)
- [Kurocoの設定](#kurocoの設定)
  - [APIを作成する](#apiを作成する)
  - [OAuth SP設定を追加する](#oauth-sp設定を追加する)
- [フロントエンドでの実装](#フロントエンドでの実装)
- [利用方法](#利用方法)
- [関連ドキュメント](#関連ドキュメント)

## Kurocoの設定

### APIを作成する

SSOログインを実装する際に、Kuroco側に動的トークンによってログイン認証可能なAPIを作成する必要があります。Cookie認証や静的トークンではSSOは実装できませんのでご注意ください。

なお、Kurocoでは複数のAPIを作成出来ますが、ログインセッションはAPI毎に異なります。SSOでログインした場合も、ここで作成するAPIに対してのみログイン状態となり、他のAPIに対してはログインされません。

Kuroco管理画面の[API]をクリックします。
[追加]をクリックします。

[追加する]ダイアログで、以下のように入力し[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/16a7f53e042aefaf03779a2a9acc5945.png)

|項目   |設定内容  |
| :--- | :--- |
|タイトル|OAuth検証用API|
|版|1.0|
|説明|OAuth検証用API|
|並び順|0|

[セキュリティ]をクリックすると以下のダイアログが表示されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a43d407007dc45376bdec383d3bf2c1.png)

セキュリティ項目の[動的アクセストークン]を選択し、[保存する]をクリックします。

[新しいエンドポイントの追加]をクリックし、以下のように入力し[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/31b959cc1f31eef5fc68e7c55995bca6.png)

|項目   |設定内容  |備考  |
| :--- | :--- | :--- |
|パス|token||
|カテゴリー|認証||
|モデル|Login||
|オペレーション|token||
|use_refresh_token|チェックあり||
|access_token_lifespan|86400|単位[秒]で1日を指定します|
|refresh_token_lifespan|604800|単位[秒]で7日を指定します|

以上で、APIの設定が完了しました。

### OAuth SP設定を追加する
[外部システム連携] -> [ID連携] -> [OAuth SP]をクリックします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/73eb838e1113048df534ea34be2b9b34.png)
[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa509003cbad6d80b36a622488e8d68e.png)

OAuth SP編集画面が表示されますので、下記を入力して[追加する]をクリックします。  

|項目   |設定内容  |
| :--- | :--- |
|OAuth SPの名称|`GitHub login`|
|ターゲットドメイン|API|
|タイプ|GitHub|
|(API用) Grantトークン生成|`OAuth検証用API` にチェックを入れる|
|自動ユーザー登録|チェックを入れない|
|Emailを利用せずメンバー拡張項目にIDを格納してリンクする|チェックを入れない|
|リターンURL（成功）|（ログインに成功した直後に表示するページのURL）|
|リターンURL（エラー）|（ログインに失敗した直後に表示するページのURL）|


![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d6fa52a6d03ee7e84dba5347b1b8b8c.png)

ターゲットドメインが「管理画面」ではなく「API」である事に注意してください。これによりフロントエンド側でのログインに対してSSO機能が有効になります。

以降の手順は [GitHubを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)で説明しているものと同様になりますので、そちらをご参照ください。


## フロントエンドでの実装

以下のSSO OAuth SP編集画面に表示されている OAuth検証用API 1.0横のURLをコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0b97c3081e1e459638d8172e4571993.png)

フロントエンドの任意の場所にコピーした[ログインURL]へのリンクを設置します。

```html
<a href="(URL)"><span>GitHubでログイン</span></a>
```


## 利用方法
設置したURLへのリンクを確認します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3f3d7f2dbddab67298e12688c8acf033.png)

クリックするとGitHubのログイン画面が開きますので、GitHubのログインIDとパスワードを入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5c424804026e0ee1ef0125ee7d30dfd.png)

二要素認証を設定している場合は、認証コードの入力フォームが表示されますので、入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5b18ea9a29115be388faa18f086ce76.png)

ログインに成功すると、OAuth SP設定で設定した[リターンURL（成功）] のURLに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2af7e5644655efa4104d01446c3ac839.png)

:::info
SAML認証の場合は、`&grant_token=*********` というGET変数が付与された形で[リターンURL（成功）] のURLに遷移します。  
grant_tokenはアクセストークンを発行するための一時的なトークンです。こちらを使用してアクセストークンを取得するログイン処理を実装してください。
:::

URLからgrant_tokenをコピーし、SwaggerUIに遷移して上記で作成したエンドポイント`/rcms-api/X/token` の[Try it out]をクリックします。  
[Request body]書かれているJSONの `grant_token` キーの値部分にコピーした文字列をペーストします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/efceebe56ad4a4b7565d84c7808b48ef.png)

リクエストを送信すると、レスポンスにアクセストークンが含まれていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/83c104d501de096db90b3d7914720b78.png)

このアクセストークンをリクエストヘッダーに付与してリクエストを送ることで、OAuth検証用APIに追加されたエンドポイントをフロントから利用可能です。


## 関連ドキュメント
- [GitHubを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)
- [Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- [Google Workspaceを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/)
- [GMOトラスト・ログインを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gmo-trust-login-to-implement-saml-based-sso/)
- [Auth0を利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/)
- [IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)
