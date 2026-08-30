# Kurocoドキュメント: FAQ / email-form

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- お問い合わせに添付されたファイルを通知メールに添付できますか？（`can-i-attach-inquiry-files-to-notification-emails`）
- フォームのデフォルトのステータスを変更できますか？（`can-i-change-the-default-status-of-a-form`）
- メール配信の際の送信元のメールアドレス「noreply@kuroco-mail.app」を変更できますか？（`can-i-change-the-senders-email-address`）
- お礼メールをカスタマイズできますか？（`can-i-customize-my-thank-you-e-mail`）
- 受信者の環境に合わせて、送信するメールをHTMLメールにするかテキストメールにできますか？（`can-i-send-html-or-plain-text-emails-depending-on-the-recipients-environment`）
- 重要なお知らせを全ユーザー宛に送信したいです。メルマガ拒否フラグを無視できますか？（`can-i-send-important-notifications-bypassing-newsletter-optout`）
- フォームの回答形態「日付」の期間を、任意の期間で設定できますか？（`can-i-set-a-custom-time-period-for-the-inquiry-response-date-selection`）
- フォームの項目に初期値やプレースホルダーを設定できますか？（`can-i-set-initial-value-or-placeholder-fof-form-items`）
- 複数の独自ドメインのメールを利用できますか？（`can-i-use-more-than-one-unique-e-mail-domain`）
- メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？（`can-i-use-my-custom-domain-for-the-sender-address`）
- フォームに入力した値に応じて他の項目の表示・非表示を変更できますか？（`hide-other-items-based-on-the-entered-value`）
- フォーム毎に管理者宛通知メールの内容を変えることはできますか？（`how-can-i-change-the-content-of-the-notification-e-mail-for-each-form`）
- フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？（`how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices`）
- 管理画面からメンバー登録した際にメールでパスワードを通知できますか？（`how-can-i-send-a-registration-email-with-pw-information`）
- お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？（`how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications`）
- 問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？（`how-do-i-include-content-details-in-the-thankyou-email`）
- 問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？（`how-do-i-include-inquiry-details-in-the-thankyou-email`）
- 問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？（`how-do-i-include-user-details-in-the-thankyou-email`）
- フォームの回答を1ユーザー1回までにできますか？（`how-to-limit-form-responses-to-once-per-user`）
- カスタム処理やメッセージひな形でインデントが空白で反映されてしまいます（`indentation-is-reflected-as-spaces-in-custom-functions-or-message-templates`）


---

# お問い合わせに添付されたファイルを通知メールに添付できますか？

> 元ページ: `faq/can-i-attach-inquiry-files-to-notification-emails` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-attach-inquiry-files-to-notification-emails/
> 概要: ファイルの容量やスパム判定回避の問題があり、メールへのファイル添付は現在対応されておりません。ダウンロードリンクの付与であれば対応が可能です。

ファイルの容量やスパム判定回避の問題があり、メールへのファイル添付は現在対応されておりません。  
代替手段として、通知メールに**ダウンロードリンク**を付与する対応が可能です。

## 設定方法

### メッセージひな形

以下の**管理者宛通知メール**の[メッセージひな形](/ja/docs/management/email-template/)にダウンロードURLとファイル名を追加してください。

| モジュール | 識別子 |
| :--- | :--- |
| Form | inquiry/inquiry_contact |

例：
```
ファイルダウンロードURL：
{$smarty.const.ROOT_MNG_URL}/direct/inquiry/file_download/?file_nm={$inquiry_bn_id}_ext_01
```

:::tip
- ファイルの拡張子はメッセージひな形にアサインされません。ダウンロード時に自動で補完されるので、URLに拡張子を含める必要はありません。
- **注意:** S3/GCS ストレージの場合は拡張子が必要です。
:::

### Kurocoに添付ファイルを残したくない場合

バッチ処理で一定期間（例：1週間）以上経過した回答を自動削除することが可能です。

#### 事前準備：エンドポイントの作成

内部API用に `InquiryMessage::list` エンドポイントと `InquiryMessage::delete` エンドポイントを作成してください。

#### バッチ処理

以下のコードで[バッチ処理](/ja/docs/management/batch/)を作成してください。

```smarty
{* 7日以上経過した回答一覧を取得 *}
{assign var='queries' value=$dataSet.emptyArray}
{append var='queries' index='filter' value='inst_ymdhi <:relatively "7 days ago"'}
{append var='queries' index='cnt' value='0'}
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/1/inquiry-list'
    method='GET'
    member_id='1'
    queries=$queries
}

{* 各回答を削除 *}
{foreach from=$response.list item=item}
    {assign var='target' value="/rcms-api/1/inquiry-delete/`$item.inquiry_bn_id`"}
    {api_internal
        var='del_response'
        status_var='del_status'
        endpoint=$target
        method='POST'
        member_id='1'
    }
    {logger msg1="Deleted inquiry_bn_id=`$item.inquiry_bn_id`" msg2=$del_response}
{/foreach}
```

