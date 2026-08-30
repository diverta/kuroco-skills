# Kurocoドキュメント: 管理画面 / アカウント設定

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- アカウント設定（`account`）
- 定数（`constants`）
- ダッシュボードのウィジェット（`dashboard-widget`）
- Firebase（`firebase`）
- GitHub（`github`）
- Google Analytics（`google-analytics`）
- ローカライズ（`localize`）
- 管理画面プラグイン（`management-plugin`）
- 管理画面（`management-screen`）
- シークレット（`secret`）
- SendGrid（`sendgrid`）
- サイト管理（`site-settings`）
- VAddy（`vaddy`）
- Vimeo（`vimeo`）


---

# アカウント設定

> 元ページ: `management/account` ｜ 公式ページ: https://kuroco.app/ja/docs/management/account/

アカウント設定ではKurocoのアカウント情報の確認・修正ができます。

## アカウント設定の確認方法
[環境設定] -> [アカウント設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8333f307682048e40f69b909202a1b53.png)

## アカウント設定の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/060485d7fb75ac08defd26cada402596.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8ac96258b13f34886816d4e6b3c8efb7.png)

|項目   |説明  |
| :--- | :--- |
|リージョン|リージョンを表示します。|
|サイトキー|サイトキーを表示します。|
|提供版|提供版を選択することができます。|
|サイト名|サイト名を登録します。<br/>変更すると、Kurocoから届くメールの送信者名のデフォルトと、`SITE_TITLE`の定数値が変わります。|
|管理画面URL|Kuroco管理画面のURLを表示します。|
|フロントエンド ドメイン|サイト(フロントエンド側)のURLを変更することができます。|
|ステージサイト|ステージサイトを表示します。|
|APIドメイン|APIドメインを表示します。|
|KurocoFilesドメイン|KurocoFilesドメインを表示します。|
|請求情報|請求情報を表示します。|
|月次費用監視アラート閾値|金額を入力すると、月次費用が設定金額を超えた場合にメールでお知らせします。|
|メンテナンスの設定|APIエンドポイントが503 Service Unavailableを返すようになり、バッチ処理の実行も停止します。管理画面へのアクセスは可能です。|
|メールアドレス|メールアドレスを登録します。|
|会社名|会社名を登録します。|
|名前|お名前を登録します。|
|登録日時|サイトの登録日時が表示されます。|
|サイトの削除|[サイトの削除]をクリックするとサイトコンテンツの消去ページに遷移します。|
|更新する|[更新する]をクリックすると設定を反映します。|

## 関連ドキュメント
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)
- [Kurocoのバージョン管理について](/ja/docs/update/roadmap-kuroco-version/)
- [Kurocoの解約について](/ja/docs/faq/how-do-i-terminate-my-contract/)


---

# 定数

> 元ページ: `management/constants` ｜ 公式ページ: https://kuroco.app/ja/docs/management/constants/

ここではKurocoで利用する定数の一覧の確認・追加・更新ができます。

## 定数一覧
### 確認方法
[環境設定] -> [定数]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0e0a20e53b6d3f288e381719d1b0437.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/68c0d7cb6a6911b98f528c9bfac1cf2d.png)

|項目   |説明  |
| :--- | :--- |
|名前|定数の名前を表示します。|
|値|定数の値を表示します。|
|Smarty|定数をSmartyで呼び出す際の変数を表示します。|
|更新日時|定数が最後に更新された日時を表示します。|

## 定数の編集
### 編集方法
定数一覧ページから編集をしたい定数の[名前]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8db29c9d23d71de89ee1b8c86f9e0c2c.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d8c3e79f679866f1aa625da6205c9200.png)

|項目   |説明  |
| :--- | :--- |
|名前|定数の名前を入力します。|
|値|定数の値を入力します。|

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbc9ca9e3b8db4a3627d0096d7c5b6c6.png)

|項目   |説明  |
| :--- | :--- |
|更新する|定数の変更を反映します。|
|削除する|表示している定数を削除します。|

### 更新履歴の確認
環境設定画面右上の「その他」をクリックし、[更新履歴]をクリックすると、編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f531e6bac3610a43ca50dbebf4e6bf50.png)

#### 更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc2047e6d589df8bddc43c0ccd2b7303.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [Instagram基本表示APIをkurocoから呼び出してInstagramのフィードを表示する](/ja/docs/tutorials/call-the-instagram-basic-display-api-from-kuroco/)
- [プレビュートークンの有効期限を変更できますか](/ja/docs/faq/can-i-change-the-expiration-date-of-the-preview-token/)
- [コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？](/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/)
- [閲覧権限のないファイルへアクセスした場合に任意のページにリダイレクトさせることはできますか？](/ja/docs/faq/is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)


---

# ダッシュボードのウィジェット

> 元ページ: `management/dashboard-widget` ｜ 公式ページ: https://kuroco.app/ja/docs/management/dashboard-widget/

ダッシュボードのウィジェットでは独自に設定したウィジェットの一覧を確認・追加・更新できます。

