# Kurocoドキュメント: チュートリアル / フォーム・メール通知（1/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- フォームにリマインダー機能を追加する（`add-reminder-function-to-form`）
- ログインユーザーの情報でAPIのレスポンスを動的に変更する（`change-the-api-response-with-the-logged-in-users-information`）
- 複数のメールマガジンを一度に登録・解除するページを作成する（`create-a-page-to-subscribe-and-unsubscribe-to-multiple-magazines-at-once`）
- SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する（`create-slack-app-and-get-bot-token`）
- ファイルにcreditとdescriptionのmeta情報を追加する（`file-credit-and-description-information`）
- GitHubActionsのビルド結果をslack-sendで通知する（`handling-a-slack-send-in-github-actions`）
- SendGrid連携方法（`how-to-link-sendgrid`）
- 配信購読者の登録・停止フォームを作成する（`implement-a-magazine-subscription-unsubscription-form`）
- コンテンツの特定項目が更新されたらメールで通知する（`notify-by-email-when-specific-items-in-the-content-are-updated`）
- お問い合わせの受信通知をChatworkで送信する（`send-chatwork-notification-after-a-form-has-been-submitted`）
- お問い合わせの受信通知をSlackで送信する（`send-slack-notification-after-a-form-has-been-submitted`）
- メールマガジンを送付する（`sending-email-notifications`）
- フォームの回答を送付したユーザー向けに配信メッセージを送付する（`sending-notification-messages-to-users-who-submitted-form-responses`）


---

# フォームにリマインダー機能を追加する

> 元ページ: `tutorials/add-reminder-function-to-form` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/add-reminder-function-to-form/
> 概要: Kurocoのカスタムメンバーフィルターは柔軟な設定で対象となるメンバーを絞り込むことができます。本チュートリアルではこちらを利用して、届いたフォームの対応が一定時間されていない場合に、担当者宛に通知を送るリマインダー機能を実装してみます。

## 概要
Kurocoのカスタムメンバーフィルターは柔軟な設定で対象となるメンバーを絞り込むことができます。
本チュートリアルではカスタムメンバーフィルターを利用して、届いたフォームの対応が一定時間されていない場合に、担当者宛に通知を送るリマインダー機能を実装してみます。

具体的には以下の条件に当てはまるお客様が存在する場合に、担当者宛に通知を送ります。  
- フォームが送信されてから4時間以上経過している
- 回答のステータスが「0::未対応」
- フォームの送信者が有償サポートのグループに所属する

### 学べること
以下の手順でリマインダー機能を実装します。
- [カスタムメンバーフィルターを作成する](#カスタムメンバーフィルターを作成する
)
- [バッチ処理を作成する](#バッチ処理を作成する)
- [動作確認をする](#動作確認をする)

### 前提条件
事前に次のフォームとメンバーを追加しておきます。  

#### メンバー

リマインドが必要なグループに所属するテストメンバーをいくつか追加しておきます。  
本チュートリアルでは「有償サポート契約」グループに所属するメンバーを準備しました。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/420d3d5a40813662a40aa03df11abd7c.png)

#### フォーム

リマインド機能を追加するフォームを準備します。  
基本設定のステータス一覧はデフォルトの設定にしてください。  

```
0::未対応
5::対応中
10::対応済
20::返信有り
```
他の項目は任意に作成して構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f4ed359097f46ffc98c6e22da5bb5498.png)

また、動作の確認に利用する為、テスト用のユーザーでログインした状態でフォームを送り、メンバーが紐づいた回答を作成しておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/90d2ad03e12ab50934f8fd94ecfae533.png)

ログイン状態でフォームを送ると、回答の名前にメンバー情報詳細ページへのリンクが付きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1ef660798cb85a87391f86f1e5e3ab7.png)

## カスタムメンバーフィルターを作成する

まずは対象の条件に一致するお客様を絞り込むカスタムメンバーフィルターを作成します。  
絞り込む条件は以下になります。

- フォームが送信されてから4時間以上経過している
- 回答のステータスが「0::未対応」
- フォームの送信者が有償サポートのグループに所属する

[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b9ef56bec8c05db3b158cb461714110.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f129ff533b1751131a804c4baab80691.png)

|項目|値|
|:--|:--|
|タイトル|至急対応が必要なお客様|
|アクセス制限|全体|
|モジュール検索条件|AND|
|メンバータブ|`グループ` どれかを含む `有償サポート契約`|
|フォームタブ|`フォームID` = `対象とするフォームID(15)`<br/>AND<br/>`ステータス` = `0`<br/>AND<br/>`受信日時` 相対で日付指定 < `-4 hour`|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9d6cab442d8dc3b61f968a821a972abe.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b3993435d6ae9b6fc6f0fd606aa6905.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e9c6c65b8f4aec1763958575e1f89e35.png)

:::info
カスタムメンバーフィルターのフォームタブでは、フォームの条件を元に、フォームを送信したメンバーを絞り込むことができます。  
ログイン状態でフォームの送信をし、回答とメンバーが紐づいている必要があります。  
:::

設定ができたら[追加する]をクリックしてカスタムメンバーフィルターを追加します。  

## バッチ処理を作成する

次に、作成したカスタムメンバーフィルター(至急対応が必要なお客様)で対象のユーザーが存在するかを定期的にチェックし、対象者がいる場合に、担当者宛に通知を送るバッチ処理を作成します。  

[オペレーション] -> [バッチ処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d7157130e402e302a1555ed76cab1eb.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c894d4d2fda838d2a3325531375d1d54.png)

以下の内容を設定します。

|項目|値|
|:--|:--|
|タイトル|send_reminder|
|識別子|send_reminder|
|タイプ|1時間毎|
|処理|以下の内容|

```smarty reference title="send_reminder"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/batch_processing/send_inquiry_response_reminder.txt
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/278f6b14ae1e191da63cad73567e3ed3.png)

:::caution
- `{assign       var='method_params.custom_search_id' value='21'}`の部分はご自身のカスタムメンバーフィルターのIDに変更してください。  
- `{$smarty.const.ROOT_MNG_URL}/・・・&inquiry_id=15`の部分はご自身のフォームのIDに変更してください。  
- `YOUR_MAIL_ADDRESS@example.com`には送信先のメールアドレスを記入してください。  
:::

## 動作確認をする
最後に動作の確認をします。  
バッチ処理が実行されるのを待つか、[すぐに実行する]をクリックしてバッチ処理を動作させます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d4622f126afcf62e104c9494c146837.png)

以下のメールが届きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c536315a140669f6a5462f7064c9093d.png)

メールに記載のリンクをクリックすると、受信から4時間以上経過したステータスが「0::未対応」の回答一覧が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/570f65274e127a405f83dda11418aa3f.jpg)

以上で、フォームにリマインダー機能を追加する説明を終わります。

## 関連ドキュメント
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# ログインユーザーの情報でAPIのレスポンスを動的に変更する

> 元ページ: `tutorials/change-the-api-response-with-the-logged-in-users-information` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/change-the-api-response-with-the-logged-in-users-information/
> 概要: ログインユーザーの情報を使用して、APIエンドポイントのレスポンスを動的に変更する方法を解説します。

ログインユーザーの情報を使用して、APIエンドポイントのレスポンスを動的に変更する方法を解説します。  
本チュートリアルでは、以下の構成で、ログインユーザーによってお知らせ一覧の表示内容を変更してみます。  

- [メンバー拡張に会社名を追加する](#メンバー拡張に会社名を追加する)
- [コンテンツ(お知らせ)にターゲットの会社を追加する](#コンテンツお知らせにターゲットの会社を追加する)
- [ログインユーザーの情報をフィルタークエリに設定するカスタム処理を追加する](#ログインユーザーの情報をフィルタークエリに設定するカスタム処理を追加する)
- [エンドポイントにフィルターリクエストの許可と前処理の設定をする](#エンドポイントにフィルターリクエストの許可と前処理の設定をする)

## メンバー拡張に会社名を追加する
[メンバー管理]->[メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c85c7d48fa6b512e9871cfa633d48ed8.png)

[メンバー詳細設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a1eb0d9c3a5f86333db3660338762064.png)

[登録されるメンバーの拡張項目を設定する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd21cee900649321e64eda53f56a69e0.png)

以下のように設定し、[更新する]をクリックします。

|項目|設定|
|:--|:--|
|項目名|会社名|
|識別子|company_id|
|設定|単一選択|
||1::株式会社A<br/>2::株式会社B|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c7b8472641f3e13b37b4e5c5946c432.png)

[メンバー一覧](/ja/docs/management/member/)のページから、動作確認用メンバーの名前をクリックします。    
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0e4c3785e0bd41e766881d7b0ae39641.png)

メンバー編集ページが表示されるのでプロフィール情報のタブで会社名をセットします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6a5f716c69b8335aa88d24bfbe0de46.png)

## コンテンツ(お知らせ)にターゲットの会社を追加する
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00d3a62367890dbebe6a7fce4462f026.png)

コンテンツ定義一覧から[お知らせ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d90475fb60a0050202007a6a9daff61.png)

コンテンツ定義編集画面が開くので、下記のように設定し、[更新する]をクリックします。  

|項目|設定|
|:--|:--|
|親項目|選択なし|
|項目名|ターゲット|
|項目設定|複数選択可|
||1::株式会社A<br/>2::株式会社B<br/>3::株式会社C|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c00c916670a4b86f4b72dc6788ac206a.jpg)

コンテンツ編集画面に追加した項目が表示されるので、任意のコンテンツの編集画面でターゲットとなる会社名にチェックを入れて更新します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2357beadc3fe2846a4da983bc6d1b5e4.png)

## ログインユーザーの情報をフィルタークエリに設定するカスタム処理を追加する
次にログインユーザーの情報を取得するカスタム処理を追加します。  
[カスタム処理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/08626c9403ce2cfd33536b050e828701.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/eb104fc89b1dbda55d730804ac20219a.png)

以下を設定し、[追加する]をクリックします。  

|項目|設定|
|:--|:--|
|タイトル|ログインユーザーの情報をフィルタクエリに追加|
|識別子|set_filter_request|
|処理|以下のコード|

```js
{if $smarty.session.super_flg ne 1}
{assign_member_detail var='mem' member_id=$smarty.session.member_id}
{assign var=request.filter value="ext_1 contains `$mem.company_id_key`"}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/89f4bf88915e7bfa9414923dc560637d.jpg)

