# Kurocoドキュメント: チュートリアル / 外部サービス連携（1/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Amazon S3と連携して、Storageにファイルを保存する（`amazon-s3`）
- Instagram基本表示APIをkurocoから呼び出してInstagramのフィードを表示する（`call-the-instagram-basic-display-api-from-kuroco`）
- HARファイルを作成する（`create-a-har-file`）
- Firebaseと連携して、Storageにファイルを保存する（`firebase`）
- GitHubActionsでgenerateに失敗した場合に、ビルドを中止しSlackに結果を通知する方法（`handling-a-generate-error-in-github-actions`）
- LINEユーザーにメッセージを送付する（`how-to-connect-to-line`）
- Twilioと連携してSMSを送信する（`how-to-connect-to-twillio`）
- Vimeoと連携して動画をアップロードする（`how-to-connect-to-vimeo`）
- GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法（`how-to-implement-ranking-with-google-analytics`）
- Google Analytics連携方法（`how-to-link-google-analytics`）


---

# Amazon S3と連携して、Storageにファイルを保存する

> 元ページ: `tutorials/amazon-s3` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/amazon-s3/
> 概要: Amazon S3と連携し、Kurocoからアップロードした画像や動画ファイルをAmazon S3に保存する方法を説明します。

Amazon S3との連携方法を解説します。  
Amazon S3と連携することで、Kurocoからアップロードした画像や動画ファイルを、Amazon S3のStorageに格納し利用できます。  

## Amazon S3の設定
### バケットを作成する
[Amazon S3のサイト](https://aws.amazon.com/jp/s3/)へアクセスし、[Simple Storage Service (Amazon S3) の使用を開始する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/49626f199a6c7cc6312ebba11ef0fe89.png)
ルートユーザーでサインインします。  
AWSのアカウントを持っていない場合は[こちら](https://portal.aws.amazon.com/billing/signup)からサインアップしてください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00eb9f9bcfc73024acb0803aa888f3a2.png)
[バケットを作成]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0038b186b7e2fccebf45d11f03c2126b.png)
以下のように設定し、[バケットを作成]をクリックします。  

|項目  |値  |
| :--- | :--- |
|バケット名|任意の名称を入力する。(本チュートリアルでは`kuroco-sample`)<br/>※バケット名に`.`(ドット)は使用しないでください。|
|AWSリージョン|アジアパシフィック (東京) ap-northeast-1|
|オブジェクト所有者|[ACL有効]にチェックを入れる。<br/>[希望するバケット所有者]を選択する。|
|このバケットのブロックパブリックアクセス設定|・パブリックアクセスをすべて ブロック：チェックを外す<br/>・新しいアクセスコントロールリスト (ACL) を介して付与されたバケットとオブジェクトへのパブリックアクセスをブロックする：チェックを外す<br/>・任意のアクセスコントロールリスト (ACL) を介して付与されたバケットとオブジェクトへのパブリックアクセスをブロックする：チェックを外す<br/>・新しいパブリックバケットポリシーまたはアクセスポイントポリシーを介して付与されたバケットとオブジェクトへのパブリックアクセスをブロックする：チェックを入れる<br/>・任意のパブリックバケットポリシーまたはアクセスポイントポリシーを介したバケットとオブジェクトへのパブリックアクセスとクロスアカウントアクセスをブロックする：チェックを入れる|
|パブリックアクセスのブロックをすべてオフにすると、このバケットとバケット内のオブジェクトが公開される可能性があります。|[現在の設定により、このバケットとバケット内のオブジェクトが公開される可能性があることを承認します。]にチェックを入れる|


<a href="https://diverta.gyazo.com/8d33c1a276df94b9b7912c4cb97478f3" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://t.gyazo.com/teams/diverta/8d33c1a276df94b9b7912c4cb97478f3.png" alt="Image from Gyazo" /></a>

### Cross-Origin Resource Sharing (CORS)の設定をする
続いて、Amazon S3のCORSの設定をします。  
Amazon S3のバケットページから先ほど作成したバケット名をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2e9ceadd2137c21deffa6ef914a187e.png)

[アクセス許可]のタブをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7fa437f4f0775afb9cab52c4960ae3c5.png)

[Cross-Origin Resource Sharing (CORS)]の[編集]をクリックします。  

<a href="https://diverta.gyazo.com/dca9acdb2f77169a6221e4b3a50f85db" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://t.gyazo.com/teams/diverta/dca9acdb2f77169a6221e4b3a50f85db.png" alt="Image from Gyazo" /></a>

Cross-Origin Resource Sharing (CORS)の編集画面が表示されるので、下記を設定します。  

:::caution
`https://****.g.kuroco-mng.app`の部分はご自身のKuroco管理画面のURLにしてください。  
:::

```json
[
    {
        "AllowedHeaders": [
            "Content-Type",
            "x-amz-acl",
            "x-amz-meta-*",
            "Origin"
        ],
        "AllowedMethods": [
            "GET",
            "POST",
            "HEAD"
        ],
        "AllowedOrigins": [
            "https://****.g.kuroco-mng.app"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71ab976bc07851ed801e32103d5733a9.png)
入力が完了したら[変更の保存]をクリックします。

### ポリシーを作成する
次に、ポリシーを作成し、Kurocoに与えるアクセス許可の内容を定義します。  
画面右上のユーザ名から[セキュリティ認証情報]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/86d4cd611b390fd220f060657afca782.png)  
[ポリシー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0d648f6500f383f939a5cbb5109fccb.png)
[ポリシーの作成]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffa28860a7d4754a756fb3d65db289c8.png)
ポリシーの作成画面が表示されるので、JSONのタブを開き、下記を設定します。  
`%%yourbucket%%`の部分は該当バケット名にしてください。(本チュートリアルでは`kuroco-sample`)    

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::%%yourbucket%%"
        },
        {
            "Action": [
                "s3:*"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::%%yourbucket%%/*"
            ]
        }
    ]
}
```

:::caution
`%%%yourbucket%%`の部分はご自身のバケット名にしてください。
:::

入力が完了したら[次のステップ：タグ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c821833fa5e747935316ca1ee6bd8b4b.png)  
タグについては設定不要なので、そのまま[次のステップ：確認]をクリックして進みます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9c9137711755fb801e0f7b18cd89f12.png)
ポリシーの確認ページが表示されるので、名前の項目を入力して[ポリシーの作成]をクリックします。  
今回は`kuroco-s3`という名前を付けました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f0bf093a1abe932ad03460574597219.png)
### アクセスキーを作成する
次に、Kurocoと接続するためのアクセスキーを作成しますが、ルートユーザーでのアクセスキー作成は、AWSアカウント全体への無制限アクセスが可能になるため、推奨されていません。  
そこで、制限されたアクセス許可を持つ新しい IAM ユーザーを作成し、そのユーザーのアクセスキーを生成するようにします。  

[ユーザー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/86ed66650898db6a9f2bcf096315d4e7.png)
[ユーザーを追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9be83b03059fdd787db5f26c8b7e0f9c.png)
ユーザー名を入力し、AWS 認証情報タイプは[アクセスキー - プログラムによるアクセス]を選択し、[次のステップ：アクセス権限]をクリックします。  

|項目  |値  |
| :--- | :--- |
|ユーザー名|kuroco-sample-admin|
|AWS 認証情報タイプを選択|[アクセスキー - プログラムによるアクセス]にチェックを入れる|  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/519fe55b4bc6b223501957ced4c0e6f9.png)
[既存のポリシーを直接アタッチ]を選択し、先ほど作成したポリシーを検索して選択し、[次のステップ：タグ]をクリックします。    

|項目  |値  |
| :--- | :--- |
|アクセス許可の設定|既存のポリシーを直接アタッチ|
|ポリシー名|kuroco-s3 を選択|  
|アクセス権限の境界の設定|アクセス権限の境界を設定せずにuserを作成するを選択|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f87207872c7674b4fb6cb22d956390a.png)
タグについては設定不要なので、そのまま[次のステップ：確認]をクリックして進みます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0ff8d657b0143b2c54dd9076217fb8d.png)
内容を確認し、[ユーザーの作成]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca26fc2b8a316f22111205c56e7c4607.png)
ユーザーが作成されたら「アクセスキー ID」と「シークレットアクセスキー」が表示されるので、メモをして[閉じる]をクリックします。  

:::caution
シークレットアクセスキーは画面を閉じると再表示できませんので、ご注意ください。  
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e1e998fa255b9d100d1fd61fd99d52e.png)
## Kurocoの設定

ここからはKurocoの管理画面にて作業をします。  
[外部システム連携]->[Amazon S3]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/505e5e28b7f47b69ebda09bfba90eb79.png)
Amazon S3との連携画面が表示させるので、「バケット名」「アクセスキーID」「シークレットアクセスキー」を入力して[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dc1211ffcf0a1be4300d49ca13e496bd.png)

## 利用方法
### ファイル
接続完了後、[ファイルマネージャー]をクリックすると、S3の表示が確認でき、ファイルをアップロードできます。    
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b57e42c37820e1896c8b9e3a77f9ce0.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7987e145471d180ad17c428881f90813.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab16cd4471744868cd66b2ed0b267ec4.png)

### コンテンツ定義
#### ファイル（S3にアップロード）
Kuroco管理画面の[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)より、設定項目で[ファイル（S3にアップロード）]を選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3b638146b86647e735c2a1de6a3e8d7c.png)
コンテンツ編集画面にファイルアップロードフィールドが表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c77fbd9036d4b4b6053be9111c13d61c.png)
こちらからファイルをアップロードすると、Amazon S3のStorageにファイルがアップロードされるようになります。

#### WYSIWYG
WYSIWYG項目の全般設定で「リソースを指定」にS3のパスを入力すると、WYSIWYGからアップロードしたファイルが指定したS3のフォルダに保存されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/939d61087f02b0566c541c5d30fb39a7.png)

## 関連ドキュメント
- [Amazon S3](/ja/docs/management/amazon-s3/)
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [GCS, S3に設定したファイルの有効期限について](/ja/docs/reference/expiration-for-files-in-gcs-and-s3/)


---

# Instagram基本表示APIをkurocoから呼び出してInstagramのフィードを表示する

