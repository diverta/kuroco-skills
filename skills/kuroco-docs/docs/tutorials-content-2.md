# Kurocoドキュメント: チュートリアル / コンテンツ管理（2/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 定期的に外部サイトのキャプチャをPDF化する（`how-to-use-generate-pdf`）
- 承認ワークフローを使用する（`how-to-use-workflow`）
- 検索機能を実装する（`implement-a-search-function`）
- WordPressのXMLファイルをKurocoへインポートする（`import-wordpress-xml-files-into-kuroco`）
- コンテンツにコメント機能を追加する（`integrate-activity-comment`）
- 事前に保存したHTMLをWysiwygエディタで呼び出す（`reuse-the-previously-saved-html-using-a-wysiwyg-editor`）
- コンテンツを公開したまま、指定の日時に更新する（`scheduling-updates-for-published-contents`）
- マスタ形式を使って動的に変化する選択項目を設定する（`setting-up-dynamic-options-using-master`）
- サブ項目(JSON)を使用して複雑な構造を持つコンテンツ項目を設定する（`setting-up-json-field`）
- WEBクローラーの設定方法（`setting-up-web-crawler`）
- コンテンツ一覧ページにページネーションを実装する（`splitting-the-contents-list-into-multiple-pages`）
- カテゴリ拡張設定を利用する（`using-category-ext-configuration`）
- Slackで定期的に確認をサポートするbotアプリ「KurocoWorkflow」のインストールと利用方法（`workflow-bot`）


---

# 定期的に外部サイトのキャプチャをPDF化する

> 元ページ: `tutorials/how-to-use-generate-pdf` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-generate-pdf/
> 概要: generate_pdfプラグインを利用することで、指定されたURLの画面をキャプチャし、PDFや画像形式で保存できます。今回は例として、1日1回、指定した外部サイトをキャプチャしてPDF化し、Kurocoに保存するバッチ処理を作成します。

`generate_pdf` プラグインを利用すると、指定されたURLの画面をキャプチャし、PDFや画像形式で保存できます。
カスタム処理やバッチ処理など、Smarty構文が記述可能な箇所から呼び出すことができます。

今回は例として、1日1回、指定した外部サイトをキャプチャしてPDF化し、Kurocoに保存するバッチ処理を作成します。

## 前提条件
本プラグインを利用する場合はFirebaseとの連携を設定している必要があります。  
Firebase連携については[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)をご確認ください。

## 外部サイトのキャプチャをPDF化する

### バッチ処理を作成する
Kuroco管理画面のサイドメニューの[オペレーション] -> [バッチ処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d2dd9049a23aa042744e95bf6cb395b.png)

バッチ一覧から[+追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/710fb9a80042dbf10ba73dd4b03f3387.png)

バッチ処理を作成します。今回は以下のように設定します。
- タイトル: 外部サイト日次キャプチャ取得
- 識別子: daily_capture
- バッチ: 毎日、00:00
- 処理: （以下の内容を記述してください）

```smarty
{assign var=date value=$smarty.now|date_format:'%Y%m%d'}
{assign var=path value='files/g/private/sample_'|cat:$date|cat:'.pdf'}
{generate_pdf url='https://www.diverta.co.jp' path=$path}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/113b251355c89f558359b049126038ab.jpg)

[追加する]をクリックし、設定を保存します。


### バッチ処理の確認
今回は毎日０時にバッチが実行されるように指定していますので、毎日0時にバッチが実行され、KurocoFilesにPDFが保存されます。
または、タイトル横に「すぐに実行する」ボタンがありますので、こちらをクリックするとバッチ処理が実行されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed410a2e4e56b479acdc3dbdec323d8e.png)

バッチ実行後、ファイルが作成されているか確認します。
Kuroco管理画面のサイドメニューの[ファイルマネージャー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f1356f9083771e69907eada083164cd5.png)

GCS(Private)にファイルが作成されていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57afcbc7b39ebe59719eb262de9c90c0.png)

:::tip
PDFが生成されるまでには数十秒〜数分、時間がかかる場合もあります。
:::

## 関連ドキュメント
`generate_pdf`の詳細ついては、[Smartyプラグイン -> generate_pdf](/ja/docs/reference/smarty-plugin/#generate_pdf) をご確認ください。


---

# 承認ワークフローを使用する

> 元ページ: `tutorials/how-to-use-workflow` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-workflow/
> 概要: 承認ワークフローを使用することで、記事の作成と公開を分担できます。それぞれの担当者が異なる場合や、公開前に記事の内容をチェックしたい場合などにご利用ください。

承認ワークフローを使用することで、記事の作成と公開を分担できます。  
それぞれの担当者が異なる場合や、公開前に記事の内容をチェックしたい場合などにご利用ください。

## 事前準備
事前準備として、以下を準備します。
- 編集者用、承認者用のアカウントそれぞれ1つ
- 承認ワークフローに載せるコンテンツ定義

### 1.メンバーの作成
[メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)を参考に、編集者と管理者のアカウントを1つずつ作成します。  
今回は、以下のように作成しました。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/22e903b699a51f5b7aa8fbe1dad1bdff.png)

### 2.コンテンツ定義の作成
[コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)を参考に、承認ワークフローに乗せるコンテンツ定義を作成します。  
今回は以下の通りシンプルなコンテンツ定義を作成しました。

|項目名|内容|
|:---|:---|
|名前|お知らせ（要承認）|
|本文の入力方法|テキストエリア|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2011f3f5890de86e7d9d3f1576eb3627.png)

## ワークフローを作成する

### 承認ワークフローの新規作成画面へアクセスする
`管理者`のアカウントでログインし、サイドメニューより[オペレーション] > [承認ワークフロー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa67e583c1933682b2a313fc3d8446eb.png)

画面右上の[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ccd6038d5f0de86adf387c663b380963.png)

### 基本設定
[基本設定]の必要項目を入力し、[追加する]をクリックします。  
今回は、以下のように入力しました。

|見出し|項目名|内容|
|:---|:---|:---|
||名前|承認ワークフロー|
||有効/無効|有効|
||メール通知 **※1**|通知する|
|| |承認者と申請者以外のメールアドレス|
||利用制限|選択なし|
|対象コンテンツ|コンテンツ|`お知らせ（要承認）`|
|メール設定| |申請が完了した際に配信されるメールの内容を入力します。<br/>ここでは以下の内容を入力します。<br/><code>{$smarty.const.SITE_TITLE}のサイトで承認依頼がありました。<br/>以下のリンクから確認してください。<br/>{$link}</code>|

:::note
※1 申請者と[フロー設定](#フロー設定)で指定した承認者に追加して通知メールを送信する設定になります。尚、メールアドレスが重複していた場合は「フロー設定」が優先されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/601c6eec8dc94020223377e92e1b6fff.jpg)

### フロー設定
追加後に自動的に遷移する[フロー設定]画面で、申請から公開までの承認の流れを設定します。
承認者としてのグループ、もしくはメンバーを選択し、[更新する]をクリックします。
今回は「管理者」1名のアカウントを承認者として指定します。

デフォルトでは2つの承認グループが表示されているので、1つの承認グループの[このグループを削除]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ccc0fd3462159187ddbc93a190426342.png)

以下のように承認者を設定します。

|項目名|内容|
|:---|:---|
|承認グループ名|承認者|
|承認者設定|メンバー|
||`管理者`|
|メール通知|通知する|


![Image from Gyazo](https://t.gyazo.com/teams/diverta/d4eed68d7b8fbf3138cc245c3c7498ac.png)

## コンテンツをワークフローに乗せ、申請する
[基本設定](#基本設定)の「対象コンテンツ」で選択されたコンテンツは、その編集画面の下部にワークフロー設定欄が表示されます。
- ワークフロー名
- 承認反映日時
を設定してから[追加する]をクリックすると、コンテンツをワークフローに乗せることができます。

### 対象のコンテンツ定義の新規作成画面にアクセスする
`編集者`のアカウントでログインします。  
サイドメニューより[コンテンツ]をクリックし、[基本設定](#基本設定)の「対象コンテンツ」で選択したコンテンツ定義をクリックします。  
今回は[お知らせ（要承認）]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/87c119aafc4fcfd1d91d2e28f95b4b17.png)

画面右上の[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4214b7390ea2d2708fe8a6a88d515c54.png)

### 「承認ワークフロー設定」を設定する
新規作成画面の下部に[承認ワークフロー設定]の項目があるので、以下のように設定します。

|項目名|内容|
|:---|:---|
|ワークフロー|`承認ワークフロー`|
|承認の反映日時|設定なし|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f74e91461c350bb7d39e8568338f911c.png)

[追加する]をクリックすると申請が完了します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c8cd4466f4e4da6ea92d5a4b52dd4a31.png)

## 申請中データの確認
申請データの承認/差し戻しが可能な詳細画面へは、以下の2通りの方法でアクセス可能です。
- 承認依頼メールのリンクからアクセスする。
- 承認者のアカウントで管理画面にログインしアクセスする。

今回は承認依頼メールのリンクからアクセスします。

### 承認依頼メールのリンクからアクセスする。
申請が完了すると、承認者宛（今回は`管理者`宛）に以下の承認依頼メールが配信されます。  
メールの内容は[基本設定](#基本設定)の[メール設定]で設定した内容です。  
リンクの部分をクリックすると、ログイン画面を経て詳細画面へ直接遷移します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/79039ca861993dc24f9f927622e39d68.png)

申請中データは、変更があった項目名がハイライト表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e5be80c78eda25ac587c5eeba4b5ffa.jpg)

## 申請データの承認
[承認]をクリックすると、記事の承認が完了します。  
なお、「承認ワークフロー」の部分で、全体のフローと現在の段階の確認ができます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/36e311b0671921bdf15ff5cd1b5f7d59.png)

:::note
スーパーユーザーの場合は、フロー設定で「承認者」として設定されていなくても承認が可能です。
:::

フローで設定した全ての承認が完了すると、記事が追加されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a5a2ec140b07f20ccb78865a30c1344.png)

## 承認完了メールの確認
申請者・承認者・[基本設定](#基本設定)の「メール通知」で設定したメールアドレス宛に以下の通り承認完了の通知メールが配信されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/65f00683a0d9e8a33cb36e15576effe7.png)

:::tip
承認完了・差し戻し通知のメールは[メッセージひな形](/ja/docs/management/email-template/)で編集可能です。
:::

## 関連ドキュメント
- [コンテンツを公開したまま、指定の日時に更新する](/ja/docs/tutorials/scheduling-updates-for-published-contents/)
- [管理画面マニュアル -承認ワークフロー](/ja/docs/management/workflow/)
- [リファレンス -メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)


---

# 検索機能を実装する

> 元ページ: `tutorials/implement-a-search-function` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implement-a-search-function/

Kurocoでサイト内検索を実装する方法として、下記2つの方法があります。

- filter機能を利用する
- 商用サービス(Algolia、Syncsearch等)を利用する

本チュートリアルでは、filter機能を利用したコンテンツ検索機能の実装方法を記載します。

## filter機能を利用して検索を実装する方法

APIのfilter機能を利用することで、コンテンツの条件検索やキーワード検索を実装できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/24417b57dcf673d8b36aaccf6263a07a.png)
検索機能を実装するにあたって、まずはfilter機能の概要を説明します。

filterは、APIエンドポイントの取得対象データを絞り込むための機能です。エンドポイントの「filter」パラメータに次のようなクエリを指定すると、条件に合致するデータのみを取得できます。

```sql
// topics_idが1のコンテンツを指定
topics_id = 1
```

完全一致/部分一致、数値や日付の比較、AND/ORなど、条件を柔軟に指定できるため、複雑な検索の実現も可能です。

```sql
// タイトルが「WORD」を含むコンテンツ、または2021-01-01 ~ 2021-12-31の間に追加されたコンテンツを指定
subject contains "WORD" OR (inst_ymdhi >= "2021-01-01" AND inst_ymdhi <= "2021-12-31")
```

filterパラメータは下記の2箇所から指定でき、それぞれ役割が異なります。  

| 指定箇所 | 説明 |
| :--- | :--- |
| エンドポイント設定 | Kurocoの管理画面(API画面)で設定するものです。<br/>常に付与される固定の検索条件を設定します。<br/>例えば、ここで `inst_ymdhi >=:relatively "-1 year"` を設定した場合、現在日時から1年以内に追加されたコンテンツを常に取得します。 |
| GETパラメータ | フロントエンドからAPIに動的に指定するものです。<br/>エンドポイント設定でもfilterを設定済みの場合は、以下のように両方のクエリをAND条件で結合した状態で検索を行い、結果を返します。<br/>`filterクエリ(エンドポイント設定) AND filterクエリ(GETパラメータ)` |

今回の検索機能のように、ユーザーの入力内容に応じて取得結果を変えたい場合は、GETパラメータでfilterクエリを指定します。  
固定の検索条件を追加で指定したい場合は、必要に応じてエンドポイント設定にもクエリを入力してください。

:::tip
filterは、対象のAPIモデルが機能をサポートしている場合のみ利用できます。エンドポイントの設定画面、またはSwagger UIの画面を確認し、対象のエンドポイントに「filter」パラメータが存在するかを確認してください。
:::

それではfilterを利用した検索の実装方法を説明していきます。今回は下記２パターンでの実装方法を説明します。

- 条件検索
- キーワード検索

## 事前準備
### APIを追加する 
**API**  
 
下記のAPIを作成します。  

| 項目 | 値 |
| :--- | :--- |
|タイトル|検索機能のAPI|
|版|1.0|
|説明|検索機能のAPI|
|並び順|0|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7913cec88ccda1689f8f989e96ad3430.png)

追加するをクリックすると、追加したAPIに遷移しますので、続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ec0edb46f85056afef4eb2d1d6d92d5.png)

[Cookie]を選択して[保存する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b648ab792ff01fac76b20029c5b348f7.png)
**CORS**  

次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc0b96d7362a4ec02e78b4ce7f31e8c3.png)
CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。
- `http://localhost:3000`
- フロントエンドドメイン

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。
- GET  
- POST
- OPTIONS