:::tip
filterパラメータの記法詳細は[Filter検索のパラメータ](/ja/docs/reference/filter-query/)を参照してください。  
:::

## エンドポイントにフィルターリクエストの許可と前処理の設定をする
お知らせのリストを取得するエンドポントを持つAPIをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd204dfd21b483041008fbdd5dcd5227.png)

お知らせのリストを取得するエンドポントの[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/072be2f72edc3dfb6bd185b1b2a7822a.png)

`filter_request_allow_list`のパラメータに`ext_1`を入力して、[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/232fd5cae350196cf01c54578a0488e5.png)

次に[前処理]をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c3d0b93482f8ab8337d2a2935000704f.png)

カテゴリを未分類にし、一覧から「ログインユーザーの情報をフィルタクエリに追加」を設定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/422ce355cabbc4a934801b779cbd46e2.png)

## 動作を確認する
最後に動作確認をします。
ログイン後、お知らせ一覧のページを確認すると、表示される一覧の内容がフィルタリングされていることがわかります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdb01b08cd293b1263f05281a53d15a8.png)
:::tip
動作確認はSuwagger UIで確認ができませんので、ブラウザ上で確認をするようにしてください。  
参考FAQ：[SwaggerUIで確認できないリクエストがあります。確認する方法はありますか？](/ja/docs/faq/how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui/)
:::

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [メンバー詳細設定](/ja/docs/management/new-member-settings/)
- [前処理](/ja/docs/reference/pre-processing/)
- [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
- [SwaggerUIで確認できないリクエストがあります。確認する方法はありますか？](/ja/docs/faq/how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui/)


---

# 複数のメールマガジンを一度に登録・解除するページを作成する

> 元ページ: `tutorials/create-a-page-to-subscribe-and-unsubscribe-to-multiple-magazines-at-once` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/create-a-page-to-subscribe-and-unsubscribe-to-multiple-magazines-at-once/
> 概要: MagazineInfo::listのエンドポイントにself_onlyのパラメータを設定して利用すると自身の購読している配信の一覧が取得できます。本チュートリアルではこちらを利用して、複数のメールマガジンとその購読状態が表示され、一度に登録・解除できるページを作成します。

## 概要
`MagazineInfo::list`のエンドポイントにself_onlyのパラメータを設定して利用すると自身の購読している配信の一覧が取得できます。  
本チュートリアルではこちらを利用して、複数のメールマガジンとその購読状態が表示され、一度に登録・解除できるページを作成します。  


### 学べること
以下の手順で階層構造を持ったコメントの追加と取得をします。
- [複数の配信を準備する](#複数の配信を準備する)
- [エンドポイントを設定する](#エンドポイントを設定する)
- [フロントエンドを実装する](#フロントエンドを実装する)
- [動作の確認をする](#動作の確認をする)

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

## 複数の配信を準備する
まずはKurocoの管理画面で複数の配信を登録します。  
[チャネル] -> [一括配信]で配信一覧に遷移し、右上の[追加]をクリックして配信を登録します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/83dde7ca8ec2010d77ead21da36e8a72.png)

今回は以下のように3つの配信を準備しました。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7deeedea451e9a94c82b4262579bd32.png)

配信のIDはエンドポイントに設定するのでメモしてください。

## エンドポイントを設定する
エンドポイントは Login::login_challenge のエンドポイントが設定されたAPI設定に追加します。  
そうすることでログインした認証情報を利用してエンドポイントへのリクエストが行われます。
異なるAPI間で認証情報は共有できませんので注意してください。

今回は自身の購読している配信一覧を取得するエンドポイントと、配信登録するエンドポイント、配信解除するエンドポイントの3つを設定します。  

[新しいエンドポイントの追加]をクリックして、それぞれ作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e20df3e56291487f859a3cbd905b261.png)

**配信一覧を取得するエンドポイント**

|項目|設定内容|
| :--- | :--- |
|パス|my_magazine/info|
|カテゴリー|マガジン|
|モデル|MagazineInfo|
|オペレーション|list|
|magazine_id|レスポンスの対象となる配信IDを入力する<br/>7<br/>8<br/>9|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/924e9291e755a32287452c2518d50e04.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9bc676e1818055eb7038b911559e63bd.png)

:::tip
self_onlyを有効にすると、購読している配信のみレスポンスされます。
購読有無によらない配信の一覧をAPIから取得する場合は、self_onlyを付与しない`MagazineInfo::list`のエンドポイントを別途作成して利用してください。
:::

**配信登録するエンドポイント**

|項目|設定内容|
| :--- | :--- |
|パス|magazine/subscribe|
|カテゴリー|マガジン|
|モデル|MagazineSubscriber|
|オペレーション|subscribe |
|allow_magazine_id|エンドポイントを利用して購読者登録を許可する配信IDを入力する<br/>7<br/>8<br/>9|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/034ca5590ffc13d3be0b6dfa434832ce.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6a50ba20972c3afa409925f3bff0cb69.png)

:::caution
self_onlyにチェックが無い場合、エンドポイントが分かれば他人を購読者に追加できてしまうのでご注意ください。
:::

:::caution
allow_magazine_idの指定が無い場合、全ての配信に対して購読者登録できてしまうのでご注意ください。
:::

**配信解除するエンドポイント**

|項目|設定内容|
| :--- | :--- |
|パス|magazine/unsubscribe|
|カテゴリー|マガジン|
|モデル|MagazineSubscriber|
|オペレーション|unsubscribe|
|allow_magazine_id|エンドポイントを利用して購読解除を許可する配信IDを入力する<br/>7<br/>8<br/>9|
|self_only|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/58166c33f40dac4b8b0dcd9fd4416dc5.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b35ebe8a134376a0e2d8cafb49ddab92.png)

:::caution
self_onlyにチェックが無い場合、エンドポイントが分かれば他人の購読者登録を削除できてしまうのでご注意ください。
:::

:::caution
allow_magazine_idの指定が無い場合、全ての配信に対して購読者登録の削除ができてしまうのでご注意ください。
:::

:::tip
本チュートリアルでは利用していませんがMagazineSubscriber::listのエンドポイントを利用すると、配信に対する購読者の一覧が取得できます。  
`search_mail_address contains "@example.com"`のようにフィルタをかけるとメールアドレスのドメイン名で検索が可能です。  
管理者向けの管理画面を実装する場合にご活用ください。
:::

## フロントエンドを実装する

