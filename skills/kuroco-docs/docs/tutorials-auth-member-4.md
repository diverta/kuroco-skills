# Kurocoドキュメント: チュートリアル / 認証・会員（4/4）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- KurocoとNuxt.jsで、新規会員登録画面を構築する（`setting-up-registration-form-nuxt2`）
- アカウント登録する（`signup`）
- Auth0を利用してSAML認証によるSSOを実装する（`using-auth0-to-implement-saml-based-sso`）
- カスタムメンバーフィルターを利用する（`using-custom-member-filters`）
- GMOトラスト・ログインを利用してSAML認証によるSSOを実装する（`using-gmo-trust-login-to-implement-saml-based-sso`）
- Google Workspaceを利用してSAML認証によるSSOを実装する（`using-gsuite-to-implement-saml-based-sso`）
- IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する（`using-idaas-to-implement-azure-ad-b2c-sso`）
- reCAPTCHAを利用したパスワードリマインダーを作成する（`using-recaptcha-for-password-reminders`）


---

# KurocoとNuxt.jsで、新規会員登録画面を構築する

> 元ページ: `tutorials/setting-up-registration-form-nuxt2` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-registration-form-nuxt2/
> 概要: Kurocoを利用したNuxt.jsプロジェクトで、新規会員登録画面の作成方法を紹介します。

Kurocoを利用したNuxt.jsプロジェクトで、新規会員登録画面の作成方法を紹介します。

## 前提条件
### Nuxt.jsプロジェクトの作成について
このページは、KurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。  
まだNuxt.jsプロジェクトを構築していない場合、[チュートリアル ->KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)を参照し、構築をお願いします。

### APIセキュリティについて
Kurocoでは、APIのセキュリティ方法がいくつか用意されています。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5d2188e3c2ea2c2b34b726e9fab91406.png)
新規会員登録は、APIのセキュリティ設定が「動的アクセストークン」または「Cookie」のみで動作します。そのため、APIセキュリティは「動的アクセストークン」もしくは「Cookie」にしてください。

:::info
セキュリティの種類については、[管理画面マニュアル -> API Security](/ja/docs/management/api-security/)を参照してください。
:::

:::info
セキュリティの種類の詳細な確認方法は、[Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)をご確認ください。
:::

### 推奨ブラウザについて
本チュートリアルは、動作確認のためGoogle Chromeの開発者ツールを利用しています。
そのため、ブラウザはGoogle Chromeを推奨いたします。

## ダミーの新規会員登録フォーム実装

それでは新規会員登録フォームを実装していきます。  
まずはAPIとの連携は省いた状態で、ダミーでの新規会員登録連携処理を実装します。

### 登録フォームの作成

新規会員登録画面用フォームを作成します。

`pages/login/signup/index.vue` ファイルを新規作成し、下記コードを記載してください。
```markup [pages/login/signup/index.vue]
<template>
    <div>
        <div v-if="!signupDone">
            <form @submit.prevent="signup">
                <div>
                    <label>prop1</label>
                    <input v-model="user.prop1" name="prop1" type="" placeholder="prop1">
                </div>
                <div>
                    <label>prop2</label>
                    <input v-model="user.prop2" name="prop2" type="" placeholder="prop2">
                </div>

                <div>
                    <button type="submit">
                        サインアップ
                    </button>
                </div>
            </form>
        </div>
        <div v-if="signupDone">
            新規登録が完了しました。
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            signupDone: false,

            user: {}
        }
    },
    methods: {
        signup () {
            console.log(JSON.stringify(this.user, null, '\t'))
            this.signupDone = true
        }
    }
}
</script>

<style scoped>
form > div {
    margin: 8px;
    display: flex;
    flex-direction: row;
}
form > div > * {
    display: flex;
    flex-direction: row;
    flex-basis: 100px;
}
form > div > *:nth-child(1) {
    flex: 0 0 100px;
    padding-right: 8px;
}
form > div > *:nth-child(2) {
    min-width: 0;
    flex: 1 100 auto;
}
</style>

```

ファイル保存後`npm run dev`を実行し、`http://localhost:3000/login/signup/`にアクセスします。  
簡単な新規会員登録フォームが表示されるので、Chromeの開発者ツール:コンソールを開いた状態で、下記入力し[サインアップ]をクリックします。

- prop1：text1
- prop2：text2

すると、入力したprop1とprop2がログとしてコンソールに表示されます。
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3d69303c65c87b979d45180f862cb0b2.gif)
このログに出力する値を新規会員登録用APIに実際にリクエストすることになります。

### 登録処理の実装

ひとまずAPI連携部分は仮の実装とし、下記を実装するようにします。

- 1秒間のリクエストをする、見せかけのダミー処理を追加作成
- リクエストに成功した場合、画面上で「新規登録が完了しました。」と表示

`pages/login/signup/index.vue`を修正します。

```diff [pages/login/signup/index.vue]
diff --git pages/login/signup/index.vue pages/login/signup/index.vue
index 2c93b73..c9aca24 100644
--- pages/login/signup/index.vue
+++ pages/login/signup/index.vue
@@ -1,64 +1,83 @@
 <template>
     <div>
         <div v-if="!signupDone">
             <form @submit.prevent="signup">
+                <p v-if="error" :style="{ color: 'red' }">
+                    {{ error }}
+                </p>
+
                 <div>
                     <label>prop1</label>
                     <input v-model="user.prop1" name="prop1" type="" placeholder="prop1">
                 </div>
                 <div>
                     <label>prop2</label>
                     <input v-model="user.prop2" name="prop2" type="" placeholder="prop2">
                 </div>
 
                 <div>
                     <button type="submit">
                         サインアップ
                     </button>
                 </div>
             </form>
         </div>
         <div v-if="signupDone">
             新規登録が完了しました。
         </div>
     </div>
 </template>
 
 <script>
 export default {
     data () {
         return {
             signupDone: false,
 
-            user: {}
+            user: {},
+            error: null
         }
     },
     methods: {
-        signup () {
-            console.log(JSON.stringify(this.user, null, '\t'))
-            this.signupDone = true
+        async signup () {
+            // ダミーリクエスト(1秒待機の後成功/失敗する)
+            const shouldSuccess = true
+            const request = new Promise((resolve, reject) =>
+                setTimeout(
+                    () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
+                    1000
+                )
+            )
+
+            try {
+                await request
+                this.signupDone = true
+            } catch (e) {
+                console.error(e)
+                this.error = 'エラーが発生しました。'
+            }
         }
     }
 }
 </script>
 
 <style scoped>
 form > div {
     margin: 8px;
     display: flex;
     flex-direction: row;
 }
 form > div > * {
     display: flex;
     flex-direction: row;
     flex-basis: 100px;
 }
 form > div > *:nth-child(1) {
     flex: 0 0 100px;
     padding-right: 8px;
 }
 form > div > *:nth-child(2) {
     min-width: 0;
     flex: 1 100 auto;
 }
 </style>

```

ブラウザでサインアップすると、1秒の待機の後「新規会員登録が完了しました」と表示されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/46606773e6f1aac2d1f4eaa7a855c35c.gif)
### エラー処理の実装 

次に、登録が失敗した場合の動作を確認します。  

`pages/login/signup/index.vue` ファイルの`shouldSuccess = true`を `shouldSuccess = false`へ変更します。

```diff [pages/login/signup/index.vue]
diff --git pages/login/signup/index.vue pages/login/signup/index.vue
- const shouldSuccess = true
+ const shouldSuccess = false
```

ブラウザでサインアップすると、「エラーが発生しました」と表示されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/7350de2f671dfe2f6e0105bd4be337e5.gif)
確認後は、`shouldSuccess = true`へ戻してください。

