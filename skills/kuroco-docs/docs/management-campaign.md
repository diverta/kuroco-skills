# Kurocoドキュメント: 管理画面 / キャンペーン

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- フォームコピー（`form-copy`）
- フォーム項目設定（`form-field-settings`）
- 回答（`inquiry-answer`）
- フォーム基本設定（`inquiry-basic-settings`）
- フォーム一覧（`inquiry-forms`）
- レポート（`inquiry-report`）
- メール送信（`inquiry-send-mail`）
- 配信 基本設定（`notification-basic-settings`）
- 配信一覧（`notification-list`）
- 配信 メッセージ作成（`notification-message-editor`）
- 配信メッセージ（`notification-messages`）
- 配信 購読者一覧（`notification-subscribers`）
- IDaaS SP（`sso-idaas-sp`）
- OAuth Authorization Server（`sso-oauth-idp`）
- OAuth SP（`sso-oauth-sp`）
- SAML IdP（`sso-saml-idp`）
- SAML SP（`sso-saml-sp`）
- SCIM SP（`sso-scim-sp`）
- フォームテンプレート（`template`）


---

# フォームコピー

> 元ページ: `management/form-copy` ｜ 公式ページ: https://kuroco.app/ja/docs/management/form-copy/

フォームコピーでは、既に作成済みのフォームをコピーして新しいフォームを作成できます。

## フォームコピーの確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

コピーしたいフォームの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

フォーム基本設定画面右上の[コピー]をクリックすると、フォームをコピーして新しいフォームを作成できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dfa81d7e3626eb25a66c241c4fb5ec2f.png)

表示されたメッセージの[OK]ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7e307e9c5b2d7308e278763a1e273bff.png)

コピーされた新しいフォームの編集画面が開きます。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ce0277897953b5079d30f767a6a44bf.png)

コピー内容を確認し、必要に応じて編集後に[追加する]をクリックしてフォームを保存します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e6dd04b1573579bb8c51c4cc7daac093.png)

## 関連ドキュメント
- [フォーム一覧](/ja/docs/management/inquiry-forms/)
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)


---

# フォーム項目設定

> 元ページ: `management/form-field-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/form-field-settings/

フォーム項目設定ではフォームで入力する項目の設定ができます。

## フォーム項目設定の確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

編集したいフォームの[タイトル]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

フォーム基本設定ページからタブ[項目設定]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa0ffd92f013ba2aa6a3f396ceedd076.png)

## フォーム項目設定 項目説明

### フォーム内容

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f227e005e206149491933a9cfffad53.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7310ad8e1d905fb212c841065241715d.png)

| 項目 | 説明 |
| :--- | :--- |
|タイトル|フォームに表示するタイトルです。|
|必須属性|任意：入力（選択）しなくても、エラーになりません。<br/>必須：入力（選択）していないと、エラーを表示します。<br/>利用しない：フォームで、非表示にします。|
|回答形態／入力制限|回答形態を選択します。<br/>[設定]のリンクから選択項目、拡張子、入力項目等の設定ができます。<br/>※ 詳細な記述方法は次のセクションで説明します。
|並び順(大きい方が上)|項目の並び順を指定できます。数値の大きい順に並びます。|
|識別子|項目の識別子です。自動で設定されます。|
|クリア|該当する項目の設定をクリアします。|

### 回答形態の設定方法
[設定]のリンクをクリックすると、選択した回答形態に対応した入力ページが表示されます。  
例：改行なし短文（テキストボックス）、改行ありの長文（テキストエリア）  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/51ffb16fba04e123ce99bd5c9fe8516a.png)

例：単一選択(ラジオボタン)、単一選択(セレクトボックス)、複数選択(チェックボックス) 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/32d3064d2dab280af0b73de750ea869c.jpg)  

### 例：日付フォーマット

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f17a2431fbb9d224d5563f1a7c2e8eb0.png)

### 例：ファイル(KurocoFiles)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1deafbc04d468d64554a3c5cbce9696d.png)

### 例：マトリックス

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a08868b41a779f74fd54628d7c4fbb9.png)

### カテゴリ編集
フォームに表示する、カテゴリを設定します。  
「配信先」にメールアドレスを入力することで、フォームのカテゴリによる通知メールの配信先を変更できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/30968a09f470e18fe2a45552d9e5e701.png)

| 項目 | 説明 |
| :--- | :--- |
|ID|カテゴリを追加時に自動で採番されます。|
|カテゴリ|カテゴリ名を入力します。|
|配信先メールアドレス|カテゴリ毎に通知アドレスを設定します。複数のアドレスを設定する場合は、一つのアドレスを設定後に改行（Enterキー）して設定します。|
|並び順|数値が大きい順に並びます。|
|削除|チェックボックスにチェックを入れて、最下部の[更新する]をクリックするとカテゴリの削除ができます。|

## ボタンの説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6878a27ce14694241210d86994b1a7b.png)

| 項目 | 説明 |
| :--- | :--- |
| [更新する] ボタン | 設定内容を保存します。|
| [ダウンロードする] ボタン | CSV形式でデータをダウンロードします。 |

### アップロード
CSV形式のファイルをアップロードして、項目設定の内容を一括更新できます。  
CSVファイルの内容については[更新する]横の[ダウンロードする]ボタンからダウンロードしたファイルで確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/922142902f61e42b43307e0e9011d368.png)

### 項目設定更新履歴の確認
フォーム編集画面右上の[その他]をクリックし、[項目設定更新履歴]をクリックすると、項目設定の編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3580d6a2bae2b36377a7a1e656857680.png)

#### カテゴリ編集更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c8b4b52b11bf1514b783f01cf8c9aed.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [フォーム定義で利用できるフォーム項目一覧](/ja/docs/reference/form-field-list/)
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)


---

# 回答

> 元ページ: `management/inquiry-answer` ｜ 公式ページ: https://kuroco.app/ja/docs/management/inquiry-answer/

フォームから送信された回答の一覧の確認や、回答の返信ができます。

## 回答一覧
### 確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧ページから回答を確認したいフォームの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

[回答]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7de1e45648d9a6b4d093a798c177d393.png)

### 検索
回答一覧では簡易的なキーワードによる絞り込みと、詳細検索を用意しています。  

#### キーワードによる絞り込み
![Image from Gyazo](https://t.gyazo.com/teams/diverta/de655fe4aa47ebfd144eba9d03d07afc.png)

[キーワード] テキストボックスに検索するキーワードを入力します。送信者、送信者アドレス、本文のいずれかにキーワードが含まれる回答を絞り込みます。

#### 詳細検索
[詳細検索] ボタンをクリックすると、絞り込み条件を作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d4feba1c7e80b1ceaf0afd84f624ab78.png)

|項目   |説明  |
| :--- | :--- |
|表示件数|絞込み結果の1ページに表示する件数を設定できます。|  
|絞り込み条件作成|絞り込み条件を作成して、回答を絞り込むことができます。|
|並び順|　絞込み結果の表示順を設定できます。|  

### ダウンロード
回答の一覧をダウンロードできます。  
ダウンロードしたい回答を検索機能で絞込み、[ダウンロードする]をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff2f81711c148fbe0dc3a680605e364d.png)

ダウンロード設定が開き、複数の方法でダウンロードができます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6dcea76ddaa0070cd15aa6d8ad2b4392.png)

|項目   |説明  |
| :--- | :--- |
| 生成されるCSVの行数 | ダウンロードされるデータの件数が表示されます。 |
| 文字コード | ダウンロードする文字コードを指定します。 |
|出力する列を選択する|クリックすると、CSVに含む列を選択することができます。|
| キャンセル | モーダルを閉じます。 |
|CSVをダウンロードする|絞り込んだ回答をダウンロードします。|
|ファイルダウンロードする|回答をZIP形式でダウンロードします。|
|CSVのダウンロードリンクを生成する|バッチ処理で回答内容をダウンロードします。件数が多い場合にはこちらをご利用ください。<br/>処理が完了するとダウンロードリンクが表示されます。|

### 回答一覧
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7fdf49acfec366e895b6d6746d47c83.png)

|項目   |説明  |
| :--- | :--- |
|No.|回答番号を表示します。フォームからの回答受信時に自動で採番します。|
|ステータス|回答への対応状況を確認できます。<br/>状態は基本設定のステータス一覧で独自に設定できます。|
|カテゴリ|回答に設定されたカテゴリを表示します。|
|管理メモ|管理画面の回答内容画面の[管理メモ]で入力した内容を表示します。|
|受信日時|回答の受信日時を表示します。|
|送信者|項目設定の[名前]を使用した際、フォーム送信者の名前を表示します。|
|更新日時|回答内容の最終更新日時を表示します。|

#### 表示項目設定
回答一覧右上の歯車マークをクリックすると、表示項目設定が表示されます。  
表示項目設定ではフォーム項目設定で追加した項目を回答一覧に追加できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/95a32f2d58371d07b2c7f5e52b753729.png)

### 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbf15190243e62867c0d16385d067d57.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択した回答に対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|削除する|回答を削除します。|

## 回答内容の確認と返信
### 確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧ページから回答を確認したいフォームの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

[回答]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7de1e45648d9a6b4d093a798c177d393.png)

回答一覧の画面から表示したい回答の[No.]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/22773472f24f9e9d11a97220975cc49f.png)

### 項目説明
#### 受信形態 ： 送信メール
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffcb906bf112f7f26e8bcb80c6552d8e.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a86fec420342104471001307f74bffc2.png)

#### 受信形態 ： メール受信
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2696c9a400abb4ca3487ba9eba09b2dc.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/90dffb552cf0db5c06e6cc82d77e97a9.png)

|項目   |説明  |
| :--- | :--- |
| No. | フォームから送信された回答の番号を表示します。回答受信時に自動で採番します。 |
| 受信日時 | 回答の受信日時を表示します。|
| 送信日時 | 回答の送信日時を表示します。この項目は受信形態が「送信メール」の場合に表示されます。 |
| 受信形態 | 受信形態を表示します。 |
| ブラウザ・OS情報 | フォームを送信したブラウザ・OS情報を表示します。この項目は受信形態が「受信メール」の場合に表示されます。 |
| IPアドレス | フォームを送信したIPアドレスを表示します。この項目は受信形態が「受信メール」の場合に表示されます。 |
| お問い合わせの種類 | お問い合わせの種類を表示します。この項目は受信形態が「受信メール」の場合に表示されます。|
| 送信者 | 項目設定の[名前]を使用した際、フォーム送信者の名前を表示します。 |
| 送信者アドレス | 項目設定の[E-mail]を使用した際、フォーム送信者のメールアドレスを表示します。 |
| ボディ | 回答の本文を表示します。 |
| カテゴリ/件名 | カテゴリと件名を表示します。 |
| 管理メモ | 回答の内容に関してコメントを記入することができます。 |
| ステータス | 回答への対応状況を確認することができます。<br/>状態は基本設定のステータス一覧で独自に設定できます。 |
| 対応日付 | 対応した日付を設定できます。 |
| 回答の振り分け | メールをやり取りした際に、振り分けるフォームNoを入力します。 |

:::tip
上記に加えて基本設定で設定した項目が表示されます。
:::

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9eb6083e6d0642117284e8f3f0a429ac.png)

|項目   |説明  |
| :--- | :--- |
|更新する|回答内容の変更を反映します。|
|削除する|表示している回答を削除します。|

### 追加
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8ecb5425d7af04d01f0dddc7957ddd85.png)

|項目   |説明  |
| :--- | :--- |
|あて先|返信メールのあて先を設定します。<br/>問い合わせ者のメールアドレスがデフォルトで入力されています。|
|件名|件名を編集できます。件名にはフォームNo.が自動挿入されます。|
|テンプレート|事前に作成した定型文を挿入できます。|
|メッセージ|選択した回答のメッセージ部分を引用できます。|
|ボディ|ボディを入力します。|
|送信後のステータス|チェックを入れると、送信後にステータスを変更することができます。|

### メール送信ボタン
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/55bd7cf2c2bcbd15e72d2d910273073d.png?witdh=600)

入力した内容でメールの送信ができます。

### メール履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/39fcccb5021a3bade83357db4c885cb0.png)

|項目   |説明  |
| :--- | :--- |
|No.|メールの返信にもフォームNo.が付与されます。|
|送信日時|送信日時を表示します。|
|受信者|受信者のメールアドレスを表示します。|
|件名|件名を表示します。|
|ボディ|ボディを表示します。|
|ステータス|回答への対応状況を確認することができます。|

## 回答csvアップロード
### 確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧ページから回答を確認したいフォームの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

[回答]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7de1e45648d9a6b4d093a798c177d393.png)

[アップロード]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9cbc13a890951bb37fbab68f104bd5b.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e057060ab6d29e98445b34e727272fdb.png)

|項目   |説明  |
| :--- | :--- |
|文字コード|文字コードを設定します。|
|値がない場合の動作|[有効にする]にチェックを入れると、emailを元に回答の送信者と、登録済みのメンバーとの紐づけを行います。|
|ファイル設定|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。  CSVファイルのサンプルは回答一覧のページからダウンロードできます。|
|アップロードする|アップロードしたCSVファイルの内容を反映します。|

## 関連ドキュメント
- [フォームの回答を1ユーザー1回までにできますか？](/ja/docs/faq/how-to-limit-form-responses-to-once-per-user/)


---

# フォーム基本設定

> 元ページ: `management/inquiry-basic-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/inquiry-basic-settings/

