# Kurocoドキュメント: チュートリアル / フォーム・メール通知（2/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- フォーム画面を構築する（`setting-up-inquiry-forms`）
- フォーム画面(確認ページ付)を構築する（`setting-up-inquiry-forms-with-confirmation-page`）
- アカウント情報の表示・更新・削除画面を構築する（`setting-up-the-display-update-delete-screen-for-account-information`）
- Kurocoからのメール送信に任意のメール配信サービスを使用する(blastengine)（`use-any-email-delivery-service-to-send-emails-from-kuroco-blastengine`）
- Kurocoからのメール送信に任意のメール配信サービスを使用する(Mailchimp)（`use-any-email-delivery-service-to-send-emails-from-kuroco-mailchimp`）
- reCAPTCHAを利用したフォームを作成する（`using-recaptcha`）
- Webサイトのパフォーマンス改善について（`website-performance-tuning-with-kuroco`）


---

# フォーム画面を構築する

> 元ページ: `tutorials/setting-up-inquiry-forms` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-inquiry-forms/
> 概要: Kurocoを利用したプロジェクトで、フォームの利用方法を紹介します。

Kurocoを利用したプロジェクトで、フォームの利用方法を紹介します。

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

:::info
このページはKurocoでのプロジェクトが構築済みであることを前提としています。    
まだ構築していない場合は、下記のチュートリアルを参照してください。  
Nuxt.js：[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
:::

## Kurocoにおけるフォームとは

Kurocoにおけるフォームとは、HTMLフォームの作成支援のためのデータの定義、自動返信の設定、ユーザーから送信されたフォーム用データの閲覧などができる機能です。

フォームの設定は、管理画面の[チャネル]の[WEB]の[フォーム]から管理/設定ができます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

詳細は下記を参照してください。
- [フォーム一覧](/ja/docs/management/inquiry-forms/)
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [フォーム項目設定](/ja/docs/management/form-field-settings/)

フォームへの回答の送信はAPIを通して行われますので、各種設定とフロントエンド側のコーディングが必要となります。
この記事では、フロントエンドからKurocoのフォームに回答を送信する手順を紹介します。

## フォームのデータを作成する
### フォームを作成する
まず、フォーム定義を作成します。
[フォーム一覧](/ja/docs/management/inquiry-forms/)画面より、[フォーム追加]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4e6e66adf2ce4714165e2d1dc66cbf55.png)
新規フォーム作成画面が表示されるので、[フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)を参考に、動作確認用のフォーム定義を入力します。今回は下記のように設定しました。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f005733c55df20ba50ced6662fa6f983.png)

|項目   |値  |
| :--- | :--- |
|タイトル|テストフォーム|
|説明|説明です。<br/>説明です。<br/>説明です。|
|サンクス文言|サンクス文言です。<br/>サンクス文言です。<br/>サンクス文言です。|

最下部の[追加する]をクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c91ac4d0873c83447059560d5675d5c0.png)
自動で[フォーム一覧](/ja/docs/management/inquiry-forms/)画面に遷移し、入力したフォームが新規追加されていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2844158c724cfedeb22f604ac9b24c3a.png)

この画面に表示されている`ID`が、これから作成していく対象のフォームですので、メモをしておいてください。  

:::caution
ここでは`ID: 3`となっていますが、この値は自動採番のため、値は環境によって異なります。この後の操作は、実際に画面に表示された`ID`を使用してください。
:::

ここまででフォーム定義の作成は完了しました。

### フォームの設定を確認する
次に、先ほど作成したフォームの設定やデータを確認します。

#### 「項目設定」の確認
フォーム一覧画面より、作成した[テストフォーム]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/956d0878312778be9a91699ae33de87e.png)

フォーム基本設定画面が表示されるので、[項目設定]タブをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa7b1d569921dca3bbd93f0987629441.png)

[フォーム項目設定](/ja/docs/management/form-field-settings/)画面が表示されます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/36e49a5f2e340c1ad32d68c1076ba257.jpg)

この画面は、Kurocoが受け付けるフォーム項目を定義するものです。

「name」「email」「message」は、Kurocoで必須の項目のためあらかじめ設定されています。  
項目を追加したい場合は、ご自身で項目の定義を追加できます。  
[message]以下に空白の項目が見えていますが、必要に応じて、ここに項目を追加していきます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2b0fb2ff209878affbe106b5b816971.jpg)

今回はデフォルトの項目のみでフォームを作成しますので、項目の設定はこのままにしておいてください。  

#### 「回答」の確認
続いて[回答]タブをクリックすると、ユーザーから送信されたフォームの回答データの一覧が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/13d21b4addbcfd59e41be6c242a11992.png)

ここにはフォームに送信された回答が一覧で表示されます。  
(現在はまだデータが送信されていないため、0件で表示されています)  
回答内容などの詳細はこの画面や、右隣に隣接している[レポート]タブから確認できます。

## フォーム用のAPIを作成する
次に、作成したフォームに関するAPIを作成し、フロントエンドから回答の送信ができるように設定をします。  

### API基本設定を行う
Kurocoの管理画面から[API]->[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5a0c3aacbb47a0e6c9fb95819d14622.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa425815fa52294d9cac473ad30f8128.png)

タイトル、版、ディスクリプションを入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea58072fdb40851f7545a92f029e4daf.png)

追加したAPIに遷移しますので、続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/35fecb9c385fad0db7d495c215ca0776.png)

[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
注意)  
Cookieをセキュリティ用のトークンとして利用する場合、APIドメインとフロントエンドのドメインが違うとサードパティクッキーの問題があり、Safari等で認証が効きません。  
フロントエンドとAPIドメインをサブドメイン違いで設定をする必要があるので、[独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)でAPIドメインを設定し、[アカウント設定](/ja/docs/management/account/)からAPIドメインを変更ください。  
（Chromeでは正常に動作しますので、開発やテストの段階ではまずChromeで構築していただくことをお勧めします。）

### CORS設定を行う
[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c00d2e328ea75c53a3bada503227d7f5.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000/`
- フロントエンドドメイン
- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7181aee5dfb419ad133ad40295ae1ca.png)

問題なければ [保存する] をクリックします。

### エンドポイントを設定する

今回は下記2つのエンドポイントを作成します。
- フォーム定義を取得するエンドポイント: `(GET) form`
- データを送信するエンドポイント: `(POST) form`

#### フォーム定義を取得するエンドポイントを作成する
対象のAPI画面より [新しいエンドポイントの追加] をクリックます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdf6fc2ca42acee8dfee2403612f5755.png)

今回は下記設定にてエンドポイントを作成します。  

:::tip
ここでは簡易化のため、APIリクエスト制限はNoneを指定しています。  
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f3106d8a526f020ca8f02a9fd56d518f.png)

|項目|設定内容|
| :--- | :--- |
|パス|form|
|カテゴリー|フォーム|
|モデル|InquiryForm|
|オペレーション|details|
|APIリクエスト制限|None|

[追加する]をクリックしてエンドポイントを作成します。  

#### データを送信するエンドポイントを作成する
次に、HTMLから対象のフォームにデータを送信するためのエンドポイントを作成します。

対象のAPI画面より [新しいエンドポイントの追加] をクリックます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdf6fc2ca42acee8dfee2403612f5755.png)

今回は下記設定にてエンドポイントを作成します。

:::tip
ここでも同じく、APIリクエスト制限はNoneを指定してください。  
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b5adda5a81ba913819853c3fe0c35efd.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0574bb98ba2888c1baf41ec115d05ba.png)

|項目|設定内容|
| :--- | :--- |
|パス|form|
|カテゴリー|フォーム|
|モデル|InquiryMessage|
|オペレーション|send|
|APIリクエスト制限|None|
|id|送信先のフォームID (3)|

[追加する]をクリックしてエンドポイントを作成します。  

#### SwaggerUIで確認する
SwaggerUIにて、作成したフォーム定義を取得できるか確認します。
API画面より、[Swagger UI]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/759b45e26fce65607490c1e3241f27b4.png)

Swagger UI画面が表示されるので、先ほど作成したフォーム定義を取得するエンドポイントをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c3273ebdcdedb99763922400d36fac0f.png)

[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/468de26786c3584f0cf708e25e99d10a.png)

入力項目[inquiry_id]に、先ほど作成したフォームのIDを入力し(ここでは`3`を入力しています)、[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/af7e1e3f4d4767e80312fe7130380b16.jpg)

作成したフォーム定義がJSON化されて表示されることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6e6576387ac18cb1d3f5c03a7a37964.png)

次にPOSTの動作も確認します。

先ほど作成したInquiryMessage::sendのエンドポイントの[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71a1075e19f99d5fc1b9639fd92b718d.png)

Request bodyの項目に送信できるデータのサンプルが表示されているので、以下のJSONに編集して[Execute]をクリックします。

```json
{
  "name": "My Name",
  "email": "email@example.com",
  "body": "Example Message"
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f79f9a3e47ed48c115e442ffb703f915.png)

Kurocoのフォームに登録された回答のIDと、サンクス文言がレスポンスされます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/85d9d82625e6d892caf419cacae5b5a2.png)