![Image from Gyazo](https://t.gyazo.com/teams/diverta/daf16e82023ca7539a19f66dfc631837.png)
設定できたら[保存する]をクリックし、CORSの設定が完了です。


## 条件検索の実装

ここからは先ほどの機能概要を踏まえて、条件検索機能を実装する方法を説明していきます。


### 1. コンテンツ定義とエンドポイントを作成する

下記のコンテンツ定義とエンドポイントを作成します。

**コンテンツ定義**

コンテンツ定義は下記の設定で作成します。

- グループ名：Search
- グループID：9(自動採番されます)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1892ff874df3f8a2cb8a673e9949aa74.png)
また、拡張項目を使用し下記フィールド追加しています。

| ID | 項目名 | 設定項目 | オプション |
| :--- | :--- | :--- | :--- |
| 1 | Text | テキスト | - |
| 2 | Select | 単一選択 | `01::option1`<br/>`02::option2`<br/>`03::option3` |
| 3 | Checkbox | 複数選択可 | `01::option1`<br/>`02::option2`<br/>`03::option3` |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/18b7da5ee25a10bb3fca67dd81769420.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/21f1049bfa492ff586480d511d625bfc.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/071cf154c71fd47817cc4400f7516ce5.jpg)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/30b10f9afa4dec40707a405f5ae2f98d.jpg)

また、作成したコンテンツ定義「Search」にて、下記のようにテストデータを3件登録しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f7de3160340288135c5f2d20f96a3a6.png)

**エンドポイント**

エンドポイントは下記の設定で作成します。

| 項目 | 値 |
| :--- | :--- |
| パス | content |
| カテゴリー | コンテンツ |
| モデル | Topics (v1) |
| オペレーション | list |
| topics_group_id | 9 |

:::note
topics_group_idには、ご自身のコンテンツ定義のIDを記入してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1f6fc9fd08ac9b3ceec34670d1e23bca.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/326125ab7d7470b091c0238b45746f59.png)
### 2. エンドポイントを設定する

[API] -> API LIST画面から先ほど作成したエンドポイントを選択し、「更新」 をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ecc790ba0841344ca3c53d19cac02dc5.png)
次に、`filter_request_allow_list`の設定項目に移動し、検索対象の項目名を指定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b9c10f1f029bb7fd9ab67c62409c1dd7.png)
`filter_request_allow_list`は、GETパラメータでの検索を許可する項目を指定するための設定です。

初期状態では、GETパラメータによるfilterクエリの指定は無効化されています。ここで個別に項目名を指定することで初めて、対象項目への検索が有効になります。

今回は下記を追加します。

- subject
- inst_ymdhi
- ext_1
- ext_2
- ext_3

:::tip
Kurocoをお申込みいただいたタイミングによっては、各拡張項目が`ext_1`ではなく、`ext_col_01`となる場合があります。  
うまくいかない場合は Swagger UIでレスポンスをご確認ください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22474a8fc43d10ad67a09245a7fd735b.png)
:::caution
ここで `:ALL` を指定した場合、全ての項目に対する検索が許可されます。便利な機能ですが、これは時にAPIのセキュリティを弱める原因にもなり得ます。(例えば、特定の項目をレスポンスデータに返さないよう設定している場合、その項目も含めて検索対象となります)  
そのため、基本的には対象の項目を個別に設定することを推奨します。  
`:ALL`を設定する場合は、対象のエンドポイントが返すデータの内容を確認し、本当に問題がないかどうかを確認してください。
:::

設定が完了したら、[更新] ボタンをクリックし保存してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6452f6df8c1a2a76dfea8e45d09ef09e.png)
### 3. エンドポイントの動作を確認する
API LIST画面より「Swagger UI」をクリックし、Swagger UI画面に移動します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/65335084e3ee37ba1d11cd2571727383.png)
設定したエンドポイントをクリックし、動作確認を行います。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e4400535b5349ef6f6ec8664e4e7c21.png)
[Try it out] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dd798393ad89851d728c91b9cfe0bbfc.png)
「filter」パラメータに検索条件となるクエリを入力します。

#### タイトル検索

今回は「Test」という名前の記事を作っている前提で、「`subject contains "Test"`」と記入し、この記事が取得できることを確認します。

:::tip
記述可能なクエリの形式については、下記ドキュメントを参照してください。  
[リファレンス：検索機能の使い方](/ja/docs/reference/filter-query/)
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/dbf29b337e1760057c890eeec817d580.png)
入力が完了したら [Execute] ボタンをクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f7cc82bda94075b575482267bb9a1dfe.png)
結果が表示されるので、期待通りに検索が行えているかを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b50d87637dc331d05e427de351c771ed.png)

#### 単一選択などの選択形式検索
「`ext_2 = "01"`」と記入し、「option1」が選択されたコンテンツを取得できることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/227164eef8ea8ff26a7db61c30d6e881.png)

入力が完了したら [Execute] ボタンをクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f7cc82bda94075b575482267bb9a1dfe.png)
結果が表示されるので、期待通りに検索が行えているかを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8bca6c48782efda20aed97b6062dd60c.png)

:::info
単一選択などの選択形式のkeyは文字列で保存されます。  
フィルタをかける際は明示的に `" "` で囲ってください。  

例：単一選択などの選択形式を以下のように登録していた場合でも、`ext_2 = 1`ではなく、`ext_2 = "1"`でフィルタをかける。
```
1::option1
2::option2
3::option3
```
:::


以上でエンドポイントの動作が確認できました。

### 4. 検索機能を実装する

では、先ほど設定したエンドポイントを利用して、実際に条件検索画面を実装していきましょう。

今回はNuxt.jsを使い、以下のようにシンプルな検索フォーム・検索結果テーブルを表示するコンポーネントを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/165168121619d7fe051858bf27b51ad7.png)
まずは下記のコンポーネントを、`pages/search/index.vue`として用意します。  

```markup
<template>
  <div>
    <div class="search-form">
      <p>
        <label for="subject">Title</label>
        <input v-model="searchInput.subject" type="text">
      </p>
      <p>
        <label for="inst_ymdhi">Created at</label>
        <input v-model="searchInput.inst_ymdhi.from" type="date"> 
        ~
        <input v-model="searchInput.inst_ymdhi.to" type="date"> 
      </p>
      <p>
        <label for="ext_1">Text</label>
        <input v-model="searchInput.ext_1" type="text">
      </p>
      <p>
        <label for="ext_2">Select</label>
        <select v-model="searchInput.ext_2">
          <option value="">Not selected</option>
          <option value="01">option1</option>
          <option value="02">option2</option>
          <option value="03">option3</option>
        </select>
      </p>
      <p>
        <label for="ext_3">Checkbox</label>
        <input v-model="searchInput.ext_3" type="checkbox" value="01">option1
        <input v-model="searchInput.ext_3" type="checkbox" value="02">option2
        <input v-model="searchInput.ext_3" type="checkbox" value="03">option3
      </p>  
      <button type="button">Search</button>
    </div>
    <div v-if="Object.keys(searchResult).length > 0" class="search-result">
      <template v-if="(searchResult.errors || []).length === 0">
        <table>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Created at</th>
            <th>Text</th>
            <th>Select</th>
            <th>Checkbox</th>
          </tr>
          <tr v-for="content in searchResult.list" :key="content.topics_id">
            <td>{{ content.topics_id }}</td>
            <td>{{ content.subject }}</td>
            <td>{{ content.inst_ymdhi }}</td>
            <td>{{ content.ext_1 }}</td>
            <td>{{ content.ext_2 }}</td>
            <td>{{ content.ext_3 }}</td>
          </tr>
        </table>
      </template>
      <template v-else>
        {{ searchResult.errors }}
      </template>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchInput: {
        subject: '',
        inst_ymdhi: {
          from: '',
          to: '',
        },
        ext_1: '',
        ext_2: '',
        ext_3: []
      },
      searchResult: {},
    }
  },
  mounted() {},
  methods: {}
}
</script>

<style scoped>
.search-form {
  border: 1px solid;
  padding: 10px;
}
.search-form label {
  display: block;
  float: left;
  width: 100px;
}
.search-result {
  width: 100%;
  margin-top: 20px;
}
.search-result table, th, td {
  border: solid 1px;
  border-collapse: collapse;
}
.search-result th, td {
  padding: 5px;
}
.search-result table {
  width: 100%;
}
</style>
```

`.search-form`は検索フォーム、`.search-result`は検索結果を表示するための要素です。

`data`オブジェクトの`searchInput`にはユーザーの入力内容を、`searchResult`には検索結果のレスポンスを格納します。
```js
data() {
  return {
    // ユーザーの入力内容 (.search-form)
    searchInput: {
      subject: '',
      inst_ymdhi: {
        from: '',
        to: '',
      },
      ext_1: '',
      ext_2: '',
      ext_3: []
    },
    // 検索結果のレスポンス (.search-result)
    searchResult: {},
  }
},
```

`npm run dev`コマンドを実行してローカル環境を立ち上げ、`http://localhost:3000/search` にアクセスすると、下記の画面が表示されます。  
画面上には以下の入力フォームが表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/be3a157986add6613783ec5466e2cad6.png)
しかしながら、まだエンドポイントの呼び出し処理を実装していないため「Search」ボタンをクリックしても何も起こらない状態です。ここからは`methods`を定義し、実際にエンドポイントを呼び出して検索処理を実装していきます。

まずは、`search`メソッドを作成します。ここには、「1. エンドポイントを設定する」で設定したエンドポイントを呼び出す処理を記述します。

filterクエリの生成処理については、`buildFilterQuery`メソッドへ移譲するようにしています。(このメソッドの具体的な処理については、後ほど記述します。)

```js
methods: {
  // エンドポイントへのリクエストを行い、取得結果をsearchResultに格納
  async search() {
    let searchResult;
    try {
      // 自分の環境で設定したエンドポイントのURLに置き換えてください
      const response = await this.$axios.get("/rcms-api/14/content", {
        params: {
          filter: this.buildFilterQuery()
        }
      })
      searchResult = response?.data || {};
    } catch(errorResponse) {
      searchResult = { errors: errorResponse?.data?.errors || ['Unexpected error'] };
    }
    this.searchResult = searchResult;
  },
  // filterクエリの生成
  buildFilterQuery() {
    return '';
  }
}
```

:::caution
`/rcms-api/14/content`、の箇所は、Kuroco管理画面に記載のパスをご記入ください。
:::

作成が完了したら、`search`メソッドを[Search] ボタンのクリックイベントとして定義します。
[Search] ボタンは `.search-form` 要素の最下部に存在します。

```html
<!--
    <button type="button">Search</button> <= @click="search" を追記
-->
<button type="button" @click="search">Search</button>
```

続いては、`buildFilterQuery`の具体的な処理を記述していきます。data属性 `searchInput` に格納されている値を、filterクエリに変換します。

今回は、以下のような条件でクエリを生成します。  

- 日付: 範囲指定
- テキスト: 部分一致
- 単一選択(select): 完全一致
- 複数選択可(checkbox): 部分一致

値が未入力の場合は、対象の項目は検索条件として指定しないものとします。