フォームの基本設定の編集ができます。

## フォーム基本設定の確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧から編集したいフォームの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

## 基本設定項目一覧

<a><img src="https://t.gyazo.com/teams/diverta/98e42b23df35e86675ea06830950e407.png" style={{width: '500px', maxHeight: 'none'}} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/7cdd28e115441ae096440f124a58d232.png" style={{width: '500px', maxHeight: 'none'}} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/a10b11fa133870239ab3fddbf26c1272.png" style={{width: '500px', maxHeight: 'none'}} /></a>

|項目   |説明  |
| :--- | :--- |
|タイトル|フォームのタイトルです。|
|Slug|Slugを編集できます。|
|並び順|ここで設定されている数値の大きい順に、一覧に表示します。|
|説明|ユーザー閲覧側のフォーム一覧ページに表示される説明文です。|
|サンクス文言|フォームの送信完了後に表示されます。|
|フォーム完了タグ|フォームの送信完了後に表示されます。効果測定タグなどはこちらに設定してください。|
|お礼メール送信|フォームの送信があったとき、送信者へお礼メールを送信するかどうかを設定できます。<br/>[送信する]を選択すると、送信するメールのタイトルと内容を設定できます。|
|配信先メールアドレス|フォームの送信があったとき、ここで設定したアドレスに通知されます。<br/>複数のアドレスを設定する場合は、[追加する]ボタンから行を追加ください。<br/><ul><li>通知しない：フォームの送信があった場合でも、通知はありません。</li><li>通知する：フォームの送信があった旨の通知メールが送信されます。</li><li>入力内容全て通知：フォームの送信内容が全て通知されます。<br/>「管理者送信メールのZIPパスワード」を設定すると、フォームの送信内容が圧縮されてzipファイルで送信されます。個人情報を取得する場合は、パスワードの設定を推奨します。</li><li>タイトル：ここで設定したタイトルが、通知メールのタイトルになります。入力がない場合は、フォームのタイトルを表示します。</li></ul>通知メールの内容は[メッセージひな形](/ja/docs/management/email-template/)で編集可能です。|
|メール送信元（From）|フォームから送信されたメールに対する返信用のメールアドレスを設定します。この項目が空の場合、Emailは管理者メールで設定したメールアドレスから送信されます。|
|ステータス一覧|届いたメールに設定するステータスを編集できます。|
|データベースにフォームデータを残さない|データベースにデータを保存しない場合に有効にします。<br/>Kurocoに回答データが保存されなくなり、「回答」「メール送信」「レポート」タブは表示されません。また、回答ID（inquiry_bn_id）も発行されません。|
|自動ユーザ登録|チェックを入れて、登録時にセットされるグループを設定すると、フォームの送信者がユーザ登録されてい無い場合に、自動でユーザ登録します。|
|ステータス|<ul><li>「有効にする」にチェックあり：フォームを利用できます。</li><li>「有効にする」にチェックなし：フォームの利用ができず、一覧や入力欄は表示しません。</li></ul>|

## APIリクエスト制限
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0eda44ee317e55b28bb366c67dc64b04.png)

|項目   |説明  |
| :--- | :--- |
|APIリクエスト制限|APIリクエストを許可する範囲を選択します。複数選択可能です。<br/>この範囲は、カスタムメンバーフィルターで追加・編集できます。|

## 管理画面のアクセス制限
![Image from Gyazo](https://t.gyazo.com/teams/diverta/171369bd319cca343e40ce01bd972566.png)

|項目   |説明  |
| :--- | :--- |
|アクセス制限 - 基本設定|基本設定に対してアクセス制限を設定します。<br/>「制限有り」を選択すると、許可するグループを選択できます。|
|アクセス制限 - 項目設定|項目設定に対してアクセス制限を設定します。<br/>「制限有り」を選択すると、許可するグループを選択できます。|
|アクセス制限 - 回答|フォームから送信されたメールに対してアクセス制限を設定します。<br/>「制限有り」を選択すると、許可するグループを選択できます。|
|アクセス制限 - ダウンロード|ダウンロードに対してアクセス制限を設定します。|
|編集制限 - 回答|[制限無し]にすると、過去の回答の内容を編集できるようになります。|

## 承認ワークフロー設定
承認ワークフローの承認対象コンテンツにフォームを指定すると表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc2d84e4e598bb1af1bb21bdaf1b85bf.png)

|項目   |説明  |
| :--- | :--- |
|ワークフロー|承認ワークフローを選択します。|

:::info
承認ワークフローの設定方法については、[承認ワークフロー](/ja/docs/management/workflow/)を参照してください。
:::

## ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/961aef9c2f9e314bb674727c025083f9.png)

|項目   |説明  |
| :--- | :--- |
|[更新する]ボタン|設定内容を保存・更新します。|
|[削除する]ボタン|表示しているフォームを削除します。|

### 基本設定更新履歴の確認
フォーム編集画面右上の[その他]をクリックし、[基本設定更新履歴]をクリックすると、基本設定の編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/026daeccf113e06ab333e492d8006df8.png)

#### 基本設定更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/400c3dc9b58c99cb33c81093121f40f3.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [フォームの回答を送付したユーザー向けに配信メッセージを送付する](/ja/docs/tutorials/sending-notification-messages-to-users-who-submitted-form-responses/)
- [フォーム送信によりメンバー登録されるユーザーのメンバー情報にフォームの回答内容を設定する](/ja/docs/tutorials/how-to-implement-original-function-into-the-member-info-when-form-send-with-member-regist/)
- [フォームにリマインダー機能を追加する](/ja/docs/tutorials/add-reminder-function-to-form/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)


---

# フォーム一覧

> 元ページ: `management/inquiry-forms` ｜ 公式ページ: https://kuroco.app/ja/docs/management/inquiry-forms/

フォームの設定・返信管理ができます。

## フォーム一覧の確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

## フォーム一覧の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f15d8c8623f7dda8539036cbd1a5548.png)

|項目   |説明  |
| :--- | :--- |
|検索|条件を設定してフォームを検索できます。|
|ID|フォームのIDを表示します。|
|ステータス|フォームの運用状態をを表示します。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6ba28f304045d08a896b276917750d1.jpg)：有効<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/ded341265dda92d33617efd4d4857cb2.png)：無効|
|タイトル|フォームのタイトルを表示します。|
|デフォルト|フォームから送信されたメールのうち、ステータスがデフォルト状態のメールの数を表示します。|
|合計|フォームの送信された合計件数を表示します。|
|レポート|問い合わせに対するレポートへのリンクです。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|
|更新日時|フォームが最後に更新された日時を表示します。|

## 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2b9a1fb433cdec5209f1b60425850fa.png)

フォーム一覧の左端のチェックボックスにチェックを入れて、[有効にする][無効にする][削除する]のいずれかをクリックすると、選択したフォームに対して一括で処理を行います。

## 関連ドキュメント
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)


---

# レポート

> 元ページ: `management/inquiry-report` ｜ 公式ページ: https://kuroco.app/ja/docs/management/inquiry-report/

レポートではフォームで得た回答のレポートを確認できます。

## レポートの確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

レポートを確認したいフォームの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

フォーム基本設定ページからタブ[レポート]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0701013705d904606e2a28d96fd307c.png)

## レポートの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f145f81043d4660b7df126b44aebb53f.png)

| 項目 | 説明 |
| :--- | :--- |
|基本集計|回答数、回答者数を数値とグラフで表示します。|
|アンケート設問|下記の回答形態の項目に対する回答を数値、割合、グラフで表示します。<ul><li>単一選択(ラジオボタン)</li><li>単一選択(セレクトボックス)</li><li>単一選択(チェックボックス)</li><li>都道府県</li><li>マトリックス</li></ul>|

## 関連ドキュメント
- [回答](/ja/docs/management/inquiry-answer/)
- [フォーム一覧](/ja/docs/management/inquiry-forms/)
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)


---

# メール送信

> 元ページ: `management/inquiry-send-mail` ｜ 公式ページ: https://kuroco.app/ja/docs/management/inquiry-send-mail/