回答を確認すると、送信したデータがKurocoに保存されていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d3d22d846fca11ed89cf3a22b5aa5020.png)

以上でフォーム用のエンドポイントが完成です。  

ここまでで以下の2種類のエンドポイントができました。
* フォーム定義を取得するエンドポイント: `(GET) form`
* フォームを送信するエンドポイント: `(POST) form`

では実際にこれらのエンドポイントを使用して、HTML上からフォームの作成と送信をしていきます。

## フロントエンドで、HTMLフォームを作成する

Nuxtインストールディレクトリに、下記構造のファイル追加作成します。  
今回は`/form/`のディレクトリでフォームが表示できるように、以下のファイルを作成します。

```
pages
 - form
   - index.vue 
```

追加したファイルに下記を記載します。

**Nuxt2:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/form_default.vue
```

**Nuxt3:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/form_default.vue
```


:::caution
`const FORM_ID = 3`の箇所は、ご自身の作成したフォーム定義のIDをご記入ください。  
:::

:::caution
`/rcms-api/8/form/${FORM_ID}`、`/rcms-api/8/form`の箇所は、Kuroco管理画面に記載のパスをご記入ください。
:::

### ブラウザで確認する
次に、先ほど作成したファイルをブラウザで確認します。
ローカルサーバーが停止している場合は`npm run dev`を実行し、`http://localhost:3000/form`にアクセスします。  
すると、下記画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3956415ec68ae145f18a4aadace5d4b7.png)

Chromeの開発者コンソールから、[Network]タブを確認すると、Kurocoと通信して、フォームの詳細情報を取得していることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b70e8a1ab89e71901ad7f6df015a756.png)

レスポンスされる情報の詳細は開発コンソールから確認するか、SwaggerUIを利用してKuroco管理画面から確認ください。  

### データを送信する
次に、実際にHTMLフォームからデータを送信します。    
各項目に下記のように値を入力します。

|項目名|入力値|
| :--- | :--- |
|Name|テスト名|
|Email|`test@example.com`|
|Message|テストメッセージ|

[submit]ボタンをクリックすると、データが送信されサンクス文言が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f39f6156021bed1df544b520069cd61.png)

ソースコード内「`handleOnSubmit()`」にあるように、この操作によって、[フォーム項目]のデータをKurocoにPOSTしました。  

POSTした内容も開発コンソールから確認できますので、うまく送信できない場合は、データの形式がSwaggerUIで確認した形式になっているか確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f75dee26aeb54d18fa4d3c4fd3b5276.png)

### データをKurocoで確認する。
次に、送信したデータをKurocoで確認します。  
フォーム一覧画面より、作成した[テストフォーム]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8fad490830faae8f08f597875970f8cd.png)

[回答]タブをクリックして、回答の一覧を表示すると、データが追加されていることを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/00e10acf329f6a8bb6949970179c3474.png)

[No.]をクリック(ここでは`14`)すると、回答内容の詳細を確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0e0807d9d967ae5d221355d00ff31691.jpg)

回答の詳細に、HTMLフォームから送信された値が含まれていることが確認できます。

### フォームのバリデーションを確認する
最後に、フォームのバリデーションを確認します。

先ほど作成したフロントの画面を再度表示し、[email]の項目に無効なメールアドレスを入力して、エラーが返却されることを確認します。

各行に以下を入力します。  
([email]の値は無効なメールアドレスですので、エラーとなることが望ましいです)  

|項目名|入力値|
| :--- | :--- |
|[name]|空欄|
|[email]|**mail**|
|[message]|空欄|

[submit]をクリックすると、画面上部にエラーメッセージが表示されます。  
開発コンソールでKurocoからのエラーメッセージも確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8267185496f53eaa32eeea1900de0b33.png)

このように、Kurocoにはサーバー側のバリデーションがあることを確認できます。  
エラー時はHTTPのステータスコードでのエラーと共に、レスポンスボディ内にエラー内容が返却されてきます。
ソースコード内にある通り、エラー時のハンドリングを実装したい場合には、フロント側でその実装をする必要があります。

:::tip
動的なバリデーションが必要な場合は、Kurocoから取得してきた値を元に実装が必要になります。
:::

## カスタム項目を追加する
デフォルトのフォーム項目以外に、自由にカスタム項目の定義/作成が可能です。  
カスタム項目を作成する場合の手順を確認します。

### カスタム項目追加手順
フォーム一覧画面より、作成した[テストフォーム]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8fad490830faae8f08f597875970f8cd.png)

[項目設定]タブをクリックして、[フォーム項目設定](/ja/docs/management/form-field-settings/)画面を表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/36e49a5f2e340c1ad32d68c1076ba257.jpg)

### 単一選択(セレクトボックス)を追加する。
例として、単一選択(セレクトボックス)を追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/58dba1aa68753596d498a6c139c6405b.png)

|項目名|入力値|
| :---- | :---- |
|タイトル|item|
|必須属性|任意|
|回答形態/入力制限|単一選択(セレクトボックス)|
|選択項目の設定|1::apple<br/>2::banana|

設定したら、画面下部の[更新する]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f07ff8b314eda7febfe1a0068fe4edea.png)

SwaggerUIを利用して、InquiryForm::details のエンドポイントのレスポンスに、追加したフォームの項目(ext_01)が含まれていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0edded8d7fe1af5ac5a4300adabdbe4e.png)

次にSwaggerUIを利用して、InquiryMessage::send のエンドポイントに`ext_01`の項目をどのようなデータ形式でPOSTすれば良いか確認します。    

SwagerUIのExample Value及びSchemaを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2da388f369aa6994d2c792f8d93983a1.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc60c5740b0ea6523f3a305d4b455260.png)

この場合、単一選択(セレクトボックス)は以下の形式のデータを受け付けます。

- `"ext_01": {"key": "1" , "label": "apple"}`
- `"ext_01": "1"`


確認した内容を元に、Kurocoから得たoptionsの内容を選択肢として表示し、セレクトボックスで選択されたkeyをPOSTするようにフロントエンドのコードを追加します。  

更新したコードは以下になります。

**Nuxt2:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/form_dropdown_selection.vue
```

**Nuxt3:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/form_dropdown_selection.vue
```


追加した項目が表示されることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/287636397a5adff301923b6130077263.png)

フォームを送信して、Kurocoに回答を登録できることを確認します。  
  
