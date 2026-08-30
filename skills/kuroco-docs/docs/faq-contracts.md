# Kurocoドキュメント: FAQ / contracts

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- カスタム処理で呼び出したAPIの利用料について教えてください（`api-usage-fees-for-custom-processing`）
- 一定額を超えた場合、自動で利用停止する機能はありますか（`can-i-automatically-suspend-usage-when-costs-exceed-a-certain-amount`）
- メール送信の料金はSendGridと契約していても発生しますか？（`do-i-have-to-pay-for-sending-emails-even-if-i-use-sendgrid`）
- Kuroco利用料の無料枠の計算方法を教えてください（`how-do-i-calculate-my-free-limit`）
- Kuroco利用料の支払方法を教えてください（`how-do-i-pay-the-kuroco-fee`）
- Kurocoの解約について（`how-do-i-terminate-my-contract`）
- どのようなときに従量課金として計上されますか（`how-much-does-kuroco-cost`）
- 契約者・管理者の情報を変更したいです。手続きを教えてください。（`i-need-to-change-contractor-or-admin-details-how-do-i-proceed`）
- 請求書の発行日を教えてください（`what-is-the-invoice-issue-date`）


---

# カスタム処理で呼び出したAPIの利用料について教えてください

> 元ページ: `faq/api-usage-fees-for-custom-processing` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/api-usage-fees-for-custom-processing/
> 概要: APIにリクエストを送った場合は、カスタム処理から内部的にAPIを利用した場合でも、キャッシュされていないAPI、もしくはキャッシュされたAPIの利用料が発生します。ただし、ネットワーク(https)を経由せず内部的にAPIリクエストを実行した場合は加算されません。

APIにリクエストを送った場合は、カスタム処理から内部的にAPIを利用した場合でも、キャッシュされていないAPI、もしくはキャッシュされたAPIの利用料が発生します。  
ただし、ネットワーク(https)を経由せず内部的にAPIリクエストを実行した場合は加算されません。

主なSmartyプラグインと費用発生の有無は以下になります。

## SmartyプラグインによるAPIリクエストの費用

|Smartyプラグイン|リクエスト方法|APIリクエストの費用|
|:--|:--|:--|
|`{api}`|ネットワーク経由| 外部APIへのリクエストの場合は発生しません。<br/>KurocoのAPIにリクエストを送った場合は対象のエンドポイントのリクエスト数にカウントされます。|
|`{api_internal}`|ネットワーク経由| 発生する|
|`{api_internal}`(direct=trueを指定)|内部リクエスト| 発生しない|
|`{api_method}`|内部リクエスト|発生しない|
|`{api_mng}`|内部リクエスト| 発生しない|

