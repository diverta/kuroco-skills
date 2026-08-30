# Kurocoドキュメント: チュートリアル / 認証・会員（2/4）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- LINEアカウントを使用してユーザー登録を行うと同時に公式アカウントの友達登録を行う（`implementing-oauth-sp-for-line`）
- Microsoft Entra IDを使用してSCIMプロビジョニングを実装する（`implementing-scim-provisioning-with-microsoft-entra-id`）
- SPAでのSSO認証フローを実装する（`implementing-sso-login-flow-in-spa`）
- ログイン画面に2段階認証を実装する（`implementing-two-step-verification-on-login-form`）
- 会員登録画面に2段階認証を実装する（`implementing-two-step-verification-on-registration-form`）
- ログイン画面を構築する（`integrate-login`）


---

# LINEアカウントを使用してユーザー登録を行うと同時に公式アカウントの友達登録を行う

> 元ページ: `tutorials/implementing-oauth-sp-for-line` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-oauth-sp-for-line/
> 概要: LINEアカウントを使用してKurocoにユーザー登録を行うと同時に公式アカウントの友達登録を行う方法を説明します。

## 概要

LINEアカウント連携によってユーザー登録を行いたい場合、KurocoのOAuth SP機能をご利用いただけます。
OAuth SP機能には、プリセットとしていくつかの外部サービスをご用意しており、LINEもその一つです。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8185214f226eb842593fcb84319daa26.jpg)

プリセット設定を使うと簡単に設定が行えますが、詳細なカスタマイズはできません。
例えばKurocoからの[LINEメッセージ送信機能](/ja/docs/tutorials/how-to-connect-to-line/) などを活用される場合には、ユーザー登録と同時にLINE公式アカウントへの友達登録も自動的にされていると便利ですが、LINEプリセット設定でのユーザー登録ではそれが出来ません。  

ここではKurocoのOAuth SP機能のカスタム設定を用いて、LINEアカウント連携によるKurocoにユーザー登録を行い、同時に公式アカウントの友達登録を行う方法を説明します。

### 学べること
以下の手順で、KurocoのOAuth SPでログインした際にLINE公式アカウントを友達登録させる方法を学びます。  

- [Kurocoの設定](#kurocoの設定)
- [LINE Developersコンソール上での設定](#line-developersコンソール上での設定)
- [動作確認](#動作確認)

### 前提条件

このページは、LINE Developersコンソールにてプロバイダーおよびチャンネル（Messaging API）が設定済みであることを前提としています。  
まだ設定していない場合は、下記のチュートリアルを参照してください。  
- [LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)

## Kurocoの設定

### メンバー詳細設定

まず、メンバーの情報にLINEアカウントと紐付けるためのLINE ID情報を保持できるように設定します。
サイドバーから[メンバー管理]を選択、上部のプルダウンより[メンバー詳細設定]を選択しメンバー詳細設定画面を表示します。  
[登録されるメンバーの拡張項目を設定する]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3e43800a61f30142c650c13bc7386a45.png)

拡張項目設定画面にてメンバー拡張項目に`Line ID`を追加し、[更新する]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cba03042c7b3e8fa85b1e513ca19cfbf.png)

### グループ設定

LINEアカウントと連携してユーザー登録したユーザーを他のユーザーと区別しておくと便利です。ここでは「LINEユーザー」というグループを作成し、そこに所属させるようにします。
グループ設定画面を開き[+追加]ボタンをクリックして、以下の項目を入力して[+追加する] ボタンをクリックします。

|項目   |設定内容  |
| :--- | :--- |
|名前|`LINEユーザー`|
|有効にする|`（チェックあり）`|
|ユーザー種別|`ログインユーザー`|
|IPアドレス制限|`（空）`|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cea3f9630a485ccc3f47ed76008aa4fa.png)

### APIの設定

セキュリティが動的トークンとなっているAPIを必ず一つ持つ必要があります。

ない場合はAPIを追加してください。
エンドポイント一覧画面を開き右上の[追加]ボタンをクリックします。  
ポップアップで以下のように設定し、[追加する]ボタンをクリックします。

|項目   |設定内容  |
| :--- | :--- |
|タイトル|`LINEユーザー向け`|
|版|`1.0`|
|説明|`LINEユーザー向け`|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8a9a684c9e707468fa9603a0e77aa08.png)

エンドポイント一覧画面上部の[セキュリティ]ボタンをクリックし、ポップアップ上の[セキュリティ]設定で[動的トークン]を選択し、[保存する]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ae07ee9d1f582a1331c9f09ab6a5f31.png)

## LINE Developersコンソール上での設定

LINE Developersコンソールで以下を設定します。  
(1) プロバイダー  
(2) チャンネル（Messaging API）  
(3) チャンネル（LINEログイン）  

(1)と(2)については[LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)をご参照ください。

### チャンネル（LINEログイン）の設定

LINE Developersコンソールにログインし、[LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)で作成したプロパイダーから、[新規チャンネル登録]の[LINEログイン]を選択し、入力フォームに従って、提供するサービスの情報を入力してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2442505006a27005a3a1f726f62bb00e.png)

設定画面を再度開くと、[リンクされたLINE公式アカウント]という欄が現れます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/03f8789bbbf17c031d54c8667b73543e.png)

LINE公式アカウントに関連付けられたMessaging APIのチャネルが、LINEログインのチャネルと同じプロバイダーに属している場合、ここで選択可能になります。該当するMessaging APIのチャネルを選択し、[更新]ボタンをクリックします。

また、作成したチャンネルのチャンネルIDが表示されますので、控えておいてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4201b4a76299a6c72911a78dad6d664.png)

Kurocoの OAuth SP設定画面にて、[+追加]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1513e335b3cca1af44f414c071ccece7.png)

フォームに以下のように設定します。

|項目   |設定内容  |
| :--- | :--- |
|OAuth SPの名称|`LINE(公式アカウント友達追加)`など、わかりやすい名前を設定してください|
|ターゲットドメイン|`API`|
|タイプ|`Custom`|
|クライアントID (Client ID)|`(LINEログインチャネルのチャネルID整数10桁)`|
|クライアントの秘密鍵 (Client Secret)|`(LINEログインチャネルのチャネルシークレット)`|
|承認URL|`https://access.line.me/oauth2/v2.1/authorize?prompt=consent&bot_prompt=aggressive`|
|トークンURL|`https://api.line.me/oauth2/v2.1/token`|
|リソースURL|`https://api.line.me/v2/profile`|
|(API用) Grantトークン生成|`LINEユーザー向け` にチェック|
|プライベート URL を使用|`（チェックなし）`|
|リターンURL（成功）|`（ログイン直後に遷移させたいフロントエンドURLを指定してください）`|
|リターンURL（エラー）|`(空)`|
|自動ユーザ登録	有効にする|有効にする：`（チェックあり）`<br/>登録時にセットされるグループ：`LINEユーザー`|
|登録フィールドとのIDPマッピング|名とマップする：`displayName`<br/>姓とマップする：`displayName`<br/>名前スプリッターを利用する：`（チェックあり）`|
|Emailを利用せずメンバー拡張項目にIDを格納してリンクする|有効にする：チェック有<br/>IDPのOpenIDキー：`userId`<br/>IDを保存するメンバー拡張項目：`LINE ID`|
|必要なデータのスコープ|`profile`<br/>`openId`|
|スコープセパレータ|`スペース' '`|
|ユーザーアクセストークンを保存|`(チェックなし)`|
|基本認証ヘッダーにクライアントの秘密鍵を送信|`(チェックなし)`|
|承認プロンプトのパラメータを送信しない|`(チェックなし)`|

### コールバックURLの設定

もう一度外部システム連携編集画面を開くと、以下のように[ログインURL] が表示されていますので、こちらを控えてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4d7937bf29bace7e7af3ecf10985c31.png)

LINE Developerコンソールのログインチャンネルの設定画面にて[LINEログイン設定]タブを開きます。  
[コールバックURL]に先ほど控えた[ログインURL]を記載して、[更新]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/12f6e34573cb55d13c86364cd9933be0.png)

設定は以上です。

## 動作確認

上述の[ログインURL]にお使いのデバイスなどでアクセスしてみましょう。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d47595c99a46713faa5aa0c5af01929.png)

LINEログインの同意画面の後に、[友だち追加]ボタンが現れます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dcf840a83909e07eaf1c0eae79250927.png)

[友だち追加]ボタンをクリックすると公式アカウントが友達に追加され、前述の [リターンURL（成功）]で設定したURLにリダイレクトされます。

## 関連ドキュメント

- [OAuth SP](/ja/docs/management/sso-oauth-sp/)
- [LINE](/ja/docs/management/line/)
- [LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)


---

# Microsoft Entra IDを使用してSCIMプロビジョニングを実装する

> 元ページ: `tutorials/implementing-scim-provisioning-with-microsoft-entra-id` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-scim-provisioning-with-microsoft-entra-id/
> 概要: このチュートリアルでは、Microsoft Entra IDを使用したSCIMプロビジョニングの実装方法について説明します。これにより、Microsoft Entra IDからKurocoへのメンバー情報の自動同期が可能になります。

このチュートリアルでは、Microsoft Entra IDを使用したSCIMプロビジョニングの実装方法について説明します。  
SCIM（System for Cross-domain Identity Management）を利用することで、Microsoft Entra IDからKurocoへのメンバーの作成・更新・削除を自動化できます。

:::info
SCIMプロビジョニングは、IdP（Microsoft Entra ID）からSP（Kuroco）へのメンバー情報の自動同期を行う機能です。SSOログイン機能とは異なります。  
SSOログインを実装する場合は、以下のドキュメントを参照してください。
- OAuth認証：[Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- IDaaS（Azure AD B2C）：[IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)
:::

## 前提条件

このチュートリアルは、以下の条件を満たしていることが前提となります。

- Microsoft Entra IDテナントアカウントを所持していること
- Microsoft Entra IDで、クラウドアプリケーション管理者以上のロールを持つアカウントであること
- Kurocoの管理画面にアクセスできること

## SCIMプロビジョニングの概要

SCIMプロビジョニングでは、以下のフローでメンバー情報の同期が行われます。

1. Microsoft Entra IDでユーザーがエンタープライズアプリケーションに割り当てられると、KurocoにSCIMプロトコルでメンバー情報が送信されます。
2. Kurocoは受信した情報をもとに、メンバーの作成・更新を自動的に行います。
3. Microsoft Entra ID側でユーザーの割り当てが解除されると、Kurocoのメンバーも無効化されます。

## メンバー拡張項目を追加する

SCIMプロビジョニングでは、Microsoft Entra IDのExternal IDをKurocoに保存するためのメンバー拡張項目が必要です。あらかじめ作成しておきます。

**1. メンバー拡張項目の設定ページにアクセスする**  
Kuroco管理画面で「メンバー一覧」の上の[メンバー]をクリックし、表示されたプルダウンメニューから、[メンバー詳細設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/294893803a353377bcc644b58bde717c.png)

**2. External SCIM ID用のメンバー拡張項目を追加する**  
[登録されるメンバーの拡張項目を設定する]から[拡張項目設定]を開き、以下の設定でメンバー拡張項目を作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7517c25e608bb530c4e99798173998e.png)

| 項目 | 値 |
| :-- | :--- |
| 項目名 | External SCIM ID（任意の名前） |
|識別子|external_scim_id（任意の名前）|
| タイプ | テキスト |

:::info
このメンバー拡張項目は、Microsoft Entra IDのユーザーオブジェクトIDを保存するために使用されます。メンバーIDでの紐付けができない場合の補助的な紐付け手段として機能します。詳細は本ドキュメント末尾の「メンバー紐付けの優先順位」を参照してください。
:::

## Kuroco管理画面でSCIM SP設定を追加する

次に、Kurocoの管理画面でSCIM SP設定を追加します。

**1. SCIM SP設定ページにアクセスする**  
[外部システム連携] -> [ID連携] -> [SCIM SP](/ja/docs/management/sso-scim-sp/)をクリックし、SCIM SP一覧ページにアクセスします。  
[追加]ボタンをクリックして新しいSCIM SPを追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d29c0b47595ff306c8a3b1a08dac21b.png)

**2. SCIM SP設定を入力する**  
SCIM SP編集ページで以下の項目を入力します。この段階では[有効にする]のチェックは外しておいてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0881449b7e6a582611884428e9bbfce7.png)

