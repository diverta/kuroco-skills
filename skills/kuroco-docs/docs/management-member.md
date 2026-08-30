# Kurocoドキュメント: 管理画面 / メンバー管理

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 自動ログイントークン管理（`autologin-token-list`）
- 初期グループ設定（`default-group-settings`）
- グループ（`group`）
- グループダウンロード（`group-download`）
- グループアップロード（`group-upload`）
- メンバー（`member`）
- メンバー解析（`member-analysis`）
- メンバーダウンロード（`member-download`）
- メンバー招待（`member-invite`）
- メンバーアップロード（`member-upload`）
- メンバー詳細設定（`new-member-settings`）
- 仮メンバー（`pre-members`）
- 仮メンバーアップロード（`pre-members-upload`）
- 新規メンバー登録条件（`registration-conditions`）
- 期限付き一時メンバー（`temporary-member`）


---

# 自動ログイントークン管理

> 元ページ: `management/autologin-token-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/autologin-token-list/

自動ログイントークン管理では、Kurocoに作成された自動ログイトークン一覧の確認と削除ができます。

## 自動ログイントークン管理の確認方法
[メンバー管理] -> [メンバー]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンから[自動ログイントークン管理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5205ee06a1da5db2b01682447d279f52.png)

## 自動ログイントークン管理の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdbe11ee3d2cbfac6652d4fb1463f8ad.png)

|項目   |説明  |
| :--- | :--- |
|ログインIDを記憶|発行された自動ログイントークンのIDを表示します。|
|トークン|自動ログイントークンを表示します。|
|メンバー名|自動ログイントークンを発行したメンバー名を表示します。|
|作成日時|自動ログイントークンが作成された日時を表示します。|
|有効期限|自動ログイントークンの有効期限を表示します。|
|削除する|一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると選択した自動ログイントークンを削除します。|

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [ログインログ](/ja/docs/management/login-log-list/)
- [オートログインの有効期間について教えてください](/ja/docs/faq/what-is-the-validity-period-for-auto-logins/)
- [ログインの有効期限を設定することはできますか](/ja/docs/faq/can-i-set-a-login-expiration-date/)


---

# 初期グループ設定

> 元ページ: `management/default-group-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/default-group-settings/

ここでは新しいメンバーが登録されたときに所属するデフォルトのグループを設定をします。

## 初期グループ設定の確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[メンバー詳細設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b06bf51aab354b25af7e2d6dd18c0d2b.png)

新規メンバー登録設定のページからその他の設定の[登録されるメンバーの初期の所属グループを設定する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b12850deca4df795c6c817a7f5a848e.png)

## 初期グループ設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5e540ec44cdb18c240087eb245446f8.png)

|項目   |説明  |
| :--- | :--- |
|登録グループ|新しいメンバーが登録されたときに属するグループを選択します。|
|現在の権限を表示する|クリックすると選択したグループの組み合わせで得られる権限を表示します。|

## ボタンの説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/43c89a790b06d62b2d3355f7e0cf8305.png)

[更新する]のボタンをクリックすると、初期グループ設定の変更内容が反映されます。

## 関連ドキュメント
- [メンバー詳細設定](/ja/docs/management/new-member-settings/)
- [グループ](/ja/docs/management/group/)
- [新規メンバー登録条件](/ja/docs/management/registration-conditions/)
- [メンバー登録時にドメインによって所属グループを変更する](/ja/docs/tutorials/change-the-default-group-for-member-registration-depending-on-the-domain/)
- [新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)


---

# グループ

> 元ページ: `management/group` ｜ 公式ページ: https://kuroco.app/ja/docs/management/group/

グループではサイトに登録されたグループの一覧の確認・追加・更新ができます。

## グループ一覧
### 確認方法
[メンバー管理] -> [グループ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e9822efe79c74da6b654f354bd93b52.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/83587b0ba90f0dd81f9626d635334444.jpg)

|項目   |説明  |
| :--- | :--- |
|検索する|キーワードを入力してグループを検索することができます。<br/>[詳細検索]をクリックすると詳細な条件を設定して検索ができる画面が開きます。|
|ダウンロードする|登録されているメンバー情報をダウンロードします。|
|有効|グループの状況を確認することができます。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/b694c4ccce526c6c6bfeeb4fe1321933.png)：有効<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/596dca297d70a23752963a320f7a4e93.png)：無効||
|ID|グループIDを表示します。グループ追加時に自動で採番します。|
|名前|基本設定で設定した名前が表示されます。|
|メンバー管理|メンバー登録画面で、そのグループに属するメンバーを変更することができます。|
|ユーザー種別|グループのユーザー種別（ログインユーザー、編集ユーザー、スーパーユーザー）が表示されます。|
|メンバー情報閲覧制限|メンバー情報の閲覧制限をグループ単位で設定することができます。|
|管理画面|基本設定で設定した管理画面（通常版、簡易版）が表示されます。|
|IPアドレス制限|基本設定で設定したIPアドレス制限が表示されます。<br/>`#コメント`の形式でメモを追加できます。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/57fdbe204e921845029a05804b4a74f6.jpg)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したグループに対して一括で処理を行います。

|項目|	説明|
|:--|:--|
|有効にする|	グループを有効にします。|
|無効にする|	グループを無効にします。|
|削除する|	グループを削除します。|

## グループ基本設定の編集
### 編集方法
[メンバー管理] -> [グループ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e9822efe79c74da6b654f354bd93b52.png)

グループ一覧ページから編集をしたいグループの[名前]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eba567dc20bd4741fe306faa519826cc.png)

