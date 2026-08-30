# Kurocoドキュメント: FAQ / API

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 関連情報選択で選択したコンテンツの全情報をレスポンスに追加するにはどうしたら良いですか？（`add-all-information-on-the-content-selected-in-the-relational-data-selection-to-the-response`）
- サイト内全文検索機能は実装できますか？（`can-i-create-a-search-function`）
- APIによるコンテンツの追加/更新時に関連情報をslugで指定できますか（`can-i-specify-relational-data-by-slug-when-adding-updating-content-via-api`）
- コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？（`can-i-update-topics-files-using-bulk_upsert-api`）
- 下書き保存されたコンテンツのファイル・画像をそのまま利用してAPI経由でコンテンツの登録・更新できますか？（`can-i-use-files-and-images-of-draft-content-via-api`）
- APIのレスポンスをコンテンツカテゴリで絞り込みたい（`filtering-api-responses-by-content-category`）
- APIのレスポンスをタグカテゴリで絞り込みたい（`filtering-api-responses-by-tag-category`）
- ECのAPIでカード決済を行うには？（`how-can-i-get-card-token`）
- KurocoでRSSを取得するにはどうしたら良いですか？（`how-can-i-get-rss`）
- カートを利用せずに直接商品を指定して購入するには？（`how-can-i-purchase-without-cart`）
- 管理画面プラグインから認証が必要なエンドポイントにリクエストを送るにはどうしたらいいですか？（`how-can-i-request-an-authenticated-endpoint-from-the-admin-plugin`）
- APIをJSON以外のフォーマットでレスポンスできますか？（`how-can-i-response-csv-format`）
- 1つのページで複数のAPIからのレスポンスを得たい場合はどうしたら良いですか？（`how-do-i-get-responses-from-multiple-apis-on-one-page`）
- 記事の前後ページを取得するにはどうしたら良いですか？（`how-do-i-get-sibling-topics`）
- 選択肢毎に紐付くコンテンツの件数を取得する方法はありますか？（`how-to-get-the-number-of-contents-linked-to-each-option`）
- コンテンツ定義編集で項目設定をグループ化したのですが、APIから返却される json はグループ化されません。どうすればいいですか？（`how-to-group-json-response-for-grouped-content-definition-items`）
- 「一覧に表示する > 載せない」で登録したコンテンツをAPIのレスポンスに含めることはできますか？（`is-it-possible-to-get-api-responses-for-content-registered-with-do-not-display-in-list`）
- インサートのAPIにデフォルト値を設定できますか？（`set-defaults-for-the-insert-api`）


---

# 関連情報選択で選択したコンテンツの全情報をレスポンスに追加するにはどうしたら良いですか？

> 元ページ: `faq/add-all-information-on-the-content-selected-in-the-relational-data-selection-to-the-response` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/add-all-information-on-the-content-selected-in-the-relational-data-selection-to-the-response/
> 概要: レスポンスされた関連情報のIDから対象のコンテンツの情報を取得して、エンドポイントのレスポンスに追加するカスタム処理を作成し、エンドポイントの後処理に設定することで対応ができます。

レスポンスされた関連情報のIDから対象のコンテンツの情報を取得して、エンドポイントのレスポンスに追加するカスタム処理を作成し、エンドポイントの後処理に設定することで対応ができます。  

## カスタム処理の設定
[カスタム処理編集](/ja/docs/management/function/#カスタム処理編集)の画面から以下のコードを設定したカスタム処理を作成します。  

:::info
以下のコードはext_1の項目に関連情報選択を設定している前提として書いています。  
ご自身の設定に合わせて調整ください。
:::

### module_typeがtopicsの場合

```smarty
{*  エンドポイント設定パラメータ *}
{assign_array var='method_params'           values=''}
{assign       var='method_params.topics_id' value=$json.details.ext_1.module_id}
{api_method
    var='response'
    model='Topics'
    method='details'
    version='1'
    method_params=$method_params}

{append var='json.details.ext_1' value=$response.details index='details'}
{assign var='processed_json'     value=$json}
```
### module_typeがmemberの場合

```smarty
{*  エンドポイント設定パラメータ *}
{assign_array var='method_params'           values=''}
{assign       var='method_params.member_id' value=$json.details.ext_1.module_id}
{api_method
    var='response'
    model='Member'
    method='details'
    version='1'
    method_params=$method_params}

{append var='json.details.ext_1' value=$response.details index='details'}
{assign var='processed_json'     value=$json}
```

### module_typeがformの場合

```smarty
{*  エンドポイント設定パラメータ *}
{assign_array var='method_params'            values=''}
{assign       var='method_params.inquiry_id' value=$json.details.ext_1.module_id}
{api_method
    var='response'
    model='InquiryForm'
    method='details'
    version='1'
    method_params=$method_params}

{append var='json.details.ext_1' value=$response.details index='details'}
{assign var='processed_json'     value=$json}
```

## エンドポイントの後処理に設定
追加したカスタム処理を対象のエンドポイントの後処理に設定します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1fdb4a099f1ea4d84fe886f21e627dcd.png)

## 動作確認
エンドポイントのレスポンスをSwagger UIで確認すると、以下のように、`ext_1`の下に`details`という項目名で紐づけられた関連情報の詳細が追加されていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d3aa0e0a1e88752b823e43a0ee1dedb2.png)

## listのエンドポイントの場合
Topics::listのエンドポイントの場合は、以下のコード例になります。  

```smarty
{assign_array var='empty_array' values=""}
{assign var='empty_object' value=$empty_array|@to_object}

{foreach from=$json.list key=key item=details}
	{assign var='topics_id' value=$details.ext_1.module_id}
	{assign var='module_type' value=$details.ext_1.module_type}
	{assign var='details.ext_1' value=$empty_object}
	{if $topics_id && $module_type == "topics"}
		{* エンドポイント設定パラメータ *}
		{assign_array var='method_params' values=''}
		{assign var='method_params.topics_id' value=$topics_id}
		{api_method
			var='response'
			model='Topics'
			method='details'
			version='1'
			method_params=$method_params}
		{append var='details' value=$response.details index='ext_1'}
	{/if}
	{assign_array_set var="json.list" key=$key value=$details from=$json.list}
{/foreach}


{assign var='processed_json' value=$json}
```


## 関連ドキュメント
- [後処理](/ja/docs/reference/post-processing/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)


---

# サイト内全文検索機能は実装できますか？

> 元ページ: `faq/can-i-create-a-search-function` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-create-a-search-function/
> 概要: サイト内検索には２通りの方法があります。「Kurocoのfilter機能を利用する」「別サービスを利用する」

サイト内検索には下記の２通りの方法があります。
- Kurocoのfilter機能を利用する
- Kurocoのキーワード検索機能を利用する
- 別サービスを利用する

## Kurocoのfilter機能を利用する
APIのfilter機能を利用することで、コンテンツの条件検索やキーワード検索を実装できます。  
詳細な実装方法はチュートリアルにまとめていますので、[チュートリアル -> 検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)をご確認ください。

## Kurocoのキーワード検索機能を利用する
コンテンツ定義のキーワード検索機能を利用することで、コンテンツの条件検索やキーワード検索を実装できます。  
詳細な実装方法はチュートリアルにまとめていますので、[チュートリアル -> キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)をご確認ください。