| 項目 | 値 |
| :-- | :--- |
| 有効にする | チェックを外す（後で有効にします） |
| 名前 | 任意の名前を入力します。（例：Microsoft Entra ID SCIM） |
| タイプ | Microsoft Entra IDを選択 |
| 登録時にセットされるグループ | 自動登録されるメンバーの所属グループを設定します。 |
| Internal Key to Store External ID | 先ほど作成したメンバー拡張項目（External SCIM ID）を選択 |

さらに、[Member attribute mapping]で以下のマッピングを設定します。

| 外部属性キー | 内部属性キー | 説明 |
| :-- | :--- | :--- |
| `name.givenName` | 名 | 名（Given Name） |
| `name.familyName` | 姓 | 姓（Family Name） |
| `userName` | メールアドレス | メールアドレス |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/400144cc39cac2502e80ae4ce8b25a38.png)

:::tip
[外部属性キー]は、テキストボックスに直接入力するほか、右側のプルダウン[-- スキーマから選択 --]から選択できます。[タイプ]でMicrosoft Entra IDを選択している場合、プルダウンの[共通属性]に`userName`や`name.givenName`などの属性が表示されます。詳細は[SCIM SP](/ja/docs/management/sso-scim-sp/#外部属性キー)を参照してください。
:::

:::caution
Member attribute mappingを設定しないと、名前やメールアドレスなどの基本情報がKurocoに同期されません。少なくとも上記のマッピングは設定してください。
:::

:::caution
同時に有効にできるSCIM SPは1つだけです。
:::

入力が完了したら[追加する]ボタンをクリックします。

**3. SCIM SPエンドポイントURIとシークレットキーを控える**  
追加後、作成したSCIM SP設定をクリックして編集画面を開きます。以下の情報を控えてください。Microsoft Entra IDのエンタープライズアプリケーション設定で使用します。

- **SCIM SP Endpoint URI**：Microsoft Entra IDに設定するテナントURL
- **シークレットキー**：Microsoft Entra IDに設定するシークレットトークン(Generate new Secret Keyをクリックすると入力されます)

値を控えたら[有効にする]を有効にして更新します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/569cd5e9fe9bac1eab9e3610ab818acc.png)

## Microsoft Entra IDの構成

次に、[Microsoft Entra管理センター](https://entra.microsoft.com/)でエンタープライズアプリケーションを作成し、SCIMプロビジョニングを構成します。

:::info
画面はMicrosoftの仕様によって変更される可能性があります。
:::

**1. Microsoft Entra管理センターにアクセスする**  
[Microsoft Entra管理センター](https://entra.microsoft.com/)にサインインします。

<!-- キャプチャ: Microsoft Entra管理センターのダッシュボード -->

**2. エンタープライズアプリケーションを作成する**  
左側のナビゲーションで[Entra ID] -> [エンタープライズアプリ]をクリックします。  
[新しいアプリケーション]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d7c73a7f29a964eadbbc0dda2bf0299.png)

**3. 独自のアプリケーションを作成する**  
[独自のアプリケーションの作成]をクリックします。  
アプリケーション名を入力し（例：Kuroco SCIM）、[ギャラリーに見つからないその他のアプリケーションを統合します（ギャラリー以外）]を選択して[作成]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/65661e37d8b15973062f8b2e5ffcdcc3.png)

**4. プロビジョニングを設定する**  
作成したアプリケーションの概要画面で、左側メニューの[プロビジョニング]をクリックし、[新しい構成]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/29c353ffe389ad0449d21327c3743c4b.png)

**5. 管理者資格情報を入力する**  
[新しいプロビジョニング構成]で以下の値を入力します。

| 項目 | 値 |
| :-- | :--- |
| 認証方法の選択 | ベアラー認証 |
| テナントURL | KurocoのSCIM SP編集画面で控えた[SCIM SP Endpoint URI]の値 |
| シークレット トークン | KurocoのSCIM SP編集画面で控えた[シークレットキー]の値 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bbfa671be12e0cdd3552a4532bcc434.png)

**6. 接続をテストする**  
[テスト接続]をクリックして、Microsoft Entra IDからKurocoへの接続を確認します。  
接続が正常であることを確認したら、[作成]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/222509e33b4bcc46dfbcffc3aea621e4.png)

:::caution
テスト接続に失敗した場合は、以下を確認してください。
- KurocoのSCIM SP設定が有効になっていること
- テナントURLとシークレットトークンが正しく入力されていること
:::

**7. 属性マッピングを設定する**  
[マッピング]セクションを開き、[Provision Microsoft Entra ID Users]をクリックして、Microsoft Entra IDの属性がKurocoにどのようにマッピングされるかを設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4aff6dafc69ffdcbb68b8744df0908ee.png)

Kurocoでは、SCIMの`userName`属性をメールアドレスとして扱います。Microsoft Entra IDのデフォルトでは`userName`に`mailNickname`や`objectId`などがマッピングされている場合があるため、必ず以下のとおり`userPrincipalName`に変更してください。

| customappsso属性（Kuroco側） | Microsoft Entra ID属性 |
| :-- | :--- |
| `userName` | `userPrincipalName` |
| `name.givenName` | `givenName` |
| `name.familyName` | `surname` |

設定手順:
1. 属性マッピングの一覧から、`customappsso Attribute`が`userName`の行をクリックします。
2. [ソース属性]を`userPrincipalName`に変更します。
3. [OK]をクリックして保存します。
4. ページ下部の[保存]をクリックして、マッピング全体を保存します。

:::caution
`userName`に`userPrincipalName`以外（例：`mailNickname`、`objectId`など）がマッピングされていると、Kurocoに送信されるメールアドレスが不正な形式となり、メンバー登録に失敗します。必ず`userPrincipalName`を指定してください。
:::

:::info
Kuroco側のMember attribute mapping設定と、Microsoft Entra ID側の属性マッピング設定は、整合性が取れている必要があります。
:::

**8. ユーザーとグループを割り当てる**  
アプリケーションの概要画面に戻り、[ユーザーとグループ]をクリックします。  
[Add user/group]をクリックし、SCIMプロビジョニングの対象となるユーザーまたはグループを割り当てます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a316ca66b72060402b2e48120223f20f.png)

**9. プロビジョニングを開始する**  
[プロビジョニング]画面に戻り、[プロビジョニング状態]をオンにして保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aa7f3a19ba83005386036b53e2fdc833.png)

:::info
初回のプロビジョニングサイクルは、通常20〜40分程度かかります。その後の同期は約40分間隔で自動的に実行されます。
:::

## 動作確認

SCIMプロビジョニングが正常に動作しているかを確認します。

**1. Microsoft Entra管理センターでプロビジョニングログを確認する**  
Microsoft Entra管理センターで、作成したエンタープライズアプリケーションの[プロビジョニング] -> [プロビジョニングログ]をクリックします。  
プロビジョニングが成功しているか確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/02bee9bc6520f73c394094c1f0aa7a4a.png)

**2. Kurocoでメンバーを確認する**  
Kuroco管理画面で[メンバー管理] -> [メンバー]をクリックし、Microsoft Entra IDから同期されたメンバーが表示されていることを確認します。

<!-- キャプチャ: Kurocoメンバー一覧画面（同期されたメンバーが表示されている状態） -->

:::tip
プロビジョニングが正常に動作しない場合は、以下を確認してください。
- KurocoのSCIM SP設定が有効になっていること
- Microsoft Entra IDのプロビジョニングが開始されていること
- テナントURLとシークレットトークンが正しいこと
- 対象のユーザーまたはグループがエンタープライズアプリケーションに割り当てられていること
:::

## （任意）Microsoft Entra IDのカスタム属性をマッピングする

:::info
この節の手順は任意です。名前やメールアドレスなどの基本情報を同期するだけの場合は、対応は不要です。Microsoft Entra IDのカスタム属性をKurocoのメンバー拡張項目に同期したい場合にのみ実施します。
:::

Microsoft Entra IDの`onPremisesExtensionAttributes`（extensionAttribute1〜15）などをKurocoのメンバー拡張項目に同期する場合、これらはエンタープライズアプリケーションの属性マッピング設定で定義した拡張スキーマURNとしてKurocoに送信されます。このような属性は、KurocoのSCIM SP編集画面のプルダウン[-- スキーマから選択 --]の[共通属性]や[Microsoft EntraID 拡張属性]には表示されません。

プロビジョニングを一度実行すると、Kurocoが受信したリクエストに含まれていた外部属性キーが記録され、プルダウンの[受信済みの属性]に表示されます。以下の手順でマッピングを設定します。

**1. Microsoft Entra ID側でカスタム属性のマッピングを追加する**  
エンタープライズアプリケーションの[プロビジョニング] -> [マッピング] -> [Provision Microsoft Entra ID Users]で、対象の属性のマッピングを追加して保存します。

**2. プロビジョニングを実行する**  
プロビジョニングサイクルが実行され、Kurocoがリクエストを受信するのを待ちます。

**3. Kurocoで[受信済みの属性]から選択する**  
[外部システム連携] -> [ID連携] -> [SCIM SP]で対象のSCIM SP設定を開き、[Member attribute mapping]のプルダウン[-- スキーマから選択 --]を開きます。[受信済みの属性]に表示されている属性キーを選択し、[内部属性キー]に保存先のメンバー拡張項目を指定して[更新する]をクリックします。

**4. 同期を確認する**  
次回以降のプロビジョニングで、設定した属性がKurocoのメンバー拡張項目に保存されていることを確認します。