### 基本設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f121c31b151453501bf358b64d470b49.png)

|項目   |説明  |
| :--- | :--- |
|名前|グループの名前を入力します。|
|有効|作成したグループを使用するときは「有効にする」にします。|
|ユーザー種別|グループの権限を選択します。<br/><strong>ログインユーザー：</strong><br/>ログインのみで管理画面の閲覧やコンテンツの編集ができません。<br/><strong>編集ユーザー：</strong><br/>管理画面の閲覧やコンテンツの編集を行います。また、詳細な権限を設定できます。<br/>APIや管理画面表化機能を利用した際にコンテンツ編集ユーザーに管理画面を利用させたくない場合は[管理画面利用不可]にチェックを入れてください。<br/><strong>スーパーユーザー：</strong><br/>スーパーユーザーは全ての権限が使用できます。|
|管理画面|簡易版を選択するとサイドメニューを非表示にするなど管理画面がシンプルになります。|
|IPアドレス制限|入力したIPアドレスからアクセスをした場合に、特定のグループ権限が付与されます。|

### 権限設定
ユーザー種別が編集ユーザーのときは、各機能毎の権限設定メニューが表示されます。[管理者]にチェックを入れるとスーパーユーザーと同等の権限が付与されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6082f9c5a31423da7f6034d9beb1ac88.png)

|項目   |説明  |
| :--- | :--- |
|閲覧|チェックを入れると、コンテンツや各種設定を閲覧することができます。|
|新規作成|チェックを入れると、コンテンツや各種設定を新規に追加することができます。|
|更新|チェックを入れると、コンテンツや各種設定を更新することができます。|
|削除|チェックを入れると、コンテンツや各種設定を削除することができます。|
|要承認|チェックを入れると、コンテンツや各種設定の作業に承認ワークフローの利用が必要になります。|

### 全ての機能を一括チェックしたい時
権限設定の上にある[一括チェック]のチェックボックスにチェックを入れると、各権限のチェックボックスにチェックが入ります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/027681c2c2b8fc15a29b52caccb0b079.png)

### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dea3cf4502ebbba1d32dc945fa27cad9.png)

|項目   |説明  |
| :--- | :--- |
|更新する|設定内容を保存します。|
|削除する|表示中のグループを削除します。|

## メンバー情報閲覧制限の編集
### 編集方法
グループ一覧ページから編集をしたいグループの[メンバー情報閲覧制限]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c20cc353c4192c2330a5c0670626c47.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f8b96560b7d22834aa192a621991ffae.png)

|項目   |説明  |
| :--- | :--- |
|基本方針|基本方針として、閲覧を[制限無し]か[制限有り]を選択します。|
|例外設定|基本方針で[制限有り]を選択した場合は、例外として許可するグループを選択することができます。|

### 各ボタン
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e9bc7896020162c0f75555c73794a371.png?witdh=600)

|項目   |説明  |
| :--- | :--- |
|更新する|設定内容を保存します。|

## 関連ドキュメント
- [グループを作成する](/ja/docs/tutorials/how-to-make-new-group/)
- [メンバー登録時にドメインによって所属グループを変更する](/ja/docs/tutorials/change-the-default-group-for-member-registration-depending-on-the-domain/)


---

# グループダウンロード

> 元ページ: `management/group-download` ｜ 公式ページ: https://kuroco.app/ja/docs/management/group-download/

グループダウンロードではグループの一覧をダウンロードできます。

## グループダウンロードの確認方法
[メンバー管理] -> [グループ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e9822efe79c74da6b654f354bd93b52.png)

ページタイトル「グループ一覧」の上の[グループ]をクリックし、表示されたプルダウンダウンメニューから、[ダウンロード]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c206279ee2693f310d1cc80510352ee2.png)

## グループダウンロードの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e46b8e24d37d34ef5e18aa244e4551a.png)

|項目  |説明  |
| :--- | :--- |
|文字コード|ダウンロードするファイルの文字コードを設定します。|
|[ダウンロード]ボタン|グループの一覧をダウンロードします。|

## 関連ドキュメント
- [グループ](/ja/docs/management/group/)
- [グループアップロード](/ja/docs/management/group-upload/)
- [メンバーダウンロード](/ja/docs/management/member-download/)


---

# グループアップロード