:::caution
内部的なAPIリクエストは高速に動作しますが、連続的に何回も実行するとAPIの実行時間が長くなります。  
これらの実行時間がコンピューティング料金に影響しますので、ご注意ください。
:::

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [コンピューティングの料金計上例](/ja/docs/about/how-much-does-kuroco-cost/#コンピューティングの料金計上例)


---

# 一定額を超えた場合、自動で利用停止する機能はありますか

> 元ページ: `faq/can-i-automatically-suspend-usage-when-costs-exceed-a-certain-amount` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-automatically-suspend-usage-when-costs-exceed-a-certain-amount/
> 概要: 任意の金額を指定して自動的に利用を停止する機能はありません。指定金額を超えた場合にメールで通知する「月次費用監視アラート閾値」をご利用ください。

任意の金額を指定して、超過時に自動的に利用を停止する機能はありません。  
費用の増加に気づけるようにするための機能として、「月次費用監視アラート閾値」をご用意しています。金額を設定すると、月次費用が設定金額を超えた場合にメールで通知されます。通知後も、APIやバッチ処理は停止せず、そのまま稼働します。

## 月次費用監視アラート閾値の設定方法

1. [環境設定] -> [アカウント設定]をクリックします。
2. [月次費用監視アラート閾値]に、通知を受け取りたい金額（円）を入力します。`0`を入力すると、通知は行われません。
3. [更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8ac96258b13f34886816d4e6b3c8efb7.png)

設定した金額は、[環境設定] -> [請求情報]の[月次費用監視アラート閾値]でも確認できます。[設定]をクリックすると[アカウント設定](/ja/docs/management/account/)に遷移します。

## 通知先のメールアドレス

アラートは、以下の3か所に登録されているメールアドレスに届きます。

- [アカウント設定]の[メールアドレス]に表示されている、Kurocoの申込者のメールアドレス（管理画面からは変更できません）
- [アカウント設定]の[メールアドレス]の入力欄に登録したメールアドレス（改行区切りで複数登録できます）
- [請求情報]の[メール通知]にある[請求情報送付先メールアドレス]

:::info
無料枠を超過した場合の扱いは、上記のアラートとは別の仕様です。Kuroco利用料は毎日チェックされ、無料枠分の利用を超えるとメンテナンスモードが自動的にONになります。クレジットカードを登録すると、無料枠分超過によるメンテナンスモードを解除できるようになります。詳細は[請求情報](/ja/docs/management/site-payment/)をご確認ください。
:::

:::tip
費用そのものを抑えたい場合は、[Kuroco利用料の最適化](/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/)もあわせてご確認ください。  
意図的に稼働を止めたい場合は、[アカウント設定](/ja/docs/management/account/)の[メンテナンスの設定]を手動でONにする方法があります。この場合、APIエンドポイントは503 Service Unavailableを返し、バッチ処理の実行も停止します。
:::

## 関連ドキュメント
- [アカウント設定](/ja/docs/management/account/)
- [請求情報](/ja/docs/management/site-payment/)
- [利用状況](/ja/docs/management/usage/)
- [Kuroco利用料の最適化](/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/)
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)


---

# メール送信の料金はSendGridと契約していても発生しますか？

> 元ページ: `faq/do-i-have-to-pay-for-sending-emails-even-if-i-use-sendgrid` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/do-i-have-to-pay-for-sending-emails-even-if-i-use-sendgrid/
> 概要: Sendgridは独自ドメインでメールを送信するため利用するものになりますので、SendGridと契約・接続していてもKurocoのメール送信の料金は引き続き発生します。

Sendgridは独自ドメインでメールを送信するため利用するものになりますので、
SendGridと契約・接続していてもKurocoのメール送信の料金は引き続き発生します。  

料金体系は下記をご覧ください。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2fae9dcb10b8aa710d7790e7e655dec0.png)
参考: [Kuroco説明資料 P.18](https://kuroco.app/files/sheets/ja/kuroco_salessheet.pdf)

## 関連ドキュメント
- [SendGrid](/ja/docs/management/sendgrid/)
- [SendGrid連携方法](/ja/docs/tutorials/how-to-link-sendgrid/)
- [どのようなときに従量課金として計上されますか](/ja/docs/about/how-much-does-kuroco-cost/)
- [Kuroco利用料の無料枠の計算方法を教えてください](/ja/docs/faq/how-do-i-calculate-my-free-limit/)
- [メール配信時の件数制限はありますか。](/ja/docs/faq/is-there-a-limit-to-the-number-of-e-mails-i-can-send/)


---

# Kuroco利用料の無料枠の計算方法を教えてください

> 元ページ: `faq/how-do-i-calculate-my-free-limit` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-calculate-my-free-limit/
> 概要: Kurocoのご利用には無料枠を設けており、環境設定内の利用状況にて表示されるご利用料（総額）から、無料枠分を差し引いた金額をご請求させて頂いております。無料枠分は日次で設定しており、37円/日で計算しております。このため月によって無料枠の金額は変動致します。

## 無料枠について
Kurocoのご利用には無料枠を設けており、環境設定内の利用状況にて表示されるご利用料（総額）から、無料枠分を差し引いた金額をご請求させて頂いております。  
無料枠分は日次で設定しており、37円/日で計算しております。このため月によって無料枠の金額は変動致します。  
※Kuroco管理画面の金額は税込み表示となります。

### （例）該当月が31日であった場合
例えば、該当の月が31日まである場合は以下の計算方法となります。  
- ご利用料（総額）：10,000円 - 無料枠分：1,147円（37円×31日）= ご請求金額：8,853円（税込）

## 関連ドキュメント
- [利用料金](https://kuroco.app/ja/pricing/)
- [請求情報](/ja/docs/management/site-payment/)
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)
- [請求書の発行日を教えてください](/ja/docs/faq/what-is-the-invoice-issue-date/)


---

# Kuroco利用料の支払方法を教えてください

> 元ページ: `faq/how-do-i-pay-the-kuroco-fee` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-pay-the-kuroco-fee/
> 概要: Kuroco利用料はクレジットカード払いとなります。

## 支払方法
Kuroco利用料はクレジットカード払いとなります。  
[環境設定]->[[請求情報](/ja/docs/management/site-payment/)]からクレジットカードの登録をお願いします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d8217aa64032c2c44f1609eaf9e4250.png)