:::tip
生成すべきクエリはinputの形式、対象の項目、機能要件などによって異なります。必要に応じて適した処理を実装してください。
:::

```js
methods: {
  // ...
  buildFilterQuery() {
    const filterQuery = Object.entries(this.searchInput).reduce((queries, [col, value]) => {
      switch (col) {
        // 日付: 範囲指定
        case 'inst_ymdhi':
          if (value.from !== '') {
            queries.push(`${col} >= "${value.from}"`);
          }
          if (value.to !== '') {
            queries.push(`${col} <= "${value.to}"`);
          }
          break;
        // テキスト: 部分一致
        case 'subject':
        case 'ext_1':
          if (value !== '') {
            queries.push(`${col} contains "${value}"`);
          }
          break;
        // 単一選択(select): 完全一致
        case 'ext_2':
          if (value !== '') {
            queries.push(`${col} = "${value}"`);
          }
          break;
        // 複数選択可: 部分一致
        case 'ext_3':
          if (value.length > 0) {
            queries.push('(' + value.map(v => `${col} contains "${v}"`).join(' OR ') + ')');
          }
          break;
        default:
          break;
      }
      return queries;
    }, []).join(' AND ');

    return filterQuery;
  }
}
```

最後に、`mounted`に以下のコードを追加し、初期遷移時には条件指定のないコンテンツ一覧を表示するようにします。

```js
mounted() {
  this.search();
},
```

以上で、条件検索コンポーネントの実装は完了です。
localhostにアクセスしてフォームを操作し、期待通りに結果を取得できているかを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3619f9a45d30494564d68d13c059dd2c.png)
以上で条件検索の実装を終わります。

## キーワード検索の実装

続いては、キーワード検索を実装する方法を説明します。


キーワード検索を実装するにあたって、条件検索の例を踏まえると、どのような実装方法が考えられるでしょうか。まずは以下のように、対象のカラムに対しての部分一致検索クエリを `OR` で連結する方法も考えられます。

```sql
subject contains "KEYWORD" OR ext_1 contains "KEYWORD"
```

確かにこの方法を利用すれば、キーワード検索の機能自体は実現が可能です。ですが、検索対象のカラムが増えた場合に少し問題があります。
以下のように、非常に冗長で読みづらいクエリを渡す必要があるためです。

```sql
subject contains "KEYWORD" OR ext_1 contains "KEYWORD" OR ext_4 contains "KEYWORD" OR ext_5 contains "KEYWORD" OR ext_6 contains "KEYWORD" OR ...
```

そのためfilter機能では次のように、よりシンプルなクエリでキーワード検索を実装できる仕組みを用意しています。

```sql
search_keyword contains "KEYWORD"
```

今回はこの `search_keyword` 機能を利用して、キーワード検索を実装していきます。

:::tip
Kurocoを申し込んだタイミングによって`search_keyword`ではなく`keyword`で動作するサイトがあります。  
うまく動かない場合は`keyword`でもお試しください。  
:::

### 1. コンテンツ定義とエンドポイントを作成する
今回は、下記のコンテンツ定義とエンドポイントを利用します。

**コンテンツ定義**

コンテンツ定義は[条件検索の実装](#条件検索の実装)で定義した「Search」を利用します。

**エンドポイント**

エンドポイントは下記の設定で作成します。

| 項目 | 値 |
| :--- | :--- |
| パス | content_keyword |
| カテゴリー | コンテンツ |
| モデル | Topics (v1) |
| オペレーション | list |
| topics_group_id | 9 |

:::caution
topics_group_idには、ご自身のコンテンツ定義のIDを記入してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee42b3ebba7ec52b9fa5c91ba2203740.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/244239d09424d93e96e5685f76b5858f.png)
### 2. エンドポイントを設定する

[API LIST](/ja/docs/management/api-list/)画面から、検索機能を実装したいエンドポイントを選択し、[更新] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae28b562fb571aa1ad9d0feef6dd2c31.png)
次に、`filter_request_allow_list`の設定項目に移動し、検索対象の項目名を指定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b9c10f1f029bb7fd9ab67c62409c1dd7.png)
キーワード検索の許可リストを設定する場合には、以下のフォーマットを利用できます。

| 形式 | 説明 |
| :--- | :--- |
| search_keyword | 全項目に対するキーワード検索を許可します。<br/>例) `search_keyword` |
| search_keyword:[項目名1,項目名2,...] | 対象の項目名をカンマ区切りで入力し、指定した項目名に対するキーワード検索を許可します。<br/>例) `search_keyword:[subject]`<br/>例) `search_keyword:[ext_1,ext_2]` |

:::tip
`:ALL` を指定した場合は他の項目と同様に、`search_keyword`も対象の項目として含まれます。
:::

今回は以下のように、`search_keyword:[subject,ext_1]`を指定し、タイトルとテキスト項目をキーワード検索の対象とします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c15d7ffe19fddbcb3e838f704a96af8.png)


設定が完了したら、[更新] ボタンをクリックし保存してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aee58b15706ed901f05a4d4d25a06ec9.png)
### 3. エンドポイントの動作を確認する

API LIST画面より「Swagger UI」をクリックし、Swagger UI画面に移動します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/65335084e3ee37ba1d11cd2571727383.png)
設定したエンドポイントをクリックし、動作確認を行います。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3154b61f77a9a07e161b93fe8f6e2f67.png)
[Try it out] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4f24d175a5a4678564067fe6f895c1f.png)

「filter」パラメータにクエリを入力します。部分一致で検索させるため、 `contains` を指定します。
今回は「`search_keyword contains "1"`」と記入します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0616abee307b862b4dbc38effb918ee.png)

入力が完了したら  [Execute] ボタンをクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f7cc82bda94075b575482267bb9a1dfe.png)
結果が表示されるので、期待通りに検索が行えているかを確認してください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f0bde08b70b315da55dfcdbbd1ebb4a2.png)
以上でエンドポイントの動作が確認できました。

### 4. 検索機能を実装する

では、先ほど設定したエンドポイントを利用して、実際にキーワード検索画面を実装していきましょう。

条件検索と同様に、今回もNuxt.jsを使って、以下のようなコンポーネントを作成します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a479bc078ba86518dfed65c8d0f98114.png)
まずは下記のコンポーネントを、`pages/search_keyword/index.vue`として用意します。

```markup
<template>
  <div>
    <div class="search-form">
      <p>
        <label for="keyword">Keyword</label>
        <input v-model="searchInput.search_keyword" type="text">
      </p>
      <button type="button" @click="search">Search</button>
    </div>
    <div v-if="Object.keys(searchResult).length > 0" class="search-result">
      <template v-if="(searchResult.errors || []).length === 0">
        <table>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Created at</th>
            <th>Text</th>
            <th>Select</th>
            <th>Checkbox</th>
          </tr>
          <tr v-for="content in searchResult.list" :key="content.topics_id">
            <td>{{ content.topics_id }}</td>
            <td>{{ content.subject }}</td>
            <td>{{ content.inst_ymdhi }}</td>
            <td>{{ content.ext_1 }}</td>
            <td>{{ content.ext_2 }}</td>
            <td>{{ content.ext_3 }}</td>
          </tr>
        </table>
      </template>
      <template v-else>
        {{ searchResult.errors }}
      </template>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchInput: {
        search_keyword: '',
      },
      searchResult: {},
    }
  },
  mounted() {
    this.search();
  },
  methods: {
  async search() {
      let searchResult;
      try {
        // 自分の環境で設定したエンドポイントのURLに置き換えてください
        const response = await this.$axios.get("/rcms-api/5/content_keyword", {
          params: {
            filter: this.buildFilterQuery()
          }
        })
        searchResult = response?.data || {};
      } catch(errorResponse) {
        searchResult = { errors: errorResponse?.data?.errors || ['Unexpected error'] };
      }
      this.searchResult = searchResult;
    },
    // filterクエリの生成
    buildFilterQuery() {
      return '';
    }
  }
}
</script>

<style scoped>
.search-form {
  border: 1px solid;
  padding: 10px;
}
.search-form label {
  display: block;
  float: left;
  width: 100px;
}
.search-result {
  width: 100%;
  margin-top: 20px;
}
.search-result table, th, td {
  border: solid 1px;
  border-collapse: collapse;
}
.search-result th, td {
  padding: 5px;
}
.search-result table {
  width: 100%;
}
</style>
```

:::caution
`/rcms-api/5/content_keyword`、の箇所は、Kuroco管理画面に記載のパスをご記入ください。
:::

`npm run dev`コマンドを実行してローカル環境を立ち上げ、`http://localhost:3000/search_keyword` にアクセスすると、下記の画面が表示されます。  
画面上には以下の入力フォームが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a5c0f3b4dd53bc38ba0c68872e17904e.png)
下記を除いて、コンポーネントの属性定義は条件検索のものと同様です。
- テンプレートの`.search-form`要素
- `data`オブジェクトの`searchInput`プロパティ
- `buildFilterQuery`メソッド

`.search-form`要素には、キーワードの入力フォームのみを定義しています。  
入力された値は、`searchInput.search_keyword`に格納します。

```html
<div class="search-form">
    <p>
    <label for="keyword">Keyword</label>
    <input v-model="searchInput.search_keyword" type="text">
    </p>
    <button type="button" @click="search">Search</button>
</div>
```

```js
data() {
  return {
    searchInput: {
      search_keyword: '',
    },
    searchResult: {},
  }
},
```

最後にキーワード検索機能を実装すれば完成です。
`buildFilterQuery`メソッドを編集し、キーワード検索クエリの生成処理を記述します。

```js
methods: {
  // ...
  buildFilterQuery() {
    const filterQuery = Object.entries(this.searchInput).reduce((queries, [col, value]) => {
      switch (col) {
        case 'search_keyword':
          if (value !== '') {
            queries.push(`${col} contains "${value}"`);
          }
          break;
        default:
          break;
      }
      return queries;
    }, []).join(' AND ');
    return filterQuery;
  }
}
```

以上で、キーワード検索コンポーネントの実装は完了です。

localhostにアクセスしてフォームを操作し、期待通りに結果を取得できているかを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e4cf71a1d1a60c48912ec05cfaa39aab.png)
以上でキーワード検索の実装を終わります。

## 参考：複数のコンテンツ定義をまたぐ検索を実装する
複数のコンテンツをまたいで検索する場合は、それぞれのコンテンツ定義で以下が同一になっている必要があります。

- 項目設定の種類
- コンテンツ項目のSlug
- コンテンツ項目のID  
  (項目を空で追加すると加算されていくので、同一になるよう調整してください。)

## 参考：商用サービスを利用して検索を実装する
本チュートリアルでは具体的な説明方法は割愛しますが、数万レコード以上や高速な大量のデータの検索が必要な場合には外部サービスを利用されるという選択肢もございます。特に利用制限等はございませんので、下記も参考にしてみてください。

