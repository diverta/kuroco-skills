# Kurocoドキュメント: チュートリアル / 認証・会員（3/4）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- KurocoとNuxt.jsで、ログイン画面を構築する（`integrate-login-nuxt2`）
- ログインする（`login`）
- 新しいIPアドレスからログインがあった場合に通知を送る（`send-a-notification-when-there-is-a-login-from-a-new-ip-address`）
- 会員制サンプルサイトで、開発環境と本番環境を分ける方法（`separating-development-and-production-environments-for-your-sample-membership-site`）
- Kuroco管理画面にワンタイムパスワードを利用した2要素認証を設定する（`set-up-a-one-time-password-for-logging-into-the-kuroco-admin-panel`）
- Kuroco管理画面でPasskeyを使用した二要素認証の設定方法（`set-up-passkey-for-logging-into-the-kuroco-admin-panel`）
- 会員登録画面に仮登録機能を実装する（`setting-up-pre-member-registration-form`）
- 新規会員登録画面を構築する（`setting-up-registration-form`）


---

# KurocoとNuxt.jsで、ログイン画面を構築する

> 元ページ: `tutorials/integrate-login-nuxt2` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrate-login-nuxt2/
> 概要: Kurocoを利用したNuxt.jsプロジェクトで、ログイン画面の作成方法を紹介します。今回は例として、下記流れにてログインユーザーのみコンテンツ一覧ページが閲覧できる処理を実装します。

Kurocoを利用したNuxt.jsプロジェクトで、ログイン画面の作成方法を紹介します。  
今回は例として、下記流れにてログインユーザーのみコンテンツ一覧ページが閲覧できる処理を実装します。

- API・エンドポイントの作成
- ログインフォーム実装
- ログイン処理実装(APIセキュリティ毎)

## 前提条件
### Nuxt.jsプロジェクトの作成について
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、コンテンツ一覧のページが作成されていることを前提としています。 まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)

### APIセキュリティについて
Kurocoでは、APIのセキュリティ方法がいくつか用意されています。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5d2188e3c2ea2c2b34b726e9fab91406.png)
セキュリティ「無し」を選択されている場合には、ログインの必要無くAPIからデータを取得できますが、
何らかのセキュリティを設定している場合、利用者にはフロントエンドのログインフォームから認証/認可をしていただく必要があります。

今回は、代表的なログイン方式として、以下の２つのパターンを例にしてフロントエンドのログインフォームを構築します。
- Cookie
- 動的アクセストークン

:::info
セキュリティの種類については、[管理画面マニュアル -> API Security](/ja/docs/management/api-security/)を参照してください。
:::

:::info
セキュリティの種類の詳細な確認方法は、[Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)をご確認ください。
:::

### 推奨ブラウザについて
本チュートリアルは、動作確認のためGoogle Chromeの開発者ツールを利用しています。
そのため、ブラウザはGoogle Chromeを推奨いたします。

## APIの設定
ログイン用のAPIを設定します。

### APIの作成
まずはAPIを新規で作成します。  
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/417993d1fc8a3357e8a3a24cece6c836.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8689b06228161c57065ce8e3255a41e6.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|login|
|版|1.0|
|ディスクリプション|login用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/169c75140c1f30b80fd053292cd27140.png)

### エンドポイントの作成
次にエンドポイントを作成します。今回は下記エンドポイントを作成します。

- loginエンドポイント
- profileエンドポイント
- logoutエンドポイント
- tokenエンドポイント（APIセキュリティが動的アクセストークンの場合のみ）

「新しいエンドポイントの追加」をクリックし、それぞれ作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e20df3e56291487f859a3cbd905b261.png)

#### loginエンドポイントの作成
loginエンドポイントを下記設定にて作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7fd232391acf1d8ec8c611cf715097c.png)

|項目|設定内容|
| :--- | :--- |
|パス|login|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|login_challenge|

設定完了後、「追加する」をクリックしloginエンドポイント完成です。

#### profileエンドポイントの作成
profileエンドポイントを下記設定にて作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15300b156fe0986773788745876a37cb.jpg)

|項目|設定内容|
| :--- | :--- |
|パス|profile|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|profile|
|APIリクエスト制限|GroupAuth：所属しているグループ<br/>ログインを許可するグループを選択してください。|
|基本設定：basic_info|<ul><li>email</li><li>name1</li><li>name2</li></ul>|

設定完了後、「追加する」をクリックしエンドポイント完成です。

profileエンドポイントは、アクセスしているユーザーの情報を(簡易的に)返却するものです。  
GroupAuthでの認証を設定しているため、ログイン済みで無い場合は情報を返さずにエラーとなります。

今回の場合は、email,name1,name2を値を返すように設定しており、簡易的なユーザー情報を取得するほかに、ログイン状態のリストアをする際、操作しているユーザーが本当にログイン済みであるのかを検証するためにリクエストします。

#### logoutエンドポイントの作成
logoutエンドポイントを下記設定にて作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8253679d4e181188b92329265a3a14e7.png)

|項目|設定内容|
| :--- | :--- |
|パス|logout|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|logout|
|APIリクエスト制限|None|

設定完了後、「追加する」をクリックしエンドポイント完成です。

#### tokenエンドポイントの作成
tokenエンドポイントを下記設定にて作成します。

:::tip
tokenエンドポイントは、APIセキュリティが動的アクセストークンの場合のみ必要になります。
APIセキュリティがCookieの場合、作成する必要はありません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14c7ee1c0f3363ac78618c9227b1c273.png)

|項目|設定内容|
| :--- | :--- |
|パス|token|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|token|
|APIリクエスト制限|None|

設定完了後、「追加する」をクリックしエンドポイント完成です。

### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e4f4ff71679c45b81ecb2d54b79999d.png)

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
以上で、APIの設定が完了です。

## ログインフォーム実装
次に、フロントエンドにログインフォームを作成します。

### ダミーのログインフォーム実装

まずはAPIとの連携は省いた状態でログイン画面用コンポーネントの作成し、ダミーでのログイン連携処理を実装していきます。  
また、お知らせ一覧画面ではログイン済みかどうかのフラグを参照し、ログイン済みでなければログイン画面に画面遷移するように変更します。

まず、ログイン画面用コンポーネントを作成します。
`pages/login/index.vue` ファイルを新規作成し、以下を記載してください。
```markup [pages/login/index.vue]
<template>
    <form @submit.prevent="login">
        <input v-model="email" name="email" type="email" placeholder="email"/>
        <input
            v-model="password"
            name="password"
            type="password"
            placeholder="password"
        />
        <button type="submit">
            ログイン
        </button>
    </form>
</template>

<script>
export default {
    data () {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        login () {
            console.log(this.email, this.password)
        }
    },
};
</script>

```

この状態で`npm run dev`を実行し、`http://localhost:3000/login`にアクセスすると簡単なログインフォームが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6fd3b6262b1bc084bd306a34a0cd2ae9.png)

ここまでで、一度ログの確認をします。  
Chromeの開発者ツール:コンソールを開いた状態でフォームに下記を入力し、[ログイン]をクリックします。

- email:`test@example.com`
- password:password

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0445a7f55742fd2b89ace826f2f36d58.png)

すると、入力したemailとpasswordがログとしてコンソールに表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0fb5d190d7550e759fbc58b8760a4553.png)

このログに出力された値をログイン用APIに実際にリクエストすることになります。ひとまずAPI連携部分は仮で実装をし、ログイン後の動きを確認します。

1秒間のリクエストをする見せかけのダミー処理を追加作成し、ログインリクエストに成功した場合、画面上で"ログイン成功"と表示されるように、下記のように修正します。

```diff
diff --git a/pages/login/index.vue b/pages/login/index.vue
index 44146fc..492b108 100644
--- a/pages/login/index.vue
+++ b/pages/login/index.vue
@@ -1,28 +1,63 @@
 <template>
     <form @submit.prevent="login">
+        <p v-if="loginStatus !== null" :style="{ color: resultMessageColor }">
+            {{ resultMessage }}
+        </p>
+
         <input v-model="email" name="email" type="email" placeholder="email"/>
         <input
             v-model="password"
             name="password"
             type="password"
             placeholder="password"
         />
         <button type="submit">
             ログイン
         </button>
     </form>
 </template>
 
 <script>
 export default {
     data () {
         return {
             email: '',
-            password: ''
+            password: '',
+
+            loginStatus: null,
+            resultMessage: null
         };
     },
+    computed: {
+        resultMessageColor () {
+            switch (this.loginStatus) {
+            case 'success':
+                return 'green'
+            case 'failure':
+                return 'red'
+            default:
+                return ''
+            };
+        }
+    },
     methods: {
-        login () {
-            console.log(this.email, this.password)
+        async login () {
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
+                this.loginStatus = 'success'
+                this.resultMessage = 'ログインに成功しました。'
+            } catch (e) {
+                this.loginStatus = 'failure'
+                this.resultMessage = 'ログインに失敗しました。'
+            };
         }
     },
 };
 </script>
```

1秒の待機の後、[ログインに成功しました]が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef9fba1bd155c07942d3b6358cca26ee.png)

失敗した際にどうなるかを確認します。

ソースコードから、`shouldSuccess = true`を `shouldSuccess = false`へ変更し、レスポンスがエラーとなる場合を再現確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/65b275244baa02a566029ba77919a757.png)

確認後は、`shouldSuccess = true`へ戻してください。

### ログイン状態の保持
次にログイン状態を保持できるように実装します。


#### a. storeの作成
まずはログイン状態をWebアプリ全体で保持しておき、他の画面でも参照できるよう**store**を作成します。

`store/index.js`ファイルを新規作成し、下記のコードを記載してください。

```javascript
export const state = () => ({
    profile: null
})

export const getters = {
    authenticated (state) {
        return state.profile !== null
    }
}

export const mutations = {
    setProfile (state, { profile }) {
        state.profile = profile
    }
}
```

`getters`の`authenticated`は、後ほど作成していくprofileデータが空かどうかでtrue/falseが返却されるものです。  
profileデータが空で無ければログイン状態と判定する想定をしています。