開発コンソールで、セレクトボックスで選択したkeyが`"ext_01":"1"`の形式でPOSTされていることを合わせて確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8b57505f2bff955e1472ca4e5467a4f.png)

### 日付の入力項目を追加する
続いて、日付の入力項目を追加してフォームを確認します。

#### 日付の入力項目をフォーム定義に追加する
既存で作成したフォーム定義の[項目設定]タブをクリックして、[フォーム項目設定](/ja/docs/management/form-field-settings/)画面を表示します。  
ここに日付のinput項目を追加定義します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/349525fc750bac75a162325b978fc0bd.png)

|項目名|入力値|
| :---- | :---- |
|タイトル|date|
|必須属性|任意|
|回答形態/入力制限|日付フォーマット|
|選択項目の設定|(なし)|

設定したら、画面下部の[更新する]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f07ff8b314eda7febfe1a0068fe4edea.png)

先ほどと同じようにSwaggerUIで項目の追加とPOSTするデータの形式を確認します。  
日付はString形式で`Y-m-d`でPOSTすることがわかるので、対応するようにindex.vueを修正します。  

**Nuxt2:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/form_date.vue
```

**Nuxt3:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/form_date.vue
```


Dateの項目に`1900/01/01`を入力してフォームを送信し、Kurocoに回答を登録できることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/12cd9b292a6ab68d8b0f5f4dac6ac864.png)

#### 日付の入力項目にバリデーションを設定する

項目にはKuroco側でのバリデーションを設定できます。  
今回は一例として、今現在から10年前までを許容範囲とするバリデーションを設定します。

作成したフォーム定義の[項目設定]から、[フォーム項目設定](/ja/docs/management/form-field-settings/)画面を表示します。  
[設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0401ccf1e0a96c113e16645b9b23dd4f.png)

設定画面にて、`開始までの期間`に`-10 years`を入力して設定、適用します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/87efcd3a1470a948712667bbe3c3e181.png)

:::tip
項目設定については、[フォーム定義で利用できるフォーム項目一覧 -> 日付フォーマット](/ja/docs/reference/form-field-list/#%E6%97%A5%E4%BB%98%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88)を参照してください。
:::

これでバリデーションが設定されましたので、10年前より以前の日付はエラーとなります。  
フロントエンドのフォーム画面から先ほどと同様に`1900-01-01`をリクエストして、失敗することを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d3c9c6c59abd69af95d233b14fdf559.png)

:::info
Kuroco側のバリデーションはあくまでバックエンド側のバリデーションです。  
フロントエンドでのバリデーションをさらに実施されたい場合には、ご自身で実装していただく必要があります。  
:::

:::tip
フォーム項目の設定で`年 (下限)`、`年 (上限)`を設定すると、InquiryForm::details のレスポンスのdetails.cols.ext_02.options で、選択肢となる年のリストが取得できます。  
こちらを利用して選択できる年を制限したり、セレクトボックスで年を選択させることも可能です。  
例えば、Kurocoのエンドポイントへのリクエストが`"ext_02":"1990-01-01"`の形式になっていれば、日付の項目をどんなタグで入力させても構いません。
:::

### ファイルの入力項目を追加する
カスタム項目のうち、ファイルの入力項目を追加してフォームを確認します。

#### ファイルの入力項目をフォーム定義に追加する

既存で作成したフォーム定義の[項目設定]タブをクリックして、[フォーム項目設定](/ja/docs/management/form-field-settings/)画面を表示します。  
ここにファイルのinput項目を追加定義します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ebff93420f8323510216f17263aa479.png)

|項目名|入力値|
| :---- | :---- |
|タイトル|file|
|必須属性|任意|
|回答形態/入力制限|ファイル(KurocoFiles)|
|拡張子の設定|（なし）|

設定したら、画面下部の[更新する]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f07ff8b314eda7febfe1a0068fe4edea.png)

#### アップロード用のエンドポイントを作成する

ファイルアップロードの実装は下記の流れとなります。
1. Kurocoへファイルをアップロードする
2. アップロードしたファイルIDを送信する

そのため、まずはアップロードの受け口となるエンドポイントを追加します。  
[API]より対象のAPIを選択し、API管理画面より [新しいエンドポイントの追加] をクリックます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdf6fc2ca42acee8dfee2403612f5755.png)

今回は下記設定にてエンドポイントを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a379f3ca20798fa4daf06a30b85552ae.png)

|項目|設定内容|
| :--- | :--- |
|パス|file|
|カテゴリー|ファイル|
|モデル|Files|
|オペレーション|upload|
|APIリクエスト制限|None|

:::tip
簡易化のため、APIリクエスト制限はNoneを指定しています。
:::

#### SwaggerUIで確認する
SwaggerUIにて、作成したフォーム定義を取得できるか確認します。
API画面より、[Swagger UI]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/759b45e26fce65607490c1e3241f27b4.png)

Swagger UI画面が表示されるので、先ほど作成したエンドポイントをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/619b015491ef49438cf7aeffa1ffca98.png)

[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0297503ec6adf1bab1f49fbb0efbe462.png)

入力項目[file]に、サンプルのファイルを選択し、[Execute]をクリックします。ここでは`kuroco.png`というロゴ画像を選択しました。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/22573d7a463010d712eca6fc9650e6cd.png)

ファイルがアップロードされ、一時領域にファイルが格納されます。`file_id`には、ファイルの格納先が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/065ff6b8d012661d7ec029d79ffd36d3.png)

:::note
ファイルアップロードの場合は、ヘッダーの指定が`'Content-Type: multipart/form-data'`になります。フロントエンドからPOST処理を行う場合に指定するように注意してください。
:::

なお、`file_id`にブラウザでアクセスすると、アップロードした画像が表示され、ファイルが格納されていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0e4b32f59f76f1a6c1673498c276d27c.png)

:::tip
確認先のURLは、`管理画面のホスト名 + file_id`です。
:::

この`file_id`をInquiryMessage::send のエンドポイントに送信すると、一時領域に格納されたファイルが、回答に紐づいてKurocoFilesに保存されます。  

以上でフォーム用のエンドポイントが完成しました。

#### フォームを修正してファイルを送信する。

次に、`pages/form/index.vue`を変更します。

以下が更新したコードです。

**Nuxt2:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/form_file.vue
```

**Nuxt3:**

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/form_file.vue
```


では実際に画像のアップロードとフォームデータ送信し、新しい[file]項目がKurocoに送信されることを確認します。  

フロント画面から画像ファイルをアップロードすると、アップロードしたタイミングで、Files::upload のエンドポイントにリクエストが送付され、`file_id`を取得したことを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1480ae74fa1f1820aad0c9bd7ae1b5f8.png)

次に、必須項目を入力して、[submit]をクリックすると、`file_id`をInquiryMessage::send のエンドポイントにPOSTしたことが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5e2cc4403bcb370fc79ef2434319af26.png)

管理画面の[フォーム]から[回答]タブをクリックして回答の一覧を表示し、データが追加されていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bf63e7001a98148be2248e186c3623e2.png)

[No.]をクリック(ここでは`31`)して詳細を表示すると、新規追加した項目[file]と、その項目に入力した値が適用されていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e1f5282470c1dd990014d184fbca2ec1.jpg)

## 参考
本チュートリアルでは簡易化のため、Kurocoの各項目に対応したHTMLをフロントエンドで書いています。そのため、Kurocoの項目設定を変更するとフロントエンドのコードも更新が必要です。

Kurocoの項目設定に合わせてフロントエンドの表示を動的に変更する場合は、InquiryForm::detailsのレスポンスに含まれる`type`を利用して出し分けしてください。  