以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/mypage/magazine/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/multiple_magazines_update.vue
```

**Nuxt3:**

```markup reference title="/pages/mypage/magazine/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/multiple_magazines_update.vue
```


今回はサンプルとしてラジオボタンで購読状態を表示し、変更があった場合は変更があったタイミングですぐにAPIリクエストを送信する実装としました。  

:::tip
Sumbitボタンを付けて、Submit時にまとめてPOSTのリクエストを送る場合は、配信の数が増えると処理に時間がかかる場合があります。  
変更のない配信へのリクエストを省略したり、新しい購読状態をバッチに登録させて処理させるなどの工夫をしてください。  
:::

## 動作の確認をする

ログイン後に対象のディレクトリにアクセスすると、配信の一覧が表示され、購読状態を更新したタイミングでAPIリクエストが送信されることを確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab1328c88661fefa5e2b689603e5ee54.gif)

## 関連ドキュメント
- [KurocoとNuxt.jsで配信購読者の登録・停止フォームを作成する](/ja/docs/tutorials/implement-a-magazine-subscription-unsubscription-form/)


---

# SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する

> 元ページ: `tutorials/create-slack-app-and-get-bot-token` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/create-slack-app-and-get-bot-token/
> 概要: KurocoとSlackを連携する際に共通で必要となる、Slackアプリの作成、Bot User OAuth Tokenの取得、Kurocoへの設定手順を説明します。

## 概要

KurocoとSlackを連携するには、Slackアプリを作成し、そのアプリの「Bot User OAuth Token」をKurocoに設定します。  
このページでは、Slack連携を行う各チュートリアルで共通となる以下の手順を説明します。

- [Slackアプリの作成](#slackアプリの作成)
- [AppをWorkspaceにインストール](#appをworkspaceにインストール)
- [Bot User OAuth Tokenの取得](#bot-user-oauth-tokenの取得)
- [Appの情報編集](#appの情報編集)
- [Slackチャンネルへアプリの追加](#slackチャンネルへアプリの追加)
- [KurocoとSlackの連携](#kurocoとslackの連携)

:::info
Appマニフェスト（YAML）の内容は、実現したい連携内容によって異なります。  
このページを参照しているチュートリアルにマニフェストが記載されている場合は、そのマニフェストを使用してください。
:::

## Slackアプリの作成

### Appを作成する

[Slack API](https://api.slack.com/apps)にアクセスし、[Create an App]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e668c5bc17cc4680068a05bfb3b8434f.png)

ポップアップでApp作成画面が表示されるので、[From an app manifest]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b516cfed5eb19c0c429264b42ea0617b.png)

Workspace選択画面が表示されます。  
「Pick a workspace to develop your app in:」フィールドより、Appを利用するworkspaceを選択し[Next]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bfd8157d34e6d10919c78a5aa8df0c70.png)

Enter app manifest below画面が表示されるので、「YAML」のテキストエリアにAppマニフェストを貼り付けます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05af84f691c3ce19be77ed9c46ac2058.png)

Slackへメッセージを投稿するだけの場合は、以下のマニフェストを利用できます。

```yaml
_metadata:
  major_version: 1
  minor_version: 1
display_information:
  name: KurocoNotification
features:
  bot_user:
    display_name: KurocoNotification
    always_online: true
oauth_config:
  scopes:
    bot:
      - chat:write
      - im:write
```

:::tip
上記設定ではボットからSlackへのメッセージ追加を許可します。  
チャンネルの情報や投稿済みの内容の読み込み等を行いたい場合はSlackのリファレンスを参考にしてください。  
-[Create and configure apps with manifests](https://api.slack.com/reference/manifests)  
-[OAuth Permission scopes](https://api.slack.com/legacy/oauth-scopes)
:::

貼り付け後、[NEXT]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ebb427257f9947a57a16800aa3ac766a.png)

[Create]をクリックし、Appの作成が完了です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa8e63a798475bc9f0c1c9f59774a0d8.png)

## AppをWorkspaceにインストール

次に、先ほど作成したAppをWorkspaceにインストールします。

[Install to Workspace]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5baa88cfef6d57d2a5a5b59db86e9746.png)

アクセス権限のリクエスト画面が表示されるので、[許可する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0721418961354224dd376b0ab8c80bdc.png)

## Bot User OAuth Tokenの取得

左サイドバーより、[OAuth & Permissions]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c00f3825f3fee66a8f1653f1eda3faad.png)

「Bot User OAuth Token」が表示されるので、コピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a47ea50f37f54e8859570e74f96b9d0d.png)

:::caution
Bot User OAuth TokenはSlackワークスペースを操作できる資格情報です。第三者に共有しないでください。
:::

## Appの情報編集

デフォルトだとAppのアイコンが表示されないので、画像設定をします。
左サイドバーより[Basic Information]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74a29f2b989ec7ee14402d817409bf52.png)

「Display Information」より、[Add App Icon]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/072296a329667f736281048e2b5c901b.png)

ここではKurocoのアイコンをアップロードしました。(画像は[こちら](https://kuroco.app/files/user/img/documentation/kuroco_logo_512.png)から表示／保存できます。)
画像アップロードされたら完了です。  
アイコンが設定されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7bd0bf41aa5528a09d6235c73762ad98.png)

Workspaceを確認すると、Appに作成したAppが追加されていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2625af80f869fc2a8d5568e485b7dfd.png)

## Slackチャンネルへアプリの追加

ボットからチャンネルへ投稿する場合は、投稿先のSlackチャンネルへAppを追加します。

投稿先のチャンネルで、チャンネル名をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4020f4f472054a42968be13015f3e600.png)

[インテグレーション]->[App]の[アプリを追加する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f5b33b0fe4615be2801c5221d611f647.png)

作成したAppを追加します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/24bca7292c0ec11ab2a3ebc44a19fd71.png)

## KurocoとSlackの連携

Kuroco管理画面より[チャネル] -> [メッセージング] -> [Slack]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/568e5421e71f00b08fa282a6b021b695.png)

Slack連携設定画面が表示されるので、「有効にする」にチェックを入れます。「Bot User OAuth Token」には先ほどコピーしたBot User OAuth Tokenを入力し、[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/524e32fc0461971f25916cd8cfe4312b.png)

以上でKurocoとSlackの連携設定が完了です。

:::info
連携が正しく設定されているかは、Slack連携設定画面のテスト送信フォームから確認できます。詳細は[Slack](/ja/docs/management/slack/)を参照してください。
:::

## 関連ドキュメント
- [Slack](/ja/docs/management/slack/)
- [お問い合わせの受信通知をSlackで送信する](/ja/docs/tutorials/send-slack-notification-after-a-form-has-been-submitted/)
- [Slackで定期的に確認をサポートするbotアプリ「KurocoWorkflow」のインストールと利用方法](/ja/docs/tutorials/workflow-bot/)


---

# ファイルにcreditとdescriptionのmeta情報を追加する

> 元ページ: `tutorials/file-credit-and-description-information` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/file-credit-and-description-information/
> 概要: ファイルにクレジットや説明のメタデータを追加するには、ファイルマネージャのKurocoFiles(メタデータ付き) ディレクトリを使用します。

## 概要
クレジット情報は、ファイルの作成者や所有者の著作物を正確に特定するのに役立ち、説明文は、他の人がファイルの目的や内容を理解するのを容易にします。特に著作権で保護された資料の場合、クレジット情報と説明文の記載が法的に要求される場合があります。  
ファイルにクレジットや説明のメタデータを追加するには、ファイルマネージャのKurocoFiles(メタデータ付き) ディレクトリを使用します。

## 設定方法
[ファイルマネージャー](/ja/docs/management/file-manager/)から[KurocoFiles(メタデータ付き)]ディレクトリに遷移します。  
なお、クレジットや説明文の情報は、このディレクトリにあるファイルにしか入れることができません。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f127f71c21d886f1710c996958fce61c.jpg)

追加したいファイルの上で右クリックし、「メタデータ」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b242401af6bfdffa340e239d9fd6e22.png)

メタデータウィンドウが開くので、説明とクレジットを入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/70c16d4b0bc54292efdc28c1787e0c70.png)

以上です。この情報はファイルとともに保存され、ファイルの出所や目的を特定するために使用できます。

## 確認方法
設定したクレジットと説明はAPIのレスポンスに含まれます。  

### コンテンツ定義を作成する
確認のため、ファイル(ファイルマネージャーから)の項目を持つコンテンツ定義を用意します。

[コンテンツ定義一覧](/ja/docs/management/content-structure-topics-group/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d110338461cc1372404040efe7e58014.png)

以下の内容で設定をします。  

全般

|項目|設定|
|:--|:--|
|名前|My Content|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0309edcb5566f09a23c038ceb2001b1.png)

項目設定

|項目|設定|
|:--|:--|
|項目名|My Image|
|項目設定|ファイル(ファイルマネージャーから)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/16381f1fcaffca2dd282ee510fde5f64.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8f046a24c79079908014b2874befa433.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。  

### コンテンツを追加する
[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7178ec2a0600c86f25320ad3eca58d8.png)

以下を入力し、[追加する]をクリックします。 

|項目|値|
|:--|:--|
|タイトル|My Image|
|My Image|クレジットと説明を追加したファイル|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e19d20bd9098d06d26acfff4c6eecd50.png)

### エンドポイントを作成する
[API](/ja/docs/management/api-list/)の画面から[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21831b02823d8ec43ef328ba8c998ad7.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|list|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|list|
|topics_group_id|コンテンツ定義のID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c094bdd38abe6bb38e1ca0549832f88.jpg)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

### Swagger UIでレスポンスを確認する
対象のAPIから[Swagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d94c23921b75e396d141f8d88ec62c0a.png)

Topics::listのエンドポイントのTry it Outをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0778409cc19b8b867d73478909e50a7d.png)

[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c8a6b9e73587aaca570da4532474de8.jpg)

ファイルのクレジットと説明のメタデータを含むレスポンスが得られます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/37d2e0973b0a98debdcec3364d95118b.png)

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [KurocoFilesディレクトリとドメインの使い分けについて](/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [ファイルマネージャーにアップロードした画像をコンテンツの拡張項目で使用できますか？](/ja/docs/faq/can-i-use-kurocofiles-images-in-additional-fields/)


---

# GitHubActionsのビルド結果をslack-sendで通知する

> 元ページ: `tutorials/handling-a-slack-send-in-github-actions` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/handling-a-slack-send-in-github-actions/
> 概要: このチュートリアルでは、GitHub Actionsとslack-sendを組み合わせて、ビルド結果をSlackに通知する方法を紹介します。

## 概要
このチュートリアルでは、GitHub Actionsとslack-sendを組み合わせて、ビルド結果をSlackに通知する方法を紹介します。

### 前提条件
本チュートリアルは、下記条件にてサイト運用をしていることを前提とします。
- Next.js/Nuxt.jsを利用している。
- KurocoFrontを利用している。
- GitHub Actionsを利用している。

また、このチュートリアルではslack-sendを利用してslackに通知を行います。
詳細は[slack-sendのドキュメント](https://github.com/marketplace/actions/slack-send)を参照してください。

## Slackアプリ設定から通知用アプリを作成する
以下の画面からアプリを作成します。  
https://api.slack.com/apps?new_app=1

`From an app manifest`を選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f71f308af9438575efab8f5a34452b6.png)

アプリを追加するワークスペースを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b82feba53d594319fb081662d1192e90.png)

`App Manifest`に以下のYAMLを設定してください。  
incoming-webhookでSlackに通知を行います。
```
_metadata:
  major_version: 1
  minor_version: 1