:::info
[受信済みの属性]に表示される属性キーの仕様（記録のタイミング、記録されない属性、上限件数）については、[SCIM SP](/ja/docs/management/sso-scim-sp/#受信済みの属性について)を参照してください。
:::

## 運用時の役割分担

SCIMプロビジョニングを導入した後は、Microsoft Entra IDとKurocoでそれぞれ管理する領域が異なります。

### Microsoft Entra ID側で管理するもの

以下の情報は、Microsoft Entra ID側で管理します。SCIMプロビジョニングによりKurocoに自動同期されます。

- ユーザーの作成・削除（有効化・無効化）
- マッピングされたメンバー属性情報（名前、メールアドレスなど）
- グループの作成・削除およびグループへのメンバー割り当て
- Entra IDエンタープライズアプリケーションへのユーザー・グループの割り当て

### Kuroco側で管理するもの

以下の設定は、SCIMプロビジョニングの同期対象外であり、Kurocoの管理画面で管理します。

- グループの権限設定（グループ自体の作成とメンバー割り当てはEntra IDから同期されますが、そのグループにどのような権限を付与するかはKuroco側で設定が必要です）
- Kuroco独自のグループの作成・削除およびグループへのメンバー割り当て（Entra IDで管理しないKuroco固有のグループは、Kuroco管理画面で作成し、メンバーを割り当てます）
- KurocoのコンテンツやAPIのアクセス権限
- SCIM SP設定のメンテナンス

:::caution
SCIMプロビジョニングによる同期対象のメンバー属性（名前やメールアドレスなど）をKurocoの管理画面から直接編集した場合、次回のプロビジョニング同期時にEntra ID側の情報で上書きされます。メンバー情報の変更はMicrosoft Entra ID側で行ってください。
:::

:::info
SCIMプロビジョニングではグループの作成とメンバーのグループ割り当ては同期されますが、グループの権限（アクセス権など）の同期は行われません。Entra IDから同期されたグループに対して、Kurocoの管理画面で権限を設定してください。
:::

## メンバー紐付けの優先順位

SCIMプロビジョニングでは、Microsoft Entra IDから送信されたユーザー情報をKurocoの既存メンバーと紐付ける際に、以下の優先順位でマッチングが行われます。

| 優先順位 | 紐付け方法 | 説明 |
| :--: | :-- | :--- |
| 1 | メンバーID | プロビジョニング実行後、Kuroco側のメンバーIDとEntra ID側のユーザーが紐付けられます。以降の同期ではこのメンバーIDによる紐付けが最優先で使用されます。 |
| 2 | Internal Key to Store External ID | メンバーIDでの紐付けができない場合（例：初回プロビジョニング時など）、Internal Key to Store External IDに保存されたExternal IDを使用してマッチングを試みます。 |
| 3 | メールアドレス | 上記2つの方法で紐付けができない場合、メールアドレスでのマッチングを試みます。 |
| 4 | 新規作成 | いずれの方法でも既存メンバーと紐付けられない場合、新規メンバーとして作成されます。 |

:::info
初回のプロビジョニングでは、メンバーIDによる紐付けはまだ存在しないため、Internal Key to Store External IDまたはメールアドレスを使用して紐付けが行われます。一度紐付けが確立されると、それ以降はメンバーIDによる紐付けが優先されます。
:::

## 関連ドキュメント
- [SCIM SP](/ja/docs/management/sso-scim-sp/)
- [Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- [IDaaSを使用してMicrosoft Entra External ID（旧 Azure AD B2C）SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)
- [メンバー詳細設定](/ja/docs/management/new-member-settings/)


---

# SPAでのSSO認証フローを実装する

> 元ページ: `tutorials/implementing-sso-login-flow-in-spa` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-sso-login-flow-in-spa/
> 概要: Kurocoと外部IdP（Microsoft Entra IDなど）を使用して、フロントエンドSPAにおけるSSO（シングルサインオン）認証フローを実装するステップバイステップのチュートリアルです。grant_tokenの交換、トークン管理、ログイン後のリダイレクトについて解説します。

## 概要

このチュートリアルでは、KurocoをバックエンドAPIとして利用するフロントエンドSPA（Single Page Application）において、SSOログインフローの全体を実装する方法を解説します。

[SSOによるログインをフロントエンドで利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)ではKurocoの基本設定とgrant_tokenの概念を説明していますが、本チュートリアルでは**フロントエンド側の実装の詳細**に焦点を当てます。具体的には、リダイレクトフローの処理、トークンの交換、ログイン後にユーザーの元のページへ復帰する方法について説明します。

以下のシーケンス図は、Microsoft Entra IDをIdPとして使用した場合の完全なフローを示しています。Kurocoで設定されたSSOプロバイダー（OAuth SP、SAML SP、IDaaS SP）であれば、同じパターンが適用されます。

![SSO認証フローのシーケンス図](/img/tutorial/sso-flow-ja.png)

[図を拡大して表示](pathname:///img/tutorial/sso-flow-ja.png)

### 学べること

- SSOリダイレクトフローのエンドツーエンドの仕組み
- SSOリダイレクトをまたいでユーザーの元のURLを保存・復元する方法
- `grant_token`を`access_token`に交換する方法
- ログインを確定し、元のページに遷移する方法

### 前提条件

- SSOが設定済みのKurocoプロジェクト（OAuth SP、SAML SP、またはIDaaS SP）
  - SSO設定画面の **「(API用) Grantトークン生成」** で対象APIにチェックを入れてください
- **動的アクセストークン**セキュリティのAPIに、以下の`token`エンドポイントを作成済みであること

  |項目|設定内容|
  | :--- | :--- |
  |パス|token|
  |カテゴリー|認証|
  |モデル|Login(v1)|
  |オペレーション|token|
  |use_refresh_token|チェックあり|
  |access_token_lifespan|86400（1日、秒単位）|
  |refresh_token_lifespan|604800（7日、秒単位）|

- フロントエンドSPA（React、Vue、Nuxt、Next.jsなど）

まだKurocoでSSOを設定していない場合は、以下のチュートリアルを先にご参照ください：
- [SSOによるログインをフロントエンドで利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)
- [OAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)
- [IDaaSを使用してMicrosoft Entra External ID SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)

## フロー概要

SSOログインフローは以下のステップで構成されます：

1. 未認証でユーザーが保護されたページにアクセス
2. フロントエンドが現在のURLを保存し、KurocoのSSOログインエンドポイントにリダイレクト
3. Kurocoがブラウザを外部IdP（例：Entra ID）にリダイレクト
4. ユーザーがIdPで認証
5. IdPが結果をKurocoに返却し、KurocoがフロントエンドのコールバックURLに`grant_token`付きでリダイレクト
6. フロントエンドが`grant_token`を`access_token`と`refresh_token`に交換
7. フロントエンドがprofileエンドポイントを呼び出してログインを確定
8. フロントエンドがユーザーを元のページに遷移

## トークンの種類と役割

SSOフローでは3種類のトークンが登場します。それぞれ用途と寿命が異なります。

| トークン | 用途 | 取得方法 | 寿命 | 使用回数 |
| :--- | :--- | :--- | :--- | :--- |
| `grant_token` | `access_token`を発行するための一時トークン | SSO認証成功後、リターンURLのクエリパラメータとして付与される | 非常に短い（即時交換が必要） | **1回のみ** |
| `access_token` | APIリクエストの認証に使用。`X-RCMS-API-ACCESS-TOKEN`ヘッダーに設定する | `grant_token`または`refresh_token`をtokenエンドポイントに送信して取得 | 設定値（例：86400秒 = 1日） | 有効期限内は何度でも使用可能 |
| `refresh_token` | 期限切れの`access_token`を再発行するためのトークン | `grant_token`をtokenエンドポイントに送信した際に`access_token`と同時に取得 | 設定値（例：604800秒 = 7日） | 有効期限内は何度でも使用可能 |

トークンの流れ：

```
SSO認証成功
  └→ grant_token（URLパラメータ）
       └→ tokenエンドポイントに送信
            ├→ access_token（API認証に使用）
            └→ refresh_token（access_token期限切れ時に再発行）
                  └→ tokenエンドポイントに送信
                       ├→ 新しいaccess_token
                       └→ 新しいrefresh_token
```

:::info
`access_token`と`refresh_token`はいずれもtokenエンドポイント（`/rcms-api/{api_id}/token`）から取得しますが、リクエストボディのパラメータが異なります：
- 初回発行：`{ "grant_token": "..." }`
- 再発行（リフレッシュ）：`{ "refresh_token": "..." }`
:::

## 使用するエンドポイント

本チュートリアルで使用するエンドポイントの一覧です。いずれもKuroco管理画面であらかじめ作成しておく必要があります。

| エンドポイント | メソッド | パス | 用途 | 認証ヘッダー |
| :--- | :--- | :--- | :--- | :--- |
| SSOログイン | GET | 管理画面のSSO設定から取得 | SSO認証フローを開始する | 不要 |
| token | POST | `/rcms-api/{api_id}/token` | `grant_token`→`access_token`の交換、`refresh_token`による再発行 | 不要 |
| profile | GET | `/rcms-api/{api_id}/profile` | ログイン確認とユーザー情報の取得 | `X-RCMS-API-ACCESS-TOKEN` |
| logout | POST | `/rcms-api/{api_id}/logout` | ログアウト処理 | `X-RCMS-API-ACCESS-TOKEN` |

:::tip
tokenエンドポイントとprofileエンドポイントは、Kuroco管理画面のAPI設定で以下のように作成します：

**tokenエンドポイント**（前提条件の設定テーブルを参照）
- カテゴリー：認証 / モデル：Login(v1) / オペレーション：token

**profileエンドポイント**
- カテゴリー：認証 / モデル：Login(v1) / オペレーション：profile

**logoutエンドポイント**
- カテゴリー：認証 / モデル：Login(v1) / オペレーション：logout
:::

## 実装

### ステップ1：未認証状態の検出

ユーザーが保護されたページにアクセスした際、有効なトークンがあるかを確認します。なければ、ログイン後にリダイレクトできるよう現在のURLを保存します。

```js
const currentPath = window.location.pathname + window.location.search

if (!accessToken) {
  sessionStorage.setItem("post_login_redirect", currentPath)
}
```

:::tip
リダイレクトURLの保存には`localStorage`ではなく`sessionStorage`を使用してください。ブラウザタブを閉じたときに自動的にクリアされるため、一時的なログイン状態の管理により適しています。
:::

### ステップ2：SSOログインへのリダイレクト

ユーザーをKurocoのSSOログインURLにリダイレクトします。このURLはKuroco管理画面のSSO設定画面から取得できます。

SSOの種類によって、ログインURLの確認場所が異なります：

| SSO種別 | 管理画面の場所 | URL表示項目 |
| :--- | :--- | :--- |
| OAuth SP | [外部システム連携] → [ID連携] → [OAuth SP] → 編集画面 | ログインURL |
| SAML SP | [外部システム連携] → [ID連携] → [SAML SP] → 編集画面 | ログインSAML SP ACS URI |
| IDaaS SP | [外部システム連携] → [ID連携] → [IDaaS SP] → 編集画面 | ログインURL |

```js
// KurocoのAPIドメイン（独自ドメインを設定している場合はそのドメインを使用）
const KUROCO_API = "https://api.example.com"

// SSOログインURLはKuroco管理画面のSSO設定画面から取得します
// 例: https://{管理画面ドメイン}/direct/login/saml_login/?spid={sp_id}
const SSO_LOGIN_URL = "https://{management-domain}/direct/login/saml_login/?spid={sp_id}"
```

SSOログインURLへリダイレクトします。`api_id`パラメータを付与すると、grant_tokenを生成する対象APIを明示的に指定できます（管理画面で複数APIにチェックを入れている場合に有用です）。

```js
// api_idを指定する場合はクエリパラメータに追加
window.location.href = `${SSO_LOGIN_URL}&api_id={api_id}`

// api_idが不要な場合（対象APIが1つのみの場合）
window.location.href = SSO_LOGIN_URL
```

:::caution
SSOログインURLはKuroco管理画面のSSO設定画面から取得してください。コールバックURL（認証後のリダイレクト先）は管理画面の **「リターンURL（成功）」** で設定します。ユーザーの実際の戻り先は、ステップ1で示したように`sessionStorage`で別途管理します。
:::

### ステップ3：コールバックの処理

SSO認証が成功すると、Kurocoは管理画面で設定した「リターンURL（成功）」に `grant_token` と `member_id` をGETパラメータとして付与してリダイレクトします（例：`https://front-end.example.com/?grant_token=*********&member_id=123`）。コールバックページでこれらを取得します。

```js
const params = new URLSearchParams(window.location.search)
const grantToken = params.get("grant_token")
const memberId = params.get("member_id")

if (!grantToken) {
  // エラー処理：ログインページにリダイレクトするか、エラーを表示
  throw new Error("コールバックURLにgrant_tokenが存在しません")
}
```

### ステップ4：grant_tokenをaccess_tokenに交換

`grant_token`をKurocoのトークンエンドポイントに送信して、`access_token`と`refresh_token`を取得します。

```js
const response = await fetch(
  `${KUROCO_API}/rcms-api/{api_id}/token`,
  {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ grant_token: grantToken }),
  }
)

const data = await response.json()
const { access_token, refresh_token } = data
```

:::info
`grant_token`は1回限り有効な短命のトークンです。URLに露出するため、コールバック受信後直ちにアクセストークンに交換する必要があり、再利用はできません。
:::

トークンエンドポイントのレスポンスは以下のような構造です。実際のトークン文字列は `.value` プロパティに格納されています：

```json
{
  "access_token": { "value": "アクセストークン文字列", ... },
  "refresh_token": { "value": "リフレッシュトークン文字列", ... }
}
```

### ステップ5：トークンの保存

トークンを安全に保存します。SPAではメモリ内での保存が推奨されます。トークン文字列は `.value` から取得します。

```js
// メモリまたはセキュアなストレージに保存
setAccessToken(access_token.value)
setRefreshToken(refresh_token.value)
```

### ステップ6：ログインの確定

新しいアクセストークンでprofileエンドポイントを呼び出し、ログインを確認します。

```js
const profileResponse = await fetch(`${KUROCO_API}/rcms-api/{api_id}/profile`, {
  credentials: "include",
  headers: {
    "X-RCMS-API-ACCESS-TOKEN": access_token.value,
  },
})

const user = await profileResponse.json()
```

### ステップ7：元のページへの遷移

`sessionStorage`から保存済みのURLを取得し、ユーザーを元のページに遷移させます。

```js
const redirectPath =
  sessionStorage.getItem("post_login_redirect") || "/"

sessionStorage.removeItem("post_login_redirect")

// ルーターのナビゲーションを使用（例：React Router、Vue Router）
navigate(redirectPath)
```

## トークンリフレッシュ

`access_token`の有効期限が切れた場合は、`refresh_token`を使用して新しいトークンを取得します。リフレッシュも失敗した場合は、SSOフローを再実行します。

```js
const refreshResponse = await fetch(
  `${KUROCO_API}/rcms-api/{api_id}/token`,
  {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ refresh_token: refreshToken }),
  }
)

if (!refreshResponse.ok) {
  // リフレッシュ失敗 — SSOフローを再開
  sessionStorage.setItem(
    "post_login_redirect",
    window.location.pathname + window.location.search
  )
  window.location.href = SSO_LOGIN_URL
  return
}

const refreshData = await refreshResponse.json()
setAccessToken(refreshData.access_token.value)
setRefreshToken(refreshData.refresh_token.value)
```

:::tip
APIリクエストが`401 Unauthorized`を返した場合に、自動的に`refresh_token`でトークンを再取得してリクエストをリトライする仕組みを実装すると、ユーザー体験が向上します。リトライも失敗した場合はトークンを破棄してSSOフローを再開します。
:::

## 重要な設計ポイント

### SSOログインURLとコールバックURL

SSOログインURL（例：`https://{管理画面ドメイン}/direct/login/saml_login/?spid={sp_id}`）と、認証後のコールバックURL（リターンURL）は、いずれもKuroco管理画面のSSO設定で管理します。SSO設定画面の **「(API用) Grantトークン生成」** で対象APIにチェックを入れることで、リターンURL遷移時に`grant_token`パラメータが付与されるようになります。ユーザーの実際の戻り先は、フロントエンド側で`sessionStorage`を使用して別途管理します。

### 認証スコープごとに1つのAPI

Kurocoでは、動的アクセストークン認証の場合、ログインセッションはAPI（`api_id`）単位でスコープされます。SSOログインを使用した場合、ユーザーはSSOが設定されたAPIに対してのみ認証されます。認証が必要なすべてのエンドポイントを同一の`api_id`にまとめることで、セッションの問題を回避できます。

> **注意**: Cookie認証の場合は、複数の`api_id`間で認証状態が共有されます。詳細は[APIのセキュリティ](/ja/docs/management/api-security/)を参照してください。

### grant_tokenのセキュリティ

`grant_token`はURLに露出するため、コールバックで受け取ったら直ちに`access_token`に交換してください。詳細は上記の[トークンの種類と役割](#トークンの種類と役割)を参照してください。

## 関連ドキュメント

- [SSOによるログインをフロントエンドで利用する](/ja/docs/tutorials/implementing-oauth-sp-based-sso-front/)
- [OAuth認証によるSSOを実装する](/ja/docs/tutorials/implementing-oauth-sp-based-sso/)
- [Microsoftを利用してOAuth認証によるSSOを実装する](/ja/docs/tutorials/implement-login-with-microsoft/)
- [IDaaSを使用してMicrosoft Entra External ID SSOを実装する](/ja/docs/tutorials/using-idaas-to-implement-azure-ad-b2c-sso/)
- [Google Workspaceを利用してSAML認証によるSSOを実装する](/ja/docs/tutorials/using-gsuite-to-implement-saml-based-sso/)


---

# ログイン画面に2段階認証を実装する

> 元ページ: `tutorials/implementing-two-step-verification-on-login-form` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-two-step-verification-on-login-form/
> 概要: Kurocoのログインのエンドポイントには2段階認証を実装するためのパラメータの準備があり、Email, Authenticator, SMSによる2段階認証を容易に実装できます。

## 概要
Kurocoのログインのエンドポイントには2段階認証を実装するためのパラメータの準備があり、Email, Authenticator, SMSによる2段階認証を容易に実装できます。

本チュートリアルでは3つの認証方法による2段階認証のログイン動作を確認し、それを利用したフロントエンドのコードを紹介します。

### 学べること
以下の手順でログイン画面に2段階認証を実装します。

- [2段階認証の動作を確認する](#2段階認証の動作を確認する)
  - [Emailによる2段階認証](#emailによる2段階認証)
  - [Authenticatorによる2要素認証](#authenticatorによる2要素認証)
  - [SMSによる2要素認証](#smsによる2要素認証)
  - [追加認証の強制](#追加認証の強制)
- [フロントエンドの実装をする](#フロントエンドの実装をする)

### 前提条件
このページは、KurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  

:::info
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)   
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

:::tip
本ドキュメントではCookie認証による設定の流れを説明します。  
動的アクセストークンを利用する場合は、[動的アクセストークンの場合の認証方法](#動的アクセストークンの場合の認証方法)も参照してください。
:::

## 2段階認証の動作を確認する
### Emailによる2段階認証
#### エンドポイントの作成
任意のAPIで「新しいエンドポイントの追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0da1dd80f2c46ce371589890a4612c72.png)

以下の設定をします。

|項目|設定内容|
|:--|:--|
|パス|2steplogin/email|
|カテゴリー|認証|
|モデル|Login|
|オペレーション|login_challenge |
|twofactor_method|email|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/799a76348ad775d91cb7d4169f60911d.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

#### SwaggerUIで動作の確認
対象のAPIから[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2611950c27f7c5808551da8664384a9.png)

追加したエンドポイントを開き[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca5ef0830be1223d9a285a40bc52e94b.png)

認証情報を入力して[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c71335322e93cddb21ff6f320c6699c3.png)

正しい認証情報が入力された場合は「追加の認証情報が必要です。」のレスポンスが返ります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e85c7f3b5782b1ac4ac92a1f30afa6b6.png)

ユーザーのメールアドレス宛に認証コードが届きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/edc90af9660f4ebfbe9f973700f6b03c.png)

:::tip
通知の内容は`login/authentication_code`の[メッセージひな形](/ja/docs/management/email-template/)で編集可能です。
:::

Request bodyから`password`を削除し、`onetime_password`を入力して再度[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c314191a75a617ec071a1084cffa12cb.png)

grant_tokenが発行され、ログインできたことを確認できました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dd1022c33fc898a8fb93a9f6f1b53355.png)

### Authenticatorによる2要素認証
Authenticatorによる2要素認証を利用するには、まずKurocoの管理画面でワンタイムパスワードを設定する必要があります。  

#### ワンタイムパスワードの利用設定をする

[環境設定] -> [サイト一覧]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e62d36fc06738d5bd8bde2772e0d807.png)

ログインの項目のワンタイムパスワードを[利用する]に設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/782b5eb20e42fc14840edf327cce67da.png)

#### ワンタイムパスワードを登録する

[メンバー管理]->[メンバー]から自身のメンバー情報に遷移するか、管理画面右上のアイコンから自身のメンバー情報に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6a612079b1f9b09d4fde7f7716c73f6.png)

ID情報タブからワンタイムパスワードの[設定する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d7a5b20595ef61281e73dda3e6ec486.png)

ワンタイムパスワードの設定画面が開くので、[登録する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74c042c775907c2278de2f102c9eafe5.png)

Google Authenticatorのアプリを開き、QRコードを読み込み、6桁の認証コードを入力します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5cff2ee8efceb36ef73380c48370d52.png)

登録しました。の表示が出たら設定は完了です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e20fc4dd62251782ecf9d02f335cb95.png)

#### エンドポイントの作成
ワンタイムパスワード利用の準備ができたら、任意のAPIで「新しいエンドポイントの追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0da1dd80f2c46ce371589890a4612c72.png)