詳しくはコーポレートサンプルサイトのリポジトリを参照してください。  
https://github.com/diverta/front_nuxt_corporate/blob/main/pages/contact/index.vue

## 関連ドキュメント
- [フォーム一覧](/ja/docs/management/inquiry-forms/)
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [フォーム画面(確認ページ付)を構築する](/ja/docs/tutorials/setting-up-inquiry-forms-with-confirmation-page/)
- [reCAPTCHAを利用したフォームを作成する](/ja/docs/tutorials/using-recaptcha/)
- [フォーム定義で利用できるフォーム項目一覧](/ja/docs/reference/form-field-list/)


---

# フォーム画面(確認ページ付)を構築する

> 元ページ: `tutorials/setting-up-inquiry-forms-with-confirmation-page` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-inquiry-forms-with-confirmation-page/
> 概要: Kurocoを利用したプロジェクトで、入力内容の確認ページを含んだフォームの作成方法を紹介します。本チュートリアルでは、デフォルトの項目(名前、メールアドレス、問い合わせ内容)のみのシンプルなフォームを作成します。

## 概要
Kurocoを利用したプロジェクトで、入力内容の確認ページを含んだフォームの作成方法を紹介します。  
フォームは、デフォルトの項目(名前、メールアドレス、問い合わせ内容)のみのシンプルなフォームを作成し、  
フロントエンドのコードとして、Nuxt.jsを紹介します。

追加項目の実装方法は[KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/#カスタム項目を追加する)を参照してください。

### 学べること
以下の手順で確認ページ付きのフォームを作成します。
- [フォームを作成する](#フォームを作成する)
- [エンドポイントを作成する](#エンドポイントを作成する)
- [フロントエンドの実装をする](#フロントエンドの実装をする)

### 前提条件
:::info
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## フォームを作成する
まずは、回答を受け付けるフォームを作成します。  
[チャネル] -> [WEB] -> [フォーム]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧から[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/19b2303d90338e3d3cea6b87e149712e.png)

デフォルトの設定のまま[追加する]をクリックしてフォームを追加します。  
追加したフォームIDは後ほど使うのでメモしてください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/829c31307bf96193a55d38c3ffe4873b.png)

## エンドポイントを作成する
APIページから、[新しいエンドポイントの追加]をクリックして、フォームのバリデーションを行うエンドポイントとフォームの送信をするエンドポイントの2つを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4968a6df7132b965957098116b1daefd.png)

### バリデーションを行うエンドポイント

以下の設定でエンドポイントを作成します。  

|項目|設定内容|
| :--- | :--- |
|パス|form_validate|
|カテゴリー|フォーム|
|モデル|InquiryMessage|
|オペレーション|send|
|id|利用するフォームのID(16)|
|validation_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c62f32eb18b48eb727d1ecbee992f89b.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/86d20c0bb3cde41d964fbf1590a0dc5c.png)

入力ができたら[追加する]をクリックしてエンドポイントを作成します。  

### フォームの送信を行うエンドポイント

以下の設定でエンドポイントを作成します。  

|項目|設定内容|
| :--- | :--- |
|パス|form_send|
|カテゴリー|フォーム|
|モデル|InquiryMessage|
|オペレーション|send|
|id|利用するフォームのID(16)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe96d2287a98a615b0052c8dfba94a8f.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a78adeffe9f3b5dfe61f569864466a36.png)

入力ができたら[追加する]をクリックしてエンドポイントを作成します。  

### SwaggerUIで確認する
SwaggerUIで、フォームのバリデーションを行うエンドポイントが動作するかを確認します。
APIページより、[Swagger UI]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/229b94677de655efe05b3a5a5c466a8b.png)

先ほど作成した`/form_validate`を選択し、[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1da5922ff21e7947ecfcaa5060daf6fc.png)

Request bodyに以下を入力して、[Execute]をクリックします。

```json
{
  "email": "test"
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c7ac31d451b318cfe75841243392286.png)


レスポンスコード422が返ってくることと、`errors`にエラー内容が表示されていることを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/23d45df7aa9e1939a4772fd37f032f69.png)

次に、Request bodyに以下を入力し、[Execute]をクリックします。

```json
{
    "name":"Diverta Taro",
    "email":"example@example.com",
    "body":"this is test message"
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a2bcda0ee3e6c585d9671b523774af6.png)

レスポンスコード200が返って来ますが、`id`が`null`になっており、フォームの回答は追加されていないことを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4e6aef498f750f3f9ff7db9dd37d9a8.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/86601a0ace21d732437913798dec1585.png)

こちらを利用して、バリデーション用のエンドポイントにリクエストを送り、200のレスポンスコードが返ってきた場合に確認画面を表示するようフロントエンドを実装します。

## フロントエンドの実装をする
### ファイルを追加する
フォームのページを以下のコードで追加します。

**Nuxt2:**

```markup reference title="/pages/form_with_confirmation_page/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/form_with_confirmation_page.vue
```

**Nuxt3:**

```markup reference title="/pages/form_with_confirmation_page/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/form_with_confirmation_page.vue
```


### ブラウザで確認する
次に、先ほど作成したページをブラウザで確認します。
ローカルサーバーが停止している場合は`npm run dev`を実行し、`http://localhost:3000/form_with_confirmation_page`にアクセスします。  

入力画面で必須項目を空白にして[入力内容の確認]をクリックすると、エラーが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3df406d93e01fc00f650a36918167132.gif)

必要項目を入力して[入力内容の確認]をクリックすると、確認画面が表示されます。デザインは任意のものをあててください。  
この画面で[送信]をクリックすると、問い合わせが送信されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14b3e75919049fabcd50321e07319926.gif)

以上で確認ページ付の問い合わせフォームの作成が完了しました。

## 関連ドキュメント
- [チュートリアル：KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)


---

# アカウント情報の表示・更新・削除画面を構築する

> 元ページ: `tutorials/setting-up-the-display-update-delete-screen-for-account-information` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-the-display-update-delete-screen-for-account-information/
> 概要: Kurocoを利用したNuxt.jsプロジェクトで、アカウント情報の表示・更新・削除画面の作成方法を紹介します。

## 概要
Kurocoを利用したNuxt.jsプロジェクトで、アカウント情報の表示・更新・削除画面の作成方法を紹介します。