## 別サービスを利用する
Google検索のような、ページ全体を検索したい場合には別サービスと連動して実装いただくことになります。  
例えば下記サービスをご利用になれます。
- [Google プログラム可能な検索エンジン](https://programmablesearchengine.google.com/intl/ja_jp/about/)
- [Algolia](https://www.algolia.com/)

利用できる検索エンジンに制約はありません。  
その他のサービスのご利用については、[弊社サポート](https://kuroco.zendesk.com/hc/ja)までご相談ください。

## 関連ドキュメント
- [検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)
- [あいまい検索用のベクトルテンプレートを用意する](/ja/docs/tutorials/how-to-implement-vector-search/)
- [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
- [Kurocoのキーワード検索の種類](/ja/docs/reference/keyword-search-types/)


---

# APIによるコンテンツの追加/更新時に関連情報をslugで指定できますか

> 元ページ: `faq/can-i-specify-relational-data-by-slug-when-adding-updating-content-via-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-specify-relational-data-by-slug-when-adding-updating-content-via-api/
> 概要: profile APIは会員制サイトでログインしているかどうかのチェックをするのに利用できるAPIとなっております

可能です。コンテンツの関連情報選択は`module_id`をslugで指定したリクエストに対応しています。  
以下の形式でリクエストを送ってください。

- GETのレスポンスと同じ形式
```json
"ext_1": {
  "module_id": "slug",
  "module_type": "topics"
}
```

- 短縮記法
```
"ext_1": "slug"
```

## 関連ドキュメント
- [関連情報選択で選択したコンテンツの全情報をレスポンスに追加するにはどうしたら良いですか？](/ja/docs/faq/add-all-information-on-the-content-selected-in-the-relational-data-selection-to-the-response/)
- [他のコンテンツと同じSlugを設定できますか？](/ja/docs/faq/can-i-set-the-same-slug-as-other-content/)
- [コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？](/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/)
- [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)


---

# コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？

> 元ページ: `faq/can-i-update-topics-files-using-bulk_upsert-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/
> 概要: コンテンツのbulk_upsert APIで画像・ファイル項目の更新は可能です。

コンテンツのbulk_upsert APIで画像・ファイル項目の更新は可能です。

:::caution
zipファイルを利用する方法では、以下の項目のみ更新できます。Vimeo項目の更新には対応していません。
- 画像（KurocoFilesにアップロード）
- ファイル（KurocoFilesにアップロード）

GCS・S3項目を更新する場合は、[クラウドソースフォルダを利用する方法](#クラウドソースフォルダを利用したs3gcsファイルの更新)をご参照ください。
:::

## zipファイルの用意
bulk_upsert APIでファイル項目を更新するには、zip形式のファイルを用意する必要があります。

任意の名称でフォルダを作成し、その直下に更新対象のファイルを配置してください。ファイル名には任意の半角英数字を設定できます。
```
.
`- assets
    |- File1.png
    |- PdfFile.pdf
    `- Image.png
```

作成したフォルダをzip形式で圧縮します。
```
.
|- assets # 作成したフォルダ
`- assets.zip # assetsフォルダを圧縮したzipファイル
```

## Files::uploadを利用したファイルアップロード
`Files::upload`のAPIを利用して、先ほど作成したZIPファイルをアップロードします。詳しい手順は、[APIを使ったファイルのアップロードについて](/ja/docs/reference/uploading-files-using-the-api/)をご参照ください。

```js
// Files::uploadのレスポンス
{
  "file_id": "files/temp/*.zip",
  "errors": []
}
```

完了したら、以下のようなリクエストボディを`Topics::bulk_upsert`にPOSTします。

`Files::upload`のレスポンスに含まれる`file_id`を`assets_file`に、設定したいファイルの名称を`list`の各項目(ファイルまたは画像項目)に指定してください。


```js
{
    "assets_file": {
        "file_id": "files/temp/*.zip" // Files::uploadのレスポンスに含まれるfile_id
    },
    "list": [
        {
            "topics_id": 1,
            // ...
            "file_field": { "file_nm":  "File.png" } // zipファイル内のファイル名
        },
        {
            "topics_id": 2,
            // ...
            "file_field": { "file_nm":  "PdfFile.pdf" }
        },
        {
            "subject": "New Content",
            // ...
            "file_field": { "file_nm":  "Image.png" }
        }
    ]
}
```

:::caution
- `file_field`の部分はご自身の拡張項目のID(ext_X)かslugに変更してください。
:::

## カスタム処理でのアップロード

カスタム処理からbulk_upsertを呼び出す場合は、`Files::upload`のAPIを利用できないため、ファイル操作系のプラグインを利用してファイルをアップロードします。

以下は、ファイルマネージャの`/files/ltd`ディレクトリに配置した`assets.zip`ファイルをカスタム処理でアップロードする例です。
```smarty
{rcms_hash var='temp_name' data='bulk_upsert_assets' key=$smarty.now|strval}
{assign var='temp_assets_path' value="/files/temp/`$temp_name`.zip"}
{put_file path=$temp_assets_path files_path="/files/ltd/assets.zip"}

{assign_array var='body' values=''}

{* assets_file *}
{assign_array var='body.assets_file'         values=''}
{assign       var='body.assets_file.file_id' value=$temp_assets_path|trim:'/'}

{* list *}
{assign_array var='body.list' values=''}
{assign_array var='content'                    values=''}
{assign       var='content.topics_id'          value=1}
{assign_array var='content.file_field'         values=''}
{assign       var='content.file_field.file_nm' value='File.png'}
{assign var='body.list.' value=$content}

{* POST Topics::bulk_upsert *}
{api_internal var='response' method='POST' endpoint='/rcms-api/1/topics/bulk_upsert' queries=$body use_current_session=1}
```

:::caution
- `value=1`の部分は更新したいコンテンツIDに置き換えてください。
- `file_field`の部分はご自身の拡張項目のID(ext_X)かslugに変更してください。  
- `File.png`はアップロードしたファイルの名前に変更してください。  
- `/rcms-api/1/topics/bulk_upsert`の部分はご自身のエンドポイントに変更してください。セキュリティが動的アクセストークンに設定されたAPIである必要があります。
:::

:::info
参考: [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)  
参考: [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)  
:::

## クラウドソースフォルダを利用したS3/GCSファイルの更新

クラウドストレージが有効な環境では、`cloud_source_dir`パラメータを利用して、クラウドストレージ上のファイルを直接参照してS3/GCS項目を更新できます。

zipファイルのアップロードは不要で、クラウドストレージ上の指定フォルダからファイルがコピーされます。

### 事前準備
更新対象のファイルをクラウドストレージの任意のフォルダに配置します。パスはファイルマネージャのプライベートディレクトリ配下を指定します。

例えば、`cloud_source_dir`に`upload/assets`を指定した場合、以下のパスが参照されます:
- S3の場合: `files/a/private/upload/assets/`
- GCSの場合: `files/g/private/upload/assets/`

### リクエスト例

```js
{
    "cloud_source_dir": "upload/assets",
    "list": [
        {
            "topics_id": 1,
            // ...
            "s3_file_field": { "file_nm": "Document.pdf" } // cloud_source_dir内のファイル名
        },
        {
            "topics_id": 2,
            // ...
            "s3_file_field": { "file_nm": "Image.png" }
        }
    ]
}
```

:::caution
- `s3_file_field`の部分はご自身のS3/GCS拡張項目のID(ext_X)かslugに変更してください。
- `cloud_source_dir`で指定したフォルダ内に該当ファイルが存在する必要があります。
- クラウドストレージが有効なサイトでのみ利用可能です。
:::

:::tip
`cloud_source_dir`は、zipファイルによる画像・ファイル項目の更新と組み合わせて利用することもできます。その場合、S3/GCS項目は`cloud_source_dir`から、画像・ファイル項目は`assets_file`のzipからそれぞれ参照されます。
:::

## 関連ドキュメント
- [APIを使ったファイルのアップロードについて](/ja/docs/reference/uploading-files-using-the-api/)
- [bulk_upsert APIを利用して、任意のCSVファイルをコンテンツにインポートする](/ja/docs/tutorials/bulk-upload-using-api/)


---

# 下書き保存されたコンテンツのファイル・画像をそのまま利用してAPI経由でコンテンツの登録・更新できますか？

> 元ページ: `faq/can-i-use-files-and-images-of-draft-content-via-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-files-and-images-of-draft-content-via-api/
> 概要: できます。Topics::draft_details APIのレスポンスに含まれるfile_idを、Topics::insert / Topics::updateのファイル項目に指定してください。

できます。  
API経由で下書き保存されたコンテンツのファイル・画像を、再度アップロードすることなくそのまま利用してコンテンツの登録・更新を行えます。

## 仕様

`Topics::draft_details` API（承認待ちデータも同様）のレスポンスに、下書き保存時のファイル・画像の `file_id` が含まれます。

```json
"images": [
  {
    "id": "210861_ext_05_0",
    "url": "https://.../files/temp/t=pv_.../topics/2c36f971ab1f93a1ecc0f1b21fe8673f/210861_ext_5_0.jpg",
    "desc": "",
    "url_org": "https://...",
    "file_id": "files/temp/topics/2c36f971ab1f93a1ecc0f1b21fe8673f/210861_ext_5_0.jpg"
  }
]
```

- レスポンスの `file_id`（例: `files/temp/topics/.../210861_ext_5_0.jpg`）を取得します。
- この `file_id` をそのまま `Topics::insert` / `Topics::update` API のファイル項目に指定することで、保存済みのファイル・画像をそのまま利用して追加・更新できます。
- 繰り返しあり・なしいずれのファイル項目でも利用できます。

## 関連ドキュメント
- [APIでのコンテンツ更新・追加時にワークフローは利用できますか？](/ja/docs/faq/can-i-add-or-update-workflow-content-via-api/)


---

# APIのレスポンスをコンテンツカテゴリで絞り込みたい

> 元ページ: `faq/filtering-api-responses-by-content-category` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/filtering-api-responses-by-content-category/
> 概要: contents_typeのパラメータを指定して絞込みしてください。コンテンツカテゴリの親子関係を考慮する場合はcategory_parent_idやexclude_category_parent_idのパラメータを利用します。

`contents_type`のパラメータを指定して絞込みしてください。  
コンテンツカテゴリの親子関係を考慮する場合は`category_parent_id`や`exclude_category_parent_id`のパラメータを利用します。

## コンテンツ例
以下のコンテンツをフィルターした場合の結果を確認します。

|トピックスID|タイトル|コンテンツカテゴリID|カテゴリ名|
|:--|:--|:--|:--|
|1152|親カテゴリの記事|17|親NEWS|
|1153|子カテゴリの記事|54|子NEWS|
|1154|孫カテゴリの記事|55|孫NEWS|

- コンテンツカテゴリ設定
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/bae8bc040d19387a4a4a3fd4ca6cad31.png)

- コンテンツ一覧
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/7b63f011c03ab287ea84bc56d69059ad.png)

### contents_typeでのフィルター
`contents_type`によるフィルターはコンテンツカテゴリの親子関係を考慮しないため、指定したコンテンツカテゴリに所属するコンテンツの一覧がレスポンスされます。

#### contents_type=[17]を指定 
「親カテゴリの記事」のみが表示されます。  

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?contents_type%5B%5D=17`

Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1152,
      "ymd": "2023-02-16",
      "contents_type": 17,
      "contents": "",
      "subject": "親カテゴリの記事",
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 1,
    ・
    ・
    ・
  }
}
```

#### contents_type=[17,54]を指定
「親カテゴリの記事」と「子カテゴリの記事」が表示されます。  

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?contents_type%5B%5D=17&contents_type%5B%5D=54`

Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1152,
      "ymd": "2023-02-16",
      "contents_type": 17,
      "contents": "",
      "subject": "親カテゴリの記事",
      ・
      ・
      ・
    },
    {
      "topics_id": 1153,
      "ymd": "2023-02-16",
      "contents_type": 54,
      "contents": "",
      "subject": "子カテゴリの記事",
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 2,
    ・
    ・
    ・
  }
}
```

### category_parent_idでのフィルター
`category_parent_id`によるフィルターはコンテンツカテゴリの親子関係を考慮するため、指定したコンテンツカテゴリとその配下のカテゴリに所属するコンテンツの一覧がレスポンスされます。

#### category_parent_id=[17]を指定
「親カテゴリの記事」「子カテゴリの記事」「孫カテゴリの記事」が表示されます。  

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?category_parent_id%5B%5D=17`

Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1152,
      "ymd": "2023-02-16",
      "contents_type": 17,
      "contents": "",
      "subject": "親カテゴリの記事",
      ・
      ・
      ・
    },
    {
      "topics_id": 1153,
      "ymd": "2023-02-16",
      "contents_type": 54,
      "contents": "",
      "subject": "子カテゴリの記事",
      ・
      ・
      ・
    },
    {
      "topics_id": 1154,
      "ymd": null,
      "contents_type": 55,
      "contents": "",
      "subject": "孫カテゴリの記事",
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 3,
    ・
    ・
    ・
  }
}
```

#### category_parent_id=[54]を指定
「子カテゴリの記事」と「孫カテゴリの記事」が表示されます。 

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?category_parent_id%5B%5D=54`

Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1153,
      "ymd": "2023-02-16",
      "contents_type": 54,
      "contents": "",
      "subject": "子カテゴリの記事",
      ・
      ・
      ・
    },
    {
      "topics_id": 1154,
      "ymd": null,
      "contents_type": 55,
      "contents": "",
      "subject": "孫カテゴリの記事",
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 2,
    ・
    ・
    ・
  }
}
```

### exclude_category_parent_idでのフィルター
`exclude_category_parent_id`によるフィルターを使うと、指定したコンテンツカテゴリとその配下のカテゴリに所属するコンテンツの一覧がレスポンスから除外されます。

#### exclude_category_parent_id=[54]を指定
「親カテゴリの記事」のみが表示されます。

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?exclude_category_parent_id%5B%5D=54`
	
Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1152,
      "ymd": "2023-02-16",
      "contents_type": 17,
      "contents": "",
      "subject": "親カテゴリの記事",
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 1,
    ・
    ・
    ・
  }
}
```

## 関連ドキュメント
- [APIのレスポンスをタグカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-tag-category)


---

# APIのレスポンスをタグカテゴリで絞り込みたい

> 元ページ: `faq/filtering-api-responses-by-tag-category` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/filtering-api-responses-by-tag-category/
> 概要: tag_category_idのパラメータを指定して絞込みしてください。このパラメータの指定はタグカテゴリの親子関係を考慮します。

`tag_category_id`のパラメータを指定して絞込みしてください。  
このパラメータの指定はタグカテゴリの親子関係を考慮します。  

## コンテンツ例
以下のコンテンツをフィルターした場合の結果を確認します。

|トピックスID|タイトル|タグカテゴリID|タグカテゴリ名|タグID|タグ名|
|:--|:--|:--|:--|:--|:--|
|1152|親カテゴリの記事|7|親タグカテゴリ|186|親タグ|
|1153|子カテゴリの記事|8|子タグカテゴリ|187|子タグ|
|1154|孫カテゴリの記事|9|孫タグカテゴリ|188|孫タグ|

- タグカテゴリ設定
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/7b0c4420598d83f884aa2d5d78e3c32b.png)

- タグ一覧
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/698a6bb0d9a23c7928acca421efea9a9.png)

- コンテンツ一覧
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/cef0804c19153bddc8c8a6e2aa9cb4d1.png)