以下の設定をします。

|項目|設定内容|
|:--|:--|
|パス|2steplogin/code|
|カテゴリー|認証|
|モデル|Login|
|オペレーション|login_challenge |
|twofactor_method|code|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2448e8c93c44bbd1872be34755fb64c8.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

#### SwaggerUIで動作の確認
対象のAPIから[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2611950c27f7c5808551da8664384a9.png)

追加したエンドポイントを開き[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7d730d8c789bde559491c22747e7ff2a.png)

認証情報を入力して[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c71335322e93cddb21ff6f320c6699c3.png)

正しい認証情報が入力された場合は「追加の認証情報が必要です。」のレスポンスが返ります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e85c7f3b5782b1ac4ac92a1f30afa6b6.png)

端末からGoogle Authenticatorのアプリを開き認証コードを確認します。  

Request bodyから`password`を削除し、`onetime_password`を入力して再度[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/839b935ef021e42c6e7941fe5c830dbe.png)

grant_tokenが発行され、ログインできたことを確認できました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dd1022c33fc898a8fb93a9f6f1b53355.png)

### SMSによる2要素認証
SMSによる2要素認証を利用するには、Twilioとの連携が必要です。  
また、メンバー情報の電話番号に"090","080","070","060"から始まる日本国内の電話番号が登録されている必要があります。  
始めに、以下のドキュメントを参考に設定をしてください。  

:::info
[Twilioと連携してSMSを送信する](/ja/docs/tutorials/how-to-connect-to-twillio/)
:::

#### エンドポイントの作成
SMS利用の準備ができたら、任意のAPIで「新しいエンドポイントの追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0da1dd80f2c46ce371589890a4612c72.png)

以下の設定をします。

|項目|設定内容|
|:--|:--|
|パス|2steplogin/sms|
|カテゴリー|認証|
|モデル|Login|
|オペレーション|login_challenge |
|twofactor_method|sms|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3de90680b6aa1174ff261888dbf2ec28.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。

#### SwaggerUIで動作の確認
対象のAPIから[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2611950c27f7c5808551da8664384a9.png)

追加したエンドポイントを開き[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a1385323d255fa212e5c0c9c5ff2de9.png)

認証情報を入力して[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c71335322e93cddb21ff6f320c6699c3.png)

正しい認証情報が入力された場合は「追加の認証情報が必要です。」のレスポンスが返ります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e85c7f3b5782b1ac4ac92a1f30afa6b6.png)

SMSで認証コードが届きますので値を確認します。  

:::tip
通知の内容は`login/sms_authentication_code`の[メッセージひな形](/ja/docs/management/email-template/)で編集可能です。
:::

Request bodyから`password`を削除し、`onetime_password`を入力して再度[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c314191a75a617ec071a1084cffa12cb.png)

grant_tokenが発行され、ログインできたことを確認できました。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dd1022c33fc898a8fb93a9f6f1b53355.png)

### 追加認証の強制
追加の認証情報が登録されていない場合は`twofactor_method`のパラメータが設定してあってもログインが成功します。  
ログイン後に電話番号等を登録させることを想定していますが、ログインをさせずにエラーを出したい場合はカスタム処理を作成し、[後処理](/ja/docs/reference/post-processing/)に設定することで対応してください。  

以下は追加の認証情報のステップを通さずにログインが完了した場合に、強制ログアウトし、エラーのレスポンスを出す後処理の例です。  