以上でダミーのフォームが完成です。

## 新規会員登録用エンドポイント作成と確認

次に新規会員登録をするためのAPIエンドポイントを作成します。

### エンドポイントの作成

Kurocoの管理画面のエンドポイント一覧より[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9901c98e07d385241f627da79bd4bc24.png)

下記エンドポイントを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/286ac1bc9d129cd08339d93f696089a9.png)

|設定項目|設定||
| :--- | :--- | :--- |
|パス| |member/regist|
||有効/無効|有効|
|モデル|カテゴリー|メンバー|
||モデル|Member：v1|
||オペレーション |insert|
|APIリクエスト制限| |None|
|基本設定|default_group_id|適用するメンバーグループのIDを入力してください。<br/>グループIDは[グループ](/ja/docs/management/group/)より確認できます。|
||login_ok_flg|チェックを入れる|

### 新規会員登録用エンドポイントのスキーマ確認
作成したエンドポイントのスキーマを確認します。

エンドポイント一覧画面より、「Swagger UI」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fe6311bdeb0f8f28b299b22abdce2d4a.png)
SwaggerUI画面から、先ほど作成したエンドポイントをクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2ff35a77b605a5bcc1df16ee040115db.png)
「Request Body」の「Schema」を選択すると、このエンドポイントへ渡せるデータのスキーマが表示されます。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7c0a65c72f5f52d9b4e9070119b559f8.png)
フロントエンドから新規会員登録のデータをPOSTリクエストする際には、記載されているスキーマに沿って設定したい項目をリクエストのボディに適用してリクエストを送信します。

以上でエンドポイントの作成完了です。

## 新規会員登録フォーム実装
それでは新規会員登録フォームを作成します。

今回は例として、下記項目をリクエスト送信対象にします。

- 姓：name1
- 名：name2
- メールアドレス：email
- ログインパスワード：login_pwd

### ファイルの修正

先ほど作成した、新規会員登録フォーム(`/pages/login/signup/index.vue`)を修正します。
```diff [/pages/login/signup/index.vue]
diff --git a/pages/login/signup/index.vue b/pages/login/signup/index.vue
index c9aca24..f2bee20 100644
--- a/pages/login/signup/index.vue
+++ b/pages/login/signup/index.vue
@@ -7,12 +7,20 @@
                 </p>
 
                 <div>
-                    <label>prop1</label>
-                    <input v-model="user.prop1" name="prop1" type="" placeholder="prop1">
+                    <label>name1</label>
+                    <input v-model="user.name1" name="name1" type="text" placeholder="name1">
                 </div>
                 <div>
-                    <label>prop2</label>
-                    <input v-model="user.prop2" name="prop2" type="" placeholder="prop2">
+                    <label>name2</label>
+                    <input v-model="user.name2" name="name2" type="text" placeholder="name2">
+                </div>
+                <div>
+                    <label>email</label>
+                    <input v-model="user.email" name="email" type="email" placeholder="email">
+                </div>
+                <div>
+                    <label>login_pwd</label>
+                    <input v-model="user.login_pwd" name="login_pwd" type="password" placeholder="login_pwd">
                 </div>
 
                 <div>

```

フィールドが修正されているのを確認します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3ec4d62ff6dca4139eddbc386020000d.png)
### APIへのリクエスト/ハンドリング実装

次に、APIへのリクエストを実装します。

ここからは、APIのセキュリティの設定によって対応する内容が異なります。
ご自身のセキュリティ設定をご確認いただき、下記より該当するセキュリティ内容に沿って進んでください。

- [セキュリティ設定がCookieの場合](#セキュリティ設定がcookieの場合)
- [セキュリティ設定が動的アクセストークンの場合](#セキュリティ設定が動的アクセストークンの場合)

### セキュリティ設定がCookieの場合

下記のように新規会員登録フォームを修正してください。
```diff
diff --git a/pages/login/signup/index.vue b/pages/login/signup/index.vue
index f2bee20..da12179 100644
--- a/pages/login/signup/index.vue
+++ b/pages/login/signup/index.vue
@@ -48,17 +48,13 @@ export default {
     },
     methods: {
         async signup () {
-            // ダミーリクエスト(1秒待機の後成功/失敗する)
-            const shouldSuccess = true
-            const request = new Promise((resolve, reject) =>
-                setTimeout(
-                    () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
-                    1000
+            try {
+                // 新規会員登録のリクエスト
+                await this.$axios.$post(
+                    '/rcms-api/1/member/regist',
+                    { ...this.user } // フォームの内容をリクエストボディとして適用
                 )
-            )
 
-            try {
-                await request
                 this.signupDone = true
             } catch (e) {
                 console.error(e)

```

:::caution
「/rcms-api/1/member/regist」の「1」には、ご自身のAPIのidを記入してください。  
APIのidは、エンドポイント一覧画面より確認できます。
:::
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/41cc59cb8c013dc475439ef26dc95097.png)
実際に新規会員登録をします。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/097c072cea861d7156ccb14cedd7463b.gif)
会員が登録されているか確認します。  
管理画面から[メンバー管理] -> [メンバー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/702976f9920e36fdf69df964827b2cfa.png)

メンバー一覧画面を開き、実際に会員が登録されているかを確認してください。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57244f40bcb956f41e66a006433e2d2d.png)

### セキュリティ設定が動的アクセストークンの場合

動的アクセストークンにてセキュアなエンドポイントへアクセスするには、トークン値をリクエストヘッダに送信する必要があります。  
今回のようなケース(AnonymousUserによるリクエスト)においても同様です。

従って、新規会員登録用エンドポイントへのリクエストには、事前に取得したAnonymousTokenをカスタムヘッダに適用する必要があります。

下記のように新規会員登録フォームを修正してください。

```diff
diff --git a/pages/login/signup/index.vue b/pages/login/signup/index.vue
index f2bee20..68670bc 100644
--- a/pages/login/signup/index.vue
+++ b/pages/login/signup/index.vue
@@ -48,17 +48,28 @@ export default {
     },
     methods: {
         async signup () {
-            // ダミーリクエスト(1秒待機の後成功/失敗する)
-            const shouldSuccess = true
-            const request = new Promise((resolve, reject) =>
-                setTimeout(
-                    () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
-                    1000
+            try {
+                // AnonymousTokenの取得
+                const tokenRes = await this.$axios.$post(
+                    '/rcms-api/1/token',
+                    {} // AnonymousUserでのトークン値取得要求のため、リクエストボディは空のオブジェクトを指定
+                )
+                const anonymousToken = tokenRes.access_token.value
+
+                // AnonymousTokenを適用したカスタムヘッダを作成
+                const customHeaderConfig = {
+                    headers: {
+                        'X-RCMS-API-ACCESS-TOKEN': anonymousToken
+                    }
+                }
+
+                // 新規会員登録のリクエスト
+                await this.$axios.$post(
+                    '/rcms-api/1/member/regist',
+                    { ...this.user }, // フォームの内容をリクエストボディとして適用
+                    customHeaderConfig
                 )
-            )
 
-            try {
-                await request
                 this.signupDone = true
             } catch (e) {
                 console.error(e)

```

:::caution
「/rcms-api/1/member/regist」の「1」には、ご自身のAPIのidを記入してください。  
APIのidは、エンドポイント一覧画面より確認できます。
:::
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/41cc59cb8c013dc475439ef26dc95097.png)

実際に新規会員登録をします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/962300ed769a9f94d8beb702c66e97fc.gif)
会員が登録されているか確認します。  
管理画面から[メンバー管理] -> [メンバー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/702976f9920e36fdf69df964827b2cfa.png)