> 元ページ: `tutorials/call-the-instagram-basic-display-api-from-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/call-the-instagram-basic-display-api-from-kuroco/
> 概要: Kurocoは自由にAPIを作成でき、さらに外部のAPIにリクエストを送るプラグインを持っているため、外部システム連携に表示されていないサービスについても、カスタム処理やバッチ処理に動作を記述することで利用が可能です。本チュートリアルはその例として、Instagram基本表示APIを利用してみます。

:::caution
Instagram基本表示APIは廃止されました。  
任意のサービスと連携する場合の参考としてご利用ください。
:::

## 概要
Kurocoは自由にAPIを作成でき、さらに外部のAPIにリクエストを送るプラグインを持っているため、外部システム連携に表示されていないサービスについても、カスタム処理やバッチ処理に動作を記述することで利用が可能です。  
本チュートリアルはその例として、Instagram基本表示APIを利用してみます。

kurocoの外部システム連携にInstagramの項目はありませんが、`{api}`のプラグインでInstagram基本表示APIにリクエストを送ることで、Instagramのフィードを表示します。  

### 学べること
以下の手順でInstagramのフィードを表示します。 
- [Instagramの設定](#instagramの設定)
- [Kurocoの設定(事前準備)](#kurocoの設定事前準備)
- [KurocoとNuxt.jsで認証の動作を実装する](#kurocoとnuxtjsで認証の動作を実装する)
- [Kurocoで定期的にInstagramのフィードを取得する](#kurocoで定期的にinstagramのフィードを取得する)
- [Kurocoで定期的に長期アクセストークンを更新する](#kurocoで定期的に長期アクセストークンを更新する)
- [KurocoとNuxt.jsでInstagramのフィードを表示する](#kurocoとnuxtjsでinstagramのフィードを表示する)

### 前提条件
以下のアカウントが必要になりますので、持っていない場合はアカウントを作成してください。  
- Facebook開発者アカウント。
- Instagramアカウント。

また、このページはKurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。
まだ構築していない場合は、下記のチュートリアルを参照してください。
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)

:::caution
Instagram基本表示APIは[公式ドキュメント](https://developers.facebook.com/docs/instagram-basic-display-api)を参考に実装しています。  
差分があった場合は公式ドキュメントの記載を優先させて下さい。
:::

## Instagramの設定
### Facebookアプリを作成する
[developers.facebook.com/apps](https://developers.facebook.com/apps/)にアクセスし、[アプリを作成]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e7787b7275b15e5e1b5061cd001a3b2.png)

[その他]を選択して[次へ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/64d800687eab7d1179073a30c6d39c6c.png)

アプリタイプは[なし]を選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9a1bca189a6f250f1bac06c6e8034ec6.png)

アプリ名を入力して[アプリを作成]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9a697e2452fde1ec32e2db311d4b3afe.png)

アプリが作成されてアプリダッシュボードが表示されたら、[設定] -> [バーシック]に移動し、ページの下までスクロールして[プラットフォームを追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c85d08e97f256e64df1d310028bb8274.png)

Websiteを選択して[次へ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4c80879989084d07122e30ac651bf61.png)

サイトURLの入力欄が表示されるので、KurocoのフロントエンドURLを入力して[変更を保存]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a92593f8cca7428526048589496349b6.png)

### Instagramアプリを作成する
ダッシュボードに戻り、製品を追加の項目からInstagram Basic Displayを探して[設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/202c3ac63f5ac06582189782f74dfed3.png)

ページの下部にスクロールして[Create New App]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3936da409d4a13a4fc43f209dd678274.png)

Facebookアプリのアプリ名が表示されているので、そのまま[アプリを作成]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/527612dd2b571e3640aa19aff9594712.png)

Instagramアプリが作成されたら、「有効なOAuthリダイレクトURI」「コールバックURLの許可の取り消し」「データの削除リクエストURL」に`https://フロントエンドURL/auth/`のURLを入力し、[変更を保存]をクリックします。  
「コールバックURLの許可の取り消し」「データの削除リクエストURL」は、最終的にはその処理をできるURLに変更しますが、ここではOAuthリダイレクトURIと同じにして構いません。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f5dcf192b723c19ea67e816b8be2ae3.png)

### Instagramテストユーザーを追加する
[アプリの役割]->[役割]に遷移し、下にある[Instagramテスター]セクションまでスクロールして、[Instagramテスターを追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef14b34ef4bf156d76a5afde3263815e.png)

Instagramアカウントのユーザーネームを入力し、送信をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8726032780be7b73b71331c18b18e26b.png)

[www.instagram.com](https://www.instagram.com/)にアクセスして、先ほど招待したInstagramアカウントにサインインします。(プロフィールアイコン) -> [プロフィールを編集] -> [アプリとウェブサイト] -> [テスターの招待]に移動し、招待を受け入れます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0948189110495bf78410047cb6d2f5b6.png)

これで、Instagramアカウントは、開発モードになっていても、Facebookアプリからアクセスできるようになりました。

### 処理の流れの確認 
ユーザーの認証から、長期Instagramユーザーアクセストークンの取得までの流れを確認します。  

ユーザーの認証は、以下のURLから始まります。  

`https://api.instagram.com/oauth/authorize?client_id={app-id}&redirect_uri={redirect-uri}&scope=user_profile,user_media&response_type=code`

`{app-id}`と、`{redirect-uri}`は[INstagram Basic Display]->[Basic Display]の「InstagramアプリID」と「有効なOAuthリダイレクトURI」に置き換えます。  
InstagramアプリIDはフェイスブックアプリIDと異なることに注意してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1ed80d6c2f6a4c731c5691d9c949edb3.png)

例えば以下のようなURLになります。  
`https://api.instagram.com/oauth/authorize?client_id=684477648739411&redirect_uri=https://socialsizzle.herokuapp.com/auth/&scope=user_profile,user_media&response_type=code`

ご自身のInstagramアプリに対応したURLへアクセスすると以下の画面が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/24fc4f67c929a3cf76129a15c2a96d4a.png)

[許可する]をクリックすると、
指定したリダイレクトURIにリダイレクトされ、URLに認証コードが付加されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae5239e588bc7a39564d9444d637b96d.png)

こちらの認証コードをInstagramアプリIDやInstagram App Secretと共にInstagramのAPIにリクエストすることで、アクセストークンと交換してます。  
さらに取得したアクセストークンとユーザーIDをInstagramのAPIにリクエストすることで、Instagramのフィードを取得します。  

## Kurocoの設定(事前準備)
ここからはKurocoで設定をしていきます。  

### コンテンツ定義の作成
まずはInstagram長期アクセストークンと、Instagramフィードを保存するコンテンツ定義を作成します。  

[コンテンツ定義一覧](/ja/docs/management/content-structure-topics-group/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/22303613bafe005dc86e92cf56be990c.png)

以下の内容で設定をします。  

|項目|設定|
|:--|:--|
|名前|Instagram|
|ID=1|項目設定：テキスト<br/>項目名：アクセストークン<br/>識別子：token<br/>繰り返し回数：1|
|ID=2|項目設定：テキスト<br/>項目名：メディアURL<br/>識別子：media_url<br/>繰り返し回数：6|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8f5b5fc23f11335b8df424886e81030e.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f88fc9772a47083eea8cee5e1444edf8.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfc5a99f6572970275b8de5d2c2e5f2e.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。  

### コンテンツの作成
後で作成するカスタム処理でコンテンツを更新していくように実装するため、空のコンテンツを作成しておきます。  

[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e032238938e700a0081661d8d60c8b1b.png)

以下を入力し、[追加する]をクリックします。 

|項目|値|
|:--|:--|
|Slug:|instagram|
|タイトル|任意のタイトル|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd4de7dd81599d9c1b256b4efe88a280.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/72ca2599a82ca4044cd6a191d850967f.png)

### 定数とシークレットの作成
InstagramアプリIDと、Instagram App SecretはKurocoのカスタム処理で何度か利用する為、定数とシークレットに登録しておきます。  
特に機密性の高いものはシークレットに登録することをお勧めします。

InstagramアプリのBasic DisplayからInstagramアプリIDと、Instagram App Secretを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/90e9d62e3477d11d9b0351cbd89d7b96.png)

Kurocoの管理画面に戻り、[環境設定]->[定数]から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c1ab648086738b9cd9974c7e33b7f5fc.png)

以下を入力して、[追加する]をクリックします。

|項目|設定|
|:--|:--|
|名前|INSTAGRAM_APP_ID|
|値|InstagramアプリID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dfdf9bb1a3653f61b66025ba296c9dc6.png)

追加が完了すると、Smartyで呼び出すための変数が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/39ff4a3ded090dffa9244d8aa763220b.png)

次に、[環境設定]->[シークレット]から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e62506859a178befda4c615a002a3a2d.png)

以下を入力して、[追加する]をクリックします。

|項目|設定|
|:--|:--|
|名前|INSTAGRAM_APP_ID|
|値|Instagram App Secret|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/06a0e91c7d775ea4697e9bc7a694ee2b.png)

追加が完了すると、Smartyで呼び出すための変数が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/530c7810802be72cf51b3369785dc71d.png)

### APIの作成
#### 内部処理用のAPI作成
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

## KurocoとNuxt.jsで認証の動作を実装する
### エンドポイントの作成
エンドポイントはフロントエンドから認証コードを受け取るためのinstagram_authエンドポイントと、取得した長期アクセストークンをKurocoに保存するためのinstagram/updateエンドポイントの2つを作成します。  

#### instagram_authエンドポイント
instagram_authエンドポイントはフロントエンドからリクエストを送るため、DefaultのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21831b02823d8ec43ef328ba8c998ad7.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|instagram_auth|
|カテゴリー|API|
|モデル|Api|
|オペレーション|request_api_post|
|name|instagram_auth<br/>(後で設定するカスタム処理の識別子と一致させます。)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/09a45cbdf8dd43d51248ff14bce5cd9d.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fd6179223c2fc761831024ecae0b8898.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

#### instagram/updateエンドポイント
instagram/updateエンドポイントはカスタム処理から呼び出す内部向けのエンドポイントになるため、InternalのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|instagram/update|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|update|
|topics_group_id|先ほど作成したコンテンツ定義のID(8)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/41e930de0be762a3115bf25befa360ff.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e68fb00f1569ff02a20e398a7ba35967.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

### カスタム処理の作成
[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cf05595e31dd0f905466ec2a09bb835.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|instagram_auth|
|識別子|instagram_auth<br/>(Api::request_apiエンドポイントのnameと一致させてください。)|
|処理|以下のコード|

```smarty
{* 短期トークンの取得 *}
{append var=headers value="Content-Type': 'application/x-www-form-urlencoded"}
{assign_array var='body'            values=''}
{assign       var='body.client_id'    value=$smarty.const.INSTAGRAM_APP_ID}
{secret       var='body.client_secret' key='INSTAGRAM_APP_SECRET'}
{assign       var='body.grant_type' value='authorization_code'}
{assign       var='body.redirect_uri' value="`$smarty.const.ROOT_URL`/auth/"}
{assign       var='body.code' value=$smarty.request.code}

{api
    endpoint='https://api.instagram.com/oauth/access_token'
    method='POST'
    headers=$headers
    body=$body
    var=response1
    status_var=status1
}

{* apiプラグインのレスポンスをjson形式に変換*}
{assign var=response1 value=$response1|@json_decode}
{logger msg1="短期アクセストークンの取得" msg2=$body msg3=$response1 msg4=$status1}

{* 長期トークンの取得 *}
{assign_array var='body2'            values=''}
{secret       var='body2.client_secret' key='INSTAGRAM_APP_SECRET'}
{assign       var='body2.grant_type' value='ig_exchange_token'}
{assign       var='body2.access_token' value=$response1.access_token}

{api
    endpoint='https://graph.instagram.com/access_token'
    method='GET'
    queries=$body2
    var=response2
    status_var=status2
}

{* apiプラグインのレスポンスをjson形式に変換*}
{assign var=response2 value=$response2|@json_decode}
{logger msg1="長期アクセストークンの取得" msg2=$body2 msg3=$response2 msg4=$status2}

{* 長期トークンをコンテンツに追加 *}
{assign_array var='body3'            values=''}
{assign       var='body3.token'    value=$response2.access_token}

{if $response2.access_token != null}
    {api_internal
        var='response'
        status_var='status'
        endpoint='/rcms-api/4/instagram/update/instagram'
        method='POST'
        queries=$body3
        member_id='1'}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6255ac0db713e056ba378a3f92dcb23.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。  

### フロントエンドの実装
次にリダイレクトURIにアクセスがあった場合に、Kurocoのエンドポイントに認証コードを送信し、カスタム処理を動作させる処理をフロントエンドで実装します。  

`/pages/auth/`のディレクトリに以下の`index.vue`ファイルを作成します。  

```markup [/auth/index.vue]
<template>
  <div>
    <p>認証が完了しました</p>
  </div>
</template>

<script>
export default {
  validate({ query }) {
        return query.code != null
    },
  methods: {
    async makeAccessToen() {
      const payload = {
        code: this.$route.query.code
      }
      await this.$axios.post('/rcms-api/1/instagram_auth', payload);
    }
  },
  mounted($route) {
    this.makeAccessToen();
  }
}
</script>
```

### 動作確認

以下のURLにアクセスして、[許可する]をクリックします。  

`https://api.instagram.com/oauth/authorize?client_id={app-id}&redirect_uri={redirect-uri}&scope=user_profile,user_media&response_type=code`

`{app-id}`と、`{redirect-uri}`は[INstagram Basic Display]->[Basic Display]の「InstagramアプリID」と「有効なOAuthリダイレクトURI」に置き換えます。  

リダイレクトURIに遷移し、コンテンツにアクセストークンが保存されていることを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7dfa739958ea2c345ede6762f290becc.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c83a2d9433f4c278d9d98b855f3bd2ff.png)