後にログインした時やログイン状態のリストア時にprofileデータを自動取得し、それ以外のログアウトなどで値が設定されないようにしていきます。

#### b. middlewareの作成
次にmiddlewareを作成します。

`middleware/auth.js`を新規作成し、下記のコードを記載してください。

```javascript
export default async ({ app, store, redirect }) => {
    if (!store.getters.authenticated) {
        return redirect('/login')
    }
    await null
}
```

middlewareは各画面のソース`page/*.vue`が処理をする以前に動作します。
storeの`authenticated`がfalseである場合にはログインページへ強制的にリダイレクトさせます。

#### c. middlewareの動作確認

middlewareの動作を確認します。
`pages/login/index.vue`にニュース一覧ページへのリンクを追加します。

```diff
diff --git a/pages/login/index.vue b/pages/login/index.vue
index eb123b4..37d845a 100644
--- a/pages/login/index.vue
+++ b/pages/login/index.vue
@@ -14,6 +14,12 @@
         <button type="submit">
             ログイン
         </button>
+
+        <div>
+            <nuxt-link to="/news">
+                ニュース一覧ページへ
+            </nuxt-link>
+        </div>
     </form>
 </template>

```

ニュース一覧画面の`pages/news/index.vue`のソースコードを変更して、middlewareを適用します。

```diff
diff --git a/pages/news/index.vue b/pages/news/index.vue
index ac8e0fd..dcdd806 100644
--- a/pages/news/index.vue
+++ b/pages/news/index.vue
@@ -10,6 +10,7 @@
 
 <script>
 export default {
+    middleware: 'auth',
     async asyncData ({ $axios }) {
         return {
             response: await $axios.$get('/rcms-api/4/news'),

```

:::caution
`/rcms-api/4/news`の部分はご自身のエンドポイントのURLに変更してください。<br/>
以下同様に、ソースコード内のエンドポイントURLはご自身のエンドポイントURLに変更をお願いします。
:::

この処理により、ニュース一覧画面にアクセスするためにはログインが必要になります。
ログインしていない場合は、ニュース一覧ページへアクセスすると強制的にログイン画面へとリダイレクトされるようになります。

次に、ログイン成功時、`store`の`prfofile`をnull以外の状態へ変更するようにします。
`pages/login/index.vue`を下記のように変更します。

```diff
diff --git a/pages/login/index.vue b/pages/login/index.vue
index 37d845a..b3cd6a1 100644
--- a/pages/login/index.vue
+++ b/pages/login/index.vue
@@ -59,6 +59,8 @@ export default {
 
             try {
                 await request
+                this.$store.commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
+
                 this.loginStatus = 'success'
                 this.resultMessage = 'ログインに成功しました。'
             } catch (e) {

```

ログインページにアクセスし、ログイン操作をしてニュース一覧ページに画面遷移することを確認します。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/56dec7340110021efd1a8a6580d8e340.gif)
:::tip
確認には[Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd/reviews?hl=ja&authuser=2)を使用しています。
:::

### ログイン状態のリストアの実装

これまでの実装によって通常のログイン処理は実装されました。
しかしながら、直接URLアクセスやブラウザで画面更新されたとき、これまでの実装では一度ログインしたはずであるのにも関わらずログイン画面にリダイレクトされる不具合が発生します。

上記の操作では、`store`の`profile`はNuxtが初期化されるためnullとなり、
直前に一度ログインしていた場合であってもログイン状態と判定されないためです。

この対応には、一度ログインしたことがある場合にはブラウザのLocalStorageにフラグを設定しておき、
フラグがtrueである場合に`store`の`profile`にダミーのデータを適用するようにします。

`/store/index.js`を下記のように修正してください。

```diff
diff --git a/store/index.js b/store/index.js
index 1c36f1d..5cca182 100644
--- a/store/index.js
+++ b/store/index.js
@@ -13,3 +13,15 @@ export const mutations = {
         state.profile = profile
     }
 }
+
+export const actions = {
+    async restoreLoginState ({ commit }) {
+        const authenticated = JSON.parse(localStorage.getItem('authenticated'))
+
+        if (!authenticated) {
+            throw new Error('need to login')
+        }
+        commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.
+        await null
+    }
+}

```

また、`/middleware/auth.js`を下記のように修正してください。

```diff
diff --git a/middleware/auth.js b/middleware/auth.js
index d3c7ffe..4aa086c 100644
--- a/middleware/auth.js
+++ b/middleware/auth.js
@@ -1,7 +1,9 @@
 export default async ({ app, store, redirect }) => {
     if (!store.getters.authenticated) {
-        return redirect('/login')
+        try {
+            await store.dispatch('restoreLoginState')
+        } catch (err) {
+            return redirect('/login')
+        }
     }
-
-    await null
 }

```

ニュース一覧ページにアクセスし、下記4点を確認します。
- LocalStorageの`authenticated`がtrue以外である場合、ログインページにリダイレクトされること
- LocalStorageの`authenticated`がtrueである場合、ログインページにリダイレクトされないこと
- LocalStorageの`authenticated`がtrueかつブラウザの画面更新をした場合でも、ログインページにリダイレクトされないこと
- LocalStorageの`authenticated`をfalseにしてブラウザの画面更新をすると、ログインページにリダイレクトされること

今回はLocalStorageの状態を、chromeの開発者ツールの[Application]タブにて確認します。  
chromeの開発者ツールより[Application]タブをクリックし、[Storage] -> [Local Storage] -> [http://localhost:3000]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/aa339de13a1d00de92fc5c44048f863d.png)
ログインページよりログイン後、Keyに`authenticated`、Valueに`true`または`false`を入力し、上記4点の動作を確認します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/314b063e93383a7eb636abdef9d722ae.gif)
### ログイン動作修正
次にログイン動作を修正します。  
ログイン成功時にLocalStorageの`authenticated`をtrueにさせます。また、今後の修正に備えてログイン処理を一部`store`に移動します。

`/pages/login/index.vue`を下記のように修正します。

```diff
diff --git a/pages/login/index.vue b/pages/login/index.vue
index b3cd6a1..25f6a8c 100644
--- a/pages/login/index.vue
+++ b/pages/login/index.vue
@@ -48,18 +48,12 @@ export default {
     },
     methods: {
         async login () {
-            // ダミーリクエスト(1秒待機の後成功/失敗する)
-            const shouldSuccess = true
-            const request = new Promise((resolve, reject) =>
-                setTimeout(
-                    () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
-                    1000
-                )
-            )
-
             try {
-                await request
-                this.$store.commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
-
+                const payload = {
+                    email: this.email,
+                    password: this.password
+                }
+                await this.$store.dispatch('login', payload)
 
                 this.loginStatus = 'success'
                 this.resultMessage = 'ログインに成功しました。'

```

次に`/store/index.js`を下記のように修正します。

```diff
diff --git a/store/index.js b/store/index.js
index 5cca182..b09c428 100644
--- a/store/index.js
+++ b/store/index.js
@@ -11,10 +11,29 @@ export const getters = {
 export const mutations = {
     setProfile (state, { profile }) {
         state.profile = profile
+    },
+    updateLocalStorage (state, payload) {
+        Object.entries(payload).forEach(([key, val]) => {
+            localStorage.setItem(key, val)
+        })
     }
 }
 
 export const actions = {
+    async login ({ commit }, payload) {
+        // ダミーリクエスト(1秒待機の後成功/失敗する)
+        const shouldSuccess = true
+        const request = new Promise((resolve, reject) =>
+            setTimeout(
+                () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
+                1000
+            )
+        )
+        await request
+
+        commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
+        commit('updateLocalStorage', { authenticated: true })
+    },
     async restoreLoginState ({ commit }) {
         const authenticated = JSON.parse(localStorage.getItem('authenticated'))

```

ログイン成功時に`authenticated`がtrueになることを確認します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3c9b258dc445720d0b8598e6d40cd149.gif)
以上でフロントエンドの実装を終了します。

次にAPIを実装します。
なお、実装はAPIセキュリティ毎に実装方法が変わります。
今回はAPIセキュリティがCookieの場合と、動的アクセストークンの場合の実装方法を記載します。
ご自身のAPIセキュリティに併せて、それぞれの対応方法をご確認ください。

- A. [ログイン処理実装(APIセキュリティがCookieの場合)](#a-ログイン処理実装apiセキュリティがcookieの場合)
- B. [ログイン処理実装(APIセキュリティが動的アクセストークンの場合)](#b-ログイン処理実装apiセキュリティが動的アクセストークンの場合)


## A. ログイン処理実装(APIセキュリティがCookieの場合)
次に、先ほどダミーで作成していたログイン処理をloginエンドポイントへとアクセスするように変更します。
まずはAPIセキュリティがCookieの場合の実装方法を説明します。
Kuroco管理画面より、[API] -> [login] をクリックし、「セキュリティ」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84a08a9b4d235d33269d95aab19064ad.png)
「セキュリティ」よりCookieを選択し、「保存する」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8f655bfb466cef7bc2683e3b2e0c0aa9.png)

### loginエンドポイントへのリクエスト実装
`store/index.js`を下記に修正します。

```diff
diff --git a/store/index.js b/store/index.js
index b09c428..45982c8 100644
--- a/store/index.js
+++ b/store/index.js
@@ -21,15 +21,7 @@ export const mutations = {
 
 export const actions = {
     async login ({ commit }, payload) {
-        // ダミーリクエスト(1秒待機の後成功/失敗する)
-        const shouldSuccess = true
-        const request = new Promise((resolve, reject) =>
-            setTimeout(
-                () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
-                1000
-            )
-        )
-        await request
+        await this.$axios.$post('/rcms-api/9/login', payload)
 
         commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
         commit('updateLocalStorage', { authenticated: true })

```

次に、loginエンドポイントへリクエストされているか確認します。

ログインページを開き、Chromeの開発者ツール:ネットワークを開いた状態でログイン処理を行います。
すると、loginエンドポイントへとリクエストされていることが確認できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e5ba4778eecabe224ae2fa018819eb04.png)

