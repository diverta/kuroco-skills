# Kurocoドキュメント: Kurocoについて

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Kurocoについて（`about-kuroco`）
- 災害対策（DR）（`disaster-recovery`）
- Kurocoの解約について（`how-do-i-terminate-my-contract`）
- どのようなときに従量課金として計上されますか（`how-much-does-kuroco-cost`）
- Jamstackについて（`jamstack`）
- Jamstackのアーキテクチャパターン（`jamstack-architecture`）
- Jamstackを学ぶためのリソース（`jamstack-resources`）
- Jamstackと一般的なWebサイトの違い（`jamstack-website`）
- KurocoFrontについて（`kurocofront`）
- 有償サポート（`paid-support`）
- Kuroco パートナープログラム（`partners`）
- 資料（`sales`）
- セキュリティ（`security`）
- 関連サービスに関するご契約（`service_request`）
- サポート（`support`）
- ヘッドレスCMSとは？国産の開発者が語る背景、メリット、デメリット、従来のCMSとの比較まで（`what-is-a-headless-cms`）
- Jamstackの利点と欠点（`why-jamstack`）


---

# Kurocoについて

> 元ページ: `about/about-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/about/about-kuroco/
> 概要: KurocoはAPIファーストのHeadless CMSです。従来のCMSのようにシステムに縛られることなく、柔軟なシステムの構築が可能となります。欲しい機能を、欲しい時に、欲しいだけ、選び取ってください。

KurocoとはAPIファーストのHeadless CMSです。  
従来のCMSのようにシステムに縛られることなく、柔軟なシステムの構築が可能となります。  
欲しい機能を、欲しい時に、欲しいだけ、選び取ってください。

![Kurocoの特徴](/files/user/img/documentation/image13.png)

## Kurocoの特徴
### 複数の会社が同時に開発できる
- API連携で高速開発。タイムラグのない世界へ！
- APIを管理画面から設計して、柔軟でスムーズな開発体験を！

### 技術スタックに囚われない
- いつもの環境でコンテンツ追加。好きな言語で開発できる！
- CMS構築のために新しく技術を習得しなくてOK！

### パーソナライズ対応
- デバイスに囚われない、パーソナライズを実現！
- 複数のタッチポイントで顧客の体験価値を向上！

## Kurocoに向いている人
- 様々なデバイスでコンテンツを表示させたい。
- すでに使っているサービスや自社のサービスと連携させたい。
- デザイナーやエンジニア、ライターを各業務に集中させたい。
- エンタープライズ対応のCMSを探している。

## もっとKurocoを知るために
より詳しい使い方はドキュメントに記載しています。ぜひご覧ください。
- [Kurocoドキュメント トップへ](/ja/docs/)

ドキュメントだけでは解決しない場合、ぜひSlackコミュニティにご参加ください。サポート担当チームと直接やりとりができます。
- [Kuroco Slackコミュニティへ](/ja/docs/about/support/)

## 関連ドキュメント
- [ヘッドレスCMSとは？国産の開発者が語る背景、メリット、デメリット、従来のCMSとの比較まで](/ja/docs/about/what-is-a-headless-cms/)
- [Jamstackについて](/ja/docs/about/jamstack/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [アカウント登録する](/ja/docs/tutorials/signup/)
- [サポート](/ja/docs/about/support/)


---

# 災害対策（DR）

> 元ページ: `about/disaster-recovery` ｜ 公式ページ: https://kuroco.app/ja/docs/about/disaster-recovery/
> 概要: Kurocoのマルチアベイラビリティゾーン（マルチAZ）構成と、リージョン規模の災害に備えたディザスタリカバリ（DR）対応について説明します。

Kurocoには、Google Cloud Platform（GCP）上で提供する**パブリックSaaS版**と、AWS上にお客様専用環境を構築するISMAP対応の**プライベートSaaS版**の2つの提供形態があり、いずれの提供形態でも障害・災害の規模に応じて多層的な対策を行っています。
このページでは、Kurocoの冗長化構成とディザスタリカバリ（DR）対応、およびお客様の要件に応じた提供形態・オプション選択の目安について説明します。

:::note 本ページの対象
本ページのDR対応（大阪リージョンへのバックアップ・復旧）は、**東京リージョンで構築された環境**を対象とした説明です。
パブリックSaaS版は東京のほかに米国（アイオワ）・EU（フィンランド）リージョンも選択できます。米国・EUリージョンをご利用の場合のDR構成については、お問い合わせください。
:::

## 災害対策の全体像

障害・災害は規模によって必要な対策が異なります。Kurocoでは次の2つのレベルに分けて対策しています。

| レベル | 想定される事象 | Kurocoの対策 |
|---|---|---|
| **AZ（データセンター）レベルの障害** | 単一データセンターの火災・停電・空調故障、ハードウェア障害、ネットワーク障害など | マルチAZ構成により、残りのAZでサービスを継続 |
| **リージョンレベルの災害** | 首都圏直下地震など広域災害により、東京リージョン内の複数AZが同時かつ長期間停止する事態 | 大阪リージョンに保管したバックアップからの復旧（プライベートSaaS版はホットスタンバイオプションあり） |

:::info AZ（アベイラビリティゾーン）とは
同一リージョン内で地理的に分離され、電源・ネットワーク設備がそれぞれ独立したデータセンター群のことです。1つのAZで障害が発生しても、他のAZには影響が及ばないように設計されています。
:::

## マルチAZ構成による冗長化（標準）

Kurocoは標準で複数のAZにまたがる冗長構成となっており、データセンター単位の障害が発生しても、残りのAZで自動的にサービスを継続します。お客様側での作業は不要です。

| 提供形態 | 基盤 | 構成 |
|---|---|---|
| パブリックSaaS版 | GCP | 3AZのマルチAZ構成 |
| プライベートSaaS版 | AWS（お客様専用のサブアカウント環境） | 2AZのマルチAZ構成（基本構成） |

マルチAZ構成で対応できるのは、あくまで**リージョン内の一部AZにとどまる障害**です。東京リージョン全体が被災するような広域災害には、次に説明するリージョンレベルのDRが必要になります。

## リージョンレベルの災害への備え（DR）

### 大阪リージョンへのバックアップ（標準）

東京リージョンで構築されたKuroco環境のバックアップは、パブリックSaaS版・プライベートSaaS版ともに大阪リージョンに保管されています。万一、東京リージョン全体が被災した場合でも、データは大阪リージョンに保全されています。

### リージョン障害時の復旧対応

東京リージョン全体が利用できなくなった場合の復旧対応は、提供形態およびオプションの有無によって異なります。

:::caution 大規模災害時のリソース確保について
東京リージョン全体が利用できなくなるような大規模災害では、東京リージョンを利用していた多くのシステムの復旧需要が大阪リージョンに集中し、大阪リージョンのクラウドリソースが枯渇する事態も予想されます。
そのため、大阪リージョンのホットスタンバイオプションを利用していない場合は、バックアップからの立ち上げに時間がかかる、または海外リージョンでの立ち上げとなる可能性が想定されます。
:::

#### パブリックSaaS版

大阪リージョンに保管されたバックアップから環境を復旧します。
復旧時間に関するSLA（保証）は提供していませんが、できる限り早期に復旧できるよう努めます。
東京リージョン復旧後の切り戻しに費用はかかりません。

#### プライベートSaaS版（標準）

パブリックSaaS版と同様に、大阪リージョンのバックアップからの復旧となり、できる限り早期の復旧に努めます。
東京リージョン復旧後の切り戻しは、作業費**55万円/回（税込）**にて弊社が実施します。

#### プライベートSaaS版 + 大阪ホットスタンバイオプション

プライベートSaaS版では、オプションとして大阪リージョンにホットスタンバイ環境を構築しておくことができます。

- 大阪リージョンにスタンバイ環境を常時稼働させておきます。スタンバイ環境のリソースを事前に確保しているため、大規模災害時に大阪リージョンのリソースが枯渇した場合でも影響を受けにくい構成です。
- 災害発生時は、事前にご提供する切り替え手順を実行することで、**15分程度**で大阪リージョン側の環境が立ち上がります。切り替え手順は、お客様のお手元のPCでの簡単なコマンドライン実行を想定しており、緊急時にお客様ご自身で迅速に切り替えを開始できます。
- 東京リージョン復旧後の切り戻しは、作業費**55万円/回（税込）**にて弊社が実施します。

:::info プライベートSaaS版の提供形態について
プライベートSaaS版には、インフラを弊社が提供するManaged形態と、お客様のAWSアカウント内に構築するSelf-Hosted（BYOC）形態があります。大阪ホットスタンバイオプションはいずれの形態でもご利用いただけますが、Self-Hosted（BYOC）の場合の設定費用等についてはお問い合わせください。
詳細は[オンプレミス版の提供はありますか？](/ja/docs/faq/a-on-premises-version-availability/)を参照してください。
:::

## SSG構成による配信側の災害対策 {#ssg-dr}

ここまでに説明したCMS基盤側の対策に加えて、サイトのアーキテクチャ自体をDR戦略の一つとすることもできます。

KurocoはヘッドレスCMSのため、SSG（静的サイトジェネレーター）構成を採用すると、ビルド済みの静的ファイルをCDN＋高冗長化された静的ファイル配信サービスから配信する形になります。この構成では、**仮にCMS（Kuroco）側が停止しても、公開済みサイトの配信は継続されます**。災害時に影響を受けるのは、管理画面でのコンテンツ更新や、APIを利用する動的機能に限定されます。

さらに静的ファイル配信側にも冗長化が必要な場合は、次のような構成が考えられます。

- **マルチCDN戦略**: 複数のCDNを併用し、一方のCDNに障害が発生しても配信を継続する構成です。
- **DNSフェイルオーバー**: 配信側の障害を検知し、DNSで別の配信先に自動的に切り替える構成です。

また、Kuroco Frontをご利用の場合、マルチリージョン対応（デフォルトはシングルリージョン）にすることができます。マルチリージョン対応にする場合は、オプション費用として**+2.2万円/月（税込）**がかかります。

SSG構成の詳細は[Jamstackについて](/ja/docs/about/jamstack/)や[KurocoFront](/ja/docs/about/kurocofront/)を参照してください。配信側の冗長化構成については、お客様の要件によって構成が異なりますので、[お問い合わせフォーム](https://kuroco.zendesk.com/hc/ja)よりご相談ください。

## プラン選択の目安

どのレベルの災害まで、どの程度の復旧スピードを求めるかによって、適したプランが変わります。

| | パブリックSaaS版 | プライベートSaaS版 | プライベートSaaS版<br/>+ 大阪ホットスタンバイ |
|---|---|---|---|
| 基盤 | GCP | AWS | AWS |
| マルチAZ構成 | 3AZ | 2AZ（基本構成） | 2AZ（基本構成） |
| AZレベルの障害 | サービス継続 | サービス継続 | サービス継続 |
| 大阪リージョンへのバックアップ | ○ | ○ | ○ |
| リージョン災害時の復旧 | ベストエフォート | ベストエフォート | 切り替え手順の実行で15分程度で復旧 |
| リージョン災害時の復旧先 | 大阪リージョン<br/>（リソース枯渇時は時間を要する、または海外リージョン） | 大阪リージョン<br/>（リソース枯渇時は時間を要する、または海外リージョン） | 大阪リージョン<br/>（リソース事前確保済み） |
| リージョン災害時の復旧時間目安 | 規定なし | 規定なし | 15分程度 |
| 切り戻し費用 | 不要 | 55万円/回（税込） | 55万円/回（税込） |

選択の目安は次のとおりです。

- **AZレベルの障害に備えられれば十分で、リージョン災害時はベストエフォートの復旧（時間を要する場合や海外リージョンでの立ち上げとなる場合を含む）で許容できる**
  → パブリックSaaS版、またはプライベートSaaS版（標準）で対応できます。日本国内でリージョン全体が長期間停止するような事態は、首都圏直下地震クラスの広域災害を想定したものであり、発生頻度は極めて低いものです。
- **リージョン災害時にも短時間（15分程度）での復旧が求められる**
  → プライベートSaaS版 + 大阪ホットスタンバイオプションをご検討ください。金融・社会インフラ・BCP要件の厳しい企業サイトなど、事業継続計画（BCP）上、リージョン災害時の復旧時間目標（RTO）が明確に定められている場合に適しています。
- **お客様のAWSアカウント内での構築（Self-Hosted/BYOC）が求められる**
  → プライベートSaaS版をご検討ください。詳細は[オンプレミス版の提供はありますか？](/ja/docs/faq/a-on-premises-version-availability/)を参照してください。
- **災害時にも公開サイトの表示継続を最優先したい（閲覧中心のサイト）**
  → 提供形態を問わず、SSG構成の採用をご検討ください。CMS側が停止しても公開済みサイトの配信は継続されます。詳細は[SSG構成による配信側の災害対策](#ssg-dr)を参照してください。

ご不明な点やお見積りについては、[お問い合わせフォーム](https://kuroco.zendesk.com/hc/ja)よりご相談ください。

## 関連ページ

- [セキュリティ](/ja/docs/about/security/)
- [Kurocoの料金について](/ja/docs/about/how-much-does-kuroco-cost/)
- [オンプレミス版の提供はありますか？](/ja/docs/faq/a-on-premises-version-availability/)

## 関連ドキュメント
- [セキュリティ](/ja/docs/about/security/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [Jamstackについて](/ja/docs/about/jamstack/)
- [バックアップ](/ja/docs/management/backup/)
- [Kurocoサービスのサーバーは冗長化されていますか？](/ja/docs/faq/are_the_kuroco_service_redundant/)
- [オンプレミス版の提供はありますか？](/ja/docs/faq/a-on-premises-version-availability/)


---

# Kurocoの解約について

> 元ページ: `about/how-do-i-terminate-my-contract` ｜ 公式ページ: https://kuroco.app/ja/docs/about/how-do-i-terminate-my-contract/
> 概要: ご解約をご希望の際には、Kuroco管理画面の[環境設定]->[アカウント設定]の[サイトの削除]から手続きをお願いいたします。

<head>
    <link rel="canonical" href="https://kuroco.app/ja/docs/faq/how-do-i-terminate-my-contract/" />
</head>

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

> 元ページ: `about/how-much-does-kuroco-cost` ｜ 公式ページ: https://kuroco.app/ja/docs/about/how-much-does-kuroco-cost/
> 概要: Kurocoは従量課金モデルとなります。そのため、毎月ご利用分のみお支払いいただくようになります。料金体系は下記をご覧ください。

<head>
    <link rel="canonical" href="https://kuroco.app/ja/docs/faq/how-much-does-kuroco-cost/" />
</head>

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
現在、管理画面の処理時間は費用に計上されませんが、今後、トリガーによって動作するカスタム処理の処理時間はバッチ処理と同様に計上される予定になっております。
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


---

# Jamstackについて

> 元ページ: `about/jamstack` ｜ 公式ページ: https://kuroco.app/ja/docs/about/jamstack/
> 概要: Jamstackとは、静的なHTMLをベースとして、必要に応じて動的にコンテンツを取得し、Webサイトを書き換えるWebアプリ・Webサイトのアーキテクチャのことを言います。Jamstackに則ることでWebサイトをより速く、より安全に、そして簡単に拡張できるよう設計できます。

Jamstackとは、静的なHTMLをベースとして必要に応じて動的にコンテンツを取得し、Webサイトを書き換えるWebアプリ・Webサイトのアーキテクチャのことを言います。Jamstackに則ることでWebサイトをより速く、より安全に、そして簡単に拡張できるよう設計できます。

## Jamstackの意味

Jamstackは**J**avaScript、**A**PIそしてプリレンダリングされた**M**arkupを組み合わせた技術スタック（**Stack**）を組み合わせた造語です。Jamstackを提唱しているNetlify創業者のMatt Biilmann氏は、特にWebサーバーに依存しない点も特徴として挙げています。

## Jamstackの特徴

Jamstackで大事なキーワードになるのが **プリレンダリング** と **デカップリング（分離）** です。

### プリレンダリング

Jamstackを利用する多くのフレームワークでは、専用の記法やテンプレートを用います。そしてWebサイトとして配置する際にはテンプレートから静的なHTMLに変換します。従来のWebサイトのようにユーザーのリクエストに応じて都度HTMLを生成する仕組みではありません。あらかじめHTMLやCSS、JavaScript、画像などのアセットを生成することからプリレンダリングと呼ばれます。

こうした静的コンテンツはCDNを利用することで、高速な配信が可能となります。

### デカップリング（分離）

ただのHTMLだけで作られたWebサイトとの違いは、JavaScriptを活用してバックエンドサーバーと通信し、動的なコンテンツ提供することです。認証やコメント機能、決済、ユーザーに応じたパーソナライズなど、一般的に動的な仕組みが必要な部分についてはJavaScriptを活用して実現されます。

APIエコノミーの発展によって、複雑なサーバーサイドを開発することなく機能を実装できるようになっています。Jamstackサイトでは、こうしたAPI群を活用することで、技術的複雑性やリスクを分離します。APIによる分離はJamstackサイトの柔軟性や移植性を高められます。

## 他のコンテンツ

### [Jamstackと一般的なWebサイトの違い](/ja/docs/about/jamstack-website/)

Jamstackと一般的なWebサイトの相違点について解説しています。

### [Jamstackの利点と欠点](/ja/docs/about/why-jamstack/)

Jamstackで構築する利点と欠点について解説しています。

### [Jamstackを学ぶためのリソース](/ja/docs/about/jamstack-resources/)

Jamstackをより深く学ぶのに役立つリソースを紹介しています。

### [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)

Jamstackのアーキテクチャパターンと、それぞれの違いについて解説しています。

## 関連ドキュメント
- [Jamstackと一般的なWebサイトの違い](/ja/docs/about/jamstack-website/)
- [Jamstackの利点と欠点](/ja/docs/about/why-jamstack/)
- [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)
- [Jamstackを学ぶためのリソース](/ja/docs/about/jamstack-resources/)
- [ヘッドレスCMSとは？国産の開発者が語る背景、メリット、デメリット、従来のCMSとの比較まで](/ja/docs/about/what-is-a-headless-cms/)


---

# Jamstackのアーキテクチャパターン

> 元ページ: `about/jamstack-architecture` ｜ 公式ページ: https://kuroco.app/ja/docs/about/jamstack-architecture/
> 概要: Jamstackでは、「SPA」「SSG」「SSR」「ISR」の4つにアーキテクチャを分けることができます。それぞれの違いについて解説します。

Jamstackでは、そのHTMLレンダリング方式によって、アーキテクチャを4つに分けることができます。

- SPA
- SSG
- SSR
- ISR

ここでは、それぞれの違いについて解説します。

## それぞれの比較

各アーキテクチャにおける相違点を以下にまとめて紹介します。

|                 | SPA | SSG | SSR | ISR |
|-----------------|-----|-----|-----|-----|
| レンダリングを実行する場所 | クライアント | サーバー | サーバー | サーバー |
| ページレンダリングタイミング | クライアントがレスポンスを受け取った際 | サーバーがリクエストを受ける前に事前にページを生成 | サーバーがリクエストを受け取った際 | サーバーがリクエストを受け取った際(キャッシュが無い場合) |
| ページ内容の新しさ | ◎ | △ | ◎ | ○ |
| SEO              | △ | ◎ | ◎ | ◎ |
| 表示の高速さ      | ○ | ◎ | △ | ◎<br />(初回リクエスト時に生成) |
| 各ページのOGP     | × | ◎ | ◎ | ◎ |
| セキュリティ      | △ | ◎ | △ | ○ |
| サーバー負荷        | ○ | ◎ | △ | ○ |

## SPA

SPAはSingle Page Applicationの略になります。CSR（Client Side Rendering）とも呼ばれます。CSRの名前の通り、クライアント側でHTMLをレンダリングするのが特徴になります。SPAの場合、最初のリクエスト時にHTMLを返却します。続いてHTML内に記述されているJavaScript/CSSをリクエストおよび返却します。HTMLの返却方法としては静的または動的のいずれもありますが、多くの場合静的にHTMLを返します。

そして、さらに表示するのに必要なデータもAPI経由で取得するケースが多いです。最初に取得したHTMLをレンダリングした後、APIリクエストなどで取得したデータを処理するため、初期表示は若干遅くなります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d45bf1e4ff5167294faee1777ca641db.png?witdh=600)
<!---
@startuml
"ブラウザ" -> "HTTPサーバー" : リクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "ブラウザ" : HTMLを返却
deactivate "HTTPサーバー"

"ブラウザ" -> "HTTPサーバー" : リクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "ブラウザ" : JS/CSSを返却
deactivate "HTTPサーバー"

"ブラウザ" -> "HTTPサーバー" : APIリクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "ブラウザ" : データを返却
deactivate "HTTPサーバー"

"ブラウザ" -> "ブラウザ" : レンダリング
@enduml
-->

画面遷移やボタンを押したりするイベントが発生した際には、必要に応じてクライアントがサーバーに対してリクエストを行います。リクエストは不要で、JavaScriptだけで画面遷移のような処理を行う場合もあります。サーバーはリクエストに対する最低限のデータだけを返却して、クライアントにて描画します。差分だけなので、2回目以降の表示処理は高速です。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/45aaeb2f830f8dab04251d9cab01e590.png?witdh=600)
<!---
@startuml
"ブラウザ" -> "HTTPサーバー" : APIリクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "ブラウザ" : データを返却
deactivate "HTTPサーバー"

"ブラウザ" -> "ブラウザ" : 表示差分更新
@enduml
-->

## SSG

SSGはStatic Site Generationの略になります。サーバー側で、あらかじめ静的なHTMLやJavaScript、CSSを生成しておくのが特徴です。あらかじめコンテンツを生成し、そのコンテンツをCDNに登録します。そのため、初回に限らず表示処理が高速です。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/301b21eebaa0d649a9c52bfae8d5694e.png?witdh=600)
<!---
@startuml
participant "ブラウザ" order 10
participant "HTTPサーバー" order 30
participant "CDN" order 20
"HTTPサーバー" -> "HTTPサーバー" : HTML/JS/CSSを生成
"HTTPサーバー" -> "CDN": HTML/JS/CSSを登録
"ブラウザ" -> "CDN": リクエスト
activate "CDN"
"CDN" -> "ブラウザ": HTML
deactivate "CDN"
"ブラウザ" -> "CDN": リクエスト
activate "CDN"
"CDN" -> "ブラウザ": JS/CSSを返却
deactivate "CDN"
@enduml
-->

SSGの難点はコンテンツの生成頻度によっては、古いコンテンツのままになってしまう点でしょう。CDNのキャッシュを有効に使うためには、なるべく長いキャッシュを利用しつつも、頻繁にアップデートされるコンテンツを含まないようにするなど、古くならない工夫が必要です。

## SSR

SSRはServer Side Renderingの略になります。CSRがクライアント側だったのに対して、SSRはサーバー側でHTMLを生成します。常にサーバー側で表示するHTMLを生成しますので、常に最新の状態に保てるのがメリットです。ただしコンテンツのキャッシュが難しく、CDNを使っている場合と比べて速度が遅かったり、サーバー側の負荷が大きくなります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9286be838f80088db7b9a846edbb96b4.png?witdh=600)
<!---
@startuml
"ブラウザ" -> "HTTPサーバー": リクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "アプリケーションサーバー": リクエスト
activate "アプリケーションサーバー"
"アプリケーションサーバー" -> "アプリケーションサーバー" : HTML生成
"アプリケーションサーバー" -> "HTTPサーバー" : HTML返却
deactivate "アプリケーションサーバー"
"HTTPサーバー" -> "ブラウザ": HTML
deactivate "HTTPサーバー"

"ブラウザ" -> "HTTPサーバー": リクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "ブラウザ": JS/CSSを返却
deactivate "HTTPサーバー"
@enduml
-->

## ISR

ISRはIncremental Static Regenerationの略になります。SSRのようにクライアントからのリクエスト時にページを生成するのですが、それをキャッシュして2回目以降のリクエスト時に利用します。SSGの場合、あらかじめすべてのページを生成しますので、ページ数が多いと生成に時間がかかります。ISRの場合、リクエストがあるまではページを生成しませんので、サーバーの立ち上げが高速です。

ISRではキャッシュの有効期限を決められます。キャッシュ生成から時間が経つと、再度サーバー側でページを生成します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cc479964da7781fbe7c20be294a7ee0a.png?witdh=600)
<!---
@startuml
participant "ブラウザ" order 10
participant "HTTPサーバー" order 30
participant "CDN" order 20

"ブラウザ" -> "HTTPサーバー": リクエスト
note left: 1回目のアクセス
activate "HTTPサーバー"
"HTTPサーバー" -> "HTTPサーバー": HTMLを生成
"HTTPサーバー" -> "ブラウザ": HTMLを返却
"HTTPサーバー" -> "CDN": HTMLを登録
deactivate "HTTPサーバー"
"ブラウザ" -> "HTTPサーバー": リクエスト
activate "HTTPサーバー"
"HTTPサーバー" -> "ブラウザ": JS/CSSを返却
"HTTPサーバー" -> "CDN": JS/CSSを登録
deactivate "HTTPサーバー"
...


"ブラウザ" -> "CDN": リクエスト
activate "CDN"
note left: 2回目以降のアクセス
"CDN" -> "ブラウザ": HTMLを返却
deactivate "CDN"
"ブラウザ" -> "CDN": リクエスト
activate "CDN"
"CDN" -> "ブラウザ": JS/CSSを返却
deactivate "CDN"
@enduml
-->

## 関連ドキュメント
- [Jamstackについて](/ja/docs/about/jamstack/)
- [Jamstackと一般的なWebサイトの違い](/ja/docs/about/jamstack-website/)
- [Jamstackの利点と欠点](/ja/docs/about/why-jamstack/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)
- [コーポレートサンプルサイトをSSGにする](/ja/docs/tutorials/corporate-sample-site-to-ssg/)


---

# Jamstackを学ぶためのリソース

> 元ページ: `about/jamstack-resources` ｜ 公式ページ: https://kuroco.app/ja/docs/about/jamstack-resources/
> 概要: Jamstackをより深く学ぶのに役立つコンテンツを紹介します。

ここではJamstackをより深く学ぶのに役立つコンテンツを紹介します。

## Webサイト

### [Jamstack](https://jamstack.org/)

Jamstack公式サイトです。

### [JAMstack -JP-](https://jamstack.jp/)

日本語でJamstackに関する情報を発信しているサイトです。

### [JAMstackの紹介](https://www.infoq.com/jp/news/2020/10/introducing-jamstack/)

技術メディアInfoQによるJamstackの紹介です。

### [Welcome to the Jamstack](https://www.netlify.com/jamstack/)

Jamstackを提唱しているNetlifyによるJamstack紹介ページです。

### [Gatsby と Netlify で Jamstack 構成のブログサイトを作ろう - to-R Media](https://www.to-r.net/media/jamstack-demo/)

静的サイトジェネレータのGatsbyと静的ホスティングサービスNetlifyでブログサイトを構築する記事です。

## 書籍

### [JAMstack 完全入門 ハイパフォーマンス Web サイト構築](https://booth.pm/ja/items/1035934)

BOOTHで販売されている電子書籍です。Jamstackが何か、について初心者向けに分かりやすく説明してくれます。

### [Webサイト高速化のための　静的サイトジェネレーター活用入門](https://www.amazon.co.jp/dp/B088WJWJK9/)
Gatsby × GitHub × Netlify × Contentfulによるサイト構築をステップバイステップで解説します。


### [JAMStackを学ぼう初級編Gatsby, React bootstrap, Netlifyでつくる企業サイト第２版: もうレンタルサーバーはいらない](https://www.amazon.co.jp/dp/B08DKQ1Q9S/)

初級編ではありますが、多少なりとも技術的な経験がある方向けの書籍になります。

### [JAMStackを学ぼう中級編 GatsbyとヘッドレスCMSでつくるコーポレートサイト ～WordPressはもう古い～](https://www.amazon.co.jp/dp/B08KRPTW2R/)

GatsbyとmicroCMSを使ってコーポレートサイトを構築するという実践的な書籍になります。

### [はじめてつくるGatsbyサイト](https://www.amazon.co.jp/dp/B08YX61888/)

Jamstackとしてよく使われているGatsbyで簡単なWebサイトを開発する書籍です。

### [はじめてつくるNext.jsサイト](https://www.amazon.co.jp/dp/B08ZSB1215/)

Jamstackとしてよく使われているNext.jsで簡単なWebサイトを開発する書籍です。

## 動画

### [Jamstack TV - YouTube](https://www.youtube.com/channel/UC8bRyfU7ycLXnEBfvdorpUg)

Jamstack公式のYouTubeチャンネルです。[Jamstack Conf October 2020](https://jamstackconf.com/2020/october/)の動画などが閲覧できます。

### [JAMStack: The Complete Guide | Udemy](https://www.udemy.com/course/jamstack/)

UdemyによるJamstack学習コンテンツです。英語ですが字幕付きです。

## 関連ドキュメント
- [Jamstackについて](/ja/docs/about/jamstack/)
- [Jamstackと一般的なWebサイトの違い](/ja/docs/about/jamstack-website/)
- [Jamstackの利点と欠点](/ja/docs/about/why-jamstack/)
- [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)


---

# Jamstackと一般的なWebサイトの違い

> 元ページ: `about/jamstack-website` ｜ 公式ページ: https://kuroco.app/ja/docs/about/jamstack-website/
> 概要: 一般的なWebサイトとJamstackサイトの大きく異なる点は、WebブラウザがWebサイトを訪問してから表示されるまでの流れにあります。Jamstackと一般的なWebサイトの相違点について解説します。

ここではJamstackと一般的なWebサイトの相違点について解説します。

## 一般的なWebサイトとは

ここで挙げる一般的なWebサイトとは、最小構成として次のようなサーバー構成で実装されるWebサイトです。PHPなどHTTPサーバーとアプリケーションサーバーが一体化している場合もあります。

- **Web（HTTP）サーバー**  
Webブラウザからのリクエストを受け取り、アプリケーションサーバーを呼び出します。その結果としてHTMLを受け取り、Webブラウザに返却します。静的コンテンツを保持しそのままHTMLや画像などを返却する場合もあります。
- **アプリケーションサーバー**  
Webサーバーからデータを受け取り、データベースサーバーと情報をやり取りします。その結果としてHTMLを生成し、Webサーバーに返却します。
- **データベースサーバー**  
ユーザー、商品、コンテンツなどの情報を格納したデータベースです。アプリケーションサーバーから呼び出され、データを返却します。

Web APIを活用したWebサイトが登場する前は、このようなアーキテクチャでWebサイトを実装することが一般的でした。

## 一般的なWebサイトとJamstackサイトの同じところ

一般的なWebサイト、JamstackサイトはどちらもWebサイトである点は共通です。Webブラウザを使ってWebサイトを訪れた場合、それが昔からのWebサイトなのか、Jamstackサイトなのかは一目では分からないかも知れません。

## 一般的なWebサイトとJamstackサイトの違うところ

一般的なWebサイトとJamstackサイトの大きく異なる点は、WebブラウザがWebサイトを訪問してから表示されるまでの流れにあります。

### 一般的なWebサイトの仕組み

一般的なWebサイト（CMSやEコマースサイトなど）というのは、次のような順番でWebサイトを表示します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/bb3235f428d7fd67824efd4d8e9f5a79.png)
<!---
@startuml

Webブラウザ -> Webサーバー : リクエスト
Webサーバー -> アプリケーションサーバー : リクエスト
アプリケーションサーバー -> データベース : クエリ送信
データベース -> アプリケーションサーバー : ロジック実行
アプリケーションサーバー -> アプリケーションサーバー : HTML生成
アプリケーションサーバー -> Webサーバー : HTML
Webサーバー -> Webブラウザ : HTML
Webブラウザ -> Webブラウザ : HTML描画

@enduml
-->

1. WebブラウザがWebサーバーにリクエスト
2. Webサーバー内でアプリケーションサーバーとデータベースサーバーが情報をやり取り
3. アプリケーションサーバーがデータを使ってHTMLを生成
4. WebサーバーがHTMLをWebブラウザに返却
5. WebブラウザがHTMLを表示

WebブラウザとWebサイトでは、ページを移動するたびにこのやり取りが繰り返されます。

### Jamstackサイトの場合

それに対してJamstackを使って構築されているWebサイトは次のように実行されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3f8843c5f29cb0bd22059f821f20dd55.png)
<!---
@startuml

Webブラウザ -> "Webサーバー/CDN" : リクエスト
"Webサーバー/CDN" -> Webブラウザ : HTML
Webブラウザ -> Webブラウザ : HTML描画

@enduml
-->

1. WebブラウザがWebサーバー（Jamstackの場合はCDNを利用するのが通常）にリクエスト
2. Webサーバー（またはCDN）がHTMLをWebブラウザに返却
3. WebブラウザがHTMLを表示

アプリケーションとデータベースのやり取り、そしてアプリケーションがHTMLを生成する部分がありません。動的な処理がないので表示が高速化し、システム負荷が小さくなります。さらにコンテンツはCDNを使って配信されるので、とても高速に配信および表示できます。

そして動的な部分（決済、認証、一部の動的コンテンツなど）は、外部サービスを通じて取得します。外部サービスはごく限られた機能を提供するものが多く、マイクロサービスと呼ばれます。Webブラウザはこうしたマイクロサービスを複数、必要に応じて呼び出して1つのWebサイトを構成します。

<!---
@startuml

Webブラウザ -> 外部サービスAPI : リクエスト
外部サービスAPI -> Webブラウザ : 結果のデータ
Webブラウザ -> Webブラウザ : HTML更新

@enduml
-->

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e45bc7c6daa17c4884807dd66880a701.png)
4. Webブラウザが外部サービスのAPI（マイクロサービス）をリクエスト
5. 外部サービスが処理結果をWebブラウザに返却
6. Webブラウザが処理結果に応じてHTMLを書き換え

一般的なWebサイトとの違いとして、外部サービスはHTMLを返却しません。データ（多くはJSON）をWebブラウザに返却します。そしてデータを受け取ったWebブラウザは、JavaScriptを使って表示します。

## Webブラウザで表示処理を行うメリット

サーバー側でHTMLを生成するのと、Webブラウザでデータから表示処理を行う違いは、表示速度にあります。HTMLを表示するのはWebブラウザにとって重たい処理になります。表示する際にはDOMを解釈し、スタイルシートを適用し、画像の高さや幅を計算して表示します。これをページ遷移の度に繰り返すため、Webサイトの表示が重たいと感じる原因になります。

Jamstackの場合、データだけを受け取ります。そのため必要な部分だけ表示を差し替える方式になります。HTML全体を表示し直すことがないので、表示が高速化されます。閲覧者の体感が良くなるので、UX（ユーザー体験）も向上します。クリックして画面を遷移するごとに、このユーザー体験の差は大きくなります。

また、HTMLを生成する負荷がなくなるので、サーバー側の負荷も軽減します。認証の伴うWebサイトの場合、生成されたHTMLのキャッシュはしづらいでしょう。しかしJamstackで利用されるデータにおいては、商品一覧などのユーザー認証に依存しないデータはキャッシュしても問題ありません。こうした点もサーバー負荷軽減につながります。

## 関連ドキュメント
- [Jamstackについて](/ja/docs/about/jamstack/)
- [Jamstackの利点と欠点](/ja/docs/about/why-jamstack/)
- [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)
- [ヘッドレスCMSとは？国産の開発者が語る背景、メリット、デメリット、従来のCMSとの比較まで](/ja/docs/about/what-is-a-headless-cms/)


---

# KurocoFrontについて

> 元ページ: `about/kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/about/kurocofront/
> 概要: KurocoFrontは、CDNを利用した静的コンテンツホスティングサービスです。独自ドメイン、TLS証明書やBasic認証、IPアドレス制限までを無料で利用することが出来ます。