フォームの機能からメールを送信できます。  
送信したメールは、回答Noが割り当てられ、回答一覧から確認できます。

## 確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧ページからメール送信をしたいフォームの[タイトル]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f68fa638bc405db1a3425d539026cbd3.png)

[メール送信]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3247fdd259589600b67783d04b293e45.png)

## 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/af73ab00f6a53a6d0877eb3dd73705b1.png)

|項目   |説明  |
| :--- | :--- |
|あて先|返信メールのあて先を設定します。|
|件名|件名を編集できます。件名にはフォーム名が自動挿入されています。|
|テンプレート|事前に作成した定型文を挿入できます。|
|ボディ|メール本文を入力します。|
|送信後のステータス|送信後のステータスを設定します。|
|メール送信|クリックするとメールの送信を実行します。|

## 関連ドキュメント
- [回答](/ja/docs/management/inquiry-answer/)
- [フォーム一覧](/ja/docs/management/inquiry-forms/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [メールログ](/ja/docs/management/mail-log-list/)


---

# 配信 基本設定

> 元ページ: `management/notification-basic-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/notification-basic-settings/

配信の基本設定をします。

## 基本設定画面への遷移方法
### 既存の配信の場合
[チャネル] -> [一括配信] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

配信一覧画面のタイトルをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eeeb19a4f3bc92a330faf543750e91b.png)

### 新規の場合
[チャネル] -> [一括配信] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

配信一覧画面右上の「追加」ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ca4efaf3d98b1fbd89a5bad083478d5.png)

## 配信基本設定 項目説明

<a><img src="https://t.gyazo.com/teams/diverta/80dda9f9781fb58a7ec9a3f5512cd88e.png" style="width:600px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/c735596cc8549c42f9fdf5d2a44c445f.png" style="width:600px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/d1b77106ca4a688e67310a25ce56a1c3.png" style="width:600px; max-height:none;" /></a>

:::tip
「基本設定」「配信メッセージ」「購読者」等のタブは、配信追加後の画面に表示されます。（新規配信作成時の画面には表示されません）
:::

|  項目  |  説明  |
| :--- | :--- |
|  名前  |  配信名を登録します。  |
|  説明  |  配信についての説明を入力します。  |
|  ステータス  |  配信の運用状態をを表示します。  |
|  チャネル  |  配信の送信方法を選択します。 |
|  メール送信元（From） | メールの送信元(From)になるアドレスと送信者名を入力します。<br/>送信者名を入力しない場合は、配信名が適用されます。 |
|  トラッキング  | トラッキングの種別を選択します。<ul><li>トラッキング: 受信者が通知を開封したことを追跡します。</li><li>開封率: 通知の開封率を追跡します。</li></ul>  |
|  署名  | 配信の署名を登録できます。 |
|  購読登録通知メール  |  配信購読に登録した際に、登録者へ通知する・しないを選択します。 |
|  購読停止通知メール  |  配信の購読を解除した際に、登録者へメールを通知する・しないを選択します。 |
|  デフォルトのあて先 |  デフォルトのあて先を追加します。<br/><ul><li>あて先を設定する：あて先を選択してクリックすると、左欄へ追加できます。</li><li>新規あて先：クリックすると、カスタムメンバーフィルター一覧のページが開きます。</li></ul>|
|  基本設定へのアクセス制限  |  基本設定へのアクセス制限を設定します。  |
|  メッセージ送信制限 |  メッセージ送信制限を設定します。 |

## ボタンの説明
### 既存の配信
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b414268928b3e5cdf75023c3c2217d69.png)

|  項目  |  説明  |
| :--- | :--- |
|  [更新する]ボタン  |  設定内容を保存します。 |
|  [削除する]ボタン  |  表示している配信を削除します。 |

### 新規の配信
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dde2a5ecc0ace07bbbaa9c049103d2b9.png)

|  項目  |  説明  |
| :--- | :--- |
|  [追加する]ボタン  |  設定内容を保存します。 |

## 関連ドキュメント
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)
- [一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する](/ja/docs/tutorials/implement-reminder-and-automatic-deletion-of-members/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)


---

# 配信一覧

> 元ページ: `management/notification-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/notification-list/

既存の配信を一覧で確認できます。
## 配信一覧画面確認方法
[チャネル] -> [一括配信] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

## 配信一覧
![Image from Gyazo](https://t.gyazo.com/teams/diverta/056d92851ab5c14923f9be1229a4c08e.png)

|項目|説明|
|:---|:---|
|検索|配信内の送信方法で絞り込み検索ができます。|
|ID|配信のID。自動で付与されます。|
|ステータス|配信の運用状態をを表示します。|
|タイトル|配信のタイトル。クリックすると基本設定画面へ遷移します。|
|チャネル|配信の送信方法|
|送信待ち|送信待ちの件数を表示します。|
|送信済み|送信済みの件数を表示します。|
|下書き|下書き保存の件数を表示します。|
|購読者|購読者数を表示します。|
|メッセージ追加|クリックすると、メール作成画面へ遷移します。|

## 配信一括更新
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ce4b0f71440ea20dda90cf076c08b87.png)

一番左端のチェックボックスにチェックを入れて、「有効にする」「無効にする」「削除する」のいずれかをクリックすると、選択した配信に対して一括で処理を行います。

## 関連ドキュメント
- [配信 基本設定](/ja/docs/management/notification-basic-settings/)
- [配信メッセージ](/ja/docs/management/notification-messages/)
- [配信 メッセージ作成](/ja/docs/management/notification-message-editor/)
- [配信 購読者一覧](/ja/docs/management/notification-subscribers/)
- [トラッキング](/ja/docs/management/notification-tracking/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)


---

# 配信 メッセージ作成

> 元ページ: `management/notification-message-editor` ｜ 公式ページ: https://kuroco.app/ja/docs/management/notification-message-editor/

配信のメッセージ内容を作成します。

## メッセージ作成画面への遷移方法
[チャネル] -> [一括配信] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

配信一覧画面のタイトルをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eeeb19a4f3bc92a330faf543750e91b.png)

配信編集画面の[メッセージ]タブをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ce82cb4dc4e08594b098dddea5ddf96.png)

メッセージ一覧画面右上の「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0fb41db52d5f9fd4a6ee76f944c11654.png)

## 配信 メッセージ作成

<a><img src="https://t.gyazo.com/teams/diverta/fa75a35a230dda0044c72d8744ab855c.png" style="width:600px; max-height:none;" /></a>
<a><img src="https://t.gyazo.com/teams/diverta/baf9bed76054b6808b48a6546e7dd1cd.png" style="width:600px; max-height:none;" /></a>

|  項目  |  説明  |
| :--- | :--- |
|  ステータス  |  このメッセージの状態が表示されます。<br/>「編集中」「送信待ち」「送信済み」のいずれかが表示されます。  |
|  送信日時  |  メッセージの配信日時を設定することができます。<br/> メールは指定された時間になると、順次配信されます。 |
|  あて先  |  デフォルトで設定したあて先以外に配信したい場合には、こちらで選択してください。  |
|  件名  |  メッセージの件名を入力します。  |
| ボディ | <ul><li>メール形式<br/>メールの配信形式を「Textメール」「HTMLメール」から選択できます。<br/>ただし、基本設定の開封率にチェックがある場合はHTMLメールで固定されます。</li><li>本文<br/>メッセージの本文を入力します。Textメールの場合は、タグなどは使用できません。<br/>これまでに作成したテンプレートの適用も可能です。<br/>配信の宛先がメンバーに紐づいている場合、`%name1%` `%name2%`でメンバーの名前を差し込みできます。</li></ul>
|  ［送信待ちにする］  | 作成したメッセージを保存し、送信待機状態にします。<br/>送信日時の「すぐに送信」にチェックがあると、すぐ送信されます。  |
|  ［途中保存する］  | 作成したメッセージを途中保存します。途中保存されたメールは、送信日時を指定していても配信されません。  |
|  ［テンプレートとして保存する］  | 作成したメッセージを、テンプレートとして保存します。<br/> 作成したテンプレートは、本文欄の「テンプレート選択」から 選択・適用することができます。 |
|  テスト送信する  | 作成したメッセージの配信テストを行えます。<br/> テストメールを送りたい送信先アドレスを入力して、［テスト送信］をクリックするとテストメールが配信されます。 |

## 関連ドキュメント
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)


---

# 配信メッセージ

> 元ページ: `management/notification-messages` ｜ 公式ページ: https://kuroco.app/ja/docs/management/notification-messages/

配信したメッセージを確認できます。
## 配信メッセージ画面への遷移方法
[チャネル] -> [一括配信] をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

配信一覧画面のタイトルをクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eeeb19a4f3bc92a330faf543750e91b.png)

配信編集画面の[メッセージ]タブをクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ce82cb4dc4e08594b098dddea5ddf96.png)

## メッセージ一覧　項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/45eef4061649b53b3c7a7fde9e613ed0.png)

|  項目  |  説明  |
| :--- | :--- |
|  ID | メッセージ作成時に自動で採番されます。  |
|  件名  |  配信したメッセージの件名です。<br/>タイトルをクリックするとメッセージの内容を確認できます。<br/> 下書きのものは編集できます。 |
|  あて先  |  配信の配信先を表示します。<br/>「購読者」「あて先のタイトル」での表示になります。  |
|  送信数  |  送信数を表示します。  |
|  送信予定日時  |  送信予定日時を表示します。 |
|  送信開始日時  |  実際に送信を開始した日時です。 |
|  送信終了日時  |  実際に送信が終了した日時です。 |

## 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f17097fb24359189f5cb76f68f0eeaec.png)

メッセージ一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したメッセージを一括で削除します。

## 関連ドキュメント
- [配信 メッセージ作成](/ja/docs/management/notification-message-editor/)
- [配信一覧](/ja/docs/management/notification-list/)
- [トラッキング](/ja/docs/management/notification-tracking/)
- [配信 基本設定](/ja/docs/management/notification-basic-settings/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)


---

# 配信 購読者一覧

> 元ページ: `management/notification-subscribers` ｜ 公式ページ: https://kuroco.app/ja/docs/management/notification-subscribers/

配信するメールアドレスを設定します。
アドレスをひとつひとつ登録することも、CSVで一括登録（アップロード）も可能です。

## 購読者一覧画面への遷移方法
[チャネル] -> [一括配信] をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7e3e73f672e541124a780460b560ccc.png)

配信一覧画面のタイトルをクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eeeb19a4f3bc92a330faf543750e91b.png)

配信基本設定画面の「購読者」タブをクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfd6d16027ec5ee98f435bb67097ad8a.png)

## 配信購読者一覧　項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/890b5c7dbf92d3738c28c817d70a1544.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/993a38699062a8c319bf52ae17a6a2ea.png)

