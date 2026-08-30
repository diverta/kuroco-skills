# Kurocoドキュメント: リファレンス / ファイル

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- バックアップ項目一覧（`backup-data`）
- GCS, S3に設定したファイルの有効期限について（`expiration-for-files-in-gcs-and-s3`）
- ファイルマネージャーで利用できるファイルの種類（`what-file-formats-does-the-file-manager-support`）


---

# バックアップ項目一覧

> 元ページ: `reference/backup-data` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/backup-data/
> 概要: Kurocoでは、サイトのバックアップが行えます。

Kurocoでは、サイトのバックアップが行えます。 

本リファレンスでは、サイトのバックアップ項目とバックアップの種類について説明します。

## バックアップ項目一覧

バックアップには下記3種類あります。
- KurocoFiles
- データベース
- 設定

KurocoFilesには、ファイルマネージャー内のファイルが含まれます。ただし、GCSやS3ファイルはバックアップには含まれません。  

それぞれでバックアップされる内容が異なります。詳細は下記をご確認ください。

|大分類|中分類|項目|設定|データベース|
|:----|:----|:----|:---:|:---:|
|コンテンツ定義|-|コンテンツ定義|◯|◯|
|コンテンツ|-|コンテンツ|×|◯|
| | |マスタ|×|◯|
| | |タグ|◯|◯|
|API|-|API|◯|◯|
| | |エンドポイント|◯|◯|
|ファイルマネージャー|-|ファイル|×|◯|
|アクティビティ|-|アクティビティ定義|×|◯|
| | |アクティビティ|×|◯|
|チャネル|WEB|KurocoFront設定|×|◯|
| | |フォーム|◯|◯|
| | |問い合わせデータ|×|◯|
| |メール|SendGrid|×|×|
| |メッセージング|Slack|×|×|
| | |テキスト メッセージ(SMS)|×|×|
| |-|一括配信|◯|◯|
| | |配信データ|×|◯|
|メンバー管理|-|メンバー|×|◯|
| | |グループ|◯|◯|
| | |カスタムメンバーフィルター|◯|◯|
| | |期限付き一時メンバー|×|◯|
|オペレーション|-|メッセージひな形|◯|◯|
| | |ログ管理|×|△(注1)|
| | |バッチ処理|◯|◯|
| | |カスタム処理|◯|◯|
| | |承認ワークフロー|×|◯|
|EC|-|商品|×|◯|
| | |注文|×|◯|
| | |設定|×|◯|
|環境設定|-|アカウント設定|×|×|
| | |管理画面|△(注2)|◯|
| | |ローカライズ|×|◯|
| | |定数|×|×|
| | |シークレット|×|×|
| | |ダッシュボードのウィジェット|×|◯|
| | |管理画面プラグイン|◯|◯|
| | |バックアップ|×|×|
| | |サイト管理|◯|◯|
|外部システム連携|-|GitHub|×|◯|
| |ID連携|SAML IdP|◯|◯|
| | |SAML SP|◯|◯|
| | |OAuth SP|◯|◯|
| |-|Firebase|×|×|
| | |Vimeo|×|×|
| | |reCAPTCHA|◯|◯|
| | |Google Analytics|◯|◯|
| | |VAddy|◯|◯|
| | |Stripe|×|×|

注1：ログ管理の集計のみ。  
注2：
設定の際の[環境設定] -> [管理画面]については下記フィールドのみバックアップされます。
- ログイン画面の文言
- オートログイン有効期間

## 関連ドキュメント
- [バックアップ](/ja/docs/management/backup/)
- [同期項目一覧](/ja/docs/reference/sync-site-data/)
- [本番環境のデータを検証環境に同期するボタンを設置する](/ja/docs/tutorials/place-a-button-to-synchronize-production-data-with-the-validation-environment/)
- [災害対策（DR）](/ja/docs/about/disaster-recovery/)


---

# GCS, S3に設定したファイルの有効期限について

> 元ページ: `reference/expiration-for-files-in-gcs-and-s3` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/expiration-for-files-in-gcs-and-s3/

Kurocoから保存したGCS,S3ファイルのURLはTopics::list/detailsなどのAPIで呼び出すと、有効期限付きのURLがレスポンスされます。
これは、コンテンツとの連動性を担保するためですが、こちらのURLをSSGなどで長期間利用している場合、有効期限切れになることがありますのでご注意ください。

それぞれのパターンでの有効期限は以下のように設定されています。

## コンテンツに紐づくGCS/S3ファイル
コンテンツに紐づくGCS/S3ファイルはTopics::list/details/preview などのAPIを経由してファイルURLを取得します。その際の有効期限になります。