### tag_category_idでのフィルター
`tag_category_id`によるフィルターはタグカテゴリの親子関係を考慮し、指定したタグカテゴリ及びその配下のタグカテゴリに所属するタグが付与されたコンテンツの一覧がレスポンスされます。  

#### tag_category_id=[7]を指定 
「親カテゴリの記事」「子カテゴリの記事」「孫カテゴリの記事」が表示されます。    

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?tag_category_id=7`

Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1152,
      "ymd": "2023-02-16",
      "contents_type": 17,
      "contents": "",
      "subject": "親カテゴリの記事",
      ・
      ・
      ・
      "tags": [
        {
          "tag_id": 186,
          "tag_nm": "親タグ",
          "open_contents_cnt": 1,
          "all_contents_cnt": 1,
          "inst_ymdhi": "2023-02-16T15:40:07+09:00",
          "update_ymdhi": "2023-02-16T15:40:52+09:00",
          "tag_category_id": 7,
          ・
          ・
          ・
        }
      ],
      ・
      ・
      ・
    },
    {
      "topics_id": 1153,
      "ymd": "2023-02-16",
      "contents_type": 54,
      "contents": "",
      "subject": "子カテゴリの記事",
      ・
      ・
      ・
      "tags": [
        {
          "tag_id": 187,
          "tag_nm": "子タグ",
          "open_contents_cnt": 1,
          "all_contents_cnt": 1,
          "inst_ymdhi": "2023-02-16T15:40:21+09:00",
          "update_ymdhi": "2023-02-16T15:40:52+09:00",
          "tag_category_id": 8,
          ・
          ・
          ・
        }
      ],
      ・
      ・
      ・
    },
    {
      "topics_id": 1154,
      "ymd": null,
      "contents_type": 55,
      "contents": "",
      "subject": "孫カテゴリの記事",
      ・
      ・
      ・
      "tags": [
        {
          "tag_id": 188,
          "tag_nm": "孫タグ",
          "open_contents_cnt": 1,
          "all_contents_cnt": 1,
          "inst_ymdhi": "2023-02-16T15:40:34+09:00",
          "update_ymdhi": "2023-02-16T15:40:52+09:00",
          "tag_category_id": 9,
          ・
          ・
          ・
        }
      ],
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 3,
    ・
    ・
    ・
  }
}
```

