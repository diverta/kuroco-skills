# Kurocoドキュメント: 管理画面 / その他

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Amazon S3（`amazon-s3`）
- Amazon SES（`amazon-ses`）
- バックアップ（`backup`）
- バッチ処理（`batch`）
- バッチテンプレート（`batch-template`）
- アクティビティ（`comment-list`）
- アクティビティ定義（`comment-module-list`）
- 独自ドメイン/TLS証明書（`custom-domain-tls-certificate`）
- カスタムメンバーフィルター（`custom-member-filter`）
- カスタムメンバーフィルターカテゴリ（`custom-member-filter-category`）
- ダッシュボード（`dashboard`）
- 拡張項目設定（`extra-information`）
- ファイルマネージャー（`file-manager`）
- JavaScriptログ（`js-log-list`）
- KurocoFront設定（`kuroco-front-settings`）
- LINE（`line`）
- トラッキング（`notification-tracking`）
- 検索（`search`）
- SendGridログ（`sendgrid-log-list`）
- サイト一覧（`site-list`）
- 請求情報（`site-payment`）
- Stripe（`stripe`）
- X（`twitter`）
- 利用状況（`usage`）
- WordPress（`wordpress`）
- WYSIWYG専用テンプレート（`wysiwygtemplate`）


---

# Amazon S3

> 元ページ: `management/amazon-s3` ｜ 公式ページ: https://kuroco.app/ja/docs/management/amazon-s3/
> 概要: Amazon S3の連携機能のための設定をします。

Amazon S3の連携機能のための設定をします。

## Amazon S3の確認方法
[外部システム連携] -> [Amazon-S3]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/230ec800b758b3415c31b865cbccbb19.png)

## Amazon S3の項目説明

<a><img src="https://t.gyazo.com/teams/diverta/97456e744ec4d13b46cefff5e3972160.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/8a02744b53965a6e97f4b231238c83e2.png" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目   |説明  |
| :--- | :--- |
|バケット|S3のバケット名を入力します。|
|AWSアクセスキー|AWSで作成したアクセスキーIDを入力します。|
|シークレットアクセスキー|AWSで作成したシークレットアクセスキーを入力します。|
|AssumeRole用IAMロールARN|引き受けるAWS IAMロールのARNを入力します。コンテナ認証情報（ECSなど）を使用する場合に設定します。アクセスキーとシークレットアクセスキーの代わりに利用できます。|
|S3 ACLを無効にする|有効にすると、S3へのファイルアップロード・コピー時にACLパラメータが付与されなくなります。S3バケットの「オブジェクト所有者」設定でACLを無効化（「バケット所有者の強制」）している場合に有効にします。|
|公開フォルダパス（ACL無効時）|[S3 ACLを無効にする]が有効な場合に表示されます。S3 ACL無効時にファイルマネージャーで公開（Public）として扱うフォルダパスを改行区切りで指定します。デフォルトは`files/a/public`です。指定できるのは`files`配下のパスのみです。バケットポリシー等で実際に公開読み取り可能になっているパスのみを指定してください。|
|CORS自動更新|無効にすると、KurocoによるS3のCORS設定の自動更新を停止し、CORS設定をAWS側で管理できます。デフォルトで有効です。|
|追加のCORSオリジン|CORSオリジン追加にドメインを入力すると、入力したドメインからS3上のファイルが表示・取得出来るようになります。|
|バケットポリシー|[S3 ACLを無効にする]が有効で、バケットと公開フォルダパス（`files/a/public`配下）が設定されている場合に表示されます。設定した公開フォルダパスへの読み取りアクセスを維持するために推奨されるバケットポリシーのJSONを確認できます。表示されたバケットポリシーはKurocoからS3バケットへ自動適用されないため、内容を確認のうえAWS側で手動で設定してください。|
|更新する|[更新する]をクリックすると設定を反映します。|

## 参考チュートリアル
Amazon S3の利用手順は、下記を参照してください。
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)

## 関連ドキュメント
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [Firebase](/ja/docs/management/firebase/)
- [GCS, S3に設定したファイルの有効期限について](/ja/docs/reference/expiration-for-files-in-gcs-and-s3/)


---

# Amazon SES

> 元ページ: `management/amazon-ses` ｜ 公式ページ: https://kuroco.app/ja/docs/management/amazon-ses/
> 概要: Amazon SESの連携機能のための設定をします。

Amazon SESの連携機能のための設定をします。

## Amazon SESの確認方法
[チャネル] -> [メール] -> [Amazon SES]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd794194d4f06d688849f64b91660621.png)

## Amazon SESの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/23399dc11ea65ff96aa2833abe866427.png)

|項目   |説明  |
| :--- | :--- |
|管理者メール|当サイトから送信されるメールの送信元などに使われるメールアドレスを入力します。（必須）|
|SES Access Key|AWSで作成したアクセスキーを入力します。|
|SES Secret Key|AWSで作成したシークレットキーを入力します。|
|SES Region|SESのリージョンを入力します。|
|送信許可ドメイン・メールアドレス|メールの送信元として許可するドメインまたはメールアドレスを、1行に1件ずつ入力します。|
|更新する|[更新する]をクリックすると設定を反映します。|

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [Kurocoからのメール送信に任意のメール配信サービスを使用する(blastengine)](/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-blastengine/)
- [Kurocoからのメール送信に任意のメール配信サービスを使用する(Mailchimp)](/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-mailchimp/)
- [メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？](/ja/docs/faq/can-i-use-my-custom-domain-for-the-sender-address/)
- [メールが送信できない場合の確認方法を教えてください。](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)


---

# バックアップ

> 元ページ: `management/backup` ｜ 公式ページ: https://kuroco.app/ja/docs/management/backup/

バックアップではKurocoに保存されたデータのバックアップファイルを作ることができます。  
バックアップの形式は、PostgreSQLのDumpファイルと画像やJS、CSSなどのファイルの圧縮ファイルの2種類です。  
サイト移行時などに必要な画像ファイルを抜き出したり、データをエクスポートする用途を想定しており、バックアップからKurocoの設定を復元する機能は持っていません。

## 確認方法
[環境設定] -> [バックアップ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e9b8b435ce59757bd0b0a62d4da9e93c.png)

## 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7be961aca734aa9ad551626366149396.png)

|項目   |説明  |
| :--- | :--- |
|メモ|バックアップにメモを残すことができます。|
|バックアップする|バックアップファイルを作成します。|
|リロード|画面を更新します。<br/>[バックアップする]をクリックしてからバックアップが完了するまで時間がかかります。[リロード]ボタンをクリックして画面を更新し、バックアップ完了しているかどうかを確認してください。|
|ステータス|バックアップの処理が処理中か完了か確認ができます。|
|バックアップ日時|バックアップを作成した日時を表示します。|
|メモ|バックアップに残したメモが表示されます。|
|サイズ|バックアップファイルの容量をファイルの容量/データベースの容量の形式で表示します。|
|リンク|[ダウンロードURL取得する]をクリックするとバックアップをダウンロードするためのリンクを表示します。<br/>ダウンロードリンクの有効期限は1時間となっており、1時間経過後は再び[ダウンロードURL取得する]のボタンが表示されます。|

## 一括削除
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3b93623fcb6cd7e1bc9d08e664a688f3.png)

一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したバックアップを一括で削除します。

## 自動バックアップ
バックアップ画面から自動バックアップを設定すると、毎日1回、自動でバックアップを取得できます。設定した保存日数を過ぎた自動バックアップは自動的に削除されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a630f1c4681e13013343ff24f1040703.png)

### 設定項目

|項目   |説明  |
| :--- | :--- |
|自動バックアップを利用する|チェックを入れると自動バックアップが有効になります。チェックを外すと無効になります。|
|バックアップ保存日数|自動バックアップを保存しておく日数を1〜365日の範囲で指定します。|
|保存する|自動バックアップの設定を保存します。|

### 動作仕様

- 自動バックアップを有効にすると、毎日1回、深夜帯（1時〜5時の間）のサイトごとに定められた時刻に自動でバックアップが取得されます。実行時刻はサーバー負荷を分散するためにサイトごとに割り当てられ、固定されます。
- 自動で取得したバックアップは、手動で取得したバックアップと同じ一覧に表示され、メモ欄には「自動バックアップ」と表示されます。手動バックアップと同様にダウンロードできます。
- 保存日数を過ぎた自動バックアップは、次回の自動バックアップ実行時に削除されます。手動で取得したバックアップは、保存日数の対象外であり削除されません。

:::note
自動バックアップの設定の保存には、環境設定の更新権限が必要です。
:::

## 関連ドキュメント
- [Backup項目一覧](/ja/docs/reference/backup-data/)


---

# バッチ処理

> 元ページ: `management/batch` ｜ 公式ページ: https://kuroco.app/ja/docs/management/batch/
> 概要: バッチ処理では登録されたバッチの一覧を確認できます。独自に追加したバッチテンプレートから登録されたバッチについては、タイトルをクリックすることで対象のバッチテンプレートの編集画面に遷移できます。

バッチ処理では登録されたバッチの一覧を確認できます。  
独自に追加したバッチテンプレートから登録されたバッチについては、タイトルをクリックすることで対象のバッチテンプレートの編集画面に遷移できます。  

## バッチ一覧
### 確認方法
[オペレーション] -> [バッチ処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/70590e03b9e9c548a6f5942d27c4b07e.png)

### 詳細検索

[詳細検索]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73c600af85d8deaa664f25ab46a3b0a3.png)

絞り込み条件を作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a48402d8ae6f62411f55baf7b8ea9612.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca951a850bc93fb317ae0dbfdf133f99.png)

|項目   |説明  |
| :--- | :--- |
|検索する|条件を設定をしてバッチの検索ができます。|
|ID|バッチのIDを表示します。|
|モジュール|バッチを利用する機能を表示します。|
|タイトル|バッチのタイトルを表示します。|
|識別子|設定した識別子を表示します。|
|ステータス|バッチの運用状態をを表示します。|
|タイプ|バッチの実行タイプを表示します。|
|実行(予定)日|バッチが実行される日を表示します。|
|最終実行日時|バッチが最後に実行された日時を表示します。|
|結果|バッチが実行された結果を表示します。|
|メモ|バッチに入力したメモを表示します。|

### 一括処理

![Image from Gyazo](https://t.gyazo.com/teams/diverta/07b6ddd67ef6cd49f3640b4c41470af7.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したバッチに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|すぐに実行する|バッチを実行します。|
|有効にする|バッチを有効にします。|
|無効にする|バッチを無効にします。|
|削除する|バッチを削除します。|

## バッチ処理編集
### 確認方法
[オペレーション] -> [バッチ処理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/70590e03b9e9c548a6f5942d27c4b07e.png)

バッチ一覧のページから編集したいバッチ処理の[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b029e3bde1398cf7ff9a58f3c014187c.png)

### 項目説明

<a><img src="https://t.gyazo.com/teams/diverta/263abe3290b92d8ffd5b299d151ee0d5.png" style="width:600px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/277c06e44785bb26232df067be9b2189.jpg" style="width:600px; max-height:none;" /></a>

|項目   |説明  |
| :--- | :--- |
|タイトル|バッチのタイトルを入力します。|
|識別子|設定したい識別子を入力します。|
|タイプ|バッチ処理の実行タイミングを選択します。|
|メンバーID|入力したメンバーIDでログインした状態でバッチが動作します。<br/>処理の先頭に`{login member_id=x}`を書いた状態と同等です。|
|メモ|バッチに関してメモを入力します。|
|使用するコンポーネント|コンポーネント設定されている場合、使用するコンポーネントを表示します。|
|テストデータ|テストをする際に$ext_dataに入るデータを入力します。|
|処理|実行内容を記述します。|

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/07603cf9cf48a23be9e3295bda77a1f7.png)