- [Algolia](https://www.algolia.com/)
- [Programmable Search Engine(Google)](https://programmablesearchengine.google.com/about/)
- [Syncsearch](https://www.syncsearch.jp/)
- [Marsflag](https://www.marsflag.com/ja/)

## 関連ドキュメント
- [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
- [Kurocoのキーワード検索の種類](/ja/docs/reference/keyword-search-types/)
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)
- [あいまい検索用のベクトルテンプレートを用意する](/ja/docs/tutorials/how-to-implement-vector-search/)
- [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)
- [サイト内全文検索機能は実装できますか？](/ja/docs/faq/can-i-create-a-search-function/)


---

# WordPressのXMLファイルをKurocoへインポートする

> 元ページ: `tutorials/import-wordpress-xml-files-into-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/import-wordpress-xml-files-into-kuroco/
> 概要: WordPressでエクスポートしたXMLデータ及びメディアファイルをKurocoへインポートできます。

## 概要
WordPressでエクスポートしたXMLデータ及びメディアファイルをKurocoへインポートできます。  

### 学べること
以下の手順でWordPressの投稿データをインポートします。
- [WordPressで投稿データをエクスポートする](#wordpressで投稿データをエクスポートする)
- [インポート先のコンテンツ定義を準備する](#インポート先のコンテンツ定義を準備する)
- [WordPressインポーターでXMLファイルをインポートする](#wordpressインポーターでxmlファイルをインポートする)
- [インポートされたデータの確認](#インポートされたデータの確認)

### 前提条件
- Wordpressで作成された以下の4投稿をKurocoにインポートします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a9e79a18ec4ce825996da649ef268f6.png)

<!--
- 各投稿には1つずつカテゴリが設定されていることととします。
- WordPressに登録された以下のカテゴリ設定をKurocoにインポートします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/96ca1bb8158d525ceb63995e4504122e.png)

- Wordpressに登録された以下のメディアファイルをKurocoにインポートします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/51a89db6f5ee6d8c973423462bd0740c.png)

:::caution
WordPress.org(サーバーインストール型) の場合は画像パスがKurocoのインポート仕様と異なる場合があります。  
メディアファイルのディレクトリを調整してZIPファイルでファイルマネージャーにアップロード/解凍するか、XMLファイルの画像パスを調整して対応ください。

WordPress.org：`/wp-content/uploads/YYYY/MM/ファイル名`  
WordPress.com：`/YYYY/MM/ファイル名`
:::
-->

:::note
現在、WordPressメディアTARファイルのインポートは動作しません。  
ファイルの登録をするには、エクスポートしたメディアファイルをZIP形式に圧縮してKurocoFilesにアップロード・解凍してください。  
:::

## WordPressで投稿データをエクスポートする
まずは[WordPressのマニュアル](https://wordpress.com/ja/support/export/)を参考に、投稿データをエクスポートします。

WordPress管理画面のサイドメニューから[ツール]->[エクスポート]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/eed680d6ad75ac70f974fb0bbb03b75a.jpg)

「コンテンツをエクスポート」の[すべてエクスポート]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0aa76e514fb5ea117b12f56596e46fe.png)

ダウンロードリンクが作成されるので[ダウンロード]をクリックして、コンテンツデータのXMLをダウンロードします。  
ZIP圧縮されているので、ダウンロード後に解凍しておきます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ab248834fede44a98ebee3e46806c73.png)

<!--
続いて、メディライブラリのエクスポートの[ダウンロード]をクリックして、メディアライブラリのTARファイルをダウンロードします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd44498870f51377da6877b9df0b3453.png)
-->

以上で、WordPress側のデータエクスポートは完了です。

## インポート先のコンテンツ定義を準備する
続いてKuroco側の設定をしていきます。
まずはWordPressのデータをインポートするコンテンツ定義を作成します。  

コンテンツ定義一覧から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6fd1b45a0a82b01bede7862492445ed3.png)

以下の設定をして、[追加する]をクリックします。  

|項目|設定|
|:--|:--|
|全般-名前|任意の名前を入力|
|項目設定-日付/並び順|日付を使う|
|項目設定-ext_1|WYSIWYG|
|その他の設定|デフォルト|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8b983d963bb3849e349c766d9d20b0dd.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/92d5de2f705d61fe405a3dc2526dc7fe.png)

## WordPressインポーターでXMLファイルをインポートする
先ほど作成したコンテンツ定義にWordPressの投稿データをインポートしてコンテンツを作成します。  

[外部システム連携]->[WordPress]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/835f5d160c7161534e2b81ee2729209e.png)

WordPressインポーターが表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/68bdafe1c7eecf23b70a4c1bb6530222.png)

以下のように設定して[入力チェックする]をクリックします。  

|項目|設定|
|:--|:--|
|WordPress XMLファイル|WordPressからエクスポートした`.xml`ファイルを選択します。|
|対象コンテンツ|先ほど作成したコンテンツ定義(WordPress Import)を選択します。|
|ステータス|公開にする|
|値がない場合の動作|無視する|

<!--|WordPressメディアTARファイル|WordPressからエクスポートした`.tar`ファイルを選択します。|-->

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4190774631d7f3bd18a27c569aed4d17.png)

入力チェックがされますので、以下のように、インポートするPost typeと、カテゴリ、項目を設定します。

|項目|設定|
|:--|:--|
|Post typeを変換する|XMLデータの中からどのPost typeのデータをインポートするか選択します。<br/>`post`がWordPressの`投稿`に該当するデータになるので、ここではpostを選択します。|
|カテゴリを変換する|インポートしたデータが所属するカテゴリを選択します。<br/>任意のカテゴリを選択して構いません。|
|内容を変換する|インポートしたデータが登録される項目を選択します。<br/>ここでは先ほど作成したWYSIWYGの項目を選択します。|
|Slug|XMLからSlugも含めてインポートする場合にチェックを入れます。<br/>ここでは無効にしておきます。|
|タグを変換する|インポートしたデータにタグが含まれる場合、タグを変換するかどうかを選択します。<br/>ここでは無効にしておきます。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f7d16d5eb7532c61b986bdc5ebbae02a.jpg)

:::note
[内容を変換する]の項目でインポートした内容を保存するコンテンツ項目を指定します。  
現在はコンテンツ(デフォルトのcontents項目)へのインポートはサポートされていませんので、事前に設定した追加項目にインポートしてください。
:::

[更新する]をクリックすると、インポートの処理がバッチ処理に追加され、実行されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c147f2000f232a13d25fa1ef1033bf4b.png)

## インポートされたデータの確認

WordPress Importのコンテンツ一覧を確認すると、
WordPressの投稿データがインポートされていることが分かります。 

- [コンテンツ一覧](/ja/docs/management/content-structure-topics/)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0af6c9d9cf67ce6b6d5a113637296f4c.png)

<!--
- [コンテンツカテゴリ一覧](/ja/docs/management/content-structure-topics-category/)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ba7c1148d013e4c94d582517b79c1920.png)

- [ファイルマネージャー](/ja/docs/management/file-manager/)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8024d8f2e2df5f3b904194afb9372eae.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/119eda8e7bdf33c813bbc5d1b45a1bc6.png)

-->

## 関連ドキュメント
- [WordPress](/ja/docs/management/wordpress)


---

# コンテンツにコメント機能を追加する

> 元ページ: `tutorials/integrate-activity-comment` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrate-activity-comment/
> 概要: Kurocoを利用したプロジェクトで、アクティビティ:コメント機能の実装方法を紹介します。本チュートリアルではフロントエンドのコードとして、Nuxt.jsを紹介します。

Kurocoを利用したプロジェクトで、アクティビティ:コメント機能の実装方法を紹介します。  
本チュートリアルではフロントエンドのコードとして、Nuxt.jsを紹介します。  

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## 事前準備
### Nuxt.jsプロジェクトの作成について
このページは、KurocoとNuxt.jsでのプロジェクトが構築済み、
かつ既に何らかの記事が閲覧できること、また`profile`エンドポイントが有効であることを前提としています。  
まだNuxt.jsプロジェクトを構築していない場合、[チュートリアル ->KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)を参照してください。  
また`profile`などは[チュートリアル ->KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)を参考にしてください。
今回はcookieによるログイン制御を前提とします。

作成済みの「お知らせ詳細」のエンドポイントをコピー、未ログインメンバーによるコメントの許可設定をした後、お知らせ詳細とそれに紐づくコメントのフォームを作成します。

### APIの作成
未承認ユーザーからの操作を許可するために、新しくAPIを作成します。  
Kuroco管理画面のAPIより「追加」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/16730cd0c84c75934d48196e0265c5d6.png)
API作成画面が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9757238971ca5ead28886be1d43bf9c6.png)

下記入力し「追加する」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a1a5446771ba224317a050f552e1a6ac.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Comment Test|
|版|1.0|
|説明|コメント機能の確認用API|

### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a433b3a87d117c8a46a3a97cab2f73b.png)
CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。  
- http://localhost:3000

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。  
- GET
- POST
- OPTIONS

設定できたら[保存する]をクリックし、CORSの設定が完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc12583c6133922cf88275baf0a7b857.png)
## ログイン不要でコメント機能の動作を確認する
### アクティビティ定義の作成
未承認ユーザーからのコメント操作を許可するために、アクティビティ定義を編集します。  
[アクティビティ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b73cbe0b67685431b15982c5100fcba2.png)
[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9454d944dbb2affe08d47744bb752918.png)
APIリクエスト制限、投稿制限を`閲覧可`、`即公開`として[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/12671f9adb9bc5b7cf15e2206d0ae29f.png)
後ほど利用するので、作成したアクティビティIDをメモしておきます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc89e2ddd79925992af7178285aab6fe.png)
### エンドポイントの作成
エンドポイントを作成します。今回は下記エンドポイントを作成します。

- newsdetailエンドポイント -> ニュース詳細
- commentsエンドポイント -> コメントの取得用
- commentエンドポイント -> コメントの追加用
- comment_deleteエンドポイント -> コメントの削除用

Comment TestのAPIで「新しいエンドポイントの追加」をクリックし、それぞれ作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1dfbc16f42969870fe73e2a3ff327888.png)
#### newsdetailエンドポイントの作成
newsdetailエンドポイントを下記設定にて作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ec0d55eca055cea3aa8c25b3f0720aa.png)

|項目|設定内容|
| :--- | :--- |
|パス|newsdetail|
|カテゴリー|コンテンツ|
|モデル|Topics v1|
|オペレーション|details|
|APIリクエスト制限|**None**|
|topics_group_id|表示するコンテンツ定義ID(9)|

設定完了後、「追加する」をクリックしnewsdetailエンドポイント完成です。  

#### commentsエンドポイントの作成
commentsエンドポイントを下記設定にて作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6a510d7e58e103626381eef6ac64acf3.jpg)

|項目|設定内容|
| :--- | :--- |
|パス|comments|
|カテゴリー|アクティビティ|
|モデル|Comment v1|
|オペレーション|list|
|APIリクエスト制限|**None**|
|id|アクティビティID(37)|
|module_type|topics|
|new_order_flg|チェックを入れる|

設定完了後、「追加する」をクリックしcommentsエンドポイント完成です。  

#### commentエンドポイントの作成
commentエンドポイントを下記設定にて作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7c65e689f7f95634c9ecf368f5487b09.png)

|項目|設定内容|
| :--- | :--- |
|パス|comment|
|カテゴリー|アクティビティ|
|モデル|Comment v1|
|オペレーション|insert|
|APIリクエスト制限|**None**|
|id|アクティビティID(37)|

設定完了後、「追加する」をクリックしcommentエンドポイント完成です。

#### comment_deleteエンドポイントの作成
comment_deleteエンドポイントを下記設定にて作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2dce8c50c45270be614df57cca00918f.png)

|項目|設定内容|
| :--- | :--- |
|パス|comment_delete|
|カテゴリー|アクティビティ|
|モデル|Comment v1|
|オペレーション|delete|
|APIリクエスト制限|**None**|
|id|アクティビティID(37)|

設定完了後、「追加する」をクリックしcomment_deleteエンドポイント完成です。  

:::caution
今回の例では、コメントの追加/削除するエンドポイントはセキュリティ`None`にしていますが、実際のサイトではコメントの追加/削除を許可するグループを設定してください。 
::: 

### フロントエンドの設定
#### コメント機能付きニュース詳細ページの追加
今回は既存のニュース詳細画面を参考に画面を作成し、同ページにコメント機能を追加します。  
まずは未承認のユーザーでもコメントの閲覧/投稿がきるようにし動作の確認をします。  

画面を表示する際にニュースへ紐づく全てのコメントを取得し、表示します。  

ユーザー名入力欄とコメント投稿のフォームが存在し、ユーザー名入力のあと、追加したコメントは即時に画面へ反映されます。  
またコメントそれぞれには削除ボタンが存在します。  

:::tip
コメントの削除はコメントの投稿・削除にパスワード(delkey)を使用するように構築するか、ログインを前提として、コメントを投稿した本人でないとできません。  
この段階では削除ボタンをクリックした場合、Code 422 "パスワードが一致しないか、書き込んだ本人でないため削除できません。" のエラーが発生します。  
:::

`/pages/news/test_with_comment.vue`を追加します。

**Nuxt2:**

```markup reference title="/pages/news/test_with_comment.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/test_with_comment_nodelete.vue
```

**Nuxt3:**

```markup reference title="/pages/news/test_with_comment.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/test_with_comment_nodelete.vue
```


以下のようにコメントの追加ができることを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50dc769924d1c6970ec7e06d1dab280d.gif)
### コメントを削除可能にする(delkeyの使用)

未承認のユーザーでもコメントの削除ができるようにするため、`delkey`を使用して削除をリクエストするように変更します。

`delkey`はコメントを追加する際に付与できる任意の値です。  
今回は以下の仕様で実装します。  
- コメントを追加する段階で`delkey`を自動的に付与
- `delkey`はブラウザのローカルストレージに保存
- 削除時にブラウザのローカルストレージから`delkey`を呼び出す
 
ブラウザへの保存はローカルストレージを使用するため、ブラウザの変更や異なる端末で操作再開する場合には削除できない点にご注意ください。

`/pages/news/test_with_comment.vue`を下記のように変更します。

**Nuxt2:**

```markup reference title="/pages/news/test_with_comment.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/test_with_comment_delkey.vue
```

**Nuxt3:**

```markup reference title="/pages/news/test_with_comment.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/test_with_comment_delkey.vue
```


以下のようにコメント済みのもののみ削除ボタンが表示して削除ができることを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/89bd9515db9ebee883f82820d798c769.gif)

## コメントをログイン必須にする
コメント機能のような変更/削除のためのPOSTエンドポイントを無施策に開放してしまうと、DoS攻撃(同時に大量のデータをPOSTすることで、DBをパンクさせるサイバー攻撃)に弱くなります。  
Kurocoのエンドポイントでは、同じIPアドレスから短時間に何回もコメントをされた場合に、投稿を受け付けないエラーを返す機能を持っていますが、本チュートリアルではページの閲覧、コメントの表示・投稿・削除にログインを必須とさせるように実装します。  

### アクティビティ定義の更新
[アクティビティ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b73cbe0b67685431b15982c5100fcba2.png)
作成したアクティビティのタイトルをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4da9b7e7f6f85c4482c9994c1099fb19.png)
未ログインメンバーのAPIリクエスト制限、投稿制限を`閲覧不可`、`受け付けない`として[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8d8b0de0829984fa80f59410ad0e389.png)
### フロントエンドの更新

`/pages/news/test_with_comment.vue`を次のように修正します。

**Nuxt2:**

```markup reference title="/pages/news/test_with_comment.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/test_with_comment_login.vue
```

**Nuxt3:**

```markup reference title="/pages/news/test_with_comment.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/test_with_comment_login.vue
```


最後に動作確認をして完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/53497dec5cb300d45f6d187b6fdbb0d8.gif)

## 関連ドキュメント
- [アクティビティ定義](/ja/docs/management/comment-module-list/)
- [アクティビティ](/ja/docs/management/comment-list/)
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [コメント機能に階層構造を追加する](/ja/docs/tutorials/add-depth-to-the-comment-function/)
- [アクティビティ機能で、特定ユーザーにしか見れないコメントを残す](/ja/docs/tutorials/how-to-only-display-comments-that-are-addressed-to-a-specific-user/)


---

# 事前に保存したHTMLをWysiwygエディタで呼び出す

> 元ページ: `tutorials/reuse-the-previously-saved-html-using-a-wysiwyg-editor` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/reuse-the-previously-saved-html-using-a-wysiwyg-editor/
> 概要: よく使用するHTMLは事前に保存しておき、Wysiwygエディタから呼び出せます。このドキュメントでは、HTMLの保存方法からWysiwygエディタで呼び出す方法までを説明します。

## 概要
よく使用するHTMLは事前に保存しておき、Wysiwygエディタから呼び出せます。  
このドキュメントでは、HTMLの保存方法からWysiwygエディタで呼び出す方法までを説明します。  

### 学べること
以下の手順で事前に保存したHTMLをWysiwygエディタで取得します。
- [テンプレートを保存する](#テンプレートを保存する)
- [テンプレートを呼び出す](#テンプレートを呼び出す)

## テンプレートを保存する
まずはよく使用するHTMLをWYSIWYGテンプレートに保存します。
[環境設定] -> [WYSIWYG専用テンプレート]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/724a35e12a85ec52a315cabec53ff7c8.png)

[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/48c656f2ded85cc498e87e9e7a512069.png)

以下のように設定します。

|項目|値|
|:--|:--|
|タイトル|任意のタイトル|
|ボディ|任意のHTML|
|公開設定|公開する|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/40512af58b2d87aa7763c9ceba6c2f25.jpg)

:::tip
[Source]のボタンをクリックするとHTMLのソースが表示されるので、直接クラス名の付与等が可能です。
:::

設定が完了したら[追加する]をクリックしてテンプレートを保存します。  

同様に必要なテンプレートをいくつか保存します。

## テンプレートを呼び出す
保存したテンプレートはコンテンツ編集画面のWYSIWYGエディタで呼び出せます。

### テンプレートを挿入する
WYSIWYGエディタのTemplatsアイコンをクリックし、利用するテンプレートをクリックします。  
テンプレート名にカーソルを載せると、テンプレートの内容がプレビューされるので、確認してクリックすると、エディタ内にテンプレートの内容が挿入されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7cc8098401250c98ee89a08cb80fcbd.gif)

## 関連ドキュメント
- [WYSIWYG専用テンプレート](/ja/docs/management/wysiwygtemplate/)
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [Kuroco管理画面のWYSIWYGエディタに任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-wysiwyg-editor/)
- [WYSIWYG カスタムカラーの設定方法](/ja/docs/reference/wysiwyg-custom-color-settings/)
- [WYSIWYGエディタに入力されたソースが自動変換されないように出来ますか？](/ja/docs/faq/can-i-prevent-sources-entered-into-the-wysiwyg-editor-from-being-automatically-converted/)


---

# コンテンツを公開したまま、指定の日時に更新する

> 元ページ: `tutorials/scheduling-updates-for-published-contents` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/scheduling-updates-for-published-contents/
> 概要: 承認ワークフローを使用して、公開中のコンテンツの更新を指定した日時に反映させる方法を説明します。

## 概要
このチュートリアルでは、[承認ワークフロー](/ja/docs/management/workflow/)を使用して、コンテンツの更新を指定した日時に反映させる方法について説明します。  

### 学べること
指定した日時にコンテンツの更新を反映させる方法を、以下の手順で実装します。  

- [承認ワークフローを作成する](#承認ワークフローを作成する)
- [コンテンツ編集画面で「承認の反映日時」を指定して更新する](#コンテンツ編集画面で「承認の反映日時」を指定して更新する)
- [承認者が承認する](#承認者が承認する)
- [反映待ちのコンテンツを確認する](#反映待ちのコンテンツを確認する)

### 前提条件
このチュートリアルでは、「お知らせ」のコンテンツにある「期間限定キャッシュバックキャンペーンのお知らせ」というタイトルの投稿を使用することにします。  
コンテンツの作成方法の詳細については、チュートリアル「[コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)」を参照してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d176ea11cb57c1b320b396bca26d0948.jpg)

## 承認ワークフローを作成する
[オペレーション]->[承認ワークフロー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aaff8286fb95f148c3d13e76d7856ea2.png)
[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ce8dbee41777aa32351506085e02f88.png)

承認ワークフローの基本設定が表示されるので、以下のように設定して[追加する]をクリックします。  

|項目   |内容  |
| :--- | :--- |
|名前|ワークフローの名前を入力します。|
|有効／無効|[有効]にチェックを入れます。|
|コンテンツ|承認ワークフローを利用するコンテンツを選択します。(今回は[お知らせ]を設定)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d7865b0d8fc6b44ee86c7a3dd71798a.jpg)

続いてフロー設定が表示されるので、以下のように設定して、[更新する]をクリックします。  
各項目の説明は[承認ワークフロー](/ja/docs/management/workflow/#項目説明-2)を参照ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/daf85f4f27a15e6e987c103944cf366e.jpg)
## コンテンツ編集画面で「承認の反映日時」を指定して更新する
先ほど設定した[お知らせ]のコンテンツで承認ワークフローが利用できるようになっています。  
更新したいコンテンツのタイトルをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4dfb719c15320ede4e1b420be7ceab42.png)

コンテンツの内容を変更し、ワークフロー設定を下記のように設定し、[更新する]をクリックします。  

|項目   |内容  |
| :--- | :--- |
|ワークフロー|ワークフローを選択します。|
|承認の反映日時|記事の更新を反映させる日付と時刻を設定します。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/76af9c428d2a5ea3f5a3faf90a036b94.jpg)

:::tip
選択できる時刻の間隔は以下のFAQを参考に変更できます。  
[コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？](/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/)
:::

## 承認者が承認する
対象のコンテンツ一覧のページに承認ワークフローで申請中のコンテンツが表示されるので、タイトルをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c2077e408e45b91dbb0e7130a8f9bbc4.png)

コンテンツの詳細が表示されるので、内容を確認し、[承認する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ec9736d6ec66584aa9d6943e461eeab6.png)

以上で、設定が完了です。  
設定した「承認の反映日時」に内容が更新されます。

:::tip
承認の作業は[承認ワークフロー](/ja/docs/management/workflow/)で設定したメンバーのほかに、「スーパーユーザー」や「コンテンツ（管理者）」の権限を持つグループのメンバーが行えます。  
:::

## 反映待ちのコンテンツを確認する
承認が完了し、反映待ちの状態になっているコンテンツは、コンテンツ一覧の申請中データの更新日時に`[承認完了]`の表示が付きます。  
また、[>>承認後反映待ち一覧]をクリックすると、バッチ一覧のページに遷移し、承認後反映待ちになっているコンテンツの一覧を確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ebee94a9de964deda96763227a614364.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fd7df17832d8b6513a349d107991284d.png)

## 関連ドキュメント
- [承認ワークフロー基本設定](/ja/docs/management/workflow/#承認ワークフロー基本設定)
- [承認ワークフローフロー設定](/ja/docs/management/workflow/#承認ワークフローフロー設定)
- [コンテンツの編集](/ja/docs/management/content-structure-topics/#コンテンツの編集)
- [コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？](/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/)


---

# マスタ形式を使って動的に変化する選択項目を設定する

> 元ページ: `tutorials/setting-up-dynamic-options-using-master` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-dynamic-options-using-master/
> 概要: このチュートリアルではマスタ形式の項目を使用して、動的に変化する選択項目を設定する方法について説明します。

## 概要
このチュートリアルでは[マスタ形式](/ja/docs/management/master/)の項目を使用して、動的に変化する選択項目を設定する方法について説明します。

### 学べること
コンテンツ定義で動的に変化する選択項目を設定する方法を学びます。

- [マスタ設定](#マスタ設定)
- [コンテンツ定義設定](#コンテンツ定義設定)
- [コンテンツ編集画面確認](#コンテンツ編集画面確認)


## マスタ設定
まずは選択肢になるkey,labelをマスタで登録します。

[コンテンツ]->[マスタ]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8edefc6a674045fb0cb60020cd9ebd39.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b7e6d73d241ee2528f7b94e1efdf75b.png)

マスタ編集が表示されるので、以下のように設定して[追加する]をクリックします。  

|項目   |内容  |
| :--- | :--- |
|タイトル|市区町村|
|表組み(テーブル)	|未設定で構いません|
|CSVで更新(文字コード)|作成したCSVの文字コードを選択|
|CSVで更新(ファイル)|以下の内容をcsvをファイルに保存して設定|

```csv
"city_cd","city_name","prefecture_cd","prefecture_name"
"13101","千代田区","13","東京都"
"13102","中央区","13","東京都"
"14101","横浜市鶴見区","14","神奈川県"
"14102","横浜市神奈川区","14","神奈川県"
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6673f9dfd6561961fbbf663f196f1b3b.png)

マスタが登録されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7706168b582326143ca3d7e5a643eac9.png)

## コンテンツ定義設定

任意のコンテンツ定義で、マスタ形式を使用した親子の2項目を設定します。  
これにより、親項目で選択したキーを使って、子項目で選択できるキーを動的に変更します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/988a021dd98672f7833d3601e9fbf1f9.png)

**親項目**

|項目   |内容  |
| :--- | :--- |
|項目名|都道府県|
|項目設定|マスタ形式|
|選択項目(マスタ)|[マスタ設定](#マスタ設定)で作成したマスタを選択してください。|
|選択項目(キー)|キーに使用するデータの列番号(0始まり)を指定します。親項目ではprefecture_cdを使用するので`2`を設定してください。|
|選択項目(値)|ラベルに使用するデータの列番号(0始まり)を指定します。親項目ではprefecture_nameを使用するので`3`を設定してください。|
|親ID|空欄|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c19782ce10e7977e06aef8a7deeb915c.png)

**子項目**

|項目   |内容  |
| :--- | :--- |
|項目名|市区町村|
|項目設定|マスタ形式|
|選択項目(マスタ)|[マスタ設定](#マスタ設定)で作成したマスタを選択してください。|
|選択項目(キー)|キーに使用するデータの列番号(0始まり)を指定します。<br/>今回は親項目で選択されるprefecture_cd(2)で行の絞り込みを行いcity_cd(0)をキーとするので、`[2,0]`と設定します。|
|選択項目(値)|ラベルに使用するデータの列番号(0始まり)を指定します。子項目ではcity_nameを使用するので`1`を設定してください。|
|親ID|親項目として使用する拡張IDを設定します。この例では`6`を設定します。(先頭のext_は不要です)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e59cd7e351af5df56ba9d579c846c5de.png)

:::info
- 動的に変化する選択項目の設定はマスタ形式とマスタ(チェックボックス)で使用可能です。
- 子項目のキーは`[a,b]`の形式で設定します。  
  - a:親項目で選択されたキー(prefecture_cd)と照合する列番号を指定。  
  - b:この項目自体のキーとして使用する列番号(city_cd)を指定。
  
  例えば、親項目で「東京都」(prefecture_cd="13")を選択すると、prefecture_cdの列が"13"の行のcity_cdとcity_nameのみが選択肢として表示されます。
:::

## コンテンツ編集画面確認
[コンテンツの編集](/ja/docs/management/content-structure-topics/#コンテンツの編集)
を参考に記事の編集ページにアクセスし、親項目を選択すると下記のように選択項目が動的に絞り込まれていることが確認できます。

- 親項目で東京を選択
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ba5cc3e5a65d11ae3ba3652d7097276.png)

- 親項目で神奈川を選択
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/18c6cf5dda3faffd8ed3158e9550be93.png)