#### tag_category_id=[8]を指定 
「子カテゴリの記事」「孫カテゴリの記事」が表示されます。      

Request URL：  
`https://example.g.kuroco.app/rcms-api/13/news?tag_category_id=8`

Response body：
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1153,
      "ymd": "2023-02-16",
      "contents_type": 54,
      "contents": "",
      "subject": "子カテゴリの記事",
      ・
      ・
      ・
      "tags": [
        {
          "tag_id": 187,
          "tag_nm": "子タグ",
          "open_contents_cnt": 1,
          "all_contents_cnt": 1,
          "inst_ymdhi": "2023-02-16T15:40:21+09:00",
          "update_ymdhi": "2023-02-16T15:40:52+09:00",
          "tag_category_id": 8,
          ・
          ・
          ・
        }
      ],
      ・
      ・
      ・
    },
    {
      "topics_id": 1154,
      "ymd": null,
      "contents_type": 55,
      "contents": "",
      "subject": "孫カテゴリの記事",
      ・
      ・
      ・
      "tags": [
        {
          "tag_id": 188,
          "tag_nm": "孫タグ",
          "open_contents_cnt": 1,
          "all_contents_cnt": 1,
          "inst_ymdhi": "2023-02-16T15:40:34+09:00",
          "update_ymdhi": "2023-02-16T15:40:52+09:00",
          "tag_category_id": 9,
          ・
          ・
          ・
        }
      ],
      ・
      ・
      ・
    }
  ],
  "pageInfo": {
    "totalCnt": 2,
    ・
    ・
    ・
  }
}
```

## 関連ドキュメント
- [APIのレスポンスをコンテンツカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-content-category)


---

# ECのAPIでカード決済を行うには？

> 元ページ: `faq/how-can-i-get-card-token` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-get-card-token/
> 概要: KurocoのECモジュールのAPIでカード決済するにはカード番号などの情報をAPIに直接渡すのでは無く、決済サービス会社の用意したAPIを利用しカード番号などを元にカードトークン情報を取得し、そのトークン情報をKurocoのAPIに設定する必要があります。

KurocoのECモジュールのAPIでカード決済するにはカード番号などの情報を
APIに直接渡すのでは無く、決済サービス会社の用意したAPIを利用し
カード番号などを元にカードトークン情報を取得し、そのトークン情報を
KurocoのAPIに設定する必要があります。

## カード利用方法
Kurocoでサポートしている決済サービスはPaygentなので
Paygentからカードトークンを取得するためのサンプルコードを記載します。
尚、詳細に関してはPaygent管理画面の「マニュアル/仕様書」より  
`02_PG外部インターフェース仕様説明書（トークン決済）.pdf`  
をダウンロードして確認してください。

### .envファイル設定

|キー名|値|
|---|---|
|PAYGENT_MARCHANT_ID|Paygentの「マーチャントID」|
|PAYGENT_TOKEN_GENERATE_PUBKEY|Paygentの「トークン生成鍵」|
|PAYGENT_TOKEN_JS|開発用)<br/>https://sandbox.paygent.co.jp/js/PaygentToken.js<br/>本番用）<br/>https://token.paygent.co.jp/js/PaygentToken.js|

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b32ade1a90619d81a24c6e321e430510.png)
#### サンプルコード
```markup title="/components/CreditCardForm.vue"
<template>
    <div>
        <vue-form-generator
            ref="form"
            :schema="schema"
            :model="cardData"
            class="c-form"
            @model-updated="onInput"
        />
        <div>
            <button
                type="button"
                @click="subscribe()"
            >
                決済実行
            </button>
        </div>
    </div>
</template>

<script>
import PaygentHelper from '@/util/paygentHelper';