|項目   |説明  |
| :--- | :--- |
|更新する|バッチ処理の変更内容を反映します。|
|テストする|バッチ処理のテストを実行します。|

## 関連ドキュメント
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [定期的に外部サイトのキャプチャをPDF化する](/ja/docs/tutorials/how-to-use-generate-pdf/)
- [バッチ処理を利用し、PDFの1ページ目をサムネイル画像にする](/ja/docs/tutorials/how-to-make-thumb-from-pdf/)
- [バッチ処理を使用して、CSVで日次データを保存する](/ja/docs/tutorials/how-to-implement-batch-function-exports-csv/)
- [一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する](/ja/docs/tutorials/implement-reminder-and-automatic-deletion-of-members/)
- [フォームにリマインダー機能を追加する](/ja/docs/tutorials/add-reminder-function-to-form/)
- [ファイルマネージャーのファイルを自動で削除する](/ja/docs/tutorials/delete-filemanager-files-by-using-smarty-plugins/)
- [デフォルトのバッチ処理 一覧](/ja/docs/reference/batch-list/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)


---

# バッチテンプレート

> 元ページ: `management/batch-template` ｜ 公式ページ: https://kuroco.app/ja/docs/management/batch-template/
> 概要: バッチテンプレートでは自作したバッチ処理を確認・追加・更新できます。またバッチテンプレート編集画面からテンプレートのバッチ登録が可能です。

バッチテンプレートでは自作したバッチ処理を確認・追加・更新できます。  
またバッチテンプレート編集画面からテンプレートのバッチ登録が可能です。  

## バッチテンプレート一覧
### 確認方法
[オペレーション] -> [バッチテンプレート]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/757a16d46f8b36f33b655d64424b098e.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/250417cb156e958533fb48fbe8fe6a41.jpg)

|項目   |説明  |
| :--- | :--- |
|検索する|条件を設定をしてバッチの検索ができます。|
|ID|バッチのIDを表示します。|
|タイトル|バッチのタイトルを表示します。|
|識別子|設定した識別子を表示します。|
|タイプ|バッチの実行タイプを表示します。|
|メモ|バッチに入力したメモを表示します。|

### 一括処理

![Image from Gyazo](https://t.gyazo.com/teams/diverta/03fe89fc89e13a81a39176b02f0a6a33.jpg)

一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したバッチに対して一括で処理を行います。  
バッチ登録されたテンプレートは、バッチ登録を解除してから削除してください。  

## バッチテンプレート編集
### 確認方法
[オペレーション] -> [バッチテンプレート]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/757a16d46f8b36f33b655d64424b098e.png)

バッチテンプレート一覧のページから編集したいバッチ処理の[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/17946dfed7f3171bcbdb6b4014d87e68.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9588ba2161d2350efdb268803df9d68e.jpg)

|項目   |説明  |
| :--- | :--- |
|タイトル|バッチのタイトルを入力します。|
|識別子|設定したい識別子を入力します。|
|タイプ|バッチ処理の実行タイミングを選択します。<br/>[バッチを登録]をクリックすると対象のテンプレートをバッチに登録します。|
|メンバーID|入力したメンバーIDでログインした状態でバッチが動作します。<br/>処理の先頭に`{login member_id=x}`を書いた状態と同等です。|
|メモ|バッチに関してメモを入力します。|
|使用するコンポーネント|コンポーネント設定されている場合、使用するコンポーネントを表示します。|
|テストデータ|テストをする際に$ext_dataに入るデータを入力します。|
|処理|実行内容を記述します。|

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7e64f42d56506c07392b79cae410f9c1.png)

|項目   |説明  |
| :--- | :--- |
|更新する|バッチ処理の変更内容を反映します。|
|削除する|表示しているバッチを削除します。|
|テストする|バッチ処理のテストを実行します。|

## 関連ドキュメント
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [定期的に外部サイトのキャプチャをPDF化する](/ja/docs/tutorials/how-to-use-generate-pdf/)
- [バッチ処理を利用し、PDFの1ページ目をサムネイル画像にする](/ja/docs/tutorials/how-to-make-thumb-from-pdf/)
- [バッチ処理を使用して、CSVで日次データを保存する](/ja/docs/tutorials/how-to-implement-batch-function-exports-csv/)
- [一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する](/ja/docs/tutorials/implement-reminder-and-automatic-deletion-of-members/)
- [フォームにリマインダー機能を追加する](/ja/docs/tutorials/add-reminder-function-to-form/)
- [ファイルマネージャーのファイルを自動で削除する](/ja/docs/tutorials/delete-filemanager-files-by-using-smarty-plugins/)
- [デフォルトのバッチ処理 一覧](/ja/docs/reference/batch-list/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)


---

# アクティビティ

> 元ページ: `management/comment-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/comment-list/

アクティビティでは、作成したアクティビティの確認・追加・更新ができます。

アクティビティは、下記3種類に分類され、
「モジュール」で選択した値により表示が変わります。

- [Firestore以外](#firestore以外)
- [Firestore](#firestore)
- [お気に入り](#お気に入り)

それぞれ説明します。

## Firestore以外
### アクティビティ一覧
#### 確認方法

[アクティビティ定義]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d03eca17e83f0ff27222735f1510d98.png)

アクティビティ定義ページから、確認をしたいアクティビティのアクティビティ数をクリックします。
（モジュール「Firestore」以外を選択してください。）

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b6a3957ebe011296a85c8fa58d16cb3.png)

#### コメント一覧
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6efccfc2cb466d38c3b73acec6611e1b.png)

|項目   |説明  |
| :--- | :--- |
|検索する|登録済みのタグを検索できます。[詳細検索]をクリックすると、カテゴリ・公開状況・表示件数の選択欄が表示されます。条件を入力し、[検索する]をクリックすると、タグの絞り込みが可能です。|
|ダウンロードする|登録されているアクティビティ情報をダウンロードします。|
|公開状況|公開状態を表示します。|
|投稿日時|投稿日時を表示します。|
|コメント|コメントを表示します。クリックすると[アクティビティ詳細画面](#アクティビティ詳細firestore以外)に遷移します。|
|タイトル|アクティビティした該当のモジュールのタイトルを表示します。|
|投稿者|アクティビティ実行ユーザーの名前とユーザーIDを表示します。|
|IPアドレス|ユーザーのIPアドレスを表示します。|
|更新日時|最後に更新した日時を表示します。|

#### 申請一覧
「申請一覧」のタブをクリックすると、公開状況が申請中になっているアクティビティのみが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/07ee332aeb0b9007688bcbda8b15a665.png)

#### 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5169f2e293031f44fa7ddab24359169.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したアクティビティに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|公開にする|アクティビティを公開します。|
|非公開にする|アクティビティを非公開します。|
|削除する|アクティビティを削除します。|

### アクティビティ詳細
#### 確認方法
アクティビティ一覧画面より[コメント]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/095971d1129b215d129df597f204a5c8.png)

#### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d70b7f976efbc6b54d605c4efa1e4e3.png)

|項目   |説明  |
| :--- | :--- |
|名前|ユーザーの名前を表示します。|
|メールアドレス|ユーザーのメールアドレスを表示します。|
|投稿日時|投稿日時を表示します。|
|コメント|コメントを表示します。|
|モジュール名|アクティビティした該当のモジュール名を表示します。|
|拡張データ| JSON形式の拡張データを表示します。|
|IPアドレス|ユーザーのIPアドレスを表示します。|
|公開・非公開|公開ステータスを選択します。|

## Firestore

:::caution
調整中のため、本機能はご利用いただけません。更新までしばらくお待ちください。
:::

### アクティビティ一覧
#### 確認方法

[アクティビティ定義]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d03eca17e83f0ff27222735f1510d98.png)

アクティビティ定義ページから、モジュール「Firestore」のアクティビティをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/90c2c7b3db00d9084725a1b300f193e1.png)

Firestoreのアクティビティ一覧ページが表示されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/1673c429f3bdca527c39e0e8962847ed.png)
#### 項目説明

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/ec25c7943ddc111a34096fc877965978.png)
Firestoreと連携した内容が表示されます。

上記画像の赤枠内はFirstoreコレクションの名前で、緑枠内はアクティビティ設定で設定できるFirestoreフィールドです。

Firestoreを確認すると、下記のように表示されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/1f823a14a32b31500f3a484a7069ef27.png)

## お気に入り
### お気に入り一覧

#### 確認方法

[アクティビティ] -> [お気に入り]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7399060a870cdd79dd068ddbaf513698.png)

#### 項目一覧

![Image from Gyazo](https://t.gyazo.com/teams/diverta/361abcf238eed417a84d440f09ff6404.png)

|項目   |説明  |
| :--- | :--- |
|検索する|お気に入りの絞り込み検索を行えます。|
|ダウンロードする|登録されているお気に入り情報をダウンロードします。|
|お気に入りID|お気に入りのIDを表示します。|
|アクション|お気に入りのアクション種別を表示します。<br/>アクション種別にSlugが指定されている場合はSlugで表示されます。|
|お気に入り日時|お気に入りに登録された日時を表示します。|
|タイトル|ユーザーがお気に入りにしたモジュールのタイトルを表示します。|
|モジュールタイプ|ユーザーがお気に入りにしたオブジェクトのモジュールタイプを表示します。|
|お気に入りしたメンバー|お気に入りに登録したユーザーの名前とメンバーIDを表示します。|

#### 一括処理

![Image from Gyazo](https://t.gyazo.com/teams/diverta/61c34b06963aeb4d26747e8253418377.png)

一覧の左端のチェックボックスにチェックを入れて、「削除する」をクリックすると、選択したお気に入りを削除します。

#### ダウンロード
ダウンロードするボタンを押すとダウンロード設定モーダルが開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0578372b63bc44601f63b78b5d5a82d6.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/644779126c16720ee728629d6a8eb8df.png)

| 項目 | 説明 |
| :--- | :--- |
| 生成されるCSVの行数 |ダウンロードされるデータの件数が表示されます。|
| 文字コード | ダウンロードする文字コードを指定します。 |
| キャンセル | モーダルを閉じます。 |
| CSVをダウンロードする | 設定した内容でダウンロードします。 |

### アクション種別一覧

#### 確認方法

[アクティビティ] -> [お気に入り]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7399060a870cdd79dd068ddbaf513698.png)

ページタイトル「お気に入り一覧」の上の[アクティビティ]をクリックし、表示されたプルダウンメニューから、[アクション種別設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe14d55a5f35bc976f516be06f01337a.png)

#### 項目一覧

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d4c864195fa54422ec5ac514cfb559a.png)

| 項目 | 説明 |
| :--- | :--- |
|アクション種別|対象のアクション種別を表示します。|
|Slug|アクション種別に設定されたSlugを表示します。|
|更新日時|最後に更新した日時を表示します。|

#### 一括処理

![Image from Gyazo](https://t.gyazo.com/teams/diverta/159c6a614d6adac4864fefee84435247.png)

一覧の左端のチェックボックスにチェックを入れて、「削除する」をクリックすると、選択したお気に入りを削除します。

#### アクション種別編集

[追加]ボタン、もしくは編集したいアクション種別のSlugをクリックするとアクション種別編集画面に遷移します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/226ee19a270633ab6ebb75caa6229d85.png)

アクション種別編集でアクション種別とそのSlugを設定できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d4f5996c92c0ed21e1a24e7492107cdf.png)

## 関連ドキュメント
- [コンテンツにコメント機能を追加する](/ja/docs/tutorials/integrate-activity-comment/)
- [コメント機能に階層構造を追加する](/ja/docs/tutorials/add-depth-to-the-comment-function/)
- [アクティビティ機能で、特定ユーザーにしか見れないコメントを残す](/ja/docs/tutorials/how-to-only-display-comments-that-are-addressed-to-a-specific-user/)


---

# アクティビティ定義

> 元ページ: `management/comment-module-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/comment-module-list/