> 元ページ: `management/group-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/management/group-upload/

グループアップロードではCSVアップロードでグループの設定ができます。

## グループアップロードの確認方法
[メンバー管理] -> [グループ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e9822efe79c74da6b654f354bd93b52.png)

画面タイトルの上のドロップダウンメニューから[アップロード]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/11a3b29d3fd3f46d0d57568e9b0b706e.png)

## グループアップロードの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed96d2bf2943e517838c3dca7b60509e.png)

|項目  |説明  |
| :--- | :--- |
|ファイル設定(グループ)|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。<br/>[サンプルをダウンロード]をクリックするとアップロード形式を確認するためのサンプルファイルがダウンロードできます。|
|ファイル設定(メンバー)|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。<br/>[サンプルをダウンロード]をクリックするとアップロード形式を確認するためのサンプルファイルがダウンロードできます。|
|文字コード|アップロードするファイルの文字コードを設定します。|

### ファイル設定 (グループ)の挙動
- 新規追加：グループIDが空の場合は、新規追加になります。
- 更新：グループIDが存在している場合は、更新になります。
- 削除：グループIDを指定して、削除フラグに1を入れると、削除になります。

### ファイル設定 (メンバー)の挙動
- 追加：グループIDとメンバーIDを指定して、削除フラグに0を入れると、グループに所属するメンバーの追加になります。
- 削除：グループIDとメンバーIDを指定して、削除フラグに1を入れると、グループに所属するメンバーの削除になります。

## 関連ドキュメント
- [グループ](/ja/docs/management/group/)
- [グループダウンロード](/ja/docs/management/group-download/)
- [メンバーアップロード](/ja/docs/management/member-upload/)
- [社内ネットワークからアクセスした場合のみスーパーユーザーとなるグループを作成する](/ja/docs/tutorials/how-to-make-new-group/)


---

# メンバー

> 元ページ: `management/member` ｜ 公式ページ: https://kuroco.app/ja/docs/management/member/

メンバーではサイトに登録されたメンバーの一覧の確認・追加・更新ができます。

## メンバー一覧
### 確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

### 詳細検索
[詳細検索]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a15b1865236dd1756d41830ee9c19d4f.png)

絞り込み条件を作成できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d106da88c8847b4674571972d0153299.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dc154c74bdac375cada3d7a93c69d36f.png)

|項目   |説明  |
| :--- | :--- |
|検索する|キーワードを入力してメンバーを検索することができます。<br/>[詳細検索]をクリックすると詳細な条件を設定して検索ができる画面が開きます。|
|ダウンロードする|登録されているメンバー情報をダウンロードします。|
|ID|メンバーIDを表示します。メンバーIDはメンバー登録時に自動で採番されます。|
|ログイン許可フラグ|Kurocoへのログインを許可するか表示します。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6ba28f304045d08a896b276917750d1.jpg) ：許可する<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/ded341265dda92d33617efd4d4857cb2.png) ：許可しない|
|名前|メンバーの名前を表示します。|
|グループ|メンバーが所属するグループを表示します。|
|更新日時|メンバー情報が最後に更新された日時を表示します。|
|並び順|数値の大きい順に並びます。数値を入力し、画面下の[並び順を更新する]をクリックすると、並び順を変更できます。|

### 表示項目の追加方法
メンバー一覧右上の⚙️をクリックすると、表示項目設定が開き、メンバー一覧に表示する項目を追加できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7f1742255317441ac6f760b21773dd5.png)

|項目   |説明  |
| :--- | :--- |
|表示項目|ドラッグ&ドロップで表示項目の位置を変更できます。|
|選択|一覧に表示するリストから選択し追加できます。|
|キャンセル|設定変更をキャンセルされます。|
|適用する|設定変更を適用します。|


### 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/510ac56b6678b3682377e30645ec768c.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したメンバーに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|ログイン許可する|メンバーのログインを許可します。|
|ログインを無効にする|メンバーのログインを無効にします。|
|削除する|メンバーを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

## メンバー編集
### 編集方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

メンバー一覧ページから編集をしたいメンバーの[名前]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f21a50e37193e673a09a450f268d78dd.png)

### 項目説明
#### ID情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cab5e658b6d0cdf289f12f1ec5b38a0.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6f883fb6928dc38334cd246b0fbf961.png)


|項目   |説明  |
| :--- | :--- |
|メンバーID|メンバーのIDを表示します。|
|名前|名前を入力します。|
|メールアドレス|Eメールアドレスを入力します。|
|メルマガ拒否フラグ|メルマガ拒否フラグを設定します。<br/>[送信しない]にチェックを入れると、配信のあて先に追加されなくなります。|
|ログインID|ログインIDを入力します。<br/>利用可能な文字：`半角英数字`、`.`(コロン)、`_`(アンダーバー)、`-`(ハイフン)<br/>※コロンは最初と最後には利用できません。|
|ログインパスワード|パスワード変更にチェックを入れると、新しいパスワードの入力ができます。|
|ワンタイムパスワード|ワンタイムパスワードの設定状況を表示します。<br /> 項目が表示されない場合は、[環境設定]->[サイト管理]で有効化してください。|
|Passkey|Passkeyの設定状況を表示します。<br /> 項目が表示されない場合は、[環境設定]->[サイト管理]で有効化してください。|
|ログインの許可|ログインを許可するか設定します。|
|ログイン許可の有効期限|ログインを許可する有効期限を設定します。|
|代理ログイン許可|代理ログインを許可するメンバーIDを入力し、自分の代わりにログインできる人を設定できます。|
|所属グループ|所属するグループを設定します。|
|備考|備考を入力します。|
|並び順|並び順を入力します。<br/>数字の大きい順に並びます。|

#### プロフィール情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1776d15b8c64dc19022099461d0004c6.png)

|項目   |説明  |
| :--- | :--- |
|ニックネーム|ニックネームを入力します。|
|住所|住所を入力します。|
|電話番号|電話番号を入力します。|

:::tip
上記のほか、拡張項目で設定した内容は本項目に表示されます。
:::

#### 配信
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9d12ad2c2c49eb7506b75a70dc75661b.jpg)

|項目   |説明  |
| :--- | :--- |
|ステータス|配信の運用中、休止中を確認が表示さます。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6ba28f304045d08a896b276917750d1.jpg) ：運用中<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/ded341265dda92d33617efd4d4857cb2.png) ：休止中|
|配信名|配信の名前が表示されます。|
|購読|メンバーが配信の購読者になるか設定ができます。|
|登録日時|メンバーが配信の購読者に登録した日時を表示します。|

#### 配送先情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/48f5c77b4c17da8cc4c9ab0c339c86af.png)

メンバーに設定された配送先情報が確認できます。

#### ポイント情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/021cabab3ee4bd8a6a1b6a235f40791e.png)

:::info
[ポイント情報]タブは、ECを利用している場合、またはサイト管理画面の[ECポイント機能](/ja/docs/management/site-settings/#メンバー)が有効な場合に表示されます。
:::

|項目   |説明  |
| :--- | :--- |
|合計ポイント|メンバーが獲得した合計のポイントを表示します。<br/>表示のみで、直接編集はできません。残高はポイント詳細への行追加、ポイント更新API、CSVアップロードなどで変動します。|
|ポイント詳細|メンバーが獲得したポイントの詳細を表示します。<br/>「残ポイント」列には確定付与分の未消費残が表示され、消費・失効の進み具合が確認できます。<br/>ポイントの設定はEC機能で設定可能です。|

ポイント詳細への行追加は、ステータスによって以下のように残高へ反映されます。

|追加する行のステータス|残高への反映|備考|
| :--- | :--- | :--- |
|確定 × 付与|即時加算|残ポイント付きのロットとして記録されます。|
|確定 × 消費|即時減算|残高不足の場合は保存前にエラーになり、メンバー情報を含めて保存されません。|
|仮|反映されない|確定バッチで確定日到来時に加算されます。|
|失効|反映されない|記録のみです。|

:::info
- 確定ステータスの行では、付与と消費を同じ行に同時に入力できません。
- 確定ステータスの既存の履歴行は編集・削除できません。既存行のステータスを確定へ変更することもできません。仮ポイントの確定は仮ポイント確定バッチで行われます。
:::

:::note
ポイントの変更はポイント履歴に記録され、メンバーの[更新履歴](#更新履歴)には記録されません。
ポイントの仕様とAPIによる操作方法の詳細は[ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)を参照してください。
:::

#### タグ
![Image from Gyazo](https://t.gyazo.com/teams/diverta/df098919db53ad6588d61d0ccebaa5df.png)

メンバーに対するタグの設定ができます。

### 各ボタン/更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/94ae42443281a3a07c5eeff70c1d7bfb.png)

|項目   |説明  |
| :--- | :--- |
|更新する|メンバーの変更を反映します。|
|削除する|表示しているメンバーを削除します。|
|更新コメント|メンバーの情報を更新する際にコメントを残すことができます。|

### その他
#### 更新履歴
メンバー編集画面右上の[その他]から[更新履歴]をクリックすると、編集履歴が一覧で確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bea24d1ffb4e1efe84694ec457a1503b.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c7edc070b3afee5e0fd1f1da2e09dde2.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

#### 注文情報
メンバー編集画面右上の[その他]から[注文情報]をクリックするとEC機能のページに遷移し、対象ユーザーの注文情報が確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5e4bd99217e76ce7ec23a21da271563.png)

#### 定期購入情報
メンバー編集画面右上の[その他]から[定期購入情報]をクリックするとEC機能のページに遷移し、対象ユーザーの定期購入情報が確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d33e706d5ba03a32d2abbc13076ee1e.png)

#### ログイン履歴
メンバー編集画面右上の[その他]から[ログイン履歴]をクリックするとログイン履歴が一覧で確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/af3ecbbef1f53f047d8aa5583d5de1dc.png)

## 関連ドキュメント
- [メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)
- [メンバーを招待する](/ja/docs/tutorials/how-to-invite-new-member/)
- [メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)
- [一定期間ログインの無いメンバーへのリマインドおよび自動退会機能を実装する](/ja/docs/tutorials/implement-reminder-and-automatic-deletion-of-members/)
- [メンバー登録時にドメインによって所属グループを変更する](/ja/docs/tutorials/change-the-default-group-for-member-registration-depending-on-the-domain/)
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/)
- [管理画面からメンバー登録した際にメールでパスワードを通知できますか？](/ja/docs/faq/how-can-i-send-a-registration-email-with-pw-information/)


---

# メンバー解析

> 元ページ: `management/member-analysis` ｜ 公式ページ: https://kuroco.app/ja/docs/management/member-analysis/

メンバー解析ではメンバー数の情報や、メンバーの拡張項目に設定した選択肢の集計を確認できます。

## メンバー解析の確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンから[メンバー解析]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c7d5cc29edcf9682af1b2b7191a92a0c.png)

## メンバー解析の項目説明
### 全メンバー数
全メンバー数ではメンバーとして登録された人数の情報が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/947d5e3ceee8b4f92725d6fe85dba553.png)

|項目   |説明  |
| :--- | :--- |
|全メンバー数|現在登録されているメンバーの総数を表示します。|
|アクティブメンバー（１ヶ月以内にログイン）数|1ヶ月以内にログインをしたメンバーの数を表示します。|
|退会会員数|今までに退会したメンバーの数を表示します。|
|メール配信可能会員数|ID情報にE-mailが登録されているメンバーの数を表示します。|

### 拡張項目毎の集計
拡張項目の集計ではメンバーの[拡張項目設定](/ja/docs/management/extra-information/)で登録された選択肢の集計が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/93e6f67a71c2553aa81a884c2f1d14df.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c642be3c4c6f7237a0fdd48f04835452.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/17cb8b3abe4db001ef7ac1f50595081b.png)

|項目   |説明  |
| :--- | :--- |
|表示名|拡張項目設定で設定した表示名が表示されます。<br/>集計の対象は入力形態が以下のものになります。<ul><li>単一選択</li><li>単一選択(ラジオボタン)</li><li>複数選択(チェックボックス)</li></ul>|
|選択肢|拡張項目設定で設定した選択肢と、選択肢を未選択の場合にカウントされる「上記以外」が表示されます。|
|人数|選択肢を選んだメンバー数が表示されます。|
|パーセンテージ|選択肢を選んだメンバーの割合が表示されます。<br/>小数点以下は切り捨てられます。|

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [拡張項目設定](/ja/docs/management/extra-information/)
- [メンバーダウンロード](/ja/docs/management/member-download/)
- [メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)


---

# メンバーダウンロード

> 元ページ: `management/member-download` ｜ 公式ページ: https://kuroco.app/ja/docs/management/member-download/

メンバーダウンロードでは、メンバー情報のダウンロードを行えます。

## メンバーダウンロードの確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd4faa382f9528a0e0be5ce2fbbff577.png)

[ダウンロードする]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e9d22472534c7f522a5319f596f6bd8.png)

## メンバーの一覧のダウンロード
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a10cbf101f26326c2315ba49222a1139.png)

|項目   |説明  |
| :--- | :--- |
|適用中のフィルター|詳細検索で絞り込み条件を作成している場合に、その内容が表示されます。|
|生成されるCSVの行数|ダウンロードされるデータの件数が表示されます。|
|文字コード|ダウンロードする文字コードを指定します。|
|出力パターン|ランダムに設定するとメンバー全体から選択した件数のメンバーをランダムに抽出してダウンロードできます。|
|出力する列を選択する|クリックすると、列名一覧が表示されます。出力したい列を選択します。|
|キャンセル|モーダルを閉じます。|
|CSVをダウンロードする|設定した内容でメンバーの一覧をダウンロードします。|
|ファイルダウンロードする|メンバー拡張でファイルを設定している場合に、メンバー情報に登録したファイルをダウンロードすることができます。<br/>メンバーに対してファイルを設定する方法は[ファイルについて](#ファイルについて)を参照してください。|

#### ファイルについて

メンバープロフィールにファイルを追加するには、メンバー-拡張項目設定画面で、入力タイプに「ファイル」を選択して新規項目を作成します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bd2a63ec1792eed6a79b41436e7e534a.png)
次に、該当するメンバーエディターの[プロフィール情報]タブで、アップロードしたいファイルを選択します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0d1e7195b10fcdb5604957653f2e7a58.jpg)
ファイルの設定方法については、以下のドキュメントを参照してください。
- [拡張項目設定](/ja/docs/management/extra-information/)
- [メンバー - メンバーの編集](/ja/docs/management/member/#メンバーの編集)

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [メンバーアップロード](/ja/docs/management/member-upload/)
- [拡張項目設定](/ja/docs/management/extra-information/)
- [カスタムメンバーフィルター](/ja/docs/management/custom-member-filter/)


---

# メンバー招待

> 元ページ: `management/member-invite` ｜ 公式ページ: https://kuroco.app/ja/docs/management/member-invite/

サイトに新規メンバーを招待できます。

## 招待するの確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

メンバー一覧ページから[招待]ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7993356bfa1eff0509ae2b50c892712.png)

## 受信者のメールアドレスを入力
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d3ac22c35f16fa444400d7b028c9d3b.png)

|項目   |説明  |
| :--- | :--- |
|招待したい人のメールアドレスを入力してください。|招待を送るメールアドレスを入力します。<br/>複数のメールアドレスに送る場合は改行区切りで入力します。|
|登録グループ|招待されたメンバーが所属するグループを設定します。|
|有効期限|招待メールの有効期限が表示されます。<br/>実際は招待メールが送信されたタイミングから720分後になります。|
|次へボタン|[次へ]ボタンをクリックすると、招待状の作成画面に遷移します。|

## 招待状
![Image from Gyazo](https://t.gyazo.com/teams/diverta/48f38850eeb6988415e7e66a8e17c8e6.png)

|項目   |説明  |
| :--- | :--- |
|招待する人のMail Address|招待のメールを送るメールアドレスが表示されます。|
|招待する人の初期登録グループ|招待されたメンバーが所属するグループが表示されます。|
|あなたのお名前|招待をする方の名前を入力します。|
|メッセージ|招待メールに記載するメッセージを入力します。|
|送信するボタン|[送信する]ボタンをクリックすると作成した招待メールが送信されます。|

## 招待されている人一覧
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a33ee3fde50b8d7b92768adee2bad124.png)

|項目   |説明  |
| :--- | :--- |
|検索する|条件を設定して招待されたメンバーの検索ができます。|
|招待中のメールアドレス|招待されたメンバーのメールアドレスが表示されます。|
|会員登録のURL|招待のメールのURLが表示されます。|
|登録グループ|招待されたメンバーが所属するグループが表示されます。|
|招待した日時|招待した日時が表示されます。|
|有効期限|招待メールの有効期限が表示されます。|
|再送信|左端のチェックボックスにチェックを入れてクリックすると、招待メールの再送信をします。|
|削除する|左端のチェックボックスにチェックを入れてクリックすると、招待を削除します。|

## 関連ドキュメント
- [メンバーを招待する](/ja/docs/tutorials/how-to-invite-new-member/)


---

# メンバーアップロード

> 元ページ: `management/member-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/management/member-upload/