## ダッシュボードのウィジェット一覧
### 確認方法
[環境設定] -> [ダッシュボードのウィジェット]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/98d736425dca24c04b22214876daa72a.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c8f55819c6dff1fd5b9338034a412730.png)

|項目   |説明  |
| :--- | :--- |
|ID|ウィジェットのIDを表示します。IDは自動で設定されます。|
|公開|公開、非公開のいずれかを表示します。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|タイトル|ウィジェットのタイトルを表示します。|
|管理画面|通常版、簡易版のいずれかを表示します。|
|更新日時|ウィジェットが最後に更新された日時を表示します。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|

### 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c164e942a3cfd2a498b425835bd90094.png)

|項目   |説明  |
| :--- | :--- |
|削除する|選択したダッシュボードのウィジェットを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

## ダッシュボードのウィジェット編集
### 確認方法
確認したいダッシュボードのウィジェットの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef71dd1cf66e695dd0877b4d0d4a6f5f.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4411a413165b578c8380a913b02d48be.jpg)

|項目   |説明  |
| :--- | :--- |
|名前|ウィジェットの名前を入力します。|
|HTML 必須|ウィジェットに表示する内容を記述します。|
|メモ|ウィジェットに関してメモを入力することができます。|
|アクセス制限|ウィジェットを適用する権限を以下のどちらかから選択し、対象のグループもしくはカスタムメンバーフィルターを指定します。<br/><ul><li>MemberCustomSeachAuth</li><li>GroupAuth</li></ul>|
|管理画面|通常版、簡易版のいずれかを選択します。|
|公開設定|ウィジェットの公開状態を設定します。|

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6eace857a0713e3ff4e0e6790c63872.png)

|項目   |説明  |
| :--- | :--- |
|更新する|ダッシュボードのウィジェットの変更を反映します。|
|削除する|表示しているダッシュボードのウィジェットを削除します。|

### 更新履歴の確認
ダッシュボードのウィジェット編集右上の「その他」から[更新履歴]をクリックすると、ダッシュボードのウィジェットの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e4b085ee9a7d7473e637dc46d81e9e6.png)

#### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/026813965a4e10dbdb606539cae52afd.png)

|項目   |説明  |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/)


---

# Firebase

> 元ページ: `management/firebase` ｜ 公式ページ: https://kuroco.app/ja/docs/management/firebase/

Firebaseへの接続/連携を設定できます。

## Firebaseの確認方法
[外部システム連携] -> [Firebase]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/10f42aa7a0a8b2833a5438d9841197a3.png)

## Firebaseの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6831c5a149829ac34dce8be33eb9b2a8.png)

### Firebase
|項目   |説明  |
| :--- | :--- |
|秘密鍵|Firebaseの管理画面で取得した秘密鍵をセットします。|
|Firebase構成|Firebaseの管理画面で取得したFirebaseConfigを貼り付けます。|
|接続する|[接続する]ボタンをクリックするとFirebaseと接続します。|

### 連携機能
|項目   |説明  |
| :--- | :--- |
|Activity|現在、こちらの機能は利用出来ません。|
|Storage|[有効]にチェックを入れるとFirebaseのストレージを有効にします。<br/>CORSオリジン追加にドメインを入力すると、入力したドメインからGCS上のファイルが表示・取得出来るようになります。|
|更新する|[更新する]をクリックすると設定を反映します。|

## 関連ドキュメント
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [定期的に外部サイトのキャプチャをPDF化する](/ja/docs/tutorials/how-to-use-generate-pdf/)
- [バッチ処理を利用し、PDFの1ページ目をサムネイル画像にする](/ja/docs/tutorials/how-to-make-thumb-from-pdf/)


---

# GitHub

> 元ページ: `management/github` ｜ 公式ページ: https://kuroco.app/ja/docs/management/github/

GitHubでは、GitHubリポジトリへの接続/連携を設定できます。

## GitHubの確認方法
[外部システム連携] -> [GitHub]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7553b3e477fd07848ee5a61724007648.png)

## GitHubの項目説明
### GitHub設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8dec4b532febe4d128e578e57bbd8052.png)

|項目   |説明  |
| :--- | :--- |
|GitHub 接続|[GitHubリポジトリと接続する]をクリックするとGitHubに接続するためのページが開きます。|

GitHubとの接続に成功すると、次のような画面が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b713ea96c72e4c4dc1b779fa4135b031.png)

|項目   |説明  |
| :--- | :--- |
|リポジトリ|連携するリポジトリを選択できます。また、KurocoFrontでデプロイする場合のYAMLファイルのサンプルコードが表示されます。|
|Githubの連携対象|ワークフロー連携したコンテンツの更新時に実行されるワークフローと対象ブランチを設定します。<br/>[Run Deployment]をクリックすると、連携したGitHub ActionsをKuroco管理画面から実行できます。|
|GitHub 接続|[接続解除する]をクリックするとGitHubとの接続を解除します。|

GitHubリポジトリとの連携方法は、[GitHubからKurocoFrontへソースをデプロイする設定](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)をご確認ください。

### ワークフロー実行リスト

