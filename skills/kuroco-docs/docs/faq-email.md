# Kurocoドキュメント: FAQ / email

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- SendGridと連携後、メール内のURLが勝手に置換されてしまいます。直せますか？（`after-linking-with-sendgrid-url-in-email-is-replaced`）
- Kurocoから送信されるメールが迷惑メールになってしまいます。解決方法を教えてください。（`emails-sent-from-kuroco-are-going-to-spam-what-should-i-do`）
- メールが送信できない場合の確認方法を教えてください。（`how-do-i-fix-email-delivery-failure`）
- 問い合わせフォームに大量のスパムメールが届きます。対策はありませんか？（`how-do-i-reduce-spam-inquiries`）
- メンバー登録後メールが届きません。設定方法を教えてください。（`how-do-i-set-up-member-registration-confirmation-emails`）
- フォームのお礼メールが届かないときの確認箇所を教えてください（`i-did-not-receive-a-thankyou-email-what-do-i-do`）
- メール配信時の件数制限はありますか。（`is-there-a-limit-to-the-number-of-e-mails-i-can-send`）
- SendGridに残るログの保存場所・期間・内容について教えてください（`sendgrid-log-storage-retention-content-details`）
- メンバー管理のメールアドレスに利用できる文字とバリデーション仕様を教えてください（`what-characters-can-be-used-as-email`）


---

# SendGridと連携後、メール内のURLが勝手に置換されてしまいます。直せますか？

> 元ページ: `faq/after-linking-with-sendgrid-url-in-email-is-replaced` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/after-linking-with-sendgrid-url-in-email-is-replaced/
> 概要: SendGridの設定で、クリックトラッキングが有効になっていると、招待メール等に表示されるサイトURLが下記のような表示になる場合があります。解決するにはクリックトラッキングの解除をしてください。

SendGridの設定で、クリックトラッキングが有効になっていると、招待メール等に表示されるサイトURLが下記のような表示になる場合があります。

`https://u12345678.ct.sendgrid.net/ls/click?upn=c-2B・・・`  
※URLは上記のようになりますが、クリックすると想定のページに遷移できます。

解決するには、[チュートリアル -> SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)の「4. Click Trackingを無効にする」を参考にクリックトラッキングの解除をして動作をご確認ください。