アクティビティ定義ではアクティビティ定義の一覧が表示されます。
アクティビティを利用することで、コンテンツに対するコメントや、お気に入りの実装が可能となります。

## アクティビティ定義一覧
### 確認方法

[アクティビティ定義]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fa623ad857577fcf2eb233b7253420.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5fda3115b96b568ed8e8dd1a2c057272.png)

|項目   |説明  |
| :--- | :--- |
|検索|登録済みのアクティビティを検索できます。[詳細検索]をクリックすると、モジュール・表示件数の選択欄が表示されます。条件を入力し、[検索する]をクリックすると、アクティビティの絞り込みが可能です。|
|ステータス|アクティビティの運用状態を表示します。|
|ID|アクティビティのIDを表示します。|
|モジュール|モジュールを表示します。|
|タイトル|アクティビティのタイトルを表示します。クリックするとアクティビティ定義編集画面に遷移します。|
|アクティビティ|件数を表示します。クリックするとアクティビティリスト画面に遷移します。|
|更新日時|最後にアクティビティを更新した日時が表示されます。|

### 一括処理

![Image from Gyazo](https://t.gyazo.com/teams/diverta/343f4530698aa5ee5eabddae3edc1094.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択した記事グループに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|有効にする|アクティビティの運用状態を「有効」にします。|
|無効にする|アクティビティの運用状態を「無効」にします。|

## アクティビティ定義追加・編集

### 確認方法
アクティビティの追加は、[追加する]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aaccae402192e6bcbdd0cd4238b01616.png)
編集をしたい場合は、アクティビティの[タイトル]をクリックします。

![Ima+B88ge from Gyazo](https://t.gyazo.com/teams/diverta/91f01f96951994c964dbb49b77cb05ba.png)

### 項目説明(モジュールが「Firebase Firestore」以外の場合)

フィールド「モジュール」で選択した値により項目が変わります。  
まずは「モジュール」が「Firebase Firestore」以外の場合の項目を説明します。　例：コンテンツ

![Image from Gyazo](https://t.gyazo.com/teams/diverta/85655e04354154739e5f891f2d7488d3.jpg)

|項目   |説明  |
| :--- | :--- |
|モジュール|利用モジュールを下記より選択します。 <ul><li>コンテンツ</li><li>アクティビティ</li>  <li>メンバー</li>  <li>タグ</li>  <li>マスタ</li>  <li>EC</li><li>Firebase Firestore</li></ul>   |
|タイトル|アクティビティのタイトルを記入します。|
|ステータス|アクティビティの運用状態を選択します。|
|APIリクエスト制限|APIリクエストの権限を選択します。<ul><li>閲覧:<br/>設定したアクティビティの閲覧制限を選択します。</li><li>投稿:<br/> アクティビティの投稿制限を選択します。</li></ul> |
|階層機能|階層機能を有効にする場合にチェックを入れます。|

### 項目説明(モジュールが「Firebase Firestore」の場合)

「モジュール」が「Firebase Firestore」の場合の項目を説明します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f4582727f227e93d4b0960a89191dda.jpg)

モジュールで「Firebase Firestore」を選択すると、入力フィールドが変更されます。  
「Firebase Firestore Collection Name」と「Firebase Firestore Collection Column Name」フィールドが追加され、「階層構造」フィールドが削除されます。

|項目   |説明  |
| :--- | :--- |
|Firebase Firestore Collection Name| Firestore collectionの名前を入力します。|
|Firebase Firestore Collection Column Name|Firestore Collectionのカラム名を入力します。含めたいカラムが複数ある場合は、改行して記入してください。|

## 関連ドキュメント
- [コンテンツにコメント機能を追加する](/ja/docs/tutorials/integrate-activity-comment/)
- [コメント機能に階層構造を追加する](/ja/docs/tutorials/add-depth-to-the-comment-function/)
- [アクティビティ機能で、特定ユーザーにしか見れないコメントを残す](/ja/docs/tutorials/how-to-only-display-comments-that-are-addressed-to-a-specific-user/)


---

# 独自ドメイン/TLS証明書

> 元ページ: `management/custom-domain-tls-certificate` ｜ 公式ページ: https://kuroco.app/ja/docs/management/custom-domain-tls-certificate/
> 概要: 独自ドメイン/TLS証明書では、サイトで使用する独自ドメインとTLS証明書の設定ができます。

独自ドメイン/TLS証明書では、サイトで使用する独自ドメインとTLS証明書の設定ができます。

## 独自ドメイン/TLS証明書の確認方法

[環境設定] -> [独自ドメイン/TLS証明書]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/62713cf2807b358cf67476802092de60.png)

## 独自ドメイン/TLS証明書の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e18944ba3437e136f893c4aeca36a527.png)

|項目   |説明  |
| :--- | :--- |
|独自ドメイン|KurocoFrontで利用するドメインを入力します。|
|独自APIドメイン|APIドメインとして利用するドメインを入力します。|
|リダイレクトドメイン|フロントエンドドメインへリダイレクトするリダイレクト元のドメインを入力します。|
|追加する|追加するをクリックすると認証に必要なDNSレコードの値が表示されます。|

## ドメイン追加後の表示

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b05a4f489a61f546308249b3944966d.png)

### 独自ドメイン

|項目   |説明  |
| :--- | :--- |
|独自ドメイン|追加した独自ドメインが表示されます。|
|ドメイン所有権の確認|ドメイン所有権確認のためのレコード種別と値が表示されます。|
|ドメインを利用する為のDNSレコード(推奨)|ドメインを利用するためのCNAMEの値が表示されます。|
|ドメインを利用する為のDNSレコード(CNAMEが利用できない場合)|ドメインを利用するためのAレコードの値が表示されます。|

### 独自APIドメイン

|項目   |説明  |
| :--- | :--- |
|独自APIドメイン|追加した独自APIドメインが表示されます。|
|ドメイン所有権の確認|ドメイン所有権確認のためのレコード種別と値が表示されます。|
|ドメインを利用する為のDNSレコード(推奨)|ドメインを利用するためのCNAMEの値が表示されます。|
|ドメインを利用する為のDNSレコード(CNAMEが利用できない場合)|ドメインを利用するためのAレコードの値が表示されます。|

### リダイレクトドメイン

|項目   |説明  |
| :--- | :--- |
|リダイレクトドメイン|追加したリダイレクトドメインが表示されます。|
|ドメイン所有権の確認|ドメイン所有権確認のためのレコード種別と値が表示されます。|
|ドメインを利用する為のDNSレコード|ドメインを利用するためのAレコードの値が表示されます。|

:::danger 要注意
独自ドメインは一度追加すると変更ができません。間違って入力してしまった場合は、サポート宛にご連絡をお願いいたします。    
[フォームより問い合わせをする](https://kuroco.zendesk.com/)
:::

## 関連ドキュメント
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)
- [別サイトで使用しているドメインをKurocoに切り替える際の手順](/ja/docs/tutorials/transferring-your-domain-from-another-site-to-kuroco/)
- [独自ドメイン登録後、kuroco-front.appのドメインをフロントエンドのステージサイトとして利用する](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)


---

# カスタムメンバーフィルター

> 元ページ: `management/custom-member-filter` ｜ 公式ページ: https://kuroco.app/ja/docs/management/custom-member-filter/
> 概要: カスタムメンバーフィルターでは、任意の検索条件を登録することができます。

ここでは任意のカスタムメンバーフィルターを登録できます。

## カスタムメンバーフィルター一覧
### 確認方法
[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bcb53cec82338ffccb79177625254bd3.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/553295a8ce7e281d56422d231f8e136e.png)

|項目   |説明  |
| :--- | :--- |
|検索する|条件を設定してカスタムメンバーフィルターを検索できます。|
|ダウンロードする|カスタムメンバーフィルターの一覧をJSON形式でダウンロードします。|
|インポート|JSONファイルを選択してカスタムメンバーフィルターをインポートします。|
|ID|カスタムメンバーフィルターのIDです。カスタムメンバーフィルターを追加すると自動で採番されます。|
|カテゴリ|カテゴリ名を表示します。|
|共有区分|カスタムメンバーフィルターを共有する範囲を表示します。|
|カスタムメンバーフィルター名|カスタムメンバーフィルターの名前を表示します。|
|メモ|カスタムメンバーフィルターに入力したメモを表示します。|
|更新日時|カスタムメンバーフィルターが最後に更新された日時を表示します。|

## カスタムメンバーフィルター編集
### 確認方法

カスタムメンバーフィルター一覧のページから[カスタムメンバーフィルター名]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb4ee0bcf32371e22f9f2246f8fb6e68.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a90a598e78cd269500b5799dc8cc5f08.png)

|項目   |説明  |
| :--- | :--- |
|ID|検索条件のIDです。検索条件を追加すると自動で採番されます。|
|タイトル|メンバーフィルターのタイトルを入力します。|
|カテゴリ|選択しているカテゴリ名が表示されます。|
|アクセス制限|検索条件を共有する範囲を設定します。|
|モジュール検索条件|メンバー検索条件、フォーム検索条件、EC検索条件、カスタム処理検索条件のうち、複数を利用する場合に、ANDにするかORにするかの条件を設定します。|
|権限設定への利用|「有効にする」にチェックが入っている場合有効になります。|
|メモ|検索条件に関してコメントを記入します。|

### カスタムメンバーフィルター編集
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e17608ddc58c9347bb16bf9a31016084.png)

|項目   |説明  |
| :--- | :--- |
|[結果を閲覧する]ボタン|クリックすると、設定したフィルターに該当する対象を確認することができます。|
|[メンバー]タブ|メンバーを検索するメンバー情報のフィルターを設定します。|
|[フォーム]タブ|ログイン状態でフォームを送信したメンバーを検索するフォームのフィルターを設定します。|
|[EC]タブ|ECのィルターを設定します。|
|[カスタム処理]タブ|カスタム処理のフィルターを設定します。|

カスタムメンバーフィルター設定方法の詳細は [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/) をご参考ください。  

### ボタンの説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c2a934169cf3b1c9c0d0c802299e000.png)

|項目   |説明  |
| :--- | :--- |
|[更新する]ボタン|検索条件の変更を反映します。|
|[削除する]ボタン|表示している検索条件を削除します。|

### 更新履歴の確認
カスタムメンバーフィルター編集画面右上の[その他]から[更新履歴]をクリックすると、カスタムメンバーフィルターを編集した履歴が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0cf56d8ddcba3af30c717914d19204cc.png)

#### カスタムメンバーフィルター更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/44de0292f857a95ee9ecb45ca716e99b.png)

|項目   |説明  |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|カスタムメンバーフィルターが更新された日時を表示します。|
|更新者|カスタムメンバーフィルターを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)
- [一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する](/ja/docs/tutorials/implement-reminder-and-automatic-deletion-of-members/)