:::tip
日本企業のみ請求書払いの対応が可能です。  
ご希望の場合は[問い合わせフォーム](/ja/docs/about/support/#3-問合せフォーム)からご連絡をお願いします。  
:::

## その他注意事項
- 対象月の請求金額が50円未満の請求の場合は翌月に繰り越し請求となります。
- 領収書はKuroco管理画面より取得が可能です。

## 関連ドキュメント
- [Kuroco利用料の無料枠の計算方法を教えてください](/ja/docs/faq/how-do-i-calculate-my-free-limit/)
- [Kurocoの解約について](/ja/docs/about/how-do-i-terminate-my-contract/)


---

# Kurocoの解約について

> 元ページ: `faq/how-do-i-terminate-my-contract` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-terminate-my-contract/
> 概要: ご解約をご希望の際には、Kuroco管理画面の[環境設定]->[アカウント設定]の[サイトの削除]から手続きをお願いいたします。

## 解約方法
ご解約をご希望の際には、Kuroco管理画面の[環境設定]->[アカウント設定]の[サイトの削除]から手続きをお願いいたします。

[環境設定]->[アカウント設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/31e64b5b45352a6698933e4fb415b756.png)
[サイトの削除のページへ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8f79fcc0c202b25b8f58b2d110559c0.png)
「サービスを解約し、これまで構築したサイトやコンテンツが消去されることに同意します。」にチェックを入れて[サイトコンテンツを消去する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/98f5c7b0265a3aab2b9272d07d404d81.png)
:::caution
サブサイトが残っている場合はサイトの削除ができません。  
[サイト一覧](/ja/docs/management/site-list/)からサブサイトを全て削除後にご対応をお願いします。
:::

## 解約の際の注意点
- Kuroco管理画面にログインできなくなります。
- 解約後のデータ復元はできません。
- アカウントを削除した後、デプロイ済みのKurocoFrontが削除されるまでに時間差が生じる場合があります。
  希望の日時で404の表示にしたい場合は以下のドキュメントを参考にご対応ください。  
  [デプロイしたサイトの表示を404に戻すことはできますか？](/ja/docs/faq/is-it-possible-to-revert-the-deployed-site-to-display-a-404-error/)

## 解約にあたって確認事項がある場合
解約に関してご不明点等がある場合は、[お問い合わせフォーム](https://kuroco.zendesk.com/hc/ja)からご連絡ください。 

## 関連ドキュメント
- [アカウント設定](/ja/docs/management/account/)
- [サイト一覧](/ja/docs/management/site-list/)
- [デプロイしたサイトの表示を404に戻すことはできますか？](/ja/docs/faq/is-it-possible-to-revert-the-deployed-site-to-display-a-404-error/)
- [契約者・管理者の情報を変更したいです。手続きを教えてください。](/ja/docs/faq/i-need-to-change-contractor-or-admin-details-how-do-i-proceed/)


---

# どのようなときに従量課金として計上されますか

> 元ページ: `faq/how-much-does-kuroco-cost` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-much-does-kuroco-cost/
> 概要: Kurocoは従量課金モデルとなります。そのため、毎月ご利用分のみお支払いいただくようになります。料金体系は下記をご覧ください。

Kurocoは従量課金モデルとなります。そのため、毎月ご利用分のみお支払いいただくようになります。  
料金体系は下記をご覧ください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2fae9dcb10b8aa710d7790e7e655dec0.png)
参考: [Kuroco説明資料 P.18](https://kuroco.app/files/sheets/ja/kuroco_salessheet.pdf)

## コンピューティングの料金計上例
「コンピューティング」に「0.0132円/1000ミリ秒」とありますが、APIで300msを超えるようなレスポンスがあった場合や、バッチ処理の処理時間が計上されます。  

例えば、KurocoはSmartyを利用できるので、ご自身である程度自由に処理を作ることが出来ます。 
そのため、下記のような処理を作成・利用すると料金計上される可能性がございます。
 
- ZIPファイルをアップロードして、ZIPの解凍をする処理
- 外部APIを定期的に叩いて何らかの処理をする
- 大量の配信をする
- APIにカスタム処理を入れて複雑な処理をして、300msを超えるレスポンスのAPIを作成する

:::tip
バッチ処理についての詳細は下記をご確認ください。  
- [バッチ処理](/ja/docs/tutorials/how-to-use-batch/) 

APIに設定するカスタム処理については下記をご確認ください。
- [前処理](/ja/docs/reference/pre-processing/)
- [後処理](/ja/docs/reference/post-processing/)
:::

:::info
現在、管理画面（ブラウザでの操作）自体の処理時間は費用に計上されません。ただし、AIエージェントの実行時間（[AIエージェント](/ja/docs/management/ai-agent/)）や、管理API・MCPへのリクエスト処理時間（[利用状況](/ja/docs/management/usage/)の「管理API・MCP処理時間」）は、コンピューティングとして課金対象です。また、今後、トリガーによって動作するカスタム処理の処理時間も、バッチ処理と同様に計上される予定になっております。
:::

## ファイルストレージ
ファイルストレージにはログ容量やDBファイル容量が含まれるため、アカウント発行直後でも0円にはなりません。

## CDN転送量
CDN転送量は、以下のデータ転送量に基づいて計上されます。

- KurocoFrontからのコンテンツ配信
- KurocoFilesからのファイル配信
- APIのレスポンス

404エラー(ページが見つからない)のレスポンスにもレスポンスサイズが存在するため、KurocoFrontにアクセスがある限り、最低単位の110円が発生します。

## 無料枠について

Kurocoは、毎月1100円(税込)までは無料でご利用になれます。

管理画面を見てみたい、試しにAPIを作成してみたい、というレベルであれば無料枠を超えることはございません。また、最初はクレジットカード登録の必要がないので、ご安心して一度お試しください。
- [Kuroco を試してみる](https://kuroco.app/ja/free_trial/)

## 料金の確認方法
詳細な利用料金は、[環境設定] -> [利用状況]より確認できます。  
詳しくは、管理画面マニュアル -> [利用状況](/ja/docs/management/usage/)をご確認ください。

## 関連ドキュメント
- [利用状況](/ja/docs/management/usage/)
- [請求情報](/ja/docs/management/site-payment/)
- [Kuroco利用料の最適化](/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/)
- [Kuroco利用料の無料枠の計算方法を教えてください](/ja/docs/faq/how-do-i-calculate-my-free-limit/)
- [Kuroco利用料の支払方法を教えてください](/ja/docs/faq/how-do-i-pay-the-kuroco-fee/)
- [カスタム処理で呼び出したAPIの利用料について教えてください](/ja/docs/faq/api-usage-fees-for-custom-processing/)


---

# 契約者・管理者の情報を変更したいです。手続きを教えてください。

> 元ページ: `faq/i-need-to-change-contractor-or-admin-details-how-do-i-proceed` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/i-need-to-change-contractor-or-admin-details-how-do-i-proceed/
> 概要: 次の箇所の登録情報を確認し、必要に応じて更新してください。

次の箇所の登録情報を確認し、必要に応じて更新してください。  

### member_id=1のメンバー情報
[メンバー管理]->[[メンバー](/ja/docs/management/member/)]に、アカウントの作成者がmember_id=1として登録されています。  
id=1のメンバーは削除ができませんので、お名前やメールアドレスなど必要な情報を更新してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b85bb5fbbad1d077a5cbc13229db55b2.png)

### アカウント設定
[環境設定]->[[アカウント設定](/ja/docs/management/account/)]に、アカウント作成時に入力した「メールアドレス」「会社名」「名前」が登録されています。  
こちらはユーザー側で変更できませんので、変更を希望する場合は[サポート](/ja/docs/about/support/)までお問い合わせください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a7f4af0b71133cd6323fbc0ed528161.png)

:::info
第三者へのアカウント移管の場合、地位継承に関する覚書の提出をお願いしております。  
- [関連サービスに関するご契約 - 他社へ契約を移管したい場合](/ja/docs/about/service_request/#6-他社へ契約を移管したい場合)
:::

### クレジットカード情報
[環境設定]->[[請求情報](/ja/docs/management/site-payment/)]にお支払い用のクレジットカード情報が登録されています。  
[変更]をクリックして更新してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/984d5d6d13cef77f9128bcdac4167d9f.png)

### 外部システム連携
その他、外部システム連携をしているサービスがあり、連携するアカウントを変更する場合は各設定画面からAPIキーなどを更新してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ef8ba75314120f5a1e03d637fe3bf88.png)