:::info
[SendGrid -> メール本文内のURLが勝手に置換されてしまいます。解除できますか？](https://support.sendgrid.kke.co.jp/hc/ja/articles/206253421-%E3%83%A1%E3%83%BC%E3%83%AB%E6%9C%AC%E6%96%87%E5%86%85%E3%81%AEURL%E3%81%8C%E5%8B%9D%E6%89%8B%E3%81%AB%E7%BD%AE%E6%8F%9B%E3%81%95%E3%82%8C%E3%81%A6%E3%81%97%E3%81%BE%E3%81%84%E3%81%BE%E3%81%99-%E8%A7%A3%E9%99%A4%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%81%8B-)
:::

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [SendGridに残るログの保存場所・期間・内容について教えてください](/ja/docs/faq/sendgrid-log-storage-retention-content-details/)
- [メール送信の料金はSendGridと契約していても発生しますか？](/ja/docs/faq/do-i-have-to-pay-for-sending-emails-even-if-i-use-sendgrid/)


---

# Kurocoから送信されるメールが迷惑メールになってしまいます。解決方法を教えてください。

> 元ページ: `faq/emails-sent-from-kuroco-are-going-to-spam-what-should-i-do` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/emails-sent-from-kuroco-are-going-to-spam-what-should-i-do/
> 概要: Kurocoから送信されるメールが迷惑メールになる理由は複数考えられます。原因1. SPF/DKIMレコードが設定されていない。原因2. ネットワーク的問題以外でスパム判定されている。

Kurocoから送信されるメールが迷惑メールになる理由は複数考えられます。

## 原因1. SPF/DKIMレコードが設定されていない
Kurocoから送信されたメールが迷惑メールになる主な理由は、SPF/DKIMレコードが設定されていないことによるものです。  
KurocoはSendGridというメール送信サービスを利用しておりますので、こちらの設定をしていただく必要があります。
デフォルトでは、Kuroco側で用意しているSendGridを利用できますが、送信元メールアドレスが固定になります。

:::info
-[SendGridの設定箇所](/ja/docs/management/sendgrid/)  
-[How to set up domain authentication](https://docs.sendgrid.com/ui/account-and-settings/how-to-set-up-domain-authentication)  
-[SendGridからメール送信する場合のSPFとDKIMの認証の仕組み – 前編](https://sendgrid.kke.co.jp/blog/?p=10883)  
-[なりすましメール撲滅に向けたSPF（Sender Policy Framework）導入の手引き](https://www.ipa.go.jp/security/topics/20120523_spf.html) 
::: 

## 原因2. ネットワーク的問題以外でスパム判定されている
SPF/DKIMレコードが設定されているにも関わらず、迷惑メールになってしまう場合には、他の要因でスパム判定されている可能性があります。
その場合は、以下の作業が必要になります。
- メールの宛先を精査する
- メールの文面を見直す
メールの宛先が正しいか？また正式な手続きで取得されているメールアドレスか？メールの文面にスパム的な文言が含まれていないか？などをご確認ください。
メールの宛先を精査するのに、SendGridが提供しているBouncesをご利用いただくことができます。

:::info
-[迷惑メール判定を回避するには？](https://sendgrid.kke.co.jp/blog/?p=310)  
-[バウンス（メールの不達）を管理する](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/manage_bounces.html)  
-[Bounces](https://docs.sendgrid.com/ui/sending-email/bounces)  
:::

## 上記で解決しないときは
SPF/DKIMレコードが設定済みで、スパム判定される要因がメール宛先や文面に見つからない場合には、受信者側・送信者側の設定に起因している可能性があります。  
これらは弊社での調整はできませんので、お客様側でご確認・ご対応くださいますようお願いいたします。

### 迷惑メールになる可能性のある設定例（受信者側の設定）
以下の設定をされている場合は、受信可能なように設定を変更してお試しください。
- PCからのメールを受信しない
- HTMLメールを受信しない
- リンク付きメールを受信しない

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [メールが送信できない場合の確認方法を教えてください。](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)
- [メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？](/ja/docs/faq/can-i-use-my-custom-domain-for-the-sender-address/)
- [メール配信の際の送信元のメールアドレス「noreply@kuroco-mail.app」を変更できますか？](/ja/docs/faq/can-i-change-the-senders-email-address/)


---

# メールが送信できない場合の確認方法を教えてください。

> 元ページ: `faq/how-do-i-fix-email-delivery-failure` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-fix-email-delivery-failure/
> 概要: メールが送信できない場合に確認いただきたい点をまとめました。ご確認お願いいたします。

メールが送信できない場合、まずはKuroco管理画面の[オペレーション] -> [ログ管理] よりメールログのご確認をお願いします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/92e21fb3b1835226042ed75518afdaae.png)
:::info
参考：管理画面マニュアル -> [メールログ](/ja/docs/management/mail-log-list/)
:::

## メールログでエラーが表示されていない場合
メールログの画面にて、202 AcceptedとなっていればSendGridへの送信は成功しています。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f4c557eff8fe66be9f4713a44595198.png)
## SendGridログでsg_eventを確認する
sg_eventがdeliveredとなっている場合は、SendGridから送信先のメールサーバへの送信も成功しています。


エラーが表示されていないにも関わらずメールが届かない場合、下記ご確認ください。

### 相手先にメールが届かない
送信されたメールが相手先の迷惑メールフォルダに入っていないかをご確認ください。

### SendGridの管理画面で、Activityを確認したときに該当メールがDeferredになっている
SendGridの管理画面にログインしてActivityを確認してください。Kurocoからの送信は完了しているが、SendGridのメールサーバーから送信が出来ていない場合があります。  
該当するメールのステータスがDeliveredになっている場合はSendGridのメールサーバーからも送信完了しております。ステータスがDrops/Deferred/Bounces/Blocks/Spam Reportsなどになっているときは送信が出来ておりません。  
Deferredの場合は待っていると解消されることがありますが、エラーの詳細を確認して解消をしてみてください。  
例えば、独自のSendGridアカウントを利用している場合で、利用開始後すぐの場合は1時間辺りの送信数が制限されていることがあります。


:::info
参考：SendGrid：[Email Activity Feed](https://docs.sendgrid.com/ui/analytics-and-reporting/email-activity-feed)
:::

### SendGridのBouncesに登録がされてしまっている
メールアドレスが不正だったり、何らかの理由で相手先のメールサーバーから拒否されている場合などはSendGridのBouncesに送信メールアドレスが登録されてしまっている場合があります。  

Kurocoでのメール送信ログが成功しているのにメールが届かない場合はこのパターンになりますが、ほとんどがメールアドレスの登録間違いが原因になっております。 

Kuroco共通のSendGridを利用されている場合は、サポートまでご連絡いただければBouncesに登録されていないか確認をいたします。
独自のSendGridのアカウントをご利用の場合はSendGridの管理画面からご確認ください。

## メールログでエラーが表示されている場合

エラーが表示されている場合は、エラー内容をもとに対応をお願いいたします。
よくあるパターンとしては以下となります。

### SendGridの「管理者メール」フィールドが入力されていない
SendGridの「管理者メール」フィールドが入力されていないとエラーとなります。  
Kuroco管理画面より[チャネル] -> [メール] -> [SendGrid]ページ内の「管理者メール」フィールドにメールアドレスが入力されているかをご確認ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7118fcc12b57c044fef6638531e61663.png)
「管理者メール」フィールドには、下記いずれかのメールアドレスを入力ください。

- SendGridと連携している場合：連携済みのメールアドレス
- SendGridと連携していない場合：noreply@kuroco-mail.app

:::info
参考：チュートリアル：[SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
:::

### メッセージひな形の「本文」フィールドが入力されていない
送信されるメッセージひな形の「本文」フィールドが入力されていないとエラーになります。  
Kuroco管理画面より[オペレーション] -> [メッセージひな形]にて、対象のひな形のテンプレート名をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e8603e84557a4682b94ce81dbbd24f9.png)

編集画面より「本文」フィールドに値が入力されているかをご確認ください。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/270d2d12871c2c996fbe99c532a8396d.png)
### メッセージひな形の「宛先」が間違えている
メッセージひな形では独自に宛先を設定できます。宛先が間違えている場合エラーとなります。
Kuroco管理画面より[オペレーション] -> [メッセージひな形]にて、対象のひな形のテンプレート名をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e8603e84557a4682b94ce81dbbd24f9.png)

「独自設定」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eecb92cc1c8cd045fcf33440bbbb7a17.png)

独自設定のポップアップが表示されるので、「宛先」にメールアドレスが入力されている場合、お間違いないかご確認ください。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6d19396e12de1cfd91ab5654fbb80944.png?witdh=600)
## その他：エラーメール/メールの表示がおかしい等の不具合について
上記対応で解決しない場合、調査が必要になります。  
調査にはメールのヘッダ情報が必ず必要になりますので、以下の方法を参考にメールのヘッダ情報を取得した上で、[サポート事務局](https://www.diverta.co.jp/contact/)までご連絡ください。   
メールのヘッダ情報がない場合には、メールの調査等をお受けできない場合もありますので予めご了承ください。

### オリジナルヘッダの確認方法
**Gmailでオリジナルヘッダを確認する方法**
1. オリジナルヘッダを確認するメールを開く
2. 右上の「...」をクリック
3. 「メッセージのソースを表示」をクリック
4. 表示されるヘッダー全文をコピーする  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a3e7ec6b5ebd165c6e3c0bec956ad5a5.png)
その他メーラーでの確認方法については、Googleなどの検索エンジンで「オリジナルヘッダ メール 確認方法」などでお調べください。