:::caution
`/rcms-api/1/inquiry-list` および `/rcms-api/1/inquiry-delete/` は実際のエンドポイントのパスに置き換えてください。
:::

## 関連ドキュメント

- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)


---

# フォームのデフォルトのステータスを変更できますか？

> 元ページ: `faq/can-i-change-the-default-status-of-a-form` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-default-status-of-a-form/
> 概要: デフォルトでは0のステータスが設定されます。変更したい場合はInquiryMessage::sendのassign_statusのパラメータを設定してください。

デフォルトでは0のステータスが設定されます。  
変更したい場合は`InquiryMessage::send`のエンドポイントで`assign_status`のパラメータを設定してください。

## 設定方法

`InquiryMessage::send`のエンドポイント設定で、`assign_status`のパラメータに任意のステータス値を設定します。  
設定したステータスで回答が登録されるようになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea117ff497fac91dce7230d0c6f2a974.png)

なお、`assign_status`はクエリパラメータでの指定はできません。  
条件によってデフォルトのステータスを分けたい場合は、`assign_status`の値が異なる複数の`InquiryMessage::send`のエンドポイントを準備しておき、カスタム処理でフォームの登録に利用するエンドポイントを使い分けるような実装方法になります。

## 関連ドキュメント
- [エンドポイントパラメータ一覧](/ja/docs/reference/endpoint-parameters/)


---

# メール配信の際の送信元のメールアドレス「noreply@kuroco-mail.app」を変更できますか？

> 元ページ: `faq/can-i-change-the-senders-email-address` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-senders-email-address/
> 概要: はい、SendGridと連携することで送信元メールアドレスの変更が可能です。SendGridと連携すると、メールアドレスをご自身のドメインに変更できます。

はい、SendGridと連携することで送信元メールアドレスの変更が可能です。  

SendGridと連携すると、メールアドレスをご自身のドメインに変更できます。KurocoとSendGridの連携方法は下記チュートリアルをご確認ください。

- [チュートリアル -> SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)

SendGridの詳細については、[SendGridのホームページ](https://sendgrid.kke.co.jp/)をご確認ください。

なお、`noreply@xxx.kuroco-mail.app`のようにkuroco-mail.appドメインを使用して一部だけ変更することはできません。

:::info
SendGrid以外のメール配信サービスを使用する場合は、「[デフォルトのメール送信方法（SendGrid）を代替](/ja/docs/reference/trigger-variables/#デフォルトのメール送信方法sendgridを代替)」のトリガーを設定したカスタム処理を利用します。  
詳しくは以下のドキュメントをご参照ください。
- [Kurocoからのメール送信に任意のメール配信サービスを使用する(Mailchimp)](/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-mailchimp/)
- [Kurocoからのメール送信に任意のメール配信サービスを使用する(blastengine)](/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-blastengine/)
:::

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [Kurocoからのメール送信に任意のメール配信サービスを使用する(Mailchimp)](/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-mailchimp/)
- [Kurocoからのメール送信に任意のメール配信サービスを使用する(blastengine)](/ja/docs/tutorials/use-any-email-delivery-service-to-send-emails-from-kuroco-blastengine/)
- [メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？](/ja/docs/faq/can-i-use-my-custom-domain-for-the-sender-address/)


---

# お礼メールをカスタマイズできますか？

> 元ページ: `faq/can-i-customize-my-thank-you-e-mail` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-customize-my-thank-you-e-mail/
> 概要: フォーム基本設定の「お礼メール送信」の箇所に以下のように記載をすることでカスタマイズ出来ます。また、Smartyでの記述が出来る場合はそちらも利用が可能です。

[フォーム基本設定](/ja/docs/management/inquiry-basic-settings/#基本設定項目一覧)の「お礼メール送信」の箇所に以下のように記載をすることでカスタマイズ出来ます。  
また、Smartyでの記述が出来る場合はそちらも利用が可能です。

## 設定箇所
[フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)の「お礼メール送信」の「内容」フィールドを編集します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfb423155d9e800ef08bf009f5c238d9.png)

## 設定可能な項目
|項目   |説明  |
| :--- | :--- |
|RCMS-X-FROM:|送信元メールアドレス|
|RCMS-X-TO:|送信先|
|RCMS-X-CC:|CC先|
|RCMS-X-BCC:|BCC先|
|RCMS-X-REPLY-TO:|返信先|
|RCMS-X-SUBJECT:|タイトル|
|RCMS-X-MAIL_FROM_NM:|送信者名|
|RCMS-X-MAIL_TYPE:|メールタイプ(HTMLメールの場合はhtmlを設定)|
|RCMS-X-AVOID:|メールの送信停止(メールの送信を停止する場合に1を設定)|

:::tip
上記の記述は、[メッセージひな形](/ja/docs/management/email-template/)でもご利用可能です。
:::

## 関連FAQ
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)

## 関連ドキュメント
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [フォームのお礼メールが届かないときの確認箇所を教えてください](/ja/docs/faq/i-did-not-receive-a-thankyou-email-what-do-i-do/)


---

# 受信者の環境に合わせて、送信するメールをHTMLメールにするかテキストメールにできますか？

> 元ページ: `faq/can-i-send-html-or-plain-text-emails-depending-on-the-recipients-environment` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-send-html-or-plain-text-emails-depending-on-the-recipients-environment/
> 概要: 配信機能では、受信者の環境に合わせて切り替えが可能です。

配信機能では、受信者の環境に合わせて下記のように切り替えが可能です。

- 受信者がHTMLメールを表示できる場合：HTMLメールを送信
- 受信者がHTMLメールを表示できない場合：テキストメールを送信

## 設定方法
[チャネル] -> [一括配信]をクリックし、配信一覧画面へ遷移します。  
配信一覧より、対象の配信タイトルの[追加]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b06351ff25b0c396a7ced1293520fddc.png)
ラジオボタンより[Htmlメール]を選択し、「Html」フィールド、「テキスト」フィールドに内容を記入します。
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/f299141fd40370f3d5e19b2ee74a6733.png)
「テキスト」エリアに入力がある状態でHTMLメールを送信すると、ユーザー側でHTMLメールの表示をしない設定にしている場合に、「テキスト」内の記述が表示されます。  

