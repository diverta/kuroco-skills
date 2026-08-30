# Kurocoドキュメント: 管理画面 / API

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- API（`api-list`）
- API 後処理（`api-postprocessing`）
- API セキュリティ（`api-security`）


---

# API

> 元ページ: `management/api-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/api-list/

APIではAPIの作成・設定と、エンドポイントの作成が行なえます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8eaac23a823cf68e8a19164f95db180.png)

## メニューリスト
画面上部にメニューリストが表示されます。  
[その他]をクリックすると追加のメニューが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e6b2a47e0cf3641cb9d9caa41d6b0c37.png)

### キャッシュクリアする
API設定のキャッシュをクリアします。  
Kuroco内部の動作に変更があった場合、キャッシュをクリアして最新版を適用/反映します。

### Swagger UI
Swagger UI画面に遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c773a1b377d3b68478c5fda555cdeb45.png)
詳細な利用方法は [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)をご確認ください。

### API構造の追加
API作成画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8909547c8d8b15fe645fbc367b13f411.png)

|項目   |説明  |
| :--- | :--- |
|タイトル|APIタイトルを記入します(必須)|
|版|バージョンを記入します(必須)|
|説明|APIに関する説明を記入します(必須)|
|並び順|APIの並び順を入力します。降順に並びます。|
|セキュリティ|APIのセキュリティを選択します。|
|追加する|クリックすると新しいAPIが作成されます|

### ステータス
API ID毎に有効無効を切り替えます。  
トグルスイッチをクリックすると確認モーダルが表示され、全てのエンドポイントを無効にできます。
実行すると作成済みのトークン(静的アクセストークン等)も削除されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfabd5cc8d5c9d29ea2c9adf034dd1c6.png)

### セキュリティ
APIのセキュリティを設定できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9907f9fb098097b7dce459fba9b03b6a.png)
セキュリティの設定については[APIセキュリティ](/ja/docs/management/api-security/)をご覧ください。

### CORS
CORS用に、Kurocoサーバーからレスポンンスヘッダに返却する情報をカスタマイズできます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cfaac5034eaf6833b1f5766a05a2fae7.png)
CORSに設定されたOriginは、Content-Security-Policy: frame-ancestorsに指定されるOriginとしても利用されます。

例えば、ローカル上のフロントエンド `http://localhost:8080` からKurocoサーバーにアクセスする場合には、下記の`http://localhost:8080`を設定してください。

詳細は[MDN](https://developer.mozilla.org/docs/Web/HTTP/CORS)のドキュメントを参照してください。

|項目   |対応するレスポンスヘッダ  |`http://localhost:8080`の例  |
| :--- | :--- | :--- |
|CORS_ALLOW_ORIGINS|Access-Control-Allow-Origin|`http://localhost:8080`|
|CORS_ALLOW_METHODS|Access-Control-Allow-Methods|GET,POST,OPTIONS|
|CORS_ALLOW_HEADERS|Access-Control-Allow-Headers|*|
|CORS_MAX_AGE|Access-Control-Max-Age|600|
|CORS_ALLOW_CREDENTIALS|access-control-allow-credentials|:white_check_mark:|

### API構造の編集
API編集画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/642dbeb89a6330c9f6ed16cb3a435793.png)

|項目   |説明  |
| :--- | :--- |
|API ID|自動で採番されるIDが表示されます。編集ボタンをクリックすると任意の数字を設定可能です。|
|タイトル|APIタイトルを記入します(必須)|
|版|バージョンを記入します(必須)|
|説明|APIに関する説明を記入します(必須)|
|並び順|APIの並び順を入力します。降順に並びます。|
|更新する|クリックするとAPIが更新されます|

### エクスポートする
JSON/YAML 形式でエクスポートが可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/259ed1b01f1922e015f3c973cdb2d050.png)

エクスポートされるファイルはKuroco独自のフォーマットの設定ファイルです。  
エクスポートに前処理/後処理を含める場合は、「前後の処理ブロックを含む」にチェックを入れてください。

### OpenAPIエクスポートする
JSON/YAML 形式でエクスポートが可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b76c2bf6fddb5f6ef8c1f59c364dd306.png)