メンバーアップロードでは、メンバー情報の変更・新規追加・削除を一括で行うことができます。

## メンバーアップロードの確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[アップロード]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6915e2a1e6a1d4918be9fb4b6a887e4.png)

## メンバーアップロード
メンバーIDをキーにしてCSVでの一括アップロードができます。メンバーIDがないと新規追加扱いになります。削除フラグに1をセットすると削除できます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d9b8193de6ddf003da93a3b894c43c9.png)

|項目   |説明  |
| :--- | :--- |
|ファイル設定|アップロードするCSVファイルを選択します。<br/>[サンプルをダウンロード]をクリックするとCSVファイルのサンプルをダウンロードできます。|
|文字コード|CSVファイルの文字コードを設定します。|
|値がない場合の動作|値が無い場合の動作を設定します。<ul><li>パスワード設定: ランダムに生成するにチェックを入れると新規追加時にパスワードがランダムにセットされます。</li><li>メンバーIDがない場合にemailから設定する: メンバーIDをセットする代わりにメールアドレスをキーにして更新を行います。存在しないemailがセットされている場合には新規追加になります。</li><li>メンバーIDがない場合にログインIDから設定する: メンバーIDをセットする代わりにログインIDをキーにして更新を行います。存在しないログインIDがセットされている場合には新規追加になります。</li></ul>|
|登録グループ|CSVアップロードしたメンバーの登録されるグループを設定します。<br/>チェックが無い場合、新規追加では初期グループ設定のグループが登録され、更新では現在の設定のままとなります。|