## 関連ドキュメント
- [コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#コンテンツ定義編集)
- [コンテンツの編集](/ja/docs/management/content-structure-topics/#コンテンツの編集)


---

# サブ項目(JSON)を使用して複雑な構造を持つコンテンツ項目を設定する

> 元ページ: `tutorials/setting-up-json-field` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-json-field/
> 概要: サブ項目(JSON)はコンテンツ定義に設定できる拡張項目の1つで、任意のJSON形式でデータを登録できるため、深いネスト構造を設定したり、外部システムから取得したJSONをそのまま格納したりできます。

## 概要

サブ項目(JSON)はコンテンツ定義に設定できる拡張項目の1つで、任意のJSON形式でデータを登録できるため、深いネスト構造を設定したり、外部システムから取得したJSONをそのまま格納したりできます。  
また、設定したJSONデータ定義からUIを自動生成できますので、項目の繰り返しと組み合わせてネスト構造を設定したり、ブロックエディタと組み合わせてカードUIのサブ項目として利用するなど、柔軟な利用が可能です。

本チュートリアルでは[サブ項目(JSON)]の設定について、想定される利用法方法を紹介します。

### 学べること
サブ項目(JSON)の使用例と、その設定方法を学びます。

- [JSONデータをそのまま入力する](#jsonデータをそのまま入力する)
- [項目の繰り返しと合わせてネストされた項目を設定する](#項目の繰り返しと合わせてネストされた項目を設定する)
- [ブロックエディタのサブ項目として利用する](#ブロックエディタのサブ項目として利用する)

## JSONデータをそのまま入力する
UIが不要でJSONデータをそのまま利用する場合、JSON構造に制限はありません。  
JSONデータ定義でJSON構造とそのバリデーションを設定します。

ここでは例として、「組織→部門→チーム→サービス」の深いネスト構造を持つ項目を設定します。

### コンテンツ定義設定

以下のコンテンツ定義を設定します。

|項目   |内容  |
| :--- | :--- |
|項目名|所属部署|
|項目設定|サブ項目(JSON)|
|JSONデータ定義からUIを構成する|無効|
|JSONデータ定義(入力制限タブ)|以下のJSONを入力|

```json
{
  "title": "Organization → Department → Team → Service",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "name": { "type": "string" },
    "departments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": { "type": "string" },
          "name": { "type": "string" },
          "teams": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": { "type": "string" },
                "services": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "name": { "type": "string" }
                    },
                    "additionalProperties": false,
                    "required": ["name"]
                  }
                }
              },
              "additionalProperties": false,
              "required": ["name", "services"]
            }
          }
        },
        "additionalProperties": false,
        "required": ["code", "name", "teams"]
      }
    }
  },
  "additionalProperties": false,
  "required": ["id", "name", "departments"]
}
```

上記のJSONデータ定義では、以下の項目を定義します。

- 組織:`id`, `name`, `departments`  
- 部門:`code`, `name`, `teams`  
- チーム:`name`, `services`  
- サービス:`name`  


### コンテンツ編集画面

コンテンツ編集画面でJSONデータを入力します。  
エディタ形式の入力フォームですが、定義外の項目が存在する場合と定義された項目が存在しない場合にバリデーションエラーを出しますので、フロントエンド側は指定されたJSON構造がレスポンスされる前提で実装できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/64a1fb949df92d9b1628c5d46cb538e4.png)

以下が期待されるJSONの例です。

```json
{
  "id": "org-001",
  "name": "業務本部",
  "departments": [
    {
      "code": "",
      "name": "",
      "teams": [
        {
          "name": "",
          "services": [
            {
              "name": "監査係"
            }
          ]
        }
      ]
    },
    {
      "code": "HR",
      "name": "人事部",
      "teams": [
        {
          "name": "採用チーム",
          "services": [
            {
              "name": "エンジニア採用係"
            }
          ]
        },
        {
          "name": "研修チーム",
          "services": [
            {
              "name": "エンジニア研修係"
            }
          ]
        }
      ]
    }
  ]
}
```

JSONデータの項目に過不足がある場合にバリデーションエラーが出ることも確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d75961c960f873533d214ed82ecf99d8.png)

## 項目の繰り返しと合わせてネストされた項目を設定する
コンテンツ定義で「JSONデータ定義からUIを構成する」を有効にすると、設定したJSONデータ定義から自動でUIが生成されるため、
直感的なコンテンツ登録が可能になります。

自動で生成するUIについて、JSONデータ定義のサンプルについては以下のリファレンスをご参照ください。

:::info
- [JSON Schemaパターンサンプル](/ja/docs/reference/json-column-schema/)
:::

ここでは、項目の繰り返し設定とサブ項目(JSON)の繰り返し設定を組み合わせて、2段階のネスト構造を設定する例を紹介します。

### コンテンツ定義設定

まずはコンテンツ定義で以下の項目を作成します。

|項目   |内容  |
| :--- | :--- |
|項目名|FAQ項目|
|項目設定|サブ項目(JSON)|
|JSONデータ定義からUIを構成する|有効|
|JSONデータ定義(入力制限タブ)|以下のJSONを入力|

```json
{
  "type": "object",
  "properties": {
    "faqCategory": {
      "type": "string",
      "title": "FAQカテゴリ"
    },
    "faqs": {
      "type": "array",
      "title": "FAQ",
      "items": {
        "type": "object",
        "properties": {
          "question": {
            "type": "string",
            "title": "質問"
          },
          "answer": {
            "type": "string",
            "format": "textarea",
            "title": "回答"
          }
        }
      }
    }
  }
}
```

次に作成したサブ項目(JSON)の繰り返し設定をします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a450b36c08d491f3046068bf43c45a1e.png)

### コンテンツ編集画面

コンテンツの編集画面にアクセスすると、項目の繰り返しでFAQのカテゴリを追加し、サブ項目(JSON)の繰り返しでFAQを追加できるUIが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/46f7c9371efb942778ce9081795a18df.png)

## ブロックエディタのサブ項目として利用する
サブ項目(JSON)を使用すると、1つの項目内に複数のデータをまとめて登録できます。  
こちらを利用してカードUIを作成し、ブロックエディタのサブ項目として利用できます。

### コンテンツ定義設定

まずはコンテンツ定義で以下の項目を作成します。

|項目   |内容  |
| :--- | :--- |
|項目名|ニュースカード|
|項目設定|サブ項目(JSON)|
|JSONデータ定義からUIを構成する|有効|
|JSONデータ定義(入力制限タブ)|以下のJSONを入力|

```json
{
  "type": "object",
  "properties": {
    "news": {
      "type": "array",
      "title": "ニュース一覧",
      "description": "最新のニュースを最大10件まで登録できます",
      "minItems": 1,
      "maxItems": 10,
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "title": "タイトル",
            "description": "ニュースのタイトルを入力してください",
            "maxLength": 100
          },
          "link": {
            "type": "string",
            "title": "リンク",
            "description": "ニュース記事のURLを入力してください"
          },
          "publishDate": {
            "type": "string",
            "title": "公開日",
            "format": "date"
          },
          "category": {
            "type": "string",
            "title": "カテゴリー",
            "enum": ["press", "blog", "event", "update"],
            "enumNames": ["プレスリリース", "ブログ", "イベント", "アップデート"]
          }
        },
        "required": ["title", "link"]
      }
    }
  }
}
```

次に作成したサブ項目(JSON)をブロックエディタのサブ項目として設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/40b36432955a9c41c5048f6e15760cc6.png)