### cookieの有効化

クロスオリジンでのcookieを有効化するため、`nuxt.config.js`を下記のように修正してください。

```diff
diff --git a/nuxt.config.js b/nuxt.config.js
index 56cd22f..0445d45 100644
--- a/nuxt.config.js
+++ b/nuxt.config.js
@@ -51,9 +51,9 @@ export default {
 
     // Axios module configuration: https://go.nuxtjs.dev/config-axios
-     axios: {},
+     axios: {
+         baseURL: process.env.BASE_URL,
+         credentials: true,
+         withCredentials: true
+     },
 
     // Build Configuration: https://go.nuxtjs.dev/config-build

```

### profileエンドポイントへのリクエスト/ハンドリング実装

今までの実装では、ブラウザのLocalStorageの`authenticated`フラグによってログイン済かどうかを判断する実装をしています。  
しかしながら、LocalStorageはブラウザ上で簡単に改ざんが可能です。

またセッション有効期限によって`authenticated`がtrueであっても、実際には他のエンドポイントへのリクエストがアクセスエラーとなる場合もあります。  
これらによる誤動作を防ぐため、profileのAPIにリクエストし、ユーザー情報が返ってくるか否かを確認することで二重のチェックを行います。  

:::tip
二重のチェックは、profileエンドポイントである必要はありませんが、ログイン中のユーザー名を表示する等、profileが返すデータを最初に必要とするユースケースが多いため、profileエンドポイントの利用が、スタンダードになっています。
:::

`/store/index.js`を下記のように修正します。

```diff
--- a/store/index.js
+++ b/store/index.js
@@ -24,7 +24,13 @@ export const mutations = {
 export const actions = {
   async login({ commit }, payload) {
     await this.$axios.$post('/rcms-api/9/login', payload)

-    commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
+    const profileRes = await this.$axios.$get('/rcms-api/9/profile')
+    commit('setProfile', { profile: profileRes })
     commit('updateLocalStorage', { authenticated: true })
   },
   async restoreLoginState({ commit }) {
     const authenticated = JSON.parse(localStorage.getItem('authenticated'))

     if (!authenticated) {
       throw new Error('need to login')
     }
-    commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.
-    await null
+
+    const profileRes = await this.$axios.$get('/rcms-api/9/profile')
+    commit('setProfile', { profile: profileRes })
   }
 }
```

修正ができたらリストアの動作を確認します。

ログインページを開き、Chromeの開発者ツール:アプリケーションを開いた状態でログイン処理を行います。
すると、`authenticated`が`true`となります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/022f5f48843929fdd94f23b3fe4c220b.png)
この状態で、「ニュース一覧ページへ」をクリックし画面遷移します。  
今までの実装と同じように、`authenticated`が`true`のまま、ニュース一覧ページの表示を確認できます。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/78a69c39bb4de3780b8f38cbb3a73f2a.gif)

### logoutエンドポイントへのリクエスト/ハンドリング実装
次に、ログアウト処理を実装します。

Kuroco側でセッションが残っていながらフロント側で再ログインした場合など、予期せぬ動作が発生する可能性もあります。  
そのため、ログイン状態ではないと判定する場合はAPIへログアウト状態にするようリクエストする必要があります。

`/store/index.js`を下記のように修正します。

```diff
diff --git a/store/index.js b/store/index.js
index 296c4dc..068e184 100644
--- a/store/index.js
+++ b/store/index.js
@@ -27,13 +27,29 @@ export const actions = {
         commit('setProfile', { profile: profileRes })
         commit('updateLocalStorage', { authenticated: true })
     },
-    async restoreLoginState ({ commit }) {
+    async logout ({ commit }) {
+        try {
+            await this.$axios.$post('/rcms-api/9/logout')
+        } catch {
+            /** No Process */
+            /** エラーが返却されてきた場合は、結果的にログアウトできているものとみなし、これを無視します。 */
+        }
+        commit('setProfile', { profile: null })
+        commit('updateLocalStorage', { authenticated: false })
+
+        this.$router.push('/login')
+    },
+    async restoreLoginState ({ commit, dispatch }) {
         const authenticated = JSON.parse(localStorage.getItem('authenticated'))
 
         if (!authenticated) {
+            await dispatch('logout')
+            throw new Error('need to login')
+        }
+        try {
+            const profileRes = await this.$axios.$get('/rcms-api/9/profile')
+            commit('setProfile', { profile: profileRes })
+        } catch {
+            await dispatch('logout')
             throw new Error('need to login')
         }
-        const profileRes = await this.$axios.$get('/rcms-api/9/profile')
-        commit('setProfile', { profile: profileRes })
     }
 }

```

また、ニュース一覧画面を以下のように修正し、ログアウトボタンを作成します。

```diff
diff --git pages/news/index.vue pages/news/index.vue
index dcdd806..e79e075 100644
--- pages/news/index.vue
+++ pages/news/index.vue
@@ -1,23 +1,31 @@
 <template>
     <div>
         <p>ニュース一覧ページ</p>
+        <button type="button" @click="logout">
+            ログアウト
+        </button>
         <div v-for="n in response.list" :key="n.slug">
             <nuxt-link :to="`/news/${n.topics_id}`">
                 {{ n.ymd }} {{ n.subject }}
             </nuxt-link>
         </div>
     </div>
 </template>
 
 <script>
+import { mapActions } from 'vuex';
+
 export default {
     middleware: 'auth',
     async asyncData ({ $axios }) {
         return {
             response: await $axios.$get('/rcms-api/4/news'),
         };
     },
+    methods: {
+        ...mapActions(['logout'])
+    },
 };
 </script>

```

ログイン状態のニュース一覧画面にてログアウトボタンをクリックすると、下記となることを確認します。
- logoutエンドポイントへリクエストしている
- ログイン画面に遷移する
- そのままログインせずにニュース一覧画面へアクセスすると、ログイン画面に自動遷移される

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/8627f900c0652b11a1c84c3f33199842.gif)
以上でAPIセキュリティがcookieの場合のログイン処理の実装が完了です。

## B. ログイン処理実装(APIセキュリティが動的アクセストークンの場合)
次に、先ほどダミーで作成していたログイン処理をloginエンドポイントへとアクセスするように変更します。
ここではAPIセキュリティが動的アクセストークンの場合の実装方法を説明します。
Kuroco管理画面より、[API] -> [login] をクリックし、「セキュリティ」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84a08a9b4d235d33269d95aab19064ad.png)
「セキュリティ」より動的アクセストークンを選択し、「保存する」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/62acbc6f847a833939cc592bcc2d8f47.png)
### login,tokenエンドポイントへのリクエスト実装

`store/index.js`を下記に修正します。

```diff
diff --git a/store/index.js b/store/index.js
index b09c428..64e6e2d 100644
--- a/store/index.js
+++ b/store/index.js
@@ -21,15 +21,11 @@ export const mutations = {
 
 export const actions = {
     async login ({ commit }, payload) {
-        // ダミーリクエスト(1秒待機の後成功/失敗する)
-        const shouldSuccess = true
-        const request = new Promise((resolve, reject) =>
-            setTimeout(
-                () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
-                1000
-            )
+        const { grant_token } = await this.$axios.$post('/rcms-api/9/login', payload)
+        const { access_token } = await this.$axios.$post(
+            '/rcms-api/9/token',
+            { grant_token }
         )
-        await request
 
         commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
         commit('updateLocalStorage', { authenticated: true })

```

loginエンドポイントとtokenエンドポイントへリクエストされているか確認します。

ログインページを開き、Chromeの開発者ツール:ネットワークを開いた状態でログイン処理を行います。 すると、loginエンドポイントとtokenエンドポイントへとリクエストされていることが確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/79bc58bf120ff305145d5a9dfc71d706.gif)
### tokenの保持

ここまでは、ログインしているかどうかをLocalStorageの`authenticated`のフラグ値で判定していました。  
しかし、動的アクセストークンでは認証を要求するエンドポイントには実際のtoken値が必要になります。  
そのため、`authenticated`を`token`へ変更し、token値を保持するようにします。

`store/index.js`を下記に修正します。

```diff
diff --git store/index.js store/index.js
index 64e6e2d..9b048c5 100644
--- store/index.js
+++ store/index.js
@@ -1,42 +1,50 @@
 export const state = () => ({
     profile: null
 })
 
 export const getters = {
     authenticated (state) {
         return state.profile !== null
     }
 }
 
 export const mutations = {
     setProfile (state, { profile }) {
         state.profile = profile
     },
     updateLocalStorage (state, payload) {
         Object.entries(payload).forEach(([key, val]) => {
             localStorage.setItem(key, val)
         })
+    },
+    setAccessTokenOnRequestHeader (state, { rcmsApiAccessToken }) {
+        this.$axios.defaults.headers.common = {
+            'X-RCMS-API-ACCESS-TOKEN': rcmsApiAccessToken
+        }
     }
 }
 
 export const actions = {
     async login ({ commit }, payload) {
         const { grant_token } = await this.$axios.$post('/rcms-api/9/login', payload)
         const { access_token } = await this.$axios.$post(
             '/rcms-api/9/token',
             { grant_token }
         )
 
+        commit('updateLocalStorage', { rcmsApiAccessToken: access_token.value })
+        commit('setAccessTokenOnRequestHeader', { rcmsApiAccessToken: access_token.value })
+
         commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
-        commit('updateLocalStorage', { authenticated: true })
     },
     async restoreLoginState ({ commit }) {
-        const authenticated = JSON.parse(localStorage.getItem('authenticated'))
+        const rcmsApiAccessToken = localStorage.getItem('rcmsApiAccessToken')
+        const authenticated = typeof rcmsApiAccessToken === 'string' && rcmsApiAccessToken.length > 0
 
         if (!authenticated) {
             throw new Error('need to login')
         }
         commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.
         await null
     }
 }

```

ログイン成功後の動きを確認します。