export default Vue.extend({
    name: 'CreditCardForm',
    components: {
        'vue-form-generator': VueFormGenerator.component
    },
    data() {
        return {
            paygent: null,
            cardData: {
                cardNumber: '',
                expireMonth: '',
                expireYear: '',
                cvc: '',
                name: '',
            },
            cardToken: '',
        };
    },
    created() {
        this.paygent = new PaygentHelper();
        this.cardData.expireYear = this.formatYear(new Date().getFullYear() + 1);
    },
    mounted() {
        this.schema = {
            fields: [
                {
                    type: 'vuetifyText',
                    inputType: 'text',
                    min: 0,
                    max: 16,
                    label: 'カード番号',
                    model: 'cardNumber',
                    text: this.cardData.cardNumber,
                    placeholder: '※ハイフンは入力しないでください。',
                    required: true,
                    texttype: 'number',
                    labelClasses: 'required',
                },
                {
                    label: '有効期限',
                    model: 'expireMonth',
                    placeholder: '月',
                    contents: [
                        {
                            key: '01',
                            value: '1月',
                        },
                        (略)
                        {
                            key: '12',
                            value: '12月',
                        },
                    ],
                    option: {
                        key: this.cardData.expireMonth,
                        value: this.cardData.expireMonth + '月',
                    },
                    required: true,
                    labelClasses: 'required',
                    type: 'vuetifySingleOption',
                    styleClasses: 'c-form__twoColumns'
                },
                {
                    model: 'expireYear',
                    label: '',
                    placeholder: '年',
                    contents: [],
                    option: {
                        key: this.cardData.expireYear,
                        value: '20' + this.cardData.expireYear + '年',
                    },
                    required: true,
                    type: 'vuetifySingleOption',
                    styleClasses: 'c-form__twoColumns'
                },
                {
                    model: 'cvc',
                    type: 'vuetifyText',
                    inputType: 'text',
                    min: 3,
                    max: 4,
                    label: 'セキュリティコード',
                    text: this.cardData.cvc,
                    placeholder: '',
                    required: true,
                    labelClasses: 'required',
                },
                {
                    type: 'vuetifyText',
                    inputType: 'text',
                    min: 0,
                    max: 100,
                    label: 'カード名義人',
                    model: 'name',
                    text: this.cardData.name,
                    placeholder: '',
                    required: true,
                    labelClasses: 'required',
                },
            ]
        }

        // 年を自動設定
        this.schema.fields.map((item) => {
            if (item.model === 'expireYear') {
                const year_array = this.arrYear()
                year_array.map((y) => {
                    let option = {
                            key: y,
                            value: '20' + y + '年'
                    }
                    item.contents.push(option)
                })
            }
            return item
        })
    },
    computed: {
        canGenerateToken() {
            const paygentConfigValues = Object.values(this.paygentConfig);
            const cardDataValues = Object.values(this.cardData);
            return (
                paygentConfigValues.filter((v) => v).length === paygentConfigValues.length &&
                cardDataValues.filter((v) => v).length === cardDataValues.length
            );
        },
    },
    methods: {
        onInput (value, fieldName) {
            this.$set(this.cardData, fieldName, value);
        },
        formatYear(year) {
            return ('' + year).slice(-2);
        },
        arrYear() {
            const date = new Date();
            const thisYear = this.formatYear(date.getFullYear());
            const intYear = parseInt(thisYear);
            const years = [];
            for (let y = intYear; y <= intYear + 10; y++) {
                years.push(`${y}`);
            }
            return years;
        },
        async generateToken() {
            this.cardToken = '';
            try {
                const response = await this.paygent.fetchToken(this.cardData);
                this.cardToken = response.cardToken;
            } catch (errorResponse) {
                this.$store.dispatch('snackbar/setError', `[${errorResponse.code}] ${errorResponse.error}`);
                this.$store.dispatch('snackbar/snackOn');
            }
        },
        async subscribe() {
            await this.generateToken()

            if (this.cardToken === '') {
                // トークン取得エラー
                return;
            }

            const self = this;

            this.loading = true

            const cartItem = {
                "product_id": 41202,
                "quantity": 1
            }
            let orderInfo = {
                "order_products": [
                    cartItem
                ],
                "ec_payment_id": 58,
                "card_token": self.cardToken,
            }

            this.$auth.ctx.$axios
            .post('/rcms-api/1/subscribe', orderInfo)
            .then(function (response) {
                alert('購入しました。')
            })
            .catch(function (error) {
                if (error.response) {
                    alert(error.response.data.errors?.[0].message);
                } else {
                    alert("エラーが発生しました");
                }
            });
        }
    },
});
</script>
```

```js title="paygentHelper.js"
import { paygentConfig, paygentScriptUrl, paygentErrorCodeDetails } from './paygentConfig';

export default class PaygentHelper {
  constructor(config = null, lang = 'ja') {
    this.config = config ? config : paygentConfig
    this.lang = lang;

    if (!document.body.querySelector(`script[src*='${paygentScriptUrl}']`)) {
      // JS未読み込み
      const script = document.createElement('script');
      script.type = 'text/javascript';
      script.src = paygentScriptUrl;
      document.body.appendChild(script);
      this.script = script;
      this.script.onload = () => {
        this.paygentToken = new PaygentToken();
      };
    } else {
      // JS読み込み済み
      this.paygentToken = new PaygentToken();
    }
  }
  setConfig(config) {
    this.config = config;
  }
  async fetchToken(cardData) {
    return new Promise((resolve, reject) => {
      if (!this.paygentToken) {
        reject({
          code: 'XXXX',
          cardToken: '',
          error: 'Unexpected error',
        });
      }
      this.paygentToken.createToken(
        this.config.merchantId,
        this.config.tokenGeneratePubkey,
        {
          card_number: cardData.cardNumber,
          expire_year: cardData.expireYear,
          expire_month: cardData.expireMonth,
          cvc: cardData.cvc,
          name: cardData.name,
        },
        (response) => {
          const resultCode = response.result || '';
          if (response.result === undefined || response.result !== '0000') {
            reject({
              code: resultCode,
              cardToken: '',
              error: paygentErrorCodeDetails[resultCode]['ja'] || 'Unexpected error',
            });
          } else {
            resolve({
              code: resultCode,
              cardToken: response.tokenizedCardObject.token,
              error: '',
            });
          }
        },
      );
    });
  }
}
```

```js
export const paygentConfig = {
  merchantId: process.env.PAYGENT_MARCHANT_ID,
  tokenGeneratePubkey: process.env.PAYGENT_TOKEN_GENERATE_PUBKEY,
};