### 学べること
以下の手順でアカウント情報の表示・更新・削除画面を作成します。
- [エンドポイントを設定する](#エンドポイントを設定する)
- [フロントエンドを実装する](#フロントエンドを実装する)
  - [自身のメンバー情報の表示](#自身のメンバー情報の表示)
  - [自身のメンバー情報の更新](#自身のメンバー情報の更新)
  - [自身のメンバー情報の削除](#自身のメンバー情報の削除)

### 前提条件
:::info
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、ログイン画面の実装がされていることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## エンドポイントを設定する
エンドポイントは Login::login_challenge のエンドポイントが設定されたAPI設定に追加します。  
そうすることでログインした認証情報を利用してエンドポイントへのリクエストが行われます。
異なるAPI間で認証情報は共有できませんので注意してください。

今回はメンバー情報を表示するエンドポイントと、メンバー情報を更新するエンドポイント、そしてメンバー情報を削除するエンドポイントの3つを設定します。 
いずれも`self_only`のパラメータを有効にすることで、自身のメンバー情報のみにアクセスできるよう制限します。  

[新しいエンドポイントの追加]をクリックして、それぞれ作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e20df3e56291487f859a3cbd905b261.png)

**メンバー情報を表示するエンドポイント**

|項目|設定内容|
| :--- | :--- |
|パス|member/details|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|details|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d3e6adf9a7578add039563bf16a2411d.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/64cb3bfbe1738ea841babbcf49cd98d7.png)

:::caution
self_onlyのパラメータを有効にしない場合、エンドポイントのURLが分かれば誰でも任意のメンバー情報を取得できます。  
その場合は、エンドポイントにAPIリクエスト制限をかけてリクエストを送付できるユーザーを制限してください。`custom_search_id`や`group_id`のパラメータを設定して、エンドポイントから取得できるメンバーを制限したり、後処理の[出力許可リスト](/ja/docs/reference/post-processing/#出力許可リスト)を使用して、レスポンスされる項目を絞る方法も有効です。  
:::

**メンバー情報を更新するエンドポイント**

|項目|設定内容|
| :--- | :--- |
|パス|member/update|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|update|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a87acd800d2f0e766b0c2e6e88cae9c.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0e862ce849e1c5bc56562573d2a80466.png)

:::caution
self_onlyのパラメータを有効にしない場合、APIリクエストが許可されたユーザーであれば他人のメンバー情報を更新できます。
APIリクエストを許可するユーザーを注意して設定するとともに、以下のパラメータ設定も併用してください。
- `allowed_group_ids`：所属グループを変更するリクエストを送る場合、このパラメータに設定されたグループIDのみ変更できるよう制限します。
- `use_columns`：このパラメータに設定されたkeyの項目のみ更新できるよう制限します。
- `unuse_columns`：このパラメータに設定されたkeyの項目は更新できないよう制限します。
:::

**メンバー情報を削除するエンドポイント**

|項目|設定内容|
| :--- | :--- |
|パス|member/delete|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|delete|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b1bd94ae2131d1e92e669e14540582a.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b0272f79240c4fa210ab5b32b952b641.png)

:::caution
self_onlyのパラメータを有効にしない場合、APIリクエストが許可されたユーザーであれば他人のメンバー情報を削除できます。  
APIリクエスト制限の設定でAPIリクエストを送付できるユーザーを制限し、`allowed_group_ids`のパラメータ設定で削除できるユーザーをグループで制限してください。
:::

## フロントエンドを実装する
### 自身のメンバー情報の表示
まずは自信のメンバー情報を取得し、表示する画面を作成します。

以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/mypage/details/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/member_detail.vue
```

**Nuxt3:**

```markup reference title="/pages/mypage/details/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/member_detail.vue
```


ログイン後に対象のディレクトリにアクセスすると、メンバー情報の表示が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c748080eee7923fe52c4e4f5b1284dd.png)

### 自身のメンバー情報の更新

以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/mypage/update/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/member_update.vue
```

**Nuxt3:**

```markup reference title="/pages/mypage/update/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/member_update.vue
```


ログイン後に対象のディレクトリにアクセスすると、メンバー情報の入力ができ、[Update]ボタンをクリックすることで更新できることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a17a2a53667018250bcd8ada73794d66.gif)

### 自身のメンバー情報の削除

以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/mypage/delete/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/member_delete.vue
```

**Nuxt3:**

```markup reference title="/pages/mypage/delete/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/member_delete.vue
```


ログイン後に対象のディレクトリにアクセスすると、削除直前の警告文章が表示され、[Proceed]ボタンをクリックすると自身の情報を削除できることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a103565a00aba2e1098b4490a5bbbee.gif)

以上でアカウント情報の表示・更新・削除の動作が実装できました。  
チュートリアルでは最低限の項目の表示・更新としていますので、必要な要件に合わせて表示する項目も調整してください。  

## 関連ドキュメント
- [メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)


---

# Kurocoからのメール送信に任意のメール配信サービスを使用する(blastengine)

> 元ページ: `tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-blastengine` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-blastengine/
> 概要: トリガ「デフォルトのメール送信方法（SendGrid）を代替」を利用すると、SendGridの代わりに、blastengine、Mailchimp、Amazon SESなどの任意のメール配信サービスを利用して、通知や招待のメールを送信できます。本チュートリアルではその例として、SendGridによるメール送信をblastengineに代替する手順を紹介します。

## 概要
トリガ「デフォルトのメール送信方法（SendGrid）を代替」を利用すると、SendGridの代わりに、blastengine、Mailchimp、Amazon SESなどの任意のメール配信サービスを利用して、通知や招待のメールを送信できます。  

本チュートリアルではその例として、SendGridによるメール送信をblastengineに代替する手順を紹介します。

### 学べること
以下の手順で任意のメール配信サービスを使用したメール送信を実装します。
- [blastengineの設定](#blastengineの設定)
- [Kurocoの設定](#kurocoの設定)
- [動作の確認](#動作の確認)
- [メールの到達率を上げる](#メールの到達率を上げる)

### 前提条件
:::info
本チュートリアルではメールの送信にblastengine（ブラストエンジン）を使用します。  
サービスの詳細は[blastengine](https://blastengine.jp/)とその[APIドキュメント](https://blastengine.jp/documents/)を確認してください。  

また、SPF/DKIMの設定をするのでfromのメールに使用するドメインは自身が所有しているものを利用することとします。
:::

:::caution
SendGridを利用しない場合、配信の[トラッキング機能](/ja/docs/management/notification-tracking/)(配信、メールバウンス、開封率、クリック数)はご利用できませんのでご注意ください。
:::

:::caution
SendGridを利用しない場合、メール送信リクエストの記録は[メールログ](/ja/docs/management/mail-log-list/)ではなく、[APIリクエストログ](/ja/docs/management/api-request-log-list/)に保存されます。ログの詳細は、SendGridを利用した場合と同様に、ご利用のメール配信サービス側のログをご確認ください。
:::

## blastengineの設定
まずは[blastengine](https://blastengine.jp/)にアクセスして、無料トライアルに登録します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e342dee64d1605373031dbcc3e0602f0.png)

トライアルアカウントにログインしたら[API連携で試す]タブの[アドレス登録]をクリックして、blastengineからの配信を許可するアドレスを入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/24730e7df6d12a0f28cc719581c3a0c1.png)

続いて、APIキーの取得をします。  
[設定ページ]をクリックしてblastengineの設定ページに遷移します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3152f3a91b517ab3853739f4815f27a1.png)

APIキーの[確認・再発行]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/924c4a21ee53270cdab9b9374f4aae6b.png)

APIキーが表示されるのでメモします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3150681ecd00867e78e1db73956812e9.png)

また、[アカウント管理](https://app.engn.jp/be/admin/account)のページにアクセスし、IDをメモします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e7ec78852bf9b7eb06c055ecf07586a.png)

## Kurocoの設定
### シークレットを登録する
Kurocoの管理画面にアクセスし、[環境設定] -> [シークレット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/25b831fd4835ad993f02298629b9e8cf.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c51de1ecc8ead6fa837c6492757a7276.png)

以下のblastengineの管理画面で確認したAPIキーと、IDを登録します。

|項目|値|
|:--|:--|
|名前|BLASTENGINE_API_KEY|
|値|blastengineのAPIキー|

|項目|値|
|:--|:--|
|名前|BLASTENGINE_ID|
|値|blastengineのID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e74f1f77c4739eb2ce2ebab7d404ac63.png)

以上でblastengineを利用する準備が整いました。

### カスタム処理を登録する
blastengineを利用する準備ができたら、SendGridによるメール送信をblastengineに代替するカスタム処理を書きます。

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

以下のように設定します。

|項目|値|
|:--|:--|
|タイトル|sending_email_with_blastengine|
|識別子|sending_email_with_blastengine|
|トリガ|デフォルトのメール送信方法（SendGrid）を代替|
|処理|以下の内容|

```smarty title="sending_email_with_blastengine"
{* Create BearerToken *}
{secret var='apiKey' key='BLASTENGINE_API_KEY'}
{secret var='id' key='BLASTENGINE_ID'}
{rcms_hash var='token' data="`$id``$apiKey`" algo="sha256"}
{assign var='BearerToken' value=$token|strtolower|base64_encode}

{* Set Request Headers *}
{append var=headers value="Authorization: Bearer `$BearerToken`"}
{append var=headers value="Content-Type: application/json"}
{append var=headers value="Accept-Language: ja-JP"}

{* Set Body *}
{assign var='body' value=$payload|@json_decode}
{assign var='body.from.email' value="noreply@kuroco-mail.app"}

{* Send Request *}
{api
    endpoint="https://app.engn.jp/api/v1/deliveries/transaction"
    method='POST'
    headers=$headers
    body=$body
    var=response
    status_var=status
}

{logger msg1="blastengine_mail_log" msg2=$body msg3=$response}
{assign var='is_mail_sent' value=true}
```

:::caution
`noreply@kuroco-mail.app`の部分は自身のメールアドレスに変更してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/28478906d91560352ad8a09951298cef.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

## 動作の確認
実際にKurocoからのメールを送信してみます。  
動作の確認のため、パスワードリマインダーを使用してみます。

Kurocoのログイン画面にアクセスし、[パスワードを忘れた場合はこちら]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f585084835c88fda19163c26eabdf5f.png)

blastengineからの配信を許可したメールアドレスを入力して、[送信する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71089ec62b43826f3812de3f23ef7194.png)

届いたメールを確認すると、fromがカスタム処理内のメールアドレスになっており、`besender-s.jp 経由`の表示が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3da9e6d15f41149ec177a463419b6f0.png)

また、blastengineの[配信ログ](https://app.engn.jp/be/admin/logs)を確認すると、該当のメールがblastengineから送られたことが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c89ebbece9c5035d88769182c3e5349.png)

## メールの到達率を上げる
ここまでで、blastengineを利用したメールの送信はできていますが、
送信したメールが迷惑メールと判断されるのを防ぐために、SPFレコードとDKIMの設定をしてメール認証を実施します。  

メール認証を実施することで、メールのなりすましを防ぎ、実際にメールを送信したのがドメイン所有者であると判断できます。  

SPF/DKIMの設定がされていないメールに対する処理が年々厳しくなっていますので必ず実施するようにしてください。

:::info
- [メール送信者のガイドライン](https://support.google.com/mail/answer/81126)
- [SPF認証が必要な理由と設定方法](https://blastengine.jp/blog_content/spf_basic/)
- [【図解】初めてでも腹落ち！DKIMの仕組みと設定方法](https://blastengine.jp/blog_content/dkim_basic/)
:::

### SPFレコードを設定する

ドメイン管理サービスで以下のTXTレコードを設定します。


|ホスト名|TYPE|VALUE|
|:--|:--|:--|
|空欄|TXT|v=spf1 include:spf.besender.jp ~all|

設定ができたら[MxToolboxのSPF Record Check](https://mxtoolbox.com/spf.aspx)で、正しく設定されているか確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/84c9f0f754fcddd12ff14b38369d25d4.png)

### DKIMを設定する
次にDKIMの設定をします。  
まず、公開鍵・秘密鍵のペアを準備し、blastengineに秘密鍵を設定します。  

#### 秘密鍵・公開鍵の生成
秘密鍵はローカル環境でOpenSSLのコマンドラインツールを使用して、生成します。  
まず、ターミナル開いて以下のコマンドでOpenSSLが利用可能か確認します。  

```bash
openssl version
```

:::info
Windowsの場合などでOpenSSLがインストールされていない場合は別途インストールしてください。
:::

次に以下のコマンドで秘密鍵を作成します。  

```bash
openssl genpkey -algorithm RSA -out private_key.pem
```

公開鍵は、OpenSSLを使用して、秘密鍵から抽出します。  
以下がそのコマンドです。

```bash
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

#### blastengineに登録
作成した秘密鍵をblastengineに登録します。    

blastengineの[設定ページ](https://app.engn.jp/be/admin/settings)にアクセスしてDKIM作成者署名の設定の[確認・変更]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/792b66373c8baaa13115e040809cd4f4.png)

DKIM作成者署名の設定が表示されるので、新規登録をクリックし、以下を設定します。

|項目|値|
|:--|:--|
|セレクタ|kuroco|
|ドメイン|fromメールで利用するドメイン|
|秘密鍵|先ほど作成した`-----BEGIN PRIVATE KEY-----`から始まる秘密鍵|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae34738520eca91c1f75de8e78e785d2.png)

入力が完了したら[確認]をクリックして登録します。  

#### DNSを設定
ドメイン管理サービスで以下のTXTレコードを設定します。

|ホスト名|TYPE|VALUE|
|:--|:--|:--|
|kuroco._domainkey|TXT|v=DKIM1; k=rsa; p=`公開鍵の-----BEGIN PUBLIC KEY-----と-----END PUBLIC KEY-----を抜いた部分`|

:::caution
VALUEの長さが設定できる文字数を超える場合はTXTレコードを分割して登録する必要があります。  
対応が必要な場合はドメイン管理サービスに問い合わせて設定してください。
:::

設定ができたら[MxToolboxのDKIM Record Lookup](https://mxtoolbox.com/dkim.aspx)で、正しく設定されているか確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/38fcf2313f9de8c460af71b5773b6f97.png)

再度Kurocoからのメールを送信して確認すると、fromがカスタム処理内のメールアドレスになっており、今度は`besender-s.jp 経由`の表示が無いことを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/caed71f08b416c58117d17a481fbef70.png)

以上で、任意のメール配信サービスを利用する設定は完了です。

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)