- APIにキャッシュ期間が設定されている場合で7日以内の場合  
=> APIのキャッシュ期間＋30秒
- APIにキャッシュ期間が設定されている場合で7日以上の場合  
=> 7日
- APIにキャッシュ期間が設定されていない場合  
=> 30分または、セッション時間＋30秒の短い方

:::caution
SSGなどでこちらのURLを長期間使用していると有効期限切れになる恐れがあります。
:::

:::tip
コンテンツに紐づくGCS/S3ファイル項目では、項目設定で `公開状態と連動して恒久URLで配信` を有効にすると、コンテンツが公開中の間は有効期限のない固定URL（恒久URL）で配信できます。設定方法は[コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/#ファイルgcsにアップロード)を参照してください。
:::

## ファイルマネージャーのGCS/S3ファイル
ファイルマネージャーからGCS/S3のディレクトリに保存したファイルのURLは以下の有効期限になります。

- 閲覧制限フォルダのファイルをAPI経由で取得した場合  
[コンテンツに紐づくGCS/S3ファイル](#コンテンツに紐づくgcss3ファイル)と同様
- 閲覧制限フォルダのファイルをファイルマネージャーのファイルパスから開いた場合  
=> 30分または、セッション時間＋30秒の短い方
- パブリックフォルダ  
=> 無期限

## 管理画面の表示に使用するURL
コンテンツの編集画面、承認ワークフローのコンテンツ詳細画面、フォームの回答などで表示されるGCS/S3ファイルのURLは以下の有効期限になります。

=> 30分または、セッション時間＋30秒の短い方

:::info
アクセス毎にファイルURLが更新されるため、通常の管理画面利用での影響はありません。
:::

## 関連ドキュメント
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)


---

# ファイルマネージャーで利用できるファイルの種類

> 元ページ: `reference/what-file-formats-does-the-file-manager-support` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/what-file-formats-does-the-file-manager-support/
> 概要: 静的ファイル全般をご利用になれます。[画像最適化機能]も有効になっておりますので、画像ファイルではそちらもご活用ください

## 利用できるファイルについて
静的ファイル全般をご利用になれます。[画像最適化機能](/ja/docs/reference/api-convert-image/)  も有効になっておりますので、画像ファイルではそちらもご活用ください。  


拡張子としては、以下が許可されています。
- jpg
- jpeg
- gif
- css
- js
- html
- htm
- mp3
- mp4
- m4a
- m4b
- xml
- json
- docx
- xlsx
- xlsm
- xltx
- pptx
- 7z
- aiff
- asf
- asx
- avi
- bmp
- csv
- doc
- fla
- flv
- gz
- gzip
- jpeg
- mid
- mov
- m4a
- mpc
- mpeg
- mpg
- ods
- odt
- pdf
- png
- ppt
- pxd
- qt
- ram
- rar
- rm
- rmi
- rmvb
- rtf
- sdc
- sitd
- swf
- sxc
- sxw
- tar
- tgz
- tif
- tiff
- txt
- vsd
- wav
- wma
- wmv
- xls
- zip
- ico
- lzh
- htc
- dxf
- 3g2
- 3gp
- m4v
- dwg
- btb
- bml
- clt
- mng
- ecm
- ai
- ttf
- svg
- eot
- woff
- otf
- epub
- psd
- cur
- xap
- x-font-ttf
- obj
- stl
- plist
- ipa
- webm
- map
- rdf
- ogg
- woff2
- msi
- m3u8
- ts
- bcmap
- properties
- dotx
- xltm
- conf
- mobileconfig
- apk
- log
- webp
- oam
- wasm
- heic
- heif
- meclib

お手持ちのファイル形式が上記になく、利用できるかの確認をご希望の際には[サポート事務局](https://kuroco.zendesk.com/)までお問い合わせください。


## 制限事項
- php/cgi/perl などサーバーサイド側でのプログラムは動作しません。SSIや.htaccessなども利用できません。
- `.`(ドット)から始まる隠しファイルはアップロードできません。

## 補足
### 80MB以上のファイルをアップロードしたい場合
Amazon S3/Google Cloud Storageと連動する仕組みがありますので、80MB以上の大きさのファイル（※5GBまで）をアップロードされる場合は、そちらの利用もご検討ください。  
Google Cloud Storageの設定は[Firebase](/ja/docs/management/firebase/)をご確認ください。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [Amazon S3](/ja/docs/management/amazon-s3/)
- [Firebase](/ja/docs/management/firebase/)
- [コンテンツ投稿時にアップロードできるファイルの最大容量を教えてください。](/ja/docs/faq/what-is-the-maximum-size-of-files-that-can-be-uploaded/)