## Kurocoで定期的にInstagramのフィードを取得する
Instagramの情報はKurocoのバッチ処理で定期的に取得しに行き、コンテンツを更新するように実装します。  

### バッチ処理の作成
[オペレーション] -> [バッチ処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbbe745e3943541e470fb5c0dc66969f.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/82e14b4bc626dd8d97c97d7ac082842f.png)

以下のように設定します。  

|項目|設定内容|
| :--- | :--- |
|タイトル|instagram_get_media|
|識別子|instagram_get_media|
|バッチ|毎日 00:00|
|処理|以下のコード|

```smarty
{*現在の長期アクセストークンの取得*}
{assign_array var='method_params'           values=''}
{assign       var='method_params.topics_id' value="instagram"}
{api_method
    var='response'
    model='Topics'
    method='details'
    version='1'
    method_params=$method_params}

{*最新のメディアデータ取得*}
{assign_array var='body'            values=''}
{assign       var='body.fields'    value='media_url'}
{assign       var='body.access_token' value=$response.details.token}
{assign       var='body.limit' value=6}

{api
    endpoint='https://graph.instagram.com/me/media'
    method='GET'
    queries=$body
    var='media'
    status_var=status
}

{* apiプラグインのレスポンスをjson形式に変換 *}
{assign var=media value=$media|@json_decode}

{* apiプラグインのレスポンスをアップデート用の配列に変換 *}
{assign_array var='data.media_url' values=''}
{foreach from=$media.data item=foo}
    {append var='data.media_url' value=$foo.media_url}
{/foreach}

{* コンテンツを更新 *}
{api_internal
        var='response2'
        status_var='status'
        endpoint='/rcms-api/4/instagram/update/instagram'
        method='POST'
        queries=$data
        member_id='1'}

{logger msg1="Instagramメディアの取得" msg2=$response2}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c24f78dc8a084cd87f8ad717a71ec56.png)

入力ができたら[追加する]をクリックしてバッチ処理を追加します。 

### 動作確認
最後に、[すぐに実行する]をクリックして動作の確認をします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1bd17db74cbaeb644650a3bb0b85a451.png)

正しく設定ができていれば以下のようにInstagramメディアURLがコンテンツに保存されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8cbfc90942f867254ff7e090fa1e026.png)

## Kurocoで定期的に長期アクセストークンを更新する
Instagram基本表示APIの長期アクセストークンは有効期限が60日となっています。  
Instagram側で長期アクセストークンを更新するエンドポイントが準備されているので、定期的にリクエストを送るバッチ処理を作成します。  

### バッチ処理の作成
[オペレーション] -> [バッチ処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbbe745e3943541e470fb5c0dc66969f.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/82e14b4bc626dd8d97c97d7ac082842f.png)

以下のように設定します。  

|項目|設定内容|
| :--- | :--- |
|タイトル|update_token|
|識別子|update_token|
|バッチ|毎日 01:00|
|処理|以下のコード|

```smarty
{*現在の長期アクセストークンの取得*}
{assign_array var='method_params'           values=''}
{assign       var='method_params.topics_id' value="instagram"}
{api_method
    var='topics'
    model='Topics'
    method='details'
    version='1'
    method_params=$method_params}

{* 長期トークンの更新 *}
{assign_array var='body'            values=''}
{assign       var='body.grant_type' value='ig_refresh_token'}
{assign       var='body.access_token' value=$topics.details.token}

{api
    endpoint='https://graph.instagram.com/refresh_access_token'
    method='GET'
    queries=$body
    var=response
    status_var=status
}

{* apiプラグインのレスポンスをjson形式に変換*}
{assign var=response value=$response|@json_decode}
{logger msg1="長期アクセストークンの更新" msg2=$body msg3=$response msg4=$status}

{* 長期トークンをコンテンツに追加 *}
{assign_array var='body2'            values=''}
{assign       var='body2.token'    value=$response.access_token}

{if $response.access_token != null}
    {api_internal
        var='response'
        status_var='status'
        endpoint='/rcms-api/4/instagram/update/instagram'
        method='POST'
        queries=$body2
        member_id='1'}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c96d8bfd2fac7437f9ef1b0e7b2d2257.png)

入力ができたら[追加する]をクリックしてバッチ処理を追加します。 

### 動作確認
最後に、[すぐに実行する]をクリックして動作の確認をします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c57daa60b28a655dd546adb71b449bb7.png)

正しく設定ができていればコンテンツのアクセストークンが更新されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad4872d7804ae4a4684b7d71544f273.png)

## KurocoとNuxt.jsでInstagramのフィードを表示する
ここまで準備ができたら後はKurocoのコンテンツに追加したInstagramのメディアURLをフロントに表示するだけです。  

### エンドポイントの作成
DefaultのAPIから[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21831b02823d8ec43ef328ba8c998ad7.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|instagram|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|details|
|topics_group_id|コンテンツ定義のID(8)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c3e840d05b5f4bf49a17bf4fab86f3e.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea1113a47e6e577b57d9daf272b6da56.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

### フロントエンドの実装
フロントエンドは`/pages/instagram/`のディレクトリに以下の`index.vue`ファイルを作成しました。  

```markup [/pages/instagram/index.vue]
<template>
  <div>
    <h2>Instagram</h2>
    <div class="square_contents">
      <a v-for="(n,i) in response.details.media_url" :key=i href="https://www.instagram.com/" target="_blank">
        <img :src=n>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    return {
      response: await $axios.$get('/rcms-api/1/instagram/instagram'),
    };
  },
};
</script>

<style>
.square_contents {
  display: flex;
  flex-wrap: wrap;
  width:720px;
}
.square_contents a {
  display: block;
  position: relative;
  width: 31%;
  margin: 1%;
}
.square_contents a::before {
  content: "";
  display: block;
  padding-top: 100%;
}
.square_contents img {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  object-fit: cover;
}
</style>
```

### 表示の確認
フロントエンドの表示を確認すると、Instagramのフィードが表示できていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae470166ecc592ca12dbdb67b29e7b9d.jpg)


以上で、Instagramのフィードが表示され、更新があった場合も自動でKucoroのコンテンツが更新されるようになりました。  

今回はInstagramのフィードを表示させるのみのため、Instagram基本表示APIを利用しましたが、@メンションやハッシュタグが付いたメディアの特定、他のInstagramユーザーに関するデータの取得、ストーリーズの利用等をする場合は同様の手順でInstagramグラフAPIを利用ください。

## うまく動かなかった時は？
うまく動作しない時は、以下のような点をご確認ください。  
- フロントエンドは正しくデプロイされていますか？（`/auth/?code=1234`のページは表示できますか？）  
- Kuroco管理画面の`INSTAGRAM_APP_ID`に、`InstagramアプリID`ではなく、`アプリID`を設定していませんか？<br/>  
  **正（`InstagramアプリID`）:**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/00b526d869976716b817c5a321d50316.png)  
  **誤（`アプリID`）:**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/9683b73ca808fc0dbcad18ec38cedd2d.png)  
- Kuroco管理画面の`INSTAGRAM_APP_SECRET`に、`Instagram App Secret`ではなく`App Secret`を設定していませんか？<br/>  
  **正(`Instagram App Secret`):**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/c9c4b96a0abaea904137c1b33975683c.png)  
  **誤(`App Secret`):**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f2b13ff1c06052877386c9bf5ea5acf.png)  

## 関連ドキュメント
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# HARファイルを作成する

> 元ページ: `tutorials/create-a-har-file` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/create-a-har-file/

ページ読み込み時の表示が遅いなどブラウザ由来の問題が発生した場合、問題発生時に作成したHARファイルを利用して調査できます。

HARファイルを調べることで、問題が発生した時にブラウザが生成したネットワークリクエストに関する詳細情報を確認できます。
なお、HARファイルには、個人情報データが含まれますのでご注意ください。

## HARファイルの作成方法
HARファイルの作成方法はブラウザによって異なります。今回はChromeとFirefoxの場合の作成方法を記載します。

### Chrome
1. Google Chromeを開き、問題が発生しているページにアクセスする
2. Chromeのメニューバー（要素を検証）から「表示」>「デベロッパー」>「デベロッパーツール(開発ツール)」を選択する
3. ウィンドウの左右、または下部に表示さるパネルで、「Network」タブを選択する
4. 左上端にある丸いRecordボタンを探し、ボタンが赤くなっていることを確認する<br/>※ ボタンが灰色になっている場合は、1回クリックすると赤くなります。
5. チェックボックス「Preserve log」にチェックを入れる
6. Clearボタン（斜線が入った丸）をクリックして、既存のログをすべて消去する
7. 発生した問題を再現する
8. 問題が再現できたら、画面下部の一覧を右クリックして「Save as HAR with Content」を選択し、ファイルを保存する

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8bf989639b27d3cd6faf0b6a2be71d21.gif)
### Firefox
1. Firefoxで、問題が発生しているページを表示する
2. ウィンドウ右上にあるFirefoxメニュー（3本の平行線）を選択し、「ウェブ開発」 -> 「ネットワーク」を選択する -> ウィンドウの横、または下に開発ツールが開きます。
3. 「ネットワーク」タブをクリックして、問題の動作を再現する -> 記録は自動的に開始するので、ブラウザで実行してください。
4. すべてのアクションが開発者ネットワークパネルで生成されたことを確認したら、ネットワークパネル「ファイル」列の下の任意の場所を右クリックして、「すべてをHARファイルとして保存」をクリックする

## HARファイル作成時の注意点
- 項目名やボタンの位置はブラウザ側の仕様変更で本内容と異なる場合があります。　
- その他のブラウザでの生成方法は、「ブラウザ名　HARファイル　作り方」などのワードで検索エンジンにてご確認ください。
- Kurocoサポートへのお問い合わせの際は、HARファイルを添付してお送りください。

## HARファイルの確認方法