GitHubと接続していると、ワークフロー実行リストの確認ができます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/86b02fcf7b58b83e557ccf1a58ea73cf.png)

|項目   |説明  |
| :--- | :--- |
|ブランチで絞り込み|表示するワークフロー実行リストをブランチで絞り込みます。|
|ID|Githubのrun_idを表示します。|
|名前|Actionsの名前、実行者、日付を表示します。|
|ステータス|Actionsの実行ステータスを表示します。|
|再実行|クリックするとGithub Actionsを再実行します。|

### AIエージェント(β) - GitHub Personal Access Token

AIエージェント(β) がこのリポジトリにアクセスするための GitHub Personal Access Token (PAT) を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ea19f06c104f5939fc8b55f4012cc68.png)

|項目   |説明  |
| :--- | :--- |
|GitHub PAT|ghp_から始まるGitHub Personal Access Token (PAT)を入力します。|

## 関連ドキュメント
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [GitHubActionsでgenerateに失敗した場合に、ビルドを中止しSlackに結果を通知する方法](/ja/docs/tutorials/handling-a-generate-error-in-github-actions/)
- [コンテンツの更新時にGitHub Actionsを自動実行する](/ja/docs/tutorials/auto-run-github-with-contents-update/)
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)


---

# Google Analytics

> 元ページ: `management/google-analytics` ｜ 公式ページ: https://kuroco.app/ja/docs/management/google-analytics/

ここではGoogle Analyticsの接続と設定を実施できます。

## Google Analyticsの確認方法
[外部システム連携] -> [Google Analytics]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2e7e230256f3f1e3ca50fa996cd2d0d.png)

## アカウント情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c33e2ad46421a1a5d60bbb7c0ab9d394.png)

|項目   |説明  |
| :--- | :--- |
|GoogleクライアントID|Google側で作成したOAuth 2.0 クライアント IDを入力します。|
|Googleクライアントシークレット|Google側で作成したクライアントシークレットを入力します。|
|Googleリフレッシュトークン|接続が完了するとリフレッシュトークンが表示されます。|
|接続|入力したクライアントIDとクライアントシークレットで接続のページへリダイレクトします。|

## 接続ステータス

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cc2905263640457fcd2fa85937c3abe2.png)

接続が完了すると「OAuth2.0認証で接続しています」の表示になります。

## プロファイル情報

![Image from Gyazo](https://t.gyazo.com/teams/diverta/89e29283f4c109c14aecc4f67a9e66b6.png)

接続が完了すると、[プロパティID / 測定ID]を入力できるようになります。

|項目   |説明  |
| :--- | :--- |
|プロパティID / 測定ID|GA4のプロパティID（数字）または測定ID（`G-`で始まるID）を入力します。更新時にプロパティの存在とアクセス権限を確認します。測定IDを入力した場合はアクセス可能なプロパティを検索するため、更新に時間がかかることがあります。|

プロパティIDは`123456789`のほか、`properties/123456789`の形式でも入力できます。測定IDは大文字・小文字を区別しません。
保存後は、入力欄の下に測定IDが表示されます。

:::info
Googleの認証が完了していない場合は、「Googleの認証が通ると、プロパティID／測定IDを設定できるようになります。先に認証情報を入力して接続してください。」と表示されます。
:::

:::caution
設定に失敗した場合は、次のメッセージが表示され、設定は保存されません。

- 「指定されたプロパティID／測定IDが見つからないか、アクセス権限がありません。入力内容と接続中のGoogleアカウントの権限を確認してください。」<br/>入力値に該当するプロパティが無い、または接続中のGoogleアカウントにアクセス権限がない場合に表示されます。
- 「Google Analyticsのプロパティ情報を取得できませんでした。接続ステータスを確認して、しばらくしてから再度お試しください。」<br/>プロパティ情報の取得自体に失敗した場合に表示されます。
:::


## 更新するボタン

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/aa7741beafd84790ab8e5d001f276afb.png)

[更新する]のボタンをクリックすると、Google Analyticsの変更を反映します。

## 関連ドキュメント
- [Google Analytics連携方法](/ja/docs/tutorials/how-to-link-google-analytics/)
- [GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法](/ja/docs/tutorials/how-to-implement-ranking-with-google-analytics/)


---

# ローカライズ

> 元ページ: `management/localize` ｜ 公式ページ: https://kuroco.app/ja/docs/management/localize/

ここでは、多言語・タイムゾーン・日付フォーマットの設定ができます。

## ローカライズの確認方法
[環境設定] -> [ローカライズ]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9737d2b18c03dd08d3c60c7c3eab386.png)

## ローカライズの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f93b656e31bbb1f12c3762a99a4b40cc.jpg)