管理画面からメンバー一覧画面を開き、実際に会員が登録されているかを確認してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/57244f40bcb956f41e66a006433e2d2d.png)

以上でKurocoを利用したNuxt.jsプロジェクトで、新規会員登録画面を構築する方法の紹介を終わります。

今回は基本的な説明のため、簡単に新規会員登録画面を作成して最低限の実装を実現しました。 
実際に利用する際には、フォームのバリデーション処理やメール認証の実装をする必要性も考えられますが、基本的な会員登録の流れの理解としてご利用いただければ幸いです。

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [新規メンバー登録条件](/ja/docs/management/registration-conditions/)
- [KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login-nuxt2/)
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)


---

# アカウント登録する

> 元ページ: `tutorials/signup` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/signup/
> 概要: Kurocoを利用するためにまずはアカウント登録が必要です。本チュートリアルではKurocoのアカウント登録方法を説明します。

Kurocoを利用するためにまずはアカウント登録が必要です。  
本チュートリアルではKurocoのアカウント登録方法を説明します。

## アカウント登録方法
[Kuroco Free Trial画面](https://kuroco.app/ja/free_trial/)に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ea14cd111496bdd1721cafca0471c93.jpg)
必要項目に記入し、「登録する」をクリックします。

|項目 |説明 |
| :--- | :--- |
|リージョン|リージョンを選択します。|
|サイトキー|サイト独自のキーを入力します。サイトキーはエンドポイントURLの一部になります。|
|会社名|会社名を入力します。個人利用の場合は「個人」と入力してください。|
|姓|姓を入力します。|
|名|名を入力します。|
|メールアドレス|メールアドレスを入力します。|

パスワードの入力欄はありません。管理画面の初期パスワードはKurocoがサーバー側で生成し、登録完了のメールに記載して通知します。

「送信する」をクリックすると、登録したメールアドレスに登録完了のメールが届きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/826fd3623e1cddac5c65b9080dcda189.png)

メール内に記載されている管理画面URLをクリックし、同じくメールに記載されている初期パスワードでログインを行うとKuroco管理画面が表示されます。  
初回ログイン時にはパスワードの変更が求められます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/de5a9ba789ab79fb1152b58f4517d1bd.png)
以上でアカウント登録完了です。

## 関連ドキュメント
- [ログインする](/ja/docs/tutorials/login/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [Kurocoを利用したプロジェクトの進行イメージ](/ja/docs/tutorials/starting-a-project-on-kuroco/)


---

# Auth0を利用してSAML認証によるSSOを実装する

> 元ページ: `tutorials/using-auth0-to-implement-saml-based-sso` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/
> 概要: Auth0を利用してSSOを実装する方法を説明します。Auth0をIdP, KurocoをSPとしたSAML認証によるシングルサインオンになります。

Auth0を利用して、SAML認証によるSSOを実装する手順を説明します。    
Auth0をIdP, KurocoをSPとしたSAML認証によるシングルサインオンになります。

## 前提条件
このチュートリアルはAuth0のアカウントを所持していることが前提となります。

## Auth0でアプリの作成
### Auth0にログインする
Auth0に[ログイン](https://auth0.com/api/auth/login?redirectTo=dashboard)し、[Applications]メニューから、画面右上の[Create Application]ボタンをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a83837a2a4261ec18313ad7a85189c6.png)

### アプリを作成する
任意の名前を入力し、「Regular Web Applications」を選択して[Create]をクリックします。    

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a3589a0947c068bdebf62e68c50d0026.png)

### 設定情報を取得する
アプリの作成ができたら[Settingsタブ]に遷移します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/63769bb3d4785f5a39f04db21456bc18.png)

画面下までスクロールし、[Advanced Ssettings]を開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d7281749e3201a3e8c3ff6d2f5a0ba1a.png)

#### 証明書をダウンロードする
[Cartificates]タブを開き、[Download Certificate]をクリックして証明書をダウンロードします。  
ファイル形式はPEMを選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14292299e2c403c652f350769fb6db0d.png)

#### SAML Protocol URLを取得する

[Endpoints]タブを開き、SAML項目のSAML Protocol URLをコピーします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c6e6f364e5d260c6235c6f7b02997f9.png)

## Kurocoの設定
### SAML SPを追加する
Kuroco管理画面の左メニューから[外部システム連携] -> [ID連携] -> [SAML SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/176a78956266a9e56c2b0304d681af33.png)

[追加]ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2447f5b4ad701d6a91126ab47d5c0675.png)

SAML SP編集画面の各項目を下記の通り設定します。  
証明書の入力欄は[設定ファイルがありませんか？こちらをクリックしてください。]をクリックして表示してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eb1c7a355b88ec74554b6b702f01e34c.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/68cef493b52fe27859f1500b95234f25.png)

#### 項目説明

|項目   |説明  |
| :--- | :--- |
|ログインSAML SP Name|任意の名称を入力します。|
|ターゲットドメイン|[管理画面]を選択します。|
|エンティティID|任意の文字列を入力します。|
|証明書|[ファイルを選択]ボタンをクリックし、Auth0から取得した証明書(.pemファイル)をアップロードします。|
|IDP URL|Auth0から取得したSAML Protocol URLを入力します。|
|IDPエンティティID|Auth0から取得したSAML Protocol URLを入力します。IDP URLと同じになります。|
|有効期限|任意の日時を設定します。|
|ログインIDを使用|チェックをOFFにします。|
|自動ユーザー登録|チェックをONにし、任意のグループを選択します。|
|IDP起点フローを許可|チェックをONにします。|
|Binding Method|「POST」を選択します。|

### ログインSAML SP ACS URIを確認する
先ほど追加した[ログインSAML SP Name]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/89bd49a4e12449f129185f39b0e5c9ca.png)

[ログインSAML SP ACS URI]が表示されているのでコピーします。  

また、証明書ファイルが無くなっているので再度アップロードして更新します。   

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2762cf8f3f8ba382c6e2462038640dad.png)

## Auth0でSAML2 WEB APPを有効にする
Auth0のアプリ設定に戻り、[Addons]タブの[SAML2 WEB APP]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/184394f6e3c0ae6c5a6f9f2253d99fb0.png)

Addonの設定が開くので、Application Callback URLにKuroco管理画面で確認したログインSAML SP ACS URIを入力し、Settingsに以下のJSONを入力します。  