### Google Chromeのデベロッパーツールから確認する 
HARファイルはGoogle Chromeの「デベロッパーツール(開発ツール)」で確認ができます。
1. Chromeのメニューバー（要素を検証）から「表示」>「デベロッパー」>「デベロッパーツール(開発ツール)」を選択する
2. ウィンドウの左右、または下部に表示さるパネルで、「Network」タブを選択する
3. 「↑」アイコンをクリックしてHARファイルをアップロードする
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c92134d58befec0b2b42b809e1d7d4f4.png)
参考) [Chrome Developers HAR import and export buttons](https://developer.chrome.com/blog/new-in-devtools-76/#HAR)

## 関連ドキュメント
- [お問い合わせのしおり](/ja/docs/troubleshooting/contact-guidelines/)
- [よくあるお問い合わせ](/ja/docs/troubleshooting/before-sending-your-inquiry/)
- [PCのブラウザでJSエラーを確認する方法を教えてください。](/ja/docs/faq/how-to-check-for-js-errors-in-a-pc-browser/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)


---

# Firebaseと連携して、Storageにファイルを保存する

> 元ページ: `tutorials/firebase` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/firebase/
> 概要: Firebaseとの連携方法を解説します。Firebaseと連携することで、Kurocoからアップロードした画像や動画ファイルを、FirebaseのStorageに格納し利用が可能です。

Firebaseとの連携方法を解説します。  
Firebaseと連携することで、Kurocoからアップロードした画像や動画ファイルを、FirebaseのStorageに格納し利用が可能です。

## Firebaseのプロジェクト作成
[Firebase公式サイト](https://firebase.google.com/)より、Firebaseのプロジェクトを作成します。  
Cloud Storage for Firebaseを利用するには、請求先アカウントの設定およびBlazeプラン（従量課金制）への変更が必要です。本チュートリアルではBlazeプランを利用します。

:::info
[Firebase料金プラン](https://firebase.google.com/pricing)
:::

### 1. Firebase(Google Cloud Platform)の利用を申し込む
[Firebase公式サイト](https://firebase.google.com/)にアクセスし、[使ってみる]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e807acad195169fff4436e7f3a92632f.png)

### 2. プロジェクトを作成する  
「firebaseへようこそ」の画面で[プロジェクト作成]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/70b5829719f81fadba812b594b19aed8.png)

### 3. プロジェクト名をセットして、続行をクリックする
プロジェクト名を入力し、「自身の取引、ビジネス、仕事、または職業のみを目的としてFirebaseを利用することを正式に認めます。」へチェックを入れて、[続行]をクリックします。  
プロジェクト名はあとから変更ができませんのでご注意ください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb115a42526740463dd268eb32c12c6b.png)

### 4. Googleアナリティクスの設定をする  
Googleアナリティクスの有効/無効を設定します。  
有効にした場合、次の画面でGoogleアナリティクスのアカウント設定画面に遷移します。今回は[無効]に変更します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5e62d93c133a13f5e67e2d1df156b87b.png)

### 5. プロジェクトの作成が完了したら、続行をクリックする
プロジェクトの作成完了画面で[続行]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bde55442584c88164cf3ec4f55887082.png)

以上でFirebaseプロジェクトが完成します。

### 6. Blazeプランにアップグレードする
Cloud Storage for Firebaseを利用するには、Blazeプラン（従量課金制）へのアップグレードが必要です。  
Firebaseコンソール左下の[アップグレード]をクリックし、画面の指示に従って請求先アカウントの設定とBlazeプランへの変更を行います。

:::caution
2026年2月3日以降、SparkプランではCloud Storageが利用できなくなりました。Blazeプランでも無料枠の範囲内であれば料金は発生しません。  
詳細: [Cloud Storage for Firebaseの変更に関するFAQ](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)
:::

:::tip
Blazeプランへのアップグレード時に予算アラートを設定することを推奨します。
:::

## Firebaseの設定・Credentialsの取得

ここからはFirebaseの管理画面にて作業します。

### 7. [プロジェクトの設定]にアクセスする
Firebaseのダッシュボードの歯車マークから、「プロジェクトを設定」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c1c11f5b83a3cb83de90a6ddeaece0f8.jpg)

### 8. 秘密鍵のダウンロードをする
[サービスアカウント]のタブを開き、[新しい秘密鍵の生成]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1345caeac70910faf0b1f5c6fee0a772.png)
  
表示されたポップアップの中の[キーを生成]をクリックします。  
すると、ファイルがダウンロードされます。

:::note
ダウンロードしたファイルは後ほど使用しますので保存しておいて下さい。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/003bc04a79c820aa19063a9e208608b7.png)

### 9. Firebaseのストレージの利用開始設定をする

サイドメニューの[構築] -> [storage]をクリックし、Storageの画面で[始める]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/66f04986cde9381e8b194d9b211727c6.png)

[次へ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c53cba3f9b2bf46c59f96599fb37c732.png)

Cloud Storage のロケーションは「asia-northeast1」または「asia-northeast2」を選択し、[完了]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/05782cded7ebb2e84b79dee77f67c3ac.png)

### 10. Firebaseのアプリ追加設定をする
サイドメニューの[プロジェクトの概要]からプロジェクトホーム画面に戻り、WEBタイプアプリ[< / >]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73a2dc2fd699aa5dfd04852c2c491328.png)

アプリのニックネームを入力し、[アプリを登録]をクリックします。      

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b17490d3dfcba0378657d4fea2fb4c6a.png)

「Firebase SDKの追加」画面が表示されるので、[コンソールに進む]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ec764ca41ea38964b4e2897baa27ec9b.png)  


### 11. FirebaseConfigを取得する
「プロジェクト概要」の横の歯車マークをクリックし、[プロジェクト設定]の画面にアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c1c11f5b83a3cb83de90a6ddeaece0f8.jpg)

画面下部の「マイアプリ」->「SDKの設定と構成」の[Config]を選択します。  
すると、firebaseConfigが表示されます。後ほど使用するので、コピーします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a122c76ca6a6d43a3888574c12006627.png)

## Kurocoでの設定

ここからはKurocoの管理画面にて作業します。

### 12. Firebase設定画面に上記の8と11で取得したCredentialsをセットする  
Kuroco管理画面のサイドメニューの[外部システム連携] -> [firebase]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/86d14b73e133a8a6b2ceb141ec505be1.png)

Credentialsの欄に「8. 秘密鍵のダウンロードをする。」で取得したファイルをセットします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e6766204136632e7b31945966e5b536.png)

また、App Configの欄に「11. FirebaseConfigを取得する」で取得したFirebaseConfigを貼り付けます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdf4816301c6c7493f94d44843828b9e.png)

[接続する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1a3c3cdc1210b264aed0f1cc0f27cb4c.png)

### 13. StorageをEnableにする  
「Storage」の[Enable]にチェックを入れ、[更新する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c496d85c162da862d4698dab1c3cf70.png)

以上でFirebaseとの連携が完了です。  

## 利用方法
### ファイル
接続完了後、[ファイルマネージャー]をクリックすると、GCSの表示が確認でき、ファイルをアップロードできます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5308fa4547eef87dd25ebe7982f1b0db.png)

### コンテンツ定義
#### ファイル(GCSにアップロード)
Kuroco管理画面の[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)より、設定項目で[ファイル(GCSにアップロード)]を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2f3c1fc8e4dfe681542b90731503f19.png)

コンテンツ編集画面にファイルアップロードフィールドが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed4c0df948b6f34fcd039a496fa32b51.png)

こちらからファイルをアップロードすると、FirebaseのStorageにファイルがアップロードされるようになります。

#### WYSIWYG
WYSIWYG項目の全般設定で「リソースを指定」にGCSのパスを入力すると、WYSIWYGからアップロードしたファイルが指定したGCSのフォルダに保存されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a1b98b35034215b4bc9471dddb7c14c1.png)

## 関連ドキュメント
- [Firebase](/ja/docs/management/firebase/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [Vimeoと連携して動画をアップロードする](/ja/docs/tutorials/how-to-connect-to-vimeo/)
- [バッチ処理を利用し、PDFの1ページ目をサムネイル画像にする](/ja/docs/tutorials/how-to-make-thumb-from-pdf/)
- [GCS, S3に設定したファイルの有効期限について](/ja/docs/reference/expiration-for-files-in-gcs-and-s3/)


---

# GitHubActionsでgenerateに失敗した場合に、ビルドを中止しSlackに結果を通知する方法

> 元ページ: `tutorials/handling-a-generate-error-in-github-actions` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/handling-a-generate-error-in-github-actions/

KurocoFrontにてサイト運用をしている際に、generateエラーが発生するとページの一部が生成されず404エラーとなる場合があります。  
サイト運用時に404エラーとなることは避けたいので、generateエラー発生時にビルドを中止する方法を説明します。

併せて、ビルドが中止された際にSlackへ通知する設定も紹介します。

## 前提
本チュートリアルは、下記条件にてサイト運用をしていることを前提とします。

- Nuxt.jsを利用
- KurocoFrontを利用

## nuxt generateのエラー発生時にビルドを中止する方法
まずは、nuxt generate時にエラーが発生した際にビルドを中止する方法を説明します。

### package.jsonの修正

package.jsonに記載されている`nuxt generate`コマンドに、`–fail-on-error` オプションを追加します。

```json [package.json]
{
  ...,
  "scripts": {
    ...
    "build": "cross-env NODE_ENV=development nuxt build",
    "generate": "cross-env NODE_ENV=development nuxt generate –fail-on-error",
    "build-prod": "cross-env NODE_ENV=production nuxt build",
    "generate-prod": "cross-env NODE_ENV=production nuxt generate –fail-on-error",
    ...
  },
  ...
}
```

:::info
`–fail-on-error` オプション はNuxt v2.14.4以降のバージョンで利用可能です。詳細は [NuxtJS公式ドキュメント](https://nuxtjs.org/ja/docs/get-started/commands/#%E3%82%A8%E3%83%A9%E3%83%BC%E6%99%82%E3%81%AE%E5%A4%B1%E6%95%97%EF%BC%88fail-on-error%EF%BC%89)をご確認ください。
:::

こちらの対応で、nuxt generate時にエラーが発生するとビルドが中止されます。

## ビルド失敗時にSlackに通知する
上記対応で、generateでエラーが発生したらビルドを中止させることができました。  
しかしながら、現状だとビルドの中止を確認するためにはGitHub Actionsを確認しに行く必要があります。

毎回GitHub Actionsを確認する手間を省くため、ビルド失敗時にSlackへ通知する方法を紹介します。

### Slackのchannelにincoming webhookの追加

`https://[ワークスペースID].slack.com/apps`にアクセスします。

:::caution
[ワークスペースID]にはご自身のSlackのワークスペースIDを記入してください。
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0fb70946a9b79e600fc1501de1d47617.png)
「Incoming webhook」を検索します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1f81091be5eed7d519f274a45a4fc123.png)
Slackに追加をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/13b43e20605ca3736a6f94e89a312908.png)
アプリを追加したいチャンネルを選択します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f062cfe356070465dc23224310cbeac7.png)
「Incomming Webhookインテグレーションの追加」ボタンをクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7c007e35ba2a25fb908c1b7f57105403.png)
すると、Incoming webhookが追加されました。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c5405407a4d041b1fceff054b5e57e1e.png)
Webhook URLをコピーします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2099ad9b3fb36c0333829130387d1489.png)
以上でSlackの設定は終了です。