ログインページを開き、Chromeの開発者ツール:アプリケーションを開いた状態でログイン処理を行います。 すると、`rcmsApiAccessToken`に値が保存されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/7683dcc908622c9f2fbe03f7c53995c9.gif)
### profileエンドポイントへのリクエスト/ハンドリング実装

今までの実装では、ブラウザのLocalStorageの`rcmsApiAccessToken`フラグによってログイン済かどうかを判断する実装をしています。  
しかしながら、LocalStorageはブラウザ上で簡単に改ざんが可能です。

またセッション有効期限によって`rcmsApiAccessToken`がtrueであっても、実際には他のエンドポイントへのリクエストがアクセスエラーとなる場合もあります。  
これらによる誤動作を防ぐため、APIへアクセスすることによって、もう1クッションの追加確認をします。


そのため、`/store/index.js`を下記のように修正します。

```diff
diff --git store/index.js store/index.js
index 9b048c5..c64b3a9 100644
--- store/index.js
+++ store/index.js
@@ -1,50 +1,57 @@
 export const state = () => ({
     profile: null
 })
 
 export const getters = {
     authenticated (state) {
         return state.profile !== null
     }
 }
 
 export const mutations = {
     setProfile (state, { profile }) {
         state.profile = profile
     },
     updateLocalStorage (state, payload) {
         Object.entries(payload).forEach(([key, val]) => {
             localStorage.setItem(key, val)
         })
     },
     setAccessTokenOnRequestHeader (state, { rcmsApiAccessToken }) {
         this.$axios.defaults.headers.common = {
             'X-RCMS-API-ACCESS-TOKEN': rcmsApiAccessToken
         }
     }
 }
 
 export const actions = {
     async login ({ commit }, payload) {
         const { grant_token } = await this.$axios.$post('/rcms-api/9/login', payload)
         const { access_token } = await this.$axios.$post(
             '/rcms-api/9/token',
             { grant_token }
         )
 
         commit('updateLocalStorage', { rcmsApiAccessToken: access_token.value })
         commit('setAccessTokenOnRequestHeader', { rcmsApiAccessToken: access_token.value })
 
-        commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.state.profileに適用
+        const profileRes = await this.$axios.$get('/rcms-api/9/profile')
+        commit('setProfile', { profile: profileRes })
     },
     async restoreLoginState ({ commit }) {
         const rcmsApiAccessToken = localStorage.getItem('rcmsApiAccessToken')
         const authenticated = typeof rcmsApiAccessToken === 'string' && rcmsApiAccessToken.length > 0
 
         if (!authenticated) {
             throw new Error('need to login')
         }
-        commit('setProfile', { profile: {} }) // ダミーのオブジェクトをstore.
-        await null
+
+        try {
+            commit('setAccessTokenOnRequestHeader', { rcmsApiAccessToken })
+            const profileRes = await this.$axios.$get('/rcms-api/9/profile')
+            commit('setProfile', { profile: profileRes })
+        } catch {
+            throw new Error('need to login')
+        }
     }
 }

```

ログイン後、ブラウザの画面更新をしてニュース一覧画面に遷移し、ログイン状態がリストアされることを確認します。

ログインページを開き、Chromeの開発者ツール:アプリケーションを開いた状態でログイン処理を行います。 すると、`rcmsApiAccessToken`に値が保存されます。

また、この状態で、「ニュース一覧ページへ」をクリックし画面遷移しても、`rcmsApiAccessToken`に値が保存されたままであることを確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/49669f73da2cd59af13c17bf9a37ceb8.gif)
さらに、LocalStorageの`rcmsApiAccessToken`をChromeの開発者ツールより修正した場合、リストア時にログイン画面へ強制的に画面遷移されることが確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5edfbdf317001395e794f30c6ca8380e.gif)

### logoutエンドポイントへのリクエスト/ハンドリング実装

次に、ログアウト処理を実装します。

Kuroco側でセッションが残っていながらフロント側で再ログインした場合など、予期せぬ動作が発生する可能性もあります。  
そのため、ログイン状態ではないと判定する場合はAPIへログアウト状態にするようリクエストする必要があります。

`/store/index.js`を下記のように修正します。

```diff
diff --git a/store/index.js b/store/index.js
index c64b3a9..0e97247 100644
--- a/store/index.js
+++ b/store/index.js
@@ -38,19 +38,32 @@ export const actions = {
         const profileRes = await this.$axios.$get('/rcms-api/9/profile')
         commit('setProfile', { profile: profileRes })
     },
-    async restoreLoginState ({ commit }) {
+    async logout ({ commit }) {
+        try {
+            await this.$axios.$post('/rcms-api/9/logout')
+        } catch {
+            /** No Process */
+            /** エラーが返却されてきた場合は、結果的にログアウトできているものとみなし、これを無視します。 */
+        }
+        commit('setProfile', { profile: null })
+        commit('updateLocalStorage', { rcmsApiAccessToken: null })
+        commit('setAccessTokenOnRequestHeader', { rcmsApiAccessToken: null })
+
+        this.$router.push('/login')
+    },
+    async restoreLoginState ({ commit, dispatch }) {
         const rcmsApiAccessToken = localStorage.getItem('rcmsApiAccessToken')
         const authenticated = typeof rcmsApiAccessToken === 'string' && rcmsApiAccessToken.length > 0
 
         if (!authenticated) {
+            await dispatch('logout')
             throw new Error('need to login')
         }
 
         try {
             commit('setAccessTokenOnRequestHeader', { rcmsApiAccessToken })
             const profileRes = await this.$axios.$get('/rcms-api/9/profile')
             commit('setProfile', { profile: profileRes })
         } catch {
+            await dispatch('logout')
             throw new Error('need to login')
         }
     }

```

また、ニュース一覧画面を以下のように修正し、ログアウトボタンを作成します。

```diff
diff --git pages/news/index.vue pages/news/index.vue
index dcdd806..e79e075 100644
--- pages/news/index.vue
+++ pages/news/index.vue
@@ -1,23 +1,31 @@
 <template>
     <div>
         <p>ニュース一覧ページ</p>
+        <button type="button" @click="logout">
+            ログアウト
+        </button>
         <div v-for="n in response.list" :key="n.slug">
             <nuxt-link :to="`/news/${n.topics_id}`">
                 {{ n.ymd }} {{ n.subject }}
             </nuxt-link>
         </div>
     </div>
 </template>
 
 <script>
+import { mapActions } from 'vuex';
+
 export default {
     middleware: 'auth',
     async asyncData ({ $axios }) {
         return {
             response: await $axios.$get('/rcms-api/4/news'),
         };
     },
+    methods: {
+        ...mapActions(['logout'])
+    },
 };
 </script>

```

ログイン状態のニュース一覧画面にてログアウトボタンをクリックすると、下記となることを確認します。
- logoutエンドポイントへリクエストしている
- ログイン画面に遷移する
- そのままログインせずにニュース一覧画面へアクセスすると、ログイン画面に自動遷移される

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a1fc423b3d9bb866e38ec20091f21020.gif)
以上でAPIセキュリティが動的アクセストークンの場合のログイン処理の実装が完了です。

## 参考
以上でKurocoを利用したNuxt.jsプロジェクトで、ログイン画面の作成方法の紹介を終わります。

今回は基本的な説明のため、簡単にログイン画面を作成して最低限のログイン制御を実現しました。
実際に利用する際には、フォームのバリデーション処理や、`@nuxt/auth` などのライブラリをご利用いただく必要性が考えられますが、基本的なログイン構築の流れの理解としてご利用いただければ幸いです。

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form-nuxt2/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [profile APIの役割について](/ja/docs/faq/about-profile-api/)


---

# ログインする

> 元ページ: `tutorials/login` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/login/
> 概要: Kurocoログイン方法を説明します。

Kurocoログイン方法を説明します。

## ログイン画面へ遷移

ご自分のKuroco URL/management にアクセスします。  
ログイン画面が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffc6ba82742414c61c14d278ccbae1d4.png)
## ログイン

Kurocoに登録済のメールアドレス（またはログインID）とパスワードを入力し[ログイン]ボタンをクリックします。

## ログイン完了

ログインできている場合、管理画面トップページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/54dc7616053ef7d8a7a0ea1980f5b350.png)
ログインしていない場合はエラー画面が表示されるので、再度メールアドレスとパスワードを入力してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fcf83e8d6a9969b6b8582b00be787603.png)

## 関連ドキュメント
- [アカウント登録する](/ja/docs/tutorials/signup/)
- [アカウント設定](/ja/docs/management/account/)
- [Kuroco管理画面にワンタイムパスワードを利用した2要素認証を設定する](/ja/docs/tutorials/set-up-a-one-time-password-for-logging-into-the-kuroco-admin-panel/)
- [Kuroco管理画面でPasskeyを使用した二要素認証の設定方法](/ja/docs/tutorials/set-up-passkey-for-logging-into-the-kuroco-admin-panel/)
- [ログインロックについて教えてください。](/ja/docs/faq/what-causes-accounts-to-be-locked/)


---

# 新しいIPアドレスからログインがあった場合に通知を送る

> 元ページ: `tutorials/send-a-notification-when-there-is-a-login-from-a-new-ip-address` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/send-a-notification-when-there-is-a-login-from-a-new-ip-address/
> 概要: Kurocoは管理画面へのログイン履歴を取得するAPIを持っています。こちらのAPIを利用して新しいIPアドレスからログインがあった場合に通知を送る機能の実装方法を紹介します。

## 概要
Kurocoは管理画面へのログイン履歴を取得するAPIを持っています。
こちらのAPIを利用して新しいIPアドレスからログインがあった場合に通知を送る機能の実装方法を紹介します。  

### 学べること
以下の手順で新しいIPアドレスからのログインを検出し、通知を送ります。