エクスポートされるファイルはOpenAPI仕様に沿った形式の設定ファイルです。  
APIのドキュメント化、クライアントやサーバーコードの自動生成、APIテストとモックの作成など、開発ライフサイクル全体で利用されることを目的としています。

:::info
同じ内容は Admin MCP サーバの `api-export_openapi` ツールでも取得できます。詳細は [MCP サーバ リファレンス -> OpenAPI 定義の取得](/ja/docs/reference/mcp-server/#openapi-定義の取得) を参照してください。
:::

**サンプル**

```yaml
openapi: 3.1.0
info:
  title: Default
  version: '1.0'
  description: 'Default API'
servers:
  -
    url: 'https://xxxxxx.g.kuroco.app'
    description: 'API Backend'
paths:
  /rcms-api/1/news/list:
    get:
      tags:
        - コンテンツ
      summary: ''
      parameters:
        -
          name: _output_format
          schema:
            type: string
            format: ''
          in: query
          required: false
          style: form
          explode: true
          description: '形式 (json|xml|csv|zip)'
        -
          name: _lang
          schema:
            type: string
            format: ''
          in: query
          required: false
          style: form
          explode: true
          description: 言語
        -
          name: _charset
          schema:
            type: string
            format: ''
          in: query
          required: false
          style: form
          explode: true
          description: 文字コード
        -
          name: cnt
          schema:
            type: integer
            format: int64
          in: query
          required: false
          style: form
          explode: true
          description: 1ページの行数
        -
          name: pageID
          schema:
            type: integer
            format: int64
          in: query
          required: false
          style: form
          explode: true
          description: ページID
        -
          name: filter
          schema:
            type: string
            format: ''
          in: query
          required: false
          style: form
          explode: true
          description: フィルタークエリ
      responses:
        200:
          description: 'Topics data successfully fetched'
        404:
          description: 'Topics data could not be found'
・
・
・
```

### インポート
JSON/YAML 形式でインポートが可能です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5c5808d0e6989b2d259496b020236d9.png)

「新しいAPIとしてインポート」を選択すると、新しいAPIが作成されます。  
「現在のAPIへのインポート」を選択すると、現在のAPIが更新されます。

### 削除
クリックするとAPIが削除されます。
削除されたAPIの復活はできませんのでご注意ください。

## エンドポイント一覧
メニューリスト下部にエンドポイントの一覧が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dad3b5b22ee1a8d22ba27c7015f82a47.png)

新しいAPIを作成した時点では、ここには何も表示されていませんが、エンドポイントを追加することで表が表示されます。  
この表は作成したエンドポイントの[カテゴリ]によってグループ化して表示されます。

| 項目 | 説明 |
| :--- | :--- |
| 有効 | APIが有効/無効であるか |
| メソッド | HTTPメソッド |
| パス | エンドポイントのパス |
| モデル | エンドポイントに紐づいているKurocoのモデル |
| オペレーション | モデルに紐づくオペレーション |
| サマリー | エンドポイント作成時に指定した値 |
| パラメータ | オペレーション事項時のパラメータ |
| 認証 | 認証方式 |
| 7日間の利用状況 | 直近7日間の利用状況を「A / B / C / D」の形式で表示します。左から順に、キャッシュを経由しなかったAPI通信回数（hits）、キャッシュを経由したAPI通信回数（hits）、レスポンスボディの平均サイズ、平均実行時間（ms）です。<br/>利用実績がない場合は、この項目自体が表示されません。 |
| [更新] | クリックするとエンドポイントの編集ができます |
| [前処理] | クリックするとPre-processingの設定ができます<br/>また、前処理が設定されている場合はその数が表示されます。|
| [後処理] | クリックするとPost-processingの設定ができます<br/>また、前処理が設定されている場合はその数が表示されます。|
| [削除] | クリックするとエンドポイントを削除します |

### 追加
[追加]をクリックするとエンドポイント作成画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f7b7d352910c90fdd02973566732b4f.png)

エンドポイントの作成については[エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)をご覧ください。

### 更新履歴の確認
エンドポイントの設定画面からエンドポイントの編集履歴が確認できます。