### Webhook URLをGitHubのActions secretsに追加する
次にGitHubを設定します。以下の設定にはAdminの権限が必要になります。  
GitHubの対象のリポジトリから、[Settings] -> [Secrets] をクリックしActions secrets画面を表示します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8fdbef7e1553cb0c6d58518990e26cb5.png)
Actions secrets画面より、「New repository secret」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/83548bfa32e7013fee8cb4749095f748.png)
下記を記入し、「Add secret」をクリックします。

| 項目 | 値 |
| :--- | :--- | 
| Name | SLACK_WEBHOOK_URL |
| Value | コピーしたWebhook URL |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/22b7973a2c06a4b1b94b8110ca4f34a3.png)
すると、Repository secretsが追加されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fd59cc6b346fe879b47d1f2035671b9d.png)
以上でGitHubの設定は完了です。

### .github/workflowsのYAMLファイル修正
最後に、`.github/workflows`配下に配置したYAMLファイルへSlack通知の設定を追記します。  
YAMLファイルの`pullreq_build`と`pushed_build`のstepに下記のように設定を記入します。

```yml 
      - name: Slack Notification on Failure
        uses: rtCamp/action-slack-notify@master
        if: failure()
        env:
          SLACK_CHANNEL: kuroco_channel
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}
          SLACK_TITLE: build error
          SLACK_MESSAGE: 'https://example.g.kuroco.app/'
          SLACK_COLOR: danger
```

なお、下記項目は、ご自身の環境により修正してください。

| 項目 | 値 |
| :--- | :--- | 
| SLACK_CHANNEL | 通知先チャンネル名を記入 |
| SLACK_MESSAGE | 通知時に表示するメッセージを記入。 |

:::tip
Slackの通知に[rtCamp/action-slack-notify](https://github.com/rtCamp/action-slack-notify)を利用しています。
:::

それでは、YAMLファイルの`pullreq_build`と`pushed_build`のstepにそれぞれ追記します。

#### pullreq_buildへの追記

`pullreq_build`のstepsに追記します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/901a095c3a4a8a06e783526ca3f27e30.png)
#### pushed_buildへの追記

`pushed_build`のstepsに追記します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/120be53bdf79c62c79981e6612ab6653.png)
以上で設定完了です。  

設定後、generateエラーが発生した際に下記のようにSlackに通知されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/381ab88698119c2583c27c40c4e175c7.png)