display_information:
  name: github-action-slack-send
features:
  bot_user:
    display_name: github-action-slack-send
oauth_config:
  scopes:
    bot:
      - incoming-webhook
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/368a7240d14111e8f79764fe2d159d96.png)

[Create]をクリックしてアプリを作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/53ee0dcbfb91c61cb538bc2383c984de.png)

## ワークスペースにアプリをインストールする
`Basic Infomation`の`Install to Workspace`からワークスペースに作成したアプリをインストールします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b87265fe036478803a870fde77d73fd2.png)

通知するチャンネルを選択します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/284e65bf367d54d4cc06841c47492064.png)

アプリが追加できたら`Install app`に`Bot User OAuth Token`と`Webhook URL`が追加されているのが確認できます。  
`Webhook URL`はGitHubに登録するのでコピーしてください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ad1726519c4f79f22dfe63a8c808a2a.png)


## GitHubにSecretsにWebhook URLを追加する
GitHubのリポジトリのページを開きます。  
`Settings` -> `Secrets and variables` -> `Actions` の`New repository secret`をクリック
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7fd74fd355d28ff13d31fd221c434d5.png)

Nameに`SLACK_INCOMING_WEBHOOK_URL`を設定します。  
Secretにコピーした`Webhook URL`を設定します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d7f0c1dd230b542c6970dcafe533a97f.png)

入力できたら[Add secret]をクリックしてGitHubシークレットを追加します。

## Slack通知用のワークフローファイルを作成する
`.github/workflows/`に`slack-build-notifier.yml`を作成し、以下の内容を設定。
`workflows`にはビルド用のワークフローファイルの name を設定してください。
```
name: Slack Build Notifier
on:
  workflow_run:
    workflows:
      - Build and deploy to Kuroco front
    types: [completed]
jobs:
  on-success:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
      - uses: actions/checkout@v2
      - name: Send GitHub Action trigger data to Slack workflow
        id: slack
        uses: slackapi/slack-github-action@v1.23.0
        with:
          payload: |
            {
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "ビルド成功"
                  }
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "GitHub Actions: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.event.workflow_run.id }}"
                  }
                },
                {
                  "type": "context",
                  "elements": [
                    {
                      "type": "mrkdwn",
                      "text": "Author: <https://github.com/${{ github.event.sender.login }}|@${{ github.event.sender.login }}>"
                    }
                  ]
                }
              ]
            }
        env:
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_INCOMING_WEBHOOK_URL }}
  on-failure:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    steps:
      - uses: actions/checkout@v2
      - name: Send GitHub Action trigger data to Slack workflow
        id: slack
        uses: slackapi/slack-github-action@v1.23.0
        with:
          payload: |
            {
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "ビルド失敗"
                  }
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "GitHub Actions: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.event.workflow_run.id }}"
                  }
                },
                {
                  "type": "context",
                  "elements": [
                    {
                      "type": "mrkdwn",
                      "text": "Author: <https://github.com/${{ github.event.sender.login }}|@${{ github.event.sender.login }}>"
                    }
                  ]
                }
              ]
            }
        env:
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_INCOMING_WEBHOOK_URL }}
```

通知が成功するとSlackに以下のように通知されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9adc3954dad22ef61b39b7521f7f379.png)

## 関連ドキュメント
- [GitHubActionsでgenerateに失敗した場合に、ビルドを中止しSlackに結果を通知する方法](/ja/docs/tutorials/handling-a-generate-error-in-github-actions/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [コンテンツの更新時にGitHub Actionsを自動実行する](/ja/docs/tutorials/auto-run-github-with-contents-update/)
- [GitHub Actionsワークフローのアクションを最新バージョンに保つ方法はありますか？](/ja/docs/faq/how-to-keep-github-actions-up-to-date/)


---

# SendGrid連携方法

> 元ページ: `tutorials/how-to-link-sendgrid` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-link-sendgrid/
> 概要: KurocoではSendGridと連携することで、問い合わせへの返信や、システムからの通知のメールを、任意のメールアドレスに設定することができます。

KurocoではSendGridと連携することで、問い合わせへの返信や、システムからの通知のメールを、任意のメールアドレスに設定できます。  
SendGridと連携しない場合、通知のメールアドレスは「`noreply@kuroco-mail.app`」となります。

このチュートリアルでは、Kuroco管理画面でのSendGridとの接続作業の方法と、メールアドレスの変更方法を説明します。

:::caution
SendGrid側の仕様の変更により、SendGrid APIKEYの取得方法は本チュートリアルと異なる箇所がある場合もございます。詳細は[SendGrid](https://sendgrid.kke.co.jp/)で最新情報をご確認ください。
:::

:::caution
SendGridと契約・接続していてもKurocoのメール送信の料金は引き続き発生します。
:::

## SendGridの設定
### 1. アカウントを作成する 
[SendGrid](https://sendgrid.kke.co.jp/plan/)のプランを確認し、アカウントの作成をお願いいたします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b1a48b08225521ce6100181e24b9683f.png)
:::caution
海外からSendGridを利用する場合、 `https://signup.sendgrid.com/` にアクセスしてアカウント作成をお願いします。
:::

### 2. 送信ドメインを認証する  
[SendGridのチュートリアル](https://sendgrid.kke.co.jp/docs/User_Manual_JP/Settings/Sender_authentication/How_to_set_up_domain_authentication.html)を参考に送信ドメインの認証をします。

ダッシュボードにログイン後、[Settings] -> [Sender Authentication]にアクセスし、Authenticate Your Domainの[Get Started]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5e3416a6a0da720c9b305c4a525fbb36.png)
①で利用しているDNSのホストを選択し、②のLink Brandingの項目はNoを選択し[Next]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/807bfa280cfc8bf3886835a2cffa7190.png)

認証したいドメインを入力し[Next]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a0b370456038d2525ef22d134d3eaad3.png)
設定の必要なDNSレコードが表示されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f96e029c701b8d82f012eb84aff4e1b.jpg)
こちらのDNSレコードを、ご自身が管理するドメインのDNSに追加します。  
(下記はお名前.comの画面例です)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b97b5742aeb0b411906f23e383599bfd.png)
DNSにレコードを追加したら、内容が反映されるまでしばらく待ちます。最大48時間かかる場合があります。

DNSの登録が反映されたら、[I'v added these records.]にチェックを入れて[Verify]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/371e9b67cf3b2fede039f96afbb278c0.jpg)
下記画面が表示されたらドメインの認証手続きは完了です。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/27b930cf976d1496f8e9af33267879de.png)

:::info
SendGridの場合、上記の3つのCNAMEレコードを設定することで、SPF/DKIMの認証が完了します。  
また、サブドメインでのCNAME設定になるため、既存のメールシステムからのメール送信には影響せず、既存のSPFコード修正も不要です。

詳しくは[SendGridからメール送信する場合のSPFとDKIMの認証の仕組み](https://sendgrid.kke.co.jp/blog/?p=10883)を参照してください。
:::

### 3. SendGrid APIKEYを確認する  
[SendGridのチュートリアル](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/manage_api_key.html)を参考にAPIキーを発行します。  
ダッシュボードにログイン後、[Settings] -> [API Keys]にアクセスし、画面右上の[Create API Key]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ac33170d57d97c449606c686fcf78eb5.png)
API Key Nameを記入し、Restricted Accessを選択し、[Create & View]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/410c20df43d49b4d6ab92258b5cfc8ec.png)
下記画面が表示されたらAPI Keyの発行は完了です。  
API Keyは画面を閉じると再表示できませんので、メモしておいてください。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4f91901cfa7aa9dd332f927572a1514c.png)
### 4. Click Trackingを無効にする  
[Settings] -> [Tracking]にアクセスし、Click Tracking横の鉛筆マークをクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/23d843ddb0da19d88a419d06a8fce120.png)
設定画面が表示されるので、[DISABLED ENABLED]のスライダーをクリックして、DISABLEDに設定し、[Save]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bed487ab5d76088b7f3cb4a3d2e203ff.png)
「Success! The Click Tracking setting has been updated.」の表示がされ、Click TrackingのステータスがDisabledになったら設定は完了です。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/78624e868fb04d5e46b4cd042c5e9742.png)