KurocoFrontは、CDNを利用した静的コンテンツホスティングサービスです。独自ドメイン、TLS証明書やBasic認証、IPアドレス制限までを無料で利用することが出来ます。
KurocoFrontに関するドキュメントは以下になります。順次、ドキュメントは追加予定です。

## 仕様について
- GitHub ActionsからDeployされるとGitHubのコミットハッシュ毎にファイルを静的に保持しています。  
- CDNに365日(31536000秒)の有効期限でキャッシュされます。利用するコミットハッシュが変わるとキャッシュは全てクリアされます。  
- URLに付与されているクエリーストリングはキャッシュのキーとして利用されません。  
- ファイルの拡張子がgif png jpg jpeg webpの場合には、画像が動的に変換・最適化されます。
- Trailing Slash(URL の最後につける「/」（スラッシュ）を自動的に付与する動作)が常に有効になっています。  


## チュートリアル
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [GitHubからKurocoFrontへソースをデプロイする設定](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)

## 関連ドキュメント
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [KurocoFrontでどのハッシュが利用されているかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-the-hash-responses-used-by-kurocofront/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [KurocoFrontをProxy Serverを通して別のサーバーから使うにはどのようにすればよいですか？](/ja/docs/faq/can-i-access-kurocofront-through-a-proxy-server/)
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)