### ボタンの説明
|項目   |説明  |
| :--- | :--- |
|[アップロードする]ボタン|設定したCSVファイルでメンバー情報を更新します。|
|[バッチ処理でアップロードする]ボタン|CSVアップロードによるメンバー情報更新をバッチ処理で実行します。件数が多い場合にはこちらをご利用ください。|

## ポイント（ec_point列）の上書き
CSVの `ec_point` 列でメンバーのポイント残高を上書きできます。残高が変わった場合は、差分がポイント履歴に記録されます（理由=「CSVで更新」）。bulk_upsert APIも同じ挙動です。

|CSVの内容|残高|ポイント履歴|
| :--- | :--- | :--- |
|`ec_point` 列があり、現在より大きい値|上書き|差分を付与として記録|
|`ec_point` 列があり、現在より小さい値|上書き|差分を消費として記録|
|`ec_point` 列があり、現在と同じ値|変化なし|記録されない|
|`ec_point` 列があり空欄 ＋ 空更新設定ON|クリア（空）|従来残高の全額を消費として記録|
|新規メンバーの行に `ec_point` あり|初期値として設定|初期残高を付与として記録|
|`ec_point` 列がない|一切変化しない|記録されない|

:::note
残高の上書き後にポイント履歴の記録に失敗した行がある場合は、「会員データは更新されましたが、ポイント履歴の記録に失敗しました。」というエラーが表示されます。この場合、該当行のメンバーデータ（残高の上書きを含む）自体は更新されています。
:::