### お問い合わせ時に必要な情報
オリジナルヘッダと併せて以下の情報をお送りいただくと、より迅速にログの調査が可能です。ご協力の程よろしくお願いいたします。
 
**対象のフォームや、配信のID（または、管理画面のURL）** 
- 例）`https://example.kuroco.r-cms.jp/management/inquiry/inquiry_edit/inquiry_id=**`
- 例）`https://example.kuroco.r-cms.jp/management/magazine/magazine_edit/magazine_id=**`
 
**対象のメールの情報**  
下記情報について、複数ある場合は全てお書きください。
 - 対象メールのNo.
 - 配信元メールアドレス（FROM）
 - 配信先メールアドレス（TO） 
 - 受信日時（フォームの場合）、配信日時（配信の場合）

## メールが送信できない場合の調査の限界
インターネット上のメールシステムは分散型のシステムとなっており、送信側だけではメールが送信されて受信できているかを完全に把握できません。  
また、メールアドレスの存在を隠す等の理由で受信側のエラーの内容が正確でない場合や、メールボックスの容量制限を超えている場合など様々なエラー要因があります。  

原則として、SendGridから送信が成功していて、Bouncesにメールがない場合にはこれ以上は調査ができません。  
しかしながら、何か他に調査できるようなシステム的なログなどの提供があれば再調査は可能ですので、受信側のサーバー管理者様とも連携して調査いただければ幸いです。