:::caution
APIキーなどの連携情報を更新すると、旧アカウントに紐づいたファイル等は見れなくなる可能性があります。
:::

## 関連ドキュメント
- [メンバー](/ja/docs/management/member/)
- [アカウント設定](/ja/docs/management/account/)
- [請求情報](/ja/docs/management/site-payment/)
- [関連サービスに関するご契約](/ja/docs/about/service_request/)
- [サポート](/ja/docs/about/support/)


---

# 請求書の発行日を教えてください

> 元ページ: `faq/what-is-the-invoice-issue-date` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-the-invoice-issue-date/
> 概要: Kuroco利用料の請求書発行日は、利用対象月の翌月3営業日内となっております。

Kuroco利用料の請求書発行日は、利用対象月の翌月3営業日内となっております。

## ご請求書の発行日
締め日は月末、支払日は翌月末となりますが、対象月の翌月に利用状況の確認をしていることから、請求書の発行日は翌月の3営業日内とさせて頂いております。  
（例：2023年1月ご利用料は2023年2月3日までに発行。1月末締め、2月末払いとなります。）

Kuroco利用料は基本的にはクレジットカード支払いをお願いしておりますが、請求書払いをご希望の際にはKurocoサポートサイトよりお問い合わせをお願いいたします。  
※日本企業のみ請求書払いの対応が可能です。

- [フォームより問い合わせをする](https://kuroco.zendesk.com/)  

## ご請求書の発行方法
ご請求書の発行につきましては、BtoBプラットフォームのご利用をお願いしております。  
- （参考）[BtoBプラットフォーム](https://www.infomart.co.jp/seikyu/index.asp)

## 関連ドキュメント
- [請求情報](/ja/docs/management/site-payment/)
- [Kuroco利用料の支払方法を教えてください](/ja/docs/faq/how-do-i-pay-the-kuroco-fee/)
- [どのようなときに従量課金として計上されますか](/ja/docs/faq/how-much-does-kuroco-cost/)
- [契約者・管理者の情報を変更したいです。手続きを教えてください。](/ja/docs/faq/i-need-to-change-contractor-or-admin-details-how-do-i-proceed/)
