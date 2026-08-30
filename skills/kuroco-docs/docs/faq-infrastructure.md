# Kurocoドキュメント: FAQ / infrastructure

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- オンプレミス版の提供はありますか？（`a-on-premises-version-availability`）
- Kurocoサービスのサーバーは冗長化されていますか？（`are_the_kuroco_service_redundant`）
- KurocoでWAFを利用できますか？（`can-i-use-wafs-with-kuroco`）
- アップデートのスケジュールを教えてください（`what-is-your-update-schedule-like`）


---

# オンプレミス版の提供はありますか？

> 元ページ: `faq/a-on-premises-version-availability` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/a-on-premises-version-availability/
> 概要: AWSのご利用を前提とした、ISMAP対応のプライベートSaaS版での構築プランを準備しております。

AWSのご利用を前提とした、ISMAP対応のプライベートSaaS版での構築プランを準備しております。  
ご希望の場合は以下からお問い合わせください。

:::info info
- [フォームから問い合わせする](https://kuroco.zendesk.com/hc/ja/requests/new?ticket_form_id=900002698263)
:::

## ISMAP対応プライベートSaaS版
- AWSにお客様専用サブアカウントでプライベート環境を構築し、Kurocoをインストールします。
- AWSでは、Fargate / Aurora / EFS / ElastiCache / S3 等を利用してマルチAZでの構築になります。
- マルチリージョン対応や特定のセキュリティサービスの導入等は別途、お見積もりになります。
- インストール作業は一部の設定をダッシュボードで設定後、基本的にCDKを利用して構築を行います。
- ライセンスは年間契約となります。
- FastlyはISMAPに対応していませんが、CDNであるため、ISMAP対応のサービスを構築する場合でも、基本的にはセキュリティ上に問題はありません。  
  ただし、申請が別途必要な場合があります。  
- Fastlyが利用できない場合、キャッシュ機能や画像最適化等に制限があります。  
  ※Cloudfrontで代替する開発を進めております。  
- BigQueryに依存しているログ検索画面が利用できません。CloudWatchでCLI等で確認することになります。  
  ※CloudWatchでも動作するログ検索画面の開発を進めております。  

### Managed - インフラ部分を弊社で提供する場合
弊社のAWSアカウント内のお客様専用のサブアカウントでプライベート環境を構築し、Kurocoをインストールします。

- **Fastlyが利用できる場合：**
  - 保守費用(ラインセンスを含む)：47.3万円/月〜（利用ドメイン数でお見積り）  
  - インストール費用：保守費用に含まれる  
  - 従量課金利用料：パブリックSaaS版と同じ ※定額契約がお勧めです  
  - パブリックSaaS版と比べた場合の制約事項：BigQueryに依存しているログ検索画面が利用不可
　　
- **Fastlyが利用できない場合：**
  - 保守費用(ラインセンスを含む)：47.3万円/月〜（利用ドメイン数でお見積り）  
  - インストール費用：保守費用に含まれる  
  - 従量課金利用料：パブリックSaaS版と同じ ※定額契約がお勧めです  
  - パブリックSaaS版と比べた場合の制約事項：BigQueryに依存しているログ検索画面が利用不可、APIのキャッシュ機能、画像最適化機能等のFastlyに依存している機能が利用不可  

### Self-Hosted(BYOC) - インフラ部分をお客様側で用意する場合
お客様がご契約のAWSアカウント内の環境（サブアカウント利用を推奨）にKurocoをインストールします。

- **Fastlyが利用できる場合：**  
  - 保守費用(ラインセンスを含む)：55万円/月〜（利用ドメイン数でお見積り）  
  - インストール費用：220万円〜（構築内容や要求事項でお見積もり）
  - 従量課金利用料：APIと転送量の課金のみ  
  - パブリックSaaS版と比べた場合の制約事項： BigQueryに依存しているログ検索画面が利用不可

- **Fastlyが利用できない場合：**
  - 保守費用(ラインセンスを含む)：55万円/月〜（利用ドメイン数でお見積り）  
  - インストール費用：220万円〜（構築内容や要求事項でお見積もり）
  - 従量課金利用料：なし  
  - パブリックSaaS版と比べた場合の制約事項：BigQueryに依存しているログ検索画面が利用不可、APIのキャッシュ機能、画像最適化機能等のFastlyに依存している機能が利用不可  

その他、詳細な要件がある場合はご相談ください。  

※上記の価格はいずれも税込になります。

## 関連ドキュメント
- [Kurocoサービスのサーバーは冗長化されていますか？](/ja/docs/faq/are_the_kuroco_service_redundant/)
- [セキュリティ](/ja/docs/about/security/)
- [どのようなときに従量課金として計上されますか](/ja/docs/about/how-much-does-kuroco-cost/)
- [サポート](/ja/docs/about/support/)


---

# Kurocoサービスのサーバーは冗長化されていますか？

> 元ページ: `faq/are_the_kuroco_service_redundant` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/are_the_kuroco_service_redundant/
> 概要: Kurocoは Google Cloudの機能を利用して冗長化されております。また、フロントエンドシステムからのAPIアクセスに関しては標準でCDNが利用されております。

Kurocoは Google Cloudの機能を利用して冗長化されております（Google Kubernetes Engine、App Engine、Cloud Functions、Cloud SQL、Memorystore、Cloud Storage、FileStore、BigQuery、Pub/Sub、Google Cloud Armor、Cloud Logging など）。  
また、フロントエンドシステムからのAPIアクセスに関しては標準でCDNが利用されております。

## 冗長化構成図
KurocoはGoogle Cloud側にてネットワーク冗長化されております。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/edae666af786ca1832ead49760cae332.jpg)