:::note
ポイントの仕様（残高・履歴・失効）とAPIによる操作方法は[ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)を参照してください。
:::

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [メンバーダウンロード](/ja/docs/management/member-download/)
- [初期グループ設定](/ja/docs/management/default-group-settings/)
- [バッチ処理](/ja/docs/management/batch/)
- [メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)
- [ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)


---

# メンバー詳細設定

> 元ページ: `management/new-member-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/management/new-member-settings/

ここではメンバー登録時の設定を編集できます。

## メンバー詳細設定の確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[メンバー詳細設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/294893803a353377bcc644b58bde717c.png)

## 現在の設定
[設定を変更する]をクリックすると新規メンバーの登録条件を変更する画面に遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/04544f39c572c12ef364b1cda04e0896.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a76285d4b42a85845176fc3500cab600.png)

## その他の設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5290f5aa047d57e6e4929500d454126.png)

|項目   |説明  |
| :--- | :--- |
|登録されるメンバーの初期の所属グループを設定する|新しいメンバーが登録されたときに属するグループと、ログインの許可の設定をします。|
|登録されるメンバーの拡張項目を設定する|標準の項目以外の項目を登録したい場合に利用します。|

## メール通知
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1fc9a540c1443caafe5b5e963186b158.png)

|項目   |説明  |
| :--- | :--- |
|登録時送信アドレス|メンバー登録した場合の、通知・非通知を設定します。<br/>[通知する]をONにすると、メンバー登録があった際に枠内に登録したメールアドレス宛てに通知メールを配信します。|
|登録時ユーザー宛|ユーザー宛ての登録完了の通知、非通知を設定します。<br/>[通知する]をONにすると、新規メンバー登録を行ったユーザー宛てに、登録完了の通知メールを配信します。<br/>※Emailに登録がない場合は、通知されません。|
|編集時送信アドレス|既存メンバーの情報を編集した場合の、通知・非通知を設定します。<br/>[通知する]をONにすると、メンバー情報編集があった際に、枠内に登録したメールアドレス宛てに、通知メールを配信します。|
|編集時ユーザー宛|既存メンバーの情報を編集した場合の、ユーザー宛ての編集完了の通知、非通知を設定します。<br/>[通知する]をONにすると、メンバー情報編集を行ったユーザー宛てに、編集完了の通知メールを配信します。<br/>※Emailに登録がない場合は、通知されません。|

### メール通知の内容編集方法
通知するメールの内容は[オペレーション][メッセージひな形]から変更できます。

## ボタンの説明
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3187c9f3e1c61828cb37018018d679ae.png)  

[更新する]のボタンをクリックすると、新規メンバー登録設定の変更内容が反映されます。

## 関連ドキュメント
- [新規メンバー登録条件](/ja/docs/management/registration-conditions/)
- [初期グループ設定](/ja/docs/management/default-group-settings/)
- [拡張項目設定](/ja/docs/management/extra-information/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)


---

# 仮メンバー

> 元ページ: `management/pre-members` ｜ 公式ページ: https://kuroco.app/ja/docs/management/pre-members/

ここではサイトに登録された仮メンバーの一覧の確認・追加・更新ができます。

## 仮メンバー一覧
### 確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

メンバー一覧ページから[メンバー]をクリックし、表示されたプルダウンから[仮メンバー一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d10649491e3a189749f0fe88210c807c.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/71a5fff2b731d849c070884ef22af936.png)

|項目   |説明  |
| :--- | :--- |
|検索する|条件を設定して仮メンバーの検索ができます。|
|ダウンロードする|登録されている仮メンバー情報をダウンロードします。|
|ID|仮メンバーIDを表示します。仮メンバーIDは仮メンバー登録時に自動で採番されます。|
|メールアドレス|仮メンバーのメールアドレスを表示します。|
|Key|本登録ページで使用するKeyを表示します。Keyは仮メンバー登録時に自動で採番されます。|
|有効期限|仮メンバー登録が有効な期限を表示します。|
|登録日時|仮メンバーを登録した日時を表示します。|

### 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/131b53107d84b7debbfb0d6c07e83d88.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択した仮メンバーに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|削除する|仮メンバーを削除します。|

## 仮メンバーの編集
### 編集方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

メンバー一覧ページから[メンバー]をクリックし、表示されたプルダウンから[仮メンバー一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d10649491e3a189749f0fe88210c807c.png)

仮メンバー一覧のページから編集をしたい仮メンバーの[メールアドレス]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c392b79ff590bfdbbdcd00db3d53a9c1.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/edecb83842286ffc8251c9e7bde6d724.png)

|項目   |説明  |
| :--- | :--- |
|仮メンバーID|仮メンバーのIDを表示します。|
|メールアドレス|メールアドレスを入力します。ext_infoのemailのエイリアスです。|
|拡張情報|拡張情報を追加できます。本登録時にメンバー情報として復元するために使用します。下記の例のように記述します。<br/>例) `{"email":"example@example.com","provisional_name":"yamada taro","tel":"00-0000-0000","login_id":"example"}`
|key|本登録時に使用するKeyを表示します。|
|有効期限|仮メンバー登録が有効な期限を表示します。|
|登録日時|仮メンバーが仮登録した日時を表示します。|
|メンバーID|仮メンバーが本登録された時に採番されたメンバーIDを表示します。|

### 各ボタン/更新コメント
|項目   |説明  |
| :--- | :--- |
|更新する|仮メンバーの変更を反映します。|
|削除する|表示している仮メンバーの仮登録を取消します。|
|更新コメント|仮メンバーを更新する際にコメントを残すことができます。|

## 関連ドキュメント
- [仮メンバーアップロード](/ja/docs/management/pre-members-upload/)
- [メンバー](/ja/docs/management/member/)
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/)
- [新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)


---

# 仮メンバーアップロード

> 元ページ: `management/pre-members-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/management/pre-members-upload/

