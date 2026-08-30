# Kurocoドキュメント: FAQ / ファイル

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 画像(FileManagerにアップロード)を利用してアップロードしたファイルを他のコンテンツのファイル(ファイルマネージャーから)で使用できますか？（`can-i-attach-files-from-other-content-structure-via-filemanager`）
- ファイルマネージャーにアップロードした画像をコンテンツの拡張項目で使用できますか？（`can-i-use-kurocofiles-images-in-additional-fields`）
- KurocoFilesでは、Nuxt Imageはサポートしていますか？（`does-kuroco-files-support-nuxt-image`）
- ファイルの項目でファイル容量をレスポンスに追加するにはどうしたら良いですか？（`how-can-i-add-the-file-size-information-to-the-file-item-response`）
- PDFファイルの表示やダウンロードを制限する方法はありますか？（`how-do-i-restrict-pdf-access-and-download`）
- フロントエンドからファイルをアップロードしてコンテンツに関連づけるにはどうしたらよいですか？（`how-do-i-upload-image-and-manage-it`）
- Kuroco上にアップロードしたPDFファイルなどに含まれるテキストを検索するAPIを作成できますか？（`is-it-possible-to-create-an-api-to-search-the-contents-of-pdf-files-uploaded-to-kuroco`）
- 閲覧権限のないファイルへアクセスした場合に任意のページにリダイレクトさせることはできますか？（`is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory`）
- ファイルマネージャーで利用できるファイルの種類を教えてください（`what-file-formats-does-the-file-manager-support`）
- コンテンツ投稿時にアップロードできるファイルの最大容量を教えてください。（`what-is-the-maximum-size-of-files-that-can-be-uploaded`）
- KurocoFilesのキャッシュはいつクリアされますか？（`when-are-cached-kurocofiles-cleared`）


---

# 画像(FileManagerにアップロード)を利用してアップロードしたファイルを他のコンテンツのファイル(ファイルマネージャーから)で使用できますか？

> 元ページ: `faq/can-i-attach-files-from-other-content-structure-via-filemanager` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-attach-files-from-other-content-structure-via-filemanager/
> 概要: はい、ファイル(ファイルマネージャーから)を使用して他のコンテンツでアップロードしたファイルをコンテンツに添付できます。

はい、ファイル(ファイルマネージャーから)を使用して他のコンテンツでアップロードしたファイルをコンテンツに添付できます。

## 参照元のファイル
例えば、コンテンツ定義ID=20で以下のコンテンツ定義を持ち、コンテンツにファイルを設定しているとします。  

- コンテンツ定義
    ![Image from Gyazo](https://t.gyazo.com/teams/diverta/2166a46d48319b4be9ff0e349370e35d.png)
    ![Image from Gyazo](https://t.gyazo.com/teams/diverta/80dc6cb851900dcaac6f8010f16b4d7e.png)

- コンテンツ
    ![Image from Gyazo](https://t.gyazo.com/teams/diverta/3f1f8bd4c5511c80cda94a1852abcfb0.png)

## パラメーターの設定
このコンテンツを、他のコンテンツ定義の「ファイル(ファイルマネージャーから)」で利用したい場合は、以下のようにパラメータを設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad28f8306685f5827723bcdafeadab66.jpg)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0673c0ff106fd2f28fb8ca02b6b44b1.png)

`topics_group_id:20`の「20」の部分はファイルの参照元になるコンテンツ定義のIDを入力してください。

## 使用方法
前のステップでコンテンツ定義を設定したら、コンテンツ編集ページのファイル(ファイルマネージャーから)を通じてファイルを添付できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b9d581ad4481301d6f4cbce48bd72635.png)

他のコンテンツ定義からのファイルは、読み取りや添付はできますが、更新や削除はできません。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)


---

# ファイルマネージャーにアップロードした画像をコンテンツの拡張項目で使用できますか？

> 元ページ: `faq/can-i-use-kurocofiles-images-in-additional-fields` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-kurocofiles-images-in-additional-fields/
> 概要: コンテンツの拡張項目の「ファイル（ファイルマネージャーから）」を利用することで、ファイル上の画像をコンテンツの拡張項目に設定することが出来ます。