```smarty
{if isset($smarty.post.password) && $json.grant_token != null}
    {append var=json.errors value='追加の認証情報が登録されていません。'}
    {logout}
{/if}
{assign var=processed_json value=$json}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7b1b6f6a08625b5edabc8e1648f33bde.jpg)

## フロントエンドの実装をする
最後に、SwaggerUIで確認した動作をフロントエンドで実装します。  

`/login/2step_login/`のディレクトリにindex.vue のファイルを作成します。  
以下はEmailを利用した2段階認証の例です。

**Nuxt2:**

```markup reference title="/pages/login/2step_login/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/2step_login_email.vue
```

**Nuxt3:**

```markup reference title="/pages/login/2step_login/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/2step_login_email.vue
```


:::caution
上記サンプルのサンプルは参考のため最低限のコードになっています。  
実際に利用する際には、フォームのバリデーション処理や、`@nuxt/auth` などのライブラリもご利用ください。
:::

:::caution
`/rcms-api/1/2steplogin/email`の部分はご自身のエンドポイントのURLに変更してください。
:::

#### 動作確認
実行し、動作確認ができたら、ログイン画面への2段階認証の実装は完了です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a1cb8861b4163891da71334dd29ceb2.gif)

## 動的アクセストークンの場合の認証方法

動的アクセストークンを利用する場合、2段目の認証に Login::login_challenge_mfa のエンドポイントを使用します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4b1c69da835f68c0d44c8a8e8617754.png)

アクセストークン取得までの流れは以下のようになります。

1. Login::login_challengeのエンドポイントにemail/passwordをPOSTし、mfa_access_tokenを取得する
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/c63e33fdcffbe4fab65d983be75a74b4.png)
2. Login::login_challenge_mfa のエンドポイントに以下のリクエストを送り、grant_tokenを取得する  
    - mfa_access_tokenをX-RCMS-API-ACCESS-TOKENのヘッダーに含める
    - Request bodyにonetime_passwordを含める

  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/5f0be5a9dfddd5b56615086dc93e1027.png)
3. grant_tokenをLogin::token のエンドポイントにPOSTするとアクセストークンが取得できる

## 関連ドキュメント
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
- [KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [後処理](/ja/docs/reference/post-processing/)
- [KurocoとNuxt.jsで、会員登録画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-registration-form/)


---

# 会員登録画面に2段階認証を実装する

> 元ページ: `tutorials/implementing-two-step-verification-on-registration-form` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/implementing-two-step-verification-on-registration-form/
> 概要: 新規会員登録時に、ランダム6桁のワンタイムパスワード(OTP)を発行して認証させる2段階認証を実装します。

## 概要
新規会員登録時に、ランダム6桁のワンタイムパスワード(OTP)を発行して認証させる2段階認証を実装します。

:::tip
本チュートリアルではメールを使用した2段階認証を紹介しますが、twillioと連携することでSMSによる2要素認証も同様の手順で実装できます。
:::

### 学べること
新規会員登録時の2段階認証は、それぞれの以下の手順で実装します。

- [会員登録時の2段階認証](#会員登録時の2段階認証)
  - [エンドポイントの作成](#エンドポイントの作成)
  - [内部利用のエンドポイントの作成](#内部利用のエンドポイントの作成)
  - [カスタム処理の作成](#カスタム処理の作成)
  - [SwaggerUIで動作を確認する](#swaggeruiで動作を確認する)
  - [フロントエンドの実装をする](#フロントエンドの実装をする)


### 前提条件
このページは、KurocoとNuxt.jsでのプロジェクトが構築済みであることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  

:::info
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)  
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/)
:::

:::tip
SMSによる2要素認証を実装する場合は以下のチュートリアルも実施が必要です。  
- [Twilioと連携してSMSを送信する](/ja/docs/tutorials/how-to-connect-to-twillio/)
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## 事前準備
### APIの作成
DefaultのAPIと、内部処理用のInternalのAPIを利用します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2075e3eb4d10bf62b381c1874125c00.png)

#### 内部処理用のAPI作成
Kuroco内部でのみ利用するエンドポイントはAPIを分けておくことをお勧めします。  
そこで、まずは内部利用のためのAPIを新規で作成します。  
既に追加済みの場合は次のステップに進んで構いません。  

#### APIの作成
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c341acced8d685e67ec1da1e85abac.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Internal|
|版|1.0|
|ディスクリプション|内部処理用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c04c600fc74102913e9e668ae5cca0e.png)

#### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bc5cb1beb28c74ede6aeca89715a647.png)

セキュリティを[動的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62aaa225db5d12ee84ccc6d5a52411fe.png)

セキュリティを[動的アクセストークン]に設定後、`Login::token`のエンドポイントが無い場合、利用をお勧めされますが、内部利用のみの場合は無視して構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb1efe099bdae8f1c0481037416a5d9.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74cd7a36fd926dbc20b04812553072c7.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET  
- POST
- OPTIONS

CORS_ALLOW_REDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2bc3744fe6a2ab042456fa8c635195c.png)

問題なければ [保存する] をクリックします。  


## 会員登録時の2段階認証
それでは、会員登録時の2段階認証を実装してみます。  
フロントエンドからの操作は以下の3ステップを想定します。

|ステップ|フロント(ユーザー)の操作|Kurocoの処理|利用するAPI|
|:--|:--|:--|:--|
|1|メンバー登録のための基本情報を送付する|仮メンバーを作成する|Member::invite|
|2|招待メールのURLにアクセスし、ワンタイムパスワード送付のボタンをクリックする|emai_hashを利用して、仮メンバー情報にアクセス、ワンタイムパスワードを追加し、メールを送信する|Api::request_api<br/>Member::invite<br/>MemberProvisional::update|
|3|ワンタイムパスワードを入力して送付|emai_hashを利用して、仮メンバー情報にアクセス、ワンタイムパスワードが一致した場合に会員登録をする|Api::request_api<br/>Member::invite<br/>Member::insert|


### エンドポイントの作成
DefaultのAPIから[新しいエンドポイントの追加]をクリックしてエンドポイントを追加します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21831b02823d8ec43ef328ba8c998ad7.png)

今回は下記エンドポイントを作成します。  

- 仮メンバー登録のエンドポイント
- ワンタイムパスワードを作成・送付するカスタム処理を呼ぶエンドポイント
- ワンタイムパスワードの確認と本登録をするエンドポイント

#### 仮メンバー登録のエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|2step_member_invite|
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|invite|

#### ワンタイムパスワードを作成・送付するカスタム処理を呼ぶエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|set_and_send_otp|
|カテゴリー|API|
|モデル|Api|
|オペレーション|request_api_post|
|name|set_and_send_otp|

#### ワンタイムパスワードの確認と本登録をするエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|check_otp_and_regist|
|カテゴリー|API|
|モデル|Api|
|オペレーション|request_api_post|
|name|check_otp_and_regist|

### 内部利用のエンドポイントの作成
InternalのAPIから[新しいエンドポイントの追加]をクリックしてエンドポイントを追加します。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a2d1f79189bb2a14bb0ef9583acac2c.png)

今回は下記エンドポイントを作成します。  

- 仮メンバー更新のエンドポイント
- メンバー登録のエンドポイント

#### メンバー登録のエンドポイント
メンバー登録のエンドポイントを下記設定にて作成します。

|項目|設定内容|
| :--- | :--- |
|パス|pre_member_update |
|カテゴリー|メンバー|
|モデル|MemberProvisional|
|オペレーション|update |

#### メンバー登録のエンドポイント
メンバー登録のエンドポイントを下記設定にて作成します。

|項目|設定内容|
| :--- | :--- |
|パス|2step_member_regist |
|カテゴリー|メンバー|
|モデル|Member|
|オペレーション|insert|
|default_group_id|適用するメンバーグループのIDを入力してください。<br/>グループIDは[グループ](/ja/docs/management/group/)より確認できます。|
|login_ok_flg|チェックを入れる|

### カスタム処理の作成
#### ワンタイムパスワードを発行・送信するカスタム処理
ワンタイムパスワードとその有効期限を作成し、仮メンバー情報を更新、ワンタイムパスワードをユーザー宛に送付するカスタム処理を作成します。  

[オペレーション] -> [カスタム処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cf05595e31dd0f905466ec2a09bb835.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|set_and_send_otp|
|識別子|set_and_send_otp|
|処理|以下のコード|

```smarty reference title="set_and_send_otp"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/request_api_post/set_and_send_otp.txt
```

:::tip
ワンタイムパスワードをSMSで送付する場合は`sendmail`の`to=$pre_member_info.data.email`の部分を
<code>to="`$pre_member_info.data.ext_info.tel`@twilio.r-cms.jp"</code>
のように変更します。
:::

#### ワンタイムパスワードの一致判定をするカスタム処理
ワンタイムパスワードが一致した場合にMember::insertで会員登録をするカスタム処理を作成します。

[オペレーション] -> [カスタム処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/629aadd18b2e71dc1d5dca3784fe6252.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cf05595e31dd0f905466ec2a09bb835.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|check_otp_and_regist|
|識別子|check_otp_and_regist|
|処理|以下のコード|

```smarty reference title="check_otp_and_regist"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/request_api_post/check_otp_and_regist.txt
```

### SwaggerUIで動作を確認する
KurocoのAPIとカスタム処理の準備ができたらSwaggerUIを利用して動作の確認をします。

#### 会員登録のリクエストを送る
Default エンドポイントのSwaggurUIから`/rcms-api/1/2step_member_invite `をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88c2bf8b3086d5a25e0f8abf49c4f709.png)

[try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9c4ea6845ea131908b4101046c6a755.png)

Request bodyに以下を入力して[Execute]をクリックします。

```json
{
  "email": "example@dexample.com",
  "ext_info": {
    "name": "MyName",
    "login_pwd": "********",
    "tel": "00011112222"
  }
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/35f5d17cd9cdc4599af995358508f699.png)

200のレスポンスを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c23636c724661b11de897301c844cd1c.png)

招待メールが届くのでkeyの部分をコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1efd798cf4b084d9ec86d50ccc6b7a88.png)

:::tip
招待メールの内容は[メッセージひな形](/ja/docs/management/email-template/#メッセージひな形編集)の`member/pre_regist_thanks`のテンプレートで編集が可能です。
リンク部分を`{$smarty.const.ROOT_URL}/login/2step_regist?key={$preregist_key}`のように修正して、
メールから直接遷移できるように調整してください。
:::

#### ワンタイムパスワードの送付リクエストを送る

`/rcms-api/1/set_and_send_otp `をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f9f1f8feb44c5bd6f670c25bbbdd90d.png)

[try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e450330f9b8640e815b81abf1f26f77d.png)

Request bodyに以下を入力して[Execute]をクリックします。

```json
{
  "email_hash": "KEY"
}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6d724bf1a076a471d64d1aa86bb457d.png)

:::caution
`"KEY"`の部分は先ほどコピーした招待メールのkeyにしてください。
:::

200のレスポンスを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4ed0846c4410a3584e3bb7b5ae4b8f4.png)

ワンタイムパスワードがメールで届くので確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/34977a8e6019d19f1a42d68bc28fd073.png)

#### ワンタイムパスワードを送る

`/rcms-api/1/check_otp_and_regist `をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aeb64b1626789bb76a2765dacf1531c6.png)

[try it out]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/07027b8c6952ea046d198cb5c896d981.png)

Request bodyに以下を入力して[Execute]をクリックします。

```json
{
  "email_hash": "KEY",
  "otp":"OTP"
}
```

:::caution
`"OTP"`と`"KEY"`の部分は先ほどコピーした招待メールのkeyにしてください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb8f2bf6e1f183d7233decdcac068f8f.png)

200のレスポンスを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94cc0712de46fa0447309cacd8edbd14.png)

メンバー情報一覧に遷移すると、ユーザー登録されていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4c8c3112ab88b7dad2b384602a38e6ce.png)

以上でKuroco側の設定は完了です。  
SwaggerUIで確認した動作をフロントエンドで実装ください。

### フロントエンドの実装をする
#### 仮登録用のページ作成
`/login/2step_pre_regist/`のディレクトリで表示できるよう以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/login/2step_pre_regist/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/2step_pre_regist.vue
```

**Nuxt3:**

```markup reference title="/pages/login/2step_pre_regist/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/2step_pre_regist.vue
```


:::caution
上記サンプルのサンプルは参考のため最低限のコードになっています。  
実際に利用する際には、フォームのバリデーション処理も追加ください。
:::

#### 本登録用のページ作成
`/login/2step_regist/` のディレクトリで表示できるよう以下のファイルを作成します。

**Nuxt2:**

```markup reference title="/pages/login/2step_regist/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/2step_regist.vue
```

**Nuxt3:**

```markup reference title="/pages/login/2step_regist/index.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxt3/2step_regist.vue
```


:::info
email_hashはクエリで受け取るようにしました。  
:::

#### 動作確認
自身の環境に合わせて調整し、動作確認ができたら、新規会員登録時の2段階認証の実装は完了です。  