```json
{
	"mappings": {
		"name": "name1",
		"email": "email"
	}
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57641698ef20b437a4e245ec8abaaeee.png)

設定ができたら画面下までスクロールし、[Enable]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d794be5097954f2cd8e6a52ef27937ca.png)

[SAML2 WEB APP]が有効になったらAuth0の設定は完了です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/259b44271925495098a97cb89dd71fac.png)

## 動作の確認をする
設定が完了すると、Kurocoのログイン画面にSSOのリンクが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f006a32e24ada6a072ac791188cde147.png)

リンクをクリックすると、Auth0のログインページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4e371b0916e53c04fe776c5d4efe6d1.png)

こちらでSAMLログインができるようになります。

## 関連ドキュメント
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [Google Workspaceを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/)
- [GMOトラスト・ログインを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gmo-trust-login-to-implement-saml-based-sso/)
- [SPAでのSSO認証フローを実装する](/ja/docs/tutorials/implementing-sso-login-flow-in-spa/)
- [SAML認証を使用したシングルサインオンを利用できますか](/ja/docs/faq/can-I-use-single-sign-on-using-saml/)


---

# カスタムメンバーフィルターを利用する

> 元ページ: `tutorials/using-custom-member-filters` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-custom-member-filters/
> 概要: カスタムメンバーフィルターを登録することで、メンバーの検索の他、ページの権限設定や、マガジンの送付先など、様々な機能で任意のメンバーに向けた動作を実現できます。

カスタムメンバーフィルターを登録することで、メンバーの検索の他、ページの権限設定や、マガジンの送付先など、様々な機能で任意のメンバーに向けた動作を実現できます。

## カスタムメンバーフィルターを登録する方法
### 1. 「カスタムメンバーフィルター」ページへアクセスする 
検索条件は「カスタムメンバーフィルター」ページにて設定できますので、まずは「カスタムメンバーフィルター」に移動します。 

[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd5c2d764fb3064628d8322631176742.png)
[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c81fb5077f07469a1df8d992d5637fa.png)
### 2. カスタムメンバーフィルターの設定を登録する  
ここでは例として下記の内容を入力・設定します。  
各項目の内容は[カスタムメンバーフィルター一覧](/ja/docs/management/custom-member-filter/)の説明を参照してください。

- タイトル：新規＋特定地域メンバー
- アクセス制限：全体
- モジュール検索条件：AND
- 権限設定への利用：有効にするをチェックする
- メモ：空欄

![Image from Gyazo](https://t.gyazo.com/teams/diverta/280d9d72e85d59c86e0fc6ef4566917f.png)
### 3. カスタムメンバーフィルターを登録する 
検索条件は「メンバー」「フォーム」「EC」「カスタム処理」をそれぞれ設定できます。

ここでは例として30日以内にメンバー登録をし、かつ、住所が東京もしくは海外となっているメンバーを検索してみます。

#### 3-1. 30日以内に登録したメンバーの検索を設定する

[新規登録日時][相対で日付指定][>=]を選択し、入力欄に`today -30 day`を入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/205e0a6a94bf0fccc6f5e396c69ee0eb.png)
#### 3-2. グループ化した条件を追加する

追加するボタン横の▼をクリックし[グループ化した条件を追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b9a62e80fbea92af510e1bacf64537db.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/37ab246bc967333d7814aa636c878239.png)
#### 3-3. 住所が東京、住所が海外の条件を設定する

[都道府県][どれかを含む][東京都]を設定し、さらに[追加する]をクリックし、[都道府県][どれかを含む][海外]を設定する。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4adb16c545a8470bf5a4391ddedcf65a.png)
#### 3-4. 検索の条件を設定する

都道府県の横の条件を[OR]に、新規登録日時の横の条件を[AND]に設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/356ff81b489ce0def88ed0ae216b92cf.png)
### 4. 対象者を確認する

[結果を閲覧する]をクリックし、想定通りのメンバーが表示されていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/df542d538ec1e2ee938281d8d960146b.png)
確認後、[更新する]ボタンをクリックして設定完了です。

## 相対で日付指定の設定方法
上記の例では相対の日付指定で`today -30 day`を記述しましたが、他にも様々な設定が可能です。
記述はPHPの日付と時刻の書式に基づいています。

### 記述の例

|項目   |説明  |
| :--- | :--- |
|前日の12時|"yesterday noon", "yesterday 12:00"|
|翌月末|"last day of next month"|
|指定の日付|"2021-03-24"|
|2021年1月の最初の土曜日|"first sat of January 2021"|
|相対的な時間の指定|"+5 weeks", "+12 day", "-6 month"　等|

## 登録した検索条件が利用できる機能
今回登録した検索条件は、下記の機能にて利用可能です。

### コンテンツ編集画面、詳細設定のAPIリクエスト制限
[コンテンツ編集](/ja/docs/management/content-structure-topics/#content-editor)画面の「詳細設定」内「APIリクエスト制限」で利用可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/518dbf2edf623c2afeb5d51e1de70eca.png)
### 配信のあて先
[チャネル] -> [一括配信]より、[対象配信の基本設定](/ja/docs/management/notification-basic-settings/#existing-notification)「デフォルトのあて先」で利用可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73a78ee38609acf82afdcc3423903f8e.png)
### フォーム基本設定の閲覧制限
[チャネル] -> [WEB] -> [フォーム]より、[対象フォームの基本設定](/ja/docs/management/inquiry-basic-settings)「APIリクエスト制限」で利用可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7058e3371dff85ff6507d36d4b5ef20.jpg)
### エンドポイントの設定の認証
[API] -> [エンドポイントの設定](/ja/docs/management/api-list/)の[APIリクエスト制限]で「MemberCustomSearchAuth」を選択すると利用可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ca2e421be568aabda4ca0cc819acc66.jpg)

### メンバー一覧でのメンバー検索
[メンバー管理] -> [[メンバー](/ja/docs/management/member)]の「詳細検索」で利用可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/997889c11160a62c02d1a02a344df8b3.png)

## 関連ドキュメント
- [カスタムメンバーフィルター](/ja/docs/management/custom-member-filter/)
- [カスタムメンバーフィルターカテゴリ](/ja/docs/management/custom-member-filter-category/)
- [メンバー](/ja/docs/management/member/)
- [カスタムメンバーフィルターで利用できるカスタム処理の変数](/ja/docs/reference/variables-for-custom-function-available-in-custom-member-filters/)


---

# GMOトラスト・ログインを利用してSAML認証によるSSOを実装する

> 元ページ: `tutorials/using-gmo-trust-login-to-implement-saml-based-sso` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-gmo-trust-login-to-implement-saml-based-sso/
> 概要: GMOトラスト・ログインを利用してSSOを実装する方法を説明します。GMOトラスト・ログインをIdP, KurocoをSPとしたSAML認証によるシングルサインオンになります。

GMOトラスト・ログインを利用して、SAML認証によるSSOを実装する手順を説明します。    
GMOトラスト・ログインをIdP, KurocoをSPとしたSAML認証によるシングルサインオンになります。

## 前提条件
このチュートリアルはGMOトラスト・ログインのアカウントを所持していることが前提となります。

:::info
GMOトラスト・ログインのドキュメントも参考にしてください。
- [Kuroco のSAML認証の設定方法](https://support.trustlogin.com/hc/ja/articles/27874415834009)
- [Kuroco のSAML JIT設定方法](https://support.trustlogin.com/hc/ja/articles/27914814971673)
:::

## GMOトラスト・ログインでアプリ登録
### トラスト・ログインにログインする
トラスト・ログインに[ログイン](https://portal.trustlogin.com/users/sign_in?)し、[管理ページ] -> [アプリ]メニューを開き、画面右上の[アプリ登録]ボタンをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/516f995f56e1161944d1129a9f9b1d49.png)

### 企業アプリで「Kuroco (SAML)」を登録する
「企業アプリ登録」画面で検索し、「Kuroco (SAML)」を選択します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/60b467785ae500d7761aebf0ddf6774e.png)

### 証明書をダウンロードする
「IDプロバイダーの情報」 の「IDプロバイダーURL」「発行者・エンティティID」の値を控え、[証明書を取得]ボタンから証明書をダウンロードします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e69a2d5083ea8c30f98c8598116490f8.png)

### ダウンロードした証明書の拡張子を変更する
ダウンロードした証明書の拡張子を「.cer」に変換しておきます。  

ここで、Kuroco 側の設定に移ります。  
:::caution
[登録]ボタンは押さず、別ウィンドウでKuroco の管理画面を開いてください。
:::

## Kurocoの設定
### 外部システム連携の設定
Kuroco管理画面の左メニューから[外部システム連携] -> [ID連携] -> [SAML SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/176a78956266a9e56c2b0304d681af33.png)

[追加]ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2447f5b4ad701d6a91126ab47d5c0675.png)

### SAML SP編集
SAML SP編集画面の各項目を下記の通り設定し、最後に[追加する]ボタンで保存します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7c32376956572c66fa86e593ac4de23c.jpg)

#### 項目説明
|項目   |説明  |
| :--- | :--- |
|ログインSAML SP Name|任意の名称を入力します。|
|ターゲットドメイン|[管理画面]を選択します。|
|エンティティID|任意の文字列を入力します。|
|IDP用XML設定ファイル|[設定ファイルがありませんか？こちらをクリックしてください。]をクリックすると以下の「証明書」などの項目が表示されます。|
|証明書|[ファイルを選択]ボタンをクリックし、トラスト・ログインから取得した「証明書」（拡張子を .cer に変更したファイル    ）をアップロードします。|
|IDP URL|トラスト・ログインから取得した「IDプロバイダーURL」を入力します。|
|IDPエンティティID|トラスト・ログインから取得した「発行者・エンティティID」を入力します。|
|有効期限|任意の日時を設定します。|
|ログインIDを使用|チェックをOFFにします。|
|自動ユーザー登録|チェックをOFFにします。|
|IDP起点フローを許可|チェックをONにします。|
|Binding Method|「POST」を選択します。|

:::tip
SAML JIT(Kurocoにユーザー登録がされていない場合に自動でユーザー登録をする)の場合は[自動ユーザー登録]のチェックを有効にします。
:::

### SAML SP設定
先ほど追加した[ログインSAML SP Name]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8490f376413d0d3424904b77d820b817.png)

### 証明書の再アップロード
再度、「証明書」にトラスト・ログインから取得した「証明書」をアップロードし、[メタデータのダウンロード]ボタンをクリックしてメタデータを取得します。  
最後に[更新する]ボタンで更新します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0de0f705908d5972aa561935a400e67.jpg)

再び、トラスト・ログインの管理ページに戻ります。  

## GMOトラスト・ログインでメタデータを登録
「サービスプロバイダーの設定」の「メタデータ」で、「メタデータを選択」をクリックし、Kuroco から取得した「メタデータ」をアップロードします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd56bd1b834ff4d831faa9d5133669de.jpg)

[登録]ボタンで保存します。  

最後に、アプリが利用できるユーザーを追加したら設定は完了です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/af5e2fcf4b7beadc3b7a50ca3c9b1c75.jpg)

## 動作の確認をする
設定が完了すると、Kurocoのログイン画面にSSOのリンクが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5b781094dbf809390b937de66f2c5c6.png)

リンクをクリックすると、GMOトラスト・ログインのログインページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fb362e473797e82fe8cfa5bcc3aad961.png)

こちらでSAMLログインができるようになります。

## 関連ドキュメント
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [Auth0を利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/)
- [Google Workspaceを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/)
- [SAML認証を使用したシングルサインオンを利用できますか](/ja/docs/faq/can-I-use-single-sign-on-using-saml/)


---

# Google Workspaceを利用してSAML認証によるSSOを実装する

> 元ページ: `tutorials/using-gsuite-to-implement-saml-based-sso` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/

Google Workspaceを利用してSSOを実装する方法を説明します。  
Google WorkspaceをIdP, KurocoをSPとしたSAML認証によるシングルサインオンになります。

## 前提条件
このチュートリアルはGoogle Workspaceのアカウントを所持していることが前提となります。

## Kurucoの管理画面でSP設定を追加
まずはKurocoの管理画面でSP設定をします。  

**1. SSO SAML SP設定の画面へ遷移する**  
[SSO SAML SP編集](/ja/docs/management/sso-saml-sp/)を参考にSAML SP編集画面へ遷移します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/517150757a6c63145d9682b3234d2bd4.png)
**2. SPの設定を追加する**  
SSO SAML SP編集画面で下記を入力し、[追加する]をクリックします。
- ログインSAML SP Name: お好きな名前
- エンティティID:半角英数字でお好きなID
- 有効:チェックを外す
- (API用) Grantトークン生成:チェックする
- 自動ユーザ登録：チェックする
- Allow IDP Initiated Flow:チェックする

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c1fbe8baf6bf4989d91ce7e5a2db68b6.png)
SSO SAML SP一覧画面に、作成したSP設定が追加されます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/892362fa51a2d07bc220b342048625cb.png)
**3. SPの設定を確認する**  
SSO SAML SP一覧画面より、先ほど追加したSP設定の「ログインSAML SP Name」をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6b8864ddd7e39fc90c632eb85c5445b2.png)
編集画面より「ログインSAML SP ACS URI」「エンティティID」を確認し、コピーしておきます。  
次のGoogle Workspaceの管理画面の設定で利用します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d02711d523ed777518d27be97a78eaf9.png)
## Google Workspaceの管理画面の設定
次に、[Google Workspaceの管理画面](https://admin.google.com/)からSAML連携を設定します。    

:::caution
以下の作業は必ずGoogle Workspaceの管理者の権限でログインをお願いします。
:::

:::caution
Googleの仕様によりキャプチャの内容が変わる可能性もございます。
:::

**1. Google Workspaceの管理画面からAppsの設定画面へ遷移する**  
管理画面より[アプリ]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/90b66ea97ea86e95da3269f110116c84.png)
**2. SAML appsの設定画面へ遷移する**  
アプリ一覧画面より、[SAML アプリ]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84ce9ddfe575a684a15fcfe3f6bdddf3.png)
**3. SAML appsを追加する**  
[アプリを追加]->[カスタム SAML アプリの追加]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a95d4fc7cde1a6c28d02d03cdfce9b06.png)
**4. カスタムアプリを作成する**  
下記２点を設定し、[続行]をクリックします。
- アプリ名
- アプリのアイコン
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/76dddd2934dc2183c30cdcfcad8d4c09.png)
**5. IdP情報をダウンロードする**  
[メタデータをダウンロード]をクリックし、IdPメタデータをダウンロードします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/107219819f8e2f6140d2133f17fe6f5a.png)
ダウンロードしたら[続行]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/310a03e842dd4d9e544e8aa693e2986c.png)
**6. サービス プロバイダの情報を入力する**  
下記内容を入力します。 

- ACSのURL: Kurocoの管理画面で確認した「ログインSAML SP ACS URI」   
- エンティティID: Kurocoの管理画面で確認した「エンティティID」  
- 開始URL: / など、ログイン後のページURL  
- 署名付き応答： チェックを入れる  
- 名前IDの形式: 「EMAIL」を選択する
- 名前ID: 「Basic Information > Primary Email」を選択する

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7b25f73d4889b86308675f183279941a.png)
入力したら[続行]をクリックします。

**7. マッピング情報を設定する**  
[マッピングを追加]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/56747b7f6a97156dc219ebaa79a5c142.png)
下記内容を設定します。  
- Basic Information / Last name：name1
- Basic Information / First name：name2

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5b4f335df4cf5238aa4692fd0319624e.png)
設定したら[完了]をクリックします。  

カスタムSAMLアプリが追加されました。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/96182f4a75fca266668b26e089133ae2.png?witdh=600)
**8. ユーザーアクセスをオンにする**  
初期設定ではユーザーアクセスが「オフ」になっているので、「オン」に変更します。  
[ユーザーアクセス]の下矢印をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a618d32005aad696b1b0d1c35655becc.png)

サービスのステータスで「オン」にチェックを入れ、[保存]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d452f6c83eb9007ca037c2fa3143af6c.png)
以上でGoogle Workspaceの設定が完了です。

## Kurucoの管理画面でSP設定にIdP情報を設定する 
Kuroco管理画面に移動し、[SSO SAML SP編集](/ja/docs/management/sso-saml-sp/)を参考にSAML SP編集画面へ遷移します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6b8864ddd7e39fc90c632eb85c5445b2.png)
[2-5. IdP情報をダウンロードする]でダウンロードしたIdP情報のXMLファイルをアップロードし、有効にチェックを入れます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/db00c38e86343a2e5f6e6cedd525766e.png)
設定完了後、[更新する]ボタンをクリックしたら設定は完了です。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c23b583df339349232fb78dc1f03a3a4.png)
## 利用方法 
作成したSAML SP画面を確認します。  
SSO SAML SP一覧画面より、先ほど追加したSP設定の「ログインSAML SP Name」をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/28ecf71b9d9da226c4fef71134084d86.png)
「ログインSAML SP ACS URI」が確認できます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/91c0fb64db5e5d6c2a34cef25a11bc6b.png)
アクセスすると、Google ログイン画面に遷移します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d4afc2bf385a0db7cbd8757b9d919080.png)
こちらでSAMLログインができるようになります。

## 関連ドキュメント
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [Auth0を利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/)
- [GMOトラスト・ログインを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gmo-trust-login-to-implement-saml-based-sso/)
- [SAML認証を使用したシングルサインオンを利用できますか](/ja/docs/faq/can-I-use-single-sign-on-using-saml/)


---

# IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する

> 元ページ: `tutorials/using-idaas-to-implement-azure-ad-b2c-sso` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/
> 概要: このチュートリアルでは、Microsoft Entra External ID（旧 Azure AD B2C）を使用したIDaaS SSOの実装方法について説明します。これは、Microsoft Entra IDをIdP、KurocoをSPとするOAuth認証を使用したSSOです。

このチュートリアルでは、Microsoft Entra External ID（旧 Azure AD B2C）を使用したIDaaS SSOの実装方法について説明します。
これは、Microsoft Entra IDをIdP、KurocoをSPとするOAuth認証を使用したSSOです。

:::info
このドキュメントは、IDaaS機能を使用するActive DirectoryユーザーのSSO実装について説明しています。
MicrosoftのOAuth機能を使用したOAuth SPログインについては、[Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)を参照してください。
:::

## 前提条件
このチュートリアルはMicrosoft Entra IDテナントアカウントを所持していることが前提となります。

## Kuruco管理画面でIDaaS設定を追加する
まずは、Kurocoの管理ページにIDaaS設定を追加します。

**1. IDaaS SP設定ページにアクセス**  
[IDaaS SP編集](/ja/docs/management/sso-idaas-sp/)を参考に、IDaaS SP編集ページにアクセスします。

**2. SP設定を追加**  
IDaaS SP編集ページに以下を入力し、「追加」ボタンをクリックします。  
この段階では有効のチェックを外してください。クライアントID、秘密鍵の入力不要で追加が可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/56c497fbee163e9bb66c846d42f9680a.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/84e5550b980966daa5c9d5a6dcce8334.png)

| 項目  | 説明 |
| :-- | :--- |
| ログインIDaaS SP名   | 任意の名前を入力します。 |
| ターゲットドメイン   | IDaaS SPのターゲットドメイン<br/>本チュートリアルでは管理画面に設定して進めます。 |
| タイプ  | AzureADB2C  |
|Emailを利用せずメンバー拡張項目にIDを格納してリンクする|有効にするのチェックを外す<br/>`emails`<br/>`0`|

追加したIDaaS SPを開き、[ログインURL]を控えます。  
後ほど、Microsoft Azure Portalで使用します。  
(URLの形式は `https://<管理画面URL>/direct/login/idaas_login/spid=<SP ID>` になります。)

