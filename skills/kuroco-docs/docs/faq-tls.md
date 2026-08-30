# Kurocoドキュメント: FAQ / tls

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？（`can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta`）
- フロントエンドサーバーを自前で準備する場合に、TLS証明書を準備してもらうことは出来ますか？（`can-you-provide-tls-certificates-for-my-own-frontend-servers`）
- SSL証明書は独自に取得する必要はありますか（`do-i-need-an-ssl-certificate`）
- フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください（`how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta`）
- SSL証明書がきちんと設定されているか、確認することはできますか？（`how-do-i-verify-my-ssl-certificate-installation`）
- TLS証明書の認証局を教えてください（`which-authority-issues-the-tls-certificates`）
- TLS証明書の更新や管理は誰が行うのか教えてください（`who-updates-and-manages-the-tls-certificates`）


---

# フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？

> 元ページ: `faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/
> 概要: 基本的には、フロントエンドサーバーにKurocoFrontを利用する場合、TLS証明書はディバータで準備します。ただしご希望の場合には、証明書の設置作業1回ごとにSSL設定管理費用 55,000円(税込) をお支払いいただくことなどを条件に、任意の証明書の設置が可能です。

基本的には、フロントエンドサーバーにKurocoFrontを利用する場合、TLS証明書はディバータで準備します。  
ただしご希望の場合には以下の条件で任意の証明書の設置が可能です。

- お客様でお持ちの証明書一式(証明書・中間証明書・秘密鍵)を弊社にご提供いただく。
- 証明書の有効期限の管理はお客様にて実施いただく。
- SSL設定管理費用 55,000円(税込) を、証明書の設置作業1回ごとにお支払いいただく。

:::caution
SSL設定管理費用は初回設置時のみの費用ではありません。  
SSL証明書の最大有効期限の短縮に伴い、証明書の更新（設定作業）1回ごとに 55,000円(税込) が毎回発生いたします。  
たとえば証明書を年間で複数回更新される場合は、更新の都度この費用が発生し、55,000円(税込) × 更新回数 となります。  
なお、認証局都合による証明書の入れ替えについては、その回の上記費用に含みます（追加費用は発生しません）。
:::

:::note
証明書をお持ち込みいただく場合でもドメインの所有権確認は必要です。  
そのため、[環境設定] → [独自ドメイン/TLS証明書] にて、ドメインおよびDNSの設定を行っていただく必要があります。
:::

対応を希望する場合は[問合せフォーム](/ja/docs/about/support/#3-問合せフォーム)からお問い合わせください。

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください](/ja/docs/faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta/)
- [フロントエンドサーバーを自前で準備する場合に、TLS証明書を準備してもらうことは出来ますか？](/ja/docs/faq/can-you-provide-tls-certificates-for-my-own-frontend-servers/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)
- [TLS証明書の更新や管理は誰が行うのか教えてください](/ja/docs/faq/who-updates-and-manages-the-tls-certificates/)


---

# フロントエンドサーバーを自前で準備する場合に、TLS証明書を準備してもらうことは出来ますか？

> 元ページ: `faq/can-you-provide-tls-certificates-for-my-own-frontend-servers` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-you-provide-tls-certificates-for-my-own-frontend-servers/
> 概要: 申し訳ございませんが、フロントエンドサーバーをお客様側で用意される場合には、TLS証明書をディバータで取得してお渡しすることは出来ません。

申し訳ございませんが、フロントエンドサーバーをお客様側で用意される場合には、TLS証明書をディバータで取得してお渡しすることは出来ません。  
お手数をおかけいたしますがTLS証明書もお客様側でご用意ください。

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [SSL証明書は独自に取得する必要はありますか](/ja/docs/faq/do-i-need-an-ssl-certificate/)
- [フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください](/ja/docs/faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta/)
- [フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？](/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/)
- [TLS証明書の更新や管理は誰が行うのか教えてください](/ja/docs/faq/who-updates-and-manages-the-tls-certificates/)


---

# SSL証明書は独自に取得する必要はありますか

> 元ページ: `faq/do-i-need-an-ssl-certificate` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/do-i-need-an-ssl-certificate/
> 概要: フロントエンドサーバーにKurocoFrontを利用する場合、SSL証明書は無料で発行されます。フロントエンドサーバーをお客様にてご準備いただく場合は、SSL証明書もお客様にてご準備をお願いいたします。

フロントエンドサーバーにKurocoFrontを利用する場合、SSL証明書は無料で発行されますのでお客様にて取得いただく必要はございません。  
ただし、ご希望の場合はエンジニア作業 55,000円(税込)で任意の証明書を設置するオプションを準備しております。  

:::tip
KurocoFrontはCDNを利用した静的コンテンツホスティングサービスです。詳細は[KurocoFrontについて](/ja/docs/about/kurocofront/)をご確認ください。
:::

フロントエンドサーバーをお客様にてご準備いただく場合は、SSL証明書もお客様にてご準備をお願いいたします。

SSL証明書については、下記ドキュメントを併せてご参照ください。

- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)
- [フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください](/ja/docs/faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta/)
- [フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？](/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/)

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください](/ja/docs/faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta/)
- [フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？](/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/)
- [フロントエンドサーバーを自前で準備する場合に、TLS証明書を準備してもらうことは出来ますか？](/ja/docs/faq/can-you-provide-tls-certificates-for-my-own-frontend-servers/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)


---

# フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください

> 元ページ: `faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta/
> 概要: フロントエンドサーバーにKurocoFrontを利用する場合は、SSL証明書の取得もディバータで対応します。

