# Kurocoドキュメント: チュートリアル / API・カスタム処理（1/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- エンドポイントの設定方法（`configure-endpoint`）
- カスタム処理と紐づいたAPIエンドポイントを作成する（`creating-a-custom-function-endpoint`）
- ファイルマネージャーのファイルを自動で削除する（`delete-filemanager-files-by-using-smarty-plugins`）
- カスタム処理を利用して、コンテンツ追加時にメールを送信する（`how-to-implement-original-function-into-the-middle-of-processing-by-using-function`）
- カスタム処理を利用して、CSV出力されるデータ構造を変更する（`how-to-implement-original-function-into-the-postprocess`）
- カスタム処理を利用して、APIに独自のバリデーションを実装する（`how-to-implement-original-validation-in-api-by-using-function`）
- カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える（`how-to-overwrite-request-for-api-main-process-by-using-function`）
- Kurocoのバッチ処理を利用する（`how-to-use-batch`）
- Swagger UIを利用して、APIのセキュリティを確認する（`how-to-use-swagger-ui`）
- エンドポイント設定後の注意点（`points-to-note-after-endpoint-configuration`）


---

# エンドポイントの設定方法

> 元ページ: `tutorials/configure-endpoint` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/configure-endpoint/
> 概要: Kurocoではエンドポイントを独自に複数作成することができます。このチュートリアルでは、エンドポイントの説明と、エンドポイントの作成方法を紹介します。

Kurocoではエンドポイントを独自に複数作成できます。  
このチュートリアルでは、エンドポイントの説明と、エンドポイントの作成方法を紹介します。

## エンドポイントとは何か
エンドポイントとは、Kurocoが外部に公開している機能を識別するURLの事です。

例えばKurocoでお知らせ記事を管理し、Webサイトにその一覧を表示したい場合、WEBサイトはKurocoからお知らせ記事一覧を取得する必要があります。

このとき、Kurocoは「このURLにアクセスされたらお知らせ記事の一覧を返す」というURLを準備しなければなりません。このURLがエンドポイントです。

### APIとエンドポイントの違い
エンドポイントに似た言葉でAPIというものがあります。  
APIとは「Application Programming Interface」の頭文字で、外部に機能を提供するインターフェースを指します。

Kuroco ではAPIという単語を、関連している複数のエンドポイントをグルーピングしたものを示す概念として定義しています。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/677112de0d92ce9c351a40b40d1aaf8b.png)
### APIをどの様に分けるべきか
KurocoではAPI単位にセキュリティの設定やCORSの設定の設定をおこないます。  
そのため、下記の様な基準でAPIを分けることを推奨します。
- 同じ外部システムから呼び出されるもの
- 認証方法が同様な複数の外部システムから呼び出されるもの

## エンドポイントの作成方法
それでは、実際にエンドポイントを作成してみましょう。  
今回は、下記にて記事グループが作成されている想定で、一覧を取得するエンドポイントを設定します。
- グループID：1
- グループ名：お知らせ

### 1. 設定方法の概要
管理画面のAPIメニューからAPI一覧画面を開きます。  
サイドメニューより、[API] -> [Default]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0528fc5ddce491cfac9ecd7631944d78.png)

[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3fbe1a785f908f02f3966be2b7aa6423.png)

エンドポイント作成画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c3b68a3db18ce2594e47bcde1267245.png)

### 2. パス - URIを決める
パスを設定します。今回は `news` と入力します。  
有効/無効は「有効」とします。

:::tip
Kurocoでは、パスの先頭は必ず /rcms-api/X/ となります。  
X は整数が入り、APIのIDになります。
それ以降の部分をテキストフォームで記入します。  
:::

### 3. 操作対象となるコンテンツと操作を決める 
次にコンテンツを決めて行きます。「モデル」で以下を選択します。
- カテゴリー: コンテンツ
- モデル：Topics, v1
- オペレーション：list

サマリーとディスクリプションは任意となります。エンドポイントの概要を分かりやすくを書いてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/434a1b9d92e2f23c8bad5dc453b804d7.png)

### 4. 基本設定を設定する
エンドポイントの設定には多数の設定項目がありますが、ここでは下記２点のみ設定します。

- topics_group_id：1
- cnt：10

topics_group_id にはお知らせの記事グループIDである「1」を入力します。  
cntは１ページあたりの記事数を入力します。ここでは「10」と入力してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/341ab34bbad6a8f7520e8e87322e378f.png)

入力したら最下部の「追加する」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2f52e4431535176f11d2971719ce981.png)

## 設定したエンドポイントの確認をする

設定したエンドポイントを確認します。  
API一覧画面内パンくずリストのプルダウンより [Swagger UI] をクリックします。Swagger UI画面を表示します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/642cd6bc8d579ea990af5327de23c22c.png)

Swagger UI画面が表示されるので、作成したエンドポイントをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/16ca8e6410d930d2565d778ab3dd95a9.png)

エンドポイントの情報が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ebae5bfdff8605b72555269f59bef57c.png)

以上でエンドポイントの作成を終わります。

:::caution
エンドポイントの設定が適切にされてない場合、意図せず情報が公開されてしまう恐れがあります。
詳細な設定については、[エンドポイント設定後の注意点](/ja/docs/tutorials/points-to-note-after-endpoint-configuration/)をご確認ください。
:::

## 関連ドキュメント
- [API](/ja/docs/management/api-list/)
- [エンドポイント設定後の注意点](/ja/docs/tutorials/points-to-note-after-endpoint-configuration/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)


---

# カスタム処理と紐づいたAPIエンドポイントを作成する

> 元ページ: `tutorials/creating-a-custom-function-endpoint` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/creating-a-custom-function-endpoint/
> 概要: カスタム処理を利用することで、APIエンドポイントの標準機能だけでは実現が難しい処理を自由に追加できます。そのため、様々なユースケースに柔軟に対応できます。

Kurocoではカスタム処理と紐づいたエンドポイントの作成ができます。  

## カスタム処理を利用することのメリット

カスタム処理を利用することで、APIエンドポイントの標準機能だけでは実現が難しい処理を自由に追加できます。そのため、様々なユースケースに柔軟に対応できます。

例として、下記対応が可能です。

- リクエスト/レスポンス内容を変更する
- APIへの処理をフックする
- 独自のセキュリティ制御を実装する

このチュートリアルでは、カスタム処理とエンドポイントを紐付ける方法を紹介します。

## GETエンドポイントとカスタム処理を作成する

まずはGETエンドポイントの例を紹介します。  
ここでは例として、`PlainCustomFunction`という名前のカスタム処理をAPIエンドポイントと紐付けます。

### GETエンドポイントを作成する

カスタム処理と紐づけるためのエンドポイントを作成します。

エンドポイント一覧画面より、[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3575edd6842b897a0891f2e915d44ae.png)

今回は下記のように作成しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7c13eb6d5f69f74dce3b43a1c8f81ffa.png)

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス |  | plain-custom-endpoint |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | API |
|  | モデル | Api、v1 |
|  | オペレーション | request_api |
| サマリー(任意) |  | PlainCustomFunction<br/>**注：わかりやすい名前を記載してください。後に作成するカスタム処理名の記載を推奨します。**|
| ディスクリプション(任意) | | PlainCustomFunctionと紐づくGETエンドポイントです。<br/>**注：わかりやすい説明を記載してください。カスタム処理の意図/機能の記載を推奨します。** |
| 基本設定 | name | PlainCustomFunction<br/>**注:後に作成するカスタム処理のslugを指定します。** |

:::tip
`use_path_param`のパラメータを有効にすると、`/rcms-api/1/external_api/{data_id}`のようにパスパラメータを受け付けます。   
詳しい使い方は以下のドキュメントを参照してください。
- [コンテンツカテゴリ毎にキャッシュがクリアされるリストのエンドポイントを作成する](/ja/docs/tutorials/create-an-endpoint-that-clears-the-cache-by-content-category/)
:::

### GETエンドポイント用のカスタム処理を作成する

次に、作成したGETエンドポイント用のカスタム処理を作成します。

カスタム処理一覧画面より、[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1b6ae7314d42c39585003d6f7be8747.png)

下記の設定で作成します。

|項目   |説明  |
| :--- | :--- |
|タイトル|PlainCustomFunction|
|カテゴリ|未分類|
|識別子|PlainCustomFunction|
|処理|下記ソースコードの内容を記載してください。|
|ステータス|有効|

```php [ソースコード]
{assign var="data" value=”Hello!"}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f107c02050a5ef0d676796092c51adc.png)

#### request_api に使用できる変数

| 変数名 | 型 | 説明 |
| :--- | :-- |:-- |
| `$data` |object|この変数に代入した値は、dataの項目でレスポンスされます。|
| `$errors` |object| この変数に値を代入すると、エンドポイントがエラーを返します。代入した値はレスポンスのmessage項目になります。 |
| `$http_code` |int| この変数に値を代入すると、元のHTTPコードを上書きします。|

#### 利用可能なHTTPコード

| コード | 名称 | 意味 |
|---|---|---|
| 202 | Accepted | リクエストは受理されたが、処理はまだ完了していない |
| 204 | No Content | リクエストは成功したが、レスポンスボディを返さない |
| 400 | Bad Request | クライアントからのリクエストが不正 |
| 401 | Unauthorized | ユーザー認証が無い（未ログイン）ことによるリクエスト失敗 |
| 403 | Forbidden | コンテンツへのアクセス権が無いためにリクエスト失敗（401とは異なりユーザー認証は完了している） |
| 404 | Not Found | 指定されたエンドポイントのコンテンツが存在しないことによるリクエスト失敗 |
| 405 | Method Not Allowed | 許可されていないHTTPメソッドを使用した場合のエラー |
| 406 | Not Acceptable | リクエストの条件に合うレスポンスをサーバーが生成できない場合のエラー |
| 500 | Internal Server Error | クライアントからのリクエストは正しいが、サーバ側でエラーが発生した場合のエラー |

### GETエンドポイントの動作確認をする
それでは、作成したエンドポイントの動作確認をします。
今回はSwaggerUI画面から確認します。

エンドポイント一覧画面より、[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acbad196996fa49f8cb397ee57043779.png)

先ほど作成した、`plain-custom-endpoint`をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bf2e11f4ec95f599bdd08306f503b07d.png)

[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee2f9afff4259d287f4c71b89ba6891d.png)

[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e50cc6ed6cd5406cd5f68732afcbb766.png)

すると、Response bodyにカスタム処理で作成した内容が表示されていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6be0b94c5365c54a7645dcb3646ec4a.png)

以上で、GETエンドポイントとカスタム処理の紐付け完了です。

## POSTエンドポイントとカスタム処理を作成する

次に、POSTエンドポイントの例を紹介します。
ここでは例として、`PlainCustomFunctionPost`という名前のカスタム処理を作成することとし、サマリー/ディスクリプションに説明例を記載しています。

### POSTエンドポイントを作成する

カスタム処理と紐づけるためのエンドポイントを作成します。

エンドポイント一覧画面より、[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3575edd6842b897a0891f2e915d44ae.png)

今回は下記のように作成しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14c1425338231e514eda928a7b5525be.png)

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | | plain-custom-endpoint-post |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | API |
|  | モデル | Api、v1 |
|  | オペレーション | request_api_post |
| サマリー(任意) |  | PlainCustomFunctionPost<br/>**注：わかりやすい名前を記載してください。後に作成するカスタム処理名の記載を推奨します。**|
| ディスクリプション(任意) | | PlainCustomFunctionPostと紐づくPOSTエンドポイントです。<br/>**注：わかりやすい説明を記載してください。カスタム処理の意図/機能の記載を推奨します。** |
| 基本設定 | name | PlainCustomFunctionPost<br/>**注:後に作成するカスタム処理のslugを指定します。** |

### POSTエンドポイント用のカスタム処理を作成する

次に、作成したPOSTエンドポイント用のカスタム処理を作成します。

カスタム処理一覧画面より、[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/08a285b9d60e2d3af4c3ba7132ed5d17.png)

下記の設定で作成します。

|項目   |説明  |
| :--- | :--- |
|タイトル|PlainCustomFunctionPost|
|カテゴリ|未分類|
|識別子|PlainCustomFunctionPost|
|実行内容|下記ソースコードの内容を記載してください。|
|ステータス|有効|

```php [ソースコード]
{assign var="message" value="Hello "|cat:$smarty.post.name}
{assign var="data" value=$message}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e50ec88f28d481172ae1f5ed2c1b4479.png)