エンドポイント一覧で、[編集]をクリックしてエンドポイントの設定を開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0de11fa7e480a92d703df495dcf173f9.png)

エンドポイントの設定画面の[更新履歴]をクリックすると、エンドポイントの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a8886b617c7ccaff5d24e1c691d3cb3.png)

#### エンドポイント更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f1b8424d9e224fcf9de34aaa7bdb174.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント設定後の注意点](/ja/docs/tutorials/points-to-note-after-endpoint-configuration/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [APIにアクセス元の国や都道府県を追加する](/ja/docs/tutorials/how-to-add-region-data/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [ログインユーザーの情報でAPIのレスポンスを動的に変更する](/ja/docs/tutorials/change-the-api-response-with-the-logged-in-users-information/)
- [カスタム処理を利用して、APIエンドポイントに独自のスタブを設定する](/ja/docs/tutorials/setting-up-stubs-on-api-endpoints-using-custom-functions/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える](/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [前処理](/ja/docs/reference/pre-processing/)
- [後処理](/ja/docs/reference/post-processing/)
- [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
- [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)
- [APIのキャッシュについて](/ja/docs/reference/api-cache/)
- [APIキャッシュクリアのタイミングと範囲](/ja/docs/reference/cache-clear-operation/)
- [APIをJSON以外のフォーマットでレスポンスできますか？](/ja/docs/faq/how-can-i-response-csv-format/)


---

# API 後処理

> 元ページ: `management/api-postprocessing` ｜ 公式ページ: https://kuroco.app/ja/docs/management/api-postprocessing/

API 後処理では、APIのレスポンスを変更できます。

## API 後処理の確認方法
[API]から任意のAPI名をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0f517072eaf34ae0d330aad1d76170c.png)
エンドポイント一覧より、後処理を設定したいエンドポイントの [後処理] をクリックします。 

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f76d974ea277ac3efa5a333c094092c8.png)
[追加する][保存する]ボタンが表示されますので、[追加する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4f5caa99f3879d29ea2e8e5b1a952e49.png)
選択肢が表示されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/195b6cd9a5fa2fafe731ca955990316b.png)
### ブロックタイプ
| タイプ   |　説明 |
| :--- | :--- |
|  出力許可リスト  |  選択したフィールドのみレスポンスに表示します。<br/>ネストされたフィールドは `.` を使用します。(例： `data.content.title`)<br/>それぞれのList Indexを指定する必要はなく、サブフィールド名を指定するだけでList項目は自動的に処理されます。例えば、`list.title` は各 `list` 項目の `title`フィールドを返します。 |
|  出力変換リスト  |  機能を使用して、フィールドの名前の変更や削除、データの変更が可能です。<br/>ネストされたフィールドは、`data.content.title` -> `subject` のようにポイント区切りの名前が使用可能です。<br/>FunctionsはPHP、Smarty、RCMSのFunction名と同じ形式です。<ul><li>*Truncate*</li><li>*Trim*</li><li>*Strtotime*</li><li>*Date Format*</li><li>*RCMS Date Format*</li><li>*Uppercase*</li><li>*Lowercase*</li><li>*Sprintf*</li><li>*Nl2Br*</li><li>*FileSize*</li><li>*ImageSize*</li></ul> |
|  カスタム処理  | 作成済みのカスタム処理を選択します。 |

## 関連ドキュメント
- [後処理](/ja/docs/reference/post-processing/)


---

# API セキュリティ

> 元ページ: `management/api-security` ｜ 公式ページ: https://kuroco.app/ja/docs/management/api-security/

APIセキュリティでは、セキュリティの設定ができます。

## APIセキュリティの確認方法
サイドバーよりAPIセキュリティを確認したい［API］をクリックします。
そして、[セキュリティ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b34f0c8a111bd13598907db1faf76645.png)
セキュリティ画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d8c4673a5ac961cb995a04bd4acb5a6.png)

## セキュリティの種類

セキュリティは下記５種類から選択できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4768b87dce7ff52860ef970f29112ac.png)