フロントエンドサーバーにKurocoFrontを利用する場合は、SSL証明書の取得もディバータで対応します。  
ドメインを確定後、弊社で指定するTLS取得用のDNSレコードを、DNSサーバーにセットしていただく必要があります。  
なお、CSRの発行は不要です。

- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)
- [SSL証明書は独自に取得する必要はありますか](/ja/docs/faq/do-i-need-an-ssl-certificate/)
- [フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？](/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/)

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)
- [TLS証明書の更新や管理は誰が行うのか教えてください](/ja/docs/faq/who-updates-and-manages-the-tls-certificates/)
- [SSL証明書は独自に取得する必要はありますか](/ja/docs/faq/do-i-need-an-ssl-certificate/)
- [フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？](/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/)


---

# SSL証明書がきちんと設定されているか、確認することはできますか？

> 元ページ: `faq/how-do-i-verify-my-ssl-certificate-installation` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-verify-my-ssl-certificate-installation/
> 概要: DigiCertが提供している[SSL Installation Diagnostics Tool]で、設定状況をご確認いただけます。

DigiCertが提供している[SSL Installation Diagnostics Tool](https://www.digicert.com/help/)で、設定状況をご確認いただけます。

## SSL TOOLS利用手順

### 1. SSL Installation Diagnostics Toolへアクセス  
[SSL Installation Diagnostics Tool](https://www.digicert.com/help/)へアクセスします。

### 2. ドメイン検索欄にドメイン入力    
設定状態を確認したいドメインを入力して[CHECK SERVER]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d91a00bd82623d6d43d138be0092af49.png)
### 3. 設定状態の結果  
結果が表示されます。チェックアイコンが出ていれば問題ありません。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3751ed4dcfbbe046b7a4095c03be15e3.png)
### 4. 有効期限の確認  
[TLS Certificate expiration]でSSL証明書の有効期限を確認できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3362991892e84667ff7513bcc3409c05.png)

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [SSL証明書は独自に取得する必要はありますか](/ja/docs/faq/do-i-need-an-ssl-certificate/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)
- [TLS証明書の更新や管理は誰が行うのか教えてください](/ja/docs/faq/who-updates-and-manages-the-tls-certificates/)


---

# TLS証明書の認証局を教えてください

> 元ページ: `faq/which-authority-issues-the-tls-certificates` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/which-authority-issues-the-tls-certificates/
> 概要: TLSサーバー証明書の認証局はLet’s Encrypt になります。

KurocoFrontが標準で提供しているTLSサーバー証明書の認証局はLet’s Encrypt になります。  
Let's Encryptについては[公式サイト](https://letsencrypt.org/ja/)をご参照ください。

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [TLS証明書の更新や管理は誰が行うのか教えてください](/ja/docs/faq/who-updates-and-manages-the-tls-certificates/)
- [SSL証明書は独自に取得する必要はありますか](/ja/docs/faq/do-i-need-an-ssl-certificate/)
- [フロントエンドサーバーにKurocoFrontを利用する場合で、特定の証明書を使いたいとき、証明書持ち込みは出来ますか？](/ja/docs/faq/can-i-import-tls-certificates-into-frontend-servers-provided-by-diverta/)
- [SSL証明書がきちんと設定されているか、確認することはできますか？](/ja/docs/faq/how-do-i-verify-my-ssl-certificate-installation/)


---

# TLS証明書の更新や管理は誰が行うのか教えてください

> 元ページ: `faq/who-updates-and-manages-the-tls-certificates` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/who-updates-and-manages-the-tls-certificates/
> 概要: TLS証明書取得用のDNSレコードが有効であれば、Kurocoが自動的に更新します。KurocoのTLS証明書はLet’s Encryptを利用しております。

TLS証明書取得用のDNSレコードが有効であれば、Kurocoが自動的に更新します。  
KurocoのTLS証明書はLet’s Encryptを利用しております。

## 証明書の管理について
Let’s Encrypt は、90日間有効な証明書を発行します。  
Kurocoは、約30日前にDNSレコードの再検証と証明書更新を実施します。  
TLS証明書取得用のDNSレコードがKuroco指定のものになっていない場合、またはCAAレコードがLet's Encryptをブロックしている場合は、90日間の最終日に証明書は失効します。  
有効期限が切れる30日前に、Kurocoより有効期限切れが間近であることをメールで通知します。  

正しいTLS証明書取得用のDNSレコードが設定されており、CAAレコードによるブロックもしていないにもかかわらず更新失敗となる場合は、お手数ですが[サポート](/ja/docs/about/support/)までご連絡ください。

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [TLS証明書の認証局を教えてください](/ja/docs/faq/which-authority-issues-the-tls-certificates/)
- [SSL証明書は独自に取得する必要はありますか](/ja/docs/faq/do-i-need-an-ssl-certificate/)
- [フロントエンドサーバーにKurocoFrontを利用する場合のTLS証明書の取得について教えてください](/ja/docs/faq/how-do-i-obtain-tls-certificates-for-frontend-servers-provided-by-diverta/)
- [SSL証明書がきちんと設定されているか、確認することはできますか？](/ja/docs/faq/how-do-i-verify-my-ssl-certificate-installation/)