|項目   |説明  |
| :--- | :--- |
|多言語設定|サイトの主言語、副言語を設定できます。<br/>多言語設定をしたいときは、「有効にする」をONにし、主言語と副言語を選択します。|
|タイムゾーン|タイムゾーンを選択できます。|
|日付フォーマット|日付フォーマットを選択できます。<br/>表示の例は[日付フォーマットと表示](#日付フォーマットと表示)を参照してください。|
|[更新する]ボタン|設定内容を保存します。|

:::caution
副言語が存在する場合、主言語は変更できません。  
主言語を変更したい場合は一度副言語を全て解除して更新してください。主言語が変更できるようになります。  

ただし、主言語に登録済みのコンテンツは、変更前に登録していた副言語のコンテンツに入れ代わりません。主言語と副言語を入れ替えたい場合は事前にCSVでコンテンツをダウンロードしておくことをお勧めします。
:::

## 日付フォーマットと表示

|管理画面の表示言語|日付フォーマット|表示|
|:--|:--|:--|
| JA   | M dd, yyyy   | 11月 22, 2023 (水) |
| JA   | yyyy/mm/dd   | 2023/11/22 (水)    |
| JA   | dd-M-yyyy    | 22-11月-2023 (水)  |
| JA   | dd-mm-yyyy   | 22-11-2023 (水)    |
| EN   | M dd, yyyy   | Nov 22, 2023 (Wed) |
| EN   | yyyy/mm/dd   | 2023/11/22 (Wed)   |
| EN   | dd-M-yyyy    | 22-Nov-2023 (Wed)  |
| EN   | dd-mm-yyyy   | 22-11-2023 (Wed)   |

## 関連ドキュメント
- [KurocoとNuxt.jsで、多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)
- [プレビュー機能で副言語の場合に_langのパラメータを付与できますか?](/ja/docs/faq/can-i-add-a-_lang-parameter-for-sub-language-in-the-preview-function/)


---

# 管理画面プラグイン

> 元ページ: `management/management-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/management/management-plugin/

このページでは、Kuroco管理ページにカスタムプラグインを挿入できます。 現在、Kurocoは2種類のプラグインをサポートしています。
- Vue.js
- CSS
## プラグイン一覧

### 確認方法
[環境設定] -> [管理画面プラグイン]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/258fda59cf4af0604dafc08fc0c05262.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1215da64a32079df9941311f8045d67.png)

|項目   |説明  |
| :--- | :--- |
|ステータス|ステータスを確認できます。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6ba28f304045d08a896b276917750d1.jpg)：有効<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/ded341265dda92d33617efd4d4857cb2.png)：無効|
|プラグイン ID|プラグインのIDです。プラグインを追加すると自動で採番されます。|
|名前|プラグインの名前を表示します。|
|タイプ|プラグインのタイプを表示します。(css もしくは Vue.js)|
|ソース|プラグインの保存場所を表示します。|
|対象|プラグインを読み込む管理画面のページとスロットを表示します。|
|プロップス|プロップスに入力した内容を表示します。<br/>Vue.jsプラグインの場合は、Initial propsでJSONオブジェクトを挿入することができます。一部の特定のページやスロットは追加のpropsを利用します。|
|更新日時|プラグインが最後に更新された日時を表示します。|
|編集|[設定]をクリックするとプラグインの設定画面が開きます。|


### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9545b83c16b93a4f7565ee2b56f2845c.png)
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したプラグインに対して一括で削除処理を行います。

## プラグインの追加・編集方法

### 追加方法

[追加]をクリックすると、プラグインを追加できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4601234a2806e007d113ba0e3eb8b12.png)

内容を入力後[追加する]をクリックすることで入力内容が反映します。

<a><img src="https://t.gyazo.com/teams/diverta/cde864490a64de22c6fd06bfe1e23b5b.png" style="width:400px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/284f7bdeb35e9c386ae32d32afafad75.png" style="width:400px; max-height:none;" /></a>

### 編集方法

[設定]をクリックすると、管理画面プラグインの設定画面が開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d31266ed88cdeb7e0ed2d4e4ba5aca8a.png)

内容を更新後[更新する]をクリックすることで入力内容が反映します。

<a><img src="https://t.gyazo.com/teams/diverta/e93343527a51f4b4a29456a003a508dd.png" style="width:400px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/dbde8791201812eab29ad03246c2c49d.png" style="width:400px; max-height:none;" /></a>

### 項目説明

|項目   |説明  |
| :--- | :--- |
|ステータス|ステータスを選択できます。|
|プラグイン名|プラグインの名前を入力します。|
|タイプ|プラグインのタイプを設定します。|
|ソース<br/>コンポーネント名:|Vue.jsタイプの場合、MPAのエントリーポイントのコンポーネント名を入力してください。<br/>※KurocoはMPA形式のアプリケーションをサポートしています。<br/>例: `MyEntryPoint`|
|ソース URL：|プラグインをアップロードした場所を入力します。<br/>外部サイトに配置したものを指定することも可能です。|
|マニフェストキー：|Vue.jsタイプの場合、読み込まれるコンポーネントのWebpackマニフェストキーのリストをセミコロン区切りで入力してください。 値は、Webpackのコード分割とチャンク構成によって異なります。<br/>例: `MyEntryPoint.js;vendors.*`|
|対象<br/>ページURI:|プラグインを読み込むKuroco管理画面のURIを指定します。<br/>`/management` は省略し、相対URIで指定してください。<br/>また、任意のカスタムページを指定することも可能です。 この場合、ページはプラグインの専用コンテンツとしてアクセス可能になります。|
|スロット名:|プラグインを読み込むスロットを指定します。<br/>プラグインは値に応じて様々な場所に読み込むことがで、ページによって特定のスロットに対応しています。詳細は[管理画面プラグインで利用可能なスロット一覧](/ja/docs/reference/management-plugin-slot/)を参考にしてください。|
|スロットパラメータ: |スロットのパラメータを設定します。<br/>いくつかのページでは、スロットパラメータを設定して、プラグインを読み込む条件を設定できます。<br/>例えば、コンテンツ編集ページでは、特定のグループに対してのみプラグインを読み込む設定が可能です。|
|プロップス|propsをプラグインに渡したい場合は、ここにJSONオブジェクトとして入力します。<br/>例: `{"my_prop": "my_prop_value"}`|
|更新|管理画面プラグインの編集内容を反映します。|
|コピー|常時している管理画面プラグインをコピーして新規の管理画面プラグインを作成します。|

### 更新履歴の確認
編集画面の[更新履歴]をクリックすると、編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a25c26736ed1043758a9c8da0ed24482.png)

#### 更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c106b32be0275c2df665f978b3da02e2.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインを利用して、Kuroco管理画面に任意のVueコンポーネントを適用する](/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインで利用可能なスロット一覧](/ja/docs/reference/management-plugin-slot/)


---

# 管理画面

> 元ページ: `management/management-screen` ｜ 公式ページ: https://kuroco.app/ja/docs/management/management-screen/

Kuroco管理画面の設定ができます。

## 管理画面の確認方法
[環境設定] -> [管理画面]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8971314fe7b7c03799a8a3052749a73c.png)

## 管理画面の項目説明
<a><img src="https://t.gyazo.com/teams/diverta/7b7bc99d3fc5b3c016673b189ee78674.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/dce01981b4a77b34398e83cde674669f.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/03c15d2b50801d597a5a7cb17c61cd20.png" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目   |説明  |
| :--- | :--- |
|ログイン画面の文言|ログイン画面に表示するテキストを入力します。|
|メールアドレスを管理画面ログインに利用しない|[有効にする]にチェックを入れると、管理画面ログインの際にメールアドレスを利用しないように設定します。<br/>外部連携ログインのみ利用する場合、[有効する]にチェックを入れてください。|
|管理画面カラー|管理画面のテーマ色を変更します。<br/>設定したカラーはKuroco管理画面のファビコンにも反映されます。|
|ロゴURL|ロゴのURLを入力します。|
|管理画面のアクセス制限(IPアドレス)|管理画面のIPアドレス制限を設定します。<br/>[有効にする]にチェックを入れてIPアドレスを入力すると、登録したIPアドレスからのみ、アクセスが可能になります。<br/>IPアドレスは、単一のアドレスとして指定することも、CIDR表記を用いて指定することも可能です。<br/>`#コメント`の形式でメモを追加できます。|
|KurocoFilesのアクセス制限(IPアドレス)|KurocoFilesのIPアドレス制限を設定します。<br/>[有効にする]にチェックを入れてIPアドレスを入力すると、登録したIPアドレスからのみ、KurocoFilesへのアクセスが可能になります。<br/>IPアドレスは、単一のアドレスとして指定することも、CIDR表記を用いて指定することも可能です。<br/>`#コメント`の形式でメモを追加できます。|
|Admin MCPのアクセス制限(IPアドレス)|Admin MCPエンドポイント（`/direct/rcms_api/admin_mcp/`）のIPアドレス制限を設定します。<br/>[有効にする]にチェックを入れてIPアドレスを入力すると、登録したIPアドレスからのみ、Admin MCPへのアクセスが可能になります。<br/>IPアドレスは、単一のアドレスとして指定することも、CIDR表記を用いて指定することも可能です。<br/>`#コメント`の形式でメモを追加できます。<br/>管理画面内のAIエージェント機能によるAdmin MCPアクセスもこの制限の対象になります。<br/>詳細は[MCP サーバ リファレンス](/ja/docs/reference/mcp-server/#ip-アドレスによるアクセス制限)を参照してください。|
|ファイルマネージャーで無効化するリソース|チェックしたリソースタイプはファイルマネージャーに表示されなくなります。|
|ファイルマネージャ画像最大幅|ファイルマネージャで画像をアップロードする際の最大幅をピクセル単位で指定します。指定した幅より大きい画像は自動的にリサイズされます。<br/>`0`の場合は制限なしになります。|
|ファイルマネージャ画像最大高さ|ファイルマネージャで画像をアップロードする際の最大高さをピクセル単位で指定します。指定した高さより大きい画像は自動的にリサイズされます。<br/>`0`の場合は制限なしになります。|
|ファイルマネージャ画像品質|ファイルマネージャで画像を保存する際のJPEG品質を指定します。<br/>`1`〜`100`の値を入力してください。値が範囲外の場合は`80`が使用されます。|
|拒否IPアドレスの設定|APIとKurocoFilesへのアクセスを拒否するIPアドレスを入力します。管理画面には適用されません。<br/>`#コメント`の形式でメモを追加できます。|
|セッション有効期限|セッションの有効期限を300～604800の秒数で入力します。<br/>管理画面とAPIのセッション有効期限が同時に変更できます。|
|オートログイン有効期間|オートログインの有効期限を日単位で入力します。<br/>管理画面とAPIのオートログイン有効期限が同時に変更できます。|
|CookieでPartitionedを利用する|セッション系のCookieにPartitioned属性が付与され、ChromeでのサードパーティCookieの問題を回避します。|
|最大コンテンツ定義項目数|最大コンテンツ定義項目数を入力します。<br/>30～999まで設定が可能です。|
|コンテンツ定義項目の最大繰り返し数|コンテンツ定義項目の最大繰り返し数を入力します。<br/>1～99まで設定が可能ですが、必要以上に多くすると編集画面の動作が重くなりますのでご注意ください。|
|コンテンツに設定できるカテゴリ数|コンテンツに設定できる最大カテゴリ数を入力します。<br/>1～99まで設定が可能です。|
|最大メンバー拡張項目数|最大メンバー拡張項目数を入力します。<br/>25～999まで設定が可能です。|
|次のコンテンツID|自動採番されるコンテンツIDの値を調整します。<br/>この値は増加のみ可能です。上限に達すると新しいコンテンツを追加できなくなります。|
|[更新する]ボタン|クリックすると入力した内容を反映します。|

## 関連ドキュメント
- [サイト管理](/ja/docs/management/site-settings/)
- [アカウント設定](/ja/docs/management/account/)
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [セッションの有効期限は変更できますか？](/ja/docs/faq/can-i-change-the-session-timeout-duration/)
- [複数のIPアドレスをまとめて設定できますか？](/ja/docs/faq/is-it-possible-to-set-multiple-ip-addresses-at-once/)


---

# シークレット

> 元ページ: `management/secret` ｜ 公式ページ: https://kuroco.app/ja/docs/management/secret/

シークレットではKurocoに登録されたシークレットの確認・追加・更新ができます。  
シークレットにはアクセストークンのような機密情報を保存するのに適しています。

## シークレット一覧
### 確認方法
[環境設定] -> [シークレット]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d597a29875656e7509403793f6f90abf.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b38d337c81d11f5e3e2d853d8d6f5509.png)

|項目   |説明  |
| :--- | :--- |
|名前|シークレットの名前を表示します。|
|Smarty|シークレットの値をSmartyで呼び出す際の変数を表示します。|
|更新日時|シークレットが最後に更新された日時を表示します。|

## シークレット編集
### 確認方法
シークレット一覧のページから編集したいシークレットの[名前]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a37422911d32eeb9e69ef7fee6dc02e8.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1bc3863ab9250bb1da3e8ba3904388d5.png)