export const paygentScriptUrl = process.env.PAYGENT_TOKEN_JS;
export const paygentErrorCodeDetails = {
  '1100': {
    en: 'Merchant id - Required',
    ja: 'マーチャントID - 必須エラー',
  },
  '1200': {
    en: 'Token generation pubkey - Required',
    ja: 'トークン生成公開鍵 - 必須エラー',
  },
  '1201': {
    en: 'Token generation pubkey - Invalid value',
    ja: 'トークン生成公開鍵 - 不正エラー',
  },
  '1300': {
    en: 'Card number - Required',
    ja: 'カード番号 - 必須チェックエラー',
  },
  '1301': {
    en: 'Card number - Invalid format',
    ja: 'カード番号 - 書式チェックエラー',
  },
  '1400': {
    en: 'Expiration year - Required',
    ja: '有効期限(年) - 必須チェックエラー',
  },
  '1401': {
    en: 'Expiration month - Invalid format',
    ja: '書式チェックエラー - 数字以外が含まれている',
  },
  '1500': {
    en: 'Expiration month - Required',
    ja: '有効期限(月) - 必須チェックエラー',
  },
  '1501': {
    en: 'Expiration month - Invalid format',
    ja: '有効期限(月) - 書式チェックエラー',
  },
  '1502': {
    en: 'Expiration date - Invalid format - The value should be future date and within the next 20 years.',
    ja: '有効期限(年月)が不正です。(過去年月である、未来20年以降である)',
  },
  '1600': {
    en: 'CVC - Invalid format',
    ja: 'セキュリティコード - 書式チェックエラー',
  },
  '1601': {
    en: 'CVC - Required if you use security code token',
    ja: 'セキュリティコード - 必須エラー(セキュリティコードトークンの場合)',
  },
  '1700': {
    en: 'Name - Invalid format',
    ja: 'カード名義 - 書式チェックエラー',
  },
  '7000': {
    en: 'Unsupported browser',
    ja: '非対応のブラウザです。',
  },
  '7001': {
    en: 'Connection failure',
    ja: 'ペイジェントとの通信に失敗しました。',
  },
  '8000': {
    en: 'Under maintenance',
    ja: 'システムメンテナンス中です。',
  },
  '9000': {
    en: 'Internal server error',
    ja: 'ペイジェント決済システム内部エラー',
  },
};
```

## 関連ドキュメント
- [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/)
- [Paygentで3Dセキュアを使用する](/ja/docs/tutorials/ec-using-3d-secure-with-paygent/)
- [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
- [EC決済方法別設定](/ja/docs/reference/ec-paymet-setting/)
- [カートを利用せずに直接商品を指定して購入するには？](/ja/docs/faq/how-can-i-purchase-without-cart/)


---

# KurocoでRSSを取得するにはどうしたら良いですか？

> 元ページ: `faq/how-can-i-get-rss` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-get-rss/
> 概要: バッチ処理で定期的にRSSを取得し、Kurocoのコンテンツに追加or更新することで対応が可能です。

バッチ処理で定期的にRSSを取得し、Kurocoのコンテンツに追加or更新することで対応が可能です。

### RSSフィードの取得
バッチ処理に次のようなSmartyコードを記述すると、RSSフィードの内容を連想配列で取得できます。

```smarty
{get_file var='rss_xml' url='https://www.diverta.co.jp/RSS.rdf' save=false}{* RSSの内容を取得 *}
{xmltojson var='rss_json' xml=$rss_xml}{* XMLをJSONに変換 *}
{assign var='rss_feed' value=$rss_json|@json_decode}{* JSONを連想配列に変換 *}
```

:::tip
取得・変換したRSSの内容は以下の記述を追加してテストすることで確認できます。  
`test:{$rss_feed|@debug_print_var}`
:::

### Kurocoコンテンツの更新
複数のコンテンツを一括で更新する場合、
bulk_upsert APIを使うとリクエスト数・処理時間の削減が出来ますので、必要に応じてご利用ください。  

また、id_reference_allow_list のパラメータに設定した項目名をリクエストボディのtopics_idのフィールドに指定すると、
topics_idの代わりに任意の項目をキーとしてコンテンツを追加・更新できます。  
例えば、以下の例ではext_1が同じコンテンツが存在する場合、更新として処理されます。

```smarty
{* RSSデータをKurocoコンテンツのフォーマットに変換 *}
{assign_array var='body'      values=''}
{assign_array var='body.list' values=''}
{foreach from=$rss_feed.entry item='entry'}
    {assign_array var='topics' values=''}
    {assign       var='topics.topics_id' value='ext_1'}
    {assign       var='topics.subject'  value=$entry.title}
    {assign       var='topics.ext_1'    value=$entry.id}
    {assign       var='topics.ext_2'    value=$entry.updated}
    {assign var='body.list.' value=$topics}
{/foreach}

{* コンテンツの一括更新 *}
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/1/topics/bulk_upsert'
    method='POST'
    queries=$body
    member_id=1}
```

## 関連ドキュメント
- [bulk_upsert APIを利用して、任意のCSVファイルをコンテンツにインポートする](/ja/docs/tutorials/bulk-upload-using-api/)
- [カスタム処理からKurocoのAPIを呼び出せますか？ > 例2. POSTメソッド (認証あり)](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/#%E4%BE%8B2-post%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89-%E8%AA%8D%E8%A8%BC%E3%81%82%E3%82%8A)
- [カスタム処理でデバッグを目的としたログを出力できますか？](/ja/docs/faq/can-the-original-process-output-logs-for-debugging-purposes/)


---

# カートを利用せずに直接商品を指定して購入するには？

> 元ページ: `faq/how-can-i-purchase-without-cart` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-purchase-without-cart/
> 概要: order_products パラメータを利用することでカート機能を利用せずに直接商品を購入することが出来ます。有料会員商品など、複数の商品を同時に購入することがない前提の場合はこちらの機能を利用してください。

`order_products` パラメータを利用することでカート機能を利用せずに直接商品を購入することが出来ます。
有料会員商品など、複数の商品を同時に購入することがない前提の場合はこちらの機能を利用してください。

### 利用方法
APIは通常の `ECOrder:purchase` APIを利用します。

#### サンプルリクエスト
パターン1（複数指定）
```
{
  "order_products": [
    {
      "product_id": 12345,
      "quantity": 1
    },
    {
      "product_id": 12345,
      "quantity": 2
    }
  ],
  "ec_payment_id": XXX
}
```

パターン2（単数指定）
```
{
  "product_id": 12345,
  "quantity": 1,
  "ec_payment_id": XXX
}
```
※`cart_id`の指定は不要です。

## 関連ドキュメント
- [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
- [EC機能 API設定とSwagger UIを利用した動作確認の方法](/ja/docs/tutorials/how-to-use-purchase-by-swagger/)
- [ECサイトを作成する フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)
- [ECのAPIでカード決済を行うには？](/ja/docs/faq/how-can-i-get-card-token/)


---

# 管理画面プラグインから認証が必要なエンドポイントにリクエストを送るにはどうしたらいいですか？

> 元ページ: `faq/how-can-i-request-an-authenticated-endpoint-from-the-admin-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-request-an-authenticated-endpoint-from-the-admin-plugin/
> 概要: 管理画面のプラグインで、propsとして、api_key,signature,sidが渡されますので、これを使ってログインが可能です。エンドポイントはlogin_methodパラメータにapi_key/signatureを設定したLogin::login_challengeを使用してください。

## 管理画面からの認証について
### props
管理画面のプラグインで、propsとして、自動的に下記の値が渡されますので、これを使ってログインが可能です。  
エンドポイントは`login_method`パラメータに`api_key/signature`を設定した`Login::login_challenge`を使用してください。

|キー|型|
|:--|:--|
|api_key|String|
|signature|String|
|sid|String|

### API
セキュリティを動的アクセストークンに設定したAPIで以下のエンドポイントを準備します。  

- Login::login_challenge
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/7476dd7f99f9aa711b9a7f6866e559c3.png)
- Login::token
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/b481ebd4de1aa23b5aa17d9b4174b19b.png)

:::info
`rcms_api_access_token`は管理画面のクッキーでも作られていますが、管理画面ドメインで利用されるクッキーをAPIドメインの認証に使うのは適切ではありません。  
また、クッキーはSameSite属性や`__Host-`の利用など、ドメインを跨いで利用する場合に制約や仕様の変更が多いため、管理画面プラグインでは動的アクセストークンの利用を推奨します。
:::

### サンプルコード
「[管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加する](/ja/docs/tutorials/create-custom-pages-in-the-kuroco-admin-panel-using-the-admin-panel-plugin/)」
のドキュメントで紹介したコードのscript部分を、以下のように更新すると動的アクセストークンをカスタムヘッダーに含めたリクエストが可能です。  

コンテンツを取得するエンドポイントも同じ動的アクセストークンのAPI内に追加し、そちらを利用するように調整してください。