---

# カスタムメンバーフィルターカテゴリ

> 元ページ: `management/custom-member-filter-category` ｜ 公式ページ: https://kuroco.app/ja/docs/management/custom-member-filter-category/
> 概要: カスタムメンバーフィルターカテゴリ設定では、カスタムメンバーフィルターを利用するモジュールをカテゴリを作成して分類できます。

カスタムメンバーフィルターカテゴリ設定では、カスタムメンバーフィルターを利用するモジュールをカテゴリを作成して分類できます。  

## カスタムメンバーフィルターカテゴリ一覧
### 確認方法

[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bcb53cec82338ffccb79177625254bd3.png)

ページタイトルの上の[カスタムメンバーフィルター]をクリックし、表示されたプルダウンの中にある[カテゴリ設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/182ddedb37573723a595ad7ba97247c8.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/708fb7e34cbf5dbd44b4eec19ee159ba.png)

|項目   |説明  |
| :--- | :--- |
|ID|カテゴリ毎に固有のIDを表示します。|
|カテゴリ名|カテゴリ名を表示します。|
|モジュール|利用可能なモジュールを表示します。|
|並び順|数字の大きい順に並びます。|
|更新日時|最終更新日時を表示します。|
|削除する|カテゴリを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

## カテゴリ編集
### 確認方法
[メンバー管理] -> [カスタムメンバーフィルター]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bcb53cec82338ffccb79177625254bd3.png)

ページタイトルの上の[カスタムメンバーフィルター]をクリックし、表示されたプルダウンの中にある[カテゴリ設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/182ddedb37573723a595ad7ba97247c8.png)

編集をしたいカテゴリの[カテゴリ名]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0c12a63250c1887d0125c999d6edd6c9.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6c5fb785fd99b97ad57a5a926033d4c.png)

|項目   |説明  |
| :--- | :--- |
|カテゴリ名|カテゴリ名を表示します。|
|モジュール|カテゴリに属するカスタムメンバーフィルターをどのモジュールで使用するか指定します。<br/>指定したモジュールがどの画面で利用可能になるかは[設定したカテゴリのモジュール指定が有効になる機能](#設定したカテゴリのモジュール指定が有効になる機能)を参照してください。|
|並び順|数字の大きい順に並びます。|
|更新する|カテゴリの編集内容を反映します。|
|削除する|カテゴリを削除します。|

### 更新履歴の確認
カテゴリ編集画面右上の「その他」をクリックし、[更新履歴]をクリックすると、カテゴリの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eeff6cc6d3c2d070abb3cfa968bec1a4.png)

#### カテゴリ編集更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/56b398187e22934c22e81b286faf2e44.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

### 設定したカテゴリのモジュール指定が有効になる機能
#### コンテンツ
[コンテンツ編集](/ja/docs/management/content-structure-topics/#content-editor)画面の「詳細設定」内「APIリクエスト制限」で利用可能になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ae6762ff413665ec0323bae346f0e05.png)

#### メンバー
一覧でのメンバー検索
[メンバー管理] -> [[メンバー](/ja/docs/management/member)]の「詳細検索」で利用可能です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/077f7ac7fd8075ae8ac1bb598a4c2153.png)

#### フォーム
[チャネル] -> [WEB] -> [フォーム]より、[対象フォームの基本設定](/ja/docs/management/inquiry-basic-settings)「APIリクエスト制限」で利用可能になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3f0e6cd5bda057769234bc54a283b165.png)

#### API
[API] -> [エンドポイントの設定](/ja/docs/management/api-list/)の[APIリクエスト制限]で「MemberCustomSearchAuth」を選択した場合、利用可能になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e419187571dc84c634da109dfb42f26a.png)

#### 配信
[チャネル] -> [一括配信]より、[対象配信の基本設定](/ja/docs/management/notification-basic-settings/#existing-notification)「あて先を設定する」で利用可能になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/afecc7ea061f40e5a4706f6bdbc3aa6c.png)

## 関連ドキュメント
- [カスタムメンバーフィルター](/ja/docs/management/custom-member-filter/)
- [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)
- [カスタムメンバーフィルターで利用できるカスタム処理の変数](/ja/docs/reference/variables-for-custom-function-available-in-custom-member-filters/)


---

# ダッシュボード

> 元ページ: `management/dashboard` ｜ 公式ページ: https://kuroco.app/ja/docs/management/dashboard/
> 概要: KurocoはAPIファーストのHeadless CMSです。従来のCMSのようにシステムに縛られることなく、柔軟なシステムの構築が可能となります。欲しい機能を、欲しい時に、欲しいだけ、選び取ってください。

## ダッシュボードの確認方法
[ダッシュボード]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eea958738f634a1bdfa662270172da62.png)

## ダッシュボードの項目説明
<a><img src="https://t.gyazo.com/teams/diverta/bc18821bfe3d40084b6ab32c09772e68.png" style="width:600px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/22ac9747a237298b99e73416404a101a.png" style="width:600px; max-height:none;" /></a>

|項目   |説明  |
| :--- | :--- |
|管理メモ|管理メモが表示されます。<br/>[編集する]をクリックするとメモの編集ができます。|
|検索|コンテンツ検索を行えます。|
|申請中コンテンツ|申請中のコンテンツが表示されます。|
|最近の更新コンテンツ|更新されたコンテンツが最新10件表示されます。|
|今月の転送量|今月利用した転送量が表示されます。|
|今月の費用(無料枠1,100円適用前)|今月利用した費用が表示されます。|
|利用状況|1週間分の利用状況がグラフで表示されます。|
|最新コメント|アクティビティで追加されたコメントが最新10件表示されます。|
|フォーム|送信されたフォームが表示されます。|

## 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7412c1cdb27f900c8321a7a2307a5196.png)

|項目   |説明  |
| :--- | :--- |
|設定|[ダッシュボードのウィジェット](/ja/docs/management/dashboard-widget/)へ遷移します。|
|編集する|管理メモの編集ができます。|
|検索する|[検索](/ja/docs/management/search/)機能を利用したキーワード検索ができます。|

## 関連ドキュメント
- [ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/)


---

# 拡張項目設定

> 元ページ: `management/extra-information` ｜ 公式ページ: https://kuroco.app/ja/docs/management/extra-information/
> 概要: メンバーの拡張項目を設定では、標準の項目以外の項目をメンバーの情報に追加できます。

メンバーの拡張項目設定では、標準の項目以外の項目をメンバーの情報に追加できます。

## 拡張項目設定の確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[メンバー詳細設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c4153ee44a6727c9da745e24ccd561b.png)

その他の設定の[登録されるメンバーの拡張項目を設定する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e108df69780d992ab342c29294a6119d.png)

## 拡張項目設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/52a18c3a2737b0e2bb47321a3ec03ff7.png)

|項目   |説明  |
| :--- | :--- |
|項目名(必須)|項目名を入力します。<br/>入力した項目名はメンバー編集画面の[プロフィール情報]タブに表示されます|
|識別子(必須/半角英数字)|識別子を入力します。|
|設定|入力形態を選択します。<br/>単一選択などの選択形式の選択肢は、`[キー]::[値](改行)`の形式で入力します。<br/>例：単一選択<br/>0::受け取る<br/>1::受け取らない|
|入力制限|入力制限を設定します。|
|並び順|表示順を入力します。値の大きい方が上に並びます。|

## 一括設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/665b852d0795d0e09b5c9065af6d8a2a.png)

一括設定ではメンバーの拡張項目の設定をJSONファイルでエクスポート・インポートできます。

## ボタンの説明
[更新する]のボタンをクリックすると、拡張項目設定の変更内容が反映されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/929635c0373b14ad3107420e442707cc.png)

## 関連ドキュメント
- [メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)


---

# ファイルマネージャー

> 元ページ: `management/file-manager` ｜ 公式ページ: https://kuroco.app/ja/docs/management/file-manager/

ファイルマネージャーではWebサイト内で利用する画像やテキスト、動画などのファイルをアップロード、管理できます。サイドバーの [ファイルマネージャー] をクリックすると、新しいウィンドウが開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b57e42c37820e1896c8b9e3a77f9ce0.png)

## 画面の説明
### 概要
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4bcae1a4bc15463d66d2234c05910b5.png)

#### 1. アップロード 
新しいファイルをアップロードします。[アップロード] ボタンをクリックすると、ファイル選択ダイアログが表示されます。ファイルは幾つでも選択できます。ファイルを選択すると、アップロード処理が開始されます。ファイル形式が画像の場合、サムネイルが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e912723eb9c0e2b3c427387604ae61c5.jpg)

#### 2. 新しいフォルダを作成
[新しいフォルダを作成] ボタンをクリックすると、新しいフォルダを作成するためのダイアログが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/387a1d0dbf898ec31770f21a4f6c9c1d.png)

新しく作成したフォルダは左側のサイドバーに反映されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3b5619eebc2b1098e93e4b54061ee226.png)

#### 3. 絞り込み
検索機能です。入力条件にマッチするファイルだけに絞り込んで表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05681754f0919d6813550aa514b7e912.png)

#### 4. 表示設定
ギアアイコンをクリックすると、ファイル一覧の表示に関するカスタマイズメニューが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc0dd579ef5f4878a11a1e6fac3a9206.png)

設定項目は次の通りです。

| 項目 | 説明 |
|:------|:------|
| 表示項目 | ファイル名、日時、ファイルサイズの表示/非表示切り替えます。 |
| ビュー | 表示方法を一覧 / サムネイル / コンパクトに切り替えます。 |
| ソート | ファイル名、ファイルサイズ、日時でソートします。 |
| 順序 | ソート条件を昇順 / 降順に切り替えます。 |
| サムネイルのサイズ | サムネイル表示のアイコンサイズを150〜500に変更します。 |

#### 5. フォルダ一覧
作成しているフォルダをツリー表示します。  
デフォルトで利用できるフォルダは以下になります。  

- KurocoFiles
- KurocoFiles(メタデータ付き)
- KurocoFiles(閲覧制限)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/093da58cfe1ee90018739ee97571b243.png)

#### 6. ファイル一覧
フォルダ一覧で選択されているフォルダの中に入っているファイルを一覧表示します。表示方法は[4. 表示設定](#4-表示設定)で指定されている方法によります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/64b4e3503fb0d9208c2968abd0098fec.png)

### フォルダを選択した際のメニュー

フォルダ一覧でフォルダを選択すると、上部のツールバーが下の画像のように変わります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6506f53afa8cec3cd0b01edd2a440e60.png)

※ KurocoFiles は規定のフォルダなので、ファイル名の変更や削除はできません（ボタンも表示されません）

#### 1. アップロード
選択されているフォルダの中にファイルをアップロードします。

#### 2. 新しいフォルダを作成
選択されているフォルダの中に新しいフォルダを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/12239054fd7ff9cbc374f149e2186963.png)

#### 3. 名前を変更
名前を変更します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/671115ed7d4eb184992c6493073bbdf1.png)

#### 4. 削除
選択されているフォルダを削除します。確認ダイアログが出ますので、問題なければ[OK]ボタンを押してください。内包されているファイルも削除されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c979327dd754f11435519fa4fd62c86.png)

### ファイルを選択した際のメニュー

ファイル一覧でファイルを選択すると、上部のツールバーが変わります。これは画像とそれ以外の場合で異なります。画像の場合は次のようになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/afea3d992ba546b08edab77a1580eedd.png)