|項目   |説明  |
| :--- | :--- |
|名前|シークレットの名前を入力します。<br/>1文字目は半角英字（a-z、A-Z）またはアンダースコア（`_`）、2文字目以降は半角英字（a-z、A-Z）・半角数字（0-9）・アンダースコア（`_`）が使用できます。<br/>ハイフン（`-`）や半角スペースなどの記号は使用できません。（例: `my-secret-token` は使用できません。`my_secret_token` のように指定します。）<br/>大文字・小文字を問わず、`kuroco` で始まる名前は使用できません。|
|値|シークレットの値を入力します。<br/>セキュリティのため値は表示されません。|

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6dee185a6a446ff54128a430f10641e3.png)

|項目   |説明  |
| :--- | :--- |
|更新する|シークレットの変更を反映します。|
|削除する|表示しているシークレットを削除します。|

## 関連ドキュメント
- [Instagram基本表示APIをkurocoから呼び出してInstagramのフィードを表示する](/ja/docs/tutorials/call-the-instagram-basic-display-api-from-kuroco/)
- [お問い合わせの受信通知をChatworkで送信する](/ja/docs/tutorials/send-chatwork-notification-after-a-form-has-been-submitted/)


---

# SendGrid

> 元ページ: `management/sendgrid` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sendgrid/