## Microsoft Entra External IDの構成

次に、[Microsoft Azure Portal](https://portal.azure.com/)でMicrosoft Entra External IDアプリを登録します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4bd1a64e0d0bffa4c5e3fd21a1294468.png)

:::info
画面はMicrosoftの仕様によって変更される可能性があります。
:::

**1. Microsoft Entra External IDダッシュボードにアクセス**
Azure Portalのダッシュボードから Microsoft Entra External ID構成にアクセスします。
クイックアクセスに表示される場合は選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbaf68059cb6562b91a6ad188de39441.png)

ない場合は、検索を使用して[Azure AD B2C]（ポータル上では旧名称で表示される場合があります）を検索し、開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/95975fba6824d3d443c3cceb25fa324a.png)

**2. 新しいアプリを登録**  
[アプリの登録]をクリックし、[新規登録]をクリックします。これによりアプリ作成画面に移動します。これがMicrosoft Azure側のIdPアプリになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4c29ee6880938624f7b6f35bca0a3bf5.png)

アプリケーションの登録画面で、以下のように入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7525a188f278456efde8f3e0668ca741.png)

| 項目 | 説明  |
| :--- | :--- |
| 名前  | 任意の名前を入力してください。これはKurocoと同じである必要はありません。MicrosoftのIdPアプリの名前となります。 |
| サポートされているアカウントの種類 | このアプリケーションで有効にするアカウントの種類。アプリケーションを利用するユーザーを選択してください。 |
| リダイレクト URI - プラットフォーム | ドロップダウンから[Web]を選択します。  |
| リダイレクトURL - URL  | 前のステップで控えたKuroco管理画面IDaaS SP編集画面の[ログインURL]を入力します。 |
|アクセス許可|チェックボックスをオンにして、アプリケーションがopenIdの詳細にアクセスする権限を付与します。|