---

# Kurocoからのメール送信に任意のメール配信サービスを使用する(Mailchimp)

> 元ページ: `tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-mailchimp` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-mailchimp/
> 概要: トリガ「デフォルトのメール送信方法（SendGrid）を代替」を利用すると、SendGridの代わりに、blastengine、Mailchimp、Amazon SESなどの任意のメール配信サービスを利用して、通知や招待のメールを送信できます。本チュートリアルではその例として、SendGridによるメール送信をMailchimpに代替する手順を紹介します。

## 概要
トリガ「デフォルトのメール送信方法（SendGrid）を代替」を利用すると、SendGridの代わりに、blastengine、Mailchimp、Amazon SESなどの任意のメール配信サービスを利用して、通知や招待のメールを送信できます。  

本チュートリアルではその例として、SendGridによるメール送信をMailchimpに代替する手順を紹介します。

### 学べること
以下の手順で任意のメール配信サービスを使用したメール送信を実装します。
- [Mailchimpの設定](#mailchimpの設定)
- [Kurocoの設定](#kurocoの設定)
- [動作の確認](#動作の確認)

### 前提条件

:::info
本チュートリアルではメールの送信にMailchimpのTransactional APIを使用します。  
サービスの詳細は[Mailchimp](https://mailchimp.com/)とその[APIドキュメント](https://mailchimp.com/developer/transactional/guides/quick-start/)を確認してください。  

また、SPF/DKIMの設定をするのでfromのメールに使用するドメインは自身が所有しているものを利用することとします。
:::

:::caution
SendGridを利用しない場合、配信の[トラッキング機能](/ja/docs/management/notification-tracking/)(配信、メールバウンス、開封率、クリック数)はご利用できませんのでご注意ください。
:::

:::caution
SendGridを利用しない場合、メール送信リクエストの記録は[メールログ](/ja/docs/management/mail-log-list/)ではなく、[APIリクエストログ](/ja/docs/management/api-request-log-list/)に保存されます。ログの詳細は、SendGridを利用した場合と同様に、ご利用のメール配信サービス側のログをご確認ください。
:::

## Mailchimpの設定
### アカウント登録
まずは[Mailchimp](https://mailchimp.com/)にアクセスして、アカウント登録します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b7787c15b5474cd4ed90d3638ef73b0.png)

### APIキーの取得
アクティベートが完了し、アカウントにログインしたら[Automations]->[Transactional email]から[Launch App]をクリックしてダッシュボードにアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c17c3dad09a0d1b4f11dff832296cde1.png)

[Settings]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d9951a65d9d65562f0b07c16454d114.png)

[Add API key]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/153a1af87b99a757ad698b1529e21d9d.png)

APIキーが表示されるのでメモします。

### 送信ドメインの追加
次に、メールの送信元となるドメインを追加し、認証及び、SPF/DKIMを設定する必要があります。 

[Domains]タブをクリックし、送信元となるドメインを入力して[Add]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cbca3444652efa8de024963d1be1ac5.png)

追加したドメインと、ドメインの使用に必要な設定が表示されるので、[View details][View DKIM settings][View SPF settings]をクリックして、必要なDNSを設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a64145f256be9c5a4fb6765962b673b4.png)

