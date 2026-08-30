# Kurocoドキュメント: FAQ / password

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- パスワードの最大・最小文字数を変更できますか（`can-i-change-the-password-character-limits`）
- 過去のパスワードを利用できないようにする設定はできますか？（`can-i-disable-password-reuse`）
- ログインパスワードに有効期限を設定することはできますか？（`can-i-set-an-expiration-date-for-login-passwords`）
- メンバー管理のパスワードに利用できる文字を教えてください（`what-characters-are-allowed-in-passwords`）
- パスワードの確認方法を教えてください（`what-options-are-available-for-verifying-member-passwords`）


---

# パスワードの最大・最小文字数を変更できますか

> 元ページ: `faq/can-i-change-the-password-character-limits` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-password-character-limits/
> 概要: 環境設定 -> サイト管理の「パスワード最小文字数」「パスワード最大文字数」で変更できます。

[環境設定] -> [[サイト管理](/ja/docs/management/site-settings/)] の「パスワード最小文字数」「パスワード最大文字数」で変更できます。 
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/58588bc96427282e7d185abb79cc41ee.png?witdh=600)

## 関連ドキュメント
- [サイト管理](/ja/docs/management/site-settings/)
- [メンバー管理のパスワードに利用できる文字を教えてください](/ja/docs/faq/what-characters-are-allowed-in-passwords/)
- [過去のパスワードを利用できないようにする設定はできますか？](/ja/docs/faq/can-i-disable-password-reuse/)
- [ログインパスワードに有効期限を設定することはできますか？](/ja/docs/faq/can-i-set-an-expiration-date-for-login-passwords/)


---

# 過去のパスワードを利用できないようにする設定はできますか？

> 元ページ: `faq/can-i-disable-password-reuse` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-disable-password-reuse/
> 概要: 環境設定 -> サイト管理の「過去のパスワードは利用できない」に数字を入れることで、利用できない世代の設定ができます。

[環境設定] -> [サイト管理]の「過去のパスワードは利用できない」に数字を入れることで、利用できない世代の設定ができます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c6d535029856369d1916eaff5cf2ecc1.png)
## 入力する数字について
- 0：チェックしません。過去のパスワードも利用できます。
- 1：現在のパスワードと同じかをチェックします。現在のパスワードと同じパスワードが利用できなくなります。
- 2以上の数字：過去に遡ってチェックします。過去に利用したパスワードが利用できなくなります。

## 注意事項
スーパーユーザーの場合、パスワード変更はこの制限を受けません。

## 関連ドキュメント
- [サイト管理](/ja/docs/management/site-settings/)
- [パスワードの最大・最小文字数を変更できますか](/ja/docs/faq/can-i-change-the-password-character-limits/)
- [ログインパスワードに有効期限を設定することはできますか？](/ja/docs/faq/can-i-set-an-expiration-date-for-login-passwords/)
- [メンバー管理のパスワードに利用できる文字を教えてください](/ja/docs/faq/what-characters-are-allowed-in-passwords/)


---

# ログインパスワードに有効期限を設定することはできますか？

> 元ページ: `faq/can-i-set-an-expiration-date-for-login-passwords` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-an-expiration-date-for-login-passwords/
> 概要: ログインパスワードの有効期限は、[環境設定] -> [サイト管理]の「パスワードの有効期限日数設定」で設定できます。

ログインパスワードの有効期限は、[環境設定] -> [サイト管理]の「パスワードの有効期限日数設定」で設定できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/65bad1fd6892f5db58a10510495a16f5.png)
## 設定例
- 有効期限を10日にしたい場合：10
- 有効期限を無期限にしたい場合：0

デフォルトの状態では 0 が設定されています。

## 関連ドキュメント
- [サイト管理](/ja/docs/management/site-settings/)
- [ログインの有効期限を設定することはできますか](/ja/docs/faq/can-i-set-a-login-expiration-date/)
- [過去のパスワードを利用できないようにする設定はできますか？](/ja/docs/faq/can-i-disable-password-reuse/)
- [パスワードの最大・最小文字数を変更できますか](/ja/docs/faq/can-i-change-the-password-character-limits/)
- [メンバー管理のパスワードに利用できる文字を教えてください](/ja/docs/faq/what-characters-are-allowed-in-passwords/)


---

# メンバー管理のパスワードに利用できる文字を教えてください

> 元ページ: `faq/what-characters-are-allowed-in-passwords` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-characters-are-allowed-in-passwords/
> 概要: 半角文字の英語アルファベット、数字、記号をご利用になれます。下記の「利用可能な文字」をご参照ください。

半角文字の英語アルファベット、数字、記号をご利用になれます。下記の「利用可能な文字」をご参照ください。  

全角文字はご利用になれません。
 
## 利用可能な文字
### 英語アルファベット  
- abcdefghijklmnopqrstuvwxyz  
- ABCDEFGHIJKLMNOPQRSTUVWXYZ  

大文字小文字は区別されます。

### 数字
- 0123456789
 