|  項目  |  説明  |
| :--- | :--- |
| メールアドレスで追加 | 購読者をメールアドレスで追加します。 |
| メンバーIDで追加 | 購読者をメンバーIDで追加します。 |
|  検索機能 | 【メンバー登録あり／メンバー登録あり／無選択】＋【メールアドレス】で、購読者を検索します。  |
|  メンバーID  |  購読者がユーザー画面から購読を登録した場合、もしくはCSVで一括登録した場合に、メンバーIDが表示されます。<br/>メンバーIDとメール アドレスが紐付けられていると、アドレスが変更された際に、自動で宛先も変更されます。  |
| キー | 購読者のキーが表示されます。 |
| 登録日時  | 購読を登録した日時が表示されます。|

## 一括処理
### 購読者削除
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f90246100099454f72588bad3166e8a.png)

購読者一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択した購読者を削除します。

### 購読者一覧CSVダウンロード
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2cc67d3bb422b8689c52c82fac10f57b.png)

購読者一覧画面右上の[その他]をクリックし、 [ダウンロード]をクリックすると、CSV形式で購読者一覧をダウンロードできます。

### 購読者一覧CSVアップロード
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c58ae044276702882e4723c8cd4b4b0d.png)

購読者一覧画面右上の[その他]をクリックし、 [アップロード]をクリックすると、購読者一覧のCSVアップロードページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6beb67fa58d387303d2134272f9caa65.png)

|  項目  |  説明  |
| :--- | :--- |
|アップロード種別|CSVのデータを追加するか、現在のデータと入れ替えるか選択します。|
|ファイル設定|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。|
|更新する|クリックすると購読者のCSVアップロードが実行されます|

## 関連ドキュメント
- [配信の購読者を登録する方法](/ja/docs/tutorials/how-to-register-subscribers-on-magazine/)
- [KurocoとNuxt.jsで配信購読者の登録・停止フォームを作成する](/ja/docs/tutorials/implement-a-magazine-subscription-unsubscription-form/)


---

# IDaaS SP

> 元ページ: `management/sso-idaas-sp` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sso-idaas-sp/

IDaaS SPではサイトに登録されたIDaaS SP設定の一覧の確認・追加・更新ができます。

## IDaaS SP一覧
### 確認方法
[外部システム連携] -> [ID連携] -> [IDaaS SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a0a44ca2391e0b85c3355fe1118ed30.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7be50dc9a915959aed80178b67481a3e.png)

|項目   |説明  |
| :--- | :--- |
|有効|IDaaS SPの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効|
|ログインIDaaS SP Name|IDaaS SPの名前を表示します。|
|タイプ|IDaaS SPのタイプを表示します。|
|更新日時|最終更新日時を表示します。|


## IDaaS SPの編集
### 編集方法
[外部システム連携] -> [ID連携] -> [IDaaS SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a0a44ca2391e0b85c3355fe1118ed30.png)

IDaaS SP一覧ページから編集をしたいIDaaS SP設定の[ログインIDaaS SP Name]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/743ae918236e79110270cd173c7ccdd3.png)

### 項目説明
#### SSO IDaaS SP編集
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3fb8e3f844eebb91076f587b3eb8a559.jpg)

|項目   |説明  |
| :--- | :--- |
|ログインIDaaS SP Name|IDaaS SPの名前を入力します。<br/>有効にチェックを入れると、現在の設定が有効になり、チェックを外すと、無効になります。 テスト機能は、IDaaS SPの設定が有効になっていない場合でも機能します。|
|ターゲットドメイン|ターゲットとなるドメインを選択します。<br/>管理画面：管理画面のURLがターゲットになります。<br/>API：APIドメインがターゲットになります。|
|タイプ|IDaaS機能で利用するサービス名。<br/>※現在はMicrosoft Entra External ID（旧 Azure AD B2C）のみ対応しています。|
|ログインURL|Azure側のProviderのRedirect/Reply URIとして設定するURL|
|クライアントID (Client ID)|マイクロソフトから取得したクライアントIDを入力します。|
|クライアントの秘密鍵 (Client Secret) |マイクロソフトから取得した秘密鍵を入力します。|
|承認URL|マイクロソフトから取得した承認URLを入力します。|
|トークンURL|ログインしているユーザーのToken情報を取得するためのURL<br/>詳しくは[Microsoft Entra External ID のトークンの概要](https://learn.microsoft.com/ja-jp/azure/active-directory-b2c/tokens-overview)を参照ください。|
|リソースURL|ユーザーのResourceのURLです。クロコとマイクロソフトの間でユーザーオブジェクトの情報を交換するために使用されます。|
|JWKS URI|キーセットを処理するためのURL。これは、設定時にマイクロソフトから取得します。|
| (API用) Grantトークン生成|セキュリティが動的アクセストークンに設定されたAPIの一覧が表示されます。SSOでGrantトークンを生成する場合、利用するAPIにチェックをいれてください。表示されたURLでSSOを実施するとリターンURLへの遷移時にgrant_tokenのパラメータがURLに追加されますので、これを利用してアクセストークンを発行してください。|
|リターンURL（成功）|ユーザーがログインに成功した際にリダイレクトするURLを設定します。<br/>入力がない場合は、TOPページに戻ります。|
|リターンURL（エラー）|ユーザーがログインに失敗した際にリダイレクトするURLを設定します。<br/>入力がない場合は、ログインページに戻ります。|
|自動ユーザ登録|有効にするにチェックを入れると、IDaaSログインをしたユーザーがメンバー登録されていない場合に、自動で登録します。<br/>「登録時にセットされるグループ」で自動で登録されたメンバーの所属するグループを設定します。|
|Emailを利用せずメンバー拡張項目にIDを格納してリンクする|チェックを入れると、メールアドレスではなく、IDを認証に利用します。<br/>チェックした場合は、open_idを格納するextカラムを選択し、チェックしない場合は、emailを参照するキーを入力します。<br/>データが入れ子になっており、それに応じて処理する必要がある場合は、サブキーの追加をクリックします。|
|ユーザーアクセストークンを保存|チェックを入れるとアクセストークンをKurocoのデータベースに保存し、後で使用できるようになります。|

#### トークンとリソースリクエストの設定
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/621518f49dd5ae8d1b96be21bc309b42.png)

|項目   |説明  |
| :--- | :---|
| IDPからのリソースキー | 必要な値を含む ID プロバイダのキー |
| メンバーの拡張項目とのマッピング | 受信データをマッピングするために選択する拡張項目。<br/>このデータは選択された拡張項目に保存されます。<br/>※マッピングとして設定できるのは、テキストの拡張項目のみです。 |
| Add a Subkey | 必要なデータがネストされている場合にサブキーを追加します。追加されたサブキーは、ネストしたオブジェクトからデータを取得するために使用します。<br/>※1つの親キーと3つのサブキーが使用できます|

#### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d41752b8e5b4ff0764e3524f1615936.png)

|項目   |説明  |
| :--- | :--- |
|更新する|入力した内容を反映します。|
|テスト|IDaaS SPのテストを実行し、どのフィールドに必要なデータが含まれているかを確認できます。<br/>保存されていないデータはテストできないため、テストを実行する前に、まず設定データを更新する必要があります。|
|削除する|IDaaS SPの設定を削除します。|

## 関連ドキュメント
- [IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)
- [OAuth SP](/ja/docs/management/sso-oauth-sp/)
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [SCIM SP](/ja/docs/management/sso-scim-sp/)
- [SPAでのSSO認証フローを実装する](/ja/docs/tutorials/implementing-sso-login-flow-in-spa/)


---

# OAuth Authorization Server

> 元ページ: `management/sso-oauth-idp` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sso-oauth-idp/

OAuth Authorization Serverでは、Kuroco自身をOAuth 2.0 / OpenID Connectの認可サーバー（Authorization Server）として動作させるための設定を管理できます。外部のOAuthクライアント（MCPクライアントを含む）に対して、認可コードやアクセストークンを発行できます。1つのOAuth Authorization Server設定に対して、複数のOAuth Authorization Serverクライアントを登録して利用します。

## OAuth Authorization Server一覧

### 確認方法

[外部システム連携] -> [ID連携] -> [OAuth Authorization Server]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f5570901df2a8daf4c5d69c66e89718f.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc6e8d7a86a70125ea23af526cd3e54c.png)

| 項目 | 説明 |
| :--- | :--- |
| 有効 | OAuth Authorization Serverの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効 |
| 名前 | OAuth Authorization Serverの名前を表示します。クリックすると編集画面に移動します。 |
| 用途 | この認可サーバーの用途（ターゲットドメイン）を表示します。`API` / `Management` / `AdminMCP` のいずれかです。 |
| OAuth Authorization Server クライアント | [クライアントを管理]をクリックすると、その認可サーバーに紐づくクライアントの一覧画面に移動します。 |
| 更新日時 | 最終更新日時を表示します。 |

一覧画面では、チェックボックスで選択した認可サーバーをまとめて有効化・無効化・削除できます。

## OAuth Authorization Serverの編集

### 編集方法

[外部システム連携] -> [OAuth Authorization Server]をクリックします。新規に作成する場合は、一覧画面右上の[追加]をクリックします。既存の設定を編集する場合は、一覧画面から編集したい認可サーバーの[名前]をクリックします。