画像ではないファイルの場合は次のようになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/afc1634219da26b516f86c43c80cf559.png)

違いは[編集]ボタンの有無になります。

#### 1. アップロード
選択されているフォルダの中にファイルをアップロードします。

#### 2. 画像だけを表示
選択されているファイルを拡大表示します。画像の場合は、その内容を表示します。それ以外の場合はアイコンを表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a63fc1d3f35f078d689ca585cdfadb0.png)

#### 3. ダウンロード
選択されているファイルをダウンロードします。

#### 4. 編集
編集機能を使って画像を簡易的に編集できます。編集後、 [保存します] ボタンを押して編集内容を反映してください。編集内容を元に戻す場合は [リセット] ボタンを押してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1e8ea6da32302c93a1bcb1841378712.png)

##### 4-1. リサイズ  
画像サイズを変更します。「縦横比を維持します。」チェックボックスを付けることで、元の画像幅と高さの比率を維持します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6134fbae07d9e39d0cacc6ac19726cc6.png)

##### 4-2. クロップ

画像を一部切り抜きます。「縦横比を維持します。」チェックボックスを付けることで、元の画像幅と高さの比率を維持します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d8eab1b60b51b2f045b9f9653891562.png)

##### 4-3. 回転

画像を回転させます。右90度または左90度を指定できます。反転させる場合には2回実行してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6116c1e44e730155f04a056c9ca23a7.png)

##### 4-4. 調整します。

画像の輝度や彩度を細かく変更できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8fe50c15d7ac36010a229ad4138840e6.png)

用意されている設定は次の通りです。

| 項目 | 説明 |
|:------|:------|
| 輝度 | 輝度を調整します。 |
| コントラスト   | コントラストを調整します。 |
| 彩度 | 明度を調整します。 |
| 露出   | 露出を調整します。 |
| セピアトーン | セピア調にします。 |
| シャープ  | シャープ度を調整します。 |

##### 4-5. プリセット

予めAjustの設定を指定したプリセットを用意しています。手軽に画像を編集したい際に選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b07c989151e7020fd1fb3ece7275bf1.png)

用意されているプリセットは次の通りです。

- 明快さ
- ハー・マジェスティ―
- ノスタルジア
- ピンポール
- 日の出
- ビンテージ

#### 5. コピー

選択したファイルを指定したフォルダにコピーします。階層下のフォルダを指定する場合には、フォルダツリーの右側にある三角形をクリックしてください。同じフォルダにはコピーできませんので注意してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f383f4bda5389999cdce2ecd834a25a.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/60993dac859c0f446178b3a791045a52.png)

#### 6. 移動

選択したファイルを指定したフォルダに移動します。階層下のフォルダを指定する場合には、フォルダツリーの右側にある三角形をクリックしてください。同じフォルダには移動できませんので注意してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ac1f173f7b2fee7ffed9bb92d6adf1f.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8b275a24cdfb0e1e5e3b570ff4d57575.png)

#### 7. 名前を変更

選択したファイルの名前を変更します。デフォルト値は元のファイル名です。変更後、[OK]ボタンを押してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/26856b1c2b8786df270486f6055b0040.png)

#### 8. ファイルパス

選択したファイルのパスとURLを確認します。ファイルパスのリンクをクリックすると、URLが開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/43fe55024e6f41aaa464a0bc177930b6.png)

KurocoFiles(閲覧制限)のフォルダのファイルパスをフロントエンドで利用する場合はAPIドメインを利用してください。  
以下の用途となっております。  

- 管理画面ドメインベースのURL：サイト管理者のファイル確認用 
- APIドメインベースのURL：フロントエンドで利用するリンク用

#### 9. 削除

選択したファイルを削除します。確認ダイアログが出ますので、問題なければ[OK]ボタンを押してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/40afa1a04b4840e0aeb2da7015cb5a69.png)

## ZIPファイルの展開
アップロードしたZIPファイルを右クリックし、[Unzip]をクリックすると、ファイルマネージャー内で、ZIPファイルの展開が可能です。  
ZIPファイルをアップロード後、ファイルマネージャー内で展開することで、複数のファイルを一度にアップロードできます。  

:::info
Unzip機能が利用できるディレクトリは以下になります。
- KurocoFiles
- KurocoFiles(閲覧制限)
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb93406df692b6125f8a06aa23175a98.png)

## ZIPファイルのダウンロード
ファイルマネージャーでは、複数のファイルやフォルダをZIP形式でまとめてダウンロードできます。

- ファイル一覧で2つ以上のファイルを選択すると、ツールバーに [Download as ZIP] オプションが表示されます。
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/f83f7a5bd8326484c01d0fcc92ffb4f2.png)
- フォルダを右クリックすると、コンテキストメニューに [Download as ZIP] オプションが表示されます。
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ef573d8d206d1b2c0849655f9aa95fa.png)

:::caution
ZIPファイルのダウンロードには500MBの容量制限があります。
:::

## フォルダの権限設定
自身で作成したフォルダ(ルートフォルダ以外)を右クリックし、[フォルダーACL]をクリックすると、フォルダに対して権限の設定が可能です。  

:::info
フォルダーACLの設定にはスーパーユーザーの権限が必要です。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/34af0041e877a6127b0058c11453ecd2.png)

### 公開フォルダー(KurocoFiles)の権限
KurocoFilesとKurocoFiles(メタデータ付き)のフォルダは以下の設定ができます。  
編集許可グループ設定をした場合、権限を持たないユーザーは、ファイルマネージャー上で対象のフォルダが表示されなくなります。

- 許可する拡張子
- 拒否する拡張子
- 編集許可グループ設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dea8f24ae02fb84c7c802ab7b5ae651f.png)

### プライベートフォルダー(KurocoFiles(閲覧制限))の権限
プライベートフォルダーでは以下の設定ができます。  

- 許可する拡張子
- 拒否する拡張子
- 編集許可グループ設定
- 閲覧許可グループ設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5bf78ff083adc96f086ef7d315fc11d.png)

閲覧権限を持たないユーザーが対象のファイルにアクセスすると、「ページが存在しません。」の表示になります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd354b1140f228c46294500a21e37536.png)

### 権限の継承
親フォルダーのアクセス権限を設定すると、すべてのサブフォルダーに同じ権限が適用されます。  
サブフォルダーに特定の権限を設定する必要がある場合は、直接設定してください。  

## フォルダの拡張
外部システム連携をすることで、ファイルマネージャーからGCS、S3にファイルを保存できます。  
連携方法については以下のドキュメントをご参照ください。
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)

:::caution
GCSとAmazon S3の両方は同時に利用できません。
:::

## 関連ドキュメント
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)
- [ファイルマネージャーのファイルを自動で削除する](/ja/docs/tutorials/delete-filemanager-files-by-using-smarty-plugins/)
- [ファイルマネージャーで利用できるファイルの種類を教えてください](/ja/docs/faq/what-file-formats-does-the-file-manager-support/)
- [ファイルマネージャーにアップロードした画像をコンテンツの拡張項目で使用できますか？](/ja/docs/faq/can-i-use-kurocofiles-images-in-additional-fields/)
- [ファイルにcreditとdescriptionのmeta情報を追加する](/ja/docs/tutorials/file-credit-and-description-information)
- [閲覧権限のないファイルへアクセスした場合に任意のページにリダイレクトさせることはできますか？](/ja/docs/faq/is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory)


---

# JavaScriptログ

> 元ページ: `management/js-log-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/js-log-list/
> 概要: JavaScriptログではJavaScriptのログを確認できます。

JavaScriptログではJavaScriptのログを確認できます。

## JavaScriptログの確認方法
[オペレーション] -> [ログ管理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bec37ecc842bbf4422d0bb77e4f6b3d2.png)

ページタイトルの上の[ログ管理]をクリックし、表示されたプルダウンの中にある[JavaScriptログ]を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd3ad24cfa8fb83fe9b7fad3a339bddf.png)

## JavaScriptログの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b12c699d2d4a3de664cfda15a77ac4a5.png)

### 絞り込み条件

JavaScriptログではキーワードやログ日時による絞り込みと、詳細検索を用意しています。

#### キーワードによる絞り込み

[キーワード] テキストボックスに検索するキーワードを入力します。キーワードを含むログを絞り込みます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/64133ab1ece9d70a6b6a18cb927b5aea.png)

#### ログ日時による絞り込み

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f27512553c03647e9cbcfc0d71c2b74e.png)

ログ日時の開始と終了で期間選択します。選択した期間のログを絞り込みます。  
指定できるログの期間は35日間となります。過去のログ日時を指定する場合も35日間の範囲となるように指定してください。

#### 詳細検索

[詳細検索] ボタンをクリックすると、絞り込み条件を作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dce3c2d002c61f07e83f42aecb75c651.png)

絞り込み対象として指定できる項目は次の通りです。

| 項目 | 説明 | 指定できる条件 |
| :--- | :--- | :--- |
| ホスト | アクセスされたサイト | [検索条件](#検索に利用できるオペレーションについて) |
| URI | アクセスしたページのURI   | [検索条件](#検索に利用できるオペレーションについて) |
| メッセージ | ログの message1〜5の内容 | [検索条件](#検索に利用できるオペレーションについて) | 
| コールスタック | ログの stack | [検索条件](#検索に利用できるオペレーションについて) | 
| 送信元IPアドレス | リクエストを行ったユーザーのIPアドレス | [検索条件](#検索に利用できるオペレーションについて)  | 
| ユーザーエージェント | アクセスしたWebブラウザのユーザーエージェント | [検索条件](#検索に利用できるオペレーションについて) |


詳細検索は複数の条件をAND、またはORで連結できます。ANDの場合は指定した条件すべてにマッチするデータのみを対象とします。OR条件は指定した条件のいずれかにマッチするデータを対象とします。

#### 検索に利用できるオペレーションについて

検索では次のオペレーションが指定できます。

| オペレーション   | 型 | 対象となるデータ |
| :---               | :--- | :--- |
| 含む            |  文字列 | 条件が一部に一致するデータ |
| 含まない        | 文字列 | 条件がいずれにも一致しないデータ |
| =               | 文字列・数値 | 条件に一致するデータ |
| !=              | 文字列・数値 | 条件に一致しないデータ |
| <               | 文字列・数値 | 条件未満のデータ |
| >               | 文字列・数値 | 条件より大きいデータ |
| <=              | 文字列・数値 | 条件以下のデータ |
| >=              | 文字列・数値 | 条件以上のデータ |
| で始まる         | 文字列 | 条件ではじまるデータ |
| で始まらない     | 文字列 | 条件ではじまらないデータ |
| で終わる         | 文字列 | 条件で終わるデータ |
| で終わらない     | 文字列 | 条件で終わらないデータ |
| どれかを含む     | 文字列・数値 | 条件を複数指定し、いずれかの条件に一致するデータ |
| どれも含まない   | 文字列・数値 | 条件を複数指定し、いずれの条件にも一致しないデータ |

##### 並び順について

ソートキーと表示順を選択することで検索結果の並び順を指定できます。並び順はASC（昇順。小さい方から大きくなっていく）またはDESC（降順。大きい方から小さくなっていく）を指定できます。

### ログ一覧項目

ログとして一覧されるデータの項目は次の通りです。

| 項目 | 説明 |
| :--- | :--- |
| ログ日時 | ログの記録された日時を表示します。|
| ホスト | アクセスされたサイトを表示します。|
| URI | アクセスしたページのURIを表示します。 |
| メッセージ | ログの補完情報を表示します。 |
| コールスタック | TRACE情報を表示します。<br/>JavaScript側の実装によっては必要な情報が取得できない場合等もありますので、フロントエンド側の実装との連携が重要なログになります。 |
| 送信元IPアドレス | リクエストを行ったユーザーのIPアドレスを表示します。 |
| ユーザーエージェント | アクセスしたWebブラウザのユーザーエージェントを表示します。 |

### ボタンの説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/25f9d32cc8afcf2358c1d896736e936c.png)

| ボタン  | 説明 |
| :--- | :--- |
| 検索する | 指定した絞り込み条件で検索します。 |
| ダウンロードする | ログ一覧で表示しているログ情報をダウンロードします。 |
| 削除する | ログ一覧で表示しているログ情報を削除します。 |

### ログ一覧のダウンロード
[ダウンロードする]ボタンをクリックするとダウンロード設定が開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7fd8e52d2851176c834bf5f52cc64757.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c0de24b0571392b4b347c49feaf6cd8.png)

| 項目 | 説明 |
| :--- | :--- |
| 文字コード | CSVファイルの文字コードを設定します。 |
| キャンセル | ダウンロードをキャンセルします。 |
| ダウンロードする | ダウンロードします。 |

## 関連ドキュメント
- [ログ管理](/ja/docs/management/log-management/)
- [KurocoFrontログ](/ja/docs/management/front-log-list/)
- [PCのブラウザでJSエラーを確認する方法を教えてください。](/ja/docs/faq/how-to-check-for-js-errors-in-a-pc-browser/)


---

# KurocoFront設定

> 元ページ: `management/kuroco-front-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/kuroco-front-settings/