仮メンバーアップロードではcsvファイルをアップロードして、仮メンバーの情報を一括更新できます。

## 仮メンバーアップロードの確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[仮メンバー一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d10649491e3a189749f0fe88210c807c.png)

仮メンバー一覧のページから[アップロード]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0bc8cde9d206c4b7c131b4aa613f6b5.png)

## 仮メンバーアップロードの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8cea88b0b6955389cf49b79f6b0b9860.png)

|項目   |説明  |
| :--- | :--- |
|ファイル設定|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。<br/>CSVファイルの内容は[仮メンバーアップロードのCSVファイルについて](#仮メンバーアップロードのcsvファイルについて)をご確認ください。|
|アップロードする|アップロードしたCSVファイルの内容を反映します。|
|バッチ処理でアップロードする|アップロードしたCSVファイルの内容をバッチ処理で実行し、反映します。件数が多い場合にはこちらをご利用ください。|

## 仮メンバーアップロードのCSVファイルについて
仮メンバーアップロード用のCSVファイルは下記のように作成します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8b9a6af41673f15a001caa8055800b84.png)

|項目   |説明  |
| :--- | :--- |
|仮メンバーID|新規追加：仮メンバーIDが空の場合は、新規追加になります。<br/>更新：仮メンバーIDが存在している場合は、更新になります。|
|provisional_name|仮メンバーの名前になります。|
|E-mail|仮メンバーのE-mailになります。ext_infoのemailのエイリアスです。|
|有効期限|仮メンバーの有効期限になります。<br/>空の場合は登録から24時間後が有効期限として設定されます。|
|ext_info|ext_infoに登録したい内容は1行目に名前を入力し、各行に値を入力します。|

### 登録される内容
上記のCSVファイルをアップロードすると下記のように登録されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4688f04b6513cbcf3b458da92e82b9f1.png)

## 関連ドキュメント
- [仮メンバー](/ja/docs/management/pre-members/)
- [メンバーアップロード](/ja/docs/management/member-upload/)
- [メンバー](/ja/docs/management/member/)
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/)


---

# 新規メンバー登録条件

> 元ページ: `management/registration-conditions` ｜ 公式ページ: https://kuroco.app/ja/docs/management/registration-conditions/

新規メンバーの登録条件を設定・変更できます。

## 新規メンバー登録条件の確認方法
[メンバー管理] -> [メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f723805eaeba337a44d33e3dddf6b9b.png)