## 関連ドキュメント
- [メールログ](/ja/docs/management/mail-log-list/)
- [SendGridログ](/ja/docs/management/sendgrid-log-list/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [フォームのお礼メールが届かないときの確認箇所を教えてください](/ja/docs/faq/i-did-not-receive-a-thankyou-email-what-do-i-do/)
- [Kurocoから送信されるメールが迷惑メールになってしまいます。解決方法を教えてください。](/ja/docs/faq/emails-sent-from-kuroco-are-going-to-spam-what-should-i-do/)


---

# 問い合わせフォームに大量のスパムメールが届きます。対策はありませんか？

> 元ページ: `faq/how-do-i-reduce-spam-inquiries` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-reduce-spam-inquiries/
> 概要: reCAPTCHAを利用することで、悪質なスパム投稿からWebサイトを守ることができます。

フォームのスパム対策にはreCAPTCHAをご利用ください。

## reCAPTCHAについて 
reCAPTCHAとは、Googleが無償で提供している機能です。  
Webサイトのお問い合わせフォーム等で情報を登録する際、悪質なスパム投稿からWebサイトを守ることができます。

詳しい設定方法は、[reCAPTCHAの利用方法](/ja/docs/tutorials/using-recaptcha/)をご覧ください。

## 関連ドキュメント
- [reCAPTCHA](/ja/docs/management/recaptcha/)
- [reCAPTCHAを利用したフォームを作成する](/ja/docs/tutorials/using-recaptcha/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)


---

# メンバー登録後メールが届きません。設定方法を教えてください。

> 元ページ: `faq/how-do-i-set-up-member-registration-confirmation-emails` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-set-up-member-registration-confirmation-emails/
> 概要: メンバー登録のエンドポイントにて、「send_email_flg」にチェックが入っていない場合メールが送信されません。管理画面の[API]より、該当のエンドポイントの設定をご確認ください。

メンバー登録のエンドポイントにて、「send_email_flg」にチェックが入っていない場合メールが送信されません。
管理画面の[API]より、該当のエンドポイントの設定をご確認ください。

## 確認方法

[API]より対象のAPIを選択し、API画面を表示します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a88be65f9ffc2793384a4d86c32de01.png)


[メンバー]より、[オペレーション]が[insert]のエンドポイントの「更新」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/591617e6d3953be580efeb502ae57487.png)

[詳細設定]配下の「send_email_flg」にチェックが入っているか確認してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fdf323724d65f2e6380376908ed0da.png)

チェックが入っていない場合メールが送信されません。  
メールを送信する場合は、「send_email_flg」にチェックを入れて画面下部の[更新]をクリックしてください。