### コンテンツ編集画面

コンテンツ編集画面にアクセスすると、ブロックエディタで選択できるニュースカード項目が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/84eef78afe17d88944962ded48fb0f05.png)

## 注意事項
- JSONデータ定義からUIを構成する機能は、Object → Array → Objectを超えるネスト構造(繰り返しUIの中に繰り返しUIがネストされる構造)はサポートしていません。
- サブ項目(JSON)は現状、検索項目として使う想定になっていません。検索が必要な場合は他の項目をご利用ください。

## 関連ドキュメント
- [JSON Schemaパターンサンプル](/ja/docs/reference/json-column-schema/)
- [コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#コンテンツ定義編集)
- [コンテンツの編集](/ja/docs/management/content-structure-topics/#コンテンツの編集)


---

# WEBクローラーの設定方法

> 元ページ: `tutorials/setting-up-web-crawler` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-web-crawler/
> 概要: KurocoのWEBクローラー機能を使って外部WebページをクロールしKurocoのコンテンツに取り込む手順を、公式ドキュメントサイトの一部をクロールする実例で説明します。

## 概要

このチュートリアルでは、KurocoのWEBクローラー機能を使って外部Webページをクロールし、収集した内容をKurocoのコンテンツとして取り込む手順を説明します。

WEBクローラーは、bot（クローラー）が指定したWebページを巡回し、テキスト・画像・ファイルなどを収集してKurocoのコンテンツに取り込む機能です。収集したコンテンツはKuroco RAGのベクトルデータに変換してAIの回答に利用したり、差分検知と組み合わせて更新通知に利用したりできます。

:::caution
WEBクローラーを実行すると、クロール結果の登録や実行状態の更新のためにAPIリクエストが発生し、利用料が発生します。

APIリクエスト数は設定や実行結果によって異なります。実際のリクエスト数は[APIリクエストログ](/ja/docs/management/api-request-log-list/)で確認してください。利用状況と料金の計算方法については、[利用状況](/ja/docs/management/usage/)を参照してください。
:::

このチュートリアルでは、Kuroco公式ドキュメントサイトの更新情報ディレクトリ（`https://kuroco.app/ja/docs/update/`）を対象に、リリースノート（`release-note-*`）を除外してクロールする例を扱います。この設定では2ページ（[Kuroco リリースロードマップ](https://kuroco.app/ja/docs/update/kuroco-roadmap/)と[Kurocoのバージョン管理について](https://kuroco.app/ja/docs/update/roadmap-kuroco-version/)）のみがクロールされます。

### 学べること

このチュートリアルを終えると、次のことができるようになります。

- 収集対象のWebページを指定したWEBクローラーを作成する
- クロール結果の保存先となるコンテンツ定義を作成し、クローラーと連携する
- クロールを手動で実行し、履歴と収集結果を確認する
- クロール結果をAIの回答や更新通知に活用する方法を理解する

### 前提条件

:::info
- **Kurocoアカウント**: 有効なKurocoアカウントが必要です。アカウントをお持ちでない場合は、[無料トライアル](https://kuroco.app/ja/free_trial/)からアカウント登録してください。
:::

## クローラーの設定

まず、収集対象のWebページを定義するWEBクローラーを作成します。

**1. WEBクローラー一覧を開く**

管理画面の左メニューから[チャネル] -> [WEB] -> [WEBクローラー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee73ffbcb6617fc401526124a65d31ba.png)

WEBクローラー一覧が表示されます。右上の[+ 追加]をクリックすると、WEBクローラー編集画面が開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f260edd8481f9e50f1a86718e4a5f11c.png)

**2. 基本設定を入力する**

[基本設定]で以下を設定します。

| 項目 | 入力値 |
|------|------|
| タイトル | `Crawl Test`（任意の識別名） |
| ステータス | 「有効にする」をオンにします |
| クロール対象 | 「WEBページをクロール」を選択します |
| クロール数制限 | `0`（無制限）のままにします |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2346b274172990c75000c8691bb99469.png)

**3. 収集設定を入力する**

今回はテキストを収集するため、[テキストデータ収集]をオンにします。ファイルや画像を収集する場合は、あわせて[ファイル収集（PDFやOfficeファイル）]や[画像収集する]をオンにします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/41f6152d3c01ad710fdbd89e9fc79201.png)

**4. WEBページのクロール設定を入力する**

クロール対象に「WEBページをクロール」を選択すると、[WEBページのクロール設定]が表示されます。今回の例では以下を設定します。

| 項目 | 入力値 |
|------|------|
| 開始URL | `https://kuroco.app/ja/docs/update/kuroco-roadmap/` |
| 許可されているURL | `https://kuroco.app/ja/docs/update/` |
| 拒否されるURL | `https://kuroco.app/ja/docs/update/release-note-` |
| リンクの追跡 | オンにします |

[開始URL]からクロールを開始し、[リンクの追跡]でページ内のリンクをたどります。[許可されているURL]で`/ja/docs/update/`配下のみに対象を限定し、[拒否されるURL]でリリースノート（`release-note-*`）を除外します。

<a><img src="https://t.gyazo.com/teams/diverta/48c84fbaf50becc11c180028b34181ce.png" style={{ width: 400, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/8c239b2a25b1a2932bd012bdcaff429f.png" style={{ width: 400, maxHeight: 'none' }} /></a>


**5. 保存する**

画面を一番下までスクロールし、[更新する]をクリックして保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b148f7dbfdfa961f6b26f0d4b3a78832.png)

## コンテンツ定義の設定

次に、クロール結果を保存するコンテンツ定義を作成し、手順で作成したクローラーと連携します。

**1. コンテンツ定義を追加する**

左メニューの[コンテンツ定義]を開き、右上の[+ 追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7bad681738063e7695a7e97924abb758.png)

**2. データ種別を「クローリング」にする**

コンテンツ定義名を入力し、[全般]タブの[データ種別]で「クローリング」を選択します。クロール結果の保存に必要な項目は自動で追加されるため、項目設定は変更しないでください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2cc8dbbfdc27cf6b3bc96d2b4b5d705f.png)

:::info
[クローリング]タブは、[データ種別]で「クローリング」を選択すると左サイドバーに表示されます。選択しない場合はタブが表示されません。
:::

**3. 連携クローラーを設定する**

左サイドバーの[クローリング]をクリックし、以下を設定します。

| 項目 | 入力値 |
|------|------|
| Webページを有効にする | オンにします |
| 連携クローラー設定 | 「クローラーの設定」で作成したクローラーを選択します |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cebe53047df7c137e36db1336cce5d81.png)