:::tip
「テキスト」に入力がない場合は、HTMLメールの内容からタグを抜いた内容が表示されます。
:::  

## 関連ドキュメント
- [配信 メッセージ作成](/ja/docs/management/notification-message-editor/)
- [配信一覧](/ja/docs/management/notification-list/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)
- [メール配信時の件数制限はありますか。](/ja/docs/faq/is-there-a-limit-to-the-number-of-e-mails-i-can-send/)


---

# 重要なお知らせを全ユーザー宛に送信したいです。メルマガ拒否フラグを無視できますか？

> 元ページ: `faq/can-i-send-important-notifications-bypassing-newsletter-optout` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-send-important-notifications-bypassing-newsletter-optout/
> 概要: カスタムメンバーフィルターではメルマガ拒否フラグを無視できませんが、CSVダウンロードと購読者登録、または重要案内用の別配信リストを作成する方法があります。

カスタムメンバーフィルターで宛先指定する場合はメルマガ拒否フラグを無視できません。  
メルマガ拒否フラグを無視して配信を行いたい場合は、メールアドレスを購読者に登録してメールの送信を行ってください。

## 対応例

### CSVによる購読者登録

1. 購読者の登録がある場合は現在の購読者一覧をCSVでダウンロードする
2. 重要なお知らせを送信するメールアドレスリストをCSVでアップロードし、メール配信する
3. 必要に応じて、CSVで購読者の一覧を元に戻す

### 全ユーザー宛の配信リストを作成

1. 全メンバーを購読者にした「重要な案内」のような配信を作成する
2. そちらで重要なお知らせを送信する

## 関連ドキュメント
- [配信 購読者一覧](/ja/docs/management/notification-subscribers/)
- [カスタムメンバーフィルター](/ja/docs/management/custom-member-filter/)
- [配信の購読者を登録する](/ja/docs/tutorials/how-to-register-subscribers-on-magazine/)
- [メールマガジンを送付する](/ja/docs/tutorials/sending-email-notifications/)
- [カスタムメンバーフィルターを利用する](/ja/docs/tutorials/using-custom-member-filters/)


---

# フォームの回答形態「日付」の期間を、任意の期間で設定できますか？

> 元ページ: `faq/can-i-set-a-custom-time-period-for-the-inquiry-response-date-selection` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-a-custom-time-period-for-the-inquiry-response-date-selection/
> 概要: 日付の西暦は、任意の期間を設定することができます。

日付の西暦は、任意の期間を設定できます。
 
## フォームで期間設定手順
**1. [[フォーム] -> [項目設定]](/ja/docs/management/form-field-settings)の回答形態で[日付フォーマット]を選択する** 

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/710ee5ccba2698fd87a6d7b69936b387.png)
**2. 「設定」をクリックして、「年(下限)」「年(上限)」を設定する** 

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7da470ebdf93c92b682b3c15385b3b1e.png)  

**3. 「設定」ボタンをクリックする**

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ef2098f7de9228d3c25d20c4f8c771df.png)  

2020年～2025年を指定した場合、画像のように自動で入力されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/171df155aa45b0e35edef20f46334e79.png)
**4. 更新する**  
画面下部の「更新する」をクリックして完了です。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/16ab3c5fda1ae36f96c3bceaef9f7769.png)
## 補足
### 現在の年を起点に期間を指定したい場合
「現在の年を基点に-10年」「現在の年を基点に＋15年」のような指定をしたい場合は、回答形態/入力制限の入力欄に、下記のように記入してください。
```
minYear::-10
maxYear::+15
```
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b443f06d4fb98f3fa0f4c86972727d6f.png)