##### 仮登録
![Image from Gyazo](https://t.gyazo.com/teams/diverta/78e46e933ea3717e8669146b1b50ad84.gif)

##### 追加のワンタイムパスワード登録
![Image from Gyazo](https://t.gyazo.com/teams/diverta/de3034fa8e973e7cbac0479bfccf8595.gif)

## 関連ドキュメント
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
- [KurocoとNuxt.jsで、新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)  
- [会員登録画面に仮登録機能を実装する](/ja/docs/tutorials/setting-up-pre-member-registration-form/) 
- [メッセージひな形](/ja/docs/management/email-template/)
- [Smaratyプラグイン](/ja/docs/reference/smarty-plugin/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [ログイン画面に2段階認証を実装する](/ja/docs/tutorials/implementing-two-step-verification-on-login-form/)


---

# ログイン画面を構築する

> 元ページ: `tutorials/integrate-login` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrate-login/
> 概要: Kurocoを利用したNuxt.jsプロジェクトで、ログイン画面の作成方法を紹介します。今回は例として、下記流れにてログインユーザーのみコンテンツ一覧ページが閲覧できる処理を実装します。

Kurocoを利用したNuxt.jsプロジェクトで、ログイン画面の作成方法を紹介します。  
今回は例として、下記流れにてログインユーザーのみコンテンツ一覧ページが閲覧できる処理を実装します。

- API・エンドポイントの作成
- ログインフォーム実装
- ログイン処理実装(APIセキュリティ毎)

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt3: v3.8.0
:::

## 前提条件
### Nuxt.jsプロジェクトの作成について
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、コンテンツ一覧のページが作成されていることを前提としています。 まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)

### APIセキュリティについて
Kurocoでは、APIのセキュリティ方法がいくつか用意されています。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5d2188e3c2ea2c2b34b726e9fab91406.png)
セキュリティ「無し」を選択されている場合には、ログインの必要無くAPIからデータを取得できますが、
何らかのセキュリティを設定している場合、利用者にはフロントエンドのログインフォームから認証/認可をしていただく必要があります。

今回は、代表的なログイン方式として、以下の２つのパターンを例にしてフロントエンドのログインフォームを構築します。
- Cookie
- 動的アクセストークン

:::info
セキュリティの種類については、[管理画面マニュアル -> API Security](/ja/docs/management/api-security/)を参照してください。
:::

:::info
セキュリティの種類の詳細な確認方法は、[Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)をご確認ください。
:::

### 推奨ブラウザについて
本チュートリアルは、動作確認のためGoogle Chromeの開発者ツールを利用しています。
そのため、ブラウザはGoogle Chromeを推奨いたします。

## APIの設定
ログイン用のAPIを設定します。

### APIの作成
まずはAPIを新規で作成します。  
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/417993d1fc8a3357e8a3a24cece6c836.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8689b06228161c57065ce8e3255a41e6.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|login|
|版|1.0|
|ディスクリプション|login用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/169c75140c1f30b80fd053292cd27140.png)

### エンドポイントの作成
次にエンドポイントを作成します。今回は下記エンドポイントを作成します。

- loginエンドポイント
- profileエンドポイント
- logoutエンドポイント
- tokenエンドポイント（APIセキュリティが動的アクセストークンの場合のみ）

「新しいエンドポイントの追加」をクリックし、それぞれ作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1e20df3e56291487f859a3cbd905b261.png)

#### loginエンドポイントの作成
loginエンドポイントを下記設定にて作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7fd232391acf1d8ec8c611cf715097c.png)

|項目|設定内容|
| :--- | :--- |
|パス|login|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|login_challenge|

設定完了後、「追加する」をクリックしloginエンドポイント完成です。

#### profileエンドポイントの作成
profileエンドポイントを下記設定にて作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15300b156fe0986773788745876a37cb.jpg)

|項目|設定内容|
| :--- | :--- |
|パス|profile|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|profile|
|APIリクエスト制限|GroupAuth：所属しているグループ<br/>ログインを許可するグループを選択してください。|
|基本設定：basic_info|<ul><li>email</li><li>name1</li><li>name2</li></ul>|

設定完了後、「追加する」をクリックしエンドポイント完成です。

profileエンドポイントは、アクセスしているユーザーの情報を(簡易的に)返却するものです。  
GroupAuthでの認証を設定しているため、ログイン済みで無い場合は情報を返さずにエラーとなります。

今回の場合は、email,name1,name2を値を返すように設定しており、簡易的なユーザー情報を取得するほかに、ログイン状態のリストアをする際、操作しているユーザーが本当にログイン済みであるのかを検証するためにリクエストします。

#### logoutエンドポイントの作成
logoutエンドポイントを下記設定にて作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8253679d4e181188b92329265a3a14e7.png)

|項目|設定内容|
| :--- | :--- |
|パス|logout|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|logout|
|APIリクエスト制限|None|

設定完了後、「追加する」をクリックしエンドポイント完成です。

#### tokenエンドポイントの作成
tokenエンドポイントを下記設定にて作成します。

:::tip
tokenエンドポイントは、APIセキュリティが動的アクセストークンの場合のみ必要になります。
APIセキュリティがCookieの場合、作成する必要はありません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14c7ee1c0f3363ac78618c9227b1c273.png)

|項目|設定内容|
| :--- | :--- |
|パス|token|
|カテゴリー|認証|
|モデル|login v1|
|オペレーション|token|
|APIリクエスト制限|None|

設定完了後、「追加する」をクリックしエンドポイント完成です。

### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e4f4ff71679c45b81ecb2d54b79999d.png)

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
以上で、APIの設定が完了です。

## ログインフォーム実装
次に、フロントエンドにログインフォームを作成します。

### ダミーのログインフォーム実装

まずはAPIとの連携は省いた状態でログイン画面用コンポーネントの作成し、ダミーでのログイン連携処理を実装していきます。  
また、お知らせ一覧画面ではログイン済みかどうかのフラグを参照し、ログイン済みでなければログイン画面に画面遷移するように変更します。

まず、ログイン画面用コンポーネントを作成します。
`pages/login/index.vue` ファイルを新規作成し、以下を記載してください。

```markup [pages/login/index.vue]
<template>
  <form @submit.prevent="login">
    <input v-model="email" name="email" type="email" placeholder="email" />
    <input
      v-model="password"
      name="password"
      type="password"
      placeholder="password" />
    <button type="submit">Login</button>
  </form>
</template>

<script setup>
  const config = useRuntimeConfig();

  const email = ref('');
  const password = ref('');

  function login() {
    console.log(email.value, password.value);
  }
</script>
```

この状態で`npm run dev`を実行し、`http://localhost:3000/login`にアクセスすると簡単なログインフォームが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6fd3b6262b1bc084bd306a34a0cd2ae9.png)

ここまでで、一度ログの確認をします。  
Chromeの開発者ツール:コンソールを開いた状態でフォームに下記を入力し、[ログイン]をクリックします。

- email:`test@example.com`
- password:password

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0445a7f55742fd2b89ace826f2f36d58.png)

すると、入力したemailとpasswordがログとしてコンソールに表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0fb5d190d7550e759fbc58b8760a4553.png)

このログに出力された値をログイン用APIに実際にリクエストすることになります。ひとまずAPI連携部分は仮で実装をし、ログイン後の動きを確認します。

1秒間のリクエストをする見せかけのダミー処理を追加作成し、ログインリクエストに成功した場合、画面上で"ログイン成功"と表示されるように、下記のように修正します。

```diff
<template>
  <form @submit.prevent="login">
+    <p v-if="loginStatus !== null" :style="{ color: resultMessageColor }">
+      {{ resultMessage }}
+    </p>
+
    <input v-model="email" name="email" type="email" placeholder="email" />
    <input
      v-model="password"
      name="password"
      type="password"
      placeholder="password"
    />
    <button type="submit">Login</button>
  </form>
</template>

<script setup>
const config = useRuntimeConfig();

const email = ref("");
const password = ref("");
+const loginStatus = ref(null);
+const resultMessage = ref(null);

+let resultMessageColor = computed(() => {
+  switch (loginStatus.value) {
+    case "success":
+      return "green";
+    case "failure":
+      return "red";
+    default:
+      return "";
+  }
+});
+
-function login() {
-    console.log(email.value, password.value)
+async function login() {
+  // Dummy request(Succeed/fail after 1 sec.)
+  const shouldSuccess = true
+  const request = new Promise((resolve, reject) =>
+      setTimeout(
+          () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
+          1000
+      )
+  )
+  try {
+      await request
+      loginStatus.value = 'success'
+      resultMessage.value = 'Login successful'
+  } catch (e) {
+      loginStatus.value = 'failure'
+      resultMessage.value = 'Login failed'
+  }
}
</script>
```

1秒の待機の後、[ログインに成功しました]が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef9fba1bd155c07942d3b6358cca26ee.png)

失敗した際にどうなるかを確認します。

ソースコードから、`shouldSuccess = true`を `shouldSuccess = false`へ変更し、レスポンスがエラーとなる場合を再現確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/65b275244baa02a566029ba77919a757.png)

確認後は、`shouldSuccess = true`へ戻してください。

### ログイン状態の保持
次にログイン状態を保持できるように実装します。

#### 準備
ログイン関連の処理を保持するストアを作成するには、Piniaパッケージをインストールする必要があります。  
次のコマンドを使用して Pinia をインストールします:

```
npx nuxi@latest module add pinia
```

このコマンドは、`@pinia/nuxt` と `pinia` の両方をプロジェクトに追加します。  
もし `pinia` がインストールされていない場合は、次のように手動でインストールしてください:


:::tip
npm を使用している場合、依存関係ツリーの解決ができない `ERESOLVE` エラーが発生することがあります。  
その場合は、`package.json` に以下を追加してください:
```
"overrides": {
  "vue": "latest"
}
```

:::

次に、`nuxt.config.js` ファイルの `modules` に追加します。

```js
// nuxt.config.js
export default defineNuxtConfig({
  // ... other options
  modules: [
    // ...
    '@pinia/nuxt',
  ],
})
```

さらに、`plugins/pinia.js` ファイルを作成してください。

```js
import { createPinia } from 'pinia';
export default defineNuxtPlugin((nuxtApp) => {
  const pinia = createPinia();
  nuxtApp.vueApp.use(pinia);
});
```

#### a. storeの作成
まずはログイン状態をWebアプリ全体で保持しておき、他の画面でも参照できるよう**store**を作成します。

`stores/authentication.js`ファイルを新規作成し、下記のコードを記載してください。

```javascript
import {defineStore} from 'pinia';

export const useStore = defineStore('authentication', {
  state: () => ({
    profile: null,
  }),
  actions: {
    setProfile(profile) {
      this.profile = profile;
    },
  },
  getters: {
    authenticated: (state) => state.profile !== null,
  },
});
```

`getters`の`authenticated`は、後ほど作成していくprofileデータが空かどうかでtrue/falseが返却されるものです。  
profileデータが空で無ければログイン状態と判定する想定をしています。

後にログインした時やログイン状態のリストア時にprofileデータを自動取得し、それ以外のログアウトなどで値が設定されないようにしていきます。

#### b. middlewareの作成
次にmiddlewareを作成します。

`middleware/auth.js`を新規作成し、下記のコードを記載してください。

```javascript
import { useStore } from '~/stores/authentication';

export default defineNuxtRouteMiddleware((to) => {
  const store = useStore();
  
  // Define public paths that don't require authentication (add any login pages that don't require authentication)
  const publicPaths = ['/login'];
  
  // Allow access if the current path is public
  if (publicPaths.some(path => to.path.startsWith(path))) {
    return;
  }
  
  if (!store.authenticated) {
    return navigateTo('/login');
  }
});
```

middlewareは各画面のソース`page/*.vue`が処理をする以前に動作します。
storeの`authenticated`がfalseである場合にはログインページへ強制的にリダイレクトさせます。

#### c. middlewareの動作確認

middlewareの動作を確認します。
`pages/login/index.vue`にニュース一覧ページへのリンクを追加します。

```diff
         <button type="submit">
             Login
         </button>
+
+        <div>
+            <nuxt-link to="/news">
+                news list
+            </nuxt-link>
+        </div>
     </form>
 </template>

```

ニュース一覧画面の`pages/news/index.vue`のソースコードを変更して、middlewareを適用します。

```diff
<script setup>
+  definePageMeta({
+    middleware: ["auth"],
+  });
...
```

この処理により、ニュース一覧画面にアクセスするためにはログインが必要になります。
ログインしていない場合は、ニュース一覧ページへアクセスすると強制的にログイン画面へとリダイレクトされるようになります。

次に、ログイン成功時、`store`の`prfofile`をnull以外の状態へ変更するようにします。
`pages/login/index.vue`を下記のように変更します。

```diff
<script setup>
+import { useStore } from "~/stores/authentication";
+const store = useStore();

...
             try {
                 await request
+                store.setProfile({}); // Apply the dummy object to store.state.profile
+
                 loginStatus.value = 'success'
                 resultMessage.value = 'Login successful'
             } catch (e) {

```

ログインページにアクセスし、ログイン操作をしてニュース一覧ページに画面遷移することを確認します。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/56dec7340110021efd1a8a6580d8e340.gif)
:::tip
確認には[Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd/reviews?hl=ja&authuser=2)を使用しています。
:::