[+ 追加する]をクリックして保存します。保存後、Contents・URL・ハッシュ値・言語・画像・last-modifiedなどの項目が自動で追加されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee795b81a0da05e4d9d8e41dba56c4d9.png)

:::note
[連携クローラー設定]には、すでに作成済みのクローラーが表示されます。
:::

## クロールの動作確認

### クロールを実行

コンテンツ定義との連携が完了したら、クロールを手動で実行して結果を確認します。

左メニューの[チャネル] -> [WEB] -> [WEBクローラー]から作成したクローラーのタイトルをクリックして編集画面を開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d85879a340247073962e3c5b574ca37a.png)

右上の[クロールを実行]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9109b2c566774ff9aaaa19f7456e91b3.png)

:::note
ステータスを「有効」にしても自動ではすぐに実行されません。初回の動作確認は[クロールを実行]で手動実行してください。
:::

### 履歴の確認

WEBクローラー編集画面の右上にある[履歴]をクリックすると、実行履歴が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ded00330fbae2e3cacd3ca78bfff0f22.png)

反映までタイムラグがあるため、[リロードする]をクリックして最新の状態を確認します。ステータスが完了に変わり、クロール数が表示されれば成功です。今回の設定では、[Kuroco リリースロードマップ]と[Kurocoのバージョン管理について]の2ページがクロールされます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0af7f5e819b3488fcc6f5e91316f8aa.png)

### コンテンツの確認

左メニューから、連携先のコンテンツをクリックします。クロールで収集されたページがコンテンツとして登録されていることを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/596153bfc86aab6c7dc26cce5c58fe94.png)

各コンテンツを開くと、Markdown形式に変換された本文やURLなどが格納されていることを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5e24d9155543788e931b11b174e5ebbf.png)

:::note
WEBクローラーには差分検知の仕組みがあり、再クロール時に前回と内容が変わっていないページは更新されません。すべてのページを強制的に更新する場合は、クローラーの[基本設定]で[強制更新]をオンにします。
:::

## クロール結果の活用例

### AIからの回答として使用する

クロールしたコンテンツはKuroco RAGのベクトルデータに変換できるため、AI/RAG機能と組み合わせて活用できます。例えば、製品ドキュメントサイトをクロールしたコンテンツをもとに、ユーザーからの質問にAIが回答できるようになります。

1. [AI] -> [ベクトルデータ]で[ベクトルデータ](/ja/docs/management/vector-data/)が生成されていることを確認します。
2. チャットボットのAPIを設定し、クロールしたコンテンツ定義をデータソースとして指定します。

チャットボットの設定方法については、以下のドキュメントを参照してください。
- [AIによる回答を生成する](/ja/docs/tutorials/generating-ai-responses/)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)

### 更新通知として使用する

差分検知の仕組みとカスタム関数を組み合わせると、更新通知の仕組みを構築できます。例えば、コンテンツ定義のカスタム関数トリガーに`{sendmail}`や`{slack_post_message}`を設定すると、クロール対象ページに変更があった際に通知を送れます。

また、より細かい頻度でクロールを自動実行したい場合は、Smartyプラグイン`{kick_spider}`とバッチ処理を組み合わせる方法があります。詳しくは[kick_spider](/ja/docs/reference/smarty-plugin/#kick_spider)を参照してください。

## 関連ドキュメント

- [WEBクローラー](/ja/docs/management/spider-list/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [kick_spider（Smartyプラグイン）](/ja/docs/reference/smarty-plugin/#kick_spider)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)
- [ベクトルデータ](/ja/docs/management/vector-data/)


---

# コンテンツ一覧ページにページネーションを実装する

> 元ページ: `tutorials/splitting-the-contents-list-into-multiple-pages` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/splitting-the-contents-list-into-multiple-pages/
> 概要: 本チュートリアルではコンテンツ一覧/詳細ページを作成するで作成したコンテンツ一覧ページにページネーションを実装する方法を説明します。

コンテンツの数が多い場合、コンテンツ一覧を複数のページに分割するページネーションの実装が必要になる場合があります。    
Kurocoのトピックスリストのエンドポイントは、レスポンスに記事数・現在のページ・ページ数の合計 などが含まれるため、フロント側でページ数の計算をすることなくページネーションの実装が可能です。  

本チュートリアルでは[コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)で作成したコンテンツ一覧ページ(お知らせ一覧)にページネーションを実装する方法を説明します。

:::info
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、コンテンツ一覧のページが作成されていることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## APIの設定
APIの登録内容は[コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)と同じです。  
こちらで作成したAPIをそのまま利用する場合は[Kurocoで1ページ当たりの表示数を設定する](#kurocoで1ページ当たりの表示数を設定する)に進んでください。  

### API基本設定を行う
まずはAPIの登録をします。  
Kurocoの管理画面から[API]->[Default]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5a0c3aacbb47a0e6c9fb95819d14622.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa425815fa52294d9cac473ad30f8128.png)

タイトル、版、ディスクリプションを入力して[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/958f09b0a556a3516d3638c1353b5130.png)

追加したAPIに遷移しますので、続いて、セキュリティの設定をします。  
[セキュリティ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ec763d0832bd03f97f4df47763b86dca.png)

[Cookie]を選択して[保存する]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/6dcf2c3d012ebf03155f8926f0695379.png)
注意)  
Cookieをセキュリティ用のトークンとして利用する場合、APIドメインとフロントエンドのドメインが違うとサードパティクッキーの問題があり、Safari等で認証が効きません。  
フロントエンドとAPIドメインをサブドメイン違いで設定をする必要があるので、[独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)でAPIドメインを設定し、[アカウント設定](/ja/docs/management/account/)からAPIドメインを変更ください。  
（Chromeでは正常に動作しますので、開発やテストの段階ではまずChromeで構築していただくことをお勧めします。）

### CORS設定を行う
[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c31ec737110c5ddda6ee20e3a221d342.png)

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
次にエンドポイントを作成します。今回は下記エンドポイントを作成します。  

- お知らせ一覧エンドポイント
- お知らせ詳細エンドポイント

#### お知らせ一覧
お知らせ一覧エンドポイントを下記設定にて作成します。

|項目|設定内容|
| :--- | :--- |
|パス|news|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|list|
|topics_group_id|お知らせを登録しているコンテンツ定義ID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fda2309fde8090f4c1d2ff65fe0be0df.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a02e75811a76d820b62732e1b67c36e2.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/91afaa79ca6ef04075cf78098ad8275f.png)

設定完了後、「追加する」をクリックします。

#### お知らせ詳細 
お知らせ詳細エンドポイントを下記設定にて作成します。

|項目|設定内容|
| :--- | :--- |
|パス|newsdetail|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|details|
|topics_group_id|お知らせを登録しているコンテンツ定義ID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/95ebb0e4019f4af4cafd028a93a35f23.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a02e75811a76d820b62732e1b67c36e2.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/91afaa79ca6ef04075cf78098ad8275f.png)

設定完了後、「追加する」をクリックします。

## Kurocoで1ページ当たりの表示数を設定する
1ページ当たりのコンテンツ表示数は固定になるため、Kurocoの管理画面側でパラメータの設定をします。 
エンドポイントに表示するページの情報をパラメータとして渡すことで、各ページのレスポンスを得ていきます。  

お知らせ一覧のエンドポイントを作成したAPIのページに遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/052548ae1fe3eba592d0b01de25d79ce.png)

お知らせ一覧のエンドポイント(今回の場合は `/rcms-api/7/news`)の[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/57810fe317946b11b136a4c9e376d5b2.png)

エンドポイントの設定画面が開くので、基本設定の`cnt`に1ページ当たりの表示数を入力します。今回は`4`と入力し[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/03c946b780be0a213db4e3a7a2c84a4c.png)

## Swagger UIで各ページの情報が取得できることを確認する
次にエンドポイントからのレスポンスを確認します。  
「お知らせ一覧」のエンドポイントを作成したAPIのページに遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/052548ae1fe3eba592d0b01de25d79ce.png)

[Swagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c21ac4c4401f5e76a15d543a70dbef49.png)


「お知らせ一覧」のエンドポイントの[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e7db8be87b58432b75892f64a994c3e.png)

`pageID`に1を入力します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/299a5abf624e63bc0fe7dbe475a549df.png)
[Execute]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/91b50a53ccfd747a2c6f242c7ca34458.png)
レスポンスを確認すると1ページ目の4件のリストと、`pageInfo`の情報が確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/28e446849d1eb0926f9b16035b3626c3.png)

同様に`pageID`にページ数を入力して[Execute]をクリックすると、各ページのリストと、`pageInfo`のレスポンスが得られます。  
こちらを利用してフロントでページネーションを実装してきます。  

## 現在のページ情報をパラメータで指定する
現在のページの情報をパラメータに追加し、各ページに対応するレスポンスを得ます。  
以下の内容でファイルを作成します。  
今回は`/news_paginated/`、`/news_paginated/slug/`のディレクトリ名でページが表示できるようにファイルを作成しました。 

**Nuxt2:**

```markup reference title="/pages/news_paginated/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_paginated.vue
```

```markup reference title="/pages/news_paginated/_slug.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/news_paginated_details.vue
```

**Nuxt3:**

```markup reference title="/pages/news_paginated/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_paginated.vue
```

```markup reference title="/pages/news_paginated/[slug].vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/news_paginated_details.vue
```


:::caution
`/rcms-api/7/news`、`/rcms-api/7/newsdetail`の部分はご自身のエンドポイントのURLに変更してください。<br/>
以下同様に、ソースコード内のエンドポイントURLはご自身のエンドポイントURLに変更をお願いします。
:::

クエリパラメータに`?page=2`を追加すると、表示されるお知らせの一覧が変更されることを確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fef2aaef635a90c77defd4627fbda379.gif)

## ページ遷移のためのリンクを表示する
次にページを遷移するためのリンク部分を作成します。  
エンドポイントからのレスポンスの`pageInfo`に現在のページ数や最終ページの情報が含まれるので、こちらを利用します。  
ここでは簡単な例として`index.vue`ファイルを以下のように修正します。  
また、リンクの記述部分は流用できるよう`components`フォルダに`Pagenator.vue`のファイルを作成し、こちらに記述します。  

`index.vue`に以下の記述を追加します。

**Nuxt2:**

```diff title="/pages/news_paginated/index.vue"
      </nuxt-link>
    </div>
+    <Pagenator v-bind="{ ...response.pageInfo }" />
  </div>
</template>
```