## 関連ドキュメント
- [メッセージひな形](/ja/docs/management/email-template/)
- [新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [メールが送信できない場合の確認方法を教えてください。](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)
- [管理画面からメンバー登録した際にメールでパスワードを通知できますか？](/ja/docs/faq/how-can-i-send-a-registration-email-with-pw-information/)


---

# フォームのお礼メールが届かないときの確認箇所を教えてください

> 元ページ: `faq/i-did-not-receive-a-thankyou-email-what-do-i-do` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/i-did-not-receive-a-thankyou-email-what-do-i-do/
> 概要: フォームの基本設定の「お礼メール送信」で「送信する」を選択しているにも関わらず、お礼メールが届かない場合確認方法を記載します。

フォームの基本設定の「お礼メール送信」で「送信する」を選択しているにも関わらず、お礼メールが届かない場合は下記３点をご確認ください。

**迷惑メールフォルダに振り分けられていませんか？**  
お礼メールが迷惑メールフォルダやゴミ箱に自動的に振り分けられている可能性がありますので、一度ご確認頂きますようお願い致します。

**[[フォームの基本設定]->[お礼送信メール]](/ja/docs/management/inquiry-basic-settings)の「送信する」にチェックは入っていますか？**  
「送信する」にチェックが入っている場合のみメールが送信されます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/242b17f9361611180d41787093bd7f39.png)
**フォームの項目設定で、デフォルトの項目にある「email」を利用していますか？**  
お礼メールは「email」の項目で入力されたメールアドレス宛に配信されます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/90d3c7c2d0bbb87e40377584e1d0dd23.png)
## 解決できなかったときは
上記3点の確認では解決できず、メール送信についての調査をご希望の際には、以下のFAQを参考のうえ[サポート事務局](https://kuroco.zendesk.com/hc/ja)までお問い合わせください。    

:::info
[メールの送信に関しての調査](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)
:::

## 関連ドキュメント
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [メールログ](/ja/docs/management/mail-log-list/)
- [メールが送信できない場合の確認方法を教えてください。](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)
- [Kurocoから送信されるメールが迷惑メールになってしまいます。解決方法を教えてください。](/ja/docs/faq/emails-sent-from-kuroco-are-going-to-spam-what-should-i-do/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)


---

# メール配信時の件数制限はありますか。

> 元ページ: `faq/is-there-a-limit-to-the-number-of-e-mails-i-can-send` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-there-a-limit-to-the-number-of-e-mails-i-can-send/
> 概要: Kurocoの配信機能には件数制限はありません。ただし、無料利用ユーザーには1時間あたり約100通の送信制限があります。また、メール配信は従量課金対象となりますのでご注意ください。

Kurocoの配信機能には件数制限はありません。  
ただし、メール配信は従量課金対象となりますのでご注意ください。

:::caution 無料利用ユーザーの制限
無料利用ユーザー（決済情報未登録のユーザー）については、**1時間あたり約100通**までの送信制限があります。

制限対象外となる条件:
- 「[請求情報](/ja/docs/management/site-payment/)」でクレジットカードをご登録いただいているお客様
- 決済手段に「ディバータから請求書」と表示されているお客様
- ご自身のSendGridのAPIキーを利用して、独自ドメインのメールアドレスをご利用されている場合

詳細は下記をご確認ください。  
お知らせ -> [無料利用ユーザーのメール送信数に制限をかけます](/ja/docs/information/2025-11-26/)  
リファレンス -> [Kurocoにおける制限事項](/ja/docs/reference/limitations-in-kuroco/)
:::

:::tip
従量課金については下記をご確認ください。  
FAQ -> [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)
:::

また、SendGridと連携している場合はSendGridの利用料金が別途SendGrid側で発生します。  
SendGridの料金については、[SendGridの料金ページ](https://sendgrid.kke.co.jp/plan/)をご確認ください。

:::info
KurocoとSendGridの連携方法は下記をご確認ください。  
[SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
:::

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [請求情報](/ja/docs/management/site-payment/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)
- [Kurocoにおける制限事項](/ja/docs/reference/limitations-in-kuroco/)
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)


---

# SendGridに残るログの保存場所・期間・内容について教えてください

> 元ページ: `faq/sendgrid-log-storage-retention-content-details` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/sendgrid-log-storage-retention-content-details/
> 概要: SendGridのログの保存場所・期間・内容についての情報を提供します。

以下のドキュメントに記載の内容を案内します。  
詳細はSendGridのドキュメントを確認してください。

:::info
- [SendGrid FAQs](https://sendgrid.com/files/SendGrid-FAQ.pdf)
- [Data Retention and Deletion in Twilio Products](https://support.twilio.com/hc/en-us/articles/4410585868443-Data-Retention-and-Deletion-in-Twilio-Products)
:::

## データの保管場所について
データの保存場所に関しては、米国内のデータセンターのようです。

> Your data is stored and processed in data centers located in the United States, while we use other data
centers around the world to receive your mail quickly. 

引用：[SendGrid FAQs](https://sendgrid.com/files/SendGrid-FAQ.pdf)

## メール本文の保管期間について
メール本文は最大72時間保存されるようです。
（再送などに必要な場合がある）

> We retain email message bodies only as long as it takes for us to deliver the email. This can take up to 72 hours if we need to retry due to delivery failure.  
*Please note that if you choose to use our Scheduled Sending features, we will retain email message bodies for as long as you tell us to (up to 6 days) based on your schedule. However, once the message is sent, we retain the message only as long as it takes to deliver the email.

引用：[Data Retention and Deletion in Twilio Products](https://support.twilio.com/hc/en-us/articles/4410585868443-Data-Retention-and-Deletion-in-Twilio-Products)

## 個人データの保管期間について
Twilio SendGridサービスをご利用の場合、電子メール本文は、送信にかかる時間だけ保持し、他の個人データ、つまり電子メール受信者データを含むほとんどの個人データについては、最大37日間（30日間にデータ削除プロセスを完了するための追加日数を含む）保持されるようです。

> If you’re using the Twilio SendGrid service, we only hold email message bodies for as long as it takes to send them. Other than your account data, we retain most other personal data, including email recipient data, for a maximum of 37 days (30 days, plus a little extra to finalize the deletion process), except as described below.

引用：[Data Retention and Deletion in Twilio Products](https://support.twilio.com/hc/en-us/articles/4410585868443-Data-Retention-and-Deletion-in-Twilio-Products)

## イベントの保管期間について
送信されたメールに関連するイベントは最長1年間保持されるようです。このデータにはメッセージの内容は含まれませんが、状況によっては受信者を特定できる情報が含まれる可能性があります。

> We retain events associated with sent emails for up to a year. This data does not include the content of your messages, but it might include information that could be identified with a recipient, depending on the circumstances.

引用：[Data Retention and Deletion in Twilio Products](https://support.twilio.com/hc/en-us/articles/4410585868443-Data-Retention-and-Deletion-in-Twilio-Products)

## 関連ドキュメント
- [SendGridログ](/ja/docs/management/sendgrid-log-list/)
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [SendGridと連携後、メール内のURLが勝手に置換されてしまいます。直せますか？](/ja/docs/faq/after-linking-with-sendgrid-url-in-email-is-replaced/)
- [メール送信の料金はSendGridと契約していても発生しますか？](/ja/docs/faq/do-i-have-to-pay-for-sending-emails-even-if-i-use-sendgrid/)


---

# メンバー管理のメールアドレスに利用できる文字とバリデーション仕様を教えてください

> 元ページ: `faq/what-characters-can-be-used-as-email` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-characters-can-be-used-as-email/
> 概要: RFC準拠のメールアドレスが利用できます。Kurocoでは特定の正規表現パターンでメールアドレス検証を行います。

メンバー管理のメールアドレスに利用できる文字を教えてください

Kurocoではデフォルトの挙動では特定の正規表現パターンでメールアドレス検証を行います。ただし別途、設定をすることでRFC準拠のメールアドレス制限に変更ができます。

## メールアドレス検証の正規表現

Kurocoでは、`preg_match()`関数を使用して以下の正規表現パターンでメールアドレスの検証を行います：

```php
preg_match('/^[a-zA-Z0-9.+!#$&*=?^_{|}~-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/', $email_address)
```

この正規表現は以下の条件でメールアドレスを検証します：
- **ローカル部**（@より前）：英数字、ピリオド、パーセント、プラス、感嘆符、ハッシュ、アンパサンド、アスタリスク、等号、疑問符、ハット、アンダースコア、パイプ、波線、ハイフンが使用可能
- **ドメイン部**（@より後）：英数字、ピリオド、ハイフンが使用可能で、最後に2文字以上のトップレベルドメインが必要

## メールアドレス検証関数の実装

Kurocoでのメールアドレス検証には、設定に応じて2つの異なる検証モードがあります：

### 検証モード

**デフォルトの動作（正規表現による検証）:**  
Kurocoでは、デフォルトで**カスタム正規表現パターンによる検証**を行います：  
- 最大256文字の長さ制限を適用
- 独自に定義された特定の文字セットを許可
- 特別な設定を行わない場合の標準的な検証方法です

**RFC準拠モード（STRICT_VALIDATE_EMAIL定数による切り替え）:**  
`STRICT_VALIDATE_EMAIL`定数を設定すると、検証が**完全なRFC準拠**に切り替わります：  
- 公式のメールアドレス標準に従った完全なRFC準拠を提供
- RFC仕様を超えるカスタム長さ制限なし
- デフォルトの正規表現検証よりも寛容な検証

**デフォルトの正規表現検証からRFC準拠に切り替えるには：**

```php
STRICT_VALIDATE_EMAIL = 1;
```

この定数により、検証動作がカスタム正規表現パターンマッチングから標準的なRFC準拠のメールアドレス検証に変更されます。

:::info
`STRICT_VALIDATE_EMAIL`などの定数は、Kuroco管理画面の[定数](/ja/docs/management/constants/)で設定できます。
:::

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [メンバー](/ja/docs/management/member/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)
- [メンバー管理のパスワードに利用できる文字を教えてください](/ja/docs/faq/what-characters-are-allowed-in-passwords/)