- [APIを作成する](#apiを作成する)
- [カスタム処理を作成する](#カスタム処理を作成する)
- [動作確認をする](#動作確認をする)

## APIを作成する
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

### エンドポイントの作成
ログイン履歴を取得するエンドポイントはLoginHistory::listになります。

InternalのAPIから[新しいエンドポイントの追加]をクリックして作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

#### ログイン履歴を取得するエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|login_history|
|カテゴリー|認証|
|モデル|LoginHistory|
|オペレーション|list|
|self_only|チェックを入れる|
|login_type|0|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3048b81cc6e9725bca0548e272f948d5.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/30d7de262e6211027cb20345c44de02a.png)

## カスタム処理を作成する
エンドポイントの準備ができたら、カスタム処理を書いていきます。  

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックして、新しいIPアドレスからログインがあった場合に通知を送るカスタム処理を作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)
  

### 新しいIPアドレスからログインがあった場合に通知を送るカスタム処理
動作としてはまず、ログイン後処理のトリガを利用して、ログインがあった場合にそのIPアドレスを取得します。
次に、IPアドレスでフィルタをして過去のログイン履歴を取得し、結果が1件のみの場合は、新しいIPアドレスからのログインを検出したとして通知を送ります。

以下のように設定します。

|項目|値|
|:--|:--|
|タイトル|ip_address_login_alert|
|識別子|ip_address_login_alert|
|トリガ|ログイン後処理|
|処理|以下の内容|

```smarty
{* Retrieve information when logged in *}
{api_internal
    var='current_log'
    status_var='status'
    endpoint='/rcms-api/3/login_history'
    method='GET'
    use_current_session=1}

{* Retrieve other login histories with the same IP address *}
{* Refer to the second log (login_history_list[1]) because the api_internal retains the log. *}
{assign_array var='queries'            values=''}
{assign       var='queries.ip_address' value=$current_log.login_history_list[1].ip_address }

{api_internal
    var='log_history'
    status_var='status'
    endpoint='/rcms-api/3/login_history'
    method='GET'
    queries=$queries
    use_current_session=1}

{if $log_history.pageInfo.totalCnt == 1}
{capture name=mail_body}
A login from a new IP address has been detected.
Please verify if it was you.

IP Address: {$current_log.login_history_list[1].ip_address}
Date and Time: {$current_log.login_history_list[1].login_ymdhi}
Admin Panel URL: {$smarty.const.ROOT_MNG_URL}/management/
{/capture}

{sendmail 
 var='result'
 to=$smarty.session.email
 subject="Login detected from a new IP address."
 contents=$smarty.capture.mail_body}

{logger msg1="Login detected from a new IP address." msg2=$current_log.login_history_list[1]}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e457ed5aed09a28c9111d0e4ca902e3.png)

:::info
Smartyなどで内部的にログインをすると、`127.0.0.1`やKurocoのリクエスト元IPアドレスがログに残ります。  
上記のコードでも、認証ありの`api_internal`で内部ログインのログが残るため考慮して利用するデータを選択しています。  
Kurocoのリクエスト元IPアドレスを確認したい場合は[サポート](/ja/docs/about/support/)までご連絡ください。
:::

:::tip
[{logout}](/ja/docs/reference/smarty-plugin/#logout)のSmartyプラグインを設定すると強制的にログアウトさせることができます。  
ログイン許可IPをメンバー情報に持たせる等の対応と合わせて、新しいIPアドレスの認証機能を実装可能です。
:::

## 動作確認をする
以上で新しいIPアドレスからのログインを検出する設定は完了です。  
普段と違う環境からログインをして、通知が届くことを確認します。

想定通りに設定できていれば以下のように通知が届きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7da1dd2f6b9cf3fc6e0bc12683c6c9c4.png)

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# 会員制サンプルサイトで、開発環境と本番環境を分ける方法

> 元ページ: `tutorials/separating-development-and-production-environments-for-your-sample-membership-site` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/separating-development-and-production-environments-for-your-sample-membership-site/
> 概要: 開発環境と本番環境を分ける対応方法を学べます。開発環境と本番環境を分けることにより、変更や修正があった場合に本番サイトへの変更を公開する前に確認できます。

## 概要
本チュートリアルでは、開発環境と本番環境を分ける対応方法を学べます。  
開発環境と本番環境を分けることにより、変更や修正があった場合に本番サイトへの変更を公開する前に確認できます。

### 学べること
以下の流れで開発環境と本番環境を分けていきます。
- [独自ドメインの設定](#独自ドメインの設定)
- [GitHubの設定](#githubの設定)
- [GitHubActions用Buildファイルの修正](#githubactions用buildファイルの修正)
- [npm scriptの確認](#npm-scriptの確認)
- [envファイルの確認・修正](#envファイルの確認・修正)
- [動作確認](#動作確認)

### 前提条件
本チュートリアルは、オープンソースで公開している[会員制サンプルサイト](https://github.com/diverta/front_nuxt_auth)(NuxtAuthベースのKurocoFrontテンプレートサイト)をコピーしてサイトを構築をしていることが必要となります。  
まだサイト構築していない場合は、[会員制サンプルサイトをコピーして、Kurocoで会員制サイトを構築する方法](/ja/docs/tutorials/building-a-membership-website-on-kuroco-from-the-sample-site-template/)を参考に構築をお願いします。

また、今回は下記2種類の環境を用意することを前提としており、
開発する際の確認順序として、開発環境 -> 本番環境と段階的に確認/公開していく手順を想定しています。

- 開発環境
- 本番環境

GitHubにはそれぞれの環境に対応するブランチを作成し、それぞれのブランチが変更される度にGitHub Actionsが動作します。

それでは、自動でその対応する環境のフロントエンドが変更されるフローを設定していきます。

## 独自ドメインの設定

[KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)を参考に独自ドメインを設定してください。

また、今回は`フロントドメイン`と`APIドメイン`はサブドメイン関係(ドメインが一致する/ファーストパーティcookieとなる状態)に変更してください。
会員制サンプルサイトが利用しているCookieログイン方式においては、サードパーティcookie制限によりブラウザ/利用環境によってはcookieを維持できない可能性があるためです。

参考:[セキュリティ設定：Cookie で記事データを表示する](/ja/docs/tutorials/how-to-use-swagger-ui/#セキュリティ設定：cookie-で記事データを表示する)

## GitHubの設定

今回GitHubのリポジトリを上記2つのブランチに分ける必要があります。
下記のようにブランチを作成してください。

|項目   |ブランチ  |
| :--- | :--- |
| 本番環境 | main |
| 開発環境 | develop |

:::tip
ブランチの分け方は、[GitHub公式ドキュメント](https://docs.github.com/ja/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/managing-branches)を参照してください。  
:::

:::caution
想定外の本番環境への公開を防ぐために、mainブランチにはプロテクションをかけることをお勧めします。ブランチの保護の方法は、[GitHub公式ドキュメント](https://docs.github.com/ja/github/administering-a-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule)を参照してください。
:::

## envファイルの確認・修正
まずは、開発環境/本番環境の`./env.${environment}.js`ファイルを作成します。
今回は下記のように作成します。

- `env.development.js`
- `env.production.js`


```js title="env.production.js"
module.exports = {
    META_TITLE: 'Nuxt Auth',
    ROBOTS: 'index',
    BASE_URL: 'https://[独自APIドメイン]'
};
```

```js title="env.development.js"
module.exports = {
    META_TITLE: '[開発] Nuxt Auth',
    ROBOTS: 'noindex',
    BASE_URL: 'https://[独自APIドメイン]'
};
```

:::tip
独自APIドメインは、[独自ドメインの設定](#独自ドメインの設定)で設定した内容を記載してください。
:::

このように設定することで、下記を動的に変更します。
- 本番環境のMETA TITLE：Nuxt Auth
- 開発環境のMETA TITLE: [開発] Nuxt Auth

## nuxt.config.jsの修正
`nuxt.config.js`を以下のように修正します。

```js
const environment = process.env.APP_ENV; // <- (※1)
const envSettings = require(`./env.${environment}.js`); 

import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify';
export default defineNuxtConfig({
    runtimeConfig: {
        public: {
            kurocoApiDomain: 'https://dev-nuxt-auth.a.kuroco.app'
        }
    },

    app: {
        head: {
            title: envSettings.META_TITLE,  // <- (※2)
            htmlAttrs: {
                lang: 'ja'
            },
```

(※1)の箇所で、`APP_ENV`に指定された値によって、利用するenvSettingsの値を動的に変更します。  
- APP_ENV=development の場合は `require('./env.development.js')`
- APP_ENV=production の場合は `require('./env.production.js')`

例えば(※2)のMETAタイトルの値が、それぞれの`env.${environment}.js`ファイルから設定される仕組みになります。

APP_ENVはYAMLファイルで指定します。

## GitHubActions用Buildファイルの修正

既存の`/.github/workflow/build.yml`を修正し、develop/mainブランチでそれぞれ想定した動作をするように修正します。

下記を修正します。
- [develop/main用のbuild定義を作成する](#developmain用のbuild定義を作成する)
- [Buildファイルのイベントを変更する](#buildファイルのイベントを変更する)
- [ビルドとデプロイ先をそれぞれの環境用へ設定する](#ビルドとデプロイ先をそれぞれの環境用へ設定する)
- [開発用kuroco_front.jsonの適用](#開発環境用のkuroco_frontjsonを作成する)


### develop/main用のbuild定義を作成する
本番環境と開発環境用に２つのbuildファイルを作成します。  
今回は下記のファイルを作成します。

- 本番環境用: `.github/workflows/build.yml`
- 開発環境用: `.github/workflows/develop.yml`

`.github/workflows/build.yml`はすでに存在するので、こちらをコピーし`.github/workflows/develop.yml`を作成してください。

### ビルドとデプロイ先をそれぞれの環境用へ設定する
それぞれの環境に適したビルドを行うような動作へ変更修正します。

今回は下記のnpm scriptが動作するように修正します。
- 本番環境用はAPP_ENV=productionを指定
- 開発環境用はAPP_ENV=developmentを指定

まず、本番環境用の`.github/workflows/build.yml`でAPP_ENVをproductionに指定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eaff7bf02e1eb71918733997f52699a8.png)

```YAML title=".github/workflows/build.yml"
name: Build and deploy to Kuroco front
on:
  push:
    branches:
      - main
  issue_comment:
    types: [created, edited]
  workflow_dispatch:

env:
  APP_ENV: production

concurrency:
```

次に、開発環境用の`.github/workflows/develop.yml`を修正します。   
Kuroco管理画面より[外部システム連携] -> [GitHub]をクリックし、「GitHub Actions workflow file ステージングサイト」のテキストエリア内をコピーします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b1c730611960bf6093cec97e57c8f2b.png)

コピーした内容で`.github/workflows/develop.yml`ファイルを上書きします。

次に、`.github/workflows/develop.yml`でAPP_ENVをdevelopmentに指定します。

```YAML title=".github/workflows/develop.yml"
name: Build and deploy to Kuroco front
on:
  push:
    branches:
      - main
  issue_comment:
    types: [created, edited]
  workflow_dispatch:

env:
  APP_ENV: development

concurrency:
```

### Buildファイルのイベントを変更する
次にBuildファイルのイベントを変更します。
下記のように、それぞれのブランチが変更された時にだけイベントが発生するようにします。

- 本番環境：mainブランチが変更された時にのみイベント発生
- 開発環境：developブランチが変更された時のみイベント発生

今回は開発環境用の`.github/workflows/develop.yml`の以下画像の箇所を、下記のように修正します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/851fc47c4955463e2dd30b2851e6e9c8.png)

```YAML [.github/workflows/develop.yml]
name: Build and deploy to Kuroco front(develop)
on:
  push:
    branches:
      - develop
  issue_comment:
    types: [created, edited]
  workflow_dispatch:

env:
  APP_ENV: development

concurrency:
```

### 開発環境用のkuroco_front.jsonを作成する
次に、開発環境用にkuroco_front.jsonを作成します。
`/public` 配下の`kuroco_front.json`をコピーして、`kuroco_front_dev.json`を作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eaa88df7ebf2dccb12d6a0fd818c3252.png)

また、`develop.yml`のみに`kuroco_front_dev.json`を適用する必要があります。`develop.yml`に下記を追記します。

```diff
       - name: Checkout Repo
         uses: actions/checkout@v4
         with:
           ref: ${{ steps.get_branch.outputs.branch }}
+      - name: Copy kuroco_front.json
+        run:  cp public/kuroco_front_dev.json public/kuroco_front.json 
       - name: Use Node.js
         uses: actions/setup-node@v4
         with:
```

```diff
     steps:
       - name: Checkout Repo
         uses: actions/checkout@v4
+      - name: Copy kuroco_front.json
+        run:  cp public/kuroco_front_dev.json public/kuroco_front.json 
       - name: Use Node.js
         uses: actions/setup-node@v4
         with:
```

:::tip
kuroco_front.jsonについては、[kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)をご確認ください。
:::

以上で本番環境と開発環境の設定完了です。

## 動作確認
### ファイル構成の確認
それでは、ここまで設定した内容を確認します。  
YAMLファイルとkuroco_front.jsonは本番環境用、開発環境用にファイルで分けているので、mainブランチ、developブランチは共に以下のファイル構成になります。  

```
.github\workflows
  - build.yml
  - develop.yml
public
  - kuroco_front_dev.json
  - kuroco_front.json
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c990f6e43896d56102aad819d182ec37.png)

### ビルドの確認
それぞれの環境のPushが完了したら、GitHubの当該リポジトリにアクセスし、「Actions」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/247b06ff22179debabff76c01f2cb753.png)

動作中/動作終了したActions一覧が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/71c92f92e53e12f2a049c11055a57f7a.png)

ビルドが完了後、開発環境のMETA TITLEを確認いただくと、**[開発] Nuxt Auth** と表示されていることが確認できます。

以上で確認完了です。

## 関連ドキュメント
- [会員制サンプルサイトをコピーして、Kurocoで会員制サイトを構築する方法](/ja/docs/tutorials/building-a-membership-website-on-kuroco-from-the-sample-site-template/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [開発環境を作成する手順](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [ステージサイトにだけBasic認証をかけられますか？](/ja/docs/faq/can-i-use-basic-authentication-only-on-the-staging-site/)


---

# Kuroco管理画面にワンタイムパスワードを利用した2要素認証を設定する

> 元ページ: `tutorials/set-up-a-one-time-password-for-logging-into-the-kuroco-admin-panel` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/set-up-a-one-time-password-for-logging-into-the-kuroco-admin-panel/
> 概要: Kuroco管理画面へのログインに、ワンタイムパスワードを利用した2要素認証の設定が可能です。ワンタイムパスワードの発行にはGoogle Authenticatorを利用します。

## 概要
Kuroco管理画面へのログインに、ワンタイムパスワードを利用した2要素認証の設定が可能です。
ワンタイムパスワードの発行にはGoogle Authenticatorを利用します。

### 学べること
以下の手順でワンタイムパスワードを利用した2要素認証を設定します。
- [ワンタイムパスワードの利用設定をする](#ワンタイムパスワードの利用設定をする)
- [ワンタイムパスワードを登録する](#ワンタイムパスワードを登録する)
- [ワンタイムパスワードを利用必須にする](#ワンタイムパスワードを利用必須にする)
- [ワンタイムパスワードの解除方法](#ワンタイムパスワードの解除方法)

## ワンタイムパスワードの設定方法
ワンタイムパスワードは[環境設定]->[サイト管理]で利用の設定ができますが、
[必須]に設定した場合、ワンタイムパスワードの登録がない既存ユーザーはワンタイムパスワードを登録するまで管理画面にログインできなくなります。  

そこで本チュートリアルでは、一度ワンタイムパスワードの利用を[任意]に設定し、ユーザーそれぞれがワンタイムパスワードの登録を完了した後に[必須]の設定をする流れを紹介します。    

### ワンタイムパスワードの利用設定をする
[環境設定]->[サイト管理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/11e6419772c2d6258df0e6e98f227e01.png)

ログインの項目のワンタイムパスワードを[利用する]に設定します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/782b5eb20e42fc14840edf327cce67da.png)

### ワンタイムパスワードを登録する
ワンタイムパスワードは管理画面のメンバー設定から登録が可能です。
[メンバー管理]->[メンバー]から自身のメンバー情報に遷移するか、管理画面右上のアイコンから自身のメンバー情報に遷移します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6a612079b1f9b09d4fde7f7716c73f6.png)

ID情報タブからワンタイムパスワードの[設定する]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d7a5b20595ef61281e73dda3e6ec486.png)

ワンタイムパスワードの設定画面が開くので、[登録する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/74c042c775907c2278de2f102c9eafe5.png)

Google Authenticatorのアプリを開き、QRコードを読み込み、6桁の認証コードを入力します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5cff2ee8efceb36ef73380c48370d52.png)

ワンタイムパスワードの登録が完了し、メンバー情報に戻ったら設定は完了です。

次回ログインから、ID(もしくはメールアドレス)とパスワードの入力後、
ワンタイムパスワードの入力が必要になります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/118209f16f28243120ae12efe3cf8e17.png)

### ワンタイムパスワードを利用必須にする
最後に[環境設定]->[サイト管理]からワンタイムパスワードの設定を[必須]に変更します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/783a9cdcda75a2f8474946da02a733d4.png)

ワンタイムパスワードを登録していない既存ユーザーはワンタイムパスワードを登録するまで管理画面にログインできなくなり、ログイン時にはワンタイムパスワードの登録画面が表示されます。  
また、新規ユーザーは初回ログイン時にワンタイムパスワードの登録画面が表示されます。


:::tip
複数の二要素認証が必須に設定されている場合、必須設定された二要素認証のいずれかが必要となり、ユーザーは任意の認証方式を登録・利用できます。
:::

以上で、ワンタイムパスワードを利用した2要素認証の設定は完了です。

## ワンタイムパスワードの解除方法
Google Authenticatorをインストールした端末を紛失した場合など、ワンタイムパスワードの解除をしたい場合、対象のユーザーでは解除できません。  
サイトの管理者に連絡をして、管理者が管理画面のメンバー情報からワンタイムパスワードを解除してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7987f4483c0d832b82cc2bfdeee01fb0.png)

## 関連ドキュメント
- [サイト管理](/ja/docs/management/site-settings/)
- [メンバー](/ja/docs/management/member/)
- [Kuroco管理画面でPasskeyを使用した二要素認証の設定方法](/ja/docs/tutorials/set-up-passkey-for-logging-into-the-kuroco-admin-panel/)
- [ログイン画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-login-form/)


---

# Kuroco管理画面でPasskeyを使用した二要素認証の設定方法

> 元ページ: `tutorials/set-up-passkey-for-logging-into-the-kuroco-admin-panel` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/set-up-passkey-for-logging-into-the-kuroco-admin-panel/
> 概要: Kuroco管理者ログインでPasskeyを使用した二要素認証を設定することができます。パスワードまたはパスワードレスとして構成することも可能です。

## 概要

Kuroco管理者ログインでPasskeyを使用した二要素認証を設定することができます。パスワードまたはパスワードレスとして構成することも可能です。

### 学習内容

以下の手順に従って、Passkeyを使用した二要素認証の設定方法を学ぶことができます：

- [Passkeyの利用設定をする](#passkeyの利用設定をする)
- [Passkeyを登録する](#passkeyを登録する)
- [パスワードレスPasskeyの登録](#パスワードレスpasskeyの登録)
- [Passkeyの使用を必須にする](#passkeyの使用を必須にする)

## Passkeyの設定方法
Passkeyは[環境設定]->[サイト管理]で利用の設定ができますが、
[必須]に設定した場合、Passkeyの登録がない既存ユーザーはPasskeyを登録するまで管理画面にログインできなくなります。  
本チュートリアルでは、一度Passkeyの利用を任意に設定し、ユーザーそれぞれがPasskeyの登録を完了した後に[必須]の設定をする流れを紹介します。    

### Passkeyの利用設定をする

[環境設定]->[サイト管理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/11e6419772c2d6258df0e6e98f227e01.png)

ログインセクションでEnable Passkey Useを[利用する]に設定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/87ac8115fee2cdd9a84920abf7a7f040.png)

### Passkeyを登録する
Passkeyは管理画面のメンバー設定から登録が可能です。  
[メンバー管理]->[メンバー]から自身のメンバー情報に遷移するか、管理画面右上のアイコンから自身のメンバー情報に遷移します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6a612079b1f9b09d4fde7f7716c73f6.png)

ID情報タブからPasskeyの[設定する]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d679fc1ba1b310201b6a12151a3e3d4.png)

Passkeyの設定画面が開くので、[Register Passkey]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d53e43ff5cc757c6380dcd969d718726.png)

Passkeyの登録を促すメッセージが表示されます。  
実際の表示はデバイスによって異なります。例をいくつか挙げると、以下のようになります。

ソフトウェアベースのPasskey（Proton Password Managerなど）の場合：  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c352da8ecb4467f9f4309426b2c4f0a.png)