コンテンツの拡張項目の「ファイル（ファイルマネージャーから）」を利用することで、ファイル上の画像をコンテンツの拡張項目に設定することが出来ます。

## 拡張項目の設定画面
設定項目に「ファイル（ファイルマネージャーから）」を設定します。  
この画面の詳細は、[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)の管理画面マニュアルをご参照ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/41d2350b5a040f2605678ffef71d2714.png)

## コンテンツ編集画面
「+」ボタンをクリックするとファイルマネージャーが開き、画像を選択できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a84f4e34a59960de26b8ef46392053b7.png)

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [画像(FileManagerにアップロード)を利用してアップロードしたファイルを他のコンテンツのファイル(ファイルマネージャーから)で使用できますか？](/ja/docs/faq/can-i-attach-files-from-other-content-structure-via-filemanager/)
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)


---

# KurocoFilesでは、Nuxt Imageはサポートしていますか？

> 元ページ: `faq/does-kuroco-files-support-nuxt-image` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/does-kuroco-files-support-nuxt-image/
> 概要: はい、Nuxt Imageのご利用が可能です

はい、Nuxt Imageのご利用が可能です。  
[Fastly Provider](https://image.nuxtjs.org/providers/fastly)を参考にProvider設定を追加してください。  

ドキュメントサイト内のリファレンスページも併せてご参照ください。  
[画像の動的変換について](/ja/docs/reference/api-convert-image/)

## 関連ドキュメント
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)


---

# ファイルの項目でファイル容量をレスポンスに追加するにはどうしたら良いですか？

> 元ページ: `faq/how-can-i-add-the-file-size-information-to-the-file-item-response` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-add-the-file-size-information-to-the-file-item-response/
> 概要: 後処理の出力変換リストを使う方法と、後処理にカスタム処理を設定する方法があります。以下を参考に設定してください。

後処理の出力変換リストを使う方法と、後処理にカスタム処理を設定する方法があります。
以下を参考に設定してください。

## 出力変換リストを使う方法
### エンドポイントの後処理に設定

Topics::listのエンドポイントの後処理に以下の設定を追加します。

:::info
以下の設定はファイルの項目に`files`のslugを設定しているTopics::listのエンドポイントを前提として書いています。  
ご自身の設定に合わせて調整ください。
:::

|項目|設定|
|:--|:--|
|実行内容|出力変換リスト|
|操作|コピーする|
|項目|list.files.url|
|新しい項目|file_size|
|処理|FileSize|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed8e7719adf2f6ec657304078a407de2.png)

## カスタム処理を設定する方法

対象のファイルサイズを取得してレスポンスに追加するカスタム処理を作成し、エンドポイントの後処理に設定します。  
ファイルサイズの取得には[rcms_file_size](/ja/docs/reference/smarty-plugin/#rcms_file_size)のSmartyプラグインを利用します。

### カスタム処理を作成
[カスタム処理編集](/ja/docs/management/function/#カスタム処理編集)の画面から以下のコードを設定したカスタム処理を作成します。  

:::info
以下のコードはファイルの項目に`files`のslugを設定しているTopics::listのエンドポイントを前提として書いています。  
ご自身の設定に合わせて調整ください。
:::

```smarty
{foreach from=$json.list key=key item=details}
    {if isset($details.files) && $details.files.url_org}
        {assign var='file_url' value=$details.files.url_org}
        {assign var='file_size' value=$file_url|rcms_file_size}
        {assign_array_set var="json.list.$key.files" key="file_size" value=$file_size from=$json.list.$key.files}
    {/if}
{/foreach}

{assign var='processed_json' value=$json}
```

### エンドポイントの後処理に設定
追加したカスタム処理を対象のエンドポイントの後処理に設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7ae64572297de51fecf993718d690f0e.png)

## 動作確認
エンドポイントのレスポンスをSwagger UIで確認すると、以下のように、`files`の項目に`file_size`のレスポンスが追加されていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b531aec64f4327fcaf218fde298c3ba9.png)