## 関連ドキュメント
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [フォーム定義で利用できるフォーム項目一覧](/ja/docs/reference/form-field-list/)
- [フォームの項目に初期値やプレースホルダーを設定できますか？](/ja/docs/faq/can-i-set-initial-value-or-placeholder-fof-form-items/)


---

# フォームの項目に初期値やプレースホルダーを設定できますか？

> 元ページ: `faq/can-i-set-initial-value-or-placeholder-fof-form-items` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-initial-value-or-placeholder-fof-form-items/
> 概要: フォーム項目設定で設定が可能です。Placeholderに任意の文字列を設定すると、入力内容がレスポンスに含まれますのでフロントエンドで表示場所を調整ください。

[フォーム項目設定](/ja/docs/management/form-field-settings/)で設定が可能です。  
Placeholderに任意の文字列を設定すると、入力内容がレスポンスに含まれますのでフロントエンドで表示場所を調整ください。  

## 設定箇所
フォーム項目設定の[設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d92ad4639b572fce20ce8acf7d0d7c3.jpg)
表示された設定画面から[Placeholder]に入力します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a7fa8cf488b6894c052fd54263f7dde.png)
:::tip
APIレスポンスを確認する方法は下記のチュートリアルをご参照ください。<br/>- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
:::

## フロントエンドの記述例
フロントへの表示部分はお客様側で自由に記述ください。  
例えばNuxt.jsの場合は、[KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/) のチュートリアルの記述を以下のように変更すると、初期値やプレースホルダーを表示できます。  

- 変更前
```markup
<input :name="col.objKey" type="text" />
``` 

- 変更後(初期値)
```markup
<input :name="col.objKey" :value="col.attribute.placeholder" type="text" />
```

- 変更後(プレースホルダー)
```markup
<input :name="col.objKey" :placeholder="col.attribute.placeholder" type="text" />
```

## 関連ドキュメント
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [フォーム定義で利用できるフォーム項目一覧](/ja/docs/reference/form-field-list/)
- [フォームの回答形態「日付」の期間を、任意の期間で設定できますか？](/ja/docs/faq/can-i-set-a-custom-time-period-for-the-inquiry-response-date-selection/)


---

# 複数の独自ドメインのメールを利用できますか？

> 元ページ: `faq/can-i-use-more-than-one-unique-e-mail-domain` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-more-than-one-unique-e-mail-domain/
> 概要: SendGridのアカウントを独自にご契約いただいている場合、SendGridに複数のドメインの送信元を設定が可能です。

SendGridのアカウントを独自にご契約いただいている場合、SendGridに複数のドメインの送信元を設定が可能です。

SendGridで設定後、Kuroco側のSendGridの設定画面で送信許可ドメイン・メールアドレスに、追加のドメインをセットしてください。  
問い合わせなどの返信の送信元として利用できるようになります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/440a5fa7aaa4de2139629ba0addce028.png)