---

# 有償サポート

> 元ページ: `about/paid-support` ｜ 公式ページ: https://kuroco.app/ja/docs/about/paid-support/
> 概要: 30日毎の定額制で無制限に利用できる有償サポートをご用意しております。有償サポートに申し込むことにより、より迅速かつ詳細にお問合せ内容に返答させて頂くことが可能になります。

最低30日以上の定額制で無制限に利用できる有償サポートをご用意しております。  
有償サポートに申し込むことにより、より迅速かつ詳細にお問合せ内容に返答させて頂くことが可能になります。  
本サポート業務は、メールまたは当社指定のオンラインコミュニケーションツールを利用して提供します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b232087356148dd786ed694c018e5a01.jpg)

こちらはヘッドレスCMSやAPI中心設計でのアプリケーション開発をされるお客様にとって有益であると共に、Kurocoチームにとってもお客様のニーズや改善点の早期発見ができるため、お互いに有益なプランであると確信をしております。  

## フェアユースポリシー

サポートプランは我々のもっているリソースを利用いただき、分野を問わずに素早く回答することを目指します。
そのため、以下のようにフェアユースポリシーを定めます。  

- あくまでも開発・制作・運用の主体はお客様であり、Kurocoチームはそれを補助をする
- サポート対応は原則的にご質問への回答のみであり、提案依頼や作業依頼、打合せなどはお見積もりでの対応とする
- ドキュメントの作成やシートへの記入などは原則としてお見積もりでの対応とする
- 検索エンジンで検索して分かることや、Kurocoドキュメントサイトにある事項はURLやキーワードを共有することを中心としての回答になる
- 不具合や調査の依頼に関しては、再現手順の提示までをお客様側の担当範囲とする
- 設定の精査など将来における問題を確認する作業はお見積もりでの対応とする
- JavaScriptのエラーやその他外部サービスのエラー等の確認依頼に関しては、エラーの意味の説明をするなどは可能だが、お客様が主体となって行うトラブルシューティングの手助けをする
- ベストプラクティスに関しては、外部サービス等の利用に関しても回答できることもあるが、それが必ずベストな方法であることの保証はしない
- Kurocoチームは回答が正確であることの努力をするが、回答が必ず正しいことの保証はしない
- お客様はエビデンスや確証が必要な場合はその旨をKurocoチームに伝えることができるが、必ず提供されることの保証はしない
- 回答スピードや品質向上のため、回答の作成にAIを利用する場合がある。一次回答としてAIによる参考回答をお返しするほか、AIによる出力をそのまま参考情報として用いる場合がある。AIによる生成部分はその旨を明記する
- お客様側でAIをご利用いただくことに制限はないが、AIが生成した内容そのものの正誤判定やレビュー、コードの検証を主目的としたお問い合わせはサポート対象外とする。お客様側で内容を整理のうえ、具体的なご質問としてお寄せください
- 申込みやサポート対象はKurocoアカウント毎(サブサイト含む)とする