KurocoFront設定では、KurocoFrontでデプロイされたフロントエンドのキャッシュをクリアできます。

## KurocoFront設定の確認方法
[チャネル] -> [WEB] -> [KurocoFront設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ca6693359c8c5cd9e96495ba9ba95da.png)

## KurocoFront設定の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f8d1fa05b7a718c4bf6bd02659d1d786.jpg)

|項目   |説明  |
| :--- | :--- |
|キャッシュ|[キャッシュクリアする]をクリックするとKurocoFrontでデプロイされたフロントエンドのキャッシュをクリアします。|
|トークン|KurocoにWebhookを送信してデプロイする場合に使用するトークンを追加・削除できます。<br/>[GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)|
|90日以上前の履歴を削除する|有効にするとKurocoFrontに保存された古い履歴を自動的に削除します。<br/>削除の対象にはプレビューデプロイも含まれます。|
|KurocoFrontヒストリー|KurocoFrontへのデプロイ履歴を表示します。|

## 関連ドキュメント
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [GitHub](/ja/docs/management/github/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)


---

# LINE

> 元ページ: `management/line` ｜ 公式ページ: https://kuroco.app/ja/docs/management/line/
> 概要: LINEの連携機能のための設定をします。

LINEの連携機能のための設定をします。

## LINEの確認方法
[チャネル] -> [メッセージング] -> [LINE]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/de0f457c09e66c39aa82399486f31c7a.png)

## LINEの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c2ebacc1cd9474acd38853bcc0e528b1.png)

|項目   |説明  |
| :--- | :--- |
|LINE|LINE連携を有効にする場合はチェックを入れます。|
|チャンネルID|LINEの管理画面で確認したチャンネルIDを入力します。|
|秘密鍵|ブラウザで生成した秘密鍵を入力します。|
|アサーション署名キー|LINEの管理画面で確認したアサーション署名キー(kid)を入力します。|
|更新する|[更新する]をクリックすると設定を反映します。|

## テスト送信

LINE連携が有効で、かつチャンネルIDとアサーション署名キー(kid)が設定されている場合、テスト送信フォームが表示されます。保存済みの設定を使って、実際にLINEユーザーへメッセージを送信し、連携が正しく設定されているかを確認できます。

:::caution
テスト送信すると、指定したLINEユーザーに実際にメッセージが送信されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a0ad0b1e1b261e94356c95e63d24051.png)

| 項目 | 説明 |
| :--- | :--- |
| あて先 | 送信先のLINEユーザーIDを入力します。 |
| メッセージ | 送信するテキストを入力します。 |
| テストする | [テストする]をクリックすると、入力したメッセージをLINEに送信します。送信に成功すると「LINEメッセージを送信しました。」、失敗すると「LINEメッセージの送信に失敗しました。」と表示されます。 |

## 関連ドキュメント
- [LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)


---

# トラッキング

> 元ページ: `management/notification-tracking` ｜ 公式ページ: https://kuroco.app/ja/docs/management/notification-tracking/
> 概要: 配信のトラッキングを確認できます。

配信トラッキングを確認できます。

## トラッキングへの遷移方法
[チャネル] -> [一括配信] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

配信一覧画面のタイトルをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eeeb19a4f3bc92a330faf543750e91b.png)

配信編集画面の[トラッキング]タブをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c2b41a429e2b7c10ab4d111984e8f91.png)

## トラッキング 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15c8926961c4c805f2d0a809c787735b.png)

|  項目  |  説明  |
| :--- | :--- |
|  ID | メッセージ作成時に自動で採番されます。  |
|  件名  |  配信したメッセージの件名です。<br/>タイトルをクリックするとメッセージの内容を確認できます。 |
|  あて先  |  配信の配信先を表示します。  |
|  送信数  |  送信数を表示します。  |
|  配信  |  実際に配信が届いた数を表示します。  |
|  メールバウンス  |  配信ができなかった数を表示します。  |
|  開封率  |  配信の開封率を表示します。  |
|  クリック数  | 配信メッセージ内にURLの記載がある場合、該当URLがクリックされた数を表示します。<br/>URLが複数ある場合、複数行表示されます。   |
|  送信開始日時  |  送信を開始した日時が表示されます。  |

## 関連ドキュメント
- [配信メッセージ](/ja/docs/management/notification-messages/)
- [配信一覧](/ja/docs/management/notification-list/)
- [配信 メッセージ作成](/ja/docs/management/notification-message-editor/)
- [SendGridログ](/ja/docs/management/sendgrid-log-list/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)


---

# 検索

> 元ページ: `management/search` ｜ 公式ページ: https://kuroco.app/ja/docs/management/search/

キーワードを指定して管理画面内を横断検索できます。

## 検索の確認方法
[検索]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4eb036f1ec67184af8da2bb6b19d063d.png)

## 検索の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bdf21481950ee2f89cfe5738559c01c.png)

|項目   |説明  |
| :--- | :--- |
|キーワード|検索したいキーワードを入力します。|
|検索|クリックすると検索を実行します。|

## 検索結果の表示
検索結果では検索をした機能の名称と、キーワードでヒットした件数が表示されます。  
数字をクリックすると対象のページへ遷移します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0f1c5844332207c33c9cad07446f372.png)

## 関連ドキュメント
- [Kuroco管理画面の検索機能について](/ja/docs/reference/search-function-on-kuroco-admin-panel/)
- [管理画面](/ja/docs/management/management-screen/)
- [Kurocoのキーワード検索の種類](/ja/docs/reference/keyword-search-types/)


---

# SendGridログ

> 元ページ: `management/sendgrid-log-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sendgrid-log-list/
> 概要: SendGridのログを確認できます。

SendGridのログを確認できます。

##  SendGridログの確認方法
[オペレーション] -> [ログ管理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bec37ecc842bbf4422d0bb77e4f6b3d2.png)

ページタイトルの上の[ログ管理]をクリックし、表示されたプルダウンの中にある[SendGridログ]を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4eaf1d4f55c1caa3ddabdb0236b0f3af.png)

## SendGridログの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/005f76b673ce03a377b6fbdf5b097fc0.png)


### 絞り込み条件

SendGridではキーワードやログ日時による絞り込みと、詳細検索を用意しています。

#### キーワードによる絞り込み

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f474a9dfeaca2f54b6f4aed89f056bb9.png)

[キーワード] テキストボックスに検索するキーワードを入力します。キーワードを含むログを絞り込みます。

#### ログ日時による絞り込み

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c33c0237e71d44bf2e5f82c4c0c0f0d1.png)

ログ日時の開始と終了で期間選択します。選択した期間のログを絞り込みます。  
指定できるログの期間は35日間となります。過去のログ日時を指定する場合も35日間の範囲となるように指定してください。

#### 詳細検索

[詳細検索] ボタンをクリックすると、絞り込み条件を作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c964f8b897ce46f39798b71a56569fce.png)

絞り込み対象として指定できる項目は次の通りです。

| 項目 | 説明 | 指定できる条件 |
| :--- | :--- | :--- |
| イベント種別 | イベント種別| [検索条件](#検索に利用できるオペレーションについて) |
| 宛先メールアドレス | 宛先のメールアドレス | [検索条件](#検索に利用できるオペレーションについて) |
| 送信元IPアドレス | 送信元IPアドレス | [検索条件](#検索に利用できるオペレーションについて) |
| ユーザーエージェント | アクセスしたWebブラウザのユーザーエージェント | [検索条件](#検索に利用できるオペレーションについて) |
| 開封済み（Apple Mail Privacy Protection） | Appleのメールプライバシー保護機能を`true`または`false`で指定します。 | [検索条件](#検索に利用できるオペレーションについて) |
| URL | クリックされたURL | [検索条件](#検索に利用できるオペレーションについて) |
| URL offset | メール内に同じURLのリンクがある場合の何番目のURLか | [検索条件](#検索に利用できるオペレーションについて) |
| 配信のID | Kurocoの配信ID | [検索条件](#検索に利用できるオペレーションについて) |
| 配信メッセージID | Kurocoの配信メッセージID | [検索条件](#検索に利用できるオペレーションについて) |

詳細検索は複数の条件をAND、またはORで連結できます。ANDの場合は指定した条件すべてにマッチするデータのみを対象とします。OR条件は指定した条件のいずれかにマッチするデータを対象とします。

#### 検索に利用できるオペレーションについて

検索では次のオペレーションが指定できます。

| オペレーション   | 型 | 対象となるデータ |
| :---               | :--- | :--- |
| 含む            |  文字列 | 条件が一部に一致するデータ |
| 含まない        | 文字列 | 条件がいずれにも一致しないデータ |
| =               | 文字列・数値 | 条件に一致するデータ |
| !=              | 文字列・数値 | 条件に一致しないデータ |
| <               | 文字列・数値 | 条件未満のデータ |
| >               | 文字列・数値 | 条件より大きいデータ |
| <=              | 文字列・数値 | 条件以下のデータ |
| >=              | 文字列・数値 | 条件以上のデータ |
| で始まる         | 文字列 | 条件ではじまるデータ |
| で始まらない     | 文字列 | 条件ではじまらないデータ |
| で終わる         | 文字列 | 条件で終わるデータ |
| で終わらない     | 文字列 | 条件で終わらないデータ |
| どれかを含む     | 文字列・数値 | 条件を複数指定し、いずれかの条件に一致するデータ |
| どれも含まない   | 文字列・数値 | 条件を複数指定し、いずれの条件にも一致しないデータ |

##### 並び順について

ソートキーと表示順を選択することで検索結果の並び順を指定できます。並び順はASC（昇順。小さい方から大きくなっていく）またはDESC（降順。大きい方から小さくなっていく）を指定できます。

### ログ一覧項目

ログとして一覧されるデータの項目は次の通りです。

|項目               | 説明  |
| :---              | :---                           |
| ログ日時 | ログの記録された日時を表示します。|
| イベント種別 | イベント種別を表示します。|
| 宛先メールアドレス | 宛先のメールアドレスを表示します。|
| メッセージID | SendGridのメッセージIDを表示します。|
| 送信元IPアドレス | リクエストを行ったユーザーのIPアドレスを表示します。 |
| ユーザーエージェント | アクセスしたWebブラウザのユーザーエージェントを表示します。 |
| 開封済み（Apple Mail Privacy Protection） | Appleのメールプライバシー保護機能の利用可否を`true/false`で表示します。<br/>trueの場合は開封されている/されていないのが不明なメールとなります。 |
| URL | クリックされたURLが表示されます。 |
| URL offset | メール内に同じURLのリンクがある場合、何番目のURLかが表示されます。 |
| 配信のID | Kurocoの配信IDを表示します。 |
| 配信メッセージID | Kurocoの配信メッセージIDを表示します。 |

:::caution
SendGridのAPIキーを独自に設定している場合は、Event Webhookの設定が必要になります。  
SendGridのWebhookリファレンスは、SendGrid -> [Event Webhook Reference](https://docs.sendgrid.com/for-developers/tracking-events/event) をご確認ください。
:::

### ボタンの説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c043184d162574d057a609fdf8876e1a.png)

| ボタン  | 説明 |
| :--- | :--- |
| 検索する | 指定した絞り込み条件で検索します。 |
| ダウンロードする | ログ一覧で表示しているログ情報をダウンロードします。 |
| 削除する | ログ一覧で表示しているログ情報を削除します。 |

### ログ一覧のダウンロード
[ダウンロードする]ボタンをクリックするとダウンロード設定が開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e6b5eea2ff74f1f743ccb894fcff39d.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9c0de24b0571392b4b347c49feaf6cd8.png)

| 項目 | 説明 |
| :--- | :--- |
| 文字コード | CSVファイルの文字コードを設定します。 |
| キャンセル | ダウンロードをキャンセルします。 |
| ダウンロードする | ダウンロードします。 |

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [ログ管理](/ja/docs/management/log-management/)
- [メールログ](/ja/docs/management/mail-log-list/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [SendGridに残るログの保存場所・期間・内容について教えてください](/ja/docs/faq/sendgrid-log-storage-retention-content-details/)


---

# サイト一覧

> 元ページ: `management/site-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/site-list/