![Image from Gyazo](https://i.gyazo.com/a57ad330c42bf7777227a2439f5dee70.png)

### 項目説明

#### OAuth Authorization Server編集

| 項目 | 説明 |
| :--- | :--- |
| 名前 | OAuth Authorization Serverの名前を入力します。（必須） |
| 用途 | この認可サーバーの用途を選択します。<br/>`API`：メンバー向けの認可サーバーです。<br/>`Management`：管理者向けの認可サーバーです。<br/>`AdminMCP`：Admin MCPリソース専用の管理者向け認可サーバーです。<br/>（必須）<br/>※用途は作成後には変更できません。編集画面では[変更不可]と表示されます。用途を変更すると、保存済みの許可スコープ・グラントタイプ・リソースの紐づけと不整合になるためです。 |
| Client ID Metadata Documents（CIMD） | 有効にすると、HTTPSのURLをclient_idとして受け付け、そのURLからクライアントメタデータを取得します。メタデータ（アプリ名等）はクライアント側の自己申告であり検証されません。同意画面ではURLが信頼の基準として表示されます。詳細は[Client ID Metadata Documents（CIMD）](#cimd)を参照してください。 |
| 対応するグラントタイプ | この認可サーバーが対応するOAuthグラントタイプをチェックで選択します（1つ以上必須）。<br/>`authorization_code`：認可コードフロー。<br/>`refresh_token`：リフレッシュトークンによる再発行。<br/>`client_credentials`：クライアント認証情報によるトークン発行。<br/>初期状態では`authorization_code`と`refresh_token`が選択されています。 |
| 許可するスコープ | この認可サーバーが発行を許可するスコープ（上限）をチェックで選択します。選択したスコープだけをクライアントに割り当て・トークンに付与できます。利用するスコープを必ず選択してください（未選択のままだとクライアントにスコープを割り当てられません）。選択できるスコープは用途によって異なります（[スコープ一覧](#スコープ一覧)を参照）。 |
| OAuth Authorization Server クライアント | [クライアントを管理]をクリックすると、この認可サーバーに紐づくクライアントの一覧画面に移動します。（保存済みの認可サーバーでのみ表示されます） |
| APIエンドポイント | この認可サーバーにMCPサーバーが紐づいているAPIエンドポイントの一覧を表示します。各APIをクリックするとAPIの編集画面に移動します。（用途が`API`かつ保存済みの認可サーバーでのみ表示されます） |
| アクセストークン有効期間 | アクセストークンの有効期間を秒単位で入力します（最小60秒）。初期値は3600秒です。 |
| リフレッシュトークン有効期間 | リフレッシュトークンの有効期間を秒単位で入力します（最小60秒）。初期値は2592000秒です。 |
| 認可コード有効期間 | 認可コードの有効期間を秒単位で入力します（最小10秒）。初期値は60秒です。 |
| 並び順 | 一覧での表示順を数値で入力します。 |
| 有効 | チェックを入れると、この設定が有効になります。 |
| ログインページURL | 用途が`API`の場合に、ログインに用いるページのパスを入力します（例: `/login/`）。（用途が`API`の場合は必須）<br/>用途が`Management` / `AdminMCP`の場合は、この項目は表示されず、管理画面のログインURLが固定で使用されます。 |
| 発行元 (Issuer) URL | この認可サーバーのIssuer URLを表示します（読み取り専用）。保存済みの認可サーバーでのみ表示されます。 |
| メタデータURL | この認可サーバーのメタデータ（Authorization Server Metadata）のURLを表示します（読み取り専用）。保存済みの認可サーバーでのみ表示されます。 |

#### 各ボタン

![Image from Gyazo](https://i.gyazo.com/97e3219d586476034bb4abb64ef025d9.png)

| 項目 | 説明 |
| :--- | :--- |
| 更新する | 入力した内容を保存します。 |
| 削除する | 表示しているOAuth Authorization Serverの設定を削除します。 |

### スコープ一覧

「許可するスコープ」で選択できるスコープは、用途（ターゲットドメイン）によって異なります。

| 用途 | 選択できるスコープ |
| :--- | :--- |
| `API` | サインイン用スコープ（`openid` / `profile` / `email`）と、API 読み取り（`api:read`）、API 書き込み（`api:write`） |
| `Management` | サインイン用スコープ（`openid` / `profile` / `email`）のみ |
| `AdminMCP` | サインイン用スコープと、Admin MCPの権限レベル |

#### Admin MCPの権限レベル

用途が`AdminMCP`の場合、Admin MCPの権限レベルを次から1つ選択します。

| 権限レベル | スコープ | 説明 |
| :--- | :--- | :--- |
| 読み取り専用 | `mcp:tools.read` | 読み取りツールを利用できます。 |
| 読み書き | `mcp:tools.read` + `mcp:tools.write` | 読み書きツールを利用できます。利用できる権限の上限はKuroco側で定義されており、[Admin MCP]画面の[mcp:tools.write が委譲する権限]で確認できます。 |
| 全操作（委譲先メンバーの権限の範囲） | `mcp:tools.all` | すべての操作を委譲しますが、トークンの委譲先として選択したメンバーの権限が上限になります。ただしグループ（権限）と汎用Smartyバッチの作成・変更・削除、OAuth認可サーバーの設定変更と発行済み認可の失効、メンバーへのスーパーユーザーグループの付与、特権付き静的トークンの発行はできません。どのメンバーでも承認できます。 |
| 全権限 | `mcp:admin` | トークン発行などすべての操作を含み、コンテンツ・モジュールの制限も無視されます。このレベルを承認できるのはスーパーユーザーのみです。それ以外のメンバーには同意画面で承認可能な範囲の最も広いレベルが提示され、そのレベルでトークンが発行されます。 |

いずれの権限レベルでも、トークンの実際の権限は「認証したメンバー自身の権限 ∩ そのレベルの上限」となり、メンバーが持っていない権限が付与されることはありません。

ツール一覧を取得するための`mcp:tools.list`は、いずれの権限レベルでも保存時に自動的に付与されます。

どのモジュール・コンテンツを操作できるかは、スコープではなくクライアントの[対象リソース]（Admin MCPのエンドポイントURL）で決まります。エンドポイントURLの形式は[MCP サーバ リファレンス](/ja/docs/reference/mcp-server/)を参照してください。

:::caution
用途が`Management`および`AdminMCP`の認可サーバーは、サイト内で有効にできるのは1つだけです。それぞれのリソースサーバーは、有効な設定を1つだけ解決するためです。（`API`は、MCPを有効にした各APIが個別に1つの認可サーバーに紐づくため、複数の有効な認可サーバーを持てます。）
:::

## OpenID Connect（サインイン情報の連携）

サインイン用スコープ（`openid` / `profile` / `email`）を付与すると、この認可サーバーはOpenID Connectの認可サーバーとして、メンバーのサインイン情報（claim）をクライアントに連携します。付与されたスコープに`openid`が含まれる場合にのみ、id_tokenの発行とuserinfoエンドポイントでのclaim取得が有効になります。id_token・userinfoエンドポイント・JWKSエンドポイントなどの詳細は[OAuth Authorization ServerのOpenID Connect対応](/ja/docs/reference/oauth-authorization-server-openid-connect/)を参照してください。

## OAuth Authorization Server クライアント

1つのOAuth Authorization Serverに対して、複数のクライアントを登録できます。クライアントは、OAuth Authorization ServerのクライアントID・シークレット・リダイレクトURI・スコープなどを保持します。

### OAuth Authorization Server クライアント一覧

#### 確認方法

OAuth Authorization Server一覧画面、またはOAuth Authorization Server編集画面から[クライアントを管理]をクリックします。

![Image from Gyazo](https://i.gyazo.com/7001670b63ed3a704f6fbd9b950db91f.png)

#### 項目説明

| 項目 | 説明 |
| :--- | :--- |
| 有効 | クライアントの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効 |
| クライアント名 | クライアントの名前を表示します。クリックすると編集画面に移動します。 |
| クライアントID | クライアントIDを表示します。 |
| トークンエンドポイント認証方式 | クライアントのトークンエンドポイント認証方式を表示します。 |
| 更新日時 | 最終更新日時を表示します。 |

### OAuth Authorization Server クライアントの編集

#### 編集方法

クライアント一覧画面右上の[追加]をクリックすると、新しいクライアントを作成できます。既存のクライアントを編集する場合は、一覧画面から[クライアント名]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bf1a961e864192d165de8b03d2d9f3c0.jpg)

#### 項目説明

| 項目 | 説明 |
| :--- | :--- |
| クライアント名 | クライアントの名前を入力します。（必須） |
| クライアントID | 保存後に発行されるクライアントIDを表示します（読み取り専用）。 |
| 有効 | チェックを入れると、このクライアントが有効になります。 |
| トークンエンドポイント認証方式 | クライアントの認証方式を選択します。（必須）<br/>`none`：パブリッククライアント（PKCEのみ）。<br/>`client_secret_basic`：Basic認証ヘッダーでクライアントシークレットを送信します。<br/>`client_secret_post`：リクエストボディでクライアントシークレットを送信します。 |
| クライアントシークレット | [保存時にクライアントシークレットを再生成する]にチェックを入れると、保存時に新しいシークレットを生成し、画面に1度だけ表示します。以前のシークレットは無効化されます。（既存クライアントの編集時のみ表示されます） |
| リダイレクトURI | 認可後にリダイレクトを許可するURIを、1行に1つ入力します。（必須）<br/>MCPクライアントの代表的なコールバックURLは次のとおりです。<br/>`https://claude.ai/api/mcp/auth_callback`<br/>`https://chatgpt.com/connector_platform_oauth_redirect` |
| 信頼済みクライアント <VersionLabel version="BETA" /> | 同一組織で管理するクライアントに対して、管理者による事前同意を設定します。有効にすると、ログイン済みユーザーには同意画面を表示せず、認可コードを発行します。クライアントの[対応するグラントタイプ]で`authorization_code`を選択した場合のみ設定できます。<br/>パブリッククライアント（トークンエンドポイント認証方式が`none`）の場合は、すべてのリダイレクトURIが`https`かつループバックアドレス以外のホストである必要があります。 |
| 対象リソース | このクライアントが接続するAdmin MCPのエンドポイントURLを指定します。（親の認可サーバーの用途が`AdminMCP`の場合は必須）<br/>MCPクライアントに設定するURLと完全に一致させてください。一致しない場合、発行したトークンは接続時に拒否されます。指定のないクライアントは名前空間内のどのエンドポイント（すべてのモジュールを含む）にも到達できるトークンを要求できてしまうため、グラント種別を問わずトークン発行を拒否します。 |
| サービスメンバーID | `client_credentials`でアクセストークンを発行するときに、トークンの主体として使用するメンバーIDです。保存時にトークン生成と同じ権限チェックを行います。（親の認可サーバーが`client_credentials`を許可している場合のみ表示されます） |
| 許可するスコープ | 左のタブで[対応するグラントタイプ]と各スコープグループを切り替えて設定します。<br/>[対応するグラントタイプ]では、このクライアントが利用するグラントタイプをチェックで選択します（1つ以上必須）。親の認可サーバーで無効化されているグラントタイプは、[認可サーバーレベルで無効化されています]と表示され選択できません。<br/>各スコープグループでは、このクライアントに割り当てるスコープを選択します。選択できるスコープは、親の認可サーバーの[許可するスコープ]で許可された範囲に限られます。 |

#### 信頼済みクライアントを設定する <VersionLabel version="BETA" /> {#信頼済みクライアントを設定する}

自社サービスなど、同一組織で管理するクライアントでSSOを利用する場合は、次のように設定します。

1. OAuth Authorization Server クライアントの編集画面を開きます。
2. [許可するスコープ]の[対応するグラントタイプ]で`authorization_code`を選択します。
3. [信頼済みクライアント]を有効にします。
4. [更新する]をクリックします。

この設定は、ユーザーごとの同意内容を保存するものではありません。管理者がクライアント単位で事前同意する設定です。認可リクエストと`prompt`による挙動は[SSOで利用する認可リクエスト](/ja/docs/reference/oauth-authorization-server-openid-connect/#ssoで利用する認可リクエスト)を参照してください。

:::caution
[信頼済みクライアント]は、自社・同一組織で管理するクライアントにのみ使用してください。第三者が管理するクライアントでは有効にしないでください。

この設定で省略されるのは同意画面です。リダイレクトURI、スコープ、リソース、PKCEなどの検証は通常どおり行われます。

同意画面を省略するため、認可サーバーは検証できる資格情報でクライアントを識別します。コンフィデンシャルクライアントはトークンエンドポイントでのクライアントシークレットにより識別されます。パブリッククライアントは登録済みのリダイレクトURIだけが識別材料になるため、ループバックURI（`http://localhost:3000/callback`など）や独自スキームのURIは利用できません。ユーザーの端末上の任意のアプリが認可コードを受け取れてしまうためです。管理下のホストの`https`リダイレクトURIを登録してください。
:::

保存後に新しいクライアントシークレットが生成された場合は、画面上部に次のメッセージとともにシークレットが表示されます。

> このクライアントシークレットは一度だけ表示されます。今すぐコピーして安全に保管してください — 後から取得することはできません。

![Image from Gyazo](https://i.gyazo.com/ad57ac1479af95eaf43161b9da395d03.png)

:::caution
クライアントシークレットは、保存時に1度だけ表示されます。後から取得することはできないため、表示された時点でコピーして安全に保管してください。
:::

:::caution
API/MCP用のクライアントには、アクセス権を持つスコープを1つ以上指定してください。サインイン用スコープ（`openid` など）のみではAPI/MCPを利用できません。
:::

## Client ID Metadata Documents（CIMD） {#cimd}

OAuth Authorization Serverの編集画面で[Client ID Metadata Documents（CIMD）]を有効にすると、クライアントを事前に登録していないアプリケーションでも、HTTPSのURLをclient_idとして提示して認可を要求できるようになります。KurocoはそのURLからクライアントメタデータ（アプリケーション名・リダイレクトURI・スコープなど）を取得し、その内容を一時的なクライアントとして扱います。取得した内容はクライアントとして保存されません。

接続先ごとにクライアント登録を行わないMCPクライアント（Claude Codeなど）は、この方式で接続します。

### CIMDで接続できる条件 {#cimd-requirements}

| 項目 | 条件 |
| :--- | :--- |
| client_id | パスを含むHTTPSのURLです（例: `https://example.com/oauth/client-metadata`）。オリジンのみのURL、`.`・`..`を含むパス、Kuroco自身のホストは受け付けません。 |
| トークンエンドポイント認証方式 | `none`（パブリッククライアント）のみです。クライアントシークレットを用いる方式を宣言したメタデータは受け付けません。 |
| グラントタイプ | `authorization_code`と`refresh_token`のみです。`client_credentials`は利用できません。 |
| リダイレクトURI | メタデータに1件以上必要です（最大10件、1件あたり最大512文字）。認可リクエストのリダイレクトURIは、登録済みクライアントと同様に完全一致で照合されます。 |
| スコープ | メタデータが宣言したスコープのうち、認可サーバーの[許可するスコープ]で許可されている範囲だけが有効です。 |

取得したメタデータは、メタデータ側のCache-Controlに従って5分〜24時間キャッシュされます（指定がない場合は1時間）。メタデータの内容を変更しても、キャッシュが切れるまでは反映されません。取得に失敗した場合や上記の条件を満たさない場合は、認可リクエストはエラーになります。

### 同意画面に表示される「このサイトに未登録のアプリケーション」 {#cimd-unregistered-application}

CIMDで接続したアプリケーションの同意画面には、[このサイトに未登録のアプリケーション]という警告が表示されます。これはアプリケーションが危険であることを示すものではなく、次の状態を示しています。

- このサイトの管理者が、このアプリケーションをOAuth Authorization Server クライアントとして登録していない
- 同意画面に表示されているアプリケーション名は、client_idのURLから取得したメタデータに書かれている自己申告の名前であり、サイト側での確認は行われていない

許可してよいかどうかは、アプリケーション名ではなく[提供元ドメイン]で判断してください。

| 同意画面の表示 | 説明 |
| :--- | :--- |
| 提供元ドメイン | client_idのURLのホストです。このアプリケーションについて確認できる唯一の情報であり、信頼の基準になります。 |
| クライアント情報の取得元URL（client_id） | アプリケーションが提示したclient_id（メタデータの取得元URL）です。 |

心当たりのないドメインが表示されている場合は、[拒否する]をクリックしてください。

### 警告を表示させないようにするには {#cimd-register-client}

アプリケーションを事前に登録したクライアントとして接続させると、この警告は表示されません。

1. [OAuth Authorization Server クライアント](#oauth-authorization-server-クライアント)の一覧画面から[追加]をクリックし、アプリケーション用のクライアントを作成します。パブリッククライアント（Claude Codeなど）の場合は、[トークンエンドポイント認証方式]に`none`を選択し、[リダイレクトURI]にアプリケーションのコールバックURLを入力します。
2. 保存すると[クライアントID]が発行されます。
3. 発行されたクライアントIDをアプリケーション側に設定して接続します（設定方法はアプリケーションによって異なります）。

登録済みのクライアントIDで接続した場合は、登録した内容が使用されるため、client_idのURLからのメタデータ取得は行われません。

未登録のアプリケーションからの接続自体を禁止する場合は、OAuth Authorization Serverの編集画面で[Client ID Metadata Documents（CIMD）]を無効にします。無効にすると、URLをclient_idとして提示したリクエストは受け付けられません。

:::caution
CIMDを有効にしている間は、事前登録なしにどのアプリケーションでも認可を要求できます。トークンが発行されるのは同意画面で[許可する]をクリックした場合のみですが、そのトークンに付与されうるスコープの上限は認可サーバーの[許可するスコープ]で決まります。必要なスコープだけを許可してください。
:::

## 注意点

- 用途（ターゲットドメイン）は認可サーバーの作成後には変更できません。用途を変更したい場合は、新しい認可サーバーを作成してください。
- `Management`および`AdminMCP`の認可サーバーは、サイト内で同時に有効にできるのは1つだけです。
- クライアントに割り当てられるスコープ・グラントタイプは、親の認可サーバーで許可された範囲が上限になります。認可サーバー側で許可していないスコープ・グラントタイプは、クライアント側で選択できません。
- クライアントシークレットは保存時に1度だけ表示され、後から取得することはできません。

## 関連ドキュメント

- [OAuth Authorization ServerのOpenID Connect対応](/ja/docs/reference/oauth-authorization-server-openid-connect/)
- [OAuth SP](/ja/docs/management/sso-oauth-sp/)
- [SAML IdP](/ja/docs/management/sso-saml-idp/)
- [OAuthを利用したシングルサインオンを利用できますか](/ja/docs/faq/can-I-use-single-sign-on-using-oauth/)


---

# OAuth SP

> 元ページ: `management/sso-oauth-sp` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sso-oauth-sp/

OAuth SPではサイトに登録されたOAuth SP設定の一覧の確認・追加・更新ができます。

## OAuth SP一覧
### 確認方法
[外部システム連携] -> [ID連携] -> [OAuth SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/73eb838e1113048df534ea34be2b9b34.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/97be099bb1544556a07e99dc5fcaae50.png)

|項目   |説明  |
| :--- | :--- |
|有効|OAuth SPの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効|
|OAuth SPの名称|OAuth SPの名前を表示します。|
|タイプ|OAuth SPのタイプを表示します。|
|更新日時|最終更新日時を表示します。|

## OAuth SPの編集
### 編集方法
[外部システム連携] -> [ID連携] -> [OAuth SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/73eb838e1113048df534ea34be2b9b34.png)

OAuth SP一覧ページから編集をしたいOAuth SP設定の[OAuth SPの名称]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/13258c79d1895c05f8f7131a6aab9851.png)

### 項目説明
#### OAuth SP編集
![Image from Gyazo](https://t.gyazo.com/teams/diverta/52b7e37c7c4451997fe1c335fc6d87ba.jpg)

|項目   |説明  |
| :--- | :--- |
|OAuth SPの名称|OAuth SPの名前を入力します。<br/>有効にチェックを入れると、現在の設定が有効になり、チェックを外すと、無効になります。 テスト機能は、OAuth SPの設定が有効になっていない場合でも機能します。|
|ターゲットドメイン|ターゲットとなるドメインを選択します。<br/>管理画面：管理画面のURLがターゲットになります。<br/>API：APIドメインがターゲットになります。|
|タイプ|OAuth SPでのログインを利用するサービスを選択します。<br/>Customを選択した場合は[追加の設定項目](#customを利用した場合の追加設定項目)が表示され、サービスプロバイダーが機能するための設定を直接入力することができます。|
|ログインURL|ユーザーがログインするために使用するURLを表示します。|
|クライアントID (Client ID) |アイデンティティプロバイダーで新しいOAuthアプリケーションを作成するときに取得する識別子、クライアントIDを入力します。 クライアントIDは大切に保管し、複数のサービスプロバイダーで同じクライアントIDを使用しないでください。|
|クライアントの秘密鍵 (Client Secret)|アイデンティティプロバイダーで新しいOAuthアプリケーションを作成するときに取得する秘密鍵を入力します。秘密鍵は大切に保管してください。|
| (API用) Grantトークン生成|セキュリティが動的アクセストークンに設定されたAPIの一覧が表示されます。SSOでGrantトークンを生成する場合、利用するAPIにチェックをいれてください。表示されたURLでSSOを実施するとリターンURLへの遷移時にgrant_tokenのパラメータがURLに追加されますので、これを利用してアクセストークンを発行してください。|
|プライベート URL を使用|[戻りURLのドメインにプライベートIPを許可する]にチェックを入れると、リターンURLに`http://IPアドレス`や、`http://localhost:3000/` などのURLが設定できるようになります。<br/>セキュリティ的に推奨されない設定なので、開発時のみご利用ください。|
|リターンURL（成功）|ユーザーがログインに成功した際にリダイレクトするURLを設定します。<br/>入力がない場合は、TOPページに戻ります。|
|リターンURL（エラー）|ユーザーがログインに失敗した際にリダイレクトするURLを設定します。<br/>入力がない場合は、TOPページに戻ります。|
|自動ユーザー登録|ユーザーの自動登録を許可するかどうかを設定します。チェックが入っていない場合、未登録ユーザーがSSOを利用してログインしようとすると、リターンURL（エラー）にリダイレクトされます。|
|Emailを利用せずメンバー拡張項目にIDを格納してリンクする|有効にするにチェックを入れると、アイデンティティプロバイダーから取得されるOpenIDを利用してユーザーを認識するようになります。<br/>OpenIDはメンバーの拡張項目(テキスト)に保存されます。<br/>ユーザーがログインできなくなる可能性があるため、後でこれを変更しないでください。|
|ユーザーアクセストークンを保存|チェックを入れると、ユーザーのアクセストークンがデータベースに保存され、後で使用できるようになります。 アイデンティティプロバイダーが提供する場合、リフレッシュトークンも保存されます。 トークンは、ユーザーがログインするたびに更新されます。|

#### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/44e64cd15f73db956dcfe7eebf4e2d16.png)

|項目   |説明  |
| :--- | :--- |
|更新する|入力した内容を反映します。|
|テスト|SSO OAuth SPのテストを実行し、どのフィールドに必要なデータが含まれているかを確認できます。<br/>保存されていないデータはテストできないため、テストを実行する前に、まず設定データを更新する必要があります。|
|削除する|OAuth SPの設定を削除します。|


### Customを利用した場合の追加設定項目
タイプの設定でCustomを選択すると、下記の項目が追加で表示され、サービスプロバイダーが機能するための設定を直接入力できます。設定の多くは、アイデンティティプロバイダーのドキュメントを確認し、取得する必要があります。  

#### SSO OAuth SP編集

|項目   |説明  |
| :--- | :--- |
|ログインURL(Use Path Parameter for spid.)|IdPによってはクエリパラメータでURLを返すことを許可していない場合があります。その場合は、このチェックボックスをオンにして、代わりにパスパラメータを使用できます。|
|承認URL|ユーザーがサインインするためにリダイレクトされるURLです。 アイデンティティプロバイダーから取得します。|
|トークンURL|コードに対してアクセストークンを取得するために使用されるURLです。 アイデンティティプロバイダーから取得します。|
|リソースURL|アクセストークンを使用してログイン資格情報を取得するために使用されるURLです。 アイデンティティプロバイダーから取得します。|
|必要なデータのスコープ|アイデンティティプロバイダーにリクエストするデータのスコープです。複数のスコープを設定することができます。|
|スコープセパレータ|複数のスコープをリクエストする場合は、スコープを結合するために使用されるセパレータを指定する必要があります。 この情報は、アイデンティティプロバイダーのドキュメントに記載されています。デフォルトではカンマ`,`が使用されますが、使用しているアイデンティティプロバイダーに応じて、リストから選択できます。|
|基本認証ヘッダーにクライアントの秘密鍵を送信|チェックを入れると、クライアント秘密鍵は基本認証ヘッダーで送られます。チェックを外している場合は、URLパラメータで送信されます。 この仕様は、アイデンティティプロバイダーのドキュメントに記載されています。 不明の場合はチェックを外してください。|
|承認プロンプトのパラメータを送信しない|チェック入れると、承認プロンプトクエリがリクエストで送信されなくなります。 この仕様は、アイデンティティプロバイダーのドキュメントに記載されています。不明の場合はチェックを外してください。|

#### トークンとリソースリクエストの設定
[設定する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0933fb812b2b3fe888357e6a0b34e431.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d3b8e783bb0c7646b5d48feaf9a83b7b.png)

|項目   |説明  |
| :--- | :--- |
|リクエストタイプ|アイデンティティプロバイダーに対して行われるリクエストのタイプを設定します。 デフォルト値は`GET`になります。 アイデンティティプロバイダーがPOSTリクエストを要求している場合は、こちらで変更ください。|
|ヘッダにアクセストークンを送信しない|チェックした場合は、アクセストークンを送信するためのパラメータを１つ以上指定する必要があります。|
|追加パラメータを送信|リクエストで送信されるパラメータのキーを設定します。 一部のアイデンティティプロバイダーでは、リクエストで追加のパラメーターを送信する必要がある場合があります|
|IDPからのリソースキー|アイデンティティプロバイダーからのレスポンスをマップするためのキーと、t_member_headerテーブルのうち、データをマッピングする列を設定します。|

## 関連ドキュメント
- [外部アカウントを使用したOAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)


---

# SAML IdP

> 元ページ: `management/sso-saml-idp` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sso-saml-idp/

SAML IdPではサイトに登録されたIDP設定の一覧の確認・追加・更新ができます。

## SAML IdP一覧
### 確認方法
[外部システム連携] -> [ID連携] -> [SAML IdP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/303daa2694d787fe12510c28037bd87c.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/25b4a42344fc174a6f9865cee3cddbdc.png)

| 項目  |　説明  |
| :--- | :--- |
|有効|IDPの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効|
|ログインSAML IdP Name|IDPの名前を表示します。|
|エンティティID|SAMLエンティティIDを表示します。|
|有効期間|IDPの有効期限を表示します。|
|更新日時|最終更新日時を表示します。|

## SAML IdPの編集
### 編集方法
[外部システム連携] -> [ID連携] -> [SAML IdP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/303daa2694d787fe12510c28037bd87c.png)

SAML IdP一覧ページから編集をしたいIDP設定の[ログインSAML IdP Name]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b32f003b86bc099f0f4843a238f225c.png)

### 項目説明
#### SAML IdP編集
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c4ce44267a107aa5183597a425d2527.jpg)

|項目   |説明  |
| :--- | :--- |
| ログイン SAML IdP Name | IDPの名前を設定できます。 |
| ログイン SAML IdP URI | SPからの認証リクエストを受け付けるURL。IDPのメタデータとして表示され、IDP URLとして、SP側で手動で設定できます。 |
| エンティティID | エンティティIDを設定できます。 |
| 暗号化アルゴリズム | データを暗号化するためのアルゴリズムを選択します。 |
| 有効期間 | IDPの有効期間を入力します。 |
| Name IDフォーマット | Name IDのフォーマットを選択できます。 |
| ログインIDを使用| チェックを入れるとログインIDを使用して連携が可能になります。 |
| 証明書 | データを暗号化するための証明書ファイルと証明書キーのセット。自動生成も可能です。<br /> ※デフォルトの証明書サイズは4096ビットです。2048ビットまたは8192ビットの長さの証明書が必要な場合は、「証明書を生成」ボタンの横にある下向き矢印から選択してください。 |
| SPメタデータファイル  | SPのXMLメタデータファイルです。<br/> ファイルアップロードする代わりに、[設定ファイルがありませんか？こちらをクリックしてください。] をクリックすることでテキスト形式で必要なSPデータを手入力することも可能です。<br/>*新規IDPを作成時に空白のままにもできますが、その場合はIDPは有効にしないでください。* |
| 属性マッピング | SAML属性として、ユーザーを区別するためのユーザーフィールドをマッピングできます。SAML認証を機能させるには少なくとも一つの識別子が必要です。 |

#### 詳細設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d8f0d9ab771fcaaa1543fb1acc3ab8c1.png)

|項目   |説明  |
| :--- | :--- |
| ログインURL | ログインページのURLを入力します。空欄の場合、ユーザーはフロントエンドドメインのトップにリダイレクトされます。フロントエンドドメインは[環境 > アカウント設定](/ja/docs/management/account/#アカウント設定の項目説明)で設定できます。この目的は、フロントエンドのロジックがログイン機能を処理できるようにすることです。<br/>※管理画面のログインを使用してリダイレクトしたい場合は、URLを次のように設定できます。<br/> `https://(site-key).g.kuroco-mng.app/management/login/login/?Return_URL=/direct/login/saml_idp_auth/?idpid=(IdP-ID)`<br/>　IdP IDは構成しているIdP IDに置き換えてください|
|IDP起点フローを許可|IDP起点フローを許可する場合はチェックを入れます。|
|Binding Method|Binding Methodを選択します。|

#### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/095e200ac2a82dcf561ddcceb5c36ed8.png)

|項目   |説明  |
| :--- | :--- |
|更新する|設定内容を保存します。|
|メタデータのダウンロード|表示しているIDPのメタデータをSAML2規準に則ったXML形式でダウンロードします。|
|削除する|表示しているIDP設定を削除します。|

## 補足

### AWS Cognito

AWS Cognitoでは、設定が2つの部分に分かれています。設定バインディングと実際のバインディングです。AWSは設定中にチェックを実行し、それらのチェックが通過した場合のみCognitoはSAML SSOメタデータの保存を許可します。

設定の一部では、AWSはIdP XMLを解析します。そのため、構成時にはバインディングメソッドを「REDIRECT」に設定する必要があります。バインディングメソッドは「詳細設定」にあります。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2212bcdcf566ba7ad9374afa847bdeca.png)

AWS側でXMLが更新されたら、その後でバインディングメソッドを「POST」に変更するとSSOが機能します。

## 関連ドキュメント
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [SAML認証を使用したシングルサインオンを利用できますか](/ja/docs/faq/can-I-use-single-sign-on-using-saml/)
- [Auth0を利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/)


---

# SAML SP

> 元ページ: `management/sso-saml-sp` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sso-saml-sp/

SAML SPではサイトに登録されたSP設定の一覧の確認・追加・更新ができます。

## SAML SP一覧
### 確認方法
[外部システム連携] -> [ID連携] -> [SAML SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/176a78956266a9e56c2b0304d681af33.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/805a4aa9136f75fea450f8f31ab9a0ed.png)

| 項目  |　説明  |
| :--- | :--- |
|有効|SAML SPの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効|
|ログインSAML SP Name|SPの名前を表示します。|
|エンティティID|SAMLエンティティIDを表示します。|
|有効期間|IDPの有効期限を表示します。|
|更新日時|最終更新日時を表示します。|

## SAML SPの編集
### 編集方法
[外部システム連携] -> [ID連携] -> [SAML SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/176a78956266a9e56c2b0304d681af33.png)

SAML SP一覧ページから編集をしたいSP設定の[ログインSAML SP Name]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b0bf0eeb20f560854a6f5041a9106f78.png)

### 項目説明
#### SAML SP編集
<a><img src="https://t.gyazo.com/teams/diverta/34d8cd42707f4ca1e96729096fd04611.png" style={{ width: 600, maxHeight: 'none' }} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/b427c861ae34b6ae3614870288463853.png" style={{ width: 600, maxHeight: 'none' }} /></a>

| 項目 |説明  |
| :--- | :--- |
| ログイン SAML SP Name | SPの名前を設定します。 |
|ターゲットドメイン|ターゲットとなるドメインを選択します。<br/>管理画面：管理画面のURLがターゲットになります。<br/>API：APIドメインがターゲットになります。|
| ログインSAML SP ACS URI | SP-Initiated SAML認証フローのスタートとなるURLを表示します。 |
| エンティティID | エンティティIDを設定します。 |
| IDP用XML設定ファイル  | IDPのSAML2規準に準拠したXMLファイルをインポートします。<br/>XMLファイルがない場合は、[設定ファイルがありませんか？こちらをクリックしてください。]をクリックし、必要な情報（IDP URL、IDPエンティティID、有効期間）を手入力することも可能です。<ul><li>証明書：証明書のファイルをアップロードします。</li><li>IDP URL：IDP URLを入力します。</li><li>IDPエンティティID：IDPエンティティIDを入力します。</li><li>有効期間：IDPの有効期限を入力します。</li></ul>|
| (API用) Grantトークン生成|セキュリティが動的アクセストークンに設定されたAPIの一覧が表示されます。SSOでGrantトークンを生成する場合、利用するAPIにチェックをいれてください。表示されたURLでSSOを実施するとリターンURLへの遷移時にgrant_tokenのパラメータがURLに追加されますので、これを利用してアクセストークンを発行してください。|
| ログインIDを使用 | ログインIDの使用を有効にするか無効にするかを選択できます。 |
|自動ユーザー登録|有効にするにチェックを入れると、SAMLログインをしたユーザーがメンバー登録されていない場合に、自動で登録します。<br/>「SAMLログイン時にメンバー情報の更新も行う」にチェックを入れると、既に登録済みのメンバーがSAMLログインした際に、IdPから連携されたメンバー情報で既存のメンバー情報を更新します。<br/>「登録時にセットされるグループ」で自動で登録されたメンバーの所属するグループを設定します。|
|プライベート URL を使用|[戻りURLのドメインにプライベートIPを許可する]にチェックを入れると、リターンURLに`http://IPアドレス`や、`http://localhost:3000/` などのURLが設定できるようになります。<br/>セキュリティ的に推奨されない設定なので、開発時のみご利用ください。|
|リクエスト時の戻り先URL指定|有効にすると、ログインSAML SP ACS URIのリクエストに`return_url`パラメータを付与することで、ログイン後の戻り先を動的に指定できます。<br/>例：`/direct/login/saml_login/?spid=1&return_url=%2Fmypage%2F`<br/>指定された値は同一ドメインまたは相対パスのみ許可されます（オープンリダイレクト対策）。不正な値が指定された場合は、下記の[リターンURL (成功)]の設定値にフォールバックします。<br/>SP-Initiatedフローのみで利用できます。|
|リターンURL (成功)|ユーザーがログインに成功した際にリダイレクトするURLを設定します。<br/>入力がない場合は、TOPページに戻ります。|
|リターンURL (エラー)|ユーザーがログインに失敗した際にリダイレクトするURLを設定します。<br/>入力がない場合は、ログインページに戻ります。|
|IDP起点フローを許可|IDP起点フローを許可する場合はチェックを入れます。|
|Binding Method|Binding Methodを選択します。|

#### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a086f8d50d055c502916bdeff20250f0.png)

|項目 |説明  |
| :--- | :--- |
|更新する|設定内容を保存します。|
|メタデータのダウンロード|表示しているSPのメタデータをSAML2規準に準拠したXML形式でダウンロードします。|
|削除する|表示しているSP設定を削除します。|

## 関連ドキュメント
- [Google Workspaceを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/)
- [Auth0を利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-auth0-to-implement-saml-based-sso/)
- [GMOトラスト・ログインを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gmo-trust-login-to-implement-saml-based-sso/)


---

# SCIM SP

> 元ページ: `management/sso-scim-sp` ｜ 公式ページ: https://kuroco.app/ja/docs/management/sso-scim-sp/

SCIM SPではサイトに登録されたSCIM SP設定の一覧の確認・追加・更新ができます。

## SCIM SP一覧
### 確認方法
[外部システム連携] -> [ID連携] -> [SCIM SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb7f32569b64579b5e066f6d7826945.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6ed381aca973dec6eebe78dc9a13879.png)

|項目   |説明  |
| :--- | :--- |
|有効|SCIM SPの有効状態を確認できます。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4b30584bb33c116421c1795f6bd0ceef.png)：有効<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9527261cd42b8bba3cb67821e783fa04.png)：無効|
|SCIM SP ID|自動で採番されるIDを表示します。|
|SCIM SP ID|SCIM SPの名前を表示します。|
|タイプ|SCIM SPのタイプを表示します。|
|更新日時|最終更新日時を表示します。|


## SCIM SPの編集
### 編集方法
[外部システム連携] -> [ID連携] -> [SCIM SP]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb7f32569b64579b5e066f6d7826945.png)

SCIM SP一覧ページから編集をしたいSCIM SP設定のIDもしくは名前をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/190c55dd36d3c939882bfc4a9684cf44.png)

### 項目説明
#### SSO SCIM SP編集
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a05a2b9aae60b6d44879c5aaec7c249a.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee3a5b77c3e1da58ca2dcb1f025bbb6f.png)