## 有償サポートプラン一覧

下記サポートプランのご用意がございます。

### 1. プレミアムサポート

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          開発・構築作業なども含む開発業務全般の問い合わせに対応。<br />
          主にパートナー様と一緒に提供するプランです。
          <ul className="mt-3 mb-0">
            <li>デザインの問い合わせ</li>
            <li>フロントエンド実装の問い合わせ</li>
            <li>HTML・JSの問い合わせ</li>
            <li>ベストプラクティスの問い合わせ</li>
            <li>Kurocoの操作方法の問い合わせ</li>
            <li>仕様の問い合わせ</li>
          </ul>
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
          ご要望をお伺いし、お見積りいたします。
      </td>
    </tr>
  </tbody>
</table>

### 2. テクニカルサポート

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          開発業務全般の問い合わせに対応。<br />
          主に開発業務のサポートのプランです。
          <ul className="mt-3">
            <li>フロントエンド実装の問い合わせ</li>
            <li>HTML・JSの問い合わせ</li>
            <li>ベストプラクティスの問い合わせ</li>
            <li>Kurocoの操作方法の問い合わせ</li>
            <li>仕様の問い合わせ</li>
          </ul>
          <span className="text-sm">※ 簡易な管理画面操作の代行作業は可能です。</span><br />
          <span className="text-sm">※ 時間内での課題解決を保証するものではありません。</span>
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
        <ul>
            <li>13.2万円/30日 (1営業日以内を目安に返信が必要な場合)</li>
            <li>26.4万円/30日 (4時間以内を目安に返信が必要な場合)</li>
            <li>39.6万円/30日 (1時間以内を目安に返信が必要な場合)</li>
        </ul>
        <span className="text-sm">※ 構築実績による割引制度もあります。</span>
      </td>
    </tr>
  </tbody>
</table>

### 3. スタンダードサポート

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          以下の問い合わせのみを受け付けます。<br />
          <ul className="mt-3">
            <li>ベストプラクティスの問い合わせ</li>
            <li>Kurocoの操作方法の問い合わせ</li>
            <li>仕様の問い合わせ</li>
          </ul>
          <span className="text-sm">※ 簡易な管理画面操作の代行作業は可能です。</span><br />
          <span className="text-sm">※ 時間内での課題解決を保証するものではありません。</span>
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
        <ul>
            <li>9.9万円/30日 (4時間以内を目安に返信が必要な場合)</li>
            <li>16.5万円/30日 (1時間以内を目安に返信が必要な場合) </li>
        </ul>
        <span className="text-sm">※ 構築実績による割引制度もあります。</span>
      </td>
    </tr>
  </tbody>
</table>

### 4. 運用サポート

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          構築後の運用フェーズでのKurocoに関するもの含めてあらゆるご質問に対応いたします。<br />
          <span className="text-sm">※ 簡易な管理画面操作の代行作業は可能です。</span><br />
          <span className="text-sm">※ 社内リソースで回答が難しい内容のものは、検索エンジン等で調べて分かる一般的な回答になる場合があります</span><br />
          <span className="text-sm">※ 用語の説明や他社サービスの説明に関しては原則として参考ページなどのリンクをご連絡する形になります。</span>
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
        <ul>
            <li>
                Kuroco従量課金額の6% (1営業日以内を目安に返信が必要な場合)<br />
                ただし、最低価格は6.6万円/30日となります。
            </li>
            <li>
                Kuroco従量課金額の15% (4時間以内を目安に返信が必要な場合)<br />
                ただし、最低価格は13.2万円/30日となります。
            </li>
        </ul>
        <span className="text-sm">※ 年間契約も可能です。お問い合わせください。</span>
      </td>
    </tr>
  </tbody>
</table>

### 5. Kuroco RAG伴走支援サポート

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          Kuroco RAGの初期構築と調整作業について伴走します。<br />
          <span className="text-sm">※Kuroco RAGに登録するデータは電子ファイルでご提供いただき、初期構築時の登録を代行します。</span><br />
          <span className="text-sm">※時間内での調整作業は、回答精度を保証するものではありません。</span>
          <ul className="mt-3 mb-0">
            <li>初期構築支援（データ登録代行サポートを込む）</li>
            <li>月2回程度の定期的なミーティングへの参加</li>
            <li>RAGに関する調整作業（ミーティングにて決定した内容）</li>
          </ul>
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
        132万円/3ヵ月～<br />
        <span className="text-sm">※ 4か月以上のプランもご提案可能です。お問い合わせください。</span>
      </td>
    </tr>
  </tbody>
</table>

### 6. 継続的サービス開発サポート

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          開発業務全般の問い合わせに対応。<br />
          実装依頼やKurocoを利用したビジネス展開に関しても伴走いたします。<br />
          主にパートナー様と一緒に提供するプランです。
          <ul className="mt-3 mb-0">
            <li>フロントエンド実装の問い合わせ</li>
            <li>HTML・JSの問い合わせ</li>
            <li>ベストプラクティスの問い合わせ</li>
            <li>Kurocoの操作方法の問い合わせ</li>
            <li>仕様の問い合わせ</li>
          </ul>
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
        264万円/3ヶ月〜
      </td>
    </tr>
  </tbody>
</table>

### 7. 優先実装依頼

<table>
  <tbody>
    <tr>
      <th style="width:120px;">対応内容</th>
      <td>
          Kurocoに欲しい機能がある場合に、優先的に実装をするように依頼することが出来ます。<br />
          当社ロードマップ等と調整が必要になるため、必ず実装、希望要件を叶えるものではありません。
      </td>
    </tr>
    <tr>
      <th>価格</th>
      <td>
        ご要望をお伺いし、お見積りいたします。
      </td>
    </tr>
  </tbody>
</table>

※上記の価格はいずれも税込になります。

## サポートプランのお申込み・問い合わせ
サポートプランのお申込みやご質問については、お問い合わせフォームよりご連絡ください。

<a href="https://kuroco.zendesk.com/hc/ja" className="button button--primary px-5 py-3 text-base">お問い合わせフォーム</a>

## 関連ドキュメント
- [サポート](/ja/docs/about/support/)
- [関連サービスに関するご契約](/ja/docs/about/service_request/)
- [Kuroco パートナープログラム](/ja/docs/about/partners/)
- [お問い合わせのしおり](/ja/docs/troubleshooting/contact-guidelines/)


---

# Kuroco パートナープログラム

> 元ページ: `about/partners` ｜ 公式ページ: https://kuroco.app/ja/docs/about/partners/
> 概要: Kurocoパートナープログラムにご参加いただいたパートナー様には、当社よりKurocoご利用希望のお客様のご紹介や、Kurocoの技術的な相談サポートを提供させていただきます。また、各社様の協業や連携面においても全面的な支援をおこなってまいります。

## Kurocoパートナープログラムのご案内

株式会社ディバータは、2021年4月15日にリリースしたAPI中心志向の次世代CMS「Kuroco(クロコ)」において、API中心設計のJAMStackでアプリケーション構築するプロジェクトのパートナー募集を開始致しました。

KurocoはAPI中心志向のヘッドレスCMSであり、JAMStackにも相性がよいため、API利用や責任範囲の明確化がしやすく複数会社間での協業やシステム連携がスムーズです。