:::caution
「ファイル(GCSにアップロード)」「ファイル(S3にアップロード)」の項目には対応しておりませんのでご注意ください。
:::

## 関連ドキュメント
- [後処理](/ja/docs/reference/post-processing/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# PDFファイルの表示やダウンロードを制限する方法はありますか？

> 元ページ: `faq/how-do-i-restrict-pdf-access-and-download` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-restrict-pdf-access-and-download/
> 概要: PDFファイルのダウンロードや印刷制限のご要望はよくいただきますが、様々な方法があります。下記以外についても、確認があれば[サポート]までご連絡ください。

PDFファイルのダウンロードや印刷制限のご要望はよくいただきますが、様々な方法があります。  
下記以外についても、確認があれば[サポート](/ja/docs/about/support/)までご連絡ください。  

## ダウンロードをさせない方法
- Office365やBoxなどのクラウドサービスを利用する
- PDFを扱う商用サービスを利用する
- [PDF.js](https://mozilla.github.io/pdf.js/)で擬似的にダウンロード出来ないようにする

## 印刷をさせない方法
- PDFのセキュリティ設定で印刷不可にする
- Office365やBoxなどのクラウドサービスを利用する
- PDFを扱う商用サービスを利用する
- [PDF.js](https://mozilla.github.io/pdf.js/)で擬似的にダウンロード出来ないようにして印刷ボタンも無効にする

## 会員のみにしかPDFを見せたくない
- Kurocoのコンテンツで閲覧制限をかけてファイル(KurocoFilesにアップロード)の拡張項目を利用する
- ファイルマネージャーのKurocoFiles(閲覧制限)のフォルダに保存する

## 問い合わせ後のみにPDFダウンロードリンクをメールで送信したい
- KurocoでGCSかS3で連携し、メールテンプレートで```{storage_url path=$path var='url' expire="+1 hour" }```のように有効期限付きURL生成機能を利用する

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [GCS, S3に設定したファイルの有効期限について](/ja/docs/reference/expiration-for-files-in-gcs-and-s3/)
- [ltdフォルダのファイルにつくt=・・・のURLの有効期限はいくつですか？](/ja/docs/faq/how-long-is-the-t-url-in-the-ltd-folder-valid/)
- [閲覧権限のないファイルへアクセスした場合に任意のページにリダイレクトさせることはできますか？](/ja/docs/faq/is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory/)


---

# フロントエンドからファイルをアップロードしてコンテンツに関連づけるにはどうしたらよいですか？

> 元ページ: `faq/how-do-i-upload-image-and-manage-it` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-upload-image-and-manage-it/
> 概要: フロントエンドからあるコンテンツの内容に画像などファイルを紐づけたい場合、Kurocoでは以下の3つの手順を実行してください。

フロントエンドからあるコンテンツの内容に画像などファイルを紐づけたい場合、Kurocoでは以下の3つの手順を実行してください。

- コンテンツ定義作成（フィールドにファイル関連を追加）
- エンドポイント作成
- フロントエンド作成

## コンテンツ定義作成
対象のコンテンツの拡張項目を作成し、`ファイル（KurocoFilesにアップロード）`を設定してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9f42d8de30af289e99c17e3a705edae.png)

## エンドポイント作成
下記APIエンドポイントを設定してください。

- カテゴリ：ファイル
- モデル：Files
- オペレーション：upload

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5e11c65fa2defaf8f6e95b23e6a153ca.png)
## フロントエンド作成
アップロード用のエンドポイントにファイルを送信し、レスポンスされてきたIDをコンテンツ更新リクエストに適用してください。
ファイル送信時のリクエストヘッダには`'Content-Type': 'multipart/form-data'`を指定してください。

```js
{
    headers: {
        'Content-Type': 'multipart/form-data',
    },
}
```

詳細なファイルのアップロード方法は、[KurocoとNuxt.jsで、フォーム画面を構築する -> ファイルの入力項目を追加する](/ja/docs/tutorials/setting-up-inquiry-forms/#ファイルの入力項目を追加する) をご参考ください。

## 関連ドキュメント
- [APIを使ったファイルのアップロードについて](/ja/docs/reference/uploading-files-using-the-api/)
- [コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？](/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/)


---

# Kuroco上にアップロードしたPDFファイルなどに含まれるテキストを検索するAPIを作成できますか？

> 元ページ: `faq/is-it-possible-to-create-an-api-to-search-the-contents-of-pdf-files-uploaded-to-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-create-an-api-to-search-the-contents-of-pdf-files-uploaded-to-kuroco/
> 概要: KurocoにはPDFファイルの内容を解析する機能がないので、PDFファイルに含まれるテキスト検索はできません。しかしながら、下記のようにPDFからテキストを抽出できるサービスと連携することで対応可能となります。

KurocoにはPDFファイルの内容を解析する機能がないので、PDFファイルに含まれるテキスト検索はできません。  
しかしながら、下記のようにPDFからテキストを抽出できるサービスと連携することで対応可能となります。

- [Adobe PDF Extract API](https://www.adobe.io/apis/documentcloud/dcsdk/pdf-extract.html)
- [Google Cloud Vision API](https://cloud.google.com/vision/docs/pdf?fbclid=IwAR1lGkE65H4kd1dCnVQV-QUe76lRiUJnitmAhc46kQ_OdyuRLKZnYU0s-zY#vision_text_detection_pdf_gcs-python)
- [AWS Lambda](https://aws.amazon.com/jp/lambda/)

## 対応方法
1. 上記サービスを利用してPDFからテキストを抽出する
2. 抽出したデータをKurocoに格納する
3. Kurocoで検索機能を実装する

注: ご紹介したサービスの利用方法については、各サイトにてご確認ください。

:::info
[チュートリアル 検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)
:::

## 関連ドキュメント
- [検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)
- [Kurocoのキーワード検索の種類](/ja/docs/reference/keyword-search-types/)
- [サイト内全文検索機能は実装できますか？](/ja/docs/faq/can-i-create-a-search-function/)


---

# 閲覧権限のないファイルへアクセスした場合に任意のページにリダイレクトさせることはできますか？

> 元ページ: `faq/is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory/
> 概要: 定数の設定で対応可能です。「LOGIN_URL_FOR_ LTD」をセットして、値にリダイレクト先のURLを入力してください。

[定数](/ja/docs/management/constants/)の設定で対応可能です。
「LOGIN_URL_FOR_LTD」をセットして、値にリダイレクト先のURLを入力してください。    

## 設定箇所
[環境設定]->[定数]で[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7cb44cbf691ccc363c9527568bddf65b.png)
## 設定値
以下の値を設定します。  
- 名前：LOGIN_URL_FOR_LTD
- 値：リダイレクト先のURL

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c391492987fa7ecca5ab6ba5be4bd3.png)

設定が完了すると、閲覧権限が無いファイルへアクセスした際、NotFoundの代わりに指定したURLへリダイレクトします。  
また、その際クエリパラメータとして、リダイレクト元のURLが付与されます。  

## 例
リダイレクト元URL：  
`https://example.g.kuroco-img.app/files/ltd/test/test_file.pdf`

リダイレクト先URL：  
`https://www.diverta.co.jp/?return_url=https%3A%2F%2Fexample.g.kuroco-img.app%2Ffiles%2Fltd%2Ftest%2Ftest_file.pdf`

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [KurocoFilesディレクトリとドメインの使い分けについて](/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)
- [ltdフォルダのファイルにつくt=・・・のURLの有効期限はいくつですか？](/ja/docs/faq/how-long-is-the-t-url-in-the-ltd-folder-valid/)
- [PDFファイルの表示やダウンロードを制限する方法はありますか？](/ja/docs/faq/how-do-i-restrict-pdf-access-and-download/)


---

# ファイルマネージャーで利用できるファイルの種類を教えてください

> 元ページ: `faq/what-file-formats-does-the-file-manager-support` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-file-formats-does-the-file-manager-support/
> 概要: 静的ファイル全般をご利用になれます。[画像最適化機能]も有効になっておりますので、画像ファイルではそちらもご活用ください

<head>
    <link rel="canonical" href="https://kuroco.app/ja/docs/reference/what-file-formats-does-the-file-manager-support/" />
</head>

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
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [コンテンツ投稿時にアップロードできるファイルの最大容量を教えてください。](/ja/docs/faq/what-is-the-maximum-size-of-files-that-can-be-uploaded/)


---

# コンテンツ投稿時にアップロードできるファイルの最大容量を教えてください。

> 元ページ: `faq/what-is-the-maximum-size-of-files-that-can-be-uploaded` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-the-maximum-size-of-files-that-can-be-uploaded/
> 概要: コンテンツ投稿時にアップロードできるファイルの最大容量をご案内します。

コンテンツ投稿時にアップロードできるファイルの最大容量をご案内します。

|  拡張項目  |  最大容量  |備考|
| :-- | :-- | :-- | 
|  WYSIWYG(Insert image)  |  80MB  || 
|  画像（KurocoFilesにアップロード）  |  80MB程度  || 
|  ファイル（KurocoFilesにアップロード）  |  80MB程度  || 
|  ファイル（ファイルマネージャーから） |  ファイルの保存場所に依存します。|<br/><ul><li>KurocoFiles：80MB程度</li><li>GCS：5GB</li><li>S3：5GB</li></ul>| 
|  ファイル（GCSにアップロード）  | 5GB |※Firebaseと連携が必要です。| 
|  ファイル（S３にアップロード）  | 5GB |※Amazon S3と連携が必要です。   | 
|  動画ファイル（Vimeo）  | 5GB |※Firebaseと連携が必要です。 | 

:::info
外部システムとの連携方法については、以下のチュートリアルを参考にしてください。  
[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)  
[Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)  
[Vimeoと連携して動画をアップロードする](/ja/docs/tutorials/how-to-connect-to-vimeo/)
:::

## ファイルアップロード時の注意点
処理時間が30秒以上になると処理が自動でキャンセルされる場合がございます。その場合はデータ量を少なくして複数回アップロードを実行してください。

## バッチ処理によるファイルアップロードについて
バッチ処理を利用してファイルをアップロードできます。複数のファイルを同時にアップロードして容量が大きくなる場合は場合はバッチをご利用ください。

:::info
バッチ処理の利用方法は、[Kurocoのバッチ処理を利用する](/docs/tutorials/how-to-use-batch/)をご確認ください。
:::

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [Vimeoと連携して動画をアップロードする](/ja/docs/tutorials/how-to-connect-to-vimeo/)
- [APIを使ったファイルのアップロードについて](/ja/docs/reference/uploading-files-using-the-api/)
- [ファイルマネージャーで利用できるファイルの種類を教えてください](/ja/docs/faq/what-file-formats-does-the-file-manager-support/)


---

# KurocoFilesのキャッシュはいつクリアされますか？

> 元ページ: `faq/when-are-cached-kurocofiles-cleared` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/when-are-cached-kurocofiles-cleared/
> 概要: KurocoFilesのCDNキャッシュは、ファイルがアップロードや削除がされるとそのフォルダ内のファイルを対象にクリアされます。

KurocoFilesのCDNキャッシュは、ファイルがアップロードや削除がされるとそのフォルダ内のファイルを対象にクリアされます。
キャッシュクリアの完了までには通常は1秒以内ですが、数秒から十数秒かかる場合があります。

## 注意点
- フォルダ名が半角英数以外でURLエンコードして表示させるような名称のものの場合、キャッシュのクリアができない場合もありますので、フォルダ名に関しては日本語等のご利用をお避けください。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [画像・ファイル管理におけるKurocoFilesとKurocoFrontの使い分けについて](/ja/docs/tutorials/difference-between-kurocofiles-and-kurocofront/)
- [画像のURL末尾にパラメータを付与してもキャッシュがクリアされません。画像のキャッシュクリアの方法を教えて下さい。](/ja/docs/faq/how-do-i-clear-cached-images/)
- [CDNにキャッシュされたレスポンスかどうかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-responses-in-the-cdn-cache/)