### 5. Event Webhookを有効にする
[Settings] -> [Mail Settings]にアクセスし、Event Webhook横の鉛筆マークをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/71b6f2932bbc786d5f832f70eacefa28.jpg)

設定画面が表示されるので、以下のように設定し、[Save]をクリックします。  

|項目|設定|
|:--|:--|
|Authorization Method|None|
|HTTP Post URL|Kuroco管理画面に記載のURL|
|DELIVERABILITY DATA|Select All|
|ENGAGEMENT DATA|Select All|
|Event Webhook Status|ENABLED|

HTTP Post URL は [[チャネル] -> [メール] -> [SendGrid]](/ja/docs/management/sendgrid/)のWebhook URLを入力してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c226e1ca7b560e977a7d7374dfb3055e.jpg)

「Success! The Event Webhook setting has been updated.」の表示がされ、Event WebhookのステータスがEnabledになったら設定は完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/03b6b79bc4c966a91252aa2304b7c21b.png)

## Kurocoの設定
ここからはKurocoの管理画面にて作業します。

### 6. KurocoとSendGridを連携する  
Kuroco管理画面にアクセスし、[チャネル] -> [メール] -> [SendGrid]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a9b92facaa18e63dfc55d7a529dcc8e.png)

[更新する]にチェックを入れて、「3. SendGrid APIKEYを確認する」で取得したSendGrid APIKEYを入力、送信許可ドメイン・メールアドレスは空にして[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50b61dbdde4377105eadb10d7cf7ebeb.png)

SendGrid との連携が完了すると、「2. 送信ドメインを認証する」で認証したドメインが表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9c749babb90eebeec79a28efb17c146.png)

### 7. 管理者メールの設定をする  
管理者メールに任意のメールアドレス、送信許可ドメインに送信元に使われるドメインを入力して更新します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0339f70a561aa759924556465b37624e.png)

## 管理者メールの変更を確認する
### 8. 招待メールを送信する  
[メンバーを招待する](/ja/docs/tutorials/how-to-invite-new-member/)のチュートリアルを参考に招待メールを送ります。

### 9. メールの送信元を確認する  
メールの送信元が設定した管理者メールになっていることを確認します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/38eb102108023955e33bd3cde42d3da6.png)

:::caution
SendGrid連携後すぐに大量のメールを送信すると、送信したメールは迷惑メールである可能性が高いと見なされ、受信拒否されることがあります。  
最初は少量〜中程度の量から配信し、次第に量を増やしていくことで、IPアドレスが正当な送信元であるというレピュテーション(メール送信者の信頼度)を得てください。  
詳しくはSendGridの[IPアドレスのウォームアップ](https://sendgrid.kke.co.jp/blog/?p=326)を参照してください。
:::

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGridログ](/ja/docs/management/sendgrid-log-list/)
- [メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？](/ja/docs/faq/can-i-use-my-custom-domain-for-the-sender-address/)
- [メール送信の料金はSendGridと契約していても発生しますか？](/ja/docs/faq/do-i-have-to-pay-for-sending-emails-even-if-i-use-sendgrid/)
- [SendGridと連携後、メール内のURLが勝手に置換されてしまいます。直せますか？](/ja/docs/faq/after-linking-with-sendgrid-url-in-email-is-replaced/)
- [Kurocoから送信されるメールが迷惑メールになってしまいます。解決方法を教えてください。](/ja/docs/faq/emails-sent-from-kuroco-are-going-to-spam-what-should-i-do/)


---

# 配信購読者の登録・停止フォームを作成する

> 元ページ: `tutorials/implement-a-magazine-subscription-unsubscription-form` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implement-a-magazine-subscription-unsubscription-form/
> 概要: Kurocoを利用したNuxt.jsプロジェクトで、配信機能の購読者を登録・解除するフォームを構築する方法について説明します。

## 概要
Kurocoを利用したNuxt.jsプロジェクトで、配信機能の購読者を登録・解除するフォームを構築する方法について説明します。  
配信の登録・解除を行う `MagazineSubscriber::subscribe/unsubscribe` のエンドポイントは`email`をポストするだけで動作しますが、
エンドポイントのURLが分かれば、他人のメールアドレスを登録・解除できてしまいます。

そこで本チュートリアルでは、ログインを必須にする方法と、keyを使って配信解除をする方法の2つを紹介します。

### 学べること
以下の2パターンで配信購読者の登録・解除をする動作を実装します。
- [ログイン必須の配信登録・解除を行う](#ログイン必須の配信登録解除を行う)
- [ログイン不要の配信登録・解除を行う](#ログイン不要の配信登録解除を行う)

### 前提条件
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  

:::info
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## ログイン必須の配信登録・解除を行う
配信の登録・解除をログイン状態でのみ動作するように実装します。  
ログイン必須(`self_only`の設定)にしたエンドポイントは`email`をpostしても動作せず、ログイン状態で自身の`member_id`をpostして配信の登録・解除を行います。

### エンドポイントの登録 
[新しいエンドポイントの追加]をクリックし、配信登録のエンドポイントと、ログインのエンドポイントを作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c309ffe7fab21034b04980537715d6e.png)

#### 配信登録のエンドポイント
以下の内容を設定し、「追加」をクリックします。

|項目|設定内容|
| :--- | :--- |
|パス|magazine_subscribe|
|カテゴリー|配信|
|モデル|MagazineSubscriber|
|オペレーション|subscribe|
|allow_magazine_id|1|
|self_only|チェックを入れる|

#### 配信解除のエンドポイント
以下の内容を設定し、「追加」をクリックします。

|項目|設定内容|
| :--- | :--- |
|パス|magazine_unsubscribe|
|カテゴリー|配信|
|モデル|MagazineSubscriber|
|オペレーション|subscribe|
|allow_magazine_id|1|
|self_only|チェックを入れる|

#### ログインのエンドポイント
ログインのエンドポイントはデフォルトで設定されているものを使用します。
無い場合は以下の内容でログインのエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|login|
|カテゴリー|認証|
|モデル|Login|
|オペレーション|login_challenge|

#### profileのエンドポイント
profileのエンドポイントはデフォルトで設定されているものを使用します。
無い場合は以下の内容でprofileのエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|profile|
|カテゴリー|認証|
|モデル|Login|
|オペレーション|profile|

### フロントエンドの実装
次に、フロントエンドにマガジンの配信登録フォームを作成します。  
`/subscribe_with_login`のディレクトリで表示できるよう以下のファイルを追加します。  

また、エラーメッセージはpostの処理のエラー時のレスポンスを受け取ることで、Kurocoのエラーメッセージをそのまま表示しています。

**Nuxt2:**

```markup reference title="/pages/subscribe_with_login/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/subscribe_with_login.vue
```

**Nuxt3:**

```markup reference title="/pages/subscribe_with_login/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/subscribe_with_login.vue
```


:::caution
上記サンプルのサンプルは参考のため最低限のコードになっています。  
実際に利用する際には、バリデーション処理や、ログイン機能のためにライブラリもご利用ください。
:::

### 動作の確認
#### 配信登録する
`npm run dev`を実行して動作の確認をします。  
`/subscribe_with_login`のURLでログイン実行後、[Subscribe]するをクリックすると、KurocoのエンドポイントにAPIリクエストが行われ、「登録しました。」の表示が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd56a892b26246738b786e268d5ee5b8.png)

[配信 購読者一覧](/ja/docs/management/notification-subscribers/)のページを確認すると、配信購読者が登録されていることが分かります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cc9fc769126af494232eb26086a9f54.png)

#### 配信解除する
次に[Subscribe]するをクリックすると、KurocoのエンドポイントにAPIリクエストが行われ、「退会しました。」の表示が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62bb09085cafb2601ede19c0241ccc85.png)

購読者一覧のページでも配信購読者が削除されていることが分かります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/91b7efec8ffb88ce3255bc77415a373c.png)

## ログイン不要の配信登録・解除を行う
配信登録はemailだけで登録できるようにし、配信解除は配信メッセージの[配信解除する]のリンクをクリックすることで解除するように実装します。  
未ログインでの配信解除では、他人の購読を勝手に解除できないよう購読者ごとに割り当てられたkeyを使用します。

keyは管理画面の[配信 購読者一覧](/ja/docs/management/notification-subscribers/)で確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdaa3a3355f3c63710afef940cf5c659.png)

### エンドポイントの登録 
[新しいエンドポイントの追加]をクリックし、配信登録のエンドポイントと、ログインのエンドポイントを作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2998d2bb87e501d4340442d27e668846.png)

#### 配信登録のエンドポイント
以下の内容を設定し、「追加」をクリックします。

|項目|設定内容|
| :--- | :--- |
|パス|magazine_subscribe_with_key|
|カテゴリー|配信|
|モデル|MagazineSubscriber|
|オペレーション|subscribe|
|allow_magazine_id|1|

#### 配信解除のエンドポイント
以下の内容を設定し、「追加」をクリックします。