SendGridでは管理者メールの設定と、SendGridとの接続ができます。

## SendGridの確認方法
[チャネル] -> [メール] -> [SendGrid]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a9b92facaa18e63dfc55d7a529dcc8e.png)

## SendGridの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8cbad23000e74ff72b664ea125f1681b.png)

|項目   |説明  |
| :--- | :--- |
|管理者メール|管理者メールとして利用するメールアドレスを設定できます。<br/>メールアドレスは送信許可ドメイン・メールアドレスに登録されている必要があります。|
|SendGrid|[更新する]にチェックを入れると、SendGrid API Keyの入力と、送信許可ドメイン・メールアドレスの設定ができます。|
| Webhook URL|SendGridのEvent Webhookに設定するURLが表示されます。|
|更新する|[更新する]をクリックすると設定を反映します。|

:::caution
SendGridと契約・接続していてもKurocoのメール送信の料金は引き続き発生します。
:::

## 関連ドキュメント
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)


---

# サイト管理

> 元ページ: `management/site-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/site-settings/

サイト管理画面では、サイト全体の設定内容を確認・変更できます。

## サイト管理の確認方法
[環境設定] -> [サイト管理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cfe98777cabc7fcc2b02cb195f4e4c6e.png)

## サイト管理の項目説明
### 共通
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea0df803077529c954b28331f809836c.png)

|項目名|説明|
|:---|:---|
|エクセル向けCSVダウンロード|チェックを入れると、数字のみのデータにタブが付きます。結果として`001`のようなデータをエクセルで開いた時に頭の0が消えることを防ぎます。|
|ファイルマネージャで同名ファイルを検出する|チェックを入れると、ファイルマネージャで同名ファイルがアップロードされた場合に、[別名で保存][上書き][スキップ]のいずれかを選択するダイアログを表示します。|
|最大ファイルアップロードサイズ|アップロードするファイルサイズバイト数（MB単位）を設定します。|
|管理画面からの更新時に改行コードをLFに統一する|チェックを入れると、管理画面からの更新時に改行コードをLFに統一します。|

### フォーム
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7c3d18972d53e9d1e047a452a8a46ee.png)

|項目名|説明|
|:---|:---|
|投稿制限IPアドレス|コメントの投稿をIPアドレスで制限します。改行で区切ってIPアドレスを入力してください。<br/>IPアドレスは、単一のアドレスとして指定することも、CIDR表記を用いて指定することも可能です。|
|フォームドメイン拒否リスト|フォームに入力するメールアドレスのドメインに対して、拒否するメールアドレスを改行区切りで入力します。<br/>`#コメント`の形式でメモを追加できます。|