MacOSデバイスの場合、OSレベルのプロンプトが表示されます：  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1081f7fe68800863a26d1967a5562895.png)

ChromeなどのブラウザベースのPasskeyの場合：  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/57eb2e68131ec51a898480eaf78d88c8.png)

Passkeyの登録が完了し、メンバー情報に戻ったら設定は完了です。

複数のPasskeyを追加することができます。別のPasskeyを追加するには、[Register a new Passkey]をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/61931e833569469f42c65493000eb5eb.png)

追加したPasskeyにはそれぞれ別の名前を設定することができます。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f974098ba7c910bbafc12c6050aa667c.png)

Passkeyは一時的に無効にすることができます。特定のデバイスを使用していない場合に便利です。Passkeyを無効にするには、[有効]トグルをオフの位置に変更します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/36f0313a56d22eacc4d2158b0e48c8d6.png)

次回ログインから、ID(もしくはメールアドレス)とパスワードの入力後、登録されたPasskeyのいずれかで認証する必要があります。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8f877fbc296910afb09f391ed23f96c.png)

### パスワードレスPasskeyの登録

パスワードレスPasskeyを使用すると、ユーザーはユーザー名/メールアドレスとパスワードを入力する必要なくログインできます。まずサイト全体で許可する必要があります。[環境設定] -> [サイト管理] から、[Enable Passkey Use without LoginID-Password]の設定を有効にしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa5bf2f43c66a1f6bf3b8e74fa8443e7.png)