#### request_api_post に使用できる変数

| 変数名 | 型 | 説明 |
| :--- | :-- |:-- |
| `$data` |object|この変数に代入した値は、dataの項目でレスポンスされます。|
| `$errors` |object| この変数に値を代入すると、エンドポイントがエラーを返します。代入した値はレスポンスのmessage項目になります。 |
| `$http_code` |int| この変数に値を代入すると、元のHTTPコードを上書きします。|

#### 利用可能なHTTPコード

| コード | 名称 | 意味 |
|---|---|---|
| 202 | Accepted | リクエストは受理されたが、処理はまだ完了していない |
| 204 | No Content | リクエストは成功したが、レスポンスボディを返さない |
| 400 | Bad Request | クライアントからのリクエストが不正 |
| 401 | Unauthorized | ユーザー認証が無い（未ログイン）ことによるリクエスト失敗 |
| 403 | Forbidden | コンテンツへのアクセス権が無いためにリクエスト失敗（401とは異なりユーザー認証は完了している） |
| 404 | Not Found | 指定されたエンドポイントのコンテンツが存在しないことによるリクエスト失敗 |
| 405 | Method Not Allowed | 許可されていないHTTPメソッドを使用した場合のエラー |
| 406 | Not Acceptable | リクエストの条件に合うレスポンスをサーバーが生成できない場合のエラー |
| 500 | Internal Server Error | クライアントからのリクエストは正しいが、サーバ側でエラーが発生した場合のエラー |

### POSTエンドポイントの動作確認をする

それでは、作成したエンドポイントの動作確認をします。
今回はSwaggerUI画面から確認します。

エンドポイント一覧画面より、[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acbad196996fa49f8cb397ee57043779.png)

先ほど作成した、`plain-custom-endpoint-post`をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0391a744de33b8c5df7726386462ecc0.png)

[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ac473336dcac698ed232aaa26fba3adc.png)

Response body に以下のように入力します。
```json
{
  "name": "Kuroco"
}
```

[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/250e183d16768c7f3aa8ccf31eb3093c.png)

すると、Response bodyにカスタム処理で作成した内容が表示されていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dfc35c5224f806a35ccc2df8c160c64e.png)

以上で、POSTエンドポイントとカスタム処理の紐付け完了です。

### 任意のリクエスト変数を付与する

上述の通り作成したエンドポイントは任意のリクエスト変数を受け付ける事ができます。  
カスタム処理内でリクエスト変数を扱うには以下のように記述します。

- GET変数 : `$smarty.get.hoge`
- POST変数 : `$smarty.post.foo`
- Cookie変数 : `$smarty.cookie.bar`

また、上記の３つをまとめたリクエスト変数も利用可能です。

- リクエスト変数 : `$smarty.request.piyo`

```php [ソースコード]
{assign var="message" value="Hello "|cat:$smarty.request.name}
{assign var="data" value=$message}
```

#### 正常終了メッセージ・エラーメッセージを返す

レスポンスにエラーメッセージ(`errors`) や正常終了メッセージ(`messages`) を送信したい場合は、カスタム処理にて以下のように記述します。

```smarty [ソースコード]
{assign var="message" value="Hello "|cat:$smarty.post.name}
{assign var="data" value=$message}
{if $smarty.post.name|strlen > 10}
    {append var="errors" value="name should be less than 10 characters."}
{else}
    {append var="messages" value="name is valid."}
{/if}
```

この例では、POST変数`name`に10文字以上の文字列が指定された場合はエラー、それ以外は正常終了メッセージをレスポンスしています。

SwaggerUI画面のRequest bodyに以下のように記載し、[Execute]をクリックしてみましょう。

```json
{
  "name": "Kuroco"
}
```

実行結果（正常終了メッセージ）：
![Image from Gyazo](https://t.gyazo.com/teams/diverta/252b5fed66e614c4a8353e94d8495f50.png)

正常終了メッセージがレスポンスされる事を確認できました。


次にSwaggerUI画面のRequest bodyに以下のように記載し、[Execute]をクリックしてみましょう。

```json
{
  "name": "KurocoDiverta"
}
```

実行結果（エラー）：
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb16431da0b385d05d1605c6025b9ab8.png)

エラーメッセージがレスポンスされる事を確認できました。  

## エンベロープなしのJSONを返す（show_contents）

`request_api`/`request_api_post`のエンドポイントは、デフォルトではテンプレートでassignした`data`変数を`{"data": ...}`形式で返します。  
エンドポイントの基本設定で`show_contents`を有効にすると、テンプレートが出力した文字列をJSONとして解釈し、その値がレスポンス全体になります（`{"data": ...}`のエンベロープなし）。  
`data`のエンベロープを付けずに、任意の形のJSONをそのまま返したい場合に利用できます。

### エンドポイントの設定を変更する

エンドポイント一覧画面より、[GETエンドポイントを作成する](#getエンドポイントを作成する)で作成した`plain-custom-endpoint`の設定を開き、基本設定の`show_contents`を有効にしてエンドポイントを更新します。

<!-- TODO: スクリーンショット: エンドポイント設定画面のshow_contentsチェックボックス -->

### カスタム処理の内容を変更する

`show_contents`が有効の場合、テンプレートはJSONを直接出力する必要があります。  
なお、`{capture}`は囲んだ内容をその場に出力せず変数（`$smarty.capture.xxx`）に格納できるタグで、利用は必須ではありませんが、`show_contents`が無効の場合に[独自のスタブを設定する](/ja/docs/tutorials/setting-up-stubs-on-api-endpoints-using-custom-functions/)チュートリアルのように`data`変数を組み立てる際に利用すると便利です。ただし、テンプレートが何も出力せず`data`変数にassignするだけの書き方では、`show_contents`を有効にするとテンプレートの出力が空になり、レスポンスは`[]`になります。  
出力が空の場合は`[]`が返り、[アプリケーションログ](/ja/docs/management/application-log-list/)にinfoログが記録されます。出力がJSONとして不正な場合は`Contents JSON error`のエラーになります。

カスタム処理の実行内容フィールドに下記を記載し、[更新する]をクリックします。

```smarty [ソースコード]
{literal}{"status":"ok","items":[1,2,3]}{/literal}
```

SwaggerUI画面からこのエンドポイントを実行すると、出力したJSONがそのままレスポンス全体として返されます。

```json
{"status":"ok","items":[1,2,3]}
```

## カスタム処理の実装例について

以上でカスタム処理とAPIエンドポイントの紐付け方法の紹介を終わります。
このチュートリアルではシンプルに紐付けの方法のみの説明にとどめましたが、カスタム処理の実装についてもっと詳しく知りたい場合は、下記ユースケース別のチュートリアルを参照してください。

- [カスタム処理を利用して、APIエンドポイントに独自のスタブを設定する](/ja/docs/tutorials/setting-up-stubs-on-api-endpoints-using-custom-functions/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える](/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/)

## 実行時間の上限

カスタム処理を含む API リクエストは、1リクエストあたり **PHP の実行時間 30 秒**で打ち切られます。カスタム処理の中で `api` プラグインを使って外部 API を呼ぶ場合は、`timeout` を 30 秒未満（例: `timeout=10`）に設定してください。既定値の 30 秒のままだと、外部 API の応答待ちの途中でエンドポイント側が先にタイムアウトします。数十秒かかる外部処理が必要な場合は、カスタム処理で待つのではなく[バッチ処理](/ja/docs/management/batch/)で事前に取り込む構成を検討してください。

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える](/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/)
- [カスタム処理を利用して、APIエンドポイントに独自のスタブを設定する](/ja/docs/tutorials/setting-up-stubs-on-api-endpoints-using-custom-functions/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# ファイルマネージャーのファイルを自動で削除する

> 元ページ: `tutorials/delete-filemanager-files-by-using-smarty-plugins` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/delete-filemanager-files-by-using-smarty-plugins/
> 概要: ファイル操作系のSmartyプラグインを利用して、一定期間前のファイルマネージャのファイルを自動で削除する方法について説明します。

## 概要

ファイル操作系のSmartyプラグインを利用して、ファイルマネージャのファイルを自動で削除する方法について説明します。

今回は、以下のようなバッチ処理を実装します。
1. 特定ディレクトリの配下に存在するファイルの一覧を取得する
2. 最終更新日時が一週間以上前のファイルを削除する
3. 削除したファイル一覧のログをCSV形式で出力し、ファイルマネージャに配置する

### 学べること

以下のファイル操作を行う方法について学ぶことができます。
- 特定ディレクトリ内のファイル情報を取得する
- ファイルを削除する
- ファイルを追加する
- テキストファイルに値を書き込む

### 前提条件

- [Smarty v2](https://www.smarty.net/docsv2/ja/)の基本的な構文がわかること
- [バッチ処理](/ja/docs/management/batch/)の使い方がわかること

## 対象のディレクトリを準備する
[ファイルマネージャー](/ja/docs/management/file-manager/)に以下の構成でディレクトリを作成します。

```
files/ltd
`-- file_plugins_tutorial
    |-- assets # 削除対象のファイルを配置するディレクトリ
    `-- logs   # 削除ログファイル(CSV)を配置するディレクトリ
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e04d84e00f42d8d0fd17d289c5248060.png)

## ファイルの削除処理を実装する
### バッチ処理を新規作成する
[バッチ処理](/ja/docs/management/batch/)を新規作成します。  
まずはファイルの削除処理を実装していきます。  

[オペレーション] -> [バッチ処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d7157130e402e302a1555ed76cab1eb.png)

[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/040171bcbc0837f310ac4cd096ee244b.png)

バッチ処理の編集画面が開くので、以下を設定します。  

|項目|値|
|:--|:--|
|タイトル|file_plugins_tutorial|
|識別子|file_plugins_tutorial|
|タイプ|毎日 02:00|
|処理|以下のコード|

```smarty title="file_plugins_tutorial"
{* Set the timestamp for comparison *}
{assign var='timestamp_to_compare' value='-1 week'|strtotime}

{* Read each file in the directory *}
{read_dir name='files_user' path='/files/ltd/file_plugins_tutorial/assets' file_var='file_info' type='file' recursive=true}
    {* Get the file's update timestamp *}
    {assign var='timestamp_updated_at' value=$file_info.mtime}
    {* Compare the timestamps *}
    {if $timestamp_updated_at < $timestamp_to_compare}
        {* If the update timestamp is over a week ago, delete the file *}
        {remove_file status_var='status' path=$file_info.path}
    {/if}
{/read_dir}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/38f1da2a367028f005a55a4cab96b5ee.png)

設定ができたら[追加する]をクリックしてバッチ処理を追加します。  

:::info
read_dirプラグインのパラメータ詳細は[Smartyプラグイン](/ja/docs/reference/smarty-plugin/#read_dir)のドキュメントを参照してください。
:::

### ファイルの削除処理を動作確認する
バッチ処理の準備ができたら早速動作の確認をします。  
バッチ処理の編集画面から[すぐに実行する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/259c0befb3fe39a294f20239fd092f65.png)

バッチ処理が実行され最終更新日時が一週間以上前のファイルが削除されます。  

:::tip
すぐに確認がしたい場合は以下の`'-1 week'`部分を`'-1 hour'`や`'now'`等に変更して確認してください。  
`{assign var='timestamp_to_compare' value='-1 week'|strtotime}`
:::

## ログファイルの出力処理を追加する
次に、ファイルを削除した際にログファイルを保存する記述を追加します。  

### バッチ処理を更新する
バッチ一覧のページでタイトルをクリックし、先ほど追加したバッチ処理を開きます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/89b8c1f1c9f3176f1e6b8f1b7a24ffbb.png)

処理にログファイルの出力処理を追記します。  
処理の全体は以下のようになります。  

```smarty reference title="file_plugins_tutorial"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/batch_processing/automatically_delete_files_older_than_one_week.txt
```

設定ができたら[更新する]をクリックし、更新を反映します。

:::info
write_file, date, put_fileの詳細は[Smartyプラグイン](/ja/docs/reference/smarty-plugin/)を参照してください。
:::

### ログファイルの出力処理を動作確認する
バッチ処理の編集画面から[すぐに実行する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/259c0befb3fe39a294f20239fd092f65.png)

バッチ処理が実行され最終更新日時が一週間以上前のファイルが削除され、ログがlogsディレクトリに残ります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/36808c786df498c67018050a502e291c.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9a1d2f6f55096771defc0f6ac757c719.png)

:::tip
すぐに確認がしたい場合は以下の`'-1 week'`部分を`'-1 hour'`や`'now'`等に変更して確認してください。  
`{assign var='timestamp_to_compare' value='-1 week'|strtotime}`
:::

以上で、設定と確認が完了しました。  
ファイル容量の管理に是非ご利用ください。

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# カスタム処理を利用して、コンテンツ追加時にメールを送信する

> 元ページ: `tutorials/how-to-implement-original-function-into-the-middle-of-processing-by-using-function` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-original-function-into-the-middle-of-processing-by-using-function/

カスタム処理を使用して、特定の処理の途中で独自の処理を実行する方法を解説します。
この機能を利用すると、標準機能以外でのタイミングで通知を送信したりデータ登録ができます。

今回は、新しくコンテンツが追加された時にメールで通知をする処理を実装します。

## カスタム処理を作成する
それではカスタム処理を作成します。

### 1. カスタム処理の一覧画面を表示する  
メニューの[オペレーション] -> [カスタム処理] をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fc571fc550915a05f0c13d0508e9f6.png)