#### Verified Domain
ドメインの認証はドメインのTXTレコードに指定された値を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d0e0dfc56f5834613c7d906a8c48947.png)

#### DKIM Settings
DKIMは`指定されたセレクタ._domainkey.ドメイン名`のTXTレコードに指定された値を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c7591b77d2beb005a6703a420251af80.png)

:::caution
VALUEの長さが設定できる文字数を超える場合はTXTレコードを分割して登録する必要があります。  
対応が必要な場合はドメイン管理サービスに問い合わせて設定してください。
:::

#### SPF Settings
SPFレコードはドメインのTXTレコードに指定された値を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6ccbc32cd030af7f351cf890ff7e826.png)

それぞれ設定すると以下のようになります。  
※キャプチャはお名前ドットコムの場合の例です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4350f835c20b96e96b45749b3ad54ebb.png)

[Test DNS Settings]をクリックして、全ての認証が確認できたら設定は完了です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b0274241048bf2f3ffa75efaf35661a.png)

:::caution
MailChimpのFreeプランでは、送信ドメインに登録されて、全ての認証が完了したドメインに対してのみメールの送受信が可能です。  
全てのメールアドレス宛への送信を許可する場合は有料プランを契約してください。
:::

## Kurocoの設定
### シークレットを登録する
Kurocoの管理画面にアクセスし、[環境設定] -> [シークレット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/25b831fd4835ad993f02298629b9e8cf.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c51de1ecc8ead6fa837c6492757a7276.png)

Mailchimpのダッシュボードで確認したAPIキーとを登録します。

|項目|値|
|:--|:--|
|名前|MAILCHIMP_API_KEY|
|値|MailchimpのAPIキー|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b43eb434d0214f5aee70351148303ae.png)

以上でMailchimpを利用する準備が整いました。

### カスタム処理を登録する
Mailchimpを利用する準備ができたら、SendGridによるメール送信をMailchimpに代替するカスタム処理を書きます。

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

以下のように設定します。

|項目|値|
|:--|:--|
|タイトル|sending_email_with_mailchimp|
|識別子|sending_email_with_mailchimp|
|トリガ|デフォルトのメール送信方法（SendGrid）を代替|
|処理|以下の内容|

```smarty title="sending_email_with_mailchimp"
{* Set Request Headers *}
{append var=headers value="Content-Type: application/json"}

{* Set Body *}
{assign var='payload' value=$payload|@json_decode}
{assign_array var='body' values=""}
{secret var='body.key' key='MAILCHIMP_API_KEY'}
{assign var='body.message.from_email' value="noreply@kuroco-mail.app"}
{assign var='body.message.subject' value=$payload.subject}
{assign var='body.message.text' value=$payload.text_part}
{assign_array var='to' values=""}
{assign var='to.email' value=$payload.to}
{assign var='to.type' value="to"}
{append var='body.message.to' value=$to}

{* Send Request *}
{api
    endpoint="https://mandrillapp.com/api/1.0/messages/send"
    method='POST'
    headers=$headers
    body=$body
    var=response
    status_var=status
}

{logger msg1="mailchimp_mail_log" msg2=$body msg3=$response}
{assign var="is_mail_sent" value=true}
```

:::caution
`noreply@kuroco-mail.app`の部分は自身のメールアドレスに変更してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2b006151abcc3ab3d1b41f0a13d17ef.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

## 動作の確認
実際にKurocoからのメールを送信してみます。  
動作の確認のため、パスワードリマインダーを使用してみます。

Kurocoのログイン画面にアクセスし、[パスワードを忘れた場合はこちら]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f585084835c88fda19163c26eabdf5f.png)

メールアドレスを入力して、[送信する]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71089ec62b43826f3812de3f23ef7194.png)

:::caution
Freeプランを利用している場合、宛先のメールアドレスはMailchimpの送信ドメインで認証したドメインである必要があります。
:::

Mailchimpの[Activity](https://mandrillapp.com/activity)を確認すると、Mailchimpからメールが送信されたことが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2336e11f7dfe8bb36f80e0d814e3dc0.png)

以上で、任意のメール配信サービスを利用する設定は完了です。

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)


---

# reCAPTCHAを利用したフォームを作成する

> 元ページ: `tutorials/using-recaptcha` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-recaptcha/

reCAPTCHAとは、Googleが無償で提供している機能です。  
Webサイトのお問い合わせフォーム等で情報を登録する際、悪質なスパム投稿からWebサイトを守ることができます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/84df007499e3c142559bebbc8dab35fa.png)
今回は、お問合せフォームにreCAPTCHA v2を導入する手順を説明します。

## 前提
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)のチュートリアルを実施し、基本的なフォーム実装について理解できていることを前提とします。
- [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display)を利用します。

## APIキーの取得方法

KurocoでreCAPTCHAを利用する場合は、先にGoogle reCAPTCHAにてAPIキーの取得が必要になります。

:::info
※ 前提として、reCAPTCHAを利用するにはGoogleアカウントが必要になります。アカウントをお持ちでない場合は、[Googleのアカウント作成ページ](https://www.google.com/intl/ja/account/about/)よりアカウント作成をお願いします。
:::

### Google reCAPTCHAへアクセスする  
[Google reCAPTCHA](https://www.google.com/recaptcha/about/)へアクセスし、[使ってみ見る]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b2b06c5045b04894d12524f916c3093c.png)

### サイト登録を行う 
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

### サイトキー、シークレットキーを確認する 
送信されると、「サイトキー」と「シークレットキー」が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e95a587d8bfebe5ab8d46bb510e04138.png)
こちらのキーはKurocoの設定で利用しますので、コピーをしておいてください。

以上でGoogle reCAPTCHA画面での設定が完了です。

## KurocoでreCAPTCHAの設定を行う
次に、Kuroco管理画面での設定となります。ご自身のKuroco管理画面へログインしてください。

### reCAPTCHA設定画面へ遷移する
[外部システム連携] -> [reCAPTCHA]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a070adc9bddf613b1fdede5ad8a05131.png)

### reCAPTCHAサイトキー、シークレットキーを入力する
サイト管理画面内にサイトキーとシークレットキーを入力する箇所がありますので、それぞれ入力します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3e2a49ac5dc4bc377b52dbb79d866a26.png)

|項目   |説明  |
| :--- | :--- |
|reCaptcha Site Key|取得したサイトキーの値を入力します。|
|reCaptcha Secret Key|取得したシークレットキーの値を入力します。|

設定完了したら、画面下部の[更新する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d2a00321b6d1c3f8618573aa1f877020.png)

## Kuroco エンドポイントの設定
### エンドポイントでreCAPTCHAを利用するように修正する
次にエンドポイントを設定します。
エンドポイント一覧画面へ移動し、reCAPTCHAを利用する `InquiryMessage::send` を設定したエンドポイントの「更新」ボタンをクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/0a28d3ff6252831564814c8e6d45769d.png)