|項目|設定内容|
| :--- | :--- |
|パス|magazine_unsubscribe_with_key|
|カテゴリー|配信|
|モデル|MagazineSubscriber|
|オペレーション|subscribe|
|allow_magazine_id|1|
|required_key|チェックを入れる|

### カスタム処理の作成
配信解除を行うためのkeyは[配信 購読者一覧](/ja/docs/management/notification-subscribers/)に表示されています。
このkeyを配信メッセージ内で使えるようにするためのカスタム処理を作成します。

[オペレーション] -> [カスタム処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cf05595e31dd0f905466ec2a09bb835.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|マガジンの差し込み(key,emailを使えるようにする)|
|識別子|substitution_key|
|これを使ったコンポーネント|トリガー: `配信の差し込み`<br/>値：1|
|処理|以下のコード|

```smarty
{assign_array var=substitutions values=''}
{assign var=substitutions.key   value=$member_info.key}
{assign var=substitutions.email value=$member_info.email}
```

### フロントエンドの実装
フロントエンドは配信登録用のページと、配信解除用のページを作成します。

まずは配信登録用のページを作成します。  
`/subscribe_with_key`のディレクトリで表示できるよう以下のファイルを追加します。  

**Nuxt2:**

```markup reference title="/pages/subscribe_with_key/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/subscribe_with_key.vue
```

**Nuxt3:**

```markup reference title="/pages/subscribe_with_key/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/subscribe_with_key.vue
```


次に配信解除用のページを作成します。  
`/subscribe_with_key/unsubscribe`のディレクトリで表示できるよう以下のファイルを追加します。

配信解除用のページは配信メッセージに記載したリンクからアクセスすることを前提としています。  

**Nuxt2:**

```markup reference title="/pages/subscribe_with_key/unsubscribe.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/subscribe_with_key_unsubscribe.vue
```

**Nuxt3:**

```markup reference title="/pages/subscribe_with_key/unsubscribe.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/subscribe_with_key_unsubscribe.vue
```


### 動作の確認
#### 配信登録する
`npm run dev`を実行して動作の確認をします。  
`/subscribe_with_key`のURLでemailを入力し[Subscribe]をクリックすると、KurocoのエンドポイントにAPIリクエストが行われ、「登録しました。」の表示が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8ad265a5f41cafd084bdb3a6ba430858.png)

[配信 購読者一覧](/ja/docs/management/notification-subscribers/)のページを確認すると、配信購読者が登録されていることが分かります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cd0bd810ac87636408dd72893ee148e.png)

#### 配信メッセージを送付する
[配信 メッセージ作成](/ja/docs/management/notification-message-editor/)から購読者宛に以下のメールを送付します。

```html
<p>Thank you for trying our service!</p>
<p>This email is sent from Kuroco. If you wish to unsubscribe, please click <a href="http://localhost:3000/subscribe_with_key/unsubscribe?email=%email%&key=%key%">here</a>.</p>
<p>Best regards,<br>Kuroco Team</p>
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca7121d24bd8b40f4daa00d4b9ddd4bb.png)

購読解除ページへのリンクが付いた配信メッセージが届きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/786defbce9bff6f5998b55990337765d.png)

#### メッセージに記載のリンクから購読解除する
リンクにアクセスすると、クエリパラメータに付与されたemailとkeyをKurocoのエンドポイントにAPIリクエストし、購読解除の処理が完了します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1ab3ab66ad2271eec4bacf1fe9244b8b.png)

以上で、配信機能の購読者を登録・解除するフォームを構築する方法についての説明を終了します。  

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧 - 配信の差し込み](/ja/docs/reference/trigger-variables/#配信の差し込み)


---

# コンテンツの特定項目が更新されたらメールで通知する

> 元ページ: `tutorials/notify-by-email-when-specific-items-in-the-content-are-updated` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/notify-by-email-when-specific-items-in-the-content-are-updated/
> 概要: assign_globalsのSmartyプラグインを使用すると、同一リクエスト中に呼び出されるトリガー間で共有可能なグローバル変数をアサインできます。これにより、コンテンツの更新前後の値を比較可能です。本チュートリアルではassign_globalsの使用例として、コンテンツの特定項目が更新されたらメールで通知する機能を実装してみます。

## 概要
`{assign_globals}`のSmartyプラグインを使用すると、同一リクエスト中に呼び出されるトリガー間で共有可能なグローバル変数をアサインできます。  
これにより、コンテンツの更新前後の値を比較可能です。  
本チュートリアルでは`{assign_globals}`の使用例として、コンテンツの特定項目が更新されたらメールで通知する機能を実装してみます。  


### 学べること
以下の手順で、コンテンツの特定項目が更新されたらメールで通知する機能を実装します。

- [コンテンツ定義に項目を設定する](#コンテンツ定義に項目を設定する)
- [カスタム処理を設定する](#カスタム処理を設定する)
- [動作を確認する](#動作を確認する)


## コンテンツ定義に項目を設定する
コンテンツ定義に比較対象となる拡張項目を設定します。  

以下の拡張項目を任意のコンテンツ定義に設定します。  

|項目名|項目設定|
|:--|:--|
|項目名|ステータス|
|Slug|status|
|項目設定|単一選択|
|選択項目|キー:1, 値:1<br/>キー:2, 値:2<br/>キー:3, 値:3|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15bc6ef8e833c01006b3739df73b372b.png)

コンテンツ定義の準備ができたらテスト用のコンテンツを追加しておきます。  

## カスタム処理を設定する

コンテンツの準備ができたら、カスタム処理を書いていきます。

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックして、「コンテンツの更新前」と、「コンテンツの更新後」のカスタム処理を作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/081fc0268e7eb56c48655784102a17d6.png)

### コンテンツの更新前

コンテンツの更新前に動作し、更新前のコンテンツの値をグローバル変数にアサインする処理を書きます。  

|項目|値|
|:--|:--|
|タイトル|capture_before_update_content|
|識別子|capture_before_update_content|
|トリガー|コンテンツの更新前/対象のコンテンツ定義IDを指定|
|処理|以下の内容|

```smarty reference title="capture_before_update_content"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/pre-processing/capture_before_update_content.txt
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6ac37e6e54cccf24dc16614986649f5.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

### コンテンツの更新後

コンテンツの更新後に動作し、更新後の値と、グローバル変数にアサインした更新前の値を比較して、変更があった場合は通知メールを送信する処理を書きます。

|項目|値|
|:--|:--|
|タイトル|compare_before_and_after_content|
|識別子|compare_before_and_after_content|
|トリガー|コンテンツの更新後/対象のコンテンツ定義IDを指定|
|処理|以下の内容|

```smarty reference title="compare_before_and_after_content"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/post-processing/compare_before_and_after_content.txt
```

:::caution
`to='test@example.com'`の部分はご自身の通知先に変更してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bcc8de8d4e6bd733711e14663b601ae.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

## 動作を確認する

テスト用に追加したコンテンツのステータスの項目を更新すると、以下のように更新前後の値が通知されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/122a8706c07c5b713a84f37bce98d043.png)

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# お問い合わせの受信通知をChatworkで送信する

> 元ページ: `tutorials/send-chatwork-notification-after-a-form-has-been-submitted` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/send-chatwork-notification-after-a-form-has-been-submitted/
> 概要: Kurocoは自由にAPIを作成でき、さらに外部のAPIにリクエストを送るプラグインを持っているため、外部システム連携に表示されていないサービスについても、カスタム処理やバッチ処理に動作を記述することで利用が可能です。本チュートリアルはその例として、Chatworkに投稿をするカスタム処理を自作し、お問い合わせの受信通知をChatworkへ投稿する方法について説明します。

## 概要
Kurocoは自由にAPIを作成でき、さらに外部のAPIにリクエストを送るプラグインを持っているため、外部システム連携に表示されていないサービスについても、カスタム処理やバッチ処理に動作を記述することで利用が可能です。  
本チュートリアルはその例として、ChatWorkに投稿をするカスタム処理を自作し、お問い合わせの受信通知をChatworkへ投稿する方法について説明します。