## 関連ドキュメント
- [GitHubActionsのビルド結果をslack-sendで通知する](/ja/docs/tutorials/handling-a-slack-send-in-github-actions/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [コンテンツの更新時にGitHub Actionsを自動実行する](/ja/docs/tutorials/auto-run-github-with-contents-update/)
- [GitHubリポジトリにpushした際にエラーが表示されます。エラー解決方法を教えてください。](/ja/docs/faq/i-get-an-error-message-when-i-push-to-the-github-repository/)


---

# LINEユーザーにメッセージを送付する

> 元ページ: `tutorials/how-to-connect-to-line` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-connect-to-line/
> 概要: このページでは、KurocoとLINEのMessaging APIを連携し、KurocoからLINEユーザーにメッセーを送信する方法を説明します。

このページでは、KurocoとLINEのMessaging APIを連携し、KurocoからLINEユーザーにメッセーを送信する方法を説明します。  

## 概要
Kuroco には LINEユーザーに対してメッセージを送信する機能が備わっています。
具体的には、LINE Messaging APIを用いて、KurocoからLINEへメッセージを送信するような命令を送る事で、ユーザーにメッセージが送信されます。
メッセージの送信はカスタム処理に該当する記述を行う必要があります。

LINE公式アカウントへの友だち追加時に、LINEユーザーIDでKurocoへのユーザー登録(ログインする権限はなし)を行い、トリガー機能を使ってKuroco内のさまざまなイベントをトリガーとし、任意のタイミングで任意のユーザーにLINEメッセージを送信出来ます。

### 学べること
以下の手順で、KurocoからLINEユーザーにメッセージを送信します。

- [概要](#概要)
  - [学べること](#学べること)
  - [前提条件](#前提条件)
- [LINE Developersコンソールでチャネルを作成する](#line-developersコンソールでチャネルを作成する)
- [LINEの接続設定をする](#lineの接続設定をする)
- [Kurocoの管理画面からLINEとの連携をする](#kurocoの管理画面からlineとの連携をする)
- [LINE公式アカウントの友だち追加時のWebhookからLINEユーザーIDを取得する](#line公式アカウントの友だち追加時のwebhookからlineユーザーidを取得する)
  - [グループを準備する](#グループを準備する)
  - [Webhookを受けるエンドポイントを作成する](#webhookを受けるエンドポイントを作成する)
  - [ユーザー登録を行うカスタム処理を作成する](#ユーザー登録を行うカスタム処理を作成する)
  - [LINEのチャネル設定でWebhook URLを設定する](#lineのチャネル設定でwebhook-urlを設定する)
  - [LINE公式アカウントを友だち追加して動作の確認をする](#line公式アカウントを友だち追加して動作の確認をする)
- [Kuroco のカスタム処理を使ってユーザーにメッセージを送信する](#kuroco-のカスタム処理を使ってユーザーにメッセージを送信する)


### 前提条件
LINE公式アカウントへの友だち追加時に送信されるWebhookを利用して、LINEユーザーIDを取得します。  

:::tip
LINEアカウントを使ってKurocoにメンバー登録する方法として、OAuth連携機能を利用することも可能です。  
詳しくは[LINE公式アカウントの友だち追加時のWebhookからLINEユーザーIDを取得する](#line公式アカウントの友だち追加時のwebhookからlineユーザーidを取得する)のヒントをご確認ください。
:::

## LINE Developersコンソールでチャネルを作成する

まず、LINE Developersコンソールにてチャネルを作成する必要があります。LINEアカウントを持っていない場合はLINEアカウントを作成してください。

[LINE Developersコンソール](https://developers.line.biz/console/) にログインしてください（初回ログイン時のみ、開発者として登録するか否かを尋ねられるので、開発者として登録してください）。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c2e109a56aa8cb881adcd0e5e28623e1.png)

次に新規プロバイダーを作成します。「作成」ボタンをクリックしてください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/eacf32b52ded57fc7a1ebd02c122317d.jpg)

プロバイダー名を指定します。ここでは「KurocoSampleProvider」とします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d601dea82a0716748ee88573482dc670.png)

つづいて、チャネルを作成します。「新規チャネル作成」をクリックしてください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/12230fb49e360e11c7ff30933e342ffc.png)

チャネルの種類は「Messaging API」を選択してください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1dcb7a1d1371416968eb40e24be08ab.png)

新規チャネル作成画面に遷移します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/87c346ac1bf5f74e2aa4ab5cee2c2361.png)

以下のように各項目を入力し「作成」ボタンをクリックしてください。

項目名 | 入力値
:-- | :--
チャネルの種類 | Messaging API
プロバイダー | 前述の手順で作成したプロバイダーを指定してください。
会社・事業者の所在国・地域 | 法人の場合は会社の所在国・地域を、個人の場合は店舗や居住地の所在国・地域を選択してください。
チャネルアイコン | チャネルのアイコンとなる画像をアップロードしてください。
チャネル名 | チャネル名を指定してください。
チャネル説明 | チャネルの説明を入力してください。
大業種 | 大業種を選択してください。
小業種 | 小業種を選択してください。
メールアドレス | このチャンネルの管理者となる方のメールアドレスを入力してください。
LINE公式アカウント利用規約 | 内容を確認の上、チェックを入れてください。
LINE公式アカウントAPI利用規約 | 内容を確認の上、チェックを入れてください

確認のダイアログが表示されますので、問題なければ「OK」をクリックしてください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/491b09c974859024efc03a78e1445027.png)

作成すると、以下のようにチャネルが表示されます。クリックして詳細情報を確認してください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdfd6dbdafcb3460f63e9f53e36c0d89.png)

以上で、チャネルが作成できました。  
チャネルIDは後述で使用しますので控えておいてください。

## LINEの接続設定をする

次にKurocoとLINEの接続設定を行います。

まず、公開鍵・秘密鍵のペアを準備し、先ほど作成したチャネルの設定画面にて公開鍵を登録する必要があります。

公開鍵・秘密鍵のペアを作成する方法はいくつかありますが、お使いのウェブブラウザが[Web Crypto API](https://developer.mozilla.org/ja/docs/Web/API/Web_Crypto_API) に対応している（たとえばGoogle Chromeブラウザなどの）場合、[SubtleCrypto.generateKey()](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/generateKey) メソッドを使って秘密鍵と公開鍵を生成できます。
ここではGoogle Chromeを例に公開鍵・秘密鍵の作成方法を説明します。

Google Chromeを起動し、ブラウザのデベロッパーツールを開きます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5697287cf9708a12ec94785a53a1e48e.png)

JavaScriptコンソールに以下のコードを入力して実行(エンターキーを押下)します。
```js
(async () => {
  const pair = await crypto.subtle.generateKey(
    {
      name: "RSASSA-PKCS1-v1_5",
      modulusLength: 2048,
      publicExponent: new Uint8Array([1, 0, 1]),
      hash: "SHA-256",
    },
    true,
    ["sign", "verify"]
  );

  console.log("=== private key ===");
  console.log(
    JSON.stringify(
      await crypto.subtle.exportKey("jwk", pair.privateKey),
      null,
      "  "
    )
  );

  console.log("=== public key ===");
  console.log(
    JSON.stringify(
      await crypto.subtle.exportKey("jwk", pair.publicKey),
      null,
      "  "
    )
  );
})();
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b69f7fedf9b26c0a52978e79b58ad68c.png)
成功すると以下のような秘密鍵と公開鍵が生成されます。

**秘密鍵の例**

```json
{
  "alg": "RS256",
  "d": "B6A6he..........",
  "dp": "ogd_VFa..........",
  "dq": "qt9TJZV..........",
  "e": "AQAB",
  "ext": true,
  "key_ops": [
    "sign"
  ],
  "kty": "RSA",
  "n": "wQoAaMQmz..........",
  "p": "92ODEIUZY..........",
  "q": "x8ItprfI7..........",
  "qi": "kfmYirMr.........."
}
```

**公開鍵の例**

```json
{
  "alg": "RS256",
  "e": "AQ..........",
  "ext": true,
  "key_ops": [
    "verify"
  ],
  "kty": "RSA",
  "n": "wQoAaMQm.........."
}
```

先ほど作成したチャネルの設定画面にてアサーション署名キーの横にある［公開鍵を登録する］ボタンをクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7e835fd433d8e21e609ef31fb4222cdd.png)

作成した公開鍵を入力します。［登録］ボタンをクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2231bdf4ecd91adbdb76e5474a4d17c9.png)

公開鍵の登録に成功すると、kidが表示されるのでコピーして控えてください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/56d4b1a5f0af4c8f5c94442ef399cdb3.png)

## Kurocoの管理画面からLINEとの連携をする

次にKuroco管理画面へ移動し、[チャネル] -> [メッセージング] -> [LINE]に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdafbf54c83d9b00c93fdb3051059d4e.png)

[LINE]欄の「有効にする」にチェックを入れ、上述で控えたチャンネルID、秘密鍵、アサーション署名キー（kid）を入力して[更新する]をクリックください。

以上でKuroco側の設定は終わりです。

## LINE公式アカウントの友だち追加時のWebhookからLINEユーザーIDを取得する

次に、LINEユーザーが公式アカウントを友だち追加した時に、そのユーザーがKurocoのメンバーとして自動登録されるように設定します。

:::tip
LINEアカウントを使ってKurocoにメンバー登録する方法として、OAuth連携機能を利用することも可能です。  
- OAuth連携でLINEログインをして、LINEユーザーIDを保存するは、[外部アカウントを使用したOAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)を参照してください。
- LINEログインのチャネルと、Messaging APIのチャネルは同じプロパイダー内に設定してください。
- LINEログインの[チャネル基本設定]->[リンクされたボット]でMessaging APIのチャネルをリンクしてください。
:::

### グループを準備する

「LINEユーザー」というグループを作成します。作成したグループのIDを控えます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/20414fdbbd8ae917d65110348366db01.png)


### Webhookを受けるエンドポイントを作成する

Kuroco側に、LINEのイベントを受けるためのWebhook用エンドポイントを作成します。
セキュリティを`Cookie`としているAPIに以下の設定でエンドポイントを作成します。

項目名 | 入力値
:-- | :--
パス|`line/webhook`
モデル | Api / Api/v1 / request_api_post
サマリ | LINE Webhook用エンドポイント
APIリクエスト制限 | None
name | line_webhook

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9dc74895d2b5237433c98b051b1a6da0.png)

また、メンバー登録用にもう一つエンドポイント作成します。
セキュリティを`動的トークン`としているAPIに以下の設定でエンドポイントを作成します。

項目名 | 入力値
:-- | :--
パス|`member/line/register`
モデル | メンバー / Member/v1 / insert
サマリ | LINEメンバー登録
APIリクエスト制限 | Group Auth / 管理者
default_group_id | 上記で作成したグループのID
not_login_after_insert | チェックなし
login_ok_flg | チェックなし
use_columns | `name1`, `email`, `login_ok_flg`

![Image from Gyazo](https://t.gyazo.com/teams/diverta/02343e446e18e4a1900619da33bf5290.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eed0c7363791df46f1d88816c82c2331.png)


### ユーザー登録を行うカスタム処理を作成する

以下の内容でカスタム処理を作成します。

- タイトル: LINE Webhook
- カテゴリ：未分類
- 識別子: line_webhook
- 処理：（以下参照）

```smarty reference title="line_webhook"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/request_api_post/line_webhook.txt
```

### LINEのチャネル設定でWebhook URLを設定する
LINEデベロッパーコンソールにて、Messaging APIチャンネル設定画面の[Messaging API]タブを開きます。  
[Webhook URL]に上記で作成したエンドポイントを登録します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/934709ad63ab8898abf92a2fbb6e9d9d.png)


### LINE公式アカウントを友だち追加して動作の確認をする

Messaging APIチャンネル設定画面に掲載されている[QRコード]をお手持ちの端末で撮影し、LINE公式アカウントを友だち追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2081d26dfbfa429810af4aeac8585595.png)

公式チャンネル名が表示されるので、確認して[友だち追加]をタップします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb6abb67c1afacd41deebd35037458d9.png)

Kuroco管理画面のメンバー一覧画面にメンバーが追加されていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88d1cc1f3eee6a3ba1e3026c7835be09.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b0cdba7885c734810583c471f41f40c.png)

## Kuroco のカスタム処理を使ってユーザーにメッセージを送信する

テストのため、カスタム処理を作成し以下のように記載してください。

- タイトル: LINE test
- カテゴリ：未分類
- 識別子: line_test
- 処理：（以下参照）
  
```smarty
{sendmail
    var=result
    subject='LINE message test' 
    contents="こんにちは[emoji:5ac21a8c040ab15980c9b43f:001][emoji:5ac21a8c040ab15980c9b43f:002][emoji:5ac21a8c040ab15980c9b43f:003] " 
    to="Uxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@text.line.r-cms.jp" 
}
```

`to` には `(LINEユーザーID)@text.line.r-cms.jp` の形式で入力してください。

`contents` には上記のように絵文字を含めることが可能です。絵文字を挿入したい箇所に以下のように記載してください。  
```
[emoji:(プロダクトID):(絵文字ID)]
```
利用可能な絵文字については[LINE絵文字定義](https://developers.line.biz/ja/docs/messaging-api/emoji-list/#line-emoji-definitions)をご参照ください。

**送信結果**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ecbea49d63df38adc9e6b1e3b7f3c33.png)

## 関連ドキュメント
- [LINE](/ja/docs/management/line/)
- [カスタム処理](/ja/docs/management/function/)
- [LINEアカウントを使用してユーザー登録を行うと同時に公式アカウントの友達登録を行う](/ja/docs/tutorials/implementing-oauth-sp-for-line/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# Twilioと連携してSMSを送信する

> 元ページ: `tutorials/how-to-connect-to-twillio` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-connect-to-twillio/
> 概要: このページでは、KurocoとTwilioを連携し、KurocoからSMSを送信する方法を説明します。KurocoからのSMS送信は"090","080","070","060"から始まる日本国内の電話番号に対応しています。

このページでは、KurocoとTwilioを連携し、KurocoからSMSを送信する方法を説明します。  
KurocoからのSMS送信は"090","080","070","060"から始まる日本国内の電話番号に対応しています。  

## Twilioと連携する
### 1. Twilioのアカウントを登録する 
Twilio のアカウントを登録してください。  
Twilio のサイトにアクセスします。

https://www.twilio.com/ja/

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b6cbd91c47c4a731ae763ad35b32275.jpg)

右上の「無料サインアップ」をクリックしてください。

必要項目を入力し、[I accept the Twilio Terms of Servece...] にチェックを入れて[無料トライアルを始めましょう] という赤いボタンをクリックしてください。途中ロボットではないことを証明するためのダイアログが表示されます。指示された内容を入力して先に進んでください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ccc11274266fd1fb2cf99db13f216944.jpg)

以下のような画面が表示され、確認用のメールが送信されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc9863b2bb0b043b04ae885ee323a09f.png)

メーラを確認してTwilioから送信されたメールを開き、メール本文内にある[Verify Your Email] と書かれている赤いボタンをクリックしてください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/560178df3573542706389b6f02117114.jpg)

これでユーザー登録が完了しました。

### 2. 二要素認証を設定する 

続いて、二要素認証を設定します。以下のURLからTwilioのコンソール画面にログインしてください。  
https://www.twilio.com/login  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/19661a5552587b379758e034ec9fc246.png)

二要素認証の設定をするため、携帯端末の電話番号を入力してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e632843bc2191c1aa3e0773ce60d6aa7.png)

携帯端末に送信されたSMSを確認し、確認コードを入力してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/208a5c655def7f24654bf30d93de2f6e.png)

以下のように復旧コードが表示されますので控えてください。携帯端末を紛失した際などに利用します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ee783714f98b8a06f344da980a41c76.png)

本人認証のためもう一度電話番号を入力します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f8057beadfc2ed40f88f612b368c0106.png)

以上で二要素認証の設定は終わりです。  
ここでTwilioからのアンケートがあります。Twilio製品を使ってあなたが構築しようとしているサービスなどについて回答してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b4b9b648bb56b819259f4fce24afa24.png)

### 3. 送信元となる電話番号を取得する  
Twilio製品を使い始めるまでの手順が表示されています。[Get a Twilio phone number]という青いボタンをクリックするとUSAまたはカナダの電話番号が1つ取得されます。この番号はTwilioを使ってSMSを送信する際の送信元電話番号として使用されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/784b92cddc4b46343f95f9783513b219.jpg)

### 4. 支払い手続きする
次にヘッダー部分の「Upgrade」をクリックして、支払い手続きを行なってください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8961a3822bbcb7f046ae5bd3d3ae42e4.png)

### 5. システム連携情報を取得する
ヘッダー部分の「My first Twilio account」と書かれている部分をクリックするとコンソールトップページに遷移します。ここでAccount Infoと書かれている部分から以下の値をコピーして控えて下さい。

- Account SID
- Auth Token
- My Twilio Phone number

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdf41fbef7aaf6fd97b2bfad2b40c52f.png)

### 6. Kurocoの管理画面に設定する 
次にKuroco管理画面へ移動し、[チャネル] -> [メッセージング] -> [テキスト メッセージ(SMS)]に遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a045602f9263d0d3684fbe5138e7a6fd.png)

[テキスト メッセージ(SMS)]欄のチェックボックスにチェックを入れ、先ほど控えたAccount SID、Auth Token、My Twilio Phone numberを入力して[更新する]をクリックください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d72f80200fe2a30ed372168c5043b0dd.png)

以上で設定は完了しました。

## 連携したSMSの利用方法

KurocoからSMSを送信するには、カスタム処理にSMS送信プログラムを記述する必要があります。本来はバッチ処理や特定の[Post-process](https://kuroco.app/ja/docs/reference/pre-processing/)など何らかのタイミングをトリガーとし、カスタム処理を呼び出して利用します。  
ここではテスト用のカスタム処理を実装して手動で実行してみることにします。

### 1. カスタム処理を追加する

管理画面サイドバーから「カスタム処理」をクリックし、カスタム処理一覧画面の[+追加]ボタンをクリックしてください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/753a5cf197018ae987d86180bb1105ac.png)

ここでは以下のように設定して[+追加する]ボタンをクリックしてください。

|項目  |値  |
| :--- | :--- |
|タイトル|任意の名称を入力する。(本チュートリアルでは`SMS送信テスト`)|
|カテゴリ|カスタム処理の種類を選択する(本チュートリアルでは`未分類`)|
|識別子|本カスタム処理を他からコールする時に利用する識別子を入力する。(本チュートリアルでは`sms_test`)|


![Image from Gyazo](https://t.gyazo.com/teams/diverta/a015ad4587ed0b591ae7fc1e5c557cdb.png)

以下のようにカスタム処理を実装して「テストする」ボタンをクリックしてください。(携帯電話番号)と書かれている部分は090xxxxxxxxなど、送信先の電話番号をハイフンなしで記載してください。

:::caution
KurocoからのSMS送信は"090","080","070","060"から始まる日本国内の電話番号に制限されています。  
:::

```php
{sendmail 
    var=result 
    to="(携帯電話番号)@twilio.r-cms.jp" 
    subject="Test" 
    contents="Kurocoから送信しています。"}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f57a0ab6b52fe953b2c6c90783896003.png)

:::caution
トライアル期間中のTwilioからは任意の電話番号にSMSを送信できません。トライアル期間中にSMSの送信テストをする場合は「Verified Caller IDs」に送信先電話番号を登録する必要があります。
:::

端末に以下のようにメッセージが届けばテスト成功です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9857e6ee5d51d6c9fdc4a8e5d99f0e4.png)

以上でKurocoとTwilioを連携しSMSを送信できるようになります。

## 関連ドキュメント
- [テキスト メッセージ(SMS)](/ja/docs/management/twilio/)
- [カスタム処理](/ja/docs/management/function/)
- [ログイン画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-login-form/)
- [会員登録画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-registration-form/)


---

# Vimeoと連携して動画をアップロードする

> 元ページ: `tutorials/how-to-connect-to-vimeo` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-connect-to-vimeo/

このページでは、KurocoとVimeoを連携し、Kurocoから動画のアップロード・表示をする方法を説明します。

## FirebaseまたはAmazon S3と連携する
Vimeoと連携して動画をアップロードするために、FirebaseまたはAmazon S3と連携がされている必要があります。  
まずは[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)、または[Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)のチュートリアルを参考に、いずれかと連携してください。

## Vimeoと連携する
**1. Vimeoのアカウントを登録する**  
Vimeoのアカウントを登録してください。  
参考) Vimeoのプランについて  
機能的にはPlusでも対応可能ですが、頻繁に利用する場合はBussinessがおすすめです。  
[https://vimeo.com/](<https://vimeo.com/>)  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9adcf326009b7831b351e68745525926.png)
**2. 新規アプリ登録の画面へ進む**  
ログインした状態のまま、[Vimeo developer](https://developer.vimeo.com/) から[新規アプリ]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5fd6266289e7e6f2e79247a3fad9e992.png)
**3. appを追加する**  
下記内容を入力し、[Create app] をクリックしてappを追加します。
- App name: お好きな名前
- App description:簡単でよいので動画利用する内容の英語の説明
- Will people besides you be able to access your app?:No

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/00f63d9590c1a7a71dfaaaa23a014328.png)
**4. appの設定画面からUpload Accessの申請画面に進む**  
[Request Upload Access]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1cc6fa6a5755d0b4f097d28d0d02a2b0.png)
**5. Request Upload Accessの申請する**  
下記内容を入力します。
- Will you be charging for sample?: 動画を見るのに課金をしなければNoを選択
- Where will these videos be uploaded?: My account
- Who created these videos?: Other people created these videos
- What kind of videos will be uploaded?: 簡単でよいのでどのような動画がアップロードされるかの説明を英語で入力します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d55161531b041665efab32f3bc27a9d1.png)
全て記載したら [Request upload access] をクリックして申請完了です。

:::tip
アプリの認証には2、3日ほどかかります。承認されない場合は[Vimeoのサポート](https://vimeo.com/help/contact)にお問い合わせください。
:::

**6. Access Tokensを作成する**   
[Vimeo developperのMy Apps](https://developer.vimeo.com/apps)を確認すると、先ほど作成したアプリが表示されるので、クリックして作成したアプリの設定画面へ遷移します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f44c1a583d2a802d95b657d824208559.png)
下記のように、Authenticatedを選択後、Scopesを選択して、[Generate]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9d4d4a4fc49c800e2afc5cc6dfc05a4d.png)
Access Tokenが作成されます。  
下記情報をメモしておいて下さい。
- Access token
- Client identifier
- Client secrets

:::caution
Access Tokenは画面を閉じると再表示できませんので、メモをしておいてください。  
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bde62e7ce65b5ea44cdd4c98dbe49700.png)
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b44dd865b2769a7dd506aea4603a4603.png)
**7. Kurocoの管理画面に設定する**  
次にKuroco管理画面へ移動し、[外部システム連携] -> [vimeo]に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbd734b6453e3bebb0702d9f468ec92d.png)

「6. Access Tokensを作成する」で取得した、「Client identifier」「Client secrets」「Access token」をセットします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/402b9060c6cd45cd755e9b41b5d3425f.png)

値を記入したら、[更新する] ボタンをクリックします。  
以上でKurocoとVimeoが連携できるようになりました。  

Plus以上のプランを契約している場合、アップロードのデフォルトを設定できるので下記設定に進んでください。  
特に設定が必要ない場合は[連携したVimeoの利用方法](#連携したvimeoの利用方法)に進んでください。

**8. Vimeoの設定をする**  
[Vimeoの設定画面](https://vimeo.com/settings/videos/embed_presets)に移動し、[新規プリセットを追加]をクリックして、プリセットの設定画面に遷移します。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bd4a5c677d313f4a250b90dd26121f38.png)
**9. プリセットを作成する**  
下記の部分でプリセットを設定します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/89962274c7b72c46919f3be3ad308bd6.png)
設定完了したら[保存]をクリックします。

**10. アップロードのデフォルトを設定する**  
[アップロードのデフォルト画面](https://vimeo.com/settings/videos/upload_defaults)からアップロードのデフォルトを設定します。プリセットは先ほど作成したものを選択してください。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e28f4e4b464facc3f830e7b36bf5b409.png)
設定完了したら[保存]をクリックします。  


## 連携したVimeoの利用方法
**1. コンテンツ定義を編集する**  
FirebaseまたはAmazon S3とVimeoの連携が完了すると、[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#コンテンツ定義編集)のページで拡張項目に「動画ファイル(Vimeo/)」が選択できるようになります。  
対象のコンテンツ定義より、「動画ファイル(Vimeo)」を設定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f863f031ff9f3914bc597c836487d944.png)

**2. コンテンツに動画をアップロードする**  
対象のコンテンツの追加・編集ページで動画をアップロードします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a070a95a23d788ac6b9fe131be7ac3b.png)

動画はVimeoにアップロードされます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0e779da8dee3dfc991867703e1ae2e3.png)

**3. フロントで表示する**  
フロントでは下記のようにVimeoのリンクを取得できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b0f95ff4dc49d9571929fe8f474dc292.png)

参考) VimeoのリンクはChromeの開発者コンソールから、[Network]タブで実際にKurocoと通信している内容を確認するか、[Swagger UI](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)を利用して確認してください。