|項目   |説明  |
| :--- | :--- |
|有効にする|有効にチェックを入れると、現在の設定が有効になり、チェックを外すと、無効になります。（同時に有効にできる SCIM SP は1つだけです。）|
|名前|SCIM SPの名前を入力します。|
|SCIM SP Endpoint URI|SCIM IdP に設定する外部システムのエンドポイント URI|
|タイプ|SCIM機能で利用するサービス名。<br/>※現在はMicrosoft Entra IDのみ対応しています。|
|シークレットキー|マイクロソフトから取得した秘密鍵を入力します。|
|登録時にセットされるグループ|自動で登録されたメンバーの所属するグループを設定します。|
|Internal Key to Store External ID|外部システムの持つ独自のメンバーID形式やデータを保存する拡張項目を設定できます。（メールアドレス/name1/name2/ニックネームを含むテキストフィールドが指定できます）|
|Member attribute mapping|メンバー属性を外部システムにマッピングする設定です。（詳細は以下のセクションで説明します）|
|更新する|入力した内容を反映します。|
|削除する|SCIM SPの設定を削除します。|

#### Member attribute mapping

最大20個のメンバー属性を外部システムにマッピングできます。各行では、外部APIを通じて外部システムから渡されるデータを含む外部属性キーと、その値をKurocoに保存する列を指定する内部属性キー（現在はテキストフィールドのみ使用可能で、特別なユースケースとしてメールアドレスやname1/name2/ニックネームを含むことができます）を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff8aa74371e8fa355e8bcdd2d1f8d895.png)