### 2. カスタム処理の編集画面を表示する 
カスタム処理一覧画面の右上の [追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9998b0797d2ae3e08dd1c0ffde72420c.png)
すると、カスタム処理編集画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fcc8d76f9247345f734858139362b6cf.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ce36fad667a7f35efa0bc8d5f6dc3e74.jpg)

### 3. タイトル・識別子を記入する
それではカスタム処理を作成していきます。  
まずはタイトルと識別子に記入します。今回は下記のように記入します。

- タイトル：コンテンツ投稿後にメールを送信する
- 識別子：sample1_trigger

:::tip
タイトル・識別子は他のカスタム処理と重複できません。
実装対象のエンドポイント名など、他と重複しない内容で記入してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb929c51d437b8da796be4ce19880262.png)
### 4. これを使ったコンポーネントを記入する
次にカスタム処理を使ったコンポーネントを記入します。  
今回は下記のように記入します。

- トリガー：コンテンツの追加後
- テキストフィールド：19

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e077d94ebe41765bcf7fdf84cdce8f23.png)
:::caution
テキストフィールドには「19」と記入していますが、こちらにはコンテンツ定義の「グループID」を記入します。 
今回は[コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)にて作成した「お知らせ」コンテンツの追加後にメールを送るため「19」を記入しておりますが、こちらはご自身の環境により修正をお願いします。
:::

**参考: コンテンツ定義一覧画面**  
グループIDは、コンテンツ定義一覧画面で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/55f5ff98f1cdf374437fc9bfc36bf6d5.png)

### 5. メール送信処理を記述する
次に、メール送信処理を記述します。

エディタ内にメール送信処理を記述していきます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/65e34913bddaeb4825d3605a56a22e88.png)
**メールを作成する処理を実装する**  
まずは、メールタイトル・本文を作成します。  

利用できる変数は下記となります。

| 変数名 | 型 | 説明
| :--- | :--- | :--- |
| topics_id |int | コンテンツID |

エディタに下記記入します。

```smarty
{*コンテンツデータ取得*}
{assign_array var='method_params'                  values=''}
{assign_array var='method_params.topics_group_id'  values=''}
{assign       var='method_params.topics_group_id.' value=19}{* トリガー設定時に指定したコンテンツ定義のIDを設定 *}
{assign       var='method_params.cnt'              value=1}
{assign_array var='method_params.topics_id'        values=''}
{assign       var='method_params.topics_id.'       value=$topics_id}
{assign       var='method_params.ignore_open_flg'  value=1}{* 非公開データでも取得出来るように指定する *}
{api_method
    var='topics_list'
    model='Topics' method='list' version='1'
    method_params=$method_params}
{assign var='topicsData' value=$topics_list.list.0}

{* タイトル *}
{assign var=mail_subject value=$topicsData.subject}
{* 本文 *}
{capture name=mail_body}
お知らせが追加されました。

詳細はこちらから確認してください。
{$smarty.const.ROOT_MNG_URL}/management/topics/topics_edit/?topics_id={$topicsData.topics_id}
{/capture}
{assign var=mail_body value=$smarty.capture.mail_body}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8cc7129c74c69546a3d32b6765dbed5.jpg)

**メールを送信する処理を実装する**  
次にメールを送信する処理を作成します。
エディタに下記を追記します。

```smarty
{sendmail 
 to='YOUR_MAIL_ADDRESS@example.com'
 subject=$mail_subject
 contents=$mail_body}
```

:::caution
`YOUR_MAIL_ADDRESS@example.com` には送信先のメールアドレスを記入してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a337caa27a8f005cc8113e4eba45842.jpg)

### 6. カスタム処理を保存する 
処理の記述が完了したら、[追加する] ボタンをクリックして保存します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c408c383626b5ed0fe76e0ff3ee90b5.png)
以上でカスタム処理の完成です。

## メール送信の確認
作成したカスタム処理の動作を確認します。  
設定したコンテンツ定義（今回の場合グループIDが19のコンテンツ定義）より、[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/261c5f5d0acf0792e67eb5716ad69f23.png)

コンテンツ内容を記入し、[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b75dc50bcbda67b3d175b78f0d267bd0.png)
すると、カスタム処理に記載したメールアドレスへメールが届きます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/69d160540f1539be17014d91c184e5d2.png)
以上です。

## メールが送信されない場合の確認ポイント
メールがうまく送信されない場合、下記ドキュメントをご参照ください。  
- [メールが送信できない場合の確認方法を教えてください](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)

## 注意点
呼び出し元が重複するカスタム処理を作成できません。
今回の場合、呼び出し元では下記を設定しております。
- トリガー：コンテンツの追加後
- テキストフィールド：19
そのため、別のカスタム処理で上記の呼び出し元を利用できませんのでご注意ください。

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [コンテンツの特定項目が更新されたらメールで通知する](/ja/docs/tutorials/notify-by-email-when-specific-items-in-the-content-are-updated/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [コンテンツ更新後のトリガが二重に呼ばれるのはなぜですか？](/ja/docs/faq/why-is-the-trigger-called-twice-after-content-update/)


---

# カスタム処理を利用して、CSV出力されるデータ構造を変更する

> 元ページ: `tutorials/how-to-implement-original-function-into-the-postprocess` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-original-function-into-the-postprocess/
> 概要: カスタム処理を利用して、APIがCSV形式で出力する記事一覧データに、管理画面の編集ページへのURLを追加する方法を説明します。

## 概要
カスタム処理を使用して、APIが標準で出力するデータを加工できます。
今回は、CSV形式で出力される記事一覧データに管理画面編集ページへのURLを追加します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0d1d3b99b1a62aa587fb09570461c03.png)

### 学べること
APIを利用したCSV出力を以下の手順で加工します。
- [カスタム処理を作成する](#カスタム処理を作成する)
- [エンドポイントにカスタム処理を登録する](#エンドポイントにカスタム処理を登録する)

### 前提条件
このチュートリアルでは、コンテンツ一覧のエンドポイントに後処理でカスタム処理を適用し、対象のエンドポイントがCSV形式でレスポンスを返した場合にカスタム処理を実行します。  
エンドポイントからCSV形式でレスポンスを得る方法は以下のドキュメントを参照ください。  
- [APIをJSON以外のフォーマットでレスポンスできますか？](/ja/docs/faq/how-can-i-response-csv-format)

## カスタム処理を作成する
それではカスタム処理を作成します。

### 1. カスタム処理の一覧画面を表示する  
メニューの[オペレーション] -> [カスタム処理] をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fc571fc550915a05f0c13d0508e9f6.png)

### 2. カスタム処理の編集画面を表示する 
カスタム処理一覧画面の右上の [追加] をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9998b0797d2ae3e08dd1c0ffde72420c.png)

すると、カスタム処理編集画面が表示されます。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fcc8d76f9247345f734858139362b6cf.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ce36fad667a7f35efa0bc8d5f6dc3e74.jpg)

### 3. タイトル・識別子を記入する
それではカスタム処理を作成していきます。  
まずはタイトルと識別子に記入します。今回は下記のように記入します。

- タイトル：コンテンツCSV編集
- 識別子：sample1_postprocess
- トリガー: 未指定

:::tip
タイトル・識別子は他のカスタム処理と重複できません。
実装対象のエンドポイント名など、他と重複しない内容で記入してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/316c33b217f6cb89e108821fb74f25e8.png)

### 4. データ操作処理を記述する
次に、実際の処理を記述します。

エディタ内にデータを追加する処理を記述していきます。

**コンテンツIDを取得する処理を記述する**  
まずは、コンテンツIDを取得するためにヘッダー行を読み取ります。  

利用できる変数は下記となります。

| 変数名 | 型 | 説明
| :--- | :--- | :--- |
|$json.csv_data |object |コンテンツデータ|

エディタに下記記入します。

```smarty
{assign_array var=processed_list values=""}

{* CSVの場合 *}
{if $json.csv_data}
    {foreach from=$json.csv_data item=row name=csv_data}
        {if $smarty.foreach.csv_data.index eq 0}{* ヘッダー行 *}
            {foreach from=$row item=header_title name=header_data}
                {if $header_title eq 'コンテンツID'}
                    {* コンテンツID列を取得 *}
                    {assign var=contents_id_col_index value=$smarty.foreach.header_data.index}
                {/if}
            {/foreach}
            {append var=row value="編集ページURL"}
        {else}{* データ *}
            {assign var=url value=$smarty.const.ROOT_MNG_URL|cat:'/management/topics/topics_edit/?topics_id='|cat:$row.$contents_id_col_index}
            {append var=row value=$url}
        {/if}
        {append var=processed_list value=$row}
    {/foreach}
    {assign var=json.csv_data value=$processed_list}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e6c4bb3a588384b6af520717d4f4206e.png)