[登録]をクリックします。  

アプリが作成されると、以下のアプリケーションダッシュボードが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/abc82ccffc1685cee18ac5636a839c2b.png)

**3. アプリケーション (クライアント) IDをコピー**  
[アプリケーション (クライアント) ID]をコピーします。これはKurocoの IDaaS SP編集画面で使用します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/437a9160dd587b8170be8c2f69fad791.png)

**4. アクセストークンフローを有効にする**  
[認証]をクリックし、[アクセストークン]のチェックボックスをオンにして[保存]をクリックします。これにより、暗黙的なフローの使用が可能になります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/00e26cdd1422ffdb0bfe1d304f6ef930.png)

**5. クライアントシークレットを生成する**  
[証明書とシークレット]をクリックし、[新しいクライアントシークレット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/03347536aeb9ceebddf6c6bcfc574cfe.png)

サイドモーダルで、説明と、シークレットの有効期限を設定して[追加]をクリックします。  

:::caution
有効期限が切れた場合、SSOによるログインが機能しなくなります。  
新しいシークレットをMicrosoftで作成し、Kurocoに再設定してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c80ed0f6c2bb75ec81020b0a3bf38fa5.png)

シークレットの値をコピーします。画面を移動すると表示されませんので注意してください。この値はKuroco IDaaS SP編集管理画面で使用します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/46cc7e1b075f435e28c98f520f6bb2ac.png)

**6. ユーザー フローを作成する**  
Ad B2C構成ダッシュボードから、[ユーザー フロー]をクリックし、[ユーザー フローの作成]をクリックします。  
（ユーザー フローは、Microsoft Entra External IDがログインと登録をどのように処理するかを定義します。フローがすでに設定されている場合は、ユーザー フロー作成の手順をスキップして構いません。）  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a741acfb9282361a4281c3463ee5fb6.png)