**Nuxt3:**

```diff title="/pages/news_paginated/index.vue"
      </nuxt-link>
    </div>
+    <Pagenator v-bind="{ ...response.pageInfo }" @page-update="updatePage" />
  </div>
</template>
```


`/components/Pagenator.vue`を下記のように作成します。  

**Nuxt2:**

```markup reference title="/components/Pagenator.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/components/Pagenator.vue
```

**Nuxt3:**

```markup reference title="/components/Pagenator.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/components/Pagenator.vue
```


各ページへのリンクが追加できました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/12280b097e535b22910a5c8b497aeaf4.png)

以上で、KurocoとNuxt.jsで、コンテンツ一覧ページにページネーションを実装する方法の説明を終わります。

## 関連ドキュメント
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)


---

# カテゴリ拡張設定を利用する

> 元ページ: `tutorials/using-category-ext-configuration` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-category-ext-configuration/

コンテンツカテゴリには項目１～項目５のフィールドがあり、こちらはカテゴリの説明や、カテゴリ毎に設定した画像のパス等、任意の情報を入力して利用できます。  
入力した内容は[コンテンツ][TopicsCategory][list]のAPIで取得します。  

[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)にあるカテゴリ拡張設定で、項目名や設定項目の編集をすることで、Kurocoの管理画面を利用するユーザーに対して、入力する内容を表示したり画像のパスを簡単に設定させることが可能です。  

今回はカテゴリ拡張設定の利用方法を説明します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/82ffe777ef17848408c2686f4928b04f.jpg)

## コンテンツ定義の設定をする
### 1. コンテンツ定義編集のページにアクセスする 
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/55f7181e474c014b626f6b19553d150f.png)

編集を行うコンテンツ定義の[名前]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/59c2b7fa2406f916d5debbf454819d12.png)

コンテンツ定義編集の[詳細設定]でカテゴリ拡張設定が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d5338b4074b70af941bb8122c0765d2.jpg)

### 2. カテゴリ拡張設定に入力する
カテゴリ拡張設定で利用できるtypeは下記の2つです。  

|項目   |説明  |
| :--- | :--- |
|text|テキスト入力エリアを表示します。|
|filemanager|KurocoFilesを開いてファイルを選択するためのボタンを表示します。|

また、`{"disabled":1}`と指定すると項目の表示を消すことができます。  

ここでは例として下記のように入力して、[更新する]をクリックします。
```
{
 "ext_col_01":{
   "name": "カテゴリ説明",
   "type": "text"
 },
 "ext_col_02":{
   "name": "メインビジュアル",
   "type": "text"
 },
 "ext_col_03":{
   "name":"画像",
   "type":"filemanager"
 },
 "ext_col_04":{
   "name":"副言語での並び順",
   "type":"text"
 },
 "ext_col_05":{"disabled":1}
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f19477a5392a9c0e37835cdc3c50229d.jpg)

## カテゴリの表示を確認する
[コンテンツカテゴリ編集](/ja/docs/management/content-structure-topics-category/#コンテンツカテゴリ編集)を参考にカテゴリの編集ページにアクセスすると、下記のように表示が変更されていることがわかります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/65611578badf894bd40a5e9e6838e16e.jpg)

表示名は変更されますが、エンドポイントからのレスポンスは`ext_col_01`～`ext_col_05`で変わりません。  

エンドポイントからのレスポンスを確認する方法は [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/) を参照ください。  

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツカテゴリ](/ja/docs/management/content-structure-topics-category/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [APIのレスポンスをコンテンツカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-content-category/)


---

# Slackで定期的に確認をサポートするbotアプリ「KurocoWorkflow」のインストールと利用方法

> 元ページ: `tutorials/workflow-bot` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/workflow-bot/
> 概要: Slackにてメンションがついた投稿にスタンプがつけられるまで、定期的にリマインドを送るbotをKurocoにて作成しました。利用方法を説明します。

:::note
想定作業時間：10分
:::


## アプリ概要説明

Slackにてメンションがついた投稿に「👍」スタンプがつけられるまで、定期的にリマインドを送るbotをKurocoにて作成しました。
- このパッケージは[Slack用「確認お願いしますボット」の仕様（誰か作ってほしい）](https://note.com/fladdict/n/n640d61574f31)の記事にインスピレーションを得て1日で作成したものです。
- 月間3000ワークフロー程度の利用で無料枠1100円/月を超える予想です。
- こちらのパッケージをOEMで提供していただく、または改造いただいても構いません。全て管理画面で設定されたものです。不具合や要望など是非、フィードバックをください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/65e9dafc85e937517558d93e54f3c871.png)
### 起動条件
下記条件にてAppが起動されます。
- @KurocoWorkflow にメンションがついていること
- 誰か宛にメンションがついていること

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/757e94967460f06eedc8056473b29778.png)
### リマインド時間の設定
下記条件にて、メンション受けた人で「👍」または「👎」スタンプをつけてない人に定期的にDMでリマインダーが送られます。
- デフォルト：12時間毎
- 投稿内に「🔥」が記載されている場合：1時間毎（メッセージを編集して、途中から緊急にもできます）

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/aba23f4eab66fef5304c2b07f9e456ec.png)
### 完了条件
下記にてリマインドが完了します。
- slackの**メッセージ**に「👍」または「👎」スタンプをつける

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/59bad220d72608911d7a648bb76c28fc.png)
### キャンセルの条件
下記にてリマインドがキャンセルされます。
- slackの**メッセージ内**に「❌」スタンプを記入する(つまり投稿者のみキャンセル可能です)

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a192a981ab3a021e4aea4fbb66ea9e13.png)
### ウォッチの条件
下記にて結果がDMで共有されます。
- slackの**メッセージ**に「👀」スタンプをつける

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4a28c8210d5d942703cf619e6540f562.png)
### ワークフロー終了の条件
メンションを受けた人が全員「👍」または「👎」のリアクションをすると、ワークフローが終了します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d664f13360eaec3dcc8dc93b01794ba0.png)

## バックエンドの準備をする
### Kurocoの登録
まずはKurocoのアカウント登録します。[無料トライアル](https://kuroco.app/ja/free_trial/)より必要項目を記入し、「登録する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a80b767e116713164250606ff2b4ca58.png)

:::caution
KurocoWorkflowはサブサイトで運用します。  
メインサイトとサブサイトで別々のサイトキーになるのでそれぞれ準備してください。

無料トライアルから登録するサイトキーはメインサイトのものになります。
:::

登録したメールアドレスに登録完了のメールが届きます。メール内に記載されている管理画面URLをクリックし、ログインを行うと下記画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a370334b8d179ad7d55cf6b62756802.png)

### サブサイトの追加
サイト一覧からKurocoWorkflow用のサブサイトを追加します。  

:::info
メインサイトのデフォルトは会員制サンプルサイト用の設定になっています。  
お支払い用のクレジットカードはメインサイトで登録し、サブサイトの利用料を含めた費用がメインサイトに請求されます。  
:::

[環境設定] -> [サイト一覧]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e62d36fc06738d5bd8bde2772e0d807.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2275c30e4535ce3d720c21ccd054af4.png)

コピー元のサイト名を`workflow(Default)`に設定し、必須項目を入力して[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/96fe6fd0e931f9771b6708d8b479bd8b.png)

サブサイトの登録完了のメールが届いたらログインをしてコンテンツを確認します。  

:::note
以降、Kuroco管理画面の説明はすべてサブサイトのものになります。
:::

### APIドメインの確認
Slack連携に必要となるAPIドメインを確認します。[環境設定] -> [アカウント設定]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f807438e08fc8685686d787544197afc.png)
アカウント設定画面が表示されるので、「APIドメイン」を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8aa379fe922d9643e95496372556a8fa.png)

こちらは後ほど利用するのでコピーをとっておいてください。

### エンドポイントの確認
Slack連携に必要となるエンドポイントを確認します。  
[API] -> [ForSlack]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/eab6c180215723426ced1cfca5dbd90d.png)
すでに作成されているエンドポイントのパスを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/60e20536b5d7c5721084705328bc387b.png)

上記の場合、`/rcms-api/3/event` をコピーしておいてください。

一旦ここまででKurocoの登録完了です。

## Slackアプリのインストール方法

Slackアプリの作成からBot User OAuth Tokenの取得、Kurocoへの設定までは共通手順です。  
[SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)を参照して実施してください。

KurocoWorkflowでは、共通手順の「Appを作成する」で貼り付けるAppマニフェストに以下を使用します。

```YAML
_metadata:
  major_version: 1
  minor_version: 1
display_information:
  name: KurocoWorkflow
features:
  bot_user:
    display_name: KurocoWorkflow
    always_online: true
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - channels:history
      - chat:write
      - emoji:read
      - im:history
      - im:write
      - mpim:history
      - reactions:read
      - team:read
      - users:read
      - groups:history
      - groups:read
      - groups:write
settings:
  event_subscriptions:
    request_url: https://sample.a.kuroco.app/rcms-api/3/event
    bot_events:
      - app_mention
      - reaction_added
      - reaction_removed
  org_deploy_enabled: true
  socket_mode_enabled: false
  token_rotation_enabled: false
```

:::caution
上記コード内の `https://sample.a.kuroco.app/rcms-api/3/event`には、先ほどKurocoの管理画面でコピーした `APIドメイン/エンドポイント`を記載してください。
:::

### イベントの設定

共通手順の[AppをWorkspaceにインストール](/ja/docs/tutorials/create-slack-app-and-get-bot-token/#appをworkspaceにインストール)まで完了したら、イベントを設定します。左サイドバーより[Event Subsctriptions]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2fc2fe859983524ae8d3563c0f464b8e.png)

Request URLには、先ほど同様コピーした `APIドメイン/エンドポイント` を入力し、[Save Changes]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/faf5c51fb03ec1bd01b583149fea8fc2.png)

イベントの設定が完了したら、共通手順の[Bot User OAuth Tokenの取得](/ja/docs/tutorials/create-slack-app-and-get-bot-token/#bot-user-oauth-tokenの取得)以降を実施し、Kuroco管理画面にBot User OAuth Tokenを設定してください。

:::note
KurocoWorkflowはリマインドをDMで送信します。チャンネルへの投稿を行わない場合、共通手順の[Slackチャンネルへアプリの追加](/ja/docs/tutorials/create-slack-app-and-get-bot-token/#slackチャンネルへアプリの追加)は不要です。
:::

以上で設定完了です。

## 動作確認

それではSlackにて動作を確認します。対象のSlack Workspaceに移動し、@kurocoWorkflow と自分にメンションをつけてメッセージを投稿します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bc922b4b9e2c694b9086b22cfc560baa.png)
「👍」スタンプでリアクションしない場合、リマインダーが届きます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/48d68e847710404d89283d5fd4efdbb2.png)
## 運用
### 投稿の確認
Kurocoの管理画面[コンテンツ] -> [ワークフロー]より、投稿状況が確認できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/46a64395f7c20c9a88537ceaff569ecb.png)
### 絵文字管理
Kurocoの管理画面[コンテンツ] -> [マスタ] -> [アクション絵文字]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/adb19b4cfcde2df774a5c9f528f5e73a.png)
マスタ編集より、絵文字とアクションの管理ができます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9e631e1513c2c28f7107e0809ecc6d39.png)

現在は下記のように設定されています。

| action | アクション名 | emoji | 絵文字 | 説明 | 
| ---- | ---- | ---- | ---- |---- |
| canceled | キャンセルする | x | ❌ |ワークフローのメッセージ内に編集で記入するとキャンセルになります。|
| approved | 承認する | 1 | 👍 |ワークフローを承認します。メンションされた人が承認か拒否を全員すると完了します。|
| rejected|拒否する	| -1 | 👎 |ワークフローを拒否します。メンションされた人が承認か拒否を全員すると完了します。|
| asap|緊急	| fire | 🔥 |ワークフローのメッセージ内に編集で入れると緊急（1時間毎に通知）になります。|
| watch | ウォッチする | eyes | 👀 |ワークフローが完了になると通知がきます |

マスタはCSVのアップロードにより、編集可能です。  

:::info
[管理画面マニュアル -> マスタ](/ja/docs/management/master/)
:::

## 関連ドキュメント
- [SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)
- [Slack](/ja/docs/management/slack/)
- [サイト一覧](/ja/docs/management/site-list/)
- [マスタ](/ja/docs/management/master/)
- [お問い合わせの受信通知をSlackで送信する](/ja/docs/tutorials/send-slack-notification-after-a-form-has-been-submitted/)