Kurocoパートナープログラムにご参加いただいたパートナー様には、当社よりKurocoご利用希望のお客様のご紹介や、Kurocoの技術的な相談サポートを提供させていただきます。
また、各社様の協業や連携面においても全面的な支援をおこなってまいります。

サポートの面では、全面支援プランリリースによって、新しいアーキテクチャに挑戦をしたくても経験不足等で手を出しにくかった全ての事業会社様・WEB制作会社様・システム会社様がJAMStackによるアプリケーション構築に挑戦できます。

日本におけるJAMStackでのWEBシステム構築はまだ充分に普及はしておりませんが、実績と豊富な知識を持つ当社が全面的にサポート致します。

## 概要

### パートナー様にやっていただくこと
- Kurocoを利用したWEB/システム構築

### ディバータから提供できること
- エンドユーザー様のご紹介
- 構築実績に応じたサポートプランの割引
- Kurocoの利用方法やJAMStackによるアプリケーション構築に関する相談会の開催
- Kurocoの営業・構築サポート（こちらはパートナープログラムなしでも提供されます）
- Slackプライベートチャンネルへの招待（有償サポートご利用の場合）

### 参加条件
- Kurocoをご理解いただき、パートナーとして長期にわたり連携いただけること
- JAMStackやAPI連携によるアプリケーション構築をしていくご意志があること

### 対応いただきたい分野
- システム企画設計・コンサルテーション・要件定義
- UI/UX 設計
- デザイン
- コーディング
- フロントエンド実装
- API開発（Kurocoカスタマイズや外部API連携等）
- テスト
- プロジェクトマネージメント

## パートナープログラム申し込み方法
パートナープログラムへのお申し込みご希望の場合、下記お問い合わせフォームよりご連絡ください。  
ご連絡いただいた後、３営業日以内に申込書類をお送りさせていただきます。

<a href="https://share.hsforms.com/1GimLb_VaQ1i2qIQ-PlUA4wcx94m" className="button button--primary px-5 py-3 text-base">パートナープログラムに申し込む</a>

## 関連ドキュメント
- [有償サポート](/ja/docs/about/paid-support/)
- [資料](/ja/docs/about/sales/)
- [関連サービスに関するご契約](/ja/docs/about/service_request/)
- [Kurocoを利用したプロジェクトの進行イメージ](/ja/docs/tutorials/starting-a-project-on-kuroco/)
- [サポート](/ja/docs/about/support/)


---

# 資料

> 元ページ: `about/sales` ｜ 公式ページ: https://kuroco.app/ja/docs/about/sales/
> 概要: Kurocoに関する営業時に利用できる資料をまとめています。社内での確認やお客様へのご提案などにご活用ください。

Kurocoに関する営業時に利用できる資料をまとめています。社内での確認やお客様へのご提案などにご活用ください。

## 契約書関連
|資料名|ファイル形式|ダウンロードリンク|
|:--|:--|:--|
|Kuroco利用規約|PDF|<a href="https://kuroco.app/files/legal/Kuroco-terms-of-service.pdf" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2  u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|Kurocoサポートサービス利用規約|PDF|<a href="https://kuroco.app/files/legal/Kuroco-support-terms-of-service.pdf" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|秘密保持契約書|DOCX|<a href="https://kuroco.app/files/sheets/ja/template_nda.docx" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|開発業務委託基本契約書の雛形|DOCX|<a href="https://kuroco.app/files/sheets/ja/template_basic_contract.docx" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|システム開発個別契約書の雛形|DOCX|<a href="https://kuroco.app/files/sheets/ja/template_individual_contract.docx" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|パートナープログラム参加規約|PDF|<a href="https://kuroco.app/files/sheets/ja/kuroco_partner_term_of_program.pdf" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|SLA|PDF|<a href="https://kuroco.app/files/sheets/ja/kuroco_sla.pdf" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|
|地位継承の覚書|DOCX|<a href="https://kuroco.app/files/sheets/ja/memorandum_of_succession.docx" className="button button--primary px-3 py-2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>|

## Kurocoに関する資料
### Kuroco説明資料

<a href="https://kuroco.app/files/sheets/ja/kuroco_salessheet.pdf" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_salessheet.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/kuroco_salessheet.pdf" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>

### 「AIの仕事場」のつくり方

<a href="https://kuroco.app/files/sheets/ja/ai_workplace_kuroco.pdf" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/ai_workplace_kuroco.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/ai_workplace_kuroco.pdf" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>

### 「API中心設計」を実現する本

<a href="https://kuroco.app/files/sheets/ja/api_centric_design.pdf" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/api_centric_design.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/api_centric_design.pdf" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>

### インフラに関するドキュメント 

<a href="https://kuroco.app/files/sheets/ja/kuroco_infrastructure.pdf" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_infrastructure.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/kuroco_infrastructure.pdf" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>


## プロジェクト進行管理
### 案件ヒアリングシート

<a href="https://kuroco.app/files/sheets/ja/kuroco_hearingsheet.xlsx" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_hearingsheet.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/kuroco_hearingsheet.xlsx" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>


### Kurocoを利用したプロジェクトの進め方（サンプル）

<a href="/ja/docs/tutorials/starting-a-project-on-kuroco/" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_project_sample.png" /></a>

<a href="/ja/docs/tutorials/starting-a-project-on-kuroco/" className="button button--primary px-5 py-3" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>ドキュメントを見る</a> 

### プロジェクト進行時のチェックリスト 

<a href="https://docs.google.com/spreadsheets/d/1VmnEvEUZsNY3QMmOL9e21M05pp4_J64Stn6_8-1qx_8/edit?usp=sharing" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_project_check_sheets.png" /></a>

<a href="https://docs.google.com/spreadsheets/d/1VmnEvEUZsNY3QMmOL9e21M05pp4_J64Stn6_8-1qx_8/edit?usp=sharing" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>Googleスプレッドシート</a>


### WBSやタスクリストのサンプル

<a href="https://docs.google.com/spreadsheets/d/1uWbBbQ96JFTFrEI5LyeDi54A9YjBY4nRZ_0Mie_GUsk/edit?usp=sharing" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_wbs_task_list.png" /></a>

<a href="https://docs.google.com/spreadsheets/d/1uWbBbQ96JFTFrEI5LyeDi54A9YjBY4nRZ_0Mie_GUsk/edit?usp=sharing" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>Googleスプレッドシート</a>

### プロジェクト役割分担表

<a href="https://kuroco.app/files/sheets/ja/kuroco_api_project_ram.xlsx" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/kuroco_api_project_ram.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/kuroco_api_project_ram.xlsx" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>


### タスク管理の簡単な流れ（Backlog利用）

<a href="https://kuroco.app/files/sheets/ja/task_management_with_backlog.pdf" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://kuroco.app/files/sheets/ja/png/task_management_with_backlog.png" /></a>

<a href="https://kuroco.app/files/sheets/ja/task_management_with_backlog.pdf" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>


## 参考資料
### 超上流から攻めるIT化の原理原則17ヶ条（外部サイト）
<a href="https://www.ipa.go.jp/files/000005109.pdf" className="button button--primary px-5 py-3"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="align-text-bottom mr-2 u-svg-icon-stroke-white"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>ダウンロード</a>

## 関連ドキュメント
- [関連サービスに関するご契約](/ja/docs/about/service_request/)
- [Kuroco パートナープログラム](/ja/docs/about/partners/)
- [有償サポート](/ja/docs/about/paid-support/)
- [Kurocoを利用したプロジェクトの進行イメージ](/ja/docs/tutorials/starting-a-project-on-kuroco/)
- [セキュリティ](/ja/docs/about/security/)


---

# セキュリティ

> 元ページ: `about/security` ｜ 公式ページ: https://kuroco.app/ja/docs/about/security/
> 概要: Kurocoではクラウドネイティブに構築されておりセキュリティに配慮した設計を行っております。

Kurocoではクラウドネイティブに構築されておりセキュリティに配慮した設計となっております。

## API
- 完全に暗号化されたHTTPS通信
- TLS証明書
- 独自ドメイン設定
- WAF
- CDN
- DDoS対策
- 固定トークン・ダイナミックトークン・Cookieを利用したアクセス制御
- CORSの柔軟な設定
- ユーザーのグループ設定による細かな権限の制御
- IPアドレス制限
- アクセスログ（監査ログ）
- アプリケーションログ
- SAML/OAuthによる外部ログイン連携
- クライアント証明書によるアクセス制御（オプション）
- Fastly DDoS Protection適用（オプション）

## 管理画面
- 完全に暗号化されたHTTPS通信
- TLS証明書
- WAF
- DDoS対策
- ID/PWDによるアクセス制限
- ユーザーのグループ設定による細かな権限の制御
- IPアドレス制限
- 暗号化されたトークンの保存機能
- アクセスログ（監査ログ）
- アプリケーションログ
- SMSや認証アプリによる2要素認証の設定
- SAML/OAuthによる外部ログイン連携
- クライアント証明書によるアクセス制御（オプション）

## KurocoFront
- 完全に暗号化されたHTTPS通信
- TLS証明書
- 独自ドメイン設定
- CDN
- DDoS対策
- Basic認証
- IPアドレス制限
- アクセスログ

## KurocoFiles
- 完全に暗号化されたHTTPS通信
- TLS証明書
- CDN
- DDoS対策
- ユーザーのグループ設定による細かな権限の制御
- IPアドレス制限
- アクセスログ

※KurocoFilesの他にGoogle Cloud StorageやAmazon S3を利用したユーザー認証ベースのファイルのアクセス制限などが可能です。

## データセンタ
パブリックSaaS版の利用開始時にどのデータセンタを利用するか選択できます。
- Google Cloud Platform 東京リージョン
- Google Cloud Platform EUリージョン
- Google Cloud Platform USリージョン

プライベートSaaS版の場合は、お客様の要件に合わせて構築可能です。