:::tip
サイドメニューにユーザーフローが存在しない場合は、Microsoft Entra ID ディレクトリではなく Microsoft Entra External ID ディレクトリにいることを確認してください。External ID 機能を使用するには、既存の従業員ベースの Microsoft Entra ID テナントとは別の Microsoft Entra External ID テナントを作成します。
- [Microsoft Entra External ID:よく寄せられる質問 (FAQ)](https://learn.microsoft.com/ja-jp/azure/active-directory-b2c/faq?tabs=app-reg-ga#azure-portal---azure-ad-b2c-----------------------)
- [チュートリアル:Microsoft Entra External ID テナントの作成](https://learn.microsoft.com/ja-jp/azure/active-directory-b2c/tutorial-create-tenant)
:::

ユーザーフローの入り口を選択します。ここで新しいユーザー登録を許可するかどうかを構成できます。このサインアップ構成は、KurocoのIDaaS SP編集画面で見られるKuroco新規ユーザー登録とは異なります。  

本ドキュメントでは[サインアップとサインイン]を選択して進めます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/666a7dbf049d1542ee19d5c6e3a6c4dd.png)

[推奨]バージョンを選択し、[作成]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88a63ebcbeecc8a2555021a78a297a44.png)

ユーザーフロー構成画面で、以下の表に従ってフィールドを設定します。データを入力した後、[作成]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/657a7e962a3e5a44a506bb8541b4c582.png)  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fd64b03dc4f5f181e4d868ca71b27b0b.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9360edd2583ff111e6c0caa830d8b737.png)


| 項目  | 説明  |
| :--- | :--- |
| 名前 | ユーザーフローの識別子。これは一意であり、将来変更できません。 |
| IDプロバイダー | ユーザーがMicrosoft IDaaSにログインする方法を選択します。この例では、電子メール/パスワードに基づくログインを選択します。 |
| 多要素認証 | ユーザーがMicrosoft Entra IDでMFAをどのように構成するかを選択します。この例では、メールを選択します。これは、ユーザー登録のためのメールを検証するためのメールOTPベースのMFAです。 |
| ユーザー属性とトークン要求 | ユーザーから収集され、Kurocoに渡すデータ。追加のデータが構成されている場合、それはKurocoのIDaaS SP編集画面で設定する必要があります。このチュートリアルでは、名と姓をKurocoに渡すために使用されます。 |

[作成]をクリックし、ユーザーフローを作成します。
作成したユーザーフローは、ユーザーフローリストに表示されます。フローを編集するには、フローをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f57e08741684ead08bb5c6ab48314608.png)

（**注意:** Kurocoにメールを渡す必要がない場合は、このステップをスキップできます）  

[アプリケーション要求]をクリックし、[メールアドレス]のチェックボックスをオンにして保存します。  
これにより、設定で1つのメールアドレスのみを持つように設定されていても、ユーザーが複数のメールアドレスを持っていても、ユーザーのメールアドレスは同じ配列形式でKurocoに渡されるようになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/91dc43fd19155616862dea7c12959e13.png)

**7. 構成URLをコピーする**  
[概要]をクリックし、[ユーザーフローを実行します]をクリックしてから、リソースリンクを新しいタブで開きます。リンクの形式は次のようになります  
（`https://<AD名>.b2clogin.com/<ADドメイン>/v2.0/.well-known/openid-configuration?p=B2C_1_<ユーザーフロー名>`）。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f3b7afc34b9d2afff2e84e1aafe3134a.png)

JSONデータが表示されます。
[authorization_endpoint]、[token_endpoint]、および[jwks_uri]をコピーしてください。これらはKurocoのIDaaS SP編集画面で使用します。URLの形式を以下の表に示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7eed063516bf5bfc6a484d518017c9c.png)

| URL  | 形式 |
| :--- | :--- |
| authorization_endpoint | `https://<AD Name>.b2clogin.com/<AD Domain>/oauth2/v2.0/authorize?p=b2c_1_<User Flow Name>` |
| token_endpoint         | `https://<AD Name>.b2clogin.com/<AD Domain>/oauth2/v2.0/token?p=b2c_1_<User Flow Name>`     |
| jwks_uri               | `https://<AD Name>.b2clogin.com/<AD Domain>/discovery/v2.0/keys?p=b2c_1_<User Flow Name>`   |

:::info
ユーザーフローが1つだけの場合は、ユーザーフロー名の代わりにデフォルトが使用されることがあります。
:::

これでMicrosoft Azure側で必要な設定が完了しました。  
次に、KurocoのIDaaS SP編集画面での設定完了が必要です。

## Kuroco管理画面でIDaaS SP編集画面の設定をする

**1. IDaaS SP編集画面の設定**  
KurocoのIDaaS SP編集画面で、[クライアントID (Client ID) ]、[クライアントの秘密鍵 (Client Secret) ]、[承認URL]、[トークンURL]、および[JWKS URI]のコピーした値を入力してください。[リソースURL]は空のままにしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b41d975de071791fc20ff78e935203cb.png)

**2. ユーザーの識別方法を設定**  
この設定はサイトの構成によります。    
Kurocoはユーザーの識別にEメールまたはAzureユーザーオブジェクト識別子を使用できます。  
Eメールを利用する場合は、[Emailを利用せずメンバー拡張項目にIDを格納してリンクする]のチェックボックスを外す必要があります。  

Eメールをユーザー識別のキーに利用する場合は以下のように設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb382ae663d9dc0f8141134db854a3b9.png)

Eメールを使用しない場合は、有効にするのチェックボックスにチェックします。その場合、open_idが保存されるメンバーの拡張項目を選択する必要があります。  
*(注: 使用するメンバーの拡張項目のタイプはテキストである必要があります)*

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a73b663ce698e2ffef80e5e27f4d59c6.png)

**3. IDaaS SPを有効にする**  
最後に[有効]のチェックボックスをオンにし、[更新する]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d038e19882f395a3b40daaef82a39290.png)

これでKuroco側のIDaaS SPも設定が完了です。

## 使用方法
KurocoのIDaaS SPページに遷移します。  
作成したSP構成の[ログインIDaaS SP Name]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7aee6ac5b6c473037be78f6d9fd5aca5.png)

[ログインURL]が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d78d7fa6e6ce7aa83d4378cadd0d7229.png)

URLをクリックすると、Microsoft Entra External IDログインページにリンクされます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b33e99da2ea192fdad0744eada5ba5a3.png)

ここでMicrosoft Entra IDユーザーのEメールとパスワードを入力し、Kuroco SPにログインできます。

## 関連ドキュメント
- [IDaaS SP](/ja/docs/management/sso-idaas-sp/)
- [Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- [Microsoft Entra IDを使用してSCIMプロビジョニングを実装する](/ja/docs/tutorials/implementing-scim-provisioning-with-microsoft-entra-id/)
- [SPAでのSSO認証フローを実装する](/ja/docs/tutorials/implementing-sso-login-flow-in-spa/)
- [OAuthを使用したシングルサインオンはできますか](/ja/docs/faq/can-I-use-single-sign-on-using-oauth/)


---

# reCAPTCHAを利用したパスワードリマインダーを作成する

> 元ページ: `tutorials/using-recaptcha-for-password-reminders` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-recaptcha-for-password-reminders/
> 概要: パスワードリマインダーにreCAPTCHA v2を導入し、悪質なスパム投稿からWebサイトを守る手順を説明します。

## 概要
reCAPTCHAとは、Googleが無償で提供している機能です。  
Webサイトのお問い合わせフォーム等で情報を登録する際、悪質なスパム投稿からWebサイトを守ることができます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6cc0132cc7db5d90668c7a29c429748.png)

今回は、パスワードリマインダーにreCAPTCHA v2を導入する手順を説明します。

### 前提条件
- [パスワードリマインダー/パスワードリセットを設定する](/ja/docs/tutorials/how-to-use-password-reminder/)のチュートリアルを実施し、基本的なパスワードリマインダーの流れについて理解できていることを前提とします。
- [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display)を利用します。