下記のようにフロントでVimeoの動画の表示が確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/70961f15062f8e2bee5092d380a6a7fa.jpg)

以上でKurocoとVimeoを連携し動画をアップロードできるようになりました。

## 関連ドキュメント
- [Vimeo](/ja/docs/management/vimeo/)
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法

> 元ページ: `tutorials/how-to-implement-ranking-with-google-analytics` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-ranking-with-google-analytics/
> 概要: 指定したコンテンツ定義の詳細ページのPV数を元に、過去1週間以内のアクセスランキングを表示する方法を説明します。

本チュートリアルでは、指定したコンテンツ定義の詳細ページのPV数を元に、過去1週間以内のアクセスランキングを表示する方法を説明します。  

GoogleAnalytics(以下、GA)のPV数を元にアクセスランキングを作成するには以下の処理を実装する必要があります。
1. [Kuroco管理画面からGAと連携する](#kuroco管理画面からgaと連携する)
2. [カスタムディメンションを設定する](#カスタムディメンションを設定する)
3. [フロント側でGAの計測タグを埋め込む](#フロント側でgaの計測タグを埋め込む)
4. [コンテンツ定義にPV数を設定するための拡張項目を設定する](#コンテンツ定義にpv数を設定するための拡張項目を設定する)
5. [取得したPV数をコンテンツのデータに設定する](#取得したpv数をコンテンツのデータに設定する)
6. [アクセスランキング取得用にPV数の降順で10件取得する一覧APIを作成する](#アクセスランキング取得用にpv数の降順で10件取得する一覧apiを作成する)


## Kuroco管理画面からGAと連携する

GAとの連携は[Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)のページを参考に行って下さい。  

## カスタムディメンションを設定する
下記、いずれかのようにカスタムディメンションを設定してください。  
閲覧されたコンテンツを特定するのに利用しますので送信する値はコンテンツID、もしくはslugとなります（どちらか一方で問題ありませんのでどちらを使用するかはフロントの構成に合わせて決めて下さい）。

slugを利用する場合のサンプル  
ディメンション名は任意のわかりやすい名前を設定して下さい。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/46eb4193f85114498a3afab205f37e1e.png)

## フロント側でGAの計測タグを埋め込む
フロント側の設定は[Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/#フロントエンドでgoogle-analyticsの設定をする)のフロントエンドでgoogle-analyticsの設定をするの項目を参考に行って下さい。  

このチュートリアルでは、ランキング取得したい詳細ページのPV数のみ取得するので、page_viewイベントの送信をmountedに埋め込む形で実装します。

```js [詳細ページのmountedに追記]
if (process.browser) {
    const slug = this.$route.params.asset_name // ページのURLなどからslugを取得(実際の構成に合わせて変更して下さい)
    this.$gtag('event', 'page_view', {
        'detail_page_slug': slug
    })
}
```

この段階でフロントの表示を確認し、正しくpage_viewイベントの送信が行われていればGAコンソール上でカスタムディメンションを指定することで、下記のようにPV数が確認出来ます。<br/>
※データが蓄積されるまで半日程度かかります、すぐに確認したい場合はリアルタイム計測でpage_viewイベントのパラメータを確認することが出来ます

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0a738ffc23fa88f79cb09f67a68ed2a.png)

## コンテンツ定義にPV数を設定するための拡張項目を設定する

![Image from Gyazo](https://t.gyazo.com/teams/diverta/139708376ac1e07bb20fd31e017520e6.png)
※項目の種別は`カウンター`を指定する必要があります。  
※PV数をコンテンツに設定する際、ここで設定したslugを利用します。

## API経由でのPV数取得の確認
https://ga-dev-tools.google/ga4/query-explorer/
を利用することでAPI経由でPV数を取得出来るか確認出来ます。

1. 左上の「Demos & Tools」下のトグルスイッチで `GA4` を選択
2. `Select property` で対象のプロパティを選択
3. `dateRanges` `dimensions` `metrics` `limit` `orderBys` をそれぞれ設定する
 `dimensions` には「customEvent:[設定したslugカスタムディメンション定義]」を指定する
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8f3ce7047cef7256bf7e452b78a53e61.png)
 4. [MAKE REQUEST] でGoogle Analytics Data APIを実行する
![Image from Gyazo](https://t.gyazo.com/teams/diverta/114056816ebfc68a103614f620244b40.png)

## 取得したPV数をコンテンツのデータに設定する
取得したPV数をコンテンツデータに設定するため、下記のようなSmartyPluginを実行させるバッチ処理を作成します。  
[オペレーション]->[[バッチテンプレート](/ja/docs/management/batch-template/)]から[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a32389e96335d0efc526bd75b5af8b0d.png)

バッチ処理の編集画面が開くので以下のバッチ処理を追加します。

```smarty
{*GAからPV数を取得してカウンターに設定*}
{googleanalytics var=result
update_column_slug="pv"
update_target_dimension="customEvent:detail_page_slug"
updated_topics_ids='updated_topics_ids'
topics_group_id=1}{*topics_group_idは対象のコンテンツ定義IDを指定して下さい*}

{*カウンターデータの内容をコンテンツデータに反映*}
{assign_array var=ext_data values=''}
{assign var=ext_data.topics_ids value=$updated_topics_ids}
{batch module='topics' name='sync_counter' ext_data=$ext_data}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/152a4106c8b97c68dbceab898f00e11e.png)

追加ができたらバッチ処理を動作させる頻度を設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c0e0611f9bd96f9cc412bc17ec0e15b.png)


### パラメータ詳細
googleanalyticsプラグインでは下記のパラメータが利用出来ます。  

| パラメータ名 | 説明 |
| :--- | :--- |
|var|取得結果をアサインする変数名|
|viewId|GoogleAnalyticsのViewID|
|update_column_slug|アップデートするカラムのSlug|
|update_column_index|繰り返しカラムの場合、何番目をアップデートするか指定|
|update_target_metric|利用するメトリック（デフォルト：ga:pageviews）|
|update_target_dimension|利用するディメンション（デフォルト：ga:pagePath）|
|topics_group_id|コンテンツ定義ID|
|startDate|集計開始日（デフォルト：7日前）|
|endDate|集計終了日（デフォルト：今日）|
|queries|クエリの直接指定|


## アクセスランキング取得用にPV数の降順で10件取得する一覧APIを作成する

PV数の降順で10件取得する為のAPI設定は下記となります。

|項目   |内容  |
| :--- | :--- |
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|list|  
|パラメータ|topics_group_id: `(対象のコンテンツ定義ID)`<br/>cnt: `10`<br/>order_query: `pv:desc`|

## 関連ドキュメント
- [Google Analytics](/ja/docs/management/google-analytics/)
- [バッチテンプレート](/ja/docs/management/batch-template/)
- [Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [カスタムディメンションで設定されている数値の集計結果を確認する方法はありますか？](/ja/docs/faq/how-to-generate-reports-using-custom-dimensions/)


---

# Google Analytics連携方法

> 元ページ: `tutorials/how-to-link-google-analytics` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-link-google-analytics/

KurocoではGoogle OAuth2.0認証情報を利用してGoogle Analyticsとの接続ができます。  
このチュートリアルでは、Kuroco管理画面での接続作業の方法と、接続に必要なGoogleClientID, GoogleClientSecret の取得の流れ、フロントエンドの設定方法を説明します。

:::caution
Google側の仕様の変更により、本チュートリアルと異なる箇所がある場合もございます。詳細はGoogleで最新情報をご確認ください。
:::

## Google Analytics アカウントの作成
まずは[Google Analytics](https://analytics.google.com/analytics/web/)にて、アカウントの作成、プロパティの作成をお願いいたします。

KurocoとGoogle Analytics連携のために、GA4のプロパティIDまたは測定IDが必要となります。

### 測定IDの確認方法
Google Analyticsの管理画面より[管理] -> [プロパティ] -> [データストリーム]をクリックします。
データストリームの詳細画面が確認できるので、測定ID（`G-`で始まるID。トラッキングID）をコピーしてください。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/26759765e3d416d7dd7842c8b5f8e433.png)

測定IDは、フロントエンドに設置するタグでも使用します。

### プロパティIDの確認方法
Google Analyticsの管理画面より[管理] -> [プロパティの詳細]をクリックし、プロパティID（数字）をコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ae600abf98fe0362a2330fd7499a1b3.png)

## Google OAuth 2.0 Client IDを発行する
KurocoとGoogleアカウントを接続するのに必要なGoogle OAuth 2.0 Client IDの発行の流れについて説明します。  
（既にクライアントIDとクライアントシークレットの準備ができている場合は[Google AnalyticsとKurocoを連携する](#google-analyticsとkurocoを連携する)へ進み、KurocoとGoogleアカウントを接続してください。）

**1. Google Cloud Platform にプロジェクトを作成する**  
[Google Cloud Platform](https://console.cloud.google.com/apis/dashboard/) にアクセスし、[プロジェクトを作成]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bbef97774e648bc1399ea7d458f49c23.png)
新しいプロジェクトの作成画面になりますので、プロジェクト名を入力して、[作成]をクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9193d421e54c2e5969f3f60f626471e6.png)
**2. Analytics API を ON にする**  
プロジェクトのダッシュボードから[APIとサービスの有効化]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a3f6632bc25ab30f14953a193aaefb38.png)
APIライブラリが表示されますので「Google Analytics API」「Google Analytics Data API」「Google Analytics Admin API」を探して有効にします。

:::note
GA4と連携する場合には「Google Analytics Reporting API」は有効にする必要はありません
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d253e53386831593c4dd02f6f326ce6f.png)

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e3f1f25c48132e921cc72832a7e58c07.png)

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d37c8cbae71d4e2db98ce8181fc8bbe7.png)

**3. OAuth 同意画面を作成する**  
[Google Cloud Platform](https://console.cloud.google.com/apis/dashboard/) に戻り、[OAuth同意画面]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/88c0d4355105f76aae7632b19c93befc.png)
User Typeを選択して[作成]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2fa6e5cef4ad35ca6465f0096a2e0a22.png)
必要情報を入力し、OAuth同意画面を作成します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1bdd649afbcf43258c90489da90f4af9.png)
**4. OAuth クライアント ID を作成する**  
ダッシュボードから、[認証情報]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6dd1d9e08538cef09b8d4b01fcdc0133.png)
[認証情報を作成] -> [OAuth クライアントID]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/590fa23c301fc4f53c5189c862246a40.png)
OAuth クライアントIDの作成画面が表示されるので、内容を入力し、[作成]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/083f5fb22b15e0046d0bfd286fc938e5.png)
- アプリケーションの種類はウェブアプリケーションを選択します。
- 認証済みのリダイレクトURIはKuroco管理画面の[Google Analytics](/ja/docs/management/google-analytics/)のページで確認ができます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ede4c10d1c6ec41b2766a9d8ffe5a09a.png)
**5. GoogleClientID, GoogleClientSecret を確認する**  
認証情報に作成したクライアントIDが表示されるので鉛筆マークをクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/56f590d0c3ff8b17cdb1fd9f06774f48.png)
クライアントIDとクライアントシークレットを確認します。 

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1ac8dc5c7e237cbf6c9cc3d658077591.png)
## Google AnalyticsとKurocoを連携する
**1. Google Analytics設定画面にアクセスする**  
Kuroco管理画面へアクセスし、[外部システム連携] -> [Google Analytics]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/45631452a7596ef6ae0427cb7c4fa603.png)
**2. Googleアカウントに接続する**  
GoogleクライアントIDとGoogleクライアントシークレットを入力して、[接続する]をクリックします。  

　![Image from Gyazo](https://t.gyazo.com/teams/diverta/a3e072f04fc87a3d8abb42012c685c37.png)

Googleのサイトへ遷移しますので、Goolge Analyticsのアカウントと同じユーザーでログインします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1a0ec4a499e64fd8dedb3fff89d07d2e.png)
OAuth 同意画面が表示されるので、[許可]をクリックして認証し
ます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7f0f938fd17c8ec78286f5f786518d9f.png)
認証が通るとKurocoの画面に戻るので再度ログインをします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ca7094c7fd7a4bf55a1dba883ab7a2cb.png)
**3. プロパティID / 測定IDを設定する**  
Googleアカウントの認証が通ると[プロファイル情報]の[プロパティID / 測定ID]に入力できるようになりますので、GA4のプロパティID（数字）または測定ID（`G-`で始まるID）を入力して[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1f34e718ad80a6ffe2f5c723186385c.png)

:::info
- プロパティIDは`123456789`のほか、`properties/123456789`の形式でも入力できます。
- 測定IDは大文字・小文字を区別しません。
- 更新時に、入力値に対応するプロパティの存在とアクセス権限を確認します。測定IDを入力した場合はアクセス可能なプロパティを検索するため、更新に時間がかかることがあります。
:::

:::caution
指定したプロパティが見つからない場合や、接続中のGoogleアカウントにアクセス権限がない場合は、「指定されたプロパティID／測定IDが見つからないか、アクセス権限がありません。入力内容と接続中のGoogleアカウントの権限を確認してください。」と表示され、設定は保存されません。
:::

以上で、Google Analyticsとの連携は完了です。

## フロントエンドでGoogle Analyticsの設定をする
最後に、フロントエンドでGoogle Analyticsの設定をします。  
今回はNuxt.jsでの設定方法を説明します。  

:::info
このドキュメントではGA4/GTMのトラッキングIDをnuxt.config.jsに直接記載するサンプルになっていますが、  
実際には環境毎のenvファイルによって定義し、それを読み込むやり方が望ましいです。
:::

### GTMを利用しない場合
#### @nuxtjs/google-gtagをインストールする
プロジェクトにGoogle Analytics用のモジュール `@nuxtjs/google-gtag` をインストールします。  
下記実行します。

```
npm install --save @nuxtjs/google-gtag
```

#### nuxt.config.jsにモジュール追加
nuxt.config.jsにGoogle Analyticsの設定をします。  
nuxt.config.jsを開き、下記追記します。

```js title="nuxt.config.js"
  modules: [
    '@nuxtjs/google-gtag'
  ],
  'google-gtag': {
    id: "G-XXXXXXX",
    debug: false
  },
```

:::caution
G-XXXXXXXには、ご自身の測定IDを入力してください。
:::

### GTMを利用する場合
#### @nuxtjs/gtmをインストールする
プロジェクトにGoogle Analytics用のモジュール `@nuxtjs/gtm` をインストールします。  
下記実行します。

```
npm install --save @nuxtjs/gtm
```

#### nuxt.config.jsにモジュール追加
nuxt.config.jsにGoogle Analyticsの設定をします。  
nuxt.config.jsを開き、下記追記します。

```js title="nuxt.config.js"
  modules: [
    '@nuxtjs/gtm'
  ],
  gtm: {
    id: 'GTM-XXXXXXXX',
    pageTracking: true,
    send_page_view: false,
  },
```

:::info
send_page_viewをfalseにすると初回のページ読み込み時に、page_viewイベントは送信されず、nuxtRouteイベントのみが送信されます。  
ページ遷移時にnuxt-linkを使用し、GTMを利用してnuxtRouteイベントをpage_viewイベントに変換してGA計測する場合、  
nuxtRouteイベントとpage_viweイベントで2重計測しないようにする際に設定して下さい。
:::

##### GTMの設定を行う
GTMに「Google Analytics GA4設定」、及び「nuxtRouteタグ」のpage_viewイベント発行設定を行う
![Image from Gyazo](https://t.gyazo.com/teams/diverta/22b53b2aef20a19282f1979bff8c7ff9.png)

##### Google Analytics GA4設定

Nuxtでpage_viewイベントだけを計測したいのであれば上記にチェックを入れずnuxtRouteイベントで「page_view」イベントを飛ばす形で設定する

「この設定が読み込まれるときにページビューイベントを送信する」にチェックを入れると
該当の設定が読み込まれたときにpage_viewのイベントがGA側に送られる

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d13498ef9668a76735d9bd3990be82ed.png)

#### nuxtRouteイベント設定（nuxt-linkによるページ遷移でGA側にpage_viewイベントを発火する）

トリガー  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b8e9b14c2359a6cffa8a8f485f86b65.jpg)

タグ  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4c35b21d5f0117ff168a9675d80bb223.jpg)

### Google Analyticsにて接続を確認する
サイトにアクセスし、Google Analyticsを確認すると無事アクセス情報が取得されています。

[レポート]→[リアルタイム]
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1188bb51c57b393bdb94141b2eea2f11.png)

[エンゲージメント]→[イベント]
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c5917f99e084d796084ddebf4a9db0da.png)

### Kuroco管理画面にてアクセスを確認する
Kuroco管理画面にアクセスし、[外部システム連携] -> [Google Analytics]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2e7e230256f3f1e3ca50fa996cd2d0d.png)

すると、アクセス情報が取得されています。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6a215c41cb4a51373ac4a1449700e5b6.png)

以上でKurocoとGoogle Analytics連携方法の説明を終わります。

## 関連ドキュメント
- [Google Analytics](/ja/docs/management/google-analytics/)
- [GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法](/ja/docs/tutorials/how-to-implement-ranking-with-google-analytics/)
- [Nuxt.jsでGoogleAnalytics4(GA4)をどのように設定すればいいですか？](/ja/docs/faq/how-do-i-set-up-google-analytics-4-in-nuxtjs/)
- [カスタムディメンションで設定されている数値の集計結果を確認する方法はありますか？](/ja/docs/faq/how-to-generate-reports-using-custom-dimensions/)