##### 外部属性キー

外部属性キーは、テキストボックスに直接入力するほか、右側のプルダウン[-- スキーマから選択 --]から選択できます。プルダウンで属性を選択すると、左のテキストボックスにその属性キーが入力されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/630eb36b87e619b03a4c7f97bdc12918.png)

プルダウンには以下のグループが表示されます。

| グループ | 説明 |
| :-- | :-- |
| 共通属性 | [タイプ]で選択したサービスのSCIMスキーマ定義に含まれる基本的な属性を表示します。（`userName`、`displayName`、`active`、`externalId`、`name.givenName`、`name.familyName`など）<br/>メールアドレスは`emails[work].value`として表示され、選択すると`emails[type eq "work"].value`が入力されます。 |
| Microsoft EntraID 拡張属性 | enterprise拡張スキーマの属性を表示します。選択すると`urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:<属性名>`の形式で入力されます。 |
| 受信済みの属性 | IdPから実際に受信したプロビジョニングリクエストに含まれていた外部属性キーを表示します。 |

:::note
[共通属性]と[Microsoft EntraID 拡張属性]は[タイプ]で選択したスキーマ定義から生成されるため、[タイプ]が未選択の場合は表示されません。[受信済みの属性]は[タイプ]の選択状態に関わらず表示され、[共通属性]や[Microsoft EntraID 拡張属性]に同じ属性キーが表示されている場合は重複して表示されません。
:::