これにより、ユーザーは単にPasskeyを使用してログインできるようになります。ユーザーは既存のPasskeyをパスワードレスとして使用できるようにする必要があります。Passkey設定から[パスワードレスを使用]のトグルを有効に変更してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8ec146c01120ceb9f75893917540a73c.png)

新しく登録されたPasskeyは自動的にパスワードレスPasskeyとして登録されます。また、ユーザーはPasskey毎にパスワードレスの設定が可能です。

パスワードレスPasskeyを設定すると、ログイン画面に[Passwordless Passkey]のボタンが表示されますので、こちらからログインが可能です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/14b972440c48a5c66c8dd16a7a71dda5.png)

### Passkeyの使用を必須にする

最後に、[環境設定] -> [サイト管理] から、Passkeyの使用を[必須]に変更してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/143e4b875f0506b3db4d16b4f55dc585.png)

Passkeyを登録していない既存ユーザーはPasskeyを登録するまで管理画面にログインできなくなり、ログイン時にはPasskeyの登録画面が表示されます。  
また、新規ユーザーは初回ログイン時にPasskeyの登録画面が表示されます。

:::tip
複数の二要素認証が必須に設定されている場合、必須設定された二要素認証のいずれかが必要となり、ユーザーは任意の認証方式を登録・利用できます。
:::

以上で、Passkeyを使用した二要素認証の設定が完了しました。

## Passkeyの無効化方法

Passkeyとして使用していたデバイスを紛失した場合やPasskeyを無効にする必要がある場合、該当するユーザーとして自分で行うことはできません。

サイト管理者に連絡し、管理パネルのメンバー情報からPasskeyを無効にするように依頼してください。

すべてのPasskeyが削除されると、ユーザーはユーザー名/メールアドレスとパスワードだけでログインし、新しいPasskeyを登録できるようになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45bbec44ef0d5a968a39b71c60a74192.png)

## 関連ドキュメント
- [サイト管理](/ja/docs/management/site-settings/)
- [メンバー](/ja/docs/management/member/)
- [Kuroco管理画面にワンタイムパスワードを利用した2要素認証を設定する](/ja/docs/tutorials/set-up-a-one-time-password-for-logging-into-the-kuroco-admin-panel/)
- [ログイン画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-login-form/)


---

# 会員登録画面に仮登録機能を実装する

> 元ページ: `tutorials/setting-up-pre-member-registration-form` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-pre-member-registration-form/
> 概要: 新規会員登録時、登録メールアドレスあてに認証用のメールを送付する仮登録機能を実装します。仮登録メールのリンクから本登録画面にアクセスし、パスワードを設定して登録完了とする流れを想定します。

## 概要
新規会員登録時、登録メールアドレスあてに認証用のメールを送付する仮登録機能を実装します。
仮登録メールのリンクから本登録画面にアクセスし、パスワードを設定して登録完了とする流れを想定します。

### 学べること
仮登録機能は以下の手順で実装します。

- [APIの設定](#apiの設定)
- [Swagger UIで仮登録機能の動作を確認する](#swagger-uiで仮登録機能の動作を確認する)  
- [メッセージひな形を調整する](#メッセージひな形を調整する)  
- [フロントエンドの実装をする](#フロントエンドの実装をする)

### 前提条件
このページは、KurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  

:::info
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## APIの設定
まずは仮登録機能で使用するAPIを登録します。  

### API基本設定を行う
まずはAPIの登録をします。  
Kurocoの管理画面から[API]->[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5a0c3aacbb47a0e6c9fb95819d14622.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa425815fa52294d9cac473ad30f8128.png)

タイトル、版、ディスクリプションを入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/21f8d14592fbff6633975e6fd606c654.png)

追加したAPIに遷移しますので、続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e275e5521228b8a03413c147921479ee.png)

[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
注意)  
- セキュリティについては何らかの設定を適用してください。本チュートリアルでは、Cookieを利用します。
- Cookieをセキュリティ用のトークンとして利用する場合、APIドメインとフロントエンドのドメインが違うとサードパティクッキーの問題があり、Safari等で認証が効きません。<br/>フロントエンドとAPIドメインをサブドメイン違いで設定をする必要があるので、[独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)でAPIドメインを設定し、[アカウント設定](/ja/docs/management/account/)からAPIドメインを変更ください。<br/>（Chromeでは正常に動作しますので、開発やテストの段階ではまずChromeで構築していただくことをお勧めします。）


### CORS設定を行う
[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a340aa95db4871c92680d9e989a23c79.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000/`
- フロントエンドドメイン
- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22cf288dd0ba8dcf174e4f18ba4ab320.png)

問題なければ [保存する] をクリックします。

### エンドポイントを設定する
次にエンドポイントを作成します。今回は下記エンドポイントを作成します。  

- メンバー登録のエンドポイント
- 仮メンバー登録のエンドポイント

#### メンバー登録のエンドポイント
メンバー登録のエンドポイントを下記設定にて作成します。

|項目|設定内容|
| :--- | :--- |
|パス|member/regist|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|insert|
|default_group_id|適用するメンバーグループのIDを入力してください。<br/>グループIDは[グループ](/ja/docs/management/group/)より確認できます。|
|login_ok_flg|チェックを入れる|


![Image from Gyazo](https://t.gyazo.com/teams/diverta/1616a83c30db1b615eaddf7b2c6796e4.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c3c5531788d2c7f9b42c5a25ec011c9.png)

設定完了後、「追加する」をクリックします。

#### 仮メンバー登録のエンドポイント
仮メンバー登録のエンドポイントを下記設定にて作成します。

|項目|設定内容|
| :--- | :--- |
|パス|member/invite|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|invite|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/96414963ec58a04a1f022ca84269d3ac.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/84fde2ba57367028949bedfbe6ca5e97.png)

設定完了後、「追加する」をクリックします。

## Swagger UIで仮登録機能の動作を確認する
APIの設定ができたらまずはSwagger UIで動作の確認をします。

### Member::inviteのエンドポイントで招待メールを送る
[Swagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/19673279fafff52541ff9eb33398f77c.png)

[/rcms-api/13/member/invite]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a04b9da39163633dfc1df837f7cacd8a.jpg)

[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/622b531b111238a400c35643ef29207e.png)

Request bodyに以下のJSONデータを入力して[Execute]をクリックします。  
```json
{
  "email": "your_mail_address@example.com",
  "ext_info": {
    "name1": "Diverta",
    "name2": "Taro"
  }
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/470996856879963017772a63e6b5dc3b.png)

200のレスポンスと、メールの受信を確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b3e2519d955e13c8cf3c1bcbab6486ab.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6ac57aad2ff7efd5fdacdbb708148c7.jpg)

メールの本文は後ほど修正するので、今はデフォルトのままで問題ありません。  
URL末尾のkeyの部分が必要になるのでメモしておきます。  

### keyを利用して、仮メンバーの情報を取得する

:::info
仮登録メールに含まれるkeyには有効期限があります。デフォルトは720分（12時間）です。  
有効期限は、管理画面の[環境設定]->[サイト管理]にあるメンバーセクションの「招待メール有効期間」で変更できます。  
詳しくは[サイト管理](/ja/docs/management/site-settings/)を参照してください。
:::

先ほどメンバー情報をpostしたMember::inviteのエンドポイントに、今度は発行されたkey情報をpostします。  

Member::inviteのRequest bodyに以下のJSONデータを入力して[Execute]をクリックします。

```json
{
  "email_hash": "26576b6b123c88d891c76af61d9b57ae"
}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b87b26b60de455a3e0b6c0a0be3b6e11.png)

`email_hash`の値はご自身のサイトで発行したkeyを利用してください。  

すると、仮登録状態のメンバー情報がレスポンスされます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/95ed0cd19e0e32e6ce17b2796d7fc3f5.png)

こちらの情報を利用して会員登録をします。

### Member::insertのエンドポイントで会員登録をする
最後に、取得した仮メンバーの情報で会員登録のエンドポイントにリクエストして完了です。  

Swagger UIで[/rcms-api/13/member/regist]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e2b5c7882f5be1b5d14eb004e20b3fd.jpg)

[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e3e713fd9703abeea2e7c124c7ae699.png)

Request bodyに以下のJSONデータを入力して[Execute]をクリックします。  
login_pwdはAPIからではなく、本登録の画面で入力させる想定です。  

```json
{
  "email": "your_mail_address@example.com",
  "name1": "Diverta",
  "name2": "Taro",
  "login_pwd": "PASSWORD"
}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d196dcee32ef72ba291fd258e0807b6e.png)

メンバーの新規追加ができました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/270bcea30076ecb368d81cd535cbf979.png)