### ログイン状態のリストアの実装

これまでの実装によって通常のログイン処理は実装されました。
しかしながら、直接URLアクセスやブラウザで画面更新されたとき、これまでの実装では一度ログインしたはずであるのにも関わらずログイン画面にリダイレクトされる不具合が発生します。

上記の操作では、`store`の`profile`はNuxtが初期化されるためnullとなり、
直前に一度ログインしていた場合であってもログイン状態と判定されないためです。

この対応には、一度ログインしたことがある場合にはブラウザのLocalStorageにフラグを設定しておき、
フラグがtrueである場合に`store`の`profile`にダミーのデータを適用するようにします。

`/stores/authentication.js`を下記のように修正してください。

```diff
    setProfile(profile) {
        this.profile = profile
    },
+    async restoreLoginState() {
+      const authenticated = localStorage.getItem("authenticated");
+      const isAuthenticated = authenticated ? JSON.parse(authenticated) : false;
+
+      if (!isAuthenticated) {
+        throw new Error("need to login");
+      }
+      try {
+        this.setProfile({}); // Store the dummy object.
+      } catch {
+        throw new Error("need to login");
+      }
+    },
   },
   getters: {
     authenticated: (state) => state.profile !== null,
```

また、`/middleware/auth.js`を下記のように修正してください。

```diff
 import { useStore } from '~/stores/authentication';

-export default defineNuxtRouteMiddleware((to) => {
+export default defineNuxtRouteMiddleware(async (to, from) => {
   const store = useStore();

   // Define public paths that don't require authentication (add any login pages that don't require authentication)
   const publicPaths = ['/login'];

   // Allow access if the current path is public
   if (publicPaths.some(path => to.path.startsWith(path))) {
     return;
   }

   if (!store.authenticated) {
-    return navigateTo('/login');
+    try {
+      await store.restoreLoginState();
+    } catch (err) {
+      return navigateTo('/login');
+    }
   }
 });
```

ニュース一覧ページにアクセスし、下記4点を確認します。
- LocalStorageの`authenticated`がtrue以外である場合、ログインページにリダイレクトされること
- LocalStorageの`authenticated`がtrueである場合、ログインページにリダイレクトされないこと
- LocalStorageの`authenticated`がtrueかつブラウザの画面更新をした場合でも、ログインページにリダイレクトされないこと
- LocalStorageの`authenticated`をfalseにしてブラウザの画面更新をすると、ログインページにリダイレクトされること

今回はLocalStorageの状態を、chromeの開発者ツールの[Application]タブにて確認します。  
chromeの開発者ツールより[Application]タブをクリックし、[Storage] -> [Local Storage] -> [http://localhost:3000]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/aa339de13a1d00de92fc5c44048f863d.png)
ログインページよりログイン後、Keyに`authenticated`、Valueに`true`または`false`を入力し、上記4点の動作を確認します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/314b063e93383a7eb636abdef9d722ae.gif)
### ログイン動作修正
次にログイン動作を修正します。  
ログイン成功時にLocalStorageの`authenticated`をtrueにさせます。また、今後の修正に備えてログイン処理を一部`store`に移動します。

`/pages/login/index.vue`を下記のように修正します。

```diff
 async function login () {
-    // Dummy request(Succeed/fail after 1 sec.)
-    const shouldSuccess = true
-    const request = new Promise((resolve, reject) =>
-        setTimeout(
-            () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
-            1000
-        )
-    )
-
     try {
-        await request
-        store.setProfile({}) // Apply the dummy object to store.state.profile
+        const payload = {
+            email: email.value,
+            password: password.value
+        }
+        await store.login(payload)

         loginStatus.value = 'success'
         resultMessage.value = 'Login Successful'

```

次に`/stores/authentication.js`を下記のように修正します。

```diff
...
  actions: {
     setProfile (profile) {
         this.profile = profile
     },
+    updateLocalStorage(payload) {
+      Object.entries(payload).forEach(([key, val]) => {
+        if (val === null || val === false) {
+          localStorage.removeItem(key);
+        } else {
+          localStorage.setItem(key, JSON.stringify(val));
+        }
+      });
+    },
+    async login (payload) {
+        // dummy request(succeed/fail after 1 sec.)
+        const shouldSuccess = true
+        const request = new Promise((resolve, reject) =>
+            setTimeout(
+                () => (shouldSuccess ? resolve() : reject(Error('login failure'))),
+                1000
+            )
+        )
+        await request
+
+        this.setProfile({}) // Apply the dummy object to store.state.profile
+        this.updateLocalStorage({ authenticated: true })
+    },
     async restoreLoginState () {
         const authenticated = JSON.parse(localStorage.getItem('authenticated'))

```

ログイン成功時に`authenticated`がtrueになることを確認します。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3c9b258dc445720d0b8598e6d40cd149.gif)
以上でフロントエンドの実装を終了します。

次にAPIを実装します。
なお、実装はAPIセキュリティ毎に実装方法が変わります。
今回はAPIセキュリティがCookieの場合と、動的アクセストークンの場合の実装方法を記載します。
ご自身のAPIセキュリティに併せて、それぞれの対応方法をご確認ください。

- A. [ログイン処理実装(APIセキュリティがCookieの場合)](#a-ログイン処理実装apiセキュリティがcookieの場合)
- B. [ログイン処理実装(APIセキュリティが動的アクセストークンの場合)](#b-ログイン処理実装apiセキュリティが動的アクセストークンの場合)


## A. ログイン処理実装(APIセキュリティがCookieの場合)
次に、先ほどダミーで作成していたログイン処理をloginエンドポイントへとアクセスするように変更します。
まずはAPIセキュリティがCookieの場合の実装方法を説明します。
Kuroco管理画面より、[API] -> [login] をクリックし、「セキュリティ」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84a08a9b4d235d33269d95aab19064ad.png)
「セキュリティ」よりCookieを選択し、「保存する」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8f655bfb466cef7bc2683e3b2e0c0aa9.png)

### loginエンドポイントへのリクエスト実装
`stores/authentication.js`を下記に修正します。

```diff
...
     async login(payload) {
-      // dummy request(succeed/fail after 1 sec.)
-      const shouldSuccess = true;
-      const request = new Promise((resolve, reject) =>
-        setTimeout(
-          () => (shouldSuccess ? resolve() : reject(Error("login failure"))),
-          1000
-        )
-      );
-      await request;
+      await $fetch("/rcms-api/1/login", {
+        method: "POST",
+        body: JSON.stringify(payload),
+        baseURL: useRuntimeConfig().public.apiBase,
+        credentials: "include",
+      });

       this.setProfile({}); // Apply the dummy object to store.state.profile
       this.updateLocalStorage({ authenticated: true})
```

次に、loginエンドポイントへリクエストされているか確認します。

ログインページを開き、Chromeの開発者ツール:ネットワークを開いた状態でログイン処理を行います。
すると、loginエンドポイントへとリクエストされていることが確認できます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e5ba4778eecabe224ae2fa018819eb04.png)

### profileエンドポイントへのリクエスト/ハンドリング実装

今までの実装では、ブラウザのLocalStorageの`authenticated`フラグによってログイン済かどうかを判断する実装をしています。  
しかしながら、LocalStorageはブラウザ上で簡単に改ざんが可能です。

またセッション有効期限によって`authenticated`がtrueであっても、実際には他のエンドポイントへのリクエストがアクセスエラーとなる場合もあります。  
これらによる誤動作を防ぐため、profileのAPIにリクエストし、ユーザー情報が返ってくるか否かを確認することで二重のチェックを行います。  

:::tip
二重のチェックは、profileエンドポイントである必要はありませんが、ログイン中のユーザー名を表示する等、profileが返すデータを最初に必要とするユースケースが多いため、profileエンドポイントの利用が、スタンダードになっています。
:::

`/stores/authentication.js`を下記のように修正します。

```diff
...
 actions: {
   async login(payload) {
      await $fetch("/rcms-api/1/login", {
        method: "POST",
        body: JSON.stringify(payload),
        baseURL: useRuntimeConfig().public.apiBase,
        credentials: "include",
      });
-    this.setProfile({}) // store a dummy object.
+    const profileRes = await $fetch("/rcms-api/1/profile", {
+        baseURL: useRuntimeConfig().public.apiBase,
+        credentials: "include",
+      });
+    this.setProfile(profileRes)
     this.updateLocalStorage({ authenticated: true })
   },
   async restoreLoginState() {
     const authenticated = JSON.parse(localStorage.getItem("authenticated"));

     if (!authenticated) {
       throw new Error('need to login')
     }
     try {
-      this.setProfile({}); // Store the dummy object.
+      const profileRes = await $fetch("/rcms-api/1/profile", {
+        baseURL: useRuntimeConfig().public.apiBase,
+        credentials: "include",
+      });
+      this.setProfile(profileRes);
     } catch {
       throw new Error("need to login");
     }
   },
  },
  getters: {
    authenticated: (state) => state.profile !== null,
  },
});
```

修正ができたらリストアの動作を確認します。

ログインページを開き、Chromeの開発者ツール:アプリケーションを開いた状態でログイン処理を行います。
すると、`authenticated`が`true`となります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/022f5f48843929fdd94f23b3fe4c220b.png)
この状態で、「ニュース一覧ページへ」をクリックし画面遷移します。  
今までの実装と同じように、`authenticated`が`true`のまま、ニュース一覧ページの表示を確認できます。  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/78a69c39bb4de3780b8f38cbb3a73f2a.gif)

### logoutエンドポイントへのリクエスト/ハンドリング実装
次に、ログアウト処理を実装します。

Kuroco側でセッションが残っていながらフロント側で再ログインした場合など、予期せぬ動作が発生する可能性もあります。  
そのため、ログイン状態ではないと判定する場合はAPIへログアウト状態にするようリクエストする必要があります。

`/stores/authentication.js`を下記のように修正します。

```diff
...
-    async restoreLoginState () {
+    async logout() {
+      try {
+        await $fetch("/rcms-api/1/logout", {
+          method: "POST",
+          baseURL: useRuntimeConfig().public.apiBase,
+          credentials: "include",
+        });
+      } catch {
+        /** No Process */
+        /** When it returns errors, it consider that logout is complete and ignore this process. */
+      }
+      this.setProfile(null);
+      this.updateLocalStorage({ authenticated: false });
+
+      navigateTo("/login");
+    },
+    async restoreLoginState () {
         const authenticated = JSON.parse(localStorage.getItem('authenticated'))

         if (!authenticated) {
           throw new Error('need to login')
         }
         try {
         const profileRes = await $fetch("/rcms-api/1/profile", {
           baseURL: useRuntimeConfig().public.apiBase,
           credentials: "include",
         });
         this.setProfile(profileRes);
       } catch {
+        await this.logout();
         throw new Error("need to login");
       }
     },
   },
   getters: {
    authenticated: (state) => state.profile !== null,
  },
});
```

また、ニュース一覧画面を以下のように修正し、ログアウトボタンを作成します。

```diff
<template>
   <div>
+    <button type="button" @click="logout">Logout</button>
     <p>News list</p>
     <div v-for="n in response.list" :key="n.slug">
       <nuxt-link :to="`/news/${n.topics_id}`">
@@ -10,6 +11,7 @@
</template>

<script setup>
+import { useStore } from "~/stores/authentication";
 definePageMeta({
   middleware: ["auth"], // Use the 'auth' middleware defined in middleware/auth.ts
 });
 const config = useRuntimeConfig(); //please add this line if not added already
@@ -18,4 +20,6 @@ const { data: response } = await useFetch("/rcms-api/1/news", {
   baseURL: config.public.apiBase,
   credentials: "include",
 });
+const store = useStore();
+const logout = () => store.logout();
</script>
```

ログイン状態のニュース一覧画面にてログアウトボタンをクリックすると、下記となることを確認します。
- logoutエンドポイントへリクエストしている
- ログイン画面に遷移する
- そのままログインせずにニュース一覧画面へアクセスすると、ログイン画面に自動遷移される

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/8627f900c0652b11a1c84c3f33199842.gif)
以上でAPIセキュリティがcookieの場合のログイン処理の実装が完了です。