```markup  title="/management-vue-plugin-sample/packages/VueSample/src/pages/VueSample.vue"
<script>
import Vue from 'vue';
window.rcmsJS.vue.registerVM(Vue, rcms_js_config.publicPath); // eslint-disable-line
const axios = require('axios').default;

export default {
    components: {},
    props: {
        root_api_url: {
            type: String,
            default: '',
        },
        endpoint: {
            type: String,
            default: '',
        },
        api_key: {
            type: String,
            default: ''
        },
        signature: {
            type: String,
            default: ''
        },
        sid: {
            type: String,
            default: ''
        },
    },
    created: function () { },
    mounted: async function () {
        try {
            // Step 1: Obtain the grant token
            const grantTokenResponse = await axios.post(`${this.root_api_url}/rcms-api/10/login/login_challenge`, {
                api_key: this.api_key,
                signature: this.signature,
                sid: this.sid,
            });
            const grant_token = grantTokenResponse.data.grant_token;

            // Step 2: Obtain the access token
            const accessTokenResponse = await axios.post(`${this.root_api_url}/rcms-api/10/login/token`, {
                grant_token,
            });
            const access_token = accessTokenResponse.data.access_token.value;

            // Step 3: Use the access token to fetch data from the endpoint
            const resp = await axios.get(this.root_api_url + this.endpoint, {
                headers: {
                    'X-RCMS-API-ACCESS-TOKEN': access_token,
                },
            });
            this.items = resp.data.list ? resp.data.list : [];
        } catch (error) {
            //console.error(error);
        }
    },
    data() {
        return {
            items: [],
        };
    },

    computed: {},
};
</script>
```

## 関連ドキュメント
- [管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加する](/ja/docs/tutorials/create-custom-pages-in-the-kuroco-admin-panel-using-the-admin-panel-plugin/)


---

# APIをJSON以外のフォーマットでレスポンスできますか？

> 元ページ: `faq/how-can-i-response-csv-format` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-can-i-response-csv-format/
> 概要: ヘッダーまたはクエリパラメータで指定可能です。デフォルトで指定されるJSONのほかに、CSVやXMLが選択できます。また、ZIP圧縮されたJSONファイルも選択できます。

はい、ヘッダーまたはクエリパラメータで指定可能です。

デフォルトで指定されるJSONのほかに、CSVやXMLが選択できます。また、ZIP圧縮されたJSONファイルも選択できます。

:::caution
認証などJSON形式以外をサポートしていないモデルも存在します。
:::

## ヘッダーで指定する場合
Acceptヘッダーにて指定します。

```header title="CSV形式の場合"
Accept: text/csv
```
```header title="XML形式の場合"
Accept: text/xml
または
Accept: application/xml
```
```header title="ZIP形式の場合"
Accept: application/zip
```

## クエリパラメーターで指定する場合
`_output_format`にて指定します。

```header title="CSV形式の場合"
?_output_format=csv
```
```header title="XML形式の場合"
?_output_format=xml
```
```header title="ZIP形式の場合"
?_output_format=zip
```

CSVのヘッダーを書き換えるなど、データを変更したい場合は[カスタム処理を利用して、CSV出力されるデータ構造を変更する](/ja/docs/tutorials/how-to-implement-original-function-into-the-postprocess/)を参照してください。

## 関連ドキュメント
- [カスタム処理を利用して、CSV出力されるデータ構造を変更する](/ja/docs/tutorials/how-to-implement-original-function-into-the-postprocess/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [KurocoでRSSを取得するにはどうしたら良いですか？](/ja/docs/faq/how-can-i-get-rss/)


---

# 1つのページで複数のAPIからのレスポンスを得たい場合はどうしたら良いですか？

> 元ページ: `faq/how-do-i-get-responses-from-multiple-apis-on-one-page` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-get-responses-from-multiple-apis-on-one-page/
> 概要: 1つのページで複数のAPIレスポンスを得る場合、下記２パターンの方法があります。

1つのページで複数のAPIレスポンスを得る場合、下記２パターンの方法があります。

- Promise.allを利用
- awaitを利用

それぞれのパターンの記述例を記載します。

:::info
Nuxt.jsを利用したプロジェクトを前提としていますので、ご自身のケースに合わせて修正ください。  
:::

:::caution
下記部分はご自身のAPIのURLに合わせてください。  
`process.env.BASE_URL + '/rcms-api/14/top/1002'`  
`process.env.BASE_URL + '/rcms-api/1/form/6'`
:::  

## Promise.all(...)で同時実行する場合の記述例  
(foo & bar & ...)のように同時にデータを取得します。  

```markup
<script>
export default {
  async asyncData({ $axios }) {
    const [foo, bar] = await Promise.all([
      $axios.$get(process.env.BASE_URL + '/rcms-api/14/top/1002'),
      $axios.$get(process.env.BASE_URL + '/rcms-api/1/form/6')
      ]);
    return {foo,bar};
  },
}
</script>
```


## awaitで逐次実行する場合の記述例  
(foo -> bar -> ...)のように順番にデータを取得します。  

```markup
<script>
export default {
    data() {
      return {
        foo: null,
        bar: null
      }
    },
    methods: {
      async doAsync() {
        const foo = await this.$axios.$get(process.env.BASE_URL + '/rcms-api/14/top/1002');
        const bar = await this.$axios.$get(process.env.BASE_URL + '/rcms-api/1/form/6');
        this.foo = foo;
        this.bar = bar;
      }
    },
    mounted() {
      this.doAsync()
    }
}
</script>
```

Promise、awaitの詳細は下記ドキュメントをご参照ください。

- MDN Web Docs -> [Promise](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- MDN Web Docs -> [await](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/await)

## 関連ドキュメント
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)


---

# 記事の前後ページを取得するにはどうしたら良いですか？

> 元ページ: `faq/how-do-i-get-sibling-topics` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-get-sibling-topics/
> 概要: 例えば、記事詳細画面にて、ひとつ前の記事/次の記事を取得/表示したいような場合には、`central_id`を指定してリクエストしてください。

例えば、記事詳細画面にて、ひとつ前の記事/次の記事を取得/表示したいような場合には、`central_id`を指定してリクエストしてください。

`central_id`が使用可能なのは、下記のエンドポイントです。

- Category: `コンテンツ`
- Model: `Topics`  
- Operation: `list`

## 動作確認方法
以下のコンテンツが登録されているとします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/303ec72163c445867e31501f8d7d2816.png)

下の条件のコンテンツの前後のコンテンツを取得したい場合の動作をSwagger UIで確認します。
- コンテンツの題名(subject)が `テストです_3`
- コンテンツのIDが`1070`

[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ccabda3702e989b328943c1805e7acf.png)

`central_id`に`1070`を指定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f3ef958d8221631b96fc8d36e7260cc.png)

[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c62f172698f8864971113c48df5f98f.png)