### 記号
- `-`（ハイフン）  
- `_`（アンダーライン）  
- `&`（アンパサンド）  
- `=`（イコール）  
- `+`（プラス）  
- `%`（パーセント）  
- `#`（シャープ）  
- `@`（アットマーク）  
- `$`（ドル記号）  
- `*`（アスタリスク）  
- `.`（ピリオド）  
- `!`（感嘆符）  
- `:`（コロン）
- `<>`（不等号）
- `^`（キャレット）  
- `()`（丸括弧）  
- `~`（チルダ）  
- `;`（セミコロン）  

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [パスワードの最大・最小文字数を変更できますか](/ja/docs/faq/can-i-change-the-password-character-limits/)
- [メンバー管理のメールアドレスに利用できる文字とバリデーション仕様を教えてください](/ja/docs/faq/what-characters-can-be-used-as-email/)
- [過去のパスワードを利用できないようにする設定はできますか？](/ja/docs/faq/can-i-disable-password-reuse/)
- [ログインパスワードに有効期限を設定することはできますか？](/ja/docs/faq/can-i-set-an-expiration-date-for-login-passwords/)
- [パスワードの確認方法を教えてください](/ja/docs/faq/what-options-are-available-for-verifying-member-passwords/)


---

# パスワードの確認方法を教えてください

> 元ページ: `faq/what-options-are-available-for-verifying-member-passwords` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-options-are-available-for-verifying-member-passwords/
> 概要: パスワードについてはセキュリティ対応の一環として暗号化を行っているため、メンバ―編集ページ、メンバーダウンロードでダウンロードしたデータでは、暗号化されたデータについては確認ができないようになっております。

パスワードについてはセキュリティ対応の一環として暗号化を行っているため、メンバ―編集ページ、メンバーダウンロードでダウンロードしたデータでは、暗号化されたデータについては確認ができないようになっております。  

しかしながら、メンバー登録完了メールにパスワードを表示する方法がありますので、メンバー登録完了メールにパスワードを表示する方法を説明します。

## 登録完了メールにパスワードを記載する方法

### 前提条件
- メンバーをCSV一括処理で登録すること
- メンバー情報にメールアドレスがあること

### 対応方法
#### 1. 会員一覧ページへ遷移する
[メンバー管理] -> [メンバー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/58b97bba5bced2da8e2b6acec02d2076.png)

#### 2.一括処理ページへ遷移する
「メンバー」上のドロップダウンメニューから、[メンバーアップロード]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f9b3374cafa2296ac6d99bc5b18f1831.jpg)
#### 3. CSVファイルアップロード
[ファイル設定] でパスワード欄を空白にしたCSVファイルを選択します。
また、下記を選択します。
- 値がない場合の動作：「値なしで更新する」を選択します
- パスワード設定:「ランダムに生成する」にチェックを入れます

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b3272c0e7950ab156f6df4e5cd4918c3.png)

[アップロードする]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab6cefd50c43627d241f1560ddd8d04d.png)

以上でメンバーが一括で登録され、登録されたメンバー宛に、パスワードが記載されたメールへ送信されます。

:::tip
メンバー一括登録の方法は、[管理画面マニュアル -> メンバー -> メンバーアップロード](/ja/docs/management/member-upload/)をご確認ください。
:::

## その他、メンバーがパスワードを忘れた場合の対応方法例

上記CSVの対応が難しい場合は、下記内容をご確認ください。

### 管理者に問い合わせる
メールアドレスが登録されてないメンバーについては、管理者に問い合わせをしてください。
管理者もパスワードの確認はできませんが、パスワードの変更は可能ですので、パスワード変更を依頼してください。

パスワードの変更方法は、[管理画面マニュアル -> メンバー -> メンバーの編集](/ja/docs/management/member/#メンバーの編集)をご確認ください。

### 初回ログイン時にパスワード変更をさせる
ユーザー登録後、初回ログイン時にパスワードを変更させる方法もございます。以下対応方法を説明します。

[環境設定] -> [サイト管理] にアクセスします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5efa69b4b242cf054b66a3e21bc9350b.png)
[メンバー管理] -> [初回ログイン時にパスワード変更をさせる] にチェックを入れます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ad006cb785ad88b9c7ca8a12846523c4.png)
[更新する] をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9d97139b549028d8b55221949e44cce0.png)
以上で、ユーザー登録後、初回ログイン時にパスワードの変更を必須とします。

### リマインダーページを利用する
メールアドレスを登録しているメンバーでリマインダーページがある場合はリマインダページよりパスワードを再設定できます。  
詳細な設定方法は、[パスワードリマインダー/パスワードリセット](/ja/docs/tutorials/how-to-use-password-reminder/)を設定するをご参照ください。

## 関連ドキュメント
- [メンバーアップロード](/ja/docs/management/member-upload/)
- [メンバー](/ja/docs/management/member/)
- [パスワードリマインダー/パスワードリセットを設定する](/ja/docs/tutorials/how-to-use-password-reminder/)
- [管理画面からメンバー登録した際にメールでパスワードを通知できますか？](/ja/docs/faq/how-can-i-send-a-registration-email-with-pw-information/)
- [メンバー管理のパスワードに利用できる文字を教えてください](/ja/docs/faq/what-characters-are-allowed-in-passwords/)