## B. ログイン処理実装(APIセキュリティが動的アクセストークンの場合)
次に、先ほどダミーで作成していたログイン処理をloginエンドポイントへとアクセスするように変更します。
ここではAPIセキュリティが動的アクセストークンの場合の実装方法を説明します。
Kuroco管理画面より、[API] -> [login] をクリックし、「セキュリティ」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84a08a9b4d235d33269d95aab19064ad.png)
「セキュリティ」より動的アクセストークンを選択し、「保存する」をクリックしてください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/62acbc6f847a833939cc592bcc2d8f47.png)

### login,tokenエンドポイントへのリクエスト実装

`stores/authentication.js`を下記に修正します。

```diff
...
     async login(payload) {
-      // dummy request(succeed/fail after 1 sec.)
-      const shouldSuccess = true;
-      const request = new Promise((resolve, reject) =>
-        setTimeout(
-          () => (shouldSuccess ? resolve() : reject(Error("login failure"))),
-          1000
-        )
-      );
-      await request;
+      const { grant_token } = await $fetch("/rcms-api/1/login", {
+          method: "POST",
+          baseURL: useRuntimeConfig().public.apiBase,
+          credentials: "include",
+          body: payload,
+      });
+      const { access_token } = await $fetch("/rcms-api/1/token", {
+          method: "POST",
+          baseURL: useRuntimeConfig().public.apiBase,
+          credentials: "include",
+          body: { grant_token: grant_token },
+      });

        this.setProfile({}) // Apply the dummy object to store.state.profile
        this.updateLocalStorage({ authenticated: true })

```

loginエンドポイントとtokenエンドポイントへリクエストされているか確認します。

ログインページを開き、Chromeの開発者ツール:ネットワークを開いた状態でログイン処理を行います。 すると、loginエンドポイントとtokenエンドポイントへとリクエストされていることが確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/79bc58bf120ff305145d5a9dfc71d706.gif)
### tokenの保持

ここまでは、ログインしているかどうかをLocalStorageの`authenticated`のフラグ値で判定していました。  
しかし、動的アクセストークンでは認証を要求するエンドポイントには実際のtoken値が必要になります。  
そのため、`authenticated`を`token`へ変更し、token値を保持するようにします。

`middleware/auth.js`を下記に修正します。

```diff
import { useStore } from '~/stores/authentication';

export default defineNuxtRouteMiddleware(async (to, from) => {
  const store = useStore();
  
  // Define public paths that don't require authentication (add any login pages that don't require authentication)
  const publicPaths = ['/login'];
  
  // Allow access if the current path is public
  if (publicPaths.some(path => to.path.startsWith(path))) {
    return;
  }
 
-  if (!store.authenticated) {
+  if (!store.access_token) {
    try {
      await store.restoreLoginState();
    } catch (err) {
      return navigateTo('/login');
    }
  }
});

```

次に、このロジックを `stores/authentication.js` でも使用するように調整します。

```diff
import { defineStore } from "pinia";

export const useStore = defineStore("authentication", {
  state: () => ({
    profile: null,
+    access_token: "",
  }),
   actions: {
    ...
+    updateLocalStorage(payload) {
+      Object.entries(payload).forEach(([key, val]) => {
+        if (val === null || val === false) {
+          localStorage.removeItem(key);
+        } else {
+          localStorage.setItem(key, JSON.stringify(val));
+        }
+      });
+    },
     async login (payload) {
        const { grant_token } = await $fetch("/rcms-api/1/login", {
        method: "POST",
        baseURL: useRuntimeConfig().public.apiBase,
        credentials: "include",
        body: payload,
      });
      const { access_token } = await $fetch("/rcms-api/1/token", {
        method: "POST",
        baseURL: useRuntimeConfig().public.apiBase,
        credentials: "include",
        body: { grant_token: grant_token },
      });

+        this.updateLocalStorage({ rcmsApiAccessToken: access_token.value })
+        this.access_token = access_token.value
+
         this.setProfile({}) // Apply the dummy object to store.state.profile
-        this.updateLocalStorage({ authenticated: true })
     },
     async restoreLoginState () {
-        const authenticated = JSON.parse(localStorage.getItem('authenticated'))
+        const rcmsApiAccessToken = JSON.parse(localStorage.getItem('rcmsApiAccessToken'))
-        if (!authenticated) {
+        if (!rcmsApiAccessToken) {
             throw new Error('need to login')
         }
         this.setProfile({}) // store dummy object.
     }
 }

```

ログイン成功後の動きを確認します。

ログインページを開き、Chromeの開発者ツール:アプリケーションを開いた状態でログイン処理を行います。 すると、`rcmsApiAccessToken`に値が保存されます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/7683dcc908622c9f2fbe03f7c53995c9.gif)
### profileエンドポイントへのリクエスト/ハンドリング実装

今までの実装では、ブラウザのLocalStorageの`rcmsApiAccessToken`フラグによってログイン済かどうかを判断する実装をしています。  
しかしながら、LocalStorageはブラウザ上で簡単に改ざんが可能です。

またセッション有効期限によって`rcmsApiAccessToken`がtrueであっても、実際には他のエンドポイントへのリクエストがアクセスエラーとなる場合もあります。  
これらによる誤動作を防ぐため、APIへアクセスすることによって、もう1クッションの追加確認をします。


そのため、`stores/authentication.js`を下記のように修正します。

```diff
export const useStore = defineStore('authentication', {
  state: () => ({
    profile: null,
    access_token: "",
  }),
  actions: {
    setProfile(profile) {
      this.profile = profile;
    },
    updateLocalStorage(payload) {
      Object.entries(payload).forEach(([key, val]) => {
        if (val === null || val === false) {
          localStorage.removeItem(key);
        } else {
          localStorage.setItem(key, JSON.stringify(val));
        }
      });
    },
    async login(payload) {
      const { grant_token } = await $fetch("/rcms-api/1/login", {
          method: "POST",
          baseURL: useRuntimeConfig().public.apiBase,
          credentials: "include",
          body: payload,
      });
      const { access_token } = await $fetch("/rcms-api/1/token", {
          method: "POST",
          baseURL: useRuntimeConfig().public.apiBase,
          credentials: "include",
          body: { grant_token: grant_token },
      });
      
      this.updateLocalStorage({ rcmsApiAccessToken: access_token.value })
      this.access_token = access_token.value

-      this.setProfile({}) // Apply the dummy object to store.state.profile
+      const { authFetch } = useAuthFetch(this.access_token);
+      const profileRes = await authFetch("/rcms-api/1/profile", {
+        baseURL: useRuntimeConfig().public.apiBase,
+      });
+      this.setProfile(profileRes);
    },
    async restoreLoginState() {
      const rcmsApiAccessToken = JSON.parse(localStorage.getItem('rcmsApiAccessToken'))

      if (!rcmsApiAccessToken) {
        throw new Error("need to login");
      }
+      this.access_token = rcmsApiAccessToken;
      try {
-      this.setProfile({}) // Apply the dummy object to store.state.profile
+        const { authFetch } = useAuthFetch(this.access_token);
+        const profileRes = await authFetch("/rcms-api/1/profile", {
+          baseURL: useRuntimeConfig().public.apiBase,
+        });
+        this.setProfile(profileRes);
      } catch {
        throw new Error("need to login");
      }
     }
  },
  getters: {
    authenticated: (state) => state.profile !== null,
    token: (state) => state.access_token,
  },
});

```

また、アプリケーション全体で、エンドポイントに動的アクセストークンを付与する仕組みをコンポーザブル（composables）を使って実現します。  
以下の `composables/authFetch.js` ファイルを作成してください：

```js
export const useAuthFetch = (accessToken = null) => {
  // If no token provided, try to get it from store
  let token = accessToken;
  if (!token) {
    const store = useStore();
    token = store.access_token;
  }

  const authFetch = (url, config = {}) => {
    return $fetch(url, {
      ...config,
      headers: {
        ...(config.headers || {}),
        "X-RCMS-API-ACCESS-TOKEN": token,
      },
    });
  };

  return { authFetch };
};
```

ログイン後、ブラウザの画面更新をしてニュース一覧画面に遷移し、ログイン状態がリストアされることを確認します。

ログインページを開き、Chromeの開発者ツール:アプリケーションを開いた状態でログイン処理を行います。 すると、`rcmsApiAccessToken`に値が保存されます。

また、この状態で、「ニュース一覧ページへ」をクリックし画面遷移しても、`rcmsApiAccessToken`に値が保存されたままであることを確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/49669f73da2cd59af13c17bf9a37ceb8.gif)
さらに、LocalStorageの`rcmsApiAccessToken`をChromeの開発者ツールより修正した場合、リストア時にログイン画面へ強制的に画面遷移されることが確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5edfbdf317001395e794f30c6ca8380e.gif)

### logoutエンドポイントへのリクエスト/ハンドリング実装

次に、ログアウト処理を実装します。

Kuroco側でセッションが残っていながらフロント側で再ログインした場合など、予期せぬ動作が発生する可能性もあります。  
そのため、ログイン状態ではないと判定する場合はAPIへログアウト状態にするようリクエストする必要があります。

`/stores/authentication.js`を下記のように修正します。

```diff
...
-   async restoreLoginState() {
+    async logout() {
+      try {
+        const { authFetch } = useAuthFetch();
+        await authFetch("/rcms-api/1/logout", {
+          method: "POST",
+          baseURL: useRuntimeConfig().public.apiBase,
+          credentials: "include",
+        });
+      } catch {
+        /** No Process */
+        /** When it returns errors, it consider that logout is complete and ignore this process. */
+      }
+      this.setProfile(null);
+      this.access_token = "";
+      this.updateLocalStorage({ rcmsApiAccessToken: null });
+
+      navigateTo("/login");
+    },
+   async restoreLoginState() {
      const rcmsApiAccessToken = JSON.parse(localStorage.getItem('rcmsApiAccessToken'))

      if (!rcmsApiAccessToken) {
        await this.logout();
        throw new Error("need to login");
      }
      this.access_token = rcmsApiAccessToken;
      
      try {
        const { authFetch } = useAuthFetch(this.access_token);
        const profileRes = await authFetch("/rcms-api/1/profile", {
          baseURL: useRuntimeConfig().public.apiBase,
        });
        this.setProfile(profileRes);
      } catch {
+        await this.logout();
        throw new Error("need to login");
      }
    },
  },
```

また、ニュース一覧画面を以下のように修正し、ログアウトボタンを作成します。

```diff
diff --git pages/news/index.vue pages/news/index.vue
index dcdd806..e79e075 100644
--- pages/news/index.vue
+++ pages/news/index.vue
@@ -1,23 +1,31 @@
 <template>
     <div>
+        <button type="button" @click="logout">
+            Logout
+        </button>
         <div v-for="n in response.list" :key="n.slug">
             <nuxt-link :to="'/news/'+ n.slug">
                 {{ n.ymd }} {{ n.subject }}
             </nuxt-link>
         </div>
     </div>
 </template>

 <script setup>
+import { useStore } from "~/stores/authentication";
const config = useRuntimeConfig();
definePageMeta({
  middleware: ["auth"], // Use the 'auth' middleware defined in middleware/auth.ts
});

const { data: response } = await useFetch("/rcms-api/1/news", {
  baseURL: config.public.apiBase,
  credentials: "include",
});
+ const store = useStore();
+ const logout = () => store.logout();
 </script>
```

ログイン状態のニュース一覧画面にてログアウトボタンをクリックすると、下記となることを確認します。
- logoutエンドポイントへリクエストしている
- ログイン画面に遷移する
- そのままログインせずにニュース一覧画面へアクセスすると、ログイン画面に自動遷移される

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a1fc423b3d9bb866e38ec20091f21020.gif)
以上でAPIセキュリティが動的アクセストークンの場合のログイン処理の実装が完了です。

## 参考
以上でKurocoを利用したNuxt.jsプロジェクトで、ログイン画面の作成方法の紹介を終わります。

今回は基本的な説明のため、簡単にログイン画面を作成して最低限のログイン制御を実現しました。
実際に利用する際には、フォームのバリデーション処理や、`@nuxt/auth` などのライブラリをご利用いただく必要性が考えられますが、基本的なログイン構築の流れの理解としてご利用いただければ幸いです。

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [新規会員登録画面を構築する](/ja/docs/tutorials/setting-up-registration-form/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [profile APIの役割について](/ja/docs/faq/about-profile-api/)