**編集したデータを出力する**  

| 変数名 | 型 | 説明
| :--- | :--- | :--- |
|$processed_json |object |コンテンツデータ|

```smarty
{assign var=processed_json value=$json}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/96daec2f0dfa4d15f8511b0081babba7.png)

### 6. カスタム処理を保存する 
処理の記述が完了したら、[追加する] ボタンをクリックして保存します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c408c383626b5ed0fe76e0ff3ee90b5.png)
以上でカスタム処理の完成です。

## エンドポイントにカスタム処理を登録する
作成したカスタム処理をエンドポイントの後処理に追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acfbbdf901602d7c17f523da04f43867.png)

詳しくは、[API後処理](/ja/docs/management/api-postprocessing/)を参照してください。

## 動作確認
以下の手順で動作確認をします。  

### 1. CSVファイルをダウンロードする。  
設定したカスタム処理はCSVで出力した場合に動作するので、`_output_format=csv`のクエリパラメータを付けてエンドポイントにアクセスします。
上記でカスタム処理を登録したAPIエンドポイントへアクセスし、CSVファイルをダウンロードします。
`https://[サイトキー].g.kuroco.app/rcms-api/**/topics/download?topics_group_id=**&_output_format=csv`  

以下3点はご自身のサイトのものを入力してください。  
- `https://[サイトキー].g.kuroco.app`  
  サイトのAPIドメインを入力して下さい。  
  [環境設定] > [アカウント設定]の画面で確認ができます。
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/1a2ad3982ce6e56971e74c63c3d717e0.png)

- `/rcms-api/**/topics/download`  
  [エンドポイントにカスタム処理を登録する](#エンドポイントにカスタム処理を登録する)のステップでカスタム処理を登録したAPIエンドポイントを入力して下さい。  

- `topics_group_id=**`  
  一覧にしたいコンテンツ定義のIDを`**`に入力して下さい。IDはコンテンツ定義一覧の画面から確認できます。
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/724b673e5e6e60d55c26525a08b7d4c2.png)

### 2. ファイルの内容を確認する。
CSVがUTF-8で保存されるので、メモ帳で開く、もしくはエクセルでインポートして、「編集ページURL」の列が追加されていることを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2ccf5352ffa8a65d3512eb62669b8187.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ceba2a9e334b5057b28fa3fda9ca03a1.png)

以上で本チュートリアルは完了です。

## 注意点
出力するデータが大きくなる場合、メモリオーバーエラーやタイムアウトの発生する可能性があります。
この場合はバッチ処理化をご検討ください。

## 関連ドキュメント
- [API後処理](/ja/docs/management/api-postprocessing/)
- [バッチ処理を使用して、CSVで日次データを保存する](/ja/docs/tutorials/how-to-implement-batch-function-exports-csv/)
- [APIをJSON以外のフォーマットでレスポンスできますか？](/ja/docs/faq/how-can-i-response-csv-format)


---

# カスタム処理を利用して、APIに独自のバリデーションを実装する

> 元ページ: `tutorials/how-to-implement-original-validation-in-api-by-using-function` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/
> 概要: カスタム処理とAPI前処理を使用して、APIに独自のバリデーション処理を実装する方法を解説します。この機能を利用すると、標準機能のみでは実現できない複雑な入力チェックを追加することができます。

カスタム処理とAPI前処理を使用して、APIに独自のバリデーション処理を実装する方法を解説します。
この機能を利用すると、標準機能のみでは実現できない複雑な入力チェックを追加できます。

今回は、POSTされたメールアドレスが特定のドメインと一致しなければエラーを返すバリデーション処理を実装します。

## 事前準備

### APIエンドポイントを作成する
まず、[エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)を参考にバリデーション処理を実装するAPIエンドポイントを作成します。
今回は「Default」のAPIに以下のエンドポイントを作成しました。

| 設定項目 | 設定       |             |
| :------- | :------- | :------- |
| パス | original_api/sample1 |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | 配信 |
|  | モデル | Magazine |
|  | オペレーション | Subscribe |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8db35933282272deaf2d5f3c8f4423a3.png)

## カスタム処理を作成する
バリデーション処理を記述するためのカスタム処理を用意します。

### カスタム処理の一覧画面を表示する  
メニューの[オペレーション] -> [カスタム処理] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/baddc3d7091c3a34bed2af152ec984ec.png)

### カスタム処理の編集画面を表示する 
カスタム処理一覧画面の右上の [追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/488c4ee6513ef4938e7d73c444b68905.png)

### タイトル・カテゴリを入力する
カスタム処理のタイトルとカテゴリを入力します。  
今回は下記のように入力しました。
- タイトル：/rcms-api/1/original_api/sample1
- カテゴリ：api
- 識別子：sample1_function

:::tip
同一カテゴリ内にタイトルが重複する処理を作成できないため、実装対象のエンドポイント名など、他と重複しないタイトルを命名してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1259638440c9aac9e1c4d0bb068e6c84.png)
### カスタム処理を保存する  
一旦ここまでで保存します。
画面下部までスクロールし、[追加する] ボタンをクリックして保存します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c2ff9f821fa872259c3f77feeac49a2.png)


## バリデーション処理を記述する
次に、バリデーション処理を記述します。

### カスタム処理編集画面を表示する 
サイドメニューより[オペレーション]を選択し、[カスタム処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/baddc3d7091c3a34bed2af152ec984ec.png)

先ほど追加したカスタム処理のタイトルをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5e72d2a08f6e3323ca8cfb9859ce328e.png)

カスタム処理の編集画面に戻り、エディタ内にバリデーション処理を記述していきます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1bc957775ba45ef32fa7991c4cbd16de.png)

### エラー変数を初期化する
バリデーション結果を格納するための$errors変数を初期化します。  

| 変数名 | 型 | 説明|
| :--- | :--- | :--- |
|$errors |array |テキスト配列|

エディタに下記を記入します。

```smarty
{* $errors = [] *}
{assign_array var="errors" values=""}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8febf5f999d216ba78efa163a2eca9f1.png)

### バリデーション処理を実装する
ユーザーの入力値をチェックし、errors変数に結果を代入します。  
入力値を参照するためには、下記のいずれかの変数を利用します。

| 変数名 | 説明 |
| :--- | :--- |
|$smarty.get | クエリパラメータ |
|$smarty.post | JSON body |
|$smarty.request | クエリパラメータ & JSON body |

```smarty
{assign_array var="errors" values=""}

{* [例] POSTされたメールアドレスが特定のドメインと一致しなければエラーを返す *}
{if $smarty.post.email|strpos:'@example.com' === false}
  {* $errors = ["メールアドレスが不正です。"] *}
  {assign var="errors." value="メールアドレスが不正です。"}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f4832e20f4fd343cb4cb0c67c191e4f.png)

### 保存する
処理の記述が完了したら、[更新する] ボタンをクリックし保存してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdd128a4f2f5cafbb30306da8b4ee7de.png)
## APIにカスタム処理を関連付ける
次に作成したカスタム処理をAPIに関連付けます。  

### API一覧画面を表示する
[API] ->[Default] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a18960024a9f08e2b2cadf906b9d3fd7.png)

### エンドポイントを選択する
事前準備で作成したエンドポイント`/rcms-api/1/original_api/sample1`の[前処理]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9cc61b8ff106fb3e961333fbaf2d3f5e.png)

テーブルの下に、「カテゴリ」と「一覧」プルダウンが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/35eb8a3f0ed1176a8aeabd36216f5ff6.png)

### カスタム処理を関連付ける
カスタム処理の選択プルダウンが表示されます。  
先ほど作成しておいたカスタム処理のカテゴリとタイトルを選択します。

- カテゴリ：API
- 一覧：/rcms-api/1/original_api/sample1

![Image from Gyazo](https://t.gyazo.com/teams/diverta/de901fe59dd1cb005394c124eb116502.png)

## APIの動作を確認する
Swagger UI画面からリクエストを行い、バリデーション処理の動作を確認します。

### Swagger UI画面を表示する

API一覧画面より [Swagger UI] をクリックし、Swagger UI画面を表示します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7d703b484b76c1bc1256cd155f9fc2f0.png)

### エンドポイントを選択する
バリデーション処理を実装したエンドポイント`/rcms-api/1/original_api/sample1`を選択し、[Try it out] ボタンをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94a54257d064cd18157eb0f13aad1221.png)

### エラーが出力される値を入力する
`magazine_id`に`1`を入力し、バリデーション処理を確認するため、下記の通り、エラーが出力される値を[Request body]に入力します。

```json title="Request&#x20;body"
{
  "email": "test@test.com"
}
```

入力が完了したら、[Execute] ボタンをクリックし、リクエストを実行します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5dbc1003c962886422334e65f90350a.png)

### レスポンスを確認する
APIのレスポンス内容を見て、想定通りのエラーが出力されることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d7bb3fbbd905fa9d79cd29af682b53c.png) 

```json [response]
{
  "errors": [
    {
      "code": "unprocessable_entity",
      "message": "メールアドレスが不正です。"
    }
  ],
  "x-rcms-request-id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxx"
}
```

以上でカスタム処理とAPIの関連付けが完了です。  

## バリデーションエラーが発生しない場合の確認ポイント
入力チェックが想定通りに行われない場合は、下記のポイントを確認してください。
- APIの前処理とカスタム処理が関連付いているか
- 関連付いているカスタム処理が正しいか
- 変数名(errors)が正しいか
- チェック対象の項目名が正しいか
- バリデーション処理のロジックが正しいか

## コード例の紹介
カスタム処理に利用できるコード例を紹介します。

### 特定の文字列を含むかどうかをチェックする

```smarty
{if $smarty.post.column_name|strpos:"期待する文字列" === false}
  {assign var="errors." value="column_nameが不正です。"}
{/if}
```
<br/>

### 数値かどうかをチェックする

```smarty
{if !$smarty.get.parameter_name|is_numeric}
  {assign var="errors." value="parameter_nameは数値で入力してください。"}
{/if}
```
<br/>

### 特定の項目に依存した入力チェックを行う

```smarty
{*
    [例] ext_col_01に1が入力された場合のみ、ext_col_02を必須項目とする
    ext_col_01: セレクト項目 ('', '1', '2')
    ext_col_02: テキスト項目
*}
{if $smarty.post.ext_col_01 === '1' || (
  !$smarty.post.ext_col_01|@empty &&
  $smarty.post.ext_col_01.key === '1'
)}
  {if !isset($smarty.post.ext_col_02) || $smarty.post.ext_col_02 === ''}
    {assign var="errors." value="テキスト項目は必須項目です。"}
  {/if}
{/if}
```
<br/>

### 特定のグループに所属するメンバーにのみ入力チェックを適用する

```smarty
{if $smarty.session.arrGroup_id|@is_array &&
  101|in_array:$smarty.session.arrGroup_id}
  {if !isset($smarty.post.column_name)}
    {assign var="errors." value="column_nameは必須項目です。"}
  {/if}
{/if}
```
<br/>


### エラー時にレスポンスコードを変更する場合
エラーチェックによってエラー応答する際に、APIのレスポンスコードを  
特定のエラーコードに変更してエラーレスポンスを行いたい場合は下記のように設定します。

```smarty
{assign var=http_code value=404}
```

#### 利用可能なHTTPコード