ページタイトル「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[メンバー詳細設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/986b98fd21b991665299956d631cf5cb.png)

新規メンバー登録設定のページから現在の設定の[設定を変更する]ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3f54b9b713a2be90b0d49b77e0e00d1.png)

## 新規メンバー登録条件の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75e99b63848ec9d8b9223820e365e6c9.png)

|項目   |説明  |
| :--- | :--- |
|新規登録は禁止。|管理画面のメンバー機能でのみメンバー登録できるようになります。<br/>※新規登録を禁止すると、招待中のメンバーも全員キャンセルされます。|
|メンバーに招待された人が新規登録できる。|招待された方がメンバー登録ができるようになります。メンバー全員が、他の人をメンバーに招待することができます。|
|特定のグループのメンバーに招待された人が新規登録できるようにする。|特定のグループのメンバーのみ、メンバー招待できるようになります。<br/>一部のグループのメンバーにのみ、他の人を招待する権利を付与することができます。 こちら選択した場合は、[設定する]ボタンをクリックしたあとに表示されるページで、招待することができるグループを選択します。|

## 設定するボタン
[設定する]のボタンをクリックすると、新規メンバー登録条件の変更内容が反映されます。  
[特定のグループのメンバーに招待された人が新規登録できるようにする]を選択した場合はグループ設定に遷移します。

### グループ設定
「特定のグループのメンバーに招待された人が新規登録できるようにする。」にチェックを入れて[設定する]をクリックした場合のみ、グループ設定の画面に遷移します。  
新規登録者を招待できるグループにチェックを入れて[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ab19c4ef30ed350fc345c4c2c040385.png)

### 更新するボタン
[更新する]のボタンをクリックすると、グループ設定の変更内容が反映されます。

## 関連ドキュメント
- [メンバー招待](/ja/docs/management/member-invite/)
- [メンバー詳細設定](/ja/docs/management/new-member-settings/)
- [メンバー](/ja/docs/management/member/)
- [サイト管理](/ja/docs/management/site-settings/)
- [メンバーを招待する](/ja/docs/tutorials/how-to-invite-new-member/)


---

# 期限付き一時メンバー

> 元ページ: `management/temporary-member` ｜ 公式ページ: https://kuroco.app/ja/docs/management/temporary-member/

期限付き一時メンバー一覧では、一定期間のみコンテンツの追加・編集などが可能となる、特別なアカウントの一覧を確認・追加・更新できます。

## 期限付き一時メンバー一覧
### 確認方法
[メンバー管理] -> [期限付き一時メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/563302f537b4f31bd11b6363ba9d4e16.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0ba88ee2fa16bd76c414ea8ccd5d651.png)

|項目   |説明  |
| :--- | :--- |
|検索する|条件を設定をして期限付き一時メンバーの検索ができます。|
|状態|期限付き一時メンバーの状態を確認できます。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：有効<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：無効|
|ログインID|ログインIDを表示します。ログインIDは権限追加時に自動で設定されます。|
|メールアドレス|設定した名前やメールアドレスを表示します。|
|有効期限|期限付き一時メンバーの有効期限を表示します。<br/>設定された日まで、権限は有効となります。|

## 期限付き一時メンバーの編集
### 編集方法
[メンバー管理] -> [期限付き一時メンバー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/563302f537b4f31bd11b6363ba9d4e16.png)

期限付き一時メンバー一覧のページから[ログインID]のリンクをクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9717b03d84e2de68e5e57e272cefad42.png)

### 項目説明
#### アカウント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b620f926c45358aab61e6ec7247aefa.png)

|項目   |説明  |
| :--- | :--- |
|ログインID|ログインIDを表示します。ログインIDは権限追加時に自動で設定されます。|
|パスワード|[表示する]をクリックするとパスワードが表示されます。<br/>再生成するにチェックを入れて更新するとパスワードが再生成されます。|
|メールアドレス|期限付き一時メンバーを送るメールアドレスを入力します。|
|名前|期限付き一時メンバーの名前を入力します。|
|有効期限|期限付き一時メンバーの有効期限を設定します。<br/>設定された日まで、権限は有効となります。|

#### リソース権限
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f717570227fb249b6e78999e5008999c.png)

|項目   |説明  |
| :--- | :--- |
|モジュール|与える権限に追加する機能を選択します。|
|アクション|与える権限ができるアクションを選択します。|
|要承認|チェックを入れると対象の行動に対して承認が必要になります。|
|言語|権限をどの言語に対して与えるか選択します。|
|対象|複数のコンテンツが登録されている場合は権限を与える対象を選択します。|
|削除|リソース権限を削除します。|
|追加|リソース権限を追加します。|

#### グループ権限
![Image from Gyazo](https://t.gyazo.com/teams/diverta/79564e990ec384e95666b484b4f6adbe.png)

|項目   |説明  |
| :--- | :--- |
|グループの選択|期限付き一時メンバーの所属するグループを設定します。|

#### メモ
![Image from Gyazo](https://t.gyazo.com/teams/diverta/79202a96c0a90b42b937a770766a4499.png)

期限付き一時メンバーに関してコメントを記入できます。

#### 各ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0549237fad1a26e473351135ac868f9.png)

|項目   |説明  |
| :--- | :--- |
|更新する|期限付き一時メンバーの変更を反映します。|
|削除する|表示している期限付き一時メンバーを削除します。|

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [グループ](/ja/docs/management/group/)
- [メンバー招待](/ja/docs/management/member-invite/)