|セキュリティ   |説明  |
| :--- | :--- |
|なし|アクセス制限なし|
|[静的アクセストークン](#静的アクセストークン)|静的生成されたトークン認証|
|[動的アクセストークン](#動的アクセストークン)|動的生成されたトークン認証|
|[Cookie](#cookie)|Cookieによる認証|
|[特権付き静的トークン](#特権付き静的トークン)|メンバーに紐付いた静的トークン認証|


## 各セキュリティについて

### なし

セキュリティなしの設定です。  
一時的な開発用APIを作成してテストをする場合や、完全にオープンなデータのみ使用する場合などに利用します。

:::note
トークンなしでダイレクトにエンドポイントへのアクセスが可能であるため、基本的には他のセキュリティを選択/設定を検討してください。
:::

### 静的アクセストークン

静的生成されたトークンによる認証方式を設定します。サーバー間通信する場合や公開情報の提供APIなどに利用します。  

静的トークンをリクエストヘッダに指定することで、セキュアなエンドポイントへアクセスできるようにします。

:::note
静的生成されたトークンは意図せずに流出した場合やフロントエンドに組み込まれる想定があるので、トークンの更新を想定したシステム構成にしてください。
:::

### 動的アクセストークン

動的生成されたトークンによる認証方式を設定します。ログインが必要なサイトなどに利用します。  

ログイン認証リクエスト毎にワンタイムトークンを動的生成し、その値をリクエストヘッダに指定することで、セキュアなエンドポイントへアクセスできるようにします。

「動的アクセストークン」の場合は下記3項目が必要となります。
- ユーザーが1人以上登録されている必要があります。
- 必須エンドポイントの作成が必要です。  
- トークンのマネジメント制御をフロントエンドで実装する必要があります。

|必須エンドポイント |カテゴリー |モデル |オペレーション |
| :--- | :--- | :--- | :--- |
|ログイン|認証|Login(v1)|login_challenge|
|トークン|認証|Login(v1)|token|

トークン認証のAPIが複数設定されている場合、
各API間（`api_id`単位）で認証状態は共有されず、APIごとに認証が必要です。

### Cookie

Cookieによる認証方式を設定します。ログインが必要なサイトなどに利用します。

ログイン認証リクエスト毎にCookieを動的生成し、その値をリクエストヘッダに指定することで、セキュアなエンドポイントにもアクセスできるようにします。

「Cookie」の場合は下記2項目が必要となります。
- ユーザーが1人以上登録されている必要があります。
- 必須エンドポイントの作成が必要です。

|必須エンドポイント |カテゴリー |モデル |オペレーション |
| :--- | :--- | :--- | :--- |
|ログイン|認証|Login(v1)|login_challenge|

cookie認証のAPIが複数設定されている場合、各API間（`api_id`が異なる場合でも）で認証状態が共有されます。

また、「Cookie」の場合サードパーティCookieの規制を回避するため、
フロントとKurocoのドメインを合わせる必要があります。  
(ドメインを一致させファーストパーティCookieにさせる必要があります)

### 特権付き静的トークン

特定のメンバーに紐付いた静的トークンによる認証方式を設定します。サーバー間通信で、特定のメンバーの権限でAPIにアクセスする必要がある場合などに利用します。

静的アクセストークンと同様にトークンをリクエストヘッダに指定しますが、トークン生成時に指定したメンバーとしてリクエストが認証されます。  
これにより、ログインや動的トークン生成のフローを経ることなく、メンバーの権限に基づいたAPIリクエスト制限のあるエンドポイントにアクセスできます。

:::note
トークンはメンバーの権限でリクエストを実行するため、適切な権限を持つメンバーを指定してトークンを生成してください。  
また、静的アクセストークンと同様にトークンの流出に注意し、トークンの更新を想定したシステム構成にしてください。
:::

## IPアドレス制限について
指定されたIPアドレスからのアクセスのみ許可します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f03801b763b1150424d1cfab91053a6f.png)

指定方式は下記の通りです。
- IPアドレス指定(例: 192.0.2.1)
- CIDR指定(例: 192.0.2.0/24)
- "-"による範囲指定(例: 192.0.2.1-192.0.2.2)

## 関連ドキュメント
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [静的アクセストークンによるAPIアクセス制限の方法](/ja/docs/tutorials/restricting-api-access-with-statictoken/)