| コード | 名称 | 意味 |
|---|---|---|
| 400 | Bad Request | クライアントからのリクエストが不正 |
| 401 | Unauthorized | ユーザー認証が無い（未ログイン）ことによるリクエスト失敗 |
| 403 | Forbidden | コンテンツへのアクセス権が無いためにリクエスト失敗（401とは異なりユーザー認証は完了している） |
| 404 | Not Found | 指定されたエンドポイントのコンテンツが存在しないことによるリクエスト失敗 |
| 405 | Method Not Allowed | 許可されていないHTTPメソッドを使用した場合のエラー |
| 406 | Not Acceptable | リクエストの条件に合うレスポンスをサーバーが生成できない場合のエラー |
| 500 | Internal Server Error | クライアントからのリクエストは正しいが、サーバ側でエラーが発生した場合のエラー |

errorsにエラーメッセージを設定する方法と組み合わせることも可能です。  
設定例）

```smarty
{if `エラー判定処理`}
  {assign var=http_code value=404}
  {assign_array var=errors values=''}
  {assign var=errors. value='コンテンツが存在しません'}
{/if}
```

レスポンス例）
```json [response]
HTTP Respnese code: 404

Response body
{
  "errors": [
    {
      "code": "unprocessable_entity",
      "message": "コンテンツが存在しません"
    }
  ],
  "x-rcms-request-id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxx"
}
```

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える](/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/)
- [カスタム処理を利用して、コンテンツ定義に独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-contents-edit-by-using-function/)
- [前処理](/ja/docs/reference/pre-processing/)


---

# カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える

> 元ページ: `tutorials/how-to-overwrite-request-for-api-main-process-by-using-function` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/
> 概要: カスタム処理とAPI Pre-processingを使用して、APIのメイン処理に渡すリクエスト値を書き換える方法を紹介します。

カスタム処理とAPI Pre-processingを使用して、APIのメイン処理に渡すリクエスト値を書き換える方法を紹介します。  

カスタム処理を利用することで、下記のような対応ができます。
- ユーザーの入力値を特定の形式に変換した上でAPIに渡す
- 追加の固定値をAPIに渡す

このチュートリアルでは、フォーム送信APIへのリクエスト時にユーザーが入力した全角数字を半角数字に変換する処理を実装します。

## カスタム処理を作成する
リクエスト書き換え処理を記述するためのカスタム処理を用意します。

### カスタム処理の一覧画面を表示する
サイドメニューより[オペレーション]を選択し、[カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fc571fc550915a05f0c13d0508e9f6.png)

### カスタム処理追加画面を表示する
カスタム処理一覧画面の右上の [追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9998b0797d2ae3e08dd1c0ffde72420c.png)

### タイトル・カテゴリを入力する
カスタム処理のタイトルとカテゴリを入力します。  
今回は下記のように入力しました。
- タイトル：/rcms-api/3/inquiry/3/messages/send
- カテゴリ：Pre-processing
- 識別子：sample2_function

:::tip
同一カテゴリ内にタイトルが重複する処理を作成できないため、実装対象のエンドポイント名など、他と重複しないタイトルを命名してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/98811006f287ee88663d807d8cb7a105.png)

### カスタム処理を保存する
一旦ここまでで保存します。
画面下部までスクロールし、[追加する] ボタンをクリックして保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7a9f5081b0ade550bd5f1f96d4a82b1.png)

## リクエスト値の書き換え処理を記述する
次に、リクエスト値の書き換え処理を記述します。 

### カスタム処理編集画面を表示する 
サイドメニューより[オペレーション]を選択し、[カスタム処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fc571fc550915a05f0c13d0508e9f6.png)

先ほど追加したカスタム処理のタイトルをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/148deb8947cc1f228700150e34284eb7.png)

編集画面内のエディタにリクエスト値の書き換え処理を記述していきます。  

### リクエスト変数を初期化する
リクエスト値を格納するための$request変数を初期化します。  

| 変数名 | 型 | 説明
| :--- | :--- | :--- |
|$request |array |連想配列|


エディタに下記記入します。
```smarty
{* $request = [] *}
{assign_array var="request" values=""}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9d024902057e9db29cc7a4b28dd25481.png)


### リクエスト値の書き換え処理を実装する
ユーザーの入力値を変換し、$request変数に変換後の値を代入します。  
入力値を参照するためには、下記のいずれかの変数を利用します。

| 変数名 | 説明 |
| :--- | :--- |
|$smarty.get | クエリパラメータ |
|$smarty.post | JSON body |
|$smarty.request | クエリパラメータ & JSON body |

入力値の変換には、[mb_convert_kana](https://www.php.net/manual/ja/function.mb-convert-kana.php)を利用します。

下記のように追記します。

```smarty
{assign_array var="request" values=""}

{* [例] POSTされた値の全角数字を半角に書き換える *}
{if isset($smarty.post.ext_01)}
  {assign
    var="request.ext_01"
    value=$smarty.post.ext_01|mb_convert_kana:'n'}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8b3a0562211ce196be329007665282b3.png)

### 保存する
処理の記述が完了したら、[更新する] ボタンをクリックし保存してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdd128a4f2f5cafbb30306da8b4ee7de.png)
## APIにカスタム処理を関連付ける
次に作成したカスタム処理をAPIに関連付けます。  

### API一覧画面を表示する
メニューの[API] をクリックし、エンドポイントを作成するAPIの一覧画面を表示します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/edec43836bdd23fc3bcdce176502a1c6.png)

### エンドポイントを作成する
フォーム送信APIの処理を実装するためのエンドポイントを作成します。  
[新しいエンドポイントの追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00c5593b74b2d0aca84a698fa9f708b5.png)

今回は下記のような設定でエンドポイントを作成しました。

| 親項目 | 子項目 | 値 |
| :--- | :--- | :--- |
| パス | - | inquiry/3/messages/send |
| モデル |カテゴリー |フォーム |
| モデル |モデル | InquiryMessage (v1) |
| モデル |オペレーション | send |
| 基本設定 |id | 3<br/>（こちらには送信対象フォームのIDを記述します。<br/>フォームIDは[フォーム一覧](/ja/docs/management/inquiry-forms/)画面から確認できます) |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b10bd880e9fdc541f263414b091a626c.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a847b8b20f1ebf7c9b35d17939cf7774.jpg)

記入したら[追加する]をクリックして、エンドポイント作成完了です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b23b07b23efc34bded37d3881edb1ea6.png)

### エンドポイントを選択する
API一覧画面より、先ほど作成したエンドポイントの[前処理] ボタンをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8d4b683129be98f4ed0dcd9093a12c85.png)

テーブルの下に、「カテゴリ」と「一覧」プルダウンが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a24336644c86da2635ffd47a04ec12c3.png)

### カスタム処理を関連付ける
エンドポイントとカスタム処理を関連付けます。  
プルダウンより、先ほど作成しておいたカスタム処理のカテゴリとタイトルを選択します。

- カテゴリ：Pre-processing
- コンテンツ：/rcms-api/3/inquiry/3/messages/send

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4049222bb0ae8001f866126039f5faab.png)

## APIの動作を確認する
Swagger UI画面からリクエストを行い、リクエスト書き換え処理の動作を確認します。

### API情報画面を表示する
API一覧画面の[Swagger UI]をクリックし、Swagger UI画面を表示します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/370b8d5684d3403541c61a654cd2252c.png)

### エンドポイントを選択する
作成した「/rcms-api/3/inquiry/3/messages/send」エンドポイントをクリックし、[Try it out] ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa9316fed4f0b4ea4f2892190a6ad3c8.png)

### 全角数字を含む値を入力する  
[Request body]フィールドが記入できるようになるので、全角数字を含む値を [Request body] に入力します。  
今回は　`"ext_01": "string",`の箇所を下記に修正します。
```json title="Request&#x20;body"
{
  ...
  "ext_01": "１２３４５",
  ...
}
```

入力が完了したら、[Execute] ボタンをクリックし、リクエストを実行します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4df314f7cd85e30d2264521349b6eb2.png)

リクエストが成功した場合、下記のようなレスポンスが出力されます。  
後ほど動作確認で使用するため、ここで発行されたidの数値を控えておいてください。
```json title="response"
{
  "errors": [],
  "messages": [
    "新規追加しました。"
  ],
  "id": 2,
  "thanks_tag": ""
}
```

### 保存された値を確認する
サイドメニューより[チャネル] -> [WEB] -> [フォーム] の順にクリックし、フォーム一覧画面にアクセスします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a19c3ed4da661b3cf6cc5d46cee513.png)

先ほど送信したフォームのタイトルをクリックし、フォーム詳細画面にアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c209690fb0cb6432e44608d39c5f9a6e.png)

[回答] タブを選択し、フォームの回答一覧画面にアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/09f91e41f23d10a700bdda512ebee2d8.png)

[No.] 列より、フォーム送信時に発行されていたidを探し出し、数値のリンクをクリックして回答内容画面にアクセスします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/91fa43a950fdf9abfab25e904c243413.png)

リクエスト値を上書きした項目を参照し、値が半角数字に書き換わっていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5768683a946dd99f31387258ee94f825.png)

以上でカスタム処理とAPIの関連付けが完了です。

## 値が書き換わらない場合の確認ポイント
リクエスト値が想定通りに書き換わらない場合は、下記のポイントを確認してください。
- APIのPre-processingとカスタム処理が関連付いているか
- 関連付いているカスタム処理が正しいか
- 変数名(request)が正しいか
- チェック対象の項目名が正しいか
- リクエスト変換処理のロジックが正しいか

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [前処理](/ja/docs/reference/pre-processing/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# Kurocoのバッチ処理を利用する

> 元ページ: `tutorials/how-to-use-batch` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-batch/
> 概要: バッチ処理とは、一定時間ごとに実行される処理です。kurocoでは15分毎、30分毎、1時間毎、毎日のいずれかの頻度でバッチ処理を実行出来ます。

## バッチ処理とは何か
バッチ処理とは、一定時間ごとに実行される処理です。
kurocoでは15分毎、30分毎、1時間毎、毎日のいずれかの頻度でバッチ処理を実行出来ます。

## どのような場面で利用できるか
バッチ処理をシステム利用者が少ない夜間や休日などに実行させることによって、システムの負荷を軽減したり、空きリソースを有効利用させることが出来ます。

また、複数のユーザーが同時に操作することによって急激に高負荷がかかってしまう処理などは、バッチ化することによって処理がキューイングされ、１件ずつ順番で実行されるようになるため負荷を軽減することが出来ます。

例えば以下の様な用途があげられます。
- 外部システムへ連携するためのCSVの生成
- 外部システムからKurocoへファイル連携によってデータを取り込む処理
- ユーザーが退会したあとに、システム内のさまざまなデータを更新する処理
- ログを集計して統計データを算出する

## バッチの作成方法

1日1回CSVファイルを出力するバッチ処理を作成してみましょう。

### 1. バッチ処理の新規作成する
[オペレーション] -> [バッチ処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8157a93cf8baf534df07749ba6eb0c66.png)

バッチ一覧画面上部にある[追加]ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b210a002b7ae8947c060c00b9b56421.png)

タイトル欄にバッチ処理の名前「CSV出力」と、識別子欄に「csv_output」と入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9cddd626272bbc9ce5948c640ad1a24.png)

### 2. バッチ処理の実行頻度を指定する 
バッチ処理欄からバッチの実行頻度を指定します。
Kurocoでは下記のいずれかから選択できます。
- 15分毎
- 30分毎
- 1時間毎
- 毎日