### 登録・招待設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4983fdc55a1023fc59a8fd8c0d9d4056.png)

|項目名|説明|
|:---|:---|
|退会完了通知|APIリクエストによる退会時に、退会完了した旨を会員にメールで通知します。（管理画面から削除した場合は通知されません。）|
|メンバー編集メール通知先メールアドレス|会員編集通知メールを送信するメールアドレスを入力してください。[メンバー詳細設定画面のメール通知](/ja/docs/management/new-member-settings/#メール通知)の「編集時送信アドレス」と連動しています。|
|メンバー登録ドメイン許可リスト|登録を許可するメールアドレスのドメインを改行区切りで入力します。<br/>`#コメント`の形式でメモを追加できます。実装例: `diverta.co.jp #ディバータ`|	
|メンバー登録ドメイン拒否リスト|登録を拒否するメールアドレスのドメインを改行区切りで入力します。<br/>`#コメント`の形式でメモを追加できます。実装例: `diverta.co.jp #ディバータ`|

### メンバー
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2eb6149de82d7403521d530bd0c2605c.png)

|項目名|説明|
|:---|:---|
|招待メール有効期間|招待メール有効期間(分)を入力します。デフォルトは720分となっています。|
|ECポイント機能|チェックを入れると、ECを利用していない場合でも、ポイント機能（メンバー編集画面のポイント情報タブなど）を利用できるようにします。ECを利用している場合、ポイント機能は本設定に関わらず利用できます。|

### ログイン
<a><img src="https://t.gyazo.com/teams/diverta/6acb76b394f83f8a3cbff09f28b1ab5b.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/f0237fb216de552adc14ed01dd603f9d.png" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目名|説明|
|:---|:---|
|ワンタイムパスワード|管理画面ログイン時のワンタイムパスワードの利用有無を選択します。設定可能な値は以下の通りです（利用しない、利用する、必須）。<br />この設定は管理画面へのログインでのみ有効です。API側はAPI毎に設定をしてください。|
|ワンタイムパスワードの方式|ワンタイムパスワードの送信方式を選択します。設定可能な値は以下の通りです（Authenticator(TOTP)、Email、SMS）。<br />この設定は管理画面へのログインでのみ有効です。API側はAPI毎に設定をしてください。|
|ログインロック機能を使う|5回ログインに失敗したら、アカウントをロックします。|
|初回ログイン時にパスワード変更をさせる|初回ログイン時、管理者がパスワードを変更した後にユーザーがログインしたタイミングで、パスワードの変更をさせる。|
|過去のパスワードは利用できない|設定された世代分の過去のパスワードの利用を禁止します。|
|パスワードは数字または記号が必須|ログインパスワードには数字または記号を1文字以上含める必要があります。|
|パスワードは数字と記号が必須|ログインパスワードには数字と記号をそれぞれ1文字以上含める必要があります。|
|パスワードの有効期限日数設定|パスワードの有効期限日数を入力します。|
|パスワード最大文字数|設定するパスワードの最大文字数を入力します。|
|パスワード最小文字数|設定するパスワードの最小文字数を入力します。|
|パスワード変更完了通知メールを送信する|パスワード変更完了時にメンバーにメールで通知をします。|
|パスワードリマインダメール有効期間|パスワードリマインダメール有効期間(分)を入力します。|
|パスワードのブラックリスト|[=login_id] ログインIDと同じものは禁止<br/>[=email] メールアドレスと同じものは禁止<br/>12345など改行区切りで入力してください。|
|パスキー|パスキーを2要素認証に使用するための設定です。設定可能な値は以下の通りです（利用しない、利用する、必須）。<br />利用しない: パスキーを第二要素として使用しないようにします。<br />利用する: メンバーが2要素認証としてパスキーを設定できるようにしますが、ログイン時に必須にはなりません。<br />必須: メンバーアカウントにパスキーの設定が必須になります。パスキーが設定されていない場合、次回ログイン時に自己登録を促す画面が表示されます。<br />この設定は管理画面へのログインでのみ有効です。API側はAPI毎に設定をしてください。|
|パスキーによるパスワードレスログイン|メールアドレスやユーザー名を入力せずに、パスキーのみでログインできるようになります。<br />この設定は管理画面へのログインでのみ有効です。API側はAPI毎に設定をしてください。<br />この設定は「パスキー」が「利用する」または「必須」の場合のみ有効です。|
|すべての2FA方式を強制的に使用する|必須に設定された二要素認証の方式が複数ある場合、通常はいずれか1つの方式で認証すればログインできます（どの方式を使うかはユーザーが選択できます）。<br />この設定を有効にすると、必須に設定されたすべての方式での認証が要求されます。|