## APIキーを取得する

KurocoでreCAPTCHAを利用する場合は、先にGoogle reCAPTCHAにてAPIキーの取得が必要になります。

:::info
※ 前提として、reCAPTCHAを利用するにはGoogleアカウントが必要になります。アカウントをお持ちでない場合は、[Googleのアカウント作成ページ](https://www.google.com/intl/ja/account/about/)よりアカウント作成をお願いします。
:::

まずは、[Google reCAPTCHA](https://www.google.com/recaptcha/about/)へアクセスし、[使ってみ見る]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b2b06c5045b04894d12524f916c3093c.png)

サイト登録画面が表示されるので、必要事項を記入します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9b60f86a19a75fc5281f8461bf2beaed.png)

|項目   |説明  |
| :--- | :--- |
|ラベル|サイト名等、わかりやすい名前を入力します。|
|reCAPTCHA タイプ|reCAPTCHA v2を選択します。<br/>また、「私はロボットではありません」チェックボックスを選択します。|
|ドメイン|「`https://`」を省略したフロントエンドドメインを入力します。<br/>例：`sitekey.g.kuroco-front.app`|

:::tip
ローカル環境でテストをする場合はドメインに`localhost`を追加します。
:::

利用規約を読み、問題なければ「reCAPTCHA 利用条件に同意する」にチェックを入れ[送信]をクリックしてください。

送信されると、「サイトキー」と「シークレットキー」が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e95a587d8bfebe5ab8d46bb510e04138.png)
こちらのキーはKurocoの設定で利用しますので、コピーをしておいてください。

以上でGoogle reCAPTCHA画面での設定が完了です。

## Kurocoの設定
次に、Kuroco管理画面での設定となります。ご自身のKuroco管理画面へログインしてください。

### reCAPTCHAと連携する
[外部システム連携] -> [reCAPTCHA]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a070adc9bddf613b1fdede5ad8a05131.png)

サイト管理画面内にサイトキーとシークレットキーを入力する箇所がありますので、それぞれ入力します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3e2a49ac5dc4bc377b52dbb79d866a26.png)

|項目   |説明  |
| :--- | :--- |
|reCaptcha Site Key|取得したサイトキーの値を入力します。|
|reCaptcha Secret Key|取得したシークレットキーの値を入力します。|

設定完了したら、画面下部の[更新する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d2a00321b6d1c3f8618573aa1f877020.png)

### エンドポイントを追加する
次にエンドポイントを作成します。
エンドポイント一覧画面へ移動し、reCAPTCHAを利用するパスワードリマインダーのエンドポイントを作成します。  

[新しいエンドポイントの追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/108ff9ede577df0e816da0c2186508bc.png)

以下のように設定します。

|項目|値|
|:--|:--|
|パス|reminder_with_recaptcha|
|カテゴリー|認証|
|モデル|Login|
|オペレーション|reminder|
|use_recaptcha|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7997ebc167c6e62891abd4e800df7662.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。  

### Swaggerにて確認する  
次に、問題なくエンドポイントが設定できているか、Swagger UIを利用して確認します。

エンドポイント一覧画面より、「Swaggr UI」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a8c0f3eb999544e1db72c9d4600edee.png)

先ほど設定したエンドポイントをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1bdb1707b11ab9f4e454f3c309249e92.png)

Request bodyのExample Valueに「recaptcha_response」のフィールドが記載されていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4295efe4fabb701dc8739af39cab7ec9.png)

以上でKuroco管理画面での設定は完了です。

## フロントエンドの実装
reCAPTCHA認証処理の実装方法例を記載します。

### reCAPTCHAモジュールのインストール
まずはNuxtのreCAPTCHAモジュールをインストールします。

ターミナルで下記実行します。

```
npm i @nuxtjs/recaptcha
```

### nuxt.config.jsの修正
次に、nuxt.config.jsにreCAPTCHAを追加します。
nuxt.config.jsの`modules:` に下記追記します。

```js
  modules: [
    '@nuxtjs/recaptcha',
  ],
```

また、モジュールに下記を追記します。

```js
 recaptcha: {
    hideBadge: true,
    language: 'ja',
    siteKey: 'reCAPTCHA_SITE_KEY',
    version: 2,
    size: 'normal'
  },
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cddf543ed94c580313533e3904533bac.png)

:::caution
reCAPTCHA_SITE_KEYには、先程取得したreCAPTCHAのサイトキーを記入してください。
:::

### 認証コンポーネントを実装する
認証コンポーネントを作成します。
今回は、`/components/inquiry`配下に`inquiry-recaptcha.vue`というファイルを作成します。

```markup title="/components/inquiry/inquiry-recaptcha.vue"
<template>
  <recaptcha @error="onError" @success="onSuccess" @expired="isExpired" />
</template>
<script>
export default {
  methods: {
    onError() {
      this.$emit('update:is-succeeded', false);
    },
    onSuccess() {
      this.$emit('update:is-succeeded', true);
    },
    isExpired() {
      this.$emit('update:is-succeeded', false);
    },
    async fetchResponse() {
      let response;
      try {
        response = await this.$recaptcha.getResponse();
      } catch (error) {
        response = '';
      }
      this.$emit('update:is-succeeded', !!response);
      return response;
    }
  }
}
</script>
```

### パスワードリマインダー画面を作成する
次に、reCAPTCHAを導入したいパスワードリマインダー画面で、上記認証コンポーネントを使用します。
今回は `/pages/form/index.vue` を下記のように作りました。  

`await this.$refs.recaptcha.fetchResponse()`で`recaptcha_response`を取得し、入力されたメールアドレスと合わせてKurocoにPOSTしています。  
送信後は `await this.$recaptcha.reset()` を呼び出す必要があります。 


```markup reference title="/pages/recaptha_for_password_reminders/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/recaptha_for_password_reminders.vue
```

:::caution
上記のコードは最低限の簡易的なものになっています。
:::

パスワードリマインダー画面を確認すると、下記のようにreCAPTCHAが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6cc0132cc7db5d90668c7a29c429748.png)

### 動作の確認
「私はロボットではありません」にチェックを入れると、Submitボタンがクリックできるようになります。  
Submitボタンをクリックすると、フォームの内容に加えて、recaptcha_responseをKurocoにPostし、渡されたトークンが自動的に検証されます。  
正当な値が渡された場合、フォーム送信が完了し、入力したメールアドレス宛にパスワードリセットのための仮パスワードが届きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/43b3659f5ed4bc77e1fe949f6032beff.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b07b1b76adf93e66f772e9f5ba1710a9.png)

:::tip
パスワードリマインダーのメールは[メッセージひな形](/ja/docs/management/email-template/)の識別子`login/reset_password`のテンプレートで編集可能です。
:::

不正な値が渡された場合は、下記のようなエラーが返ります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/85b13daef024ef8a9ea700113d5711a9.png)

以上でreCAPTHAの設定が完了です。

今回は基本的な説明のため、簡単な設定方法を例に説明しました。
reCAPTCHAの詳しい設定方法は下記Googleのドキュメントをご参照ください。  
[Google Developers reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display)

## 関連ドキュメント
- [パスワードリマインダー/パスワードリセットを設定する](/ja/docs/tutorials/how-to-use-password-reminder/)
- [reCAPTCHA](/ja/docs/management/recaptcha/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [reCAPTCHAを利用したフォームを作成する](/ja/docs/tutorials/using-recaptcha/)
- [問い合わせフォームに大量のスパムメールが届きます。対策はありませんか？](/ja/docs/faq/how-do-i-reduce-spam-inquiries/)