## 運営会社(株式会社ディバータ)
- ISMS (ISO/IEC 27001:2022 / JIS Q 27001:2023)　登録番号IA21261　[登録証](https://www.diverta.co.jp/files/user/eqa_isms_27001_20250530.pdf)
- ISMSクラウド (ISO/IEC27017:2015/JISQ27017:2016)　登録番号S0912　[登録証](https://www.diverta.co.jp/files/user/eqa_isms_27017_20250530.pdf)
- プライバシーマーク　登録番号第21000371号　[登録証](https://www.diverta.co.jp/files/user/pmark_21000371_2025.pdf)
- [生成AI活用ポリシー](https://www.diverta.co.jp/ai-policy/)

## 脆弱性診断
- 毎回のコンテナ更新時にコンテナに対する脆弱性スキャンの実施（ほぼ毎日実施）
- [VADDY](https://vaddy.net/)を利用した脆弱性診断を実施（代表サイトの標準APIのみ）
- [VADDY](https://vaddy.net/)との自動連携によるお客様サイトでのカスタマイズされたAPIの脆弱性診断が可能（※管理画面よりお申し込みいただくと自動連携機能が利用可能です）
- 個別の脆弱性診断での指摘事項で重要かつKuroco由来のものへの無償対応

## チェックリスト
Kurocoのサービスについて下記のセキュリティチェックシートの用意があり提供可能です。提供を希望する場合は[サポート](https://kuroco.zendesk.com/hc/ja)からお問い合わせください。
- 独立行政法人情報処理推進機構(IPA)監修「セキュリティ実装チェックリスト」
- 経済産業省(METI)発刊「SaaS向けSLAガイドライン別表(Kuroco版)」

## セキュリティ評価プラットフォーム
- 第三者によるセキュリティ評価プラットフォーム「Assured」での調査対応も可能です。（別途 Assured のご契約が必要です。）  
  詳しい調査の依頼は「[Assured](https://assured.jp/)」にお問い合わせください。
    - セキュリティ評価 96.6 / 100 (全体の上位5%) ※開発系サービスとしてはトップクラスのセキュリティ対策ができています。
    - [セキュリティ評価のスコアはどのように算出されますか](https://help.assured.jp/ja/articles/5233826-%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E8%A9%95%E4%BE%A1%E3%81%AE%E3%82%B9%E3%82%B3%E3%82%A2%E3%81%AF%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E7%AE%97%E5%87%BA%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%81%8B)

## 資料
- [インフラに関するドキュメント](https://kuroco.app/files/sheets/ja/kuroco_infrastructure.pdf)
- [SLA](https://kuroco.app/files/sheets/ja/kuroco_sla.pdf)

## 関連FAQ
- [脆弱性診断・検査に関して教えてください](/ja/docs/faq/what-vulnerability-diagnostic-and-assessment-services-do-you-provide/)
- [脆弱性検査のエビデンスを提供してもらうことはできますか？](/ja/docs/faq/can-you-send-me-your-vulnerability-assessment-findings/)
- [脆弱性診断で指摘を受けたのでどうすればいいか教えてください](/ja/docs/faq/my-site-was-diagnosed-with-a-security-vulnerability/)
- [セキュリティチェックシートへの記入をお願いできますか？](/ja/docs/faq/can-you-audit-my-security-checklist/)

## 関連ドキュメント
- [災害対策（DR）](/ja/docs/about/disaster-recovery/)
- [API セキュリティ](/ja/docs/management/api-security/)
- [VAddy](/ja/docs/management/vaddy/)
- [VAddyと連携してAPIエンドポイントに対する自動診断を設定する。](/ja/docs/tutorials/integrating-with-vaddy/)
- [脆弱性診断・検査に関して教えてください](/ja/docs/faq/what-vulnerability-diagnostic-and-assessment-services-do-you-provide/)
- [セキュリティチェックシートへの記入をお願いできますか？](/ja/docs/faq/can-you-audit-my-security-checklist/)


---

# 関連サービスに関するご契約

> 元ページ: `about/service_request` ｜ 公式ページ: https://kuroco.app/ja/docs/about/service_request/
> 概要: Kurocoのご利用はオンライン上の申し込み画面で完結しますが、これに付随して有償サポートや優先実装などをご依頼いただく場合には、弊社との契約が必要となります。本ドキュメントでは、その際のご案内をまとめています。

Kurocoのご利用はオンライン上の申し込み画面で完結しますが、これに付随して[有償サポート](/ja/docs/about/paid-support/)や[優先実装](/ja/docs/about/paid-support/#7-優先実装依頼)などをご依頼いただく場合には、弊社との契約が必要となります。  
以下に、そのご案内をまとめます。

:::info
関連サービスのご依頼が無い場合は本ドキュメントの対応は不要です。
:::

## 1. Kuroco利用料の請求書払いをご希望の場合

Kuroco利用料は標準ではクレジットカードでのお支払いとなっていますが、日本国内の法人については請求書払いにも対応しております。請求書払いをご希望の場合は、**専用の申込書**を提出いただく必要があります。  
ご希望の場合は、担当者までご連絡ください。

## 2. Kuroco利用料の定額制プランをご希望の場合

Kuroco利用料は基本的に従量制となっておりますが、個別に貴社の利用方法等をお伺いし、**定額制プラン**をご提案可能です。担当者が**見積書兼発注書**を作成させていただきます。  

見積書兼発注書の内容で合意いただける場合には、**発注書の提出**をお願いいたします。

## 3. 有償サポート契約をご希望の場合（お見積りが不要なプラン）

テクニカルサポート、スタンダードサポート、運用サポートをご希望の場合、**サポート申込書**を提出いただく必要があります。  
ご希望の場合には担当者までご連絡ください。  

※ プレミアムサポート等をご希望で、別途**見積書兼発注書**が発行される場合はサポート申込書は不要です。

解約時は解約希望日の3営業日前までに、ご利用のSlackチャンネルまたはメールにてご連絡ください。

## 4. 有償サポート契約をご希望の場合（お見積りが必要なプラン）

プレミアムサポート(開発・構築作業なども含むプラン)や、優先実装依頼を発注いただく場合、
ご希望内容をヒアリング後、担当者が**見積書兼発注書**を作成いたします。  
合意いただけた場合、**発注書の提出**をお願いいたします。

あわせて以下契約書への合意が必要です。

- [開発業務委託基本契約書](https://kuroco.app/files/sheets/ja/template_basic_contract.docx)
- [業務委託個別契約書](https://kuroco.app/files/sheets/ja/template_individual_contract.docx)（発注内容に応じて）

## 5. 秘密保持契約（NDA）締結をご希望の場合

弊社雛形での締結をお考えの場合は、以下をご確認ください。

- [秘密保持契約書](https://kuroco.app/files/sheets/ja/template_nda.docx)

受け入れ可能な場合はそのまま**電子契約**が可能です。調整が必要な場合は担当者までご連絡ください。

貴社雛形での締結をご希望の場合は、担当者あてに貴社雛形をご共有ください。弊社で内容の確認後、問題がなければ電子契約に進みます。

## 6. 他社へ契約を移管したい場合

他社様へ契約を移管される場合は、地位継承の覚書をご提出いただく必要があります。

- [地位継承の覚書](https://kuroco.app/files/sheets/ja/memorandum_of_succession.docx)

覚書の締結後、弊社にてアカウント設定の「メールアドレス」「会社名」「名前」を更新いたします。
**メンバー情報の更新、クレジットカード情報の更新、ご利用中のAPIキーなどの更新は、お客様側で実施をお願いいたします。**

なお、クレジットカード情報の削除をご希望の場合は、弊社にて実施しますのでサポートまでご連絡ください。  
※夜間に実行されるバッチ処理において、決済情報の登録がなく無料枠を超えたサイトはメンテナンスモードへ切り替わります。削除作業を行った当日中に、必ずクレジットカード情報の再登録をお願いいたします。

## 7. 契約方法

弊社は、**弁護士ドットコム株式会社**が提供する「[クラウドサイン](https://www.cloudsign.jp/)」による電子契約を採用しています。

クラウドサインの利用が可能な場合、以下の貴社 承認者情報を担当者までご連絡ください。

- 部署・役職
- 氏名
- メールアドレス

クラウドサイン以外の電子契約サービスを利用する場合、貴社からの契約書送付をお願いしております。  
ご利用の電子契約サービス名と利用方法を担当者までご連絡ください。

電子契約サービスがご利用いただけない場合は、その旨を担当者までご連絡ください。
書面によるご契約で対応する際は、原則として契約書類への法人印の押印をお願いしております。

## 関連ドキュメント
- [有償サポート](/ja/docs/about/paid-support/)
- [サポート](/ja/docs/about/support/)
- [請求情報](/ja/docs/management/site-payment/)
- [Kuroco利用料の支払方法を教えてください](/ja/docs/faq/how-do-i-pay-the-kuroco-fee/)
- [契約者・管理者の情報を変更したいです。手続きを教えてください。](/ja/docs/faq/i-need-to-change-contractor-or-admin-details-how-do-i-proceed/)


---

# サポート

> 元ページ: `about/support` ｜ 公式ページ: https://kuroco.app/ja/docs/about/support/
> 概要: Kurocoのサポート体制について。Kurocoドキュメント、Slackコミュニティー、お問合せ先のご連絡。有償サポートも受け付けております。

Kurocoのサポートの対応内容・対応時間は次のとおりです。
## サポートの種類
### 1. Kurocoドキュメント
KurocoドキュメントではKurocoの利用方法やよくある質問をまとめています。<br/>困った時はまずこちらをご覧ください。

<a href="/ja/docs/" className="button button--primary px-5 py-3">Kurocoドキュメントを見る</a>

### 2. Slackコミュニティ
Slackを利用し、Kurocoの利用方法やご相談などに対応するオンラインコミュニティを開設しています。  
Kurocoの開発者も参加しておりますので、お急ぎの場合はこちらでご質問ください。  
ただし、参加者全員読むことができますので、記載内容にはご注意ください。  

<a href="https://join.slack.com/t/kurocojp/shared_invite/zt-200pbif9t-A9QsdGsjZ9UAP9n8Xq~XOw" className="button button--primary px-5 py-3">Slackに参加する</a>

### 3. 問合せフォーム
ドキュメントサイトを検索しても問題が解決しなかった場合は、問い合わせフォームからお問い合わせください。

<a href="https://kuroco.zendesk.com/" className="button button--primary px-5 py-3">フォームから問い合わせをする</a>

## サポート対応時間

<table>
  <tbody>
    <tr>
      <th>営業時間</th>
      <td>平日の11時00分〜18時30分</td>
    </tr>
    <tr>
      <th>休業日</th>
      <td>土日祝日および以下に定める弊社休業日</td>
    </tr>
    <tr>
      <th>弊社休業日</th>
      <td>1月27日(創立記念日)、12月28日～1月4日(年末年始休業)</td>
    </tr>
  </tbody>
</table>

営業時間内でお問い合わせを拝見し、順次対応します。  
弊社は『[当社従業員の祝日の自由振替制度導入について](https://www.diverta.co.jp/topics/detail/id=235)』にて記載しておりますような働き方になっておりますので、祝日や営業時間外でも返信する場合があります。  

## お問い合わせ時の注意点
- サポート業務はチーム制で行っております。  
問い合わせ内容を共有し迅速に対応するためにサポート管理サービス「Zendesk」を利用いたしますのでご了承ください。
- 営業時間外にご連絡を頂いた場合は翌営業日以降に対応いたします。
- 緊急の対応が必要な場合は営業時間外でも対応できる場合があります。お問い合わせ時にその旨ご連絡ください。
- お問合せを頂いてから1営業日以内を目安に返信するように心がけておりますが、内容やサポートセンターの混雑状況によって回答時間は前後することがございます。
- 電話やWEB会議などでのお問い合わせは受け付けておりません。  
WEB会議などでのサポートが必要な場合は、[プレミアムサポート](/ja/docs/about/paid-support#プレミアムサポート)のお申し込みをお願いしております。

## サポートの範囲
### 無償サポートと有償サポートのメニューについて

<table>
  <tbody>
    <tr>
      <th>無償サポート</th>
      <td>
        <ul className="mb-0">
          <li>Kurocoの基本的な操作方法</li>
          <li>製品仕様についての情報</li>
          <li>バグ修正</li>
          <li>営業サポート</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>有償サポート</th>
      <td>
        <ul className="mb-0">
          <li>フロントエンドに関する問い合わせ</li>
          <li>HTML、CSS、または Smarty コードに関する問い合わせ</li>
          <li>汎用技術のサポート</li>
          <li>サイト固有の問題の解決</li>
          <li>サイトの構成と問題の調査</li>
          <li>サイト構築のサポート</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

無償サポートであってもKurocoに関することであれば何でもご質問いただいて構いません。  
サポートからの回答は、お問い合わせ内容によってはお時間をいただくものや、参考になる記事リンクやGoogleで検索いただくとよさそうなキーワードをお知らせするような回答になる場合もございます。  
従量課金の見積もり方法が分からない場合なども遠慮なくご質問ください。これまでの経験等から目安をご提示できる場合もございます。  

また、Kurocoを利用した開発時にご利用いただけるプレミアムサポートやテクニカルサポート、優先実装依頼などもメニューとして用意しております。  
有償サポートの場合は、開発するソースコード等へのアドバイスや管理画面の操作を実際にしてご確認いただいたり、フロントエンド開発も含めてのサポートなどが可能になっております。  

詳しくは[有償サポート](/ja/docs/about/paid-support/)をご確認ください。  

## 営業サポートについて
- Kurocoを利用した構築をクライアントに提案する際、弊社が見積りや提案のサポートをいたします。
- 弊社は原則として提案書の作成や企画はおこないません。お客様が主体となって提案活動を進めていただきます。
- 弊社が見積りを行うために、見積りに必要な前提条件をご提示いただく必要があります。  
- 見積りの前提とした条件が変更された場合、見積り金額が変わる可能性があることをご理解ください。
- 見積り作成には最低でも数営業日（構築対象の規模や弊社のリソース状況により変わります）を要するため、対応可能なスケジュールでご依頼ください。

## 不具合等の調査依頼について 
弊社側で、問題の起きている現象の再現ができない場合は調査することが難しいため、お問い合わせの際には下記２点を[弊社サポート](https://kuroco.zendesk.com/)までご連絡ください。  

- 現象を確認できる画面のURL
- 現象を再現するための手順

:::note
- 弊社側で問題の現象確認が出来ない場合は、調査できない可能性があるため、再現手順はできるだけ詳しくご連絡ください。
- キャプチャやHARファイルなどに個人情報が含まれる場合はお客様側でマスクして送付ください。
:::

## 関連ドキュメント
- [有償サポート](/ja/docs/about/paid-support/)
- [よくあるお問い合わせ](/ja/docs/troubleshooting/before-sending-your-inquiry/)
- [お問い合わせのしおり](/ja/docs/troubleshooting/contact-guidelines/)
- [問い合わせ先のslackとフォームの違いを教えてください](/ja/docs/faq/what-is-the-difference-in-usage-between-slack-and-contact-form-inquiries/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)


---

# ヘッドレスCMSとは？国産の開発者が語る背景、メリット、デメリット、従来のCMSとの比較まで

> 元ページ: `about/what-is-a-headless-cms` ｜ 公式ページ: https://kuroco.app/ja/docs/about/what-is-a-headless-cms/
> 概要: ヘッドレスCMSはAPIファーストで設計されているバックエンド型のCMSのことです。従来のCMSにあるようなUI管理機能がない代わりに大きな柔軟性を獲得しています。なぜ、このようなCMSが登場してきたのか背景からご説明いたします。

KurocoはAPIファーストで設計されているヘッドレスCMSです。このページでは、業界20年以上の経験を活かしてヘッドレスCMSの背景からメリット、デメリットまでご説明いたします。

## ヘッドレスCMSとは

ヘッドレスCMSとは、従来のCMSでは存在していた「ヘッド(表示画面)」部分が分離されたバックエンドを扱うAPIベースのCMSのことです。  
2016年頃には既に概念としては提唱され始めており当時は管理画面も「ヘッド」に該当するので、APIのみが提供されているものもありましたが、現在はほとんどのヘッドレスCMSが管理画面を持つようになっております。

![ヘッドレスCMS](/files/user/img/about/headless_overview.png)

## ヘッドレスの語源は？

ところで、表示画面がないことをヘッドレスと言うのでしょうか？
諸説ありますが、パソコンのディスプレイが下記のように大きな時代にパソコンメーカーがディスプレイなしパソコンを「ヘッドレス・コンピュータ」として売り出したことから、表示部分の機能がないことを「ヘッドレス」と呼ぶようになったと言われています。パソコンのディスプレイが頭のように見えたのでしょうね。

![CRTモニタの画像](/files/user/img/about/headless_crt.jpg)
*Marcela (talk) - 投稿者自身による著作物, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=5445374 による*

## 一番有名なのはContentful

ヘッドレスCMSとして一番有名な<a href="https://www.contentful.com/" target="_blank">Contentful</a>は2013年に創業されており、一時は3000億円近い時価総額で評価されるなどWEBコンテンツの管理システムとして次世代を担う仕組みとして注目されております。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/28806489ae1916bdf30b7cad8361fb64.png)
日本では、2020年頃から注目されだして、2021年頃から急激に注目が集まっています。国産のヘッドレスCMSであるmicroCMSも2021年9月に資金調達するなど注目の集まっているサービスになっています。  
<a href="https://prtimes.jp/main/html/rd/p/000000007.000062982.html" target="_blank">ヘッドレスCMSを運営する『株式会社microCMS』がZ Venture Capitalより資金調達を実施</a>

また、エンタープライズ向けのヘッドレスCMSであるKurocoも2021年4月に正式版をリリースいたしました。

<a href="https://prtimes.jp/main/html/rd/p/000000010.000031546.html" target="_blank">完全従量課金制！DX担当者に向けて、ソフトウェア資産を1ヶ月でWEBサービスに変身させるAPI中心設計の次世代CMS「Kuroco｜クロコ」を正式リリース</a>

その後、続々と国産のヘッドレスCMSがリリースをされていました。

## ヘッドレスCMSが登場した背景について

### 2000年から2010年頃

2000年頃から急速にブログが普及し始めます。<a href="https://www.movabletype.com/" target="_blank">MovableType</a>や<a href="https://www.blogger.com/" target="_blank">Blogger</a>などが有名でした。
この頃から企業もホームページを持つのことが当たり前の時代になります。しかし、大手企業などがホームページを作ると構築費だけで1億円以上かかることもよくありました。

しかし、ホームページ管理者からは「もっと手軽に更新をしたい」「ブログみたいに更新したい」という要望が寄せられるようになります。
そこで、流行っていたブログシステムを企業システムの更新システムとして利用する流れになります。ちょうど<a href="https://wordpress.com/"  target="_blank">WordPress</a>がオープンソースで使いやすいブログシステムとしてリリースされていました。  

このような流れでWordPressが爆発的にホームページの更新システムとして採用されていきます。プラグインなども充実していき現在の地位を築きました。

### 2011年から2018年頃

2007年にはiPhoneが発売され、2013年にはiPhone5がリリースされます。この頃には情報をインターネットで探すことが当たり前の時代になります。ホームページも紙芝居のように単純な情報を掲示するだけではなく、インタラクティブな機能や使いやすいUI、スマートフォンとPC、フィーチャーフォンの表示の切り替え、SEO、マーケティング、分析など様々な機能が必要になります。

また、2010年にはページスピードが検索順位決定のアルゴリズムの要素になるとGoogleが発表し、その後さらにその重要度も上がり、2018年にはモバイルファーストインデックスも開始されます。

WEBサイトは複雑化しているにも関わらず、さらに表示速度が重要視される状況になります。

日本国内だと意識されづらいのですが、WEBサイトがグローバルで利用されるようになっている中で表示速度に大事なCDNとWordPressなどの従来型のCMSの相性が良くありませんでした。

また、スマートフォンアプリやIoTなど様々なデバイスがインターネット接続されるようになりました。スマートフォンは回線速度が安定しない問題もあります。

そんな中でブラウザ側のJavaScriptで軽快に動作するReact/VueJS/AngularなどのJavaScriptフレームワークが登場します。  

2010年にはCloudflare創業、2011年Fastly創業、2013年にはContentful創業、Reactリリースなど現在のJAMStackの中心プレイヤーたちが続々と登場します。

そして、JAMStack（JavaScript/API/Markupを利用した構成）の提唱者Mathias BiilmannのいるNetlifyが2014年に創業します。

このJAMStackのAPI（Application Programming Interface）部分の機能を提供するCMSが「ヘッドレスCMS」になります。

また、1999年創業のSalesforceのSaaS（ソフトウェア・アズ・サービス）という考え方や2006年に提供が開始されたAmazon Web Servicesのクラウドシステムの考え方も世の中に浸透しました。

そうなると、従来のようにレンタルサーバを借りて、毎回ソフトウェアのインストールをして、設定をして、開発をして、運用やチューニングもしてという手間もコストも時間もかかる方法ではなく、クラウド（SaaS）にあるサービスを利用した方が便利で安くて早いということになります。

このようにCMSもクラウドCMSが主流になりました。

### 2018年から現在

WEBアプリケーションが単なる情報提供システムではなく、業務も含めたあらゆるアプリケーションとしてクラウド（SaaS）として当たり前に運用されるような時代になると、今度は提供されているアプリケーションに必要な機能が足りない・他のシステムと連携させたい・カスタマイズがしたいという要望がでてきます。
また、JavaScriptフレームワークやアプリから必要な情報だけ取得だけするシステムが欲しいという要望も出てきます。

ここでまた登場するのがAPIです。APIの考え方は50年以上前から存在しますが、WEB上に当たり前のように公開され始めるのがこの頃になります。

JAMStackのAPI部分は当初は単なるデータの提供場所のような想定がされていましたが、現在は決済や認証、データベース、フォームなど様々なデータのやり取りを想定されるようになっています。

弊社で提供しているKurocoはエンタープライズ向けを標榜しており、一般的なヘッドレスCMSよりも機能が豊富でデータ量が多い、カスタマイズ要件がある場合などに適しているヘッドレスCMSとなっております。コンテンツ管理以外にも様々なAPIを提供しております。

### 背景についてまとめ、そして将来

このように、様々な要因や進化の過程を経てクラウドのヘッドレスCMSが利用される時代になってきました。このJAMStackやヘッドレスCMS、JavaScriptフレームワークを利用した開発手法はまだ進化を続けており、今後、10年でどのような変遷を辿るのかは予想が難しい状況です。

個人的にはヘッドレスCMSは従来型CMS（UI部分も一体的に管理するCMS）に完全に置き換わる存在ではないと考えております。これまでの流れの中で<a href="https://www.wix.com/" target="_blank">Wix</a>や<a href="https://www.squarespace.com/" target="_blank">Squarespace</a>、<a href="https://studio.design/" target="_blank">STUDIO</a>などのローコードWEB制作ツールなども台頭してきており、従来型CMSで対応してきていた様々なニーズは細分化されて様々なサービスに置き換わっていくと考えております。

直近の動きとして、UI/UXに関わる動作はユーザーの手元の各デバイス上（フロントエンド）で処理をして、コンテンツやデータに関する処理はサーバ側（バックエンド）で処理をするという2層での処理をする考え方が主流でしたが、クラウド・エッジの近年の進化によりエッジという層が増えて3層で構成をするような考え方に変わってきています。

クラウド・エッジは、ユーザーの手元ではないがユーザーに限りなく近い場所に小さなサーバを配置して処理をさせることができます。
ユーザーの端末とサーバの距離の問題でユーザー端末のJavaScriptで無理に実行していた処理などがクラウド・エッジ側に移ってきています。

データベースやキー・バリューストアなど様々な機能もエッジで動作するようになっています。Next.jsの開発元であるVercelは、<a href="https://vercel.com/blog/framework-defined-infrastructure" target="_blank">Framework-defined infrastructure</a>を標榜しており、様々なクラウドサービスをフレームワーク側がシームレスに構築・接続できるようにするということを目指しているようです。

どのような進化をしていくか楽しみですね！


**UI/UXとCMSが密接に繋がっていることでUI/UXの改善スピードが下がる**  
![UI/UXとCMSが密結合](/files/user/img/about/2-01.png)

**UI/UXとCMSがAPIで分離されることにより、UI/UXの改善スピードが劇的に改善する**
![UI/UXとCMSが密結合](/files/user/img/about/2-02.png)

**人間中心設計(HCD)の推進もこのUI/UXの改善スピードが重要**
![人間中心設計(HCD)の推進](/files/user/img/about/2-03.jpg)

こうしてヘッドレスCMSは時代の要求に沿った製品として様々なサイトに採用されています。  
また、従来のCMSもこの流れをキャッチアップするようにAPI機能の実装を進めています。  

Kurocoは従来型のCMSでしたが、従来型のCMSのまま単純にAPIの追加対応をしていると、お客様に中途半端な価値しか提供できないと考え、大幅な改修を実施して全く新しいヘッドレスCMSとして誕生いたしました。

## ヘッドレスCMSにはどのような種類があるのでしょうか？

続々とリリースがされているヘッドレスCMSですが、どのような種類があるのでしょうか？  
大きく分けて提供方法とAPIの種類、持っている機能、出自で分類できます。

| 代表的な製品  | 提供方法 | API形式 | 持っている機能 | 出自 |
| ----------- | --------------- | ------------ | ------------ | ------------ |
| <a href="https://kuroco.app/ja/">Kuroco</a> | パブリックSaaS・プライベートSaaS | RESTful |  コンテンツ管理<br/>+APIマネージメント <br/>+パーソナライズなど様々な機能 | 従来のCMSをヘッドレスCMSに転換 |
| <a href="https://strapi.io/" target="_blank">Strapi</a> | オープンソース・クラウドのハイブリッド | RESTful or GraphQL |  コンテンツ管理がメイン | 最初からヘッドレスCMS |
| <a href="https://www.contentful.com/" target="_blank">Contentful</a> <a href="https://microcms.io/" target="_blank">microCMS</a>  | クラウド | RESTful(GraphQL) |  コンテンツ管理がメイン | 最初からヘッドレスCMS |
| <a href="https://wordpress.com/ja/" target="_blank">Wordpress</a> <a href="https://www.drupal.org/" target="_blank">Drupal</a>  | オープンソース・クラウドのハイブリッド | RESTful |  コンテンツ管理<br/>+パーソナライズなど様々な機能 | 従来のCMSにAPI機能を付与 |
| <a href="https://business.adobe.com/jp/products/experience-manager/sites/aem-sites.html" target="_blank">Adobe</a> <a href="https://www.sitecore.com/ja-jp/products/sitecore-experience-platform" target="_blank">Sitecore</a>  | 商用サーバインストール | RESTful |  コンテンツ管理<br/>+パーソナライズなど様々な機能 | 従来のCMSにAPI機能を付与 |

Kurocoは、4000社以上の実績と15年以上の歴史を持つ<a href="https://www.r-cms.jp/" target="_blank">RCMS</a>をヘッドレスCMSとして完全に作り替えた製品になっており、後発ながら他社を上回る機能を保持しています。  
WordpressやDrupalのような昔からあるCMSもAPIベースのインターフェースを用意しており、ヘッドレスCMSとしても充分に動作するサービスになっています。  
また、商用のエンタープライズCMSもAPIを用意してヘッドレスCMSとしての用途をカバーするような機能追加がされております。  
コンテンツ管理のみを考慮する場合は、最初からヘッドレスCMSとして開発されているサービスの方がUIなどが使いやすいというメリットがあります。しかし、コンテンツ管理以外のニーズに対して対応する必要がある場合には、コンテンツ管理以外の機能を持っている製品も検討するとよいです。

では、次からそれぞれの細かい違いに関して比較していきましょう。

## ヘッドレスCMSのメリット・デメリット

ここでは一般的なコンテンツ管理がメインのヘッドレスCMSとしてメリット・デメリットを挙げてきます。

### ヘッドレスCMSのメリット
主にフロントエンド機能を持っておらず、API機能が充実している点や開発が最近なので、近年のニーズを汲んでいることポイントになっています。

#### 堅牢なセキュリティ
主な外部との接続がAPI部分に限定されるので、セキュリティが担保されやすくなり、セキュリティも高くなります。

#### 高いパフォーマンス性能
CDNが標準で装備されているサービスが多く、APIのレスポンスも高速になっておりパフォーマンスを出しやすい構成になっている。

#### ベンダーロックインからの開放
APIベースで接続されているので、仮にヘッドレスCMSを入れ替えたい場合にはAPI部分を主に考慮すればよく、リニューアルなどの時に全て作り直すような事態にはならない。また、部分的にヘッドレスCMSを利用可能なので、サービスを併用して段階的に切り替えていくようなこともできる。

#### 自由なデザインやUI/UX
ヘッドレスCMSでは、表示とコンテンツ管理が切り離された構成となるので、表示側はCMSの制限を受けることなく自由に制作することが可能になります。
また、フロントエンド部分のみ技術刷新することも容易です。

#### 様々なプラットフォームへの展開
ヘッドレスCMSのコンテンツは、APIを介して様々なプラットフォームで表示できます。
そのため、デバイス間での互換が容易になります。例えば、Webサイトで利用していたコンテンツを、スマートフォンアプリやサイネージなどのデバイスへの展開が容易です。

![様々なプラットフォームへの展開](/files/user/img/about/6-01.png)

#### 開発者間の同時コラボレーション
フロントエンドとバックエンドが分離されているので、タスクの同時並行が可能になります。


### ヘッドレスCMSのデメリット

主に技術の新しさによるノウハウの不足などがデメリットになりやすく、従来型のCMSと上手に使い分ける必要があります。
ただし、これは各CMS独自のものではなく、グローバルで利用できる学習内容になるので是非、新しい仕組みに挑戦いただきたいです。

Kurocoではこれらのデメリットを解消するために技術サポートを積極的に行っております。詳しくは<a href="/ja/docs/about/support/">サポート</a>をご覧ください。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/a84fe70d56379568780610417da06fa7.png)
#### システムが分散されるので相互の接続などで慣れが必要

まず、フロントエンドとバックエンドが分離されていますので、この相互の通信に関しての技術的な知見が必要になります。

#### フロントエンド側でプログラムをする必要がある

バックエンドで行っていたプログラムがフロントエンドに移動してきたと言えますが、従来型のCMSに慣れているエンジニアは新しい言語を覚える必要があります。これにより学習コストがかかることになります。

#### 車輪の再発明になってしまうことがある

従来型のCMSはそれなりの歴史を持っており便利な機能が様々あります。ヘッドレスCMSは比較的に新しいこともあり細かい機能が揃っておらず、フロントエンド側で機能の実装をしないといけないことも多い場合があるようです。

Kurocoは従来型のCMSの良さも引き継いでいます。例えば、ページャー機能や前後のページ機能などは容易にAPI側の設定で実装できる機能が用意されています。

:::tip
Q. どんなサイトでもヘッドレスCMSを利用した方がいいですか？  
A. いいえ。ヘッドレスCMSには多くのメリットがありますが、そのメリットを充分に発揮できないタイプのサイトもあります。
しっかり比較検討をして選択をするようにしましょう。  
従来型のCMSとヘッドレスCMSの両者を知っている開発者としてフェアな観点で一緒に比較検討させていただきますので、是非サポートまでご連絡ください。  
<a href="https://kuroco.zendesk.com/hc/ja/requests/new?ticket_form_id=900002698263">お問い合わせ</a>
:::

## 関連ドキュメント
- [Kurocoについて](/ja/docs/about/about-kuroco/)
- [Jamstackについて](/ja/docs/about/jamstack/)
- [Jamstackと一般的なWebサイトの違い](/ja/docs/about/jamstack-website/)
- [Jamstackの利点と欠点](/ja/docs/about/why-jamstack/)
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)


---

# Jamstackの利点と欠点

> 元ページ: `about/why-jamstack` ｜ 公式ページ: https://kuroco.app/ja/docs/about/why-jamstack/
> 概要: JamstackによるWebサイト実装に関する利点および欠点を、「セキュリティ」「スケール」「パフォーマンス」等の観点から解説します。

ここではJamstackによるWebサイト実装に関する利点および欠点について解説します。

## 利点

Jamstackの利点を以下のポイントごとにまとめます。

- セキュリティ
- スケール
- パフォーマンス
- メンテナンス性
- 可搬性
- DX（開発者体験）

### セキュリティ

JamstackではWebアプリケーションによる動的なコンテンツ生成をなくし、静的ファイルとしてホスティングを行っています。そのため、悪意を持った訪問者からの攻撃に強くなっています。たとえばSQLインジェクションのような攻撃は意味がありません。Jamstackの構成の場合、悪意を持った攻撃対策は主にAPIに対して考慮をすることになります。

WebサーバーやCDNから配信するコンテンツはあらかじめ生成されたもの（プリレンダリング）されたものであり、読み取り専用になります。動的コンテンツは外部の信頼できるサービスベンダーのものを利用することで、信頼性を高められます。

### スケール

Jamstackを実現する多くのフレームワークやホスティングサービスではCDNを通じたキャッシュ機構を備えています。キャッシュの有効期限や仕組みについては、各サービスによって違いがありますので構築するサイトの特性に合わせて選択をするとよいでしょう。

CDNを介して配信することで高い信頼性、高速配信そして負荷分散が実現します。

### パフォーマンス

ページの読み込み速度はユーザー体験やコンバージョンに直結します。Jamstackではリクエストごとにページ生成する必要がなく、あらかじめ生成されたコンテンツを配信するだけです。しかもCDNを通じて配信されるので高速です。

多くのCDNはリクエスト元の近くに配信サーバーを配備し、より高速な配信がされるようになっています。高価かつ複雑なインフラを導入することなく、非常に高いパフォーマンスを実現できます。

### メンテナンス性

ホスティングの複雑さが軽減されると、Webサイトのメンテナンス作業も軽減されます。あらかじめ生成されたコンテンツが静的ホスティングシステム、またはCDNから配信されるという仕組みであれば、サーバー管理者が常時監視する必要性は低いでしょう。

必要な作業はデプロイ時に完了しており、稼働したWebサイトは非常に安定していることでしょう。サーバーのメンテナンスが不要になれば、サーバーにパッチを当てたり、アップデート作業などから解放されます。

### 可搬性

Jamstackで構築されたWebサイトは最終的に静的なHTMLを生成します。つまりホスティングサービスを選びません。すでに多くの静的ホスティングサービスが存在し、自由に選択できます。Jamstackならばベンダーロックインから解放されるのです。

### DX（開発者体験）

Jamstackを提供するフレームワークは多種多様に存在します。オープンソースのものも多く、商用ソフトウェアに依存することはありません。多くはすでに知られているツールを組み合わせることで、広く知られている手法を利用できます。

その結果として、Jamstackを構築できるスキルを持った開発者を見つけるのは難しくありません。開発者としても一度覚えたJamstackのスキルは他のプロジェクトでも応用可能なものになります。

### コスト

CMSなどを用いてWebサイトを運営する場合、Webサーバーとアプリケーションサーバー、データベースサーバーなどで3台以上の構成になるケースが多いでしょう。バックアップや複数台構成になれば、さらに台数は増えます。そして台数分、運用コストが増えていきます。

Jamstackの場合、静的ホスティングサービスやCDN、動的コンテンツ配信サービスを利用するコストは圧倒的に安価になるはずです。

### SEO

Googleはページ速度を重視したランキングを行っています。2021年6月からはCore Web Vitalsもランキング指標になります。Jamstackの高速度なコンテンツ配信はSEOにとって効果的です。動的部分についてはSEO上、不利になることもありますが、GoogleはJavaScriptについても解釈できるようになっているのでさほど問題にはならないでしょう。

## 欠点

### 前提となる技術スタックがある

Jamstackを実現させるための技術スタックとして、JavaScriptと静的サイトジェネレータおよびAPI、CDNなどの知識が必要になります。これらの技術を知らない開発者は、必ず習得しなければなりません。

とはいえ、静的サイトジェネレータを除けば、他の技術は一般的なWebサイトやWebアプリケーションを構築する際にも必要な技術になります。また、習得は決して難しくありません。

### ビルドに時間がかかる

Jamstackではデプロイ時に静的HTMLを生成（プリレンダリング）します。つまりコンテンツが大量にあると、ビルドに時間を要するようになります。数ページであれば気にしないでしょうが、数万ページになると数十分かかるようになるかも知れません。

例えば静的サイトジェネレータのGatsbyでは変更されたページだけを生成し直すIncremental buildsという機能があります。これによってビルド時間の短縮が可能です。このように静的サイトジェネレータを選定することで解決できる問題になるでしょう。

### サイト修正の工数

動的サイトを提供するCMSの場合、管理画面で文言やコンテンツの作成ができるでしょう。開発者ではない運用担当者がちょっと並び替えを行ったり、文言修正できます。しかしJamstackの場合はテンプレートを修正してデプロイし直す必要があるかも知れません。

開発者の工数を減らす場合には、運用担当者が修正する部分を動的コンテンツにする必要があります。静的な部分と動的な部分とを見極め、運用担当者の運用負荷を減らす工夫が必要でしょう。

## 関連ドキュメント
- [Jamstackについて](/ja/docs/about/jamstack/)
- [Jamstackと一般的なWebサイトの違い](/ja/docs/about/jamstack-website/)
- [Jamstackのアーキテクチャパターン](/ja/docs/about/jamstack-architecture/)
- [Jamstackを学ぶためのリソース](/ja/docs/about/jamstack-resources/)