以上が仮登録機能の動作の流れになります。  
この一覧の流れをフロントエンドで実装します。  

## メッセージひな形を調整する
フロントエンドの実装の前に、Member::inviteのエンドポイントを叩いた際に送付されるメールの内容を調整しておきます。  

[オペレーション]->[メッセージひな形]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2234c8651dfa74abe9d7230dd2fb37c3.png)

識別子が`member/pre_regist_thanks`のテンプレートを探して、テンプレート名をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7165302c7eede81cfb5747886862d7fc.png)

メッセージひな形編集画面が開くので、以下のように修正して、[更新する]をクリックします。  
```smarty
RCMS-X-SUBJECT:{$smarty.const.SITE_TITLE}登録のご案内
{$ext_info.name1} {$ext_info.name2}様

弊社サイト{$smarty.const.SITE_TITLE} にご登録いただきありがとうございます。

以下のURLをクリックして登録を完了してください。  

■本登録用ページ
{$smarty.const.ROOT_URL}/login/signup_pre_regist/done/?key={$preregist_key}

よろしくお願い申し上げます。
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05862712b8d4170ec573e25ab607053f.png)

## フロントエンドの実装をする
最後に、以上の動作をするフロントエンドを作成します。

### 仮登録用のページ作成
/login/signup_pre_regist/のディレクトリで表示できるようにファイルを作成します。  

**Nuxt2:**

```markup reference title="/pages/login/signup_pre_regist/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/signup_pre_regist.vue
```

**Nuxt3:**

```markup reference title="/pages/login/signup_pre_regist/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/signup_pre_regist.vue
```


:::caution
`/rcms-api/33/member_invite`の部分はご自身のエンドポイントのURLに変更してください。  
以下同様に、ソースコード内のエンドポイントURLはご自身のエンドポイントURLに変更をお願いします。
:::

### 本登録用のページ作成
/login/signup_pre_regist/done/ のディレクトリで表示できるようにファイルを作成します。  

- keyがない場合や、keyの桁数が想定と異なる場合に404のページを表示します。
- keyをMember::inviteのエンドポイントにPOSTして、仮メンバーの情報を取得します。
- 取得した仮メンバーの情報とlogin_pwdを合わせてMember::insertのエンドポイントへ送付します。

**Nuxt2:**

```markup reference title="/pages/login/signup_pre_regist/done/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/signup_pre_registdone_done.vue
```

**Nuxt3:**

```markup reference title="/pages/login/signup_pre_regist/done/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/signup_pre_registdone_done.vue
```


### 動作確認
動作の確認をして、想定通りの動作でメンバーが登録できていることを確認します。  

#### 仮登録メール送信
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c07311e5e322a4804ead5c0231a38f0.gif)

#### 仮登録メールの内容確認
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a1975e30d4117e797211d9414e4d9a25.png)

#### 本登録
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3eafa7384b9802eeffd87e48280f3040.gif)

以上で、仮登録機能の実装が完了です。

## 関連ドキュメント
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)


---

# 新規会員登録画面を構築する

> 元ページ: `tutorials/setting-up-registration-form` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-registration-form/
> 概要: Kurocoを利用したNuxt.jsプロジェクトで、新規会員登録画面の作成方法を紹介します。

Kurocoを利用したNuxt.jsプロジェクトで、新規会員登録画面の作成方法を紹介します。

## 前提条件

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt3: v3.8.0
:::

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
          <input
            v-model="user.prop1"
            name="prop1"
            type="text"
            placeholder="prop1"
          />
        </div>
        <div>
          <label>prop2</label>
          <input
            v-model="user.prop2"
            name="prop2"
            type="text"
            placeholder="prop2"
          />
        </div>
        <div>
          <button type="submit">サインアップ</button>
        </div>
      </form>
    </div>
    <div v-if="signupDone">新規登録が完了しました。</div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const signupDone = ref(false);
const user = ref({});

const signup = () => {
  console.log(JSON.stringify(user.value, null, "\t"));
  signupDone.value = true;
};
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

```diff --git pages/login/signup/index.vue pages/login/signup/index.vue
index 92a23a3..c4be0d5 100644
--- pages/login/signup/index.vue
+++ pages/login/signup/index.vue
@@ -2,6 +2,9 @@
   <div>
     <div v-if="!signupDone">
       <form @submit.prevent="signup">
+        <p v-if="error" :style="{ color: 'red' }">
+          {{ error }}
+        </p>
         <div>
           <label>prop1</label>
           <input
@@ -34,10 +37,24 @@ import { ref } from "vue";

 const signupDone = ref(false);
 const user = ref({});
+const error = ref(null);
+const signup = async () => {
+  // Dummy request (success/fail after 1-second delay)
+  const shouldSuccess = true;
+  const request = new Promise((resolve, reject) =>
+    setTimeout(
+      () => (shouldSuccess ? resolve() : reject(Error("login failure"))),
+      1000
+    )
+  );

-const signup = () => {
-  console.log(JSON.stringify(user.value, null, "\t"));
-  signupDone.value = true;
+  try {
+    await request;
+    signupDone.value = true;
+  } catch (e) {
+    console.error(e);
+    error.value = "エラーが発生しました。";
+  }
 };
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
- const shouldSuccess = true;
+ const shouldSuccess = false;
```

ブラウザでサインアップすると、「エラーが発生しました。」と表示されます。

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
           {{ error }}
                 </p>
                 </p>
 
         </p>
 
         <div>
-          <label>prop1</label>
+          <label>name1</label>
           <input
-            v-model="user.prop1"
-            name="prop1"
+            v-model="user.name1"
+            name="name1"
             type="text"
-            placeholder="prop1"
+            placeholder="name1"
           />
         </div>
         <div>
-          <label>prop2</label>
+          <label>name2</label>
           <input
-            v-model="user.prop2"
-            name="prop2"
+            v-model="user.name2"
+            name="name2"
             type="text"
-            placeholder="prop2"
+            placeholder="name2"
+          />
+        </div>
+        <div>
+          <label>email</label>
+          <input
+            v-model="user.email"
+            name="email"
+            type="email"
+            placeholder="email"
+          />
+        </div>
+        <div>
+          <label>login_pwd</label>
+          <input
+            v-model="user.login_pwd"
+            name="login_pwd"
+            type="password"
+            placeholder="login_pwd"
           />
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
@@ -57,17 +57,24 @@ const signupDone = ref(false);
 const user = ref({});
 const error = ref(null);
 const signup = async () => {
-  // Dummy request (success/fail after 1-second delay)
-  const shouldSuccess = false;
-  const request = new Promise((resolve, reject) =>
-    setTimeout(
-      () => (shouldSuccess ? resolve() : reject(Error("login failure"))),
-      1000
-    )
-  );
-
   try {
-    await request;
+    const config = useRuntimeConfig();
+
+    // New member registration request using useFetch
+    const response = await fetch(
+      `${config.public.apiBase}/rcms-api/17/member/regist`,
+      {
+        method: "POST",
+        headers: {
+          "Content-Type": "application/json",
+        },
+        body: JSON.stringify(user.value), // Use the form content as the request body
+      }
+    );
+
+    if (!response.ok) {
+      throw new Error("Failed to register");
+    }
     signupDone.value = true;
   } catch (e) {
     console.error(e);

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
@@ -52,22 +52,48 @@

 <script setup>
 import { ref } from "vue";
+import { useRuntimeConfig } from "#app";

 const signupDone = ref(false);
 const user = ref({});
 const error = ref(null);
 const signup = async () => {
-  // Dummy request (success/fail after 1-second delay)
-  const shouldSuccess = false;
-  const request = new Promise((resolve, reject) =>
-    setTimeout(
-      () => (shouldSuccess ? resolve() : reject(Error("login failure"))),
-      1000
-    )
-  );
-
   try {
-    await request;
+    const config = useRuntimeConfig();
+
+    // Get AnonymousToken
+    const tokenRes = await fetch(`${config.public.apiBase}/rcms-api/17/token`, {
+      method: "POST",
+      headers: {
+        "Content-Type": "application/json",
+      },
+      body: "{}", // Empty object for AnonymousUser token request
+    });
+    const tokenData = await tokenRes.json();
+    const anonymousToken = tokenData.access_token.value;
+
+    // Create a custom header containing AnonymousToken.
+    const customHeaderConfig = {
+      headers: {
+        "X-RCMS-API-ACCESS-TOKEN": anonymousToken,
+      },
+    };
+
+    // Send new member registration request
+    const response = await fetch(
+      `${config.public.apiBase}/rcms-api/17/member/regist`,
+      {
+        method: "POST",
+        body: JSON.stringify(user.value), // Use the form content as the request body
+        headers: {
+          "Content-Type": "application/json",
+          ...customHeaderConfig.headers,
+        },
+      }
+    );
+    if (!response.ok) {
+      throw new Error("Failed to register");
+    }
     signupDone.value = true;
   } catch (e) {
     console.error(e);

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
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/)
- [会員登録画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-registration-form/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