今回は、1日1回実行したいので「毎日」を選択し、その隣のプルダウンから「05:00」を選びます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2acd08e3bdab497cee49a7101edf680f.png)

これで毎朝5:00に実行されるバッチが作成できました。

注意)
「毎日」を選択した場合、前回の最終実行時刻から23時間以上経過していないと処理は実行されません。例えば、動作確認のために「15分毎」に実行し、その直後「毎日」に設定変更したとしても、最終実行時刻は「15分毎」で実行した時刻となります。そこから23時間以内に指定した時刻が訪れる場合、処理はスキップされますのでご注意ください。

### 3. バッチ処理を実装する
「実行内容」にSmarty構文でバッチ処理を記述していきます。

まずは一時ファイルにヘッダー行を出力します。

```smarty
{assign var="csv_header" value="記事ID,カテゴリID,カテゴリ名,件名,本文"} {* 注1 *}
{write_file var=tmp_path value=$csv_header|cat:"\n"} {* 注2 *}
```

注1) assign関数を使って、$csv_headerという変数にCSVのヘッダ行となるカンマ区切りの文字列を保存します。

注2) 続いてその変数を一時ファイルに保存し、ファイル名は$tmp_pathという変数に保存します。write_file関数を使うと自動的にユニークなファイル名を生成してそこに文字を書き出すことが出来ます。

続いて、APIを使って記事一覧を取得します。

```smarty
{assign var=queries value=$dataSet.emptyArray} {* 注3 *}
{append var=queries index=cnt value=0} {* 注4 *}
{api_internal   endpoint='/rcms-api/1/topics-list'
                method='GET'
                member_id=1
                queries=$queries
                var='topics_list_response'
}
```

注3) $queries変数に $dataSet.emptyArray を代入し空配列を準備します。この変数はAPIのクエリー変数として利用します。

注4) つぎにcntというキーに0を代入し,エンドポイント '/rcms-api/1/topics-list' に対してGETメソッドでリクエストを投げます。  
　'/rcms-api/1/topics-list' はあらかじめ記事一覧モジュールを使って作っておいたエンドポイントを想定してます。  
　記事一覧に cnt=0 を渡すとページ分割無しで全記事がレスポンスされます。ここでは簡単にするため、その様にしてますが実際にはメモリーエラーの回避のために適切な数値を設定してください。  
　api_internal関数の member_id 属性に1を渡すと管理者権限でAPIがコールされます。
レスポンスは $topics_list_response という変数に格納されます。

続いて、レスポンスを一時ファイルに追記していきます。

```smarty
{foreach from=$topics_list_response.list item="topics"} {* 注5 *}
  {assign var="row" value=$dataSet.emptyArray} {* 注6 *}
  {append var="row" value=$topics.topics_id}{* 記事ID *}
  {append var="row" value=$topics.contents_type}{* カテゴリID *}
  {append var="row" value=$topics.contents_type_nm|escapeCSV:false:"UTF-8"}{* カテゴリ名 *} {* 注7 *}
  {append var="row" value=$topics.subject|escapeCSV:false:"UTF-8"}{* 件名 *}
  {append var="row" value=$topics.contents|escapeCSV:false:"UTF-8"}{* 本文 *}
  {assign var="row_str" value=","|implode:$row} {* 注8 *}
  {write_file path=$tmp_path value=$row_str|cat:"\n" is_append=1} {* 注9 *}
{/foreach}

```
注5) $topics_list_response.list に記事のデータが配列として格納されてますので、その配列の各要素でループします。

注6) ここでもさきほどと同様に$row という変数を $dataSet.emptyArray（空配列）で初期化し、ヘッダー行の順番通りに配列要素を追加していきます。

注7) マルチバイト文字については追加するときに escapeCSV修飾子を使ってダブルクォーテーションで括る・文字コードをUTF-8に変換するといった処理をおこないます。なお escapeCSVの後ろの:false は改行コードをエスケープするかどうかを指定しています。

注8) $row配列に格納した値をカンマ区切りで文字列結合します。

注9) もう一度write_file関数を使って一時ファイルに8.の文字列＋改行コードを追記します。is_append=1を指定するとwrite_file関数は追記モードになります。このとき、path属性を使って一時ファイル名を指定しなければなりませんので、注2)で取得したファイル名を指定しておきます。

最後に一時ファイルをオンラインストレージにアップロードする処理です。

```smarty
{assign var=csv_path value='/path/to/topics_list.csv'} {* 注10 *}
{assign var="tmp_abs_path" value=$smarty.const.TEMP_DIR2|cat:'/'|cat:$tmp_path} {* 注11 *}
{put_file path=$csv_path tmp_path=$tmp_abs_path} {* 注12 *}

```
注10) オンラインストレージ上でのファイル名をフルパスで指定します。

注11) 一時ファイルのパスを絶対パスに変換します。一時ファイルはTEMP_DIR2 というパスに保存されてます。

注12) 一時ファイルをオンラインストレージにアップロードします。

完成したスクリプトは以下の様になります。

```smarty
{assign var="csv_header" value="記事ID,カテゴリID,カテゴリ名,件名,本文"}
{write_file var=tmp_path value=$csv_header|cat:"\n"}

{assign var=queries value=$dataSet.emptyArray}
{append var=queries index=cnt value=0}
{api_internal   endpoint='/rcms-api/1/topics-list'
                method='GET'
                member_id=1
                queries=$queries
                var='topics_list_response'
}
{foreach from=$topics_list_response.list item="topics"}
  {assign var="row" value=$dataSet.emptyArray}
  {append var="row" value=$topics.topics_id}{* 記事ID *}
  {append var="row" value=$topics.contents_type}{* カテゴリID *}
  {append var="row" value=$topics.contents_type_nm|escapeCSV:false:"UTF-8"}{* カテゴリ名 *}
  {append var="row" value=$topics.subject|escapeCSV:false:"UTF-8"}{* 件名 *}
  {append var="row" value=$topics.contents|escapeCSV:false:"UTF-8"}{* 本文 *}
  {assign var="row_str" value=","|implode:$row}
  {write_file path=$tmp_path value=$row_str|cat:"\n" is_append=1}
{/foreach}

{assign var=csv_path value='/path/to/topics_list.csv'}
{assign var="tmp_abs_path" value=$smarty.const.TEMP_DIR2|cat:'/'|cat:$tmp_path}
{put_file path=$csv_path tmp_path=$tmp_abs_path}
```

### 4. 更新する
記載完了したら、更新ボタンをクリックして内容を保存します。あとは前述の設定時刻の5:00になるのを待ちましょう。
実行されると指定したオンラインストレージ上のパスにファイルが生成されています。

### 5.テストする方法
debug_print_var修飾子を使うとバッチ編集画面上に変数の内容が出力されます。
ここで第一引数は表示する配列の階層の深さ、第二引数は最大文字列長になります。

```
{$csv_header|@debug_print_var:0:1000}
```
「テストする」ボタンクリックすると変更内容を保存せずに、バッチ処理を実行できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/efad52f459af4e425f6bbeaa7c2a4bd4.png)

$csv_header にヘッダ行が保存されていることが確認出来ました。
確認が終わったらdebug_print_varの行は削除しておいてください。

## 関連ドキュメント
- [バッチ処理](/ja/docs/management/batch/)
- [バッチテンプレート](/ja/docs/management/batch-template/)
- [バッチログ](/ja/docs/management/batch-log-list/)
- [バッチ処理を使用して、CSVで日次データを保存する](/ja/docs/tutorials/how-to-implement-batch-function-exports-csv/)
- [デフォルトのバッチ処理 一覧](/ja/docs/reference/batch-list/)
- [バッチ処理の実行を指定の日時や週次に設定できますか？](/ja/docs/faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly/)


---

# Swagger UIを利用して、APIのセキュリティを確認する

> 元ページ: `tutorials/how-to-use-swagger-ui` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-swagger-ui/

Kurocoでは、作成したAPIごとに動作や仕様を確認する用途として、Swagger UIを利用できます。  

このチュートリアルでは、下記パターンのセキュリティ設定で、実際に記事データをSwagger UI上で確認する方法を紹介します。

- [セキュリティ設定：なし で記事データを表示する](#セキュリティ設定なし-で記事データを表示する)
- [セキュリティ設定：Cookie で記事データを表示する](#セキュリティ設定cookie-で記事データを表示する)
- [セキュリティ設定：静的アクセストークン で記事データを表示する](#セキュリティ設定静的アクセストークン-で記事データを表示する)
- [セキュリティ設定：動的アクセストークン で記事データを表示する](#セキュリティ設定動的アクセストークン-で記事データを表示する)
- [セキュリティ設定：特権付き静的トークン で記事データを表示する](#セキュリティ設定特権付き静的トークン-で記事データを表示する)

参考) APIのセキュリティ設定については、[API Security](/ja/docs/management/api-security/)を参照してください。


## Swagger UIについて
Swagger UIは、APIの標準仕様であるOpenAPIをWEB上で可視化するオープンソースのプレイグラウンドです。  
Swagger UIの詳細な使い方はこのチュートリアルでは省略しますので、詳しくは[Swagger公式サイト](https://swagger.io/tools/swagger-ui/)をご確認ください。


## Swagger UI画面の表示方法
サイドメニューより[API]を選択し、API画面より[Swagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/194e0a1cd896a95dec3ea906e3da8492.png)

Swagger UI画面が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b060e05308da8218767ede8d58c88817.png)

## 前提条件
今回はすでに基本的なAPIが作成済みであることを前提としています。  
まだAPIを作成していない場合は、[「KurocoとNuxt.jsで、コンテンツ一覧ページを作成する」](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)を参考に、APIの設定をお願いいたします。

それではSwagger UI上で記事データを確認していきます。

## セキュリティ設定：なし で記事データを表示する

ここではAPIのセキュリティ設定：なしの状態で、下記２点をSwagger UI上で確認します。
- エンドポイントのAPIリクエスト制限が`制限無し`のときは正常にリクエスト/レスポンスする
- エンドポイントのAPIリクエスト制限が`制限無し`**以外**のときはリクエストが拒否される

#### エンドポイントのAPIリクエスト制限が`制限無し`のときは正常にリクエスト/レスポンスする
まずはエンドポイントのAPIリクエスト制限が`制限無し`のときの確認をします。

**1. セキュリティ設定を変更する**  
まずAPIのセキュリティ設定を変更します。  
API画面より、セキュリティの[設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f9e7bd7f7f498e57304e69c1de410d7.png)

セキュリティより、APIのセキュリティ設定を[無し]に変更し、[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/73e9ddb6873c98c06909646f8f4579a9.png)

:::tip
エンドポイントにAPIリクエスト制限をかけている場合はセキュリティの変更前に外してください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1f2f4ab6d080e42735f1a011b3d6dfe6.png)
:::

**2. Swagger UI画面にて表示を確認する**  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)  

`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

レスポンスコード:200でデータがレスポンスされることを確認できました。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1f9c043aefa99a564e3a613e3c4ed923.png)

#### APIリクエスト制限がかかっているときはリクエストが拒否される
次に、`news`が認証を要求する設定である場合、Swagger UI上でアクセス拒否されることを確認します。

**1. コンテンツ定義のAPIリクエスト制限を変更する**  
エンドポイントが参照するコンテンツ定義の設定を変更します。  
対象のコンテンツ一覧画面より、[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cf26a3493429dedb92e6ad6e2e5f00a7.png)

権限設定タブでAPIリクエスト制限を`制限無し`**以外**にします。ここでは「GroupAuth:Administrator」を指定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6d360c066c5221621116b5dc58615d4.png)

**2. Swagger UI画面にて表示を確認する**  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)

`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、レスポンスコード:401でデータがレスポンスされないことを確認できました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d1d0f74358f2e922a98b2cd1fa9a08d.png)

以上でセキュリティ設定：なし の場合の確認が完了です。

## セキュリティ設定：Cookie で記事データを表示する
次に、APIのセキュリティ設定：Cookie で、Swagger UI上で記事データを確認します。

**1. セキュリティ設定を変更する**  
APIのセキュリティ設定を[Cookie]に変更します。  
API画面より、セキュリティの[設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f9e7bd7f7f498e57304e69c1de410d7.png)

セキュリティより、APIのセキュリティ設定を[Cookie]に変更し、[更新する]をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b02513e0bd31eca33367c707d6275421.png)