エンドポイント修正画面より「use_recaptcha」にチェックを入れ、「更新」ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9f6afdd3bf50ad6ba97a374df0100f2.jpg)

### Swaggerにて確認する
先程の設定でエンドポイントの設定が完了しました。  
次に、問題なくエンドポイントが設定できているか、Swagger UIを利用して確認します。

エンドポイント一覧画面より、「Swagegr UI」をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3440c0eb1469632f6be52f7153e348aa.png)

先ほど設定したエンドポイントをクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a3c68894d97a7ce0421e682548ee5309.png)

Request bodyより、「Schema」をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/69c972d553228f5088351a76f0dcfaa8.png)
「recaptcha_response」というプロパティが記載されていることを確認します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a4150ae0f23012541846beae305d6065.png)

以上でKuroco管理画面での設定は完了です。

## reCAPTCHA認証の実装
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

## フロントエンド実装
次にフロントエンド実装します。
問い合わせフォームにreCAPTCHA認証を実装します。

### 認証コンポーネントを実装する
まずは認証コンポーネントを作成します。
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

### フォーム画面に認証コンポーネントを配置する
次に、reCAPTCHAを導入したいフォーム画面で、上記認証コンポーネントを使用します。
今回は `/pages/form/index.vue` を下記のように作りました。  

`await this.$refs.recaptcha.fetchResponse()`で`recaptcha_response`を取得し、フォームの内容と合わせてKurocoにPOSTしています。  
送信後は `await this.$recaptcha.reset()` を呼び出す必要があります。 

```markup reference title="/pages/form/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/recaptcha_for_form.vue
```

:::info
デフォルトの項目設定`name`,`email`,`message`のみのフォームをreCAPTCHAの動作確認用に追加し、利用しています。
フォームIDとエンドポイントURLはご自身のものに調整してください。
:::

:::caution
上記のコードは最低限の簡易的なものになっています。
:::

フォーム画面を確認すると、下記のようにreCAPTCHAが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1a2b76c115a08d740d440f096aee006c.png)

### レスポンスの確認
「私はロボットではありません」にチェックを入れると、Submitボタンがクリックできるようになります。  
Submitボタンをクリックすると、フォームの内容に加えて、recaptcha_responseをKurocoにPostし、渡されたトークンが自動的に検証されます。  
正当な値が渡された場合、フォーム送信が完了します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/371fba6b7d03cccb63f33c24d73763bf.png)

不正な値が渡された場合は、下記のようなエラーが返ります。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/d7dc8e0b69fabba990a208e7729d7ee8.png)

以上でreCAPTHAの設定が完了です。

今回は基本的な説明のため、簡単な設定方法を例に説明しました。
reCAPTCHAの詳しい設定方法は下記Googleのドキュメントをご参照ください。  
[Google Developers reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display)

:::caution
トークンの正当性確認は非ログインユーザーの場合のみ動作します。ログインユーザーの場合は検証処理をスキップします。
:::

## 関連ドキュメント
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [reCAPTCHA](/ja/docs/management/recaptcha/)
- [reCAPTCHAを利用したパスワードリマインダーを作成する](/ja/docs/tutorials/using-recaptcha-for-password-reminders/)
- [問い合わせフォームに大量のスパムメールが届きます。対策はありませんか？](/ja/docs/faq/how-do-i-reduce-spam-inquiries/)


---

# Webサイトのパフォーマンス改善について

> 元ページ: `tutorials/website-performance-tuning-with-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/website-performance-tuning-with-kuroco/

## Webサイトのパフォーマンス改善について

### `<img>` や `<video>` 要素にwidthとheightを指定する
画像や動画に幅と高さを指定することで、ブラウザは事前にそのスペースを確保できます。これにより、ページの再描画やレイアウトのシフトが発生しにくくなり、ユーザー体験が向上します。
:::info
レイアウトシフトについては、以下のドキュメントを参照ください。  
[CLSスコアについて](/ja/docs/tutorials/core-web-vitals-with-kuroco/#clsスコア)  
:::

### ファーストビューの範囲外にある `<img>` や `<iframe>` 要素のloading属性にlazyを追加する
ページのロード時間を短縮するために、'loading="lazy"'を使用してファーストビューの範囲外の画像の遅延読み込みが行えるようになります。これにより、ユーザーがスクロールして初めて見る部分の画像の読み込みが行われます。

### Webフォントの読み込みを最適化する
Webフォントを利用する場合、ロード時間が長くなる可能性があります。これを防ぐために、'rel="preload"'を使用してフォントの読み込みを最適化し、必要なテキストだけを表示するためにフォントのサブセット化を行うと良いでしょう。

### JavaScriptはbodyの末尾で読み込む
JavaScriptをbodyの末尾で読み込むことで、HTMLとCSSが先に読み込まれ、ユーザーに早くコンテンツを表示できます。

### HTML、CSS、JSをminify化する
Minify化することで、不要な空白やコメントを削除し、ファイルサイズを削減することができます。これにより、読み込み速度が向上し、パフォーマンスが改善されます。

### 画像はwebpなどの次世代画像フォーマットを使う
WebPなどの次世代画像形式は、JPEGやPNGに比べてファイルサイズが小さいため、パフォーマンスが向上します。
:::info
KurocoでWebpを利用する方法については、以下のドキュメントを参照ください。  
[画像の動的変換について](/ja/docs/reference/api-convert-image/)  
:::

### 画像・SVGのサイズを圧縮する
画像やSVGのサイズを圧縮することで、ファイルサイズが削減され、ロード時間が短縮されます。

### SSGでページを生成する際、payloadを利用した処理を行う
静的サイトジェネレーター（SSG）を用いてページを生成すると、ページがプリレンダリングされるため、クライアント側のレンダリング負荷が減ります。Payloadを利用した処理を行うことで、必要なデータだけロードし、パフォーマンスを改善できます。
:::info
payloadを利用してAPIリクエストを削減する処理については、以下のドキュメントを参照ください。  
[Nuxt.jsのSSGで、ページの生成時にAPIリクエストを減らす方法はありますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)  
:::

### CDNキャッシュを利用する
CDNを使用すると、リソースをユーザーに近いサーバーから提供することができ、ロード時間を短縮します。また、CDNのキャッシュ機能を利用することで、更にパフォーマンスの向上が期待できます。
:::info
CDNを利用したLCPのスコア改善については、以下のドキュメントを参照ください。  
[Kurocoで簡単にできるLCPのスコア改善](/ja/docs/tutorials/core-web-vitals-with-kuroco/#lcpスコア)  
:::

### 広告、SNSボタンといったサードパーティのJavaScriptを削減・非同期で読み込む
サードパーティのJavaScriptは、ロード時間の増加やパフォーマンスの低下を引き起こす可能性があります。これを削減し、非同期で読み込むことで、パフォーマンスを改善します。

### 広告、`<iframe>`、動的なコンテンツの表示改善
これらの要素のサイズを指定することで、ブラウザは事前にスペースを確保でき、CLSを防ぐことができます。
:::info
CLSのスコア改善については、以下のドキュメントを参照ください。  
[CLSスコアについて](/ja/docs/tutorials/core-web-vitals-with-kuroco/#clsスコア)  
:::

### リクエスト数を減らす
リクエスト数を減らすことで、サーバーへの負荷を減らし、ページのロード時間を短縮します。
CSSやJavaScriptファイルの結合、スプライト画像の使用などにより実現可能です。

## 関連ドキュメント
- [KurocoでできるCore Web Vitalsへの対応の進め方](/ja/docs/tutorials/core-web-vitals-with-kuroco/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [APIのキャッシュについて](/ja/docs/reference/api-cache/)
- [Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)