### EC
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00ea6a2e8604e920cb20b5cacc696792.png)

|項目名|説明|
|:---|:---|
|有料会員期限切れ通知設定|有効期限が切れる何日前に通知するかを入力します。|

### コンテンツ
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c14456a8ebb80a3d6f17df4e937d032f.png)

|項目名|説明|
|:---|:---|
|「副言語の画像やファイルがない場合の主言語のファイル表示」を無効にする|チェックを入れると、副言語の画像やファイルがない場合に主言語のファイルを自動でレスポンスする動作が無効になります。|


[更新する]をクリックすると変更内容が反映されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7fb9c93a0fea5703a76c4ea65cbdfdb0.png)

## 関連ドキュメント
- [メンバー詳細設定](/ja/docs/management/new-member-settings/)
- [アカウント設定](/ja/docs/management/account/)
- [ログインロックについて教えてください。](/ja/docs/faq/what-causes-accounts-to-be-locked/)
- [パスワードの最大・最小文字数を変更できますか](/ja/docs/faq/can-i-change-the-password-character-limits/)
- [過去のパスワードを利用できないようにする設定はできますか？](/ja/docs/faq/can-i-disable-password-reuse/)


---

# VAddy

> 元ページ: `management/vaddy` ｜ 公式ページ: https://kuroco.app/ja/docs/management/vaddy/

ここではVAddyの申込と、連携機能のための設定を実施できます。

## VAddyの確認方法
[外部システム連携] -> [VAddy]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d677b533cad527c1f106cc57e71be939.png)

## VAddyの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3bed664ca45798674eb7a6a95ad50c31.png)

|項目   |説明  |
| :--- | :--- |
|VAddyの申し込みはこちらから|クリックすると、VAddyの申込ページにサービスコードが適用された状態で遷移します。|
|Server FQDN|VAddyのプロジェクトに登録するServer FQDNが表示されます。|
|User ID (VADDY_USER)|VAddyに登録したUser IDを入力します。|
|API Auth Key (VADDY_TOKEN)|VAddyのWebAPI設定の画面から取得したAPI Auth Key (VADDY_TOKEN)を入力します。|
|プロジェクトID|VAddyで登録したプロジェクトのプロジェクトIDを入力します。|
|Project number|VAddyで登録したプロジェクトのnumberを入力します。|
|認証ファイル|VAddyで取得したサーバー所有者確認用の認証ファイルのファイル名を入力します。<br/>htmlの中身ではなく、`vaddy-`から始まり、`.html`で終わるファイル名となります。|
|Crawl ID|VAddyで登録したクロールのCrawl IDを入力します。|
|更新する|クリックすると入力した内容を反映します。|

## 関連ドキュメント
- [VAddyと連携してAPIエンドポイントに対する自動診断を設定する。](/ja/docs/tutorials/integrating-with-vaddy/)


---

# Vimeo

> 元ページ: `management/vimeo` ｜ 公式ページ: https://kuroco.app/ja/docs/management/vimeo/

ここではVIMEOとの接続を実施できます。

## Vimeoの確認方法
[外部システム連携] -> [Vimeo]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4c80c6ca1be24e94f187fa32686ef04d.png)

## Vimeoの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b88c101cfcee6352cc743c95b740d7c7.png)

|項目   |説明  |
| :--- | :--- |
|Client identifier|Vimeo developer の My Appsで取得したClient Identifierを入力します。|
|Client secrets|Vimeo developer の My Appsで取得したClient Secretsを入力します。|
|Access token|Vimeo developer の My Appsで取得したAccess Tokenを入力します。|
|Add allow domains|許可するドメインを追加します。|
|更新する|クリックすると入力した内容を反映します。|

## 関連ドキュメント
- [Vimeoと連携して動画をアップロードする](/ja/docs/tutorials/how-to-connect-to-vimeo/)
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