**2. エンドポイントのAPIリクエスト制限を変更する**  
次に作成済みのエンドポイントnewsの設定を変更します。 API一覧画面より、対象エンドポイントの[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0ac1ba241275a035ce371e27bda56e9.png)

`news`の認証を`制限無し`**以外**にします。ここでは「GroupAuth:Administrator」を指定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ba2ca1ecd203a50bf8e9a76426a55cab.png)

**3. Swagger UI画面にてコンテンツ表示を確認する**  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)

`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、レスポンスコード:401でデータがレスポンスされないことを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d1d0f74358f2e922a98b2cd1fa9a08d.png)

これはGroupAuth:Administratorの権限を有するユーザーがアクセスしないと`news`はアクセス拒否するためです。  
このためまずログイン用のエンドポイントを追加作成し、自分自身がGroupAuth:Administratorの権限を有するユーザーであることをKurocoサーバーに伝える必要があります。  
その際の認証方法は設定した通り、Cookie認証でセッションの維持をします。  

そのため、次にログイン用のエンドポイントを追加作成し、ログイン後に再度[Execute]をして、データが正常にレスポンスされることを確認します。

**4. 管理者の権限グループを持っていることを確認する**  
自分のアカウントが管理者の権限を持っていることを確認します。  
メニューより[メンバー]をクリックし、ご自身のアカウントを選択します。  
次に、「所属グループ」の項目で「Administrator」が設定されていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cfb6da13b0223656afdc618ae55ff626.png)

参考) グループ設定についての詳細は、管理画面マニュアル[グループを作成する](/ja/docs/tutorials/how-to-make-new-group/)をご確認ください。

**5. Swagger UI画面にてログインを確認する**  
Swagger UI画面にてログインを確認します。  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)

`login`エンドポイントをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/994ec49425bbc43c2dc0034d73c4d9d1.png)

[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4395805416b9e1bed89b6cad16475bfc.png)

すると、Request bodyフィールドが記述できるようになります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d125f58ff6f5bd53ed65ccbd6f59049.png)

こちらに下記のようにログイン情報を記載します。  
```json title="Request body"
{
  "email": "YOUR_MAIL_ADDRESS@example.com",
  "password": "PASSWORD",
  "login_save": 0
}
```

:::caution
`YOUR_MAIL_ADDRESS@example.com` と `PASSWORD` にはご自身のメールアドレスとパスワードを入力ください。    
:::

Request bodyに記入したら[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8876ccf1d9780ebbedad7b987a28766.png)

レスポンスコード:200でデータがレスポンスされることを確認できました。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/60c501493922c7b6fada37e1d8dde2cf.png)

:::tip
デベロッパーツールを開いて対象のリクエストを確認すると、レスポンスヘッダーの`Set-Cookie`に`rcms_api_access_token`が返されていることが分かります。  
これにより、ブラウザのCookieにトークンが保存されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1166bbcc628fda693b24591fd93bdee3.png)
:::

**6. 再度Swagger UI画面にてコンテンツ表示を確認する**  
この状態で、再度Swagger UI画面にて `news`エンドポイントを確認します。  
`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、先ほどはレスポンスコード:401でしたが、今回はレスポンスコード:200でデータがレスポンスされることを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2b9dce6c707bd24d0e7f5b92b6c75cb.png)

:::tip
デベロッパーツールを開いて対象のリクエストを確認すると、リクエストヘッダーに`rcms_api_access_token`が含まれていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d566b21451162123a0819c73e5480746.png)
:::

**セキュリティ設定：Cookie の場合の注意点**  
セキュリティ設定：Cookie の場合は、サードパーティCookieの規制を回避するため、フロントとKurocoのドメインを合わせる必要があります。  
(ドメインを一致させファーストパーティCookieにさせる必要があります)  
そのため、例えばローカル上のフロントエンド(Nuxt.js)から`login`->`news`とアクセスしても、
ドメイン(URL)が`http://localhost:3000`からのアクセスということになるため、リクエストは拒否されます。

## セキュリティ設定：静的アクセストークン で記事データを表示する
次に、APIのセキュリティ設定：静的アクセストークン で、Swagger UI上で記事データを確認します。

**1. エンドポイントのAPIリクエスト制限を変更する**  
まず作成済みのエンドポイント`news`の設定を変更します。  
API一覧画面より、`news` エンドポイントの[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dc602cae4419497d2e50ab06380542a7.png)

APIリクエスト制限で `制限無し`を選択し、[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6e42d058bf81b16a8ed42eeac4cf1bf1.png)

**2. セキュリティ設定を変更する**  
API画面より、セキュリティの[設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f9e7bd7f7f498e57304e69c1de410d7.png)

セキュリティより、APIのセキュリティ設定を[静的アクセストークン]に変更し、[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c484a3b344cd808bca62b616253b1966.png)


**3. Swagger UI画面にて表示を確認する**  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)

`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、レスポンスコード:401でデータがレスポンスされないことを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bcdd03eecc7c5625d7f40de5f4e7540.png)

これはトークンがリクエストに含まれていないものは、アクセス拒否するためです。

静的アクセストークンにおいては、ユーザーの認証にトークンを使用します。  
ユーザーがリクエストするときには、リクエストヘッダにカスタムリクエストヘッダ(`x-rcms-api-access-token`)を付与し、その値を照合することで認証をします。  
Kurocoでは、Swagger UIをカスタマイズして、このトークンを動的に生成し、Kurocoサーバー上に保持できます。  
また、リクエストの際のカスタムリクエストヘッダの自動付与も、画面上で設定が可能です。

**4. 静的アクセストークンを生成する**  
次に静的アクセストークンを生成します。  
API情報画面の[静的アクセストークン]の[生成する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/919690f93d436e541c3dccea07139c0a.png)
表示された「アクセストークンの生成」で有効期限を指定して、[生成する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2942b55544cdf1769ce3b818823cd848.png)

するとTokenが発行されるので、値をコピーしておきます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7106a941056411a5ebc6d48a21b0c6a1.png)

**5. 生成した静的アクセストークンの設定をする**  
次に、生成した静的アクセストークンをリクエストヘッダに自動付与するように設定します。  
API情報画面より、[Authorize]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1fc07ae4f7b9754bfb597b69a5e7b62d.png)

Valueに先ほどコピーした値を入力し、[Authorize]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/faaa5792c46f75e9f05bfa6dfeeeef85.png)

「Available authorizations」と表示されるので、[close]で画面を閉じます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4661c04d4733da515d131e8bd9f4d977.png)

**6. 再度Swagger UI画面にてコンテンツ表示を確認する**  
この状態で、再度Swagger UI画面にて `news`エンドポイントを確認します。  

`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、先ほどはレスポンスコード:401でしたが、今回はレスポンスコード:200でデータがレスポンスされることを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/91e3ec087b5f53c84b0c202baf848ad9.png)

「Curl」を確認すると、このリクエストには、`X-RCMS-API-ACCESS-TOKEN`が生成した静的アクセストークンとともにリクエストされていることが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f169ce2c9b6eca0afad0720233258973.png)


**セキュリティ設定：静的アクセストークン の場合の注意点**  
静的アクセストークンによるリクエストはCookieとは異なり、ドメインを一致させる必要がありません。  
このため、ヘッダーに適切にトークンが設定されている場合、ローカルからアクセスが可能です。  

Swagger UI上に表示したサンプルリクエスト(Curl)をローカル上で実行すると、以下のようにレスポンスが正常であることを確認できます。  
```bash title="bash"
curl -X 'GET' \
  'https://sample-support-kuroco.a.kuroco.app/rcms-api/1/news' \
  -H 'accept: */*' \
  -H 'X-RCMS-API-ACCESS-TOKEN: 静的アクセストークンの値'

# レスポンスが表示されます。
# {"errors":[],"messages":[],"list":[{"topics_id": ...
```

また、フロントエンド(Nuxt)からもアクセスが可能です。  
下記の用に`pages/news/index.vue`のコードを変更し、静的アクセストークンをリクエストヘッダで送信するように変更します。  

```diff title="/pages/news/index.vue"
 export default {
   async asyncData({ $axios }) {
     return {
-      response: await $axios.$get('/rcms-api/4/news'),
+      response: await $axios.$get('/rcms-api/4/news', {
+        headers: { 'x-rcms-api-access-token': 'value of Static Access Token' }
+        }
+      )
     };
   },
 };
```

:::caution
エンドポイントはご自身のサイトのものに書き換えてください。
:::

## セキュリティ設定：動的アクセストークン で記事データを表示する
次に、APIのセキュリティ設定：動的アクセストークン で、Swagger UI上で記事データを確認します。

**1. セキュリティ設定を変更する**  
API画面より、セキュリティの[設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f9e7bd7f7f498e57304e69c1de410d7.png)

セキュリティより、APIのセキュリティ設定を[動的アクセストークン]に変更し、[更新する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4c0e4390ae6171d0a5dbf5bf87e4afe.png)

**2. エンドポイントのAPIリクエスト制限を変更する**  
次に作成済みのエンドポイント`news`の設定を変更します。  
API一覧画面より、対象エンドポイントの[更新]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0ac1ba241275a035ce371e27bda56e9.png)

APIリクエスト制限を`制限無し`**以外**にします。ここでは「GroupAuth:Administrator」を指定します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ba2ca1ecd203a50bf8e9a76426a55cab.png)

**3. Swagger UI画面にて表示を確認する**  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)