サイト一覧では対象サイトに紐づくサイトの確認、追加、同期、バックアップが可能です。  
本項目はメインサイトにのみ表示され、サイト一覧のページで追加したサブサイトの管理画面には表示されません。  

また、サイト一覧で追加したサイトは別々の管理画面として動作しますが、利用料金はまとめてメインサイトに請求となります。

## サイト一覧
### 確認方法
[環境設定] -> [サイト一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d34e973cdd6985c77e9ee4bb8703410.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a7317ed665a1a8901cd263b2017c10d.png)

|項目   |説明  |
| :--- | :--- |
|検索する|各種条件を入力して、サイトの検索をすることができます。|
|サイトキー|サイトキーを表示します。|
|サイト名|サイト名を表示します。|
|提供版|提供版を表示します。|
|ステータス|サイトのステータスを表示します。|
|ログイン|ログイン可否の状態を表示します。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/839e7befa9dc7215f94402599e02a734.png)：ログイン可能です。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/2f336cebca4714ca5ac7624d81e047c8.png)：ログインロックがされています。|
|URL|フロントエンド ドメインを表示します。|
|同期元サイトキー|同期元のサイトキーを表示します。|
|同期パターン|同期のパターン(アプリ同期 or 全同期)を表示します。|
|作成日時|サイトを作成した日時を表示します。|
|使用者|使用者のお名前と会社名を表示します。|
|利用状況|利用状況を表示します。|
|メモ|サイト編集で入力したメモが表示されます。|
|編集|クリックするとサイト編集のページに遷移します。|
|バックアップ|クリックするとサイトのバックアップを作成します。|
|SSO|サブサイトにSSOでログインします。クリックすると、既にサブサイトのメンバーとして登録されている場合は、対応する権限でログインし、まだサブサイトのメンバーとして登録されていない場合は、スーパーユーザー(group_id:1)を持つメンバーとして登録されてログインします。<br/>スーパーユーザーにのみ表示されます。|
|管理画面|クリックするとサイトの管理画面に遷移します。|

### 一括処理
一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したサイトに対して一括で処理を行います。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a5e8ed8791c277950a33105d4478f60.png)

|項目   |説明  |
| :--- | :--- |
|同期する|設定された同期元サイトキーと同期パターンを元に、同期が実行されます。|
|絞り込んだサイトを同期|現在の検索条件に一致するすべての子サイトの同期を一括で予約します。チェックボックスの選択は不要です。<br/>同期パターン（アプリ同期、アプリ同期(タグを除く)、全同期）が設定されているサイトが対象です。<br/>クリックすると対象件数を表示する確認ダイアログが表示されます。確認後、ジョブが1分間隔で登録されます。<br/>同期が未設定のサイトや、既に同期が実行中のサイトはスキップされます。処理完了後、予約件数とスキップ件数が表示されます。|
|バックアップする|選択したサイトそれぞれのバックアップを取得します。|
|削除する|選択したサイトを削除します。<br/>親サイトはサイト一覧から削除できません。サブサイトをすべて削除した後に[アカウント設定](/ja/docs/management/account/)からご対応ください。|

## サイト追加
### 確認方法
[環境設定] -> [サイト一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d34e973cdd6985c77e9ee4bb8703410.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fb8b4ea96d9e73ed9f8adcd42cce40e6.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/844d234263200290b45402819c29059c.png)

|項目   |説明  |
| :--- | :--- |
|コピー元のサイト名|コピー元にするサイトをプルダウンから選択します。|
|メモ|追加するサイトに対してメモを残すことができます。|
|サイト名|サイト名を入力します。|
|提供版|提供版を選択します。|
|サイトキー|サイトキーを入力します。<br/>サイトキーはエンドポイントのURLに使われます。<br/>（https://[ここに入ります].g.kuroco-mng.app/)<br/>半角英数字のみ利用できます。|
|URL|[フロントエンド共有]にチェックを入れてURLを選択すると、選択したサイトURLがフロントエンドドメインと、APIのCORSに設定された状態でサイトが作成されます。|
|メールアドレス|サイト利用者のメールアドレスを入力します。サイトの追加が完了すると入力したメールアドレス宛に通知がとどきます。|
|会社名|サイト利用者の会社名を入力します。|
|名前|サイト利用者のお名前を入力します。|
|追加する|クリックすると入力した内容でサイトの追加がされます。|

初期パスワードの入力欄はありません。追加したサイトの管理者パスワードはKurocoがサーバー側で生成し、サイトの追加完了メールに記載して通知します。初回ログイン時にはパスワードの変更が求められます。

## サイト編集
### 確認方法
[環境設定] -> [サイト一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d34e973cdd6985c77e9ee4bb8703410.png)

編集をしたいサイトの[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a1459cf3c5bde87c9da9dda66a4a1da.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b375be70fa604d430c33d3e7ad41ee7d.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/299ab348d745669a83bde7e6e4f63fdd.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/27c9120d16426b311e294ec36ec5519a.png)

|項目   |説明  |
| :--- | :--- |
|メモ|追加するサイトに対してメモを残すことができます。|
|サイト名|サイト名を編集できます。|
|提供版|提供版が表示されます。|
|サイトキー|サイトキーが表示されます。|
|URL|フロントエンド ドメインとして利用するURLを選択します。|
|ドメイン|フロントエンドドメイン、管理画面へのリンク、APIドメイン、KurocoFilesドメインが表示されます。|
|ステータス|サイトのステータスが表示されます|
|同期|[同期する]にチェックを入れて更新すると、選択した同期元サイトキーと同期パターンで同期を実行します。|
|メールアドレス|サイト利用者のメールアドレスを入力します。サイトの追加が完了すると入力したメールアドレス宛に通知がとどきます。|
|会社名|サイト利用者の会社名を入力します。|
|名前|サイト利用者のお名前を入力します。|
|ログインロック|[有効にする]にチェックを入れると、管理画面へのログインがロックされます。<br/>ログイン許可の有効期限で期間を設定すると、その期間はログイン可能となります。|
|メンテナンスの設定|[有効にする]にチェックを入れると、APIエンドポイントが503 Service Unavailableを返し、管理画面では「ただいま、メンテナンス中です。」の文章を表示します。|
|作成日時|サイトを作成した日時を表示します。|
|更新日時|サイトを最後に更新した日時を表示します。|
|更新する|クリックすると設定した内容を反映します。|
|更新コメント|更新時にコメントを残すことができます。|

## 関連ドキュメント
- [同期項目一覧](/ja/docs/reference/sync-site-data/)
- [会員制サンプルサイトで、開発環境と本番環境を分ける方法](/ja/docs/tutorials/separating-development-and-production-environments-for-your-sample-membership-site/)
- [独自ドメイン登録後、kuroco-front.appのドメインをフロントエンドのステージサイトとして利用する](/ja/docs/tutorials/kurocofront-app-domain-for-front-end-staging-site/)
- [フロントエンドを一つのサーバにして、サイトキーを使ってバックエンドを切り替える](/ja/docs/tutorials/one-server-for-front-end-and-switch-back-end-using-site-key/)


---

# 請求情報

> 元ページ: `management/site-payment` ｜ 公式ページ: https://kuroco.app/ja/docs/management/site-payment/
> 概要: 請求情報では請求に関する情報の確認と、クレジットカードの登録ができます。

請求情報では請求に関する情報の確認と、クレジットカードの登録ができます。  

:::info
Kuroco利用料は毎日チェックをして、無料枠分の利用を超えると強制的にメンテナンスモードがONになります。  
クレジットカードを登録すると、無料枠分超過によるメンテナンスモードが解除できるようになります。
:::

## 確認方法
[環境設定] -> [請求情報]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d99f5953d23c43f6d5be081335e96e3.png)

## 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a313b0c8434e2956aae01995f84a6c60.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1bd7a3ec49346db5889e4e06b3d987e6.png)

### 請求情報
|項目   |説明  |
| :--- | :--- |
|今月(未確定)|今月分のKuroco利用料が表示されます。|
|前月|前月分のKuroco利用料が表示されます。|
|月次費用監視アラート閾値|月次費用監視アラート閾値の金額が表示されます。<br/>[設定]をクリックすると[アカウント設定](/ja/docs/management/account/)に遷移し、月次費用監視アラート閾値の金額入力ができます。|
|決済手段|決済手段が表示されます。|
|クレジットカード|[登録する]または[変更する]をクリックすると、クレジットカードの登録画面に遷移します。|

### メール通知
|項目   |説明  |
| :--- | :--- |
|名前|メール通知を送付するお名前を入力します。|
|請求情報送付先メールアドレス|メール通知を送付するメールアドレスを入力します。|
|更新する|クリックすると、入力したメール通知の内容を更新します。|

### 支払い履歴
|項目   |説明  |
| :--- | :--- |
|日付|お支払いの日付が表示されます。|
|タイトル|お支払いのタイトルが表示されます。|
|請求額|お支払いした額が表示されます。|
|ステータス|お支払いしたステータスが表示されます。|
|領収書|[領収書]のリンクをクリックすると領収書が表示されます。|

## その他注意事項
クレジットカード支払い時の最低請求金額に関して：対象月の請求金額が50円未満の場合は、ご請求を翌月に繰り越しさせて頂きます。

## 関連ドキュメント
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)


---

# Stripe