##### 受信済みの属性について

IdPが送信する属性は、IdP側の属性マッピング設定によって変わります。`onPremisesExtensionAttributes`（extensionAttribute1〜15）のようにIdP側で独自の拡張スキーマURNとして送信される属性は、[共通属性]や[Microsoft EntraID 拡張属性]には表示されません。[受信済みの属性]では、実際に受信した属性キー（外部属性キーと同じ表記。例：`userName`、`name.givenName`、拡張スキーマの場合は`urn:ietf:params:scim:schemas:extension:CustomExtensionName:2.0:User:tag`）をそのまま選択できます。

- 属性キーは、KurocoがIdPからプロビジョニングリクエスト（メンバーの作成・更新）を受信した時点で記録されます。そのため、初回のプロビジョニングが実行される前は表示されません。
- マッピングの対象外となる`schemas`、`meta`、`id`、`externalId`、`active`、`password`は記録されません。
- 記録される属性キーは、1つのSCIM SP設定につき最大100件です。上限を超えた分は記録されません。

## 関連ドキュメント
- [Microsoft Entra IDを使用してSCIMプロビジョニングを実装する](/ja/docs/tutorials/implementing-scim-provisioning-with-microsoft-entra-id/)
- [SAML SP](/ja/docs/management/sso-saml-sp/)
- [IDaaS SP](/ja/docs/management/sso-idaas-sp/)
- [グループ](/ja/docs/management/group/)


---

# フォームテンプレート

> 元ページ: `management/template` ｜ 公式ページ: https://kuroco.app/ja/docs/management/template/

フォームから送信されたメールに対して、返信する際などに使用する定型文の一覧を確認・追加・更新できます。

## フォームテンプレート一覧
### 確認方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧ページから[フォーム]をクリックし、表示されたプルダウンから[テンプレート設定]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f98bf8a59bac8a6a5294d90c7b4df59.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/da6b3d226b1a19f960b608f9780084cd.png)

|項目   |説明  |
| :--- | :--- |
|検索する|テンプレートのタイトルで検索をかけることができます。|
|テンプレートタイトル|テンプレートのタイトルを表示します。<br/>タイトルをクリックするとフォームテンプレート編集の画面へ遷移します。|
|更新日時|テンプレートが最後に更新された日時を表示します。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c7715df1cfa1071418b6ab6a7ff90fe.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したフォームテンプレートに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|削除する|フォームテンプレートを削除します。|

## フォームテンプレートの編集
### 編集方法
[チャネル] -> [WEB] -> [フォーム]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

フォーム一覧ページから[フォーム]をクリックし、表示されたプルダウンから[テンプレート設定]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f98bf8a59bac8a6a5294d90c7b4df59.png)

フォームテンプレート一覧ページから編集をしたいテンプレートの[テンプレートタイトル]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d97e24ac1cce952b134e451dbd0ce531.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b308afb9edc97a37648a00ab2a9b3dd.png)

|項目   |説明  |
| :--- | :--- |
|テンプレートタイトル|テンプレートのタイトルを設定します。|
|テンプレート(本文)|テンプレートの本文を設定します。|

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9bc7c4b56471f0c3060d5cf247f7eab3.png)

|項目   |説明  |
| :--- | :--- |
|更新する|テンプレートの変更内容を反映します。|
|削除する|表示しているテンプレートを削除します。|

## 関連ドキュメント
- [回答](/ja/docs/management/inquiry-answer/)
- [メール送信](/ja/docs/management/inquiry-send-mail/)
- [フォーム一覧](/ja/docs/management/inquiry-forms/)
- [メッセージひな形](/ja/docs/management/email-template/)