`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、レスポンスコード:401でデータがレスポンスされないことを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d93c86bad850b41c35f156c232633a67.png)

これはトークンがリクエストに含まれていない、トークンが含まれていた場合でも、GroupAuth:Administratorの権限を有するユーザーが生成したトークンの値ではない場合、アクセス拒否するためです。

動的アクセストークンにおいては、ユーザーの認証にトークンを使用します。  
ユーザーがリクエストするときには、リクエストヘッダにカスタムリクエストヘッダ(`x-rcms-api-access-token`)を付与し、その値を照合することで認証をします。  
動的アクセストークンでは、静的アクセストークンとは異なり、固定のトークンの生成/設定はできません。  
このため、ログイン用のエンドポイントと、トークン生成用のエンドポイントを追加作成し、ログイン->トークン生成によりトークンを動的生成します。  
セキュアなエンドポイントにアクセスするには、静的アクセストークン同様に、リクエストヘッダにカスタムリクエストヘッダ(`x-rcms-api-access-token`)を付与し、動的生成したトークンの値を送信します。  
Kurocoサーバーはこの値を照合することで認証をします。
また、リクエストの際のカスタムリクエストヘッダの自動付与も、画面上で設定が可能です。

**4. 管理者の権限グループを持っていることを確認する**  
自分のアカウントが管理者の権限を持っていることを確認します。  
メニューより[メンバー]をクリックし、ご自身のアカウントを選択します。  
次に、「所属グループ」の項目で「Administrator」が設定されていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cfb6da13b0223656afdc618ae55ff626.png)

参考) グループ設定についての詳細は、管理画面マニュアル[グループを作成する](/ja/docs/tutorials/how-to-make-new-group/)をご確認ください。


**5. Swagger UI画面にてログインを確認する**  
Swagger UI画面にてログインを確認します。  
[Swagger UI]をクリックしてSwagger UI画面に移動します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2bdd61536ffc429a5fd487252ca4523.png)

`login`をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/994ec49425bbc43c2dc0034d73c4d9d1.png)


[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4395805416b9e1bed89b6cad16475bfc.png)

すると、Request bodyフィールドが記述できるようになります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d125f58ff6f5bd53ed65ccbd6f59049.png)

こちらに下記のようにログイン情報を記載します。  

```json title="Request body"
{
  "email": "YOUR_MAIL_ADDRESS@example.com",
  "password": "PASSWORD",
  "login_save": 0
}
```

:::caution
`YOUR_MAIL_ADDRESS@example.com` と `PASSWORD` にはご自身のメールアドレスとパスワードを入力ください。
:::

Request bodyに記入したら[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8876ccf1d9780ebbedad7b987a28766.png)

リクエストが成功した場合、`grant_token`を含んだレスポンスが返却されますので、値をコピーしておきます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab12710f28cf8558f6ea48bbe2b4d0a8.png)

:::tip
`grant_token`は、実際に必要なトークン(`access_token`)を取得するためのワンタイムトークンです。
:::

次にSwagger UI画面より、tokenをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c35172556c316eca172642352bab665b.png)

[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/34c44be61061e801d867f7b404ad8efb.png)

Request bodyフィールドが記述できるようになります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5ba1e7ca52f46d83f818c1a14f5aefa.png)

Request bodyフィールドに下記のように記述します。

```json title="Request body"
{
  "grant_token": "GRANT_TOKEN"
}
```

:::caution
`GRANT_TOKEN`には、先ほど取得した値を入力してください。
:::

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/950d08da9ea2382466b9594d14ca3af9.png)

リクエストが成功した場合、`value`を含んだ`access_token`のレスポンスが返却されます。  
`value`の値をコピーしておいてください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9f94b2f45008af24084dc38838a94f9.png)

**6. 生成した動的アクセストークンの設定をする**  
次に、生成した動的アクセストークンをリクエストヘッダに自動付与するように設定します。  
API情報画面より、[Authorize]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f666c3cefb0056b8133086d9e8659b0d.png)

Valueに先ほどコピーした値を入力し、[Authorize]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/faaa5792c46f75e9f05bfa6dfeeeef85.png)

「Available authorizations」と表示されるので、[close]で画面を閉じます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4661c04d4733da515d131e8bd9f4d977.png)

**7. 再度Swagger UI画面にてコンテンツ表示を確認する**  
この状態で、再度Swagger UI画面にて newsエンドポイントを確認します。  
`news`エンドポイントを選択します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/695ccda34c9d7f5475700da37f5de00f.png)

[Try It Out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ad6788ca5cb785548d4bbc28914cb2d.png)

画面下部に移動し、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/174b18d88d84bfc1256f5db76343bdf3.png)

すると、先ほどはレスポンスコード:401でしたが、今回はレスポンスコード:200でデータがレスポンスされることを確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/91e3ec087b5f53c84b0c202baf848ad9.png)

また、Curlを確認すると、このリクエストには、`x-rcms-api-access-token`が生成した動的アクセストークンとともにリクエストされていることが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f169ce2c9b6eca0afad0720233258973.png)

**セキュリティ設定：動的アクセストークン の場合の注意点**  
動的アクセストークンによるリクエストはCookieとは異なり、ドメインを一致させる必要がありません。  
このため、ヘッダーに適切にトークンが設定されている場合、ローカルからアクセスが可能です。  

静的アクセストークンのときと同様に、Swagger UI上に表示したサンプルリクエスト(Curl)をローカル上で実行して、レスポンス表示も可能です。  
この場合は前述の通り、`login`->`token`->`news`と順番に実行する必要があります。

また、フロントエンド(Nuxt)からもアクセスが可能です。
下記の用に`pages/news/index.vue`のコードを変更し、`login`->`token`->`news`と順番に実行、生成したトークンをリクエストヘッダで送信するように変更します。

```diff title="/pages/news/index.vue"
 <script>
 export default {
   async asyncData({ $axios }) {
+    const loginResponse = await $axios.$post('/rcms-api/9/login',  {
+      'email': 'YOUR_MAIL_ADDRESS@example.com',
+      'password': 'PASSWORD',
+      'login_save': 0
+    });
+    const grantToken = loginResponse.grant_token;
+
+    const tokenResponse = await $axios.$post('/rcms-api/9/token',  {
+      'grant_token': grantToken,
+    });
+    const accessToken = tokenResponse.access_token.value;
     return {
-      response: await $axios.$get('/rcms-api/4/news'),
+      response: await $axios.$get('/rcms-api/4/news', {
+        headers: { 'x-rcms-api-access-token': accessToken }
+        }
+      )
     };
   },
 };
```

:::caution
エンドポイントはご自身のサイトのものに書き換えてください。<br/>
`YOUR_MAIL_ADDRESS@example.com` と `PASSWORD` にはご自身のメールアドレスとパスワードを入力ください。
:::

## セキュリティ設定：特権付き静的トークン で記事データを表示する
次に、APIのセキュリティ設定：特権付き静的トークン で、Swagger UI上で記事データを確認します。

特権付き静的トークンは、静的アクセストークンと同様のトークン認証ですが、トークン生成時にメンバーIDを指定します。  
指定したメンバーの権限でリクエストが実行されるため、APIリクエスト制限がかかっているエンドポイントにもアクセスできます。

基本的な操作は静的アクセストークンと同じです。以下の点が異なります。

**1. セキュリティ設定を変更する**  
API画面より、セキュリティの[設定]をクリックし、セキュリティを[特権付き静的トークン]に変更して[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/994681867a09d0c4e40b3d9cc07ea1c7.png)

**2. 特権付き静的トークンを生成する**  
API情報画面の[特権付き静的トークン]の[生成する]をクリックします。  
表示されたダイアログで、以下の項目を指定します。
- **有効期限**: トークンの有効期限を指定します。
- **メモ**: 任意のメモを入力できます。
- **メンバーID**: トークンに紐付けるメンバーのIDを指定します。このメンバーの権限でAPIリクエストが実行されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4bab79743ba750a3dbe2006283426fd.png)

値を入力したら[生成する]をクリックします。Tokenが発行されるので、値をコピーしておきます。

**3. 生成したトークンの設定をする**  
静的アクセストークンと同様に、Swagger UI画面の[Authorize]をクリックし、Valueにコピーしたトークンを入力して[Authorize]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57b99ff9f4bea46b338c5f269549670e.png)

**4. Swagger UI画面にてコンテンツ表示を確認する**  
エンドポイントを選択し、[Try It Out] -> [Execute]をクリックすると、レスポンスコード:200でデータがレスポンスされることを確認できます。  
メンバーIDで指定したメンバーの権限でリクエストが実行されるため、APIリクエスト制限がかかっているエンドポイントにもアクセスできます。
 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/91e3ec087b5f53c84b0c202baf848ad9.png)

**セキュリティ設定：特権付き静的トークン の場合の注意点**  
特権付き静的トークンによるリクエストはCookieとは異なり、ドメインを一致させる必要がありません。  
静的アクセストークンと同様に、ヘッダーに適切にトークンが設定されている場合、ローカルからアクセスが可能です。

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [API](/ja/docs/management/api-list/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [静的アクセストークンによるAPIアクセス制限の方法](/ja/docs/tutorials/restricting-api-access-with-statictoken/)
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [SwaggerUIで確認できないリクエストがあります。確認する方法はありますか？](/ja/docs/faq/how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui/)


---

# エンドポイント設定後の注意点

> 元ページ: `tutorials/points-to-note-after-endpoint-configuration` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/points-to-note-after-endpoint-configuration/
> 概要: エンドポイントの設定が適切にされてない場合、意図せず情報が公開されてしまう恐れがあります。エンドポイント設定後の注意点を記載しますので、セキュリティ対策のためご確認ください。

エンドポイントの設定が適切にされてない場合、意図せず情報が公開されてしまう恐れがあります。  
エンドポイント設定後の注意点を記載しますので、セキュリティ対策のためご確認ください。

## 不要なカラムを出力許可リスト機能で制御する
デフォルトでは全カラムが公開されます。そのため、必要なカラムのみ公開するためには、出力許可リスト機能を利用し、カラムを制御する必要があります。

エンドポイント一覧より、対象のエンドポイントの[後処理]より、出力許可リストを追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d81f8848df8acb75c2c5794b6c6d04a.png)  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0d42585494f8eb6d4aa9785344052a8.png)


リストに公開するフィールドを追加し、保存をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/89993d3db23578174c3d79b45c70d390.png)

以上で、必要なカラムのみ公開することが可能となります。

:::tip
API 後処理の設定については、[管理画面マニュアル -> API 後処理](/ja/docs/management/api-postprocessing/)をご確認ください。
:::

## CORSの設定の確認
エンドポイント一覧 -> [CORSを設定する]をクリックし、CORSが適切に設定されているか確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/84a33972b3efe969195e18b3f85dc897.png)  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0610530f8cd769be2f91ad55754627e.png)

CORS_ALLOW_ORIGINにテスト用のURLが残っている場合、サイト公開後には削除することが望ましいです。

:::tip
CORSについては、[管理画面マニュアル -> API -> CORSを設定する](/ja/docs/management/api-list/#corsを設定する)をご確認ください。
:::

## APIセキュリティの確認
エンドポイント一覧 -> [セキュリティ]をクリックし、APIのセキュリティが適切に設定されているか確認してください。  
また、IPアドレス制限もかけられます。特定のIPアドレスからのアクセスのみ許可する場合に設定をしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53eb4687eb36b13705ad99d71f4cfb02.png)  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/935c9f26b369e850b7b5b12085ec7724.png)  

:::tip
APIセキュリティの設定については、[管理画面マニュアル -> API セキュリティ](/ja/docs/management/api-security/)をご確認ください。
:::

## エンドポイントのAPIリクエスト制限の確認
エンドポイントのAPIリクエスト制限を確認し、適切な権限を与えてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed317104aaf3709c836658ce230e84c5.png)

APIリクエスト制限は下記3種類より選択できます。
- None
- GroupAuth
- MemberCustomSearchAuth
GroupAuthもしくはMemberCustomSearchAuthを選択すると、APIの使用時にログインユーザーの権限をチェックし、合致した場合にのみリクエストを許可します。

## 不要なエンドポイントの削除
利用していないエンドポイントは、削除するようにしてください。  

なお、エンドポイントには「サマリー」が記載できるようになっております。サマリーにエンドポイントの利用用途を明確に記載し、運用に役立ててください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/326b048542f179ef5e2b0f654aff19c8.png)

サマリーはエンドポイント一覧画面に表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7824ad110b7ab3c37f583a0cb79c63e9.png)

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [API 後処理](/ja/docs/management/api-postprocessing/)
- [API](/ja/docs/management/api-list/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