### 学べること
以下の手順でお問い合わせの受信通知をChatworkへ投稿します。
- [Chatworkの設定](#chatworkの設定)
- [Kurocoの設定](#kurocoの設定)
- [動作確認](#動作確認)

## Chatworkの設定
### ボット用のアカウントを作成する
Chatwork APIを利用した投稿の投稿者は、APIトークンを作成したアカウントになります。
そのため、まずは[Chatwork](https://www.chatwork.com/service/packages/chatwork/pre_register.php?plan=free&lang=ja&page=login)で、通知の送信元となるボット用のアカウントを作成してください。  

アカウントができたら、プロフィールから写真と名前を設定しておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2611a6795bf373130272b15b30320562.png)

### 通知が送付されるグループを作成する
つぎに、通知を受け取るためのグループチャットを作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f50f917a19e1c038d1d9ed8b355a326.jpg)

準備ができたらグループチャットの設定からルームIDを控えておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4fec81c5b691217281b73549e713706.png)

### APIトークンを取得する

[Chatwork APIへようこそ！](https://developer.chatwork.com/docs)にアクセスし、画面下部の[APIの利用申請]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a72c21d193266d90d3072e1a0293be9e.png)

ボット用のアカウントでログインすると、[APIトークン](https://www.chatwork.com/service/packages/chatwork/subpackages/api/token.php)のページに遷移し、APIトークンの確認ができます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f86ab5b2522ab3b034e7d3b2549a1dea.png)

## Kurocoの設定
### APIトークンを保存する
Kurocoの管理画面にアクセスし、[環境設定] -> [シークレット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/25b831fd4835ad993f02298629b9e8cf.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c51de1ecc8ead6fa837c6492757a7276.png)

以下のように入力して、[追加する]をクリックします。

|項目|値|
|:--|:--|
|名前|CHATWORK_API_TOKEN|
|値|Chatworkで取得したAPIトークン|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a20d882a89cb1204ace2421b56eddc0b.png)

### Chatworkに投稿をするカスタム処理を作成する
カスタム処理を利用して、Chatworkに投稿をする処理を自作します。  

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

以下のように設定します。

- カスタム処理は`{function}`のSmartyプラグインを利用して他のカスタム処理やバッチ処理から呼び出されることを前提としています。
- 通知送信先のroom_idと、送信する本文を、`room_id`と`text`の変数で受け取ります。
- `{return value=$status}`で処理の結果を返します。

|項目|値|
|:--|:--|
|タイトル|chatwork_post_message|
|識別子|chatwork_post_message|
|処理|以下の内容|

```smarty reference title="chatwork_post_message"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/function/chatwork_post_message.txt
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/97a244a7a0121530b2bbce76da40d5e0.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

### メッセージひな形を調整する
[オペレーション]->[メッセージひな形]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/337cb4628fc2f37ee59dc4658cd307f2.png)

[問い合わせ着信通知メール(管理者宛)]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74024a7550367129d8790615f1acdd10.png)

本文の冒頭に以下の記述を追加します。  

```smarty
{*Chatwork通知*}
{capture name=chatwork_text_body}
[toall]
「{$inquiryHeader.inquiry_name}」へのお問い合わせが届きました。
内容を確認してください
{$smarty.const.ROOT_MNG_URL}/management/inquiry/inquiry_reply_edit/?inquiry_bn_id={$inquiry_bn_id}
{/capture}
{function name='chatwork_post_message' room_id="123456789" text=$smarty.capture.chatwork_text_body var=status}

{*メール通知*}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b466f806b29696f68da79420ad309a0.png)

:::caution
room_idはご自身の環境のIDを利用してください。
:::

設定ができたら[更新する]をクリックして変更を反映します。  

#### TIPS
- メール通知を止めてChatwork通知のみにしたい場合は、[独自設定]から[メールの送信停止]に1をセットします。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/b43255e192879ef128775e90a6fc855c.png)
- Chatworkでメンションを`ToALL`にする場合は`[toall]`と書きます。  
- Chatworkでメンションを個人宛にする場合は`[To:{account_id}]`と書きます。

### フォーム基本設定を設定する
[チャネル] -> [WEB] -> [フォーム]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォームのタイトルをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00f449ac3c9e94e4b7f46bc9481ad3b1.png)

基本設定タブの配信先メールアドレスで、[通知する]にチェックを入れてメールアドレスとタイトルを入力します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/49aed60abf6e495cb8a19f4ea9b2c97a.png)


## 動作確認
最後に動作確認をします。  
管理者宛の通知を有効にしたフォームへ回答の送信をすると、メールの通知に加えて、Chatworkチャンネルへの通知が行われます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57b48281a35a9775353628104d616eea.png)

以上でお問い合わせの受信通知をChatworkで送信できました。  

同様の方法でKurocoの任意の動作をトリガーにChatWorkへ投稿できますのでお試しください。  

## 関連ドキュメント
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# お問い合わせの受信通知をSlackで送信する

> 元ページ: `tutorials/send-slack-notification-after-a-form-has-been-submitted` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/send-slack-notification-after-a-form-has-been-submitted/
> 概要: KurocoはSlackとのAPI連携機能を持っています。API連携をするとSlackのメッセージの読込及び、Slackチャンネルへの投稿が容易に行えるようになります。

## 概要
KurocoはSlackとのAPI連携機能を持っています。  
API連携をするとSlackのメッセージの読込及び、Slackチャンネルへの投稿が容易に行えるようになります。  

ここではSlackと連携して、お問い合わせの受信通知をSlackへ投稿する方法について説明します。