SendGridについては下記をご参照ください。  
- [メール配信の際の送信元のメールアドレス「noreply@kuroco-mail.app」を変更できますか？](https://kuroco.app/ja/docs/faq/can-i-change-the-senders-email-address/)  
- [SendGrid連携方法](https://kuroco.app/ja/docs/tutorials/how-to-link-sendgrid/)

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [メール配信の際の送信元のメールアドレス「noreply@kuroco-mail.app」を変更できますか？](/ja/docs/faq/can-i-change-the-senders-email-address/)
- [メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？](/ja/docs/faq/can-i-use-my-custom-domain-for-the-sender-address/)


---

# メールの送信元に独自ドメインを利用するにはどうしたらよいでしょうか？

> 元ページ: `faq/can-i-use-my-custom-domain-for-the-sender-address` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-my-custom-domain-for-the-sender-address/
> 概要: SendGridと連携をすることで、メールの送信元に独自ドメインを利用することができます。

SendGridと連携をすることで、メールの送信元に独自ドメインを利用できます。  
SendGridは契約主体が利用者でなければならないため、利用者がSendGridの申込みをして、[APIキー](https://sendgrid.kke.co.jp/docs/User_Manual_JP/Settings/api_keys.html)を取得する必要があります。  

また、独自ドメインをセットするために、[Sender Authenticationの設定](https://sendgrid.kke.co.jp/docs/User_Manual_JP/Settings/Sender_authentication/How_to_set_up_domain_authentication.html)が必要です。  

SendGridの設定方法は[SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)をご確認ください。

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [メール配信の際の送信元のメールアドレス「noreply@kuroco-mail.app」を変更できますか？](/ja/docs/faq/can-i-change-the-senders-email-address/)
- [複数の独自ドメインのメールを利用できますか？](/ja/docs/faq/can-i-use-more-than-one-unique-e-mail-domain/)
- [Kurocoから送信されるメールが迷惑メールになってしまいます。解決方法を教えてください。](/ja/docs/faq/emails-sent-from-kuroco-are-going-to-spam-what-should-i-do/)


---

# フォームに入力した値に応じて他の項目の表示・非表示を変更できますか？

> 元ページ: `faq/hide-other-items-based-on-the-entered-value` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/hide-other-items-based-on-the-entered-value/
> 概要: コンテンツ定義の詳細設定でJavaScriptを入力できますので、こちらを利用して処理を書いてください。例えば、以下のコードはext_1に設定された複数選択チェックボックスのチェックの有無に基づいて、ext_2, ext_3のテキスト項目の表示を制御するJavaScriptです。

コンテンツ定義の詳細設定でJavaScriptを入力できますので、こちらを利用して処理を書いてください。  

## 設定箇所
[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#コンテンツ定義編集)の詳細設定のJavaScript項目。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a5bc50f796dc50ae422c3693c5f72d5d.png)

## コード例

例えば、以下のコードはext_1に設定された複数選択チェックボックスのチェックの有無に基づいて、
ext_2, ext_3のテキスト項目の表示を制御するJavaScriptです。

```js
{literal}
window.addEventListener('load', function() {
    // チェックボックスの状態に基づいて input 要素の表示を制御する関数
    function toggleInputVisibility() {
        // id="ext_1__1" のチェックボックスを取得
        var checkbox1 = document.getElementById('ext_1__1');
        // input[name="ext_2"] 要素を取得
        var inputText2 = document.querySelector('input[name="ext_2"]');
        if (inputText2) {
            // id="ext_1__1" のチェックボックスがチェックされているか確認
            inputText2.style.display = checkbox1.checked ? '' : 'none'; // チェックされていれば表示、そうでなければ非表示
        }

        // id="ext_1__2" のチェックボックスを取得
        var checkbox2 = document.getElementById('ext_1__2');
        // input[name="ext_3"] 要素を取得
        var inputText3 = document.querySelector('input[name="ext_3"]');
        if (inputText3) {
            // id="ext_1__2" のチェックボックスがチェックされているか確認
            inputText3.style.display = checkbox2.checked ? '' : 'none'; // チェックされていれば表示、そうでなければ非表示
        }
    }

    // ページ読み込み時に一度実行して初期状態を設定
    toggleInputVisibility();

    // チェックボックスの状態変更にも反応するようにイベントリスナーを設定
    document.body.addEventListener('change', function(event) {
        // 変更された要素が id="ext_1__1" または id="ext_1__2" のチェックボックスであるか確認
        if (event.target.id === 'ext_1__1' || event.target.id === 'ext_1__2') {
            toggleInputVisibility();
        }
    });
});
{/literal}
```

:::info
コンテンツ編集画面のinput要素はJavaScriptによって動的に生成されています。こちらを考慮して、JavaScriptの実行されるタイミング等を制御してください。  
:::

## 動作例

![Image from Gyazo](https://t.gyazo.com/teams/diverta/540e354b8297d2679931eb5e357bfb71.gif)

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)


---

# フォーム毎に管理者宛通知メールの内容を変えることはできますか？

> 元ページ: `faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/
> 概要: メッセージひな形で「問い合わせ着信通知メール(管理者宛)」のテンプレートにSmartyで分岐をかけることで対応できます。

[メッセージひな形](/ja/docs/management/email-template/)で「問い合わせ着信通知メール(管理者宛)」のテンプレートにSmartyで分岐をかけることで対応できます。  
[お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)で紹介している`RCMS-X-FROM`等の記述は、「メッセージひな形」でも利用可能です。

## 設定箇所
下記の[メッセージひな形](/ja/docs/management/email-template/)の「本文」フィールドで設定します。

|モジュール   |テンプレート  |Slug  |
| :--- | :--- | :--- |
|inquiry|問い合わせ着信通知メール(管理者宛)|inquiry/inquiry_contact|

## 遷移方法
[オペレーション]->[メッセージひな形]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/be3fdd5c65007a98fd554828930f3384.png)

メッセージひな形一覧から「問い合わせ着信通知メール(管理者宛)」を探してクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a708dc1270701af779dae9524e8f7d59.png)

メッセージひな形編集のページに遷移し、ボディフィールドが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ce9721daeeda3538667e5e58a9626f5.png)

## 設定例
以下の例では問い合わせ者のメールアドレスが特定の場合に管理者宛通知メールの送信をせず、  
問い合わせのフォームによって管理者宛通知メールのCCの宛先を変更しています。

```php
{if $items.email.value eq 'test@example.com'}
RCMS-X-AVOID:1
{/if}

{if $inquiry_id eq 6}
RCMS-X-CC:list1@example.com
{else if $inquiry_id eq 7}
RCMS-X-CC:list2@example.com
{/if}

問い合わせが届きました。
以下から内容を確認してください。
{$smarty.const.ROOT_MNG_URL}/management/
```

## 関連ドキュメント
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)


---

# フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？

> 元ページ: `faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/
> 概要: フォームの項目設定下部にあるカテゴリを利用してください。各カテゴリに対して、選択された場合に送信される配信先メールアドレスを改行区切りで入力します。

[フォームの項目設定](/ja/docs/management/form-field-settings/#カテゴリ編集)下部にあるカテゴリを利用してください。  
各カテゴリに対して、選択された場合に送信される配信先メールアドレスを改行区切りで入力します。

:::info
[基本設定](/ja/docs/management/inquiry-basic-settings/)に入力した配信先メールアドレス宛には、カテゴリの選択に関わらず通知メールが届きます。
:::

:::tip
利用されるメッセージひな形は[フォーム基本設定]->[配信先メールアドレス]の設定によって以下になります。  
通知する：`inquiry/inquiry_contact`  
入力内容全て通知：`inquiry/inquiry_contact_simple`  
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/97645035dbf6e995ae2be53ff4e62098.png)

## 関連ドキュメント
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)


---

# 管理画面からメンバー登録した際にメールでパスワードを通知できますか？

> 元ページ: `faq/how-can-i-send-a-registration-email-with-pw-information` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-send-a-registration-email-with-pw-information/
> 概要: CSVファイルで且つパスワードをランダムに生成した場合に、登録されたメンバーに対してメンバー登録時に送信するメールにてパスワードを平文で表示して通知することができます。

以下の条件で、登録通知メールにてパスワードを平文で表示して通知することができます。

- CSVファイルでメンバーを登録
- パスワードをランダム生成


## 設定箇所

### メンバー詳細設定画面

[メンバー詳細設定画面のメール通知](/ja/docs/management/new-member-settings/#メール通知)で、[登録時ユーザー宛]にチェックを入れます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8553a184f9d91aa85cbdecad61bc15eb.png)


### メンバーアップロード画面

[メンバーアップロード](/ja/docs/management/member-upload/#メンバーアップロード)画面でCSVファイルアップロード時に、「値がない場合の動作」の項目で以下を設定してアップロードします。

- 値なしで更新する
- パスワード：ランダムに生成する

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d9d778c0b52ed1c53fad0b8c0f3c03f.png)

上記設定で、以下のようにパスワードが平文で表示された状態の通知メールが届きます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6163271726156240acc64bdff53cce2.png)

:::tip
- 上記メールの文面は、[メッセージひな形](/ja/docs/management/email-template/)画面で編集可能です。<br/>対象のひな形の識別子は`member/regist_thanks`です。
:::
:::tip
- パスワードポリシーは[サイト管理](/ja/docs/management/site-settings/)の「ログイン」項目から設定可能です。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fd4c75ae56f4e93d5326bdba41be5c72.png)
:::

## 関連ドキュメント
- [メンバー詳細設定](/ja/docs/management/new-member-settings/)
- [メンバーアップロード](/ja/docs/management/member-upload/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [メンバーを追加する](/ja/docs/tutorials/how-to-add-new-member/)
- [メンバー登録後メールが届きません。設定方法を教えてください。](/ja/docs/faq/how-do-i-set-up-member-registration-confirmation-emails/)


---

# お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？

> 元ページ: `faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/
> 概要: フォーム編集画面より、フィールドに変数`{$inquiry_bn_id}`を記入すると、メールに問い合わせNoを表示することができます。

フォーム編集画面より、下記フィールドに変数`{$inquiry_bn_id}`を記入すると、メールに問い合わせNoを表示できます。

- 「お礼メール送信」の「タイトル」フィールド
- 「お礼メール送信」の「内容」フィールド
- 「配信先メールアドレス」の「タイトル」フィールド

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/db34a50d040439c06f971f8468f79ddc.png)
## 関連ドキュメント
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)


---

# 問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？

> 元ページ: `faq/how-do-i-include-content-details-in-the-thankyou-email` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/
> 概要: 可能です。フォーム基本設定の「お礼メール送信」にSmartyで記述してください。

可能です。  
お礼メールからもKurocoのAPIを呼び出せるので、[カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)を参考に
コンテンツ情報を取得してください。

### 記述例
```
お問い合わせありがとうございます。
Kurocoのサービス資料は以下をご確認ください。
{assign_array var='method_params'            values=''}
{assign       var='method_params.topics_id'  value='98'}
{api_method
    var='topics'
    model='Topics'
    method='details'
    version='1'
    method_params=$method_params
}
Kurocoサービス資料：{$topics.details.ext_14.url}
```

## 関連FAQ
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)

## 関連ドキュメント
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)


---

# 問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？

> 元ページ: `faq/how-do-i-include-inquiry-details-in-the-thankyou-email` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/
> 概要: はい、可能です。問い合わせのお礼メールに、お客様が入力した内容を転載する2通りの方法を紹介します。

お礼メールに内容を転載するには、2通りの方法があります。  
下記の記述を[フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)の「お礼メール送信」の「内容」フィールドに入力ください。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d3aebb44823f4f06897496a8226ecef7.png)
## foreachを利用しない方法
```
項目のタイトル:{$items.ここにはIDを入力.value}  
```

### サンプルコード：
```php
お名前:{$items.name.value}
メールアドレス:{$items.email.value}
日付:{$items.ext_01.value} ※IDが[ext_01]の場合
100文字メッセージ:{$items.ext_04.value} ※IDが[ext_04]の場合
```

## foreachを利用する方法

### サンプルコード：
```php
{foreach from=$items key=key item=item}
{if $key == 'name'} 
【{$item.title}】{$item.value} 
{/if}
{/foreach} 
```

## 関連FAQ
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)

## 関連ドキュメント
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？](/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)


---

# 問い合わせのお礼メールに、ログインユーザーの情報を転載することはできますか？

> 元ページ: `faq/how-do-i-include-user-details-in-the-thankyou-email` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-include-user-details-in-the-thankyou-email/
> 概要: 可能です。フォーム基本設定の「お礼メール送信」にSmartyで記述してください。

以下2つの方法で対応が可能です。 
- [assign_member_detailのプラグインでメンバー情報をアサインして利用する](#assign_member_detailのプラグインでメンバー情報をアサインして利用する)
- [InquiryMessage::send のエンドポイントにmember_info_flg true の設定をする](#inquirymessagesend-のエンドポイントにmember_info_flg-true-の設定をする)

また、どちらの方法もお礼メールだけでなく、管理者宛通知メールにも可能です。  

## assign_member_detailのプラグインでメンバー情報をアサインして利用する
### 設定方法
1. [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/#基本設定項目一覧)のお礼メールに以下のsmartyの記述をする。<br/>`{assign_member_detail var=member_detail member_id=$smarty.session.member_id}`

2. member_detail.name1 などで呼び出す。

### 記述例
```
お問い合わせありがとうございます。

{assign_member_detail var=member_detail member_id=$smarty.session.member_id} 

お問い合わせ頂いた方の詳細:
Family name: {$member_detail.name1}
Given name: {$member_detail.name2}
Member ID: {$member_detail.member_id}
```

## InquiryMessage::send のエンドポイントにmember_info_flg true の設定をする

### 設定方法
InquiryMessage::send のエンドポイントの詳細設定で、`member_info_flg`にチェックを付けます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/58906651dcb63c09f299f710dfd1af60.png)

### 記述例
`member_info_flg`にチェックがある場合、フォームの送信者がログイン済みの場合にメンバー情報が `member_info`の変数名でアサインされます。  
そのため以下のように記載してメンバー情報をメールに表示できます。
```
お問い合わせありがとうございます。

お問い合わせ頂いた方の詳細:
Family name: {$member_info.name1}
Given name: {$member_info.name2}
Member ID: {$member_info.member_id}
```

## 利用できるデータの確認
格納されている情報の一覧は`@debug_print_var`を利用して、送信されたメール本文から確認できます。  

```
{assign_member_detail var=member_detail member_id=$smarty.session.member_id}
{$member_detail|@debug_print_var}
```
```
{$member_info|@debug_print_var}
```

## 関連FAQ
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/#inquiryinquiry_contact_simple/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [お礼メールや通知メールに問い合わせNoを表示させたいのですができますか？](/ja/docs/faq/how-do-i-display-inquiry-numbers-in-thankyou-emails-and-notifications/)
- [フォーム項目の選択肢によって管理者宛通知の宛先を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-destination-of-the-email-recipients-depending-on-the-item-choices/)

## 関連ドキュメント
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [問い合わせのお礼メールに、コンテンツの情報を紐づけできますか？](/ja/docs/faq/how-do-i-include-content-details-in-the-thankyou-email/)
- [フォーム毎に管理者宛通知メールの内容を変えることはできますか？](/ja/docs/faq/how-can-i-change-the-content-of-the-notification-e-mail-for-each-form/)


---

# フォームの回答を1ユーザー1回までにできますか？

> 元ページ: `faq/how-to-limit-form-responses-to-once-per-user` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-limit-form-responses-to-once-per-user/
> 概要: 対象のユーザーが回答を送付済みか否かを判別するためのエンドポイントを作成し、そのレスポンスによってフロントエンドの表示を切り替えるように対応してください。

対象のユーザーが回答を送付済みか否かを判別するためのエンドポイントを作成し、そのレスポンスによってフロントエンドの表示を切り替えるように対応してください。

## 設定例
### エンドポイント

Kuroco管理画面で以下のエンドポイントを作成します。
回答がされていない場合は`pageInfo.totalCnt`のレスポンスが0となります。

|項目|設定内容|
|:--|:--|
|パス|check_answer|
|カテゴリ|フォーム|
|モデル|InquiryMessage|
|オペレーション|list|
|inquiry_id|対象のフォームID|
|self_only|チェックを入れる|
|cnt|1|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe6a4be07625feee631f36220880f239.png)  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9a99a41be482f8d219cf97566a7e567.png)

### フロントエンドの記述例
#### 回答済みの場合にフォームの項目自体を非表示にする
例えば、以下のように記述すると回答済みの場合はフォームの項目自体が表示されなくなります。

```markup
<template>
  <div>
    <div v-if="hadSubmitted.pageInfo.totalCnt == 0">
      <form>
        ・・・
        フォーム項目の表示
        ・・・
      </form>
    </div>
    <div v-else>
      回答済みです。
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    return {
      response: await $axios.$get('/rcms-api/1/inquiry/1'),
      hadSubmitted: await $axios.$get('/rcms-api/1/check_answer'),
    };
  },
  methods: {
    async handleOnSubmit() {
      ・・・
      フォームの送信処理
      ・・・
    }
  }
};
</script>
```

#### 回答済みの場合にフォーム送信ボタンをdisabledにする
フォームの項目は表示したまま、回答済みの場合はフォームのボタンをdisabledにする場合は以下のようにボタン部分の表示を変更します。

```markup 
<template>
  <div>
    <form>
      ・・・
      フォーム項目の表示
      ・・・
      <button v-if="hadSubmitted.pageInfo.totalCnt == 0" @click.prevent="handleOnSubmit">
        送信する
      </button>
      <button v-else disabled>
        回答済み
      </button>
    </form>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    return {
      response: await $axios.$get('/rcms-api/1/inquiry/1'),
      hadSubmitted: await $axios.$get('/rcms-api/1/check_answer'),
    };
  },
  methods: {
    async handleOnSubmit() {
      ・・・
      フォームの送信処理
      ・・・
    }
  }
};
</script>
```

#### 回答済みの場合に、フォーム送信時にエラーを返す
上記2つの場合は、回答前にフォームを2つ開いておくことで二重回答が可能です。   
回答の送信時にチェックを行うには以下のようにします。  

```markup 
<template>
  <div>
    <form>
      ・・・
      フォーム項目の表示
      ・・・
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      error: null,
    }
  },
  async asyncData({ $axios }) {
    return {
      response: await $axios.$get('/rcms-api/1/inquiry/1'),
    };
  },
  methods: {
    async handleOnSubmit() {
      const hadSubmitted = await this.$axios.$get('/rcms-api/1/check_answer')
      if (hadSubmitted.pageInfo.totalCnt == 0){
        ・・・
        フォームの送信処理
        ・・・
      }
      else{
        this.error = "回答済みです";
      }
    }
  }
};
</script>
```

## 関連ドキュメント
- [KurocoとNuxt.jsで、フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)


---

# カスタム処理やメッセージひな形でインデントが空白で反映されてしまいます

> 元ページ: `faq/indentation-is-reflected-as-spaces-in-custom-functions-or-message-templates` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/indentation-is-reflected-as-spaces-in-custom-functions-or-message-templates/
> 概要: カスタム処理やメッセージひな形でSmartyを使うと任意の処理を追加できて便利ですが、インデントが空白で反映されてしまうことがあります。以下のような方法をお試しください。

HTML コードに含まれたホワイトスペースや改行がブラウザの表示に影響を及ぼす問題に何度も遭遇した事があると思います。問題を回避するには、テンプレートの全てのタグを連ねて記述する必要があります。しかしこれでは大変読みづらく管理しにくいテンプレートになってしまいます。

`{strip}{/strip}` タグで囲むと、各行の先頭と終端にある余分なホワイトスペースや改行を除去できますので、こちらを利用してください。


以下に、メッセージひな形とカスタム処理での使用例を示します。

メッセージひな形の例：

```smarty
{strip}
    {assign_member_detail var='varname' member_id=$smarty.session.member_id assign_group_flg=true}
    {foreach from=$varname.arrGroup_nm key=key item=groupName}
        {if $groupName == "Administrator"}
            {assign var=g_name value=$groupName}
        {/if}
    {/foreach}
{/strip}
RCMS-X-SUBJECT: An inquiry has been received from a member of {$g_name}.
```

カスタム処理の例：

```smarty
{strip}
    {if $log_history.pageInfo.totalCnt == 1}
        {capture name=mail_body}
            A login from a new IP address has been detected.
            Please verify if it was you.

            IP Address: {$current_log.login_history_list[1].ip_address}
            Date and Time: {$current_log.login_history_list[1].login_ymdhi}
            Admin Panel URL: {$smarty.const.ROOT_MNG_URL}/management/
        {/capture}

        {sendmail
            var='result'
            to=$smarty.session.email
            subject="Login detected from a new IP address."
            contents=$smarty.capture.mail_body}

        {logger
            msg1="Login detected from a new IP address."
            msg2=$current_log.login_history_list[1]}
    {/if}
{/strip}
```

:::tip
stripの詳細は[Kuroco ドキュメントの Smarty プラグイン](/ja/docs/reference/smarty-plugin/#strip)をご確認ください。
:::

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [カスタム処理](/ja/docs/management/function/)
- [メッセージひな形](/ja/docs/management/email-template/)
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)