> 元ページ: `management/stripe` ｜ 公式ページ: https://kuroco.app/ja/docs/management/stripe/
> 概要: Stripeの連携機能のための設定をします。

Stripeの連携機能のための設定をします。

## Stripeの確認方法
[外部システム連携] -> [Stripe]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/93bc8babb996b73c3a10c211cb888877.png)

## Stripeの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/832561fb798ce9054dfa1a5e53125e19.png)

|項目   |説明  |
| :--- | :--- |
|ステータス|Stripe連携を有効にする場合はチェックを入れます。|
|公開可能キー|Stripeで確認した公開可能キーを入力します。|
|シークレットキー|Stripeで確認したシークレットキーを入力します。|
|ウェブフックシークレット|Stripeで作成した署名シークレットを入力します。|
|更新する|[更新する]をクリックすると設定を反映します。|

:::caution
Kuroco での Stripe連携を無効にすると ([有効にする] ボックスのチェックを外すと)、新しいサブスクリプションの追加のみが無効になります。既存のサブスクリプションは引き続き課金されますのでご注意下さい。　　
既存のサブスクリプションも無効にするには、Stripeのダッシュボードから作業してください。
:::

## 関連ドキュメント
- [Stripeと連携して有料会員の機能を実装する。](/ja/docs/tutorials/subscription-billing-with-stripe/)


---

# X

> 元ページ: `management/twitter` ｜ 公式ページ: https://kuroco.app/ja/docs/management/twitter/
> 概要: X（旧Twitter）連携機能のための設定をします。

X（旧Twitter）連携機能のための設定をします。

## Xの確認方法
[チャネル] -> [メッセージング] -> [X]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/50810a9881ea300c9d82a0ba954d3b02.png)

## Xの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/11c443849cd2b9b25d133ff34515c004.png)

| Kuroco管理画面の項目 | X Developer Consoleの表記 | 説明 |
| --- | --- | --- |
| 有効にする | — | チェックを入れます。 |
| API Key | コンシューマーキー | X Developer Consoleの「Consumer Key」を記入します。 |
| API Key Secret | コンシューマーキーシークレット | X Developer Consoleの「Consumer Secret」を記入します。 |
| Access Token | アクセストークン | X Developer Consoleの「Access Token」を記入します。 |
| Access Token Secret | アクセストークンシークレット | X Developer Consoleの「Access Token Secret」を記入します。 |

## テスト投稿

X連携が有効で、かつAPI Keyが設定されている場合、テスト投稿フォームが表示されます。

:::caution
テスト送信すると、設定済みアカウントに実際にツイートが公開投稿されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/20181a6d28cd6560f4038e737f59d113.png)

| 項目 | 説明 |
| :--- | :--- |
| あて先 | 設定済みのアクセストークンに紐づくXアカウントが自動的に表示されます。投稿先はアクセストークンに紐づくアカウントで固定されます。 |
| メッセージ | 投稿するテキストを入力します。 |
| テストする | [テストする]をクリックすると、入力したメッセージをXに投稿します。投稿に成功すると「送信しました」と表示されます。 |

## 関連ドキュメント
- [X（旧Twitter）と連携し、コンテンツ投稿時にXへ自動投稿する](/ja/docs/tutorials/setting-up-twitter-integration/)


---

# 利用状況

> 元ページ: `management/usage` ｜ 公式ページ: https://kuroco.app/ja/docs/management/usage/
> 概要: KurocoはAPIファーストのHeadless CMSです。従来のCMSのようにシステムに縛られることなく、柔軟なシステムの構築が可能となります。欲しい機能を、欲しい時に、欲しいだけ、選び取ってください。

利用状況ではKurocoの費用・利用状況が確認できます。

## 確認方法
[環境設定] -> [利用状況]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a5ad5f3c9a086731791f0b84809bd58.png)

## 項目説明
### 管理サイト全体の費用
管理サイト全体の費用では、項目毎の費用、合計費用が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3b79f05bf33c005d2fd06d2a49e690d1.png)

| 項目 | 説明 | 
| ------------- | -------------  |
| 年月 | 年月でフィルターをかけられます | 

### 費用
ドロップダウンで選択したサイトの、項目毎の費用、合計費用が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e19a1229024daf0c52e9cf6b50496068.png)

### コストチャート

ドロップダウンで選択したサイトの、項目毎の費用をチャート形式で表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7e18aa1dda0dcb036d593515fbc03fc.png)

| 項目 | 説明 | 
| ------------- | -------------  |
| グラフの種類 | 以下の選択肢からグラフの種類を選択します。<ul><li>棒グラフ</li><li>折れ線グラフ</li></ul> | 
|日付型|以下の選択肢から横軸の表示単位を選択します。<ul><li>毎月</li><li>毎日</li></ul>|
|毎月|日付型を毎月に設定した場合に、コストチャートの開始月・終了月を選択します。|
|毎日|日付型を毎日に設定した場合に、コストチャートを表示する年月を選択します。|

### 日別利用量

それぞれの項目について、ドロップダウンで選択したサイトの日別の利用状況を表示します。    
項目は、管理サイト全体の費用より細かい単位で表示します。  

また、[ダウンロードする]をクリックすると、表示している月の日別利用料をCSVでダウンロードできます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3f695189f1c7566632ecdf961a42feb.png)

| 項目 | 計算される項目 | 
| ------------- | -------------  |
| キャッシュされたAPIリクエスト | キャッシュされたAPIリクエスト | 
| APIリクエスト | APIリクエスト | 
| API転送量 | CDN転送量 | 
| API追加処理時間 | コンピューティング | 
| 管理API・MCPリクエスト | APIリクエスト | 
| 管理API・MCP処理時間 | コンピューティング | 
| KurocoFront転送量 | CDN転送量 | 
| KurocoFiles転送量 | CDN転送量 | 
| メール | メール | 
| AI処理ユニット | AI処理ユニット |
| バッチ処理時間 | コンピューティング | 
| AIエージェント処理時間 | コンピューティング | 
| DBファイル容量 | ファイルストレージ | 
| ファイル容量 | ファイルストレージ | 
| KurocoFrontファイル容量 | ファイルストレージ | 
| ログファイル容量 | ファイルストレージ | 
| バックアップファイル容量 | ファイルストレージ | 

## 費用の計算方法
計算方法は、 **実際のカウント/UNIT** の値の小数点を切り上げ、**単価**をかけた値がとなります。

例として、APIリクエストが100hitの場合を説明します。  
**実際のカウント/UNIT** の計算式に当てはめると、100/1000 = **0.1**となります。(実際のカウントが100hit、APIリクエストのUNITが1000hit)  
0.1の場合、小数点切り上げとなるので**1**となります。  
**1**に単価の**55円**をかけるので、APIリクエストは**55円**となります。

## 合計金額の注意点
合計金額は、月の合算の金額が請求となりますが、**ファイルストレージのみ**集計期間での最大値を請求に利用します。

例えばファイルストレージで下記利用した場合の金額について説明します。  

- 2月1日：1GB
- 2月2日：2GB
- 2月3日：1GB

請求金額は最大値である2月2日に発生した2GB分の**110円**(2GB×55円)となります。

## 料金体系
料金体系は以下のページをご確認ください。
- [利用料金](https://kuroco.app/ja/pricing/)

## 関連ドキュメント
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)


---

# WordPress

> 元ページ: `management/wordpress` ｜ 公式ページ: https://kuroco.app/ja/docs/management/wordpress/
> 概要: WordPressでエクスポートしたXMLデータ及びメディアファイルをKurocoへインポートできます。

WordPressでエクスポートしたXMLデータ及びメディアファイルをKurocoへインポートできます。  

## WordPressの確認方法
[外部システム連携] -> [WordPress]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffcc70f9f869ab49f6824918341e53db.png)

## WordPressの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/39220519085bac28d7d8ece0e61aa1d9.png)

|項目   |説明  |
| :--- | :--- |
|WordPress XMLファイル|WordPressでエクスポートしたXMLファイルを選択します。|
|事前にアップロードされた XMLまたはZIP 圧縮された XML ファイルを選択|事前にアップロードされた XMLまたはZIP 圧縮された XML ファイルを選択します。|
|WordPressメディアTARファイル|WordPressでエクスポートしたメディアライブラリのTARファイルを選択します。|
|対象コンテンツ|インポート先のコンテンツ定義を選択します。|
|ステータス|インポートされたコンテンツの公開状態を選択します。|
|値がない場合の動作|値がない場合の動作を選択します。|
|入力チェックする|クリックするとインポートを開始します。|

## 関連ドキュメント
- [WordPressのXMLファイルをKurocoへインポートする](/ja/docs/tutorials/import-wordpress-xml-files-into-kuroco/)


---

# WYSIWYG専用テンプレート

> 元ページ: `management/wysiwygtemplate` ｜ 公式ページ: https://kuroco.app/ja/docs/management/wysiwygtemplate/

WYSIWYG専用テンプレートではWYSIWYGから呼び出すことのできるテンプレートの、確認・追加・修正ができます。

## WYSIWYG専用テンプレート一覧
### 確認方法
[環境設定] -> [WYSIWYG専用テンプレート]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6a2a98b14ac1b00580ce379393ba61a.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/64cc56e57d48d8b8f3ab2536d44d7b73.png)

|項目|説明|
|:--|:--|
|公開|公開、非公開のいずれかを表示します。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|テンプレート|テンプレートの名前を表示します|
|メモ|テンプレートに設定したメモを表示します。|
|更新日時|最後に更新された日時を表示します。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|

### 一括処理ボタン

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1794a50931d41a28fff03b0608a107d4.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したタグに対して一括で処理を行います。

|項目|説明|
|:--|:--|
|公開にする|テンプレートを公開にします。|
|非公開にする|テンプレートを非公開にします。|
|削除する|テンプレートを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

### WYSIWYG専用テンプレート編集
### 確認方法
[環境設定] -> [WYSIWYG専用テンプレート]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6a2a98b14ac1b00580ce379393ba61a.png)

WYSIWYG専用テンプレート一覧ページからテンプレートをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7385aa3b8831bfa3e15d429870f79c25.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2453fde9545323544ceb27ce335b9238.png)

|項目|説明|
|:--|:--|
|タイトル|テンプレートのタイトルを入力します。|
|対象|コンテンツ定義IDを選択します。|
|ボディ|テンプレートの内容を入力します。|
|メモ|テンプレートにメモを追加します。|

### 公開設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/680c1a86fe96b4c2f9eaa1eae3be93a2.png)

|項目|説明|
|:--|:--| 
|公開にする|テンプレートを公開状態にします。|
|非公開にする|テンプレートを非公開状態にします。|

### ボタンの説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b617053840cbb0c92d8db322dffb4b2.png)

|項目 |説明 | 
| :--- | :--- | 
|[更新する]ボタン|テンプレートの変更を反映します。| 
|[削除する]ボタン|表示しているテンプレートを削除します。|

### 更新履歴の確認
WYSIWYG専用テンプレート編集画面右上の[その他]から[更新履歴]をクリックすると、編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f8eb53add49d97e0751b8e3a4f5b7ceb.png)

#### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/94836882650a874886bad8e4f768be4b.png)

|項目   |説明  |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|
|比較する|選択した比較対象の２つ版の更新履歴を並べて表示します。|

## 関連ドキュメント
- [事前に保存したHTMLをWysiwygエディタで呼び出す](/ja/docs/tutorials/reuse-the-previously-saved-html-using-a-wysiwyg-editor/)