### 学べること
以下の手順でお問い合わせの受信通知をSlackへ投稿します。
- [SlackアプリとKurocoの連携](#slackアプリとkurocoの連携)
- [Kurocoの設定](#kurocoの設定)
- [動作確認](#動作確認)

## SlackアプリとKurocoの連携

Slackアプリの作成からBot User OAuth Tokenの取得、Kurocoへの設定までは共通手順です。  
[SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)を参照して実施してください。

お問い合わせの受信通知にはSlackへのメッセージ投稿のみを利用するため、Appマニフェストは同ページに記載の例（`KurocoNotification`）をそのまま利用できます。  
また、通知を受けるSlackチャンネルへのAppの追加も同ページの[Slackチャンネルへアプリの追加](/ja/docs/tutorials/create-slack-app-and-get-bot-token/#slackチャンネルへアプリの追加)を参照してください。

連携設定が完了したら、以下のKurocoの設定に進みます。

## Kurocoの設定
### メッセージひな形の調整
[オペレーション]->[メッセージひな形]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/337cb4628fc2f37ee59dc4658cd307f2.png)

[問い合わせ着信通知メール(管理者宛)]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74024a7550367129d8790615f1acdd10.png)

本文の冒頭に以下の記述を追加します。  

```smarty
{*Slack通知*}
{capture name=slack_text_body}
<!here>
「{$inquiryHeader.inquiry_name}」へのお問い合わせが届きました。
内容を確認してください
{$smarty.const.ROOT_MNG_URL}/management/inquiry/inquiry_reply_edit/?inquiry_bn_id={$inquiry_bn_id}
{/capture}
{slack_post_message channel='お問い合わせ通知' text=$smarty.capture.slack_text_body}

{*メール通知*}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a928b0f6e1bdbde721d3660f4c2f2a9.png)

設定ができたら[更新する]をクリックして変更を反映します。  

#### TIPS
- メール通知を止めてSlack通知のみにしたい場合は、[独自設定]から[メールの送信停止]に1をセットします。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/b43255e192879ef128775e90a6fc855c.png)
- Slackでメンションを`@channel`にする場合は`<!channel>`と書きます。  
- Slackでメンションを個人宛にする場合は`<@SlackのメンバーID>`と書きます。

### フォーム基本設定
[チャネル] -> [WEB] -> [フォーム]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォームのタイトルをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00f449ac3c9e94e4b7f46bc9481ad3b1.png)

基本設定タブの配信先メールアドレスで、[通知する]にチェックを入れてメールアドレスとタイトルを入力します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/49aed60abf6e495cb8a19f4ea9b2c97a.png)

## 動作確認
最後に動作確認をします。  
管理者宛の通知を有効にしたフォームへ回答の送信をすると、メールの通知に加えて、Slackチャンネルへの通知が行われます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/65afa4dd8c3c67fe40237c8e0081cb4d.png)

以上でお問い合わせの受信通知をSlackで送信できました。  

同様の方法で承認ワークフロー等の他の通知もSlack通知にできますのでお試しください。  

## 関連ドキュメント
- [SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)


---

# メールマガジンを送付する

> 元ページ: `tutorials/sending-email-notifications` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/sending-email-notifications/
> 概要: 配信の機能で、簡単にメールマガジンを作成・配信することができます。配信毎に配信先を設定でき、送信日時の指定も可能です。

配信の機能で、誰でも簡単にメールマガジンを作成・配信できます。
配信毎に配信先を設定でき、送信日時の指定も可能です。

## メールマガジンを送付する
### 1. 配信一覧のページにへアクセスする
[チャネル] -> [一括配信] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

### 2. 配信を追加する
[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f0aaf83875451b80f221b8e9d934902.png)

[配信 基本設定](/ja/docs/management/notification-basic-settings/)のページを参考に配信の基本設定を入力します。

:::tip
「デフォルトのあて先」は配信追加後に設定しますので、ここでは空欄で大丈夫です。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6edca62315483205a10e0bb48fae1907.jpg)

[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/27fd6a16643aeeff94386d9e2df7cae1.png)

### 3. 検索条件を登録する
[カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)のチュートリアルを参考に検索条件を登録します。  
ここでは例として「全ての会員宛」という条件を登録しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9810a70f90c9114b12952a8e7ed6923.png)

### 4. 購読者を登録する
[配信の購読者を登録する](/ja/docs/tutorials/how-to-register-subscribers-on-magazine/)のチュートリアルを参考に購読者を登録します。

### 5. デフォルトのあて先を設定する  
配信の基本設定を開きます。  
「デフォルトのあて先」の条件選択ドロップダウンリストに登録されている検索条件が表示されるので、あて先に設定したい検索条件を選択します。  
ここでは、先ほど3.で作成した「全ての会員宛」を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/851f5981863ca01151d304591e488a96.png)

検索条件を選択後、[あて先を設定する]をクリックすると左欄へ追加されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05b3e4f156fd29ffea9c636c0b6855bd.png)

あて先を削除したい場合は、[削除する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57fa1e39916e0e61f7eeca59e37f8b58.png)

[送信対象者を確認]をクリックし、配信の送付先を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d486875a776c77bd3d76c2080be1ead.png)

問題なければ[更新する]をクリックし、設定内容を反映させます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/313c24683f015e8ad3c83cad983b8c49.png)

### 6. メッセージを作成し、配信する  
追加した配信のページから[追加]をクリックし、[配信メッセージ作成](/ja/docs/management/notification-message-editor/)を参考に必要事項を入力します。  

この時にあて先の追加・削除も可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d5669f42022005c456b75cf7fc6b1ce.jpg)

入力が完了したら[送信待ちにする]をクリックして完了です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fef008bdee840bddbf5e3f48afcddfc1.png)

設定した時間になるとメールマガジンが配信されます。

### 7. 配信を確認する 
配信メッセージ一覧のページで配信したメールマガジンの送信数を確認します。  
各項目の詳細は[配信メッセージ](/ja/docs/management/notification-messages/)をご確認ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5968241b99bf6b9694137c03ae3d44ec.png)

## 関連ドキュメント
- [配信 基本設定](/ja/docs/management/notification-basic-settings/)
- [配信 メッセージ作成](/ja/docs/management/notification-message-editor/)
- [配信メッセージ](/ja/docs/management/notification-messages/)
- [配信の購読者を登録する](/ja/docs/tutorials/how-to-register-subscribers-on-magazine/)
- [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)
- [配信購読者の登録・停止フォームを作成する](/ja/docs/tutorials/implement-a-magazine-subscription-unsubscription-form/)
- [メール配信時の件数制限はありますか。](/ja/docs/faq/is-there-a-limit-to-the-number-of-e-mails-i-can-send/)


---

# フォームの回答を送付したユーザー向けに配信メッセージを送付する

> 元ページ: `tutorials/sending-notification-messages-to-users-who-submitted-form-responses` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/sending-notification-messages-to-users-who-submitted-form-responses/
> 概要: Kurocoはフォームの回答を送付したユーザーを自動的にメンバー登録する機能を持っています。こちらを利用することで、セミナー申込をしたメンバー宛に配信メッセージを送るといった作業が容易に行えます。

## 概要  
Kurocoはフォームの回答を送付したユーザーを自動的にメンバー登録する機能を持っています。  
こちらを利用することで、セミナー申込をしたメンバー宛に配信メッセージを送るといった作業が容易に行えます。  

本チュートリアルでは、回答を送付したユーザーを自動的にメンバー登録させる設定と、配信メッセージの送付方法について紹介します。

### 学べること
以下の手順でフォームの回答を送付したユーザー宛にメッセージを送付する流れを学びます。  

- [回答を送付したユーザーを自動で登録する](#回答を送付したユーザーを自動で登録する)
- [回答を送付したユーザー宛に配信メッセージを送る](#回答を送付したユーザー宛に配信メッセージを送る)

## 回答を送付したユーザーを自動で登録する
### ユーザーが所属するグループを作成する
まずは回答を送付したユーザーが会員登録される際に所属するグループを作成します。  

[メンバー管理]->[グループ]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f8b00e23ad1344bfe69c7c3dd76a3552.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e91c710371e73b065b207849bcc9a04.png)

以下のように入力します。

|項目|値|
|:--|:--|
|名前|セミナー申込書|
|ユーザー種別|ログインユーザー|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a93d05e0911dda6ade828b2d74e31516.png)

入力ができたら[追加する]をクリックしてグループを追加します。

### フォームを作成する
次にフォームの作成をします。  
[チャネル] -> [WEB] -> [フォーム]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/754ebf740af5218f923552ece41bc1b6.png)

以下のように入力します。

|項目|値|
|:--|:--|
|名前|セミナー参加申し込みフォーム|
|自動ユーザ登録|[有効にする]にチェックを入れて、先ほど作成したグループ(セミナー申込者)を設定|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dff8d5923754d33cb77be501cdbe3581.jpg)

入力ができたら[追加する]をクリックしてフォームを追加します。

今回のチュートリアルでは、フォームの基本設定はデフォルトのまま利用するため基本設定の更新は不要です。  
以下のように`name`、`email`、`message`の項目のみを利用します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/49d8e70c8adc916901a834a15d6b62a1.png)


### エンドポイントを作成する
次にフォームに回答を送付するエンドポイントを作成します。    
[API]->[Default]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c286873648f4bc2e833918284ef2940f.png)

[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21831b02823d8ec43ef328ba8c998ad7.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|seminar_application|
|カテゴリー|フォーム|
|モデル|InquiryMessage|
|オペレーション|send|
|id|先ほど作成したフォームのID (3)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c44e8e66311750960ce52fba6c64d802.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee467366fca91f6fd68898614acb99f9.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

### フォームの送付をする
DefaultのAPIの[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c770e6f045b3783f004fe3f4fed8af8.png)

作成したエンドポイントの[Try it out]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/83a94c286a18ff35b1ef61f8f8254d6e.png)

Request bodyに以下を入力して[Execute]をクリックします。

```json
{
  "name": "Diverta Jiro",
  "email": "email@example.com",
  "body": "Example Message"
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa5b9dd5a7ea7eac45589bc7459f9dd8.png)

"新規追加しました"と回答IDの表示を確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6535dee1dfd693edbcb39fc04972826.png)

[メンバー管理]->[メンバー]にアクセスすると、先ほどフォームを送付したユーザーが追加されていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbc0c7b1150fd9d29385bdb61b86c977.png)

動作の詳細は以下になります。  


- ログイン済みの場合、設定対象グループを追加
- 未ログイン、かつemailがPOSTされた場合
  - 該当emailのメンバーあり：member_idを取得し、回答データと紐づけ
  - 該当emailのメンバーなし：
    - メンバー登録をし、 追加したmember_idと回答データを紐づけ
    - 登録対象データはemail、name1、name2、email_send_ng_flg（0固定）
    - フォーム送信のnameは半角スペース区切りでname1, name2に値が設定されます。
    - nameが無い場合はemailの@マーク以前がname1 (姓) に設定されます。


同様の手順で確認用のユーザーをいくつか登録しておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/43fa656011ed68af77c9b7c8954a50b0.png)

## 回答を送付したユーザー宛に配信メッセージを送る
前のステップで回答を送付したユーザーを特定のグループに所属させて会員登できましたので、このグループ宛に配信メッセージを送付します。  

### カスタムメンバーフィルターを作成する
[メンバー管理]->[カスタムメンバーフィルター]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a77cd92df900585cdd061174f0d9405.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/40cca01c137060f45e847249a1bd2410.png)

以下のように入力します。

|項目|値|
|:--|:--|
|名前|セミナー申込者宛|
|アクセス制限|全体|
|絞り込み条件作成|`グループ` `どれかを含む` `セミナー申込者`|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b5b566c92a025daa378aa0cebfbb9f8b.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2bab50e73c229c956b3b4f1f2425c1f.png)

入力ができたら[追加する]をクリックしてカスタムメンバーフィルターを追加します。

### 配信を作成する
続いてセミナー申込者宛にメッセージを送る配信を追加します。  
[チャネル] -> [一括配信]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff23ba1a86a74a08a41a0cf0117eb789.png)

以下のように入力します。

|項目|値|
|:--|:--|
|名前|セミナー申込者宛の連絡|
|メール送信元(From)|`noreply@kuroco-mail.app`|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/744a54e37dd0388673ff681d20c3bc53.png)

入力ができたら[追加する]をクリックしてカスタムメンバーフィルターを追加します。

続いてデフォルトの宛先として、先ほど作成したカスタムメンバーフィルター(セミナー申込者宛)を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3c27e74bc72b483130a21df539c5cbe.gif)

設定ができたら[更新する]をクリックして設定を反映します。  

### メッセージを送付する
配信の基本設定から、[メッセージ]タブをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/247fb270232bdcfce350a5a7d5efdab1.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0af5d4341ee62ccdb26c1f4b94ded087.png)

送信日時、件名、本文を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f04f2a02d12e518509830ad93b7a8cf7.jpg)


[送信対象者を確認]をクリックし、配信メッセージの通知先を確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cf4d96e64efdca1c378aed1586262169.png)

問題がなければ[送信待ちにする]をクリックします。  

指定した送信日時になるとメッセージが送付されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/79235705aefd9ba4ea0c25b5589cdff7.png)

以上で、フォームの回答を送ったユーザー宛に配信メッセージを送る流れが分かりました。  
フォームの項目設定、実装、お礼メールのカスタマイズや、配信メッセージの編集等は関連ドキュメントを参考に調整してください。  

## 関連ドキュメント
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)
- [カスタム処理に利用できる変数一覧(配信の差し込み)](/ja/docs/reference/trigger-variables/#配信の差し込み)
- [フォーム送信によりメンバー登録されるユーザーのメンバー情報にフォームの回答内容を設定する](/ja/docs/tutorials/how-to-implement-original-function-into-the-member-info-when-form-send-with-member-regist/)