以下のレスポンスが得られます。  
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "topics_id": 1073,
      "ymd": "2022-09-02",
      "contents_type": 37,
      "contents": "<p>テストです_4の記事の内容</p>",
      "subject": "テストです_4",
      ...
    },
    {
      "topics_id": 1070,
      "ymd": "2022-09-02",
      "contents_type": 37,
      "contents": "<p>テストです_3の記事の内容</p>",
      "subject": "テストです_3",
      ...
    },
    {
      "topics_id": 1069,
      "ymd": "2022-09-02",
      "contents_type": 37,
      "contents": "<p>テストです_2の記事の内容</p>",
      "subject": "テストです_2",
      ...
    }
  ],
  "pageInfo": ""
}
```

さらに2つ前/2つ後のコンテンツを取得したい場合には、`cnt`を指定してリクエストしてください。  
`cnt=n`を指定すると、`central_id`に指定したコンテンツと、その前後`n`個のコンテンツを取得します。  

## 関連ドキュメント
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [コンテンツ一覧のデフォルトの並び順は何ですか？](/ja/docs/faq/what-is-the-default-sort-order-for-content-list/)


---

# 選択肢毎に紐付くコンテンツの件数を取得する方法はありますか？

> 元ページ: `faq/how-to-get-the-number-of-contents-linked-to-each-option` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-get-the-number-of-contents-linked-to-each-option/
> 概要: 可能です。TopicsGroup::details のエンドポイントにext_config_flg trueを設定し、ext_no_for_countにカウントしたい選択形式の拡張番号を入力してください。

はい、`TopicsGroup::details` のエンドポイントに`ext_config_flg true` を設定し、`ext_no_for_count`にカウントしたい単一選択などの選択形式の拡張項目番号を入力してください。

## 設定箇所
エンドポイント設定画面の基本設定の箇所で設定します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a53ea3834e09e94213b69d005b298d52.png)

## JSONレスポンスの例
指定した拡張番号にcountの項目で追加されます。


```json
{
  "errors": [],
  "messages": [],
  "details": {
    ・
    ・
    ・
  },
  "ext_config": [
    {
      "no": "1",
      "ext_col_nm": "ext_1",
      "ext_index": 1,
     ・
     ・
     ・
      "default_value": "",
      "count": {
        "1": 2,
        "2": 5,
        "3": 1,
        "4": 4
      }
    }
  ]
}
```

## 関連ドキュメント
- [API](/ja/docs/management/api-list/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# コンテンツ定義編集で項目設定をグループ化したのですが、APIから返却される json はグループ化されません。どうすればいいですか？

> 元ページ: `faq/how-to-group-json-response-for-grouped-content-definition-items` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-group-json-response-for-grouped-content-definition-items/
> 概要: エンドポイントの設定 > 基本設定から、ext_group を有効化すると json がグループ化されて返却されます。

エンドポイントの設定 > 基本設定から、ext_group を有効化すると json がグループ化されて返却されます。

## ext_group パラメータの設定方法

1. 左側のサイドバーメニューから [API] をクリックします。

2. 対象のエンドポイントを選択し、[編集] をクリックします。

3. [基本設定] タブで、`ext_group` パラメータを有効にします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/68973500cad52715bcc41ee81b3fe9d7.png)


これにより、コンテンツ定義でグループ化された項目が API レスポンスの JSON でも同様にグループ化されて返却されます。

## レスポンス例

### ext_group パラメータが無効の場合

```json
{
  "errors": [],
  "messages": [],
  "details": {
    ...
    "ext_1": "値1",
    "ext_2": "値2"
  }
}
```

### ext_group パラメータが有効の場合

```json
{
  "errors": [],
  "messages": [],
  "details": {
    ...
    "ext_1": {
      "ext_1": "値1",
      "ext_2": "値2"
    }
  }
}
```

## 関連ドキュメント
- [グループ化・繰り返しを行ったコンテンツ項目の制御](/ja/docs/reference/control-of-grouped-and-repeated-content-items/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)


---

# 「一覧に表示する > 載せない」で登録したコンテンツをAPIのレスポンスに含めることはできますか？

> 元ページ: `faq/is-it-possible-to-get-api-responses-for-content-registered-with-do-not-display-in-list` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-get-api-responses-for-content-registered-with-do-not-display-in-list/
> 概要: 可能です。一覧に載せないデータも取得するためのパラメータ(get_unlisted_data)がございますので、有効にしてレスポンスを確認してください。

可能です。  
一覧に載せないデータも取得するためのパラメータ(`get_unlisted_data`)がございますので、有効にしてレスポンスを確認してください。

## 設定方法
APIのエンドポイント一覧で、Topics::list のエンドポイントの[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/39f09df50b191586e6f4dc68e294668b.png)

詳細設定の`get_unlisted_data`のパラメータにチェックを入れて更新します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0b550e5838342631570f3e582e860b2.png)

## レスポンスの確認
エンドポイントを設定したAPIの[Suwagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6efcab6e3a20ddfdfe41dce71d84aed1.png)

対象のエンドポイントの[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/16565a26e5e2f999defceb266971198a.png)

[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/37e3e86430a9650a4d473d285ece10e1.png)


「一覧に表示する > 載せない」で登録したコンテンツもレスポンスされていることが分かります。  
「載せない」に設定したコンテンツは`topics_flg`が0になります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a905365e068b67e36e469f80309b81f.png)

## 関連ドキュメント
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)


---

# インサートのAPIにデフォルト値を設定できますか？

> 元ページ: `faq/set-defaults-for-the-insert-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/set-defaults-for-the-insert-api/
> 概要: インサートのAPIで追加されるコンテンツにデフォルトの設定をするにはいくつかの方法があります。フロントエンド、前処理、トリガーで対応する方法を紹介しますので、ご希望の方法で実装ください。

インサートのAPIで追加されるコンテンツにデフォルトの設定をするにはいくつかの方法があります。  
フロントエンド、前処理、トリガーで対応する方法を紹介しますので、ご希望の方法で実装ください。  

本FAQではMember::insertのエンドポイントを想定してコードの紹介をします。  

## Member::insertにデフォルト値を設定する
### フロントエンドで対応する
例えば、メンバーの項目の、メルマガ拒否フラグはデフォルト(リクエストに含めない状態)でチェックが入った状態で登録されます。  
フロントエンドからリクエストを送る際に、`"email_send_ng_flg": false`をリクエストに含めるように実装すると、メルマガ拒否フラグのチェックを外した状態でメンバー登録できます。  

以下のように`"email_send_ng_flg": false`をユーザーに見せないところでリクエストに追加します。

```markup reference title="/pages/signup_with_default_value.vue"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/front-end/nuxtjs/signup_with_default_value.vue
```

### 前処理を追加する
例えば、メンバーの拡張項目に数値を設定している場合、API経由のリクエストに値の指定が無いと空欄で登録されます。  
複数の数値タイプの拡張項目があり、全てデフォルトで0をセットしたい場合は、以下のように書いたカスタム処理を前処理に設定します。  

[前処理](/ja/docs/reference/pre-processing/)で設定することで、エンドポイント毎にデフォルト値を設定できます。  

```smarty reference title="set_the_default_value_for_member_register"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/pre-processing/set_the_default_value_for_member_register_using_pre_processing.txt
```

### トリガーを設定する
複数の数値タイプの拡張項目にデフォルト値を設定する方法はトリガーを利用することもできます。  
トリガーは「[メンバーの登録前](/ja/docs/reference/trigger-variables/#メンバーの登録前)」を利用します。
カスタム処理で使用する変数名が前処理のパターンと少し変わります。  

トリガーで設定することでAPIで登録される全てのメンバーにデフォルト値を設定できます。

```smarty reference title="set_the_default_value_for_member_register"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/trigger/set_the_default_value_for_member_register_using_trigger.txt
```

## 関連ドキュメント
- [前処理](/ja/docs/reference/pre-processing/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