詳細はKuroco インフラパフォーマンス概要に記載がございますのでご確認ください。

## 参考
- 冗長化構成図（GCP上でのクラウドネイティブな構成）  
  「Kuroco インフラパフォーマンス概要」資料【7p】  
  https://kuroco.app/files/sheets/ja/kuroco_infrastructure.pdf

- 障害発生時の連絡フロー（障害が発生した場合の対応・復旧フロー）  
  「Kuroco インフラパフォーマンス概要」資料【11p】  
  https://kuroco.app/files/sheets/ja/kuroco_infrastructure.pdf  
    ※障害発生時は、影響度合いにより全社への通知が必要と当社が判断した場合は、メールによる一斉通知、またはサポートサイトへの告知を実施いたします。

- 問合せ先  
  [サポート](/ja/docs/about/support/)

## 関連ドキュメント
- [災害対策（DR）](/ja/docs/about/disaster-recovery/)
- [セキュリティ](/ja/docs/about/security/)
- [オンプレミス版の提供はありますか？](/ja/docs/faq/a-on-premises-version-availability/)
- [サポート](/ja/docs/about/support/)


---

# KurocoでWAFを利用できますか？

> 元ページ: `faq/can-i-use-wafs-with-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-wafs-with-kuroco/
> 概要: KurocoではGoogle Cloud Armorを標準導入しています。お客様側での対応は不要です。

KurocoではGoogle Cloud Armorを標準導入しています。お客様側での対応は不要です。

Google Cloud Armor は、DDoS 防御サービスやウェブ アプリケーション ファイアウォール（WAF）を提供する Google Cloud のサービスです。
サービス拒否攻撃やウェブ攻撃からウェブサイトやサービスを保護できるよう支援します。

 Google Cloud Armor についての詳細は下記をご確認ください。  
- [Google Cloud Armor](https://cloud.google.com/armor)
- [Cloud Armor: Adaptive Protection、対象範囲の拡大、新規ルールでエッジでのセキュリティを強化](https://cloud.google.com/blog/ja/products/identity-security/improve-your-ddos--waf-defense-with-new-cloud-armor-features)

## 関連ドキュメント
- [WAF 検出タイプ](/ja/docs/reference/waf-detection-type/)
- [セキュリティ](/ja/docs/about/security/)
- [セキュリティ対策の資料はありますか？](/ja/docs/faq/materials-on-security-measures/)


---

# アップデートのスケジュールを教えてください

> 元ページ: `faq/what-is-your-update-schedule-like` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-your-update-schedule-like/
> 概要: Kurocoのアップデートについては以下のページを参照してください。

Kurocoのアップデートについては以下のページを参照してください。
- [Kurocoのバージョン管理について](/ja/docs/update/roadmap-kuroco-version/)

## 関連ドキュメント
- [Kurocoのバージョン管理について](/ja/docs/update/roadmap-kuroco-version/)
- [Kuroco リリースロードマップ](/ja/docs/update/kuroco-roadmap/)
- [Postmanを利用した正式版反映前のリグレッションテスト](/ja/docs/tutorials/regression-testing-before-stable-version-release-using-postman/)
