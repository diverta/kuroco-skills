# Kurocoドキュメント: リファレンス / Smarty・トリガー・バッチ（2/3）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Smartyプラグイン（`smarty-plugin`）
- トリガーメールアドレス（`trigger-email-address`）


---

# Smartyプラグイン

> 元ページ: `reference/smarty-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/smarty-plugin/

カスタム処理やバッチ処理にてSmartyプラグイン利用できます。
利用可能なSmartyプラグインをまとめます。

このページは個別のSmartyプラグインのリファレンスです。`{if}` 条件や修飾子で使えるPHP関数、未定義キーへの安全な配列アクセス、`$smarty.*` のKuroco固有挙動、`{php}` の制限など、Kuroco上で動くすべてのテンプレートに共通する言語レベルの挙動については [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/) を参照してください。

## add

変数に数値を加算します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 加算対象の変数名、加算結果も同一変数名に格納されます (必須)
value | Int | 数値

**記載例**  
```smarty
{add var=i value=5}
```

## api

外部APIをコールします。  
APIを提供している外部サービスに対してリクエストを送信し、レスポンスを変数に格納します。

**属性**  

| 項目 | 用途 | 記載例 | 備考 |
| :--- | :--- | :--- | :--- |
|endpoint|エンドポイント(必須)|`https://example.com/brah/`||
|method|メソッド|`POST`/`GET`/`PATCH`/`PURGE`/`PUT`/`DELETE`/`HEAD`||
|query|クエリ文字列|`param1=hoge&param2=foo`||
|queries|クエリ配列|`$params`||
|json_body|リクエスト Json Body|`{param1:"hoge",param2:"foo"}`||
|body|リクエスト Body|||
|files|ファイル|`['path/to/hoge.jpg', 'path/to/foo.png']`/<br/>`[{'path':'path/to/hoge.jpg'}, {'path':'path/to/foo.png'}]`|Kuroco一時フォルダからの相対パスで指定します|
|headers|リクエストヘッダー|`['Host: localhost','user-agent: hoge']`|配列で指定してください|
|cache_time|キャッシュ時間(分)|`20`||
|var|レスポンスの格納変数|`response`||
|json_var|レスポンスの格納変数|`response`|レスポンスがJSON形式の場合、デコードされた値が格納されます|
|resp_header_var|レスポンスヘッダーの格納変数|`header`|レスポンスヘッダーが配列形式で格納されます|
|dl_flg|ダウンロードフラグ|`true`/`false`|`true`とした場合、レスポンスをKurocoの一次領域にファイルとして保存します|
|status_var|0:失敗 1:成功|`status`|リクエストが成功したか失敗したかが返ります|
| http_code_var | HTTPステータスコードの格納変数 | `http_code` | レスポンスの HTTP ステータスコードが格納されます。 |
| timeout |タイムアウト|`60`| タイムアウト秒数。既定は 30、指定できるのは 1〜3600（範囲外はエラー）。 |
|sslcert|mTLS クライアント証明書|`SSLCERT001`|mTLSクライアント証明書のシークレットのキー名を指定します|
|sslkey|mTLS クライアント秘密鍵のシークレットのキー名|`SSLKEY001`|mTLSクライアント秘密鍵のシークレットのキー名を指定します|
|cainfo|mTLS サーバーCA証明書のシークレットのキー名|`CAINFO001`|mTLS CA証明書のシークレットのキー名を指定します|

**記載例**  
**PUTでファイルを送信する**

PUTメソッドで特定のURLにファイルを送信する場合は、files属性にファイルパスの配列を指定します。ただし一度に送信できるファイル数は1件のみです。したがって指定した配列の第２要素目以降は無視されます。  

```smarty
{write_file var=tmp_path value="This is test."}
{assign_array var=files values=""}
{append var=files value=$tmp_path} 
{api
    endpoint='https://www.example.com/brah/'
    method="PUT"
    var=response
    files=$files
    status_var=status
}
```

**PUTでテキストを送信する**

テキストをPUTで送信する場合は、json_body属性またはbody属性に送信したいテキストをセットします。  
JSON形式の場合はjson_body属性に値をセットします。

```smarty
{assign_array var=product values=""}
{append var=product index=name value='apple'}
{append var=product index=price value='160'}
{assign var=json value=$product|@json_encode}
{api
    endpoint='https://www.example.com/brah/'
    method='PUT'
    json_body=$json
    var=response
    status_var=status
}
```

JSON以外のテキストの場合はbody属性に値をセットします。  
このときリクエストヘッダの Content-Type に `text/***` の形式のものを指定しなければなりません。また、bodyに指定する文字列は、たとえJSON形式ではなくても、json_bodyの場合と同様にjson_encode修飾子をつける必要がありますのでご注意ください（これはマルチバイト文字部分をUnicodeにエスケープする必要があるためです）。

```smarty
{assign_array var=headers values=""}
{append var=headers value='Content-Type: text/csv'}
{assign var=csv value="ID,NAME,PRICE\n1,apple,150\n2,orange,200"}
{api
    endpoint='https://www.example.com/brah/'
    method='PUT'
    headers=$headers
    body=$csv|@json_encode
    var=response
    status_var=status
}
```

**mTLS認証によるサーバ間認証を行い通信する**  
外部システムとの連携にmTLS認証を行う必要がある場合、KurocoをmTLSクライアントとして通信することが出来ます。
まず、サーバーCA証明書、クライアント証明書、クライアント秘密鍵の内容をシークレットに保存してください。保存する際にシークレットキー名を指定する必要があります。このシークレットキー名を以下のように指定してください。

```smarty
{api 
    endpoint='https://xxx.xxx.xxx/xxxx/'
    method='GET'
    var='response'
    status_var='status'
    sslcert='SSLCERT001'
    sslkey='SSLKEY001'
    cainfo='CAINFO001'
}
```

クライアント証明書、クライアント秘密鍵を作成する際に使用したクライアントCA証明書は、mTLSサーバ側に許可する接続元の証明書として登録する必要があります。登録の仕方はシステムによって異なりますので各サービスの提供元へお問い合わせください。
ここで設定するサーバーCA証明書は接続先サーバーから提供を受けてください。
接続結果はAPIログに出力されますので、設定時にご参照ください。

**VercelにDeploy Hookを送信する**  
外部のホスティングサービスにビルドトリガーを送るWebhookとして利用できます。

```smarty
{api
    endpoint='https://api.vercel.com/v1/integrations/deploy/prj_******************'
    method="POST"
    var=response
    status_var=status
}
```

**関連ドキュメント**  
Kuroco 内部のAPIをコールする方法については、[カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/) をご確認ください。

## api_internal

内部的にAPIをリクエストして、応答をassignします。

**属性**  

Param | Type | Description
--- | --- | ---
endpoint | String | エンドポイント (必須)
method | String | メソッド (POST/GET)
query | String | クエリ文字列
queries | Array | クエリ配列
headers | Array | リクエストヘッダー
cache_time | Integer | キャッシュ時間 (分)
var | String | レスポンスの格納変数
status_var | String | 0:失敗 1:成功
member_id | Integer | 指定したログインメンバーとして実行<br/>※directのパラメータとの併用はできません。<br/>※数値のみ指定できます。変数や定数を指定できるのはスーパーユーザーのみで、スーパーユーザーのメンバーIDは指定できません。ログイン中のメンバーとして実行する場合は`use_current_session`を利用してください。
use_current_session | Boolean | 現在のセッションを引き継いでAPIリクエストを実行
direct | Boolean | ネットワーク(curl)を経由せず直接APIリクエストを実行<br/>※direct=trueをパラメータに指定できるのは、対象エンドポイントのHTTPメソッドがGETの場合に限ります。また、member_idとの併用はできません。

**記載例**    
```smarty
{api_internal
    endpoint='/rcms_api/1/sample'
    method='GET'
    query='ex=1&ex2=2'
    cache_time=20
    var='response'
    status_var='status'}
```

## api_method

エンドポイントを作成せずに、各モデルのオペレーションをします。
利用できるオペレーションはGETメソッドのもののみになります。POSTメソッドのオペレーションは利用できません。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
model | String | モデル
method | String | メソッド（オペレーション）
version | Integer | バージョン
request_params | Array | リクエスト変数
method_params | Array | メソッドの設定値。エンドポイントの設定画面に掲載されている「基本設定」「詳細設定」と同様になります。

**記載例**    
```smarty
{*  エンドポイント設定パラメータ *}
{assign_array var='method_params'                 values=''}
{assign_array var='method_params.topics_group_id' values='1'}
{* クエリパラメータ *}
{assign_array var='request_params'        values=''}
{assign       var='request_params.cnt'    value=20}
{assign       var='request_params.pageID' value=1}
{api_method
    var='topics_list'
    model='Topics'
    method='list'
    version='1'
    method_params=$method_params
    request_params=$request_params}

test:{$topics_list|@debug_print_var}
```

```smarty
{*  detailsのエンドポイントの場合はmethod_paramsでidを指定する *}
{assign_array var='method_params'           values=''}
{assign       var='method_params.ext_group' value=true}
{assign       var='method_params.topics_id' value=1234}
{api_method
    var='topics_details'
    model='Topics'
    method='details'
    version='1'
    method_params=$method_params}

test:{$topics_details|@debug_print_var}
```

## api_mng

内部的に管理APIをリクエストして、応答をassignします。

**属性**  

Param | Type | Description
--- | --- | ---
endpoint | String | エンドポイント(必須)
method | String | メソッド(POST/GET)
query | String | クエリ文字列
queries | Array | クエリ配列
headers | Array | リクエストヘッダー
files | Array | アップロードファイル
var | String | レスポンスの格納変数
status_var | String | 0:失敗 1:成功
member_id | Integer | 指定したログインメンバーとして実行<br/>※数値のみ指定できます。変数や定数を指定できるのはスーパーユーザーのみで、スーパーユーザーのメンバーIDは指定できません。ログイン中のメンバーとして実行する場合は`use_current_session`を利用してください。
use_current_session | Boolean | 現在のセッションを引き継いでAPIリクエストを実行

**記載例**    
```smarty
{api_mng
    endpoint='/management/<module>/sample'
    method='GET'
    query='ex=1&ex2=2'
    var='response'
    status_var='status'}
```

## api_token

APIトークン（[静的アクセストークン](/ja/docs/management/api-security/#静的アクセストークン)または[動的アクセストークン](/ja/docs/management/api-security/#動的アクセストークン)）を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | トークンを代入する変数名 (必須)
type | String | トークンタイプ: `static`（静的アクセストークン）または `dynamic`（動的アクセストークン）(必須)。対象APIの[セキュリティ設定](/ja/docs/management/api-security/)に対応するタイプを指定してください。
api_id | Integer | API ID (必須)。管理画面の「API」一覧画面で確認できます。
expires | Integer | 有効期限（秒）。staticトークンの新規生成時、およびdynamicトークンで使用
memo | String | メモ（staticトークンで使用）。デフォルト: `Generated by Smarty api_token plugin`
expires_var | String | トークンの有効期限（Unixタイムスタンプ）を代入する変数名 

**記載例**  
```smarty
{* 静的トークンを取得 *}
{api_token var="static_token" type="static" api_id=1}

{* 動的トークンを取得（有効期限1時間） *}
{api_token var="dynamic_token" type="dynamic" api_id=1 expires=3600}

{* staticトークンを新規生成する場合にメモを付与 *}
{api_token var="token" type="static" api_id=1 memo="Batch process token"}

{* トークンと有効期限を同時に取得 *}
{api_token var="token" type="dynamic" api_id=1 expires=3600 expires_var="token_expires"}
Token: {$token}
Expires at: {$token_expires|date_format:"%Y-%m-%d %H:%M:%S"}
```

:::note
- `static` トークンの場合、既存の有効なトークンがあればそれを返し、なければ新しいトークンを生成します。既存の有効なトークンが存在する場合、`expires` は無視されます。
- `dynamic` トークンの場合、常に新しいトークンを生成します。現在のセッションのログインメンバーとしてトークンが発行されます（セッションがない場合は、特定のメンバーに紐づかないトークンとして発行されます）。
:::

## append

テンプレートから, 新しい要素をarrayに追加します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 配列名 (必須)
value | String | 追加するオブジェクトまたは配列の名前 (必須）
index | Integer | 追加が始まる場所の配列のインデックス (optional)

**記載例**    
```smarty
{append var=options value='Option N' index='N'}
```

{/*
array_comma_match は実装中のため（Kuroco-opendev#12848）、リリース後に有効化してください。
## array_comma_match

値が、配列・カンマ区切り文字列・単一の値のいずれかの形式で指定された候補に含まれるかどうかを確認します。`topics_group_id`、`inquiry_id`、`group_id` のように複数の値を指定できるパラメータの判定に利用できます。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| （修飾子の入力） | Mixed | 検索対象。配列（`[1,2]`）、カンマ区切り文字列（`"1,2"`）、単一の値のいずれかを指定します（必須） |
| needle | Mixed | 検索対象に含まれるかどうかを確認する値（必須） |

**戻り値**

検索対象に値が含まれる場合は `true`、含まれない場合は `false` を返します。

#### 記載例

```smarty
{if $mng_plugin.slot.params.topics_group_id|array_comma_match:$topics_group_id}
  ...
{/if}
```

補足:

- 数値と文字列は緩やかに比較されます（例: `"1"` は `1` と一致します）。
- 検索対象が未設定の場合は、絞り込みなしとみなして `true` を返します。
*/}

## array_key_exists

配列にキーが存在するかどうかを確認します。PHP5互換のSmartyモディファイアです。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| array | Array | チェック対象の配列（必須） |

**戻り値**

キーが配列に存在する場合は `true`、存在しない場合は `false` を返します。第二引数が配列でない場合も `false` を返します。

#### 記載例

```smarty
{if $key|array_key_exists:$array}Key exists{/if}

{* 数値キーのチェック *}
{if 0|array_key_exists:$array}First element exists{/if}
```

補足:

- 値ではなくキーの存在を確認します。値が `null` の場合でも `true` を返します。
- 第二引数が配列でない場合は安全に `false` を返します。

## assign_api_credential

新しいAPIリクエストを生成して、'val'にアクセスキーを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
dg_key | String | DG_CODEを生成するためのキー
dg_id | String | DG_CODEを生成するためのid
api_key | String | sidリクエストの生成するためのキー (必須)
var | Array | 戻りの配列の名前。
jwt_data | Array | JWTデータ
member_id | Integer | メンバーID
expire | Integer | 有効期限（秒）

**記載例**    
```smarty
{assign_api_credential
    api_key=$api_key
    dg_key="topics_edit_api"
    dg_id="0"
    var=val}
```

## assign_array

配列をテンプレート変数としてassignします。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | assignする配列の変数名 (必須)
values | String | 配列に格納する値。delimiterで区切られた文字列
delimiter | String | valuesで指定された値を分割するための区切り文字。デフォルトはカンマ
keys | String | 連想配列とする場合、キーを指定します。デフォルトはnull

**記載例**    
```smarty
{assign_array var="foo" values="bar1,bar2"}
{assign_array var="foo" values="bar1;bar2;bar3" delimiter=";"}
{assign_array var="foo" keys="key1,key2,key3" values="bar1,bar2,bar3"}
```

## assign_array_diff

array1, array2の間にdiffの配列を割り当てます。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | assign差分配列の名前
array1 | Array | 配列1
array2 | Array | 配列2
diff_mode | String | normal, key

**記載例**    
```smarty
{assign_array_diff
    var="foo"
    array1=$array1
    array2=$array2
    diff_mode='normal'}
```

## assign_array_intersect

array1, array2の交差の配列を割り当てます。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 交差配列の名前
array1 | String | 配列1
array2 | String | 配列2
intersect_mode | String | normal, assoc, key (default=normal)

**記載例**    
```smarty
{assign_array_intersect
    var="foo"
    array1=$array1
    array2=$array2
    intersect_mode='normal'}
```

## assign_array_set

配列に要素を追加します。  
この関数は`{append}`に似ていますが、もととなる配列を変更せずに
新しい配列を作成する点が`{append}`とは異なります。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | assignする配列の変数名 (必須)
from | String | もととなる配列
key | String | キー
value | String | 値

**記載例**    

```smarty
{assign_array var="person" values=""}
{append var="person" index="name" value="Katoh"}
{append var="person" index="job" value="Sales"}
{assign_array_set var="person_ex" key="age" value="28" from=$person}

{$person_ex|@debug_print_var}

{$person|@debug_print_var}
```

**出力結果**    

```
Array (4)
name => "Katoh"
job => "Sales"
age => "28"

Array (2)
name => "Katoh"
job => "Sales"
```

## assign_csv_table

csvtable_idで示されるマスタを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
csvtable_id | Integer | マスタのID (必須)
var | String | 戻り変数の名前 (必須)
get_key_val | Boolean | オプションのパラメータの使用を有効にします。 (optional)
key_idx | Integer/Array | 返されるディメンションまたはディメンションを返します。 (optional)
value_idx | Integer | 返されるディメンションまたはディメンションを返します。 (optional)
multiple | Boolean | 次元数で場合分け (optional)
lang | String | 多言語対応している場合、言語を指定します。"ja", "en" など。
filter | String | filterの条件を指定します。(optional)
allow_list | String | filterするkey名を指定します(filterを利用する場合は必須)

**記載例**    
```smarty
{assign_csv_table csvtable_id=X var="sample_table1"}
{$sample_table1|@debug_print_var}
```

```smarty
{assign_csv_table
    csvtable_id=X
    var="sample_table2"
    get_key_val=true}
{$sample_table2|@debug_print_var}
```

```smarty
{assign_csv_table csvtable_id=X var="sample_table3" filter="key=\"test\"" allow_list="key"}
{$sample_table3|@debug_print_var}
```

## assign_favorite_cnt

お気に入り数を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
module_type | String | モジュール名。`"topics"`,`"comment"`,`"member"`,`"tag"`,`"csvtable"`,`"ec_product"` のいずれかを指定します。デフォルトは `"topics"` です。
module_id | Integer | 指定したモジュールにおけるID
var | String | 結果を格納する変数名 (必須)
time | String | strtotime フォーマット
format | String | フォーマット

**記載例**    
```smarty
{assign_favorite_cnt
    module_type="topics"
    module_id=1000
    var="favorite_cnt"}
```

## assign_globals

同一リクエスト中に呼び出されるカスタム処理間で共有可能なグローバル変数をアサインします。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | グローバル変数を格納する変数名
key | String | グローバル変数のキー
value | Mixed  | グローバル変数の値
unset | Bool | 変数の値をクリアする場合、trueを指定します。

**記載例**    
```smarty
{assign_globals key='prev_content' value=$content}
```

```smarty
{assign_globals var='prev_content' key='prev_content'}
```

## assign_group_nm

グループ名を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
group_id | Integer | グループID (必須)
var | String | 結果を格納する変数名 (必須)
lang | String | 言語コード（"ja", "en"など）

**記載例**    
```smarty
{assign_group_nm group_id=100 var='group_nm'}
```

## assign_member_detail

メンバの詳細を返します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
member_id | Int | 値のメンバID (必須)
open_by_group | Boolean | falseのとき、閲覧権限を無視します。デフォルトは `true` です。
open_flg | Int | (非推奨) -1のとき、閲覧可能なメンバーの情報しか取得できなくなります。
assign_group_flg | Boolean | グループ情報も取得するかどうか

**記載例**    
```smarty
{assign_member_detail var='varname' member_id=7}
```

## assign_my_favorite_cnt

自分がお気に入りをつけたコンテンツの数を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
module_type | String | モジュール名。`"topics"`,`"comment"`,`"member"`,`"tag"`,`"csvtable"`,`"ec_product"` のいずれかを指定します。デフォルトは `"topics"` です。
module_id | Integer | 指定したモジュールにおけるID
var | String | 結果を格納する変数名 (必須)
cookie_flg | Integer | クッキー管理のお気に入り取得フラグ
action_type | String | 対象アクション(デフォルト 0 (like))

**記載例**    
```smarty
{assign_my_favorite_cnt
    module_type="topics"
    var="favorite_cnt"
    cookie_flg=1}
```

## assign_new_comment_list

指定したコンテンツにつけられたコメントを、新しいものから順に取得します。

**属性**  

Param | Type | Description
--- | --- | ---
module_id | String | 指定したモジュールにおけるID
module_type | String | モジュール名。`"topics"`,`"comment"`,`"member"`,`"tag"`,`"csvtable"`,`"ec_product"` のいずれかを指定します。デフォルトは `"topics"` です。
var | Boolean | 結果を格納する変数名 (必須)
new_order_flg | String | `false` の場合、結果は昇順で返されます。
cnt | String | 結果の数を制限します。デフォルトは `5` です。

**記載例**    
```smarty
{assign_new_comment_list
    module_id=1
    module_type='topics'
    cnt=5
    var='new_comment_list'
}
```

## assign_pager

配列をページ分割し、そのページ分のデータとページ情報を変数に格納します。  
カスタム処理内で組み立てた配列を、一覧APIと同じ形式の `pageInfo` を付けて返す場合に利用します。

**属性**  

Param | Type | Description
--- | --- | ---
from | Array | ページ分割の対象配列 (必須)
var | String | ページ分のデータを格納する変数名。`var_pageInfo` を指定しない場合は必須です。
var_pageInfo | String | ページ情報を格納する変数名。`var` を指定しない場合は必須です。
perPage | Integer | 1ページあたりの件数。デフォルトは `20` です。
pageID | Integer | 表示するページ番号。省略した場合は、リクエストパラメータ（`urlVar`）の値が使用されます。
urlVar | String | ページ番号を受け取るリクエストパラメータ名。デフォルトは `pageID` です。

`var_pageInfo` に指定した変数には、一覧APIの `pageInfo` と同じ形式で `totalCnt` / `perPage` / `totalPageCnt` / `pageNo` / `next_page_param` などが格納されます。

**記載例**    
```smarty
{* リクエストの pageID に従ってページ分割します *}
{assign_pager from=$rows perPage=10 var="page_rows" var_pageInfo="pageInfo"}
{foreach from=$page_rows item="row"}{$row.subject}{/foreach}
```

```smarty
{* ページ番号を明示して取得します *}
{assign_pager from=$rows perPage=10 pageID=2 var="page_rows"}
```

```smarty
{* カスタム処理をAPIとして公開する場合の例です *}
{assign_pager from=$notifications perPage=20 var="items" var_pageInfo="pageInfo"}
{assign_array var="response" values=""}
{append var="response" index="list" value=$items}
{append var="response" index="pageInfo" value=$pageInfo}
{$response|@rcms_json_encode}
```

:::caution
対象配列は全件がメモリ上に載るため、あらかじめ件数を絞った配列を指定してください。  
`pageID` が総ページ数を超える場合は、最終ページに丸められます。
:::

## assign_relation_tag_list

指定したコンテンツに紐づいているタグの一覧を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
module | String | モジュール名
module_id | Integer | 指定したモジュールにおけるID（必須）
var | String | 結果を格納する変数名 (必須)
tag_category_id | Integer | タグカテゴリで絞り込みたい場合、タグカテゴリIDを指定する (オプション)
tag_relation_list | Array | タグの配列。`id` を持っている配列の配列である必要があります。<br/>指定すると`module`と`module_id`は無視され、tag_relation_listで指定したタグの詳細がvarに格納されます。 (オプション)

**記載例**    
```smarty
{assign_relation_tag_list
    module="topics"
    module_id=123
    var="rel_tag_list"}
```

```smarty
{assign_array var=tag1 values=""}
{append var=tag1 index=id value=101}
{append var=tag1 index=tag_nm value="WeaklyRecommended"}

{assign_array var=tag2 values=""}
{append var=tag2 index=id value=102}
{append var=tag2 index=tag_nm value="重要なお知らせ"}

{assign_array var=tag_list values=""}
{append var=tag_list value=$tag1}
{append var=tag_list value=$tag2}

{assign_relation_tag_list
    module="topics"
    module_id=123
    tag_relation_list=$tag_list
    var="rel_tag_list"}
```

## assign_tag_category_list

カテゴリータグをリスト化して返します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
lang | String | 言語の設定
tree_flg | Boolean | タグの階層構造 (親タグや子タグなど) の出力に関するフラグ (1でreturnする)

**記載例**    
```smarty
{assign_tag_category_list [tree_flg=true] var=tag_category_list}
```

## assign_tag_list

タグカテゴリーに紐づくタグを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
category_id | Integer | カテゴリータグのIDを指定する (必須)
order | Array | タグの出力順序を指示する配列

**記載例**    
```smarty
{assign_tag_list category_id='02' var='tag_list'}
{assign_tag_list category_id='02' order='open_contents_cnt:desc' var='tag_list'}
{assign_tag_list category_id='02' order=$tag_order var='tag_list'}
```

## assign_topics_category_list

指定されたカテゴリに紐づくコンテンツの一覧を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
topics_group_id | Integer | カテゴリ群のtopics_group_idを指定する (必須)
lang | String | 言語設定

**記載例**    
```smarty
{assign_topics_category_list
    topics_group_id=1
    var='topics_category_list'}
```

## assign_topics_detail

指定されたコンテンツの詳細情報を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
topics_id | Integer | コンテンツのID (必須)
lang | String | 言語設定
chk_open_flg | Boolean | 取得するコンテンツを公開中のもののみに限定するかどうか。デフォルトは `true` です。

**記載例**    
```smarty
{assign_topics_detail topics_id=100 var='topics_data'}
```

## backup

バックアップを実行します。

**属性**  

Param | Type | Description
--- | --- | ---
type | String | "full" を指定
memo | String | バックアップの理由などのメモ
result_var | String | 結果を格納する変数名

**記載例**    
```smarty
{backup type='full' memo='smarty' result_var='res'}
```

## backup_delete

バックアップを削除します。  

バックアップIDを指定するか、バックアップ期間（開始日および終了日）を指定する必要があります。バックアップIDを指定した場合はバックアップ期間（開始日および終了日）は無視されます。

**属性**  

Param | Type | Description
--- | --- | ---
backup_id | String | バックアップIDを指定
start_date | String | 削除する対象バックアップ期間の開始日を指定
end_date | String | 削除する対象バックアップ期間の終了日を指定
result_var | String | 結果を格納する変数名。削除に成功した場合はtrue、失敗した場合はfalseを返します。

**記載例**    
```smarty
{backup_delete backup_id='1234' result_var='res'}
```
```smarty
{backup_delete start_date='2020-01-01 00:00:00' end_date='2020-01-01 23:59:59' result_var='res'}
```

## batch

バッチ処理を登録する。

**属性**  

Param | Type | Description
--- | --- | ---
batch_id | Integer | バッチID(slugといずれかは必須)
name | String |slug(バッチIDといずれかは必須)
module | String |対象モジュール名(デフォルトバッチを登録する際に利用)
ext_data | Array | 登録したバッチに渡すデータ
var | String | 登録されたバッチのIDを格納する変数名

**記載例**    
```
{batch batch_id='1234' ext_data=$ext_data}
```

## break

foreachやsectionなどのループ内部で利用します。 breakが実行されると、プログラムはただちにループを抜けます。

**属性**  
なし。

**記載例**    
```smarty
{break}
```

## capitalize

各単語の先頭文字を大文字に変換します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| uc_digits | Boolean | 数字で始まる単語も大文字化するかどうか（任意、デフォルト `false`） |

**戻り値**

先頭文字が大文字化された文字列。

#### 記載例

```smarty
{$title|capitalize}
{"hello world"|capitalize}               {* Hello World *}
{"test 123abc hello"|capitalize}         {* Test 123abc Hello *}
{"test 123abc hello"|capitalize:true}    {* Test 123Abc Hello *}
{"it's a test"|capitalize}               {* It's A Test *}
```

補足:

- 単語の先頭がアポストロフィ `'` で始まる場合は大文字化されません。
- デフォルトでは数字で始まる単語は変換されませんが、`uc_digits=true` を指定すると数字始まりの単語も大文字化されます。
- 単語境界（`\b`）で判定するため句読点を含む文字列も正しく扱われ、`it's` のようなアポストロフィを含む語もひとつの単語として扱われます。

## cat

変数に値を連結します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| cat | Mixed | 連結する値（任意、デフォルト `""`） |

**戻り値**

連結された文字列。

#### 記載例

```smarty
{$name|cat:" Smith"}
{"Hello"|cat:" World"}
{$path|cat:".txt"}
{$count|cat:" items"}
```

補足:

- 両オペランドは `is_scalar()` で判定され、配列・オブジェクト・`null` などの非スカラー値はエラーにならず空文字列として扱われます。
- 真偽値は PHP 標準に従い `true` → `"1"`、`false` → `""` に変換されます。

## child_site

子サイトのデータを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
site_key | String | サイトキー (必須)
var | String | 結果を格納する変数名 (必須)

**記載例**    
```smarty
{child_site var='site' site_key='1234'}
```

## continue

foreachやsectionなどのループ内部で利用します。 continueが実行されると、ループ処理の残りの処理をスキップして次のループ処理に移ります。

**属性**  
なし。

**記載例**    
```smarty
{continue}
```

## conv_bool

内部関数 `convBool()` を使用して値を真偽値に変換します。フォーム入力や API レスポンス内の文字列など、さまざまな真偽相当の値を厳密な真偽値に正規化したいときに便利です。

#### 記載例

```smarty
{$value|conv_bool}

{* 条件分岐での利用 *}
{if $string_value|conv_bool}
    Value is truthy
{/if}
```

## cookie

Cookieを取得/セットします。  
値は `rcms_api_local` という単一のCookieにJSON形式で保存されます。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 取得した値を格納する変数名
key | String | Cookie内のキー名
value | String | セットする値（指定するとセット、省略すると取得）
expires | Integer | クッキーの有効期限日数
overwrite | Integer | 上書きフラグ（1: 既存の値を上書き / 0: 既存の値がある場合はスキップ）

**記載例**    

セット:
```smarty
{* key="foo" に値 "test" をセットする（有効期限30日、上書きあり） *}
{cookie key="foo" value="test" expires=30 overwrite=1}
```

取得:
```smarty
{* key="foo" の値を取得して変数 $myVar に格納する *}
{cookie key="foo" var="myVar"}
{$myVar} {* → "test" *}
```

## copy_s3_temp_file

一時アップロード用のエンドポイント（Files::create_temp_upload_url / Files::create_temp_upload_post / Files::temp_upload_url）でアップロードされた一時ファイルを、指定したパスへコピーします。

:::info
`file_id`には、自サイトの一時アップロード用エンドポイントのレスポンスで返される一時ファイルID（`files/temp/kuroco/{site_key}/{uuid}`または`files/temp/kuroco/{site_key}/{uuid}.{拡張子}`形式）のみ指定できます。それ以外のfile_id（エンドポイントの`storage`に`S3`を指定して取得したfile_idを含む）を指定した場合、コピーは実行されません。

コピー先（`dest_path`）に指定できるのは、クラウドストレージパス（`/files/g/`、`/files/a/`）および`/files/temp/`以下のパスのみです。KurocoFilesのパス（`/files/user/`等）はコピー先としてサポートされていません。
:::

**属性**  

| Param | Type | Description |
| :--- | :--- | :--- |
| file_id | String | コピー元のfile_id。一時アップロード用エンドポイントのレスポンスで返される一時ファイルIDを指定します。(必須) |
| dest_path | String | コピー先のファイルパス（例: `/files/g/public/uploaded.png`）。(必須) |
| status_var | String | コピー結果を格納する変数名（成功: `true` / 失敗: `false`） |

**記載例**    

```smarty
{* 一時ファイルをクラウドストレージの公開ディレクトリへコピー *}
{copy_s3_temp_file file_id=$file_id dest_path="/files/g/public/uploaded.png"}
```

```smarty
{* 結果を取得 *}
{copy_s3_temp_file file_id=$file_id dest_path="/files/g/private/uploaded.png" status_var="result"}
{if $result}
    <p>コピー成功</p>
{else}
    <p>コピー失敗</p>
{/if}
```

補足:

- 必須パラメータが不足している場合や、`file_id`・`dest_path`が許可されていない値の場合、コピーは実行されず`status_var`で指定した変数には`false`が格納されます。
- コピーしたファイルの公開/非公開（ACL）は、コピー先のパスから自動的に判定されます。
- コピー時にContent-Typeはファイルの内容から自動設定されます。

## count

配列の要素数をカウントします。PHP7互換のSmarty countモディファイアです。

**戻り値**

配列の要素数を表す整数を返します。入力が配列でない場合は `0` を返します。

#### 記載例

```smarty
{$array|count}
```

補足:

- インデックス配列と連想配列のどちらでも動作し、空配列に対しては `0` を返します。
- PHP ネイティブの `count()` とは異なり、非配列値に対して `1` ではなく `0` を返します。

## count_characters

テキストに含まれる文字数をカウントします。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| include_spaces | Boolean | 空白文字をカウントに含めるか（任意、デフォルト `false`） |

**戻り値**

文字数を表す整数。

#### 記載例

```smarty
{"Hello World"|count_characters}       {* 10 *}
{"Hello World"|count_characters:true}  {* 11 *}
{"Tab\there"|count_characters}         {* 7 - excludes tab *}
```

補足:

- `include_spaces=false`（デフォルト）の場合、空白・タブ・改行・キャリッジリターン・改ページ・垂直タブはカウントから除外されます。
- マルチバイト非対応 — バイト単位でカウントするため、ASCII やシングルバイトエンコーディングでの利用を想定しています。

## count_paragraphs

テキストの段落数をカウントします。

**戻り値**

段落数を表す整数。

#### 記載例

```smarty
{$article|count_paragraphs}
{"First paragraph\n\nSecond paragraph"|count_paragraphs}  {* 2 *}
{"Line1\nLine2\nLine3"|count_paragraphs}                  {* 3 *}
{"Single line"|count_paragraphs}                          {* 1 *}
```

補足:

- 1 文字以上の改行コード（`\r`、`\n`、`\r\n`）でテキストを分割し、得られた要素数を返します。
- 連続する改行はひとつの区切りとして扱われ、空文字列は `1` を返します。

## count_sentences

テキストに含まれる文の数をカウントします。

**戻り値**

文の数を表す整数。

#### 記載例

```smarty
{$text|count_sentences}
{"Hello. How are you? I'm fine."|count_sentences}  {* 3 *}
{"Mr. Smith went home."|count_sentences}           {* 1 - "Mr." not counted *}
{"End of line."|count_sentences}                   {* 1 *}
```

補足:

- 直前が非空白で直後が単語文字でないピリオドのみをカウントします。そのため `Dr.` や `Mr.` のような略語の後に文字列が続く場合はカウントされません。
- カウント対象はピリオドのみで、`?` や `!` はカウントされません。

## count_words

テキストの単語数をカウントします。

**戻り値**

単語数を表す整数。

#### 記載例

```smarty
{$text|count_words}
{"Hello world 123"|count_words}     {* 3 *}
{"   spaces   only   "|count_words} {* 2 *}
{"!!!"|count_words}                 {* 0 - no alphanumerics *}
```

補足:

- 空白でトークンに分割した後、英数字（ASCII の `a-z`/`A-Z`/`0-9`、および拡張・マルチバイト領域 `0x80`–`0xff`）を 1 文字以上含むトークンだけをカウントします。
- 句読点だけからなるトークンは単語としてカウントされません。

## date

日付に関する変数をassignします。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
time | String | strtotime フォーマット
format | String | フォーマット

**記載例**    
```smarty
{date var='yesterday' time='Yesterday' format='Y-m-d'}
{date var='today' format='Y-m-d H:i:s'}
```

## date_format

PHP の `date()` フォーマットを使ってタイムスタンプを整形します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| format | String | 日付フォーマット文字列（任意、デフォルト `'Y-m-d'`） |
| default_date | String | 入力が空のときに使用するデフォルト日付（任意、デフォルト `''`） |

**戻り値**

整形された日付文字列。入力と `default_date` の両方が空の場合は何も返しません。

#### 記載例

```smarty
{$timestamp|date_format}
{$date|date_format:"%Y-%m-%d"}
{$datetime|date_format:"Y-m-d H:i:s"}
{"2024-01-15"|date_format:"F j, Y"}
{$maybe_empty|date_format:"Y-m-d":"2024-01-01"}
```

補足:

- 入力のパースには `smarty_make_timestamp()` を使用し、Unix タイムスタンプ・日付文字列・MySQL 形式の値などをサポートします。
- フォーマット文字列に `%` が含まれている場合、strftime 形式のコード（`%Y`→`Y`、`%m`→`m`、`%d`→`d`、`%H`→`H`、`%M`→`i`、`%S`→`s` など）を PHP `date()` 用の書式に変換してから整形します。

## debug_print_var

デバッグコンソールで表示する用に変数の内容を整形します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| depth | Integer | 現在の再帰深度（内部利用、任意、デフォルト `0`） |
| length | Integer | 切り詰めまでの最大文字数（任意、デフォルト `300`） |

**戻り値**

HTML 形式に整形された変数表現。

#### 記載例

```smarty
{$var|debug_print_var}
{$array|debug_print_var:0:100}
```

補足:

- 配列は `Array (件数)`、オブジェクトは `ClassName Object (件数)`、真偽値は `<i>true</i>`/`<i>false</i>`、`null` は `<i>null</i>` として表示します。
- 特殊文字は HTML のイタリック（`<i>\n</i>`、`<i>\r</i>`、`<i>\t</i>`）として描画され、文字列は `rcms_mbtruncate()` で `...` を付けて切り詰められます。出力は `htmlspecialchars()` でエスケープされます。

## default

空の変数に対するデフォルト値を提供します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| default | Mixed | 空の場合に返すデフォルト値（任意、デフォルト `''`） |

**戻り値**

入力が未設定または空文字列のときは `default`、そうでなければ元の値を返します。

#### 記載例

```smarty
{$name|default:"Anonymous"}
{$count|default:0}
{$message|default:"No message"}
```

補足:

- 未設定の値、または空文字列 `''`（厳密比較）だけを「空」とみなします。
- `0` や `false` などの falsy な値は「空」として扱いません。この点が PHP の `empty()` とは異なります。

## detect_document_text

PDF/TIFFファイルからGoogle Cloud Vision APIを使用してテキストを検出（OCR）します。

:::info
このプラグインはバッチ処理、または管理画面のテストモードでのみ実行可能です。
:::

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を代入する変数名 (必須)
dir | String | ファイルディレクトリ（例: `/files/topics`）(必須)
file_nm | String | ファイル名（`module_id`未使用時に必須）
module_id | Integer | モジュールID（`file_nm`未使用時に必須）
ext_id | Integer | 拡張項目ID
no | Integer | ファイル番号（デフォルト: `/files/topics` の場合は `0`、それ以外は `null`）
lang | String | 言語コード
slug | String | スラッグ
type | String | 出力形式: `"text"`（デフォルト）または `"array"`
no_cache | Boolean | キャッシュを無効にする（デフォルト: `false`）

対象ファイルの指定方法は2つあります。

1. **ファイル名で指定**: `dir` と `file_nm` を指定します。
2. **モジュールパラメータで指定**: `dir` と `module_id` を指定し、必要に応じて `ext_id`、`no`、`lang`、`slug` などのオプションパラメータを指定します。

**出力形式**

- `type="text"`（デフォルト）の場合: 全ページの検出テキストが改行2つ（`\n\n`）で結合された文字列として返されます。
- `type="array"`の場合: `page`（ページ番号）と`value`（検出テキスト）を含むオブジェクトの配列として返されます。

エラーが発生した場合（対応していないファイル形式、ファイルが見つからない等）は、空配列`[]`が変数に代入されます。

**対応ファイル形式**

- PDF (`.pdf`)
- TIFF (`.tiff`)

:::caution
S3にホスティングされているファイルは対応していません。
:::

**利用可能なファイルディレクトリ**

このプラグインを利用可能なファイルは以下になります。

- `/files/topics` (GCS/KurocoFiles)
- `/files/inquiry` (GCS/KurocoFiles)
- `/files/member/ext` (GCS/KurocoFiles)
- `/files/d` (KurocoFiles)

**キャッシュ**

抽出されたテキストはデータベースにキャッシュされます。同一ファイルに対する次回以降の呼び出しでは、ファイルが更新されていなければキャッシュされた結果が返されます。`no_cache=true`を指定するとキャッシュを無効化できます。

**記載例**    
```smarty
{* ファイル名で指定 *}
{detect_document_text var="text" dir="/files/d" file_nm="document.pdf"}

{* モジュールIDで指定 *}
{detect_document_text var="text" dir="/files/topics" module_id=123 ext_id=1}

{* 配列形式で取得 *}
{detect_document_text var="pages" dir="/files/d" file_nm="document.pdf" type="array"}

{* キャッシュ無効化 *}
{detect_document_text var="text" dir="/files/topics" module_id=123 ext_id=1 no_cache=true}
```

## empty

値が空かどうかを判定します。`stdClass` オブジェクトについては拡張された処理を行います。

**戻り値**

空の場合は `true`、それ以外は `false` を返します。

#### 記載例

```smarty
{if $value|empty}Value is empty{/if}

{* オブジェクトに対しても動作 *}
{if $object|empty}Object has no properties{/if}
```

補足:

- 空とみなされる値: 空文字列 `""`、`0`、`null`、`false`、空配列 `[]`。
- プロパティを持たない `stdClass` オブジェクトについても `true` を返します。API レスポンスが空オブジェクトを返すケースなどで便利で、PHP ネイティブの `empty()` とは挙動が異なります。

## escape

指定したタイプに従って文字列をエスケープします。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| esc_type | String | エスケープタイプ: `html`、`htmlall`、`url`、`urlpathinfo`、`quotes`、`hex`、`hexentity`、`decentity`、`javascript`、`mail`、`nonstd`（任意、デフォルト `'html'`） |
| char_set | String | 文字セット（任意、デフォルト `'UTF-8'`） |

**戻り値**

エスケープされた文字列。

#### 記載例

```smarty
{$html|escape}
{$html|escape:"html"}
{$url|escape:"url"}
{$js_string|escape:"javascript"}
{$email|escape:"mail"}
```

補足:

- 主なエスケープタイプ: `html`（`ENT_QUOTES` 付きの `htmlspecialchars`）、`htmlall`（`ENT_QUOTES` 付きの `htmlentities`）、`url`（`rawurlencode`）、`urlpathinfo`（`url` と同様だが `/` を保持）、`quotes`（未エスケープのシングルクォートをエスケープ）、`hex`/`hexentity`/`decentity`（1 文字単位のエンコード）、`javascript`（バックスラッシュ・クォート・改行のエスケープと `</` → `<\/`）、`mail`（`@` と `.` を `[AT]`・`[DOT]` に置換）、`nonstd`（文字コード 126 以上の文字をエスケープ）。
- `null` や非スカラー値は空文字列を返します。未知のエスケープタイプを指定した場合は入力をそのまま返します。

## explode

区切り文字で文字列を配列に分割します。PHP8 互換で型安全に処理します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| string | String/Number | 分割対象の文字列（必須） |

**戻り値**

区切り文字で分割した文字列の配列。空文字列または文字列・数値以外の型が渡された場合は空配列 `[]` を返します。

#### 記載例

```smarty
{* 基本的な分割 *}
{','|explode:$csv_string}

{* パスの分割 *}
{'/'|explode:$file_path}

{* 数値入力も使用可 *}
{'-'|explode:12345}
```

補足:

- 区切り文字を修飾子入力として渡し、分割対象の文字列はコロンの後に指定します。
- 数値（int/float/double）は自動的に文字列に変換されてから分割されます。
- 正規表現はサポートされず、リテラル区切り文字のみを扱います。正規表現が必要な場合は `split` モディファイアを使用してください。

## function

カスタム関数をコールします。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
id | Integer | カスタム関数ID
name | String | カスタム関数の識別子

**記載例**    

以下のように、カスタム処理「sub_funtion」に記述し`function`プラグインで呼び出した場合、変数 `$result` には `"Hello World"` が代入されます。

```smarty
{* 呼び出し元 *}
{function name="sub_function" var="result" param1="Hello" param2="World"}
```
```smarty
{* 呼び出し先のカスタム処理。識別子：sub_function *}
{assign var="message" value=$param1|cat:" "|cat:$param2}
{return value=$message}
```

## gcloud_functions_token

Google Cloud Functionsの認証用bearerトークンを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
url | String | 関数のURL (必須)
sa_secret_name | String | secret_edit画面で設定したサービスアカウントのシークレット名

**記載例**    
```smarty
{gcloud_functions_token
    var="id_token"
    url="https://us-central1-**.cloudfunctions.net/functionName"
    sa_secret_name='GCP_MY_CREDENTIAL'}
```

## gcloud_pubsub_publish

Google Cloud Pub/Subのメッセージを配信します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
topic | String | 配信先のTopic名 (必須)
message | Any | 配信するメッセージ (必須)
project | String | GCPのプロジェクト名
sa_secret_name | String | secret_edit画面で設定したサービスアカウントのシークレット名

**記載例**    
```smarty
{gcloud_pubsub_publish
    var='result'
    project='projectName'
    topic='topicName'
    message=$message
    sa_secret_name='MY_GCP_CREDENTIAL'}
```

## generate_pdf

指定されたURLをもとに、PDFや画像を生成します。生成されたファイルはGCS上に保存されます。  

なお、generate_pdfでは、ヘッドレスブラウザの[Puppeteer](https://github.com/puppeteer/puppeteer)を使用しています。ヘッドレスブラウザの幅や高さ下記の各種オプションによって挙動を制御できます。

**前提条件**  
generate_pdfを利用するためには、Firebaseと連携が必要になります。
[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)を参考に連携してください。

**属性**  

| 項目 | 用途 | 記載例 |
| :--- | :--- | :--- |
| url | PDF化するページURLを記載します。 | `https://www.diverta.co.jp` |
| path | 生成したPDFのファイル格納場所を記載します。<br/>`files/g/private/` または `files/g/public/` 配下となります。 | `files/g/private/sample.pdf` |
| option | PDF化のオプションを記載します。 ||
| browser_width | ブラウザ幅を指定します。 | `browser_width=1280` |
| browser_height | ブラウザの高さを指定します。 | `browser_height=2560` |
| sleep | 指定したページをキャプチャするまでの待機時間（ミリ秒）を指定します。 | `sleep=1000` |
| ua | ユーザーエージェントを指定します。 <br/>`url`で指定した対象ページが、アクセスしてきたブラウザのユーザーエージェントによって表示が切り替わるようなページの場合にこのオプションを使うと便利です。<br/>注意：正しい文字列を送信しないと意図した通りに切り替わらない可能性があります。対象のWEBサイトの仕様をお確かめの上ご利用ください。 | `ua="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"` |
| format | 保存するファイルのフォーマットを指定します。<br/>`pdf`、 `png`、 `jpeg`、 `jpg`、 `webp` が指定可能です。 | `format="png"` |
| cookie | ログインが必要なURLをPDF化するに指定します。<br/>`$smarty.cookies` の形式を想定してます。<br/>注意：バッチ処理にてこのプラグインを利用する場合、`$smarty.cookies` は空になりますので利用できません。pre-process や post-process からカスタム処理をコールする場面でご利用ください。 | `cookie=$smarty.cookies` |
| domain | クッキーのドメインを指定します。 | `domain="www.diverta.co.jp"` |
| overwrite | ファイルが既に存在する場合に、上書きするかどうかを指定します。 | `overwrite=1` |
| callback_batch | PDFが生成された後にKurocoのバッチ処理を実行したい場合に、バッチ処理のスラッグ名を指定します。 | `callback_batch="my_callback_batch"` |
| data | その他のパラメータを指定できます。このパラメータは上述のバッチ処理に引き渡されます。 | `data=$smarty.request.data` |

**記載例**    

```smarty
{generate_pdf
    url="https://www.diverta.co.jp"
    path="files/g/private/sample.pdf"
    cookie=$smarty.cookies
    domain="www.diverta.co.jp"
}
```

**関連ドキュメント**  
`generate_pdf`の具体的な利用方法については、[定期的に外部サイトのキャプチャをPDF化する](/ja/docs/tutorials/how-to-use-generate-pdf/) をご確認ください。

## get_file

S3,GCS,外部URLなどからファイルを取得します。

**属性**  

Param | Type | Description
--- | --- | --
var | String | 結果を格納する変数名
path | String | 取得したいファイルのS3/GCS上でのパス
url | String | 取得したいファイルのURL
bucket | String | 取得したいファイルが置かれているS3/GCSのバケット名
save | Boolean | 取得したファイルをKurocoの一時領域に保存するかどうか。falseとした場合は保存せずに、varで指定した変数にファイルの内容を保存します。
save_path | String | 取得したファイルを保存するファイル名

**記載例**    
```smarty
{get_file path=$path}
```

```smarty
{get_file url="https://www.diverta.co.jp/RSS.rdf" save_path="/files/user/rss/RSS.rdf" var="temp"}
```

```smarty
{get_file url="https://www.diverta.co.jp/RSS.rdf" var="temp_file" save=false}
{if $temp_file|strlen>0}
    ファイルが見つかりました
{else}
    ファイルが見つかりません
{/if}
```

## github_deploy

GitHub連携し、フロントソースのビルド・デプロイを行います。

**属性**  

Param | Type | Description
--- | --- | ---
result_var | String | true: success false: failure

**記載例**    
```smarty
{github_deploy result_var='res'}
```

## googleanalytics

GoogleAnalyticsからデータを取得し、カウンター用のテーブルに値をセットします。  
[batch](#batch)のSmartyプラグインでsync_counterのバッチ処理にコンテンツIDを渡すと、セットした値をコンテンツに反映できます。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | GoogleAnalyticsから取得したデータをアサインする変数名
updated_topics_ids | Array | カウンターの値がセットされたコンテンツIDの配列
update_column_slug | String | アップデートするカラムのSlug
update_column_index | Integer | アップデートするカラムのindex
update_target_metric | String | 利用するメトリック
update_target_dimension | String | アップデートするカスタムディメンション
topics_group_id | Integer | コンテンツ定義ID
startDate | String | 集計開始日。PHPのstrtotime()で解釈できる文字列。デフォルトは7日前。
endDate | String | 集計終了日。PHPのstrtotime()で解釈できる文字列。デフォルトは本日。
queries | String | クエリの直接指定

**記載例**    
```smarty
{googleanalytics
    var="result"
    update_column_slug="pv"
    update_target_dimension="customEvent:slug"
    updated_topics_ids='updated_topics_ids'
    topics_group_id=1}

{assign_array var=ext_data values=''} 
{assign var=ext_data.topics_ids value=$updated_topics_ids} 
{batch module='topics' name='sync_counter' ext_data=$ext_data}
```

## gzip

ファイルをgzip圧縮してクラウドストレージにアップロードします。

**前提条件**  
gzipを利用するためには、Firebaseと連携が必要になります。
[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)を参考に連携してください。

:::info
保存先（`dest`）はGCSパス（`/files/g/`）である必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は保存先としてサポートされていません。
:::

**属性**  

| Param | Type | Description |
| :--- | :--- | :--- |
| file_url | String | 圧縮するファイルのパス。GCSパス（`/files/g/`）、または`https://`から始まるURLを指定できます。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は直接サポートされていませんが、KurocoFiles（公開）のファイルについては公開URL（例: `https://[site].g.kuroco-img.app/files/user/...`）を使用することで指定可能です。(必須) |
| dest | String | gzipファイルを保存するパス。GCSパス（`/files/g/`）である必要があります。{/* 省略した場合は一時ファイルパスが自動生成されます。 */} |
| bucket | String | バケット名。省略した場合は [外部システム連携] - [Firebase] で設定したStorageが利用されます。 |
| callback_batch | String | gzip圧縮処理完了後にコールバックするバッチ処理の識別子 |
| data | Mixed | 任意のデータ。コールバックバッチに引き渡されます。 |

**出力変数**

| 変数名 | 説明 |
| :--- | :--- |
| gzip_dest | gzipファイルが保存されるパス。実行後に自動的にassignされます。 |

**記載例**    
```smarty
{gzip
    file_url='https://[site].g.kuroco-img.app/files/user/data.csv'
    dest='/files/g/public/data.csv.gz'
}
```

```smarty
{gzip
    file_url='/files/g/private/test/image.png'
    dest='/files/g/public/test/image.gz'
    callback_batch='gzip_complete_handler'
    data=$callback_data
}
```

## html5_check

HTML5の構文検証を行います。指定されたHTMLコンテンツに対してHTML5の構文チェックを実行し、エラーがあった場合は詳細な情報を変数に格納します。

**属性**  

Param | Type | Description
--- | --- | ---
html | String | 検証するHTMLコンテンツ (必須)
var | String | エラー結果を格納する変数名 (デフォルト: 'html5_errors')

**記載例**  
```smarty
{html5_check html=$html_content var="myErrors"}
{if $myErrors|@count > 0}
    {foreach from=$myErrors item=error}
        <p>{$error}</p>
    {/foreach}
{/if}
```

## implode

区切り文字を使って配列要素を文字列に連結します。PHP7 互換で引数順序を柔軟に扱えます。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| value1 | String or Array | 区切り文字、または連結する配列（必須） |
| value2 | String or Array | 連結する配列、または区切り文字（任意、デフォルト `null`） |

**戻り値**

すべての配列要素を区切り文字で連結した文字列を返します。配列が `null` または空の場合は空文字列 `''` を返します。引数の組み合わせが該当しない場合は `null` を返します。

#### 記載例

```smarty
{* 標準的な引数順: separator|implode:array *}
{assign var='arr' value='["1","2","3"]'|json_decode}
{','|implode:$arr}  {* 出力: '1,2,3' *}

{* 区切り文字を省略（空文字列で連結） *}
{$arr|@implode}     {* 出力: '123' *}

{* PHP7 互換のレガシー順: array|@implode:separator *}
{$arr|@implode:','} {* 出力: '1,2,3' *}

{* 区切り文字 + null 配列（空文字列を返す） *}
{','|implode:null}  {* 出力: '' *}
```

補足:

- 標準形式（`separator|implode:array`）とレガシー形式（`array|@implode:separator`）の両方の引数順に対応しています。
- 配列を第一引数に渡す場合は、Smarty が要素ごとに反復処理しないよう `@` を付けて使用してください。

## in_array

配列内に値が存在するかをチェックします。PHP7 互換で型を安全に扱います。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| haystack | Array | 検索対象の配列（必須） |
| strict | Boolean | `true` の場合は厳密な型比較（`===`）を行う（任意、デフォルト `false`） |

**戻り値**

値が配列内に見つかった場合は `true`、それ以外は `false` を返します。`haystack` が配列でない場合も `false` を返します。

#### 記載例

```smarty
{* 基本的な使用例 *}
{if $value|in_array:$array}Value exists{/if}

{* 厳密な型比較 *}
{if $value|in_array:$array:true}Value exists (strict){/if}

{* $array が配列でなくても安全に動作 *}
{if "apple"|in_array:$fruits}Apple is in the list{/if}
```

補足:

- `haystack` が配列でない場合もエラーにはならず、安全に `false` を返します。
- デフォルトは緩やかな比較で、第三引数に `true` を渡すと厳密比較に切り替わります。

## increment_counter

コンテンツのカウンター型の拡張項目の値に指定した数値を加算します。

**属性**  

Param | Type | Description
--- | --- | --
var| String | 加算後の結果をassignする変数名
value | Integer | 加算する数値 (必須)
topics_group_id | Integer | コンテンツ定義ID (必須)
slug | String |  対象のコンテンツのID/Slug (必須)
ext_slug | String | 対象の項目のID/Slug (必須)
index | Integer | 0から始まる繰り返しの順番

**記載例**    
```smarty
{increment_counter
    var='result'
    value=3
    topics_group_id=10
    slug='a-content'
    ext_slug='a_col_slug'
    index=0
}
```

## indent

テキストの各行をインデントします。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| chars | Integer | インデント文字数（任意、デフォルト `4`） |
| char | String | インデントに使う文字（任意、デフォルト `" "`） |

**戻り値**

インデント済みの文字列。

#### 記載例

```smarty
{$code|indent}
{$text|indent:8}
{$html|indent:2:"\t"}
```

補足:

- マルチライン正規表現を使ってすべての行頭（先頭行を含む）にインデントを挿入します。
- スペース以外の任意の文字（タブなど）も指定でき、コード整形や入れ子のコンテンツに便利です。

## join

区切り文字を使って配列要素を文字列に連結します。`implode` モディファイアのエイリアスで、機能は同一です。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| value1 | String or Array | 区切り文字、または連結する配列（必須） |
| value2 | String or Array | 連結する配列、または区切り文字（任意、デフォルト `null`） |

**戻り値**

すべての配列要素を区切り文字で連結した文字列を返します。配列が `null` または空の場合は空文字列 `''` を返します。引数の組み合わせが該当しない場合は `null` を返します。

#### 記載例

```smarty
{* 標準的な引数順: separator|join:array *}
{assign var='arr' value='["1","2","3"]'|json_decode}
{','|join:$arr}  {* 出力: '1,2,3' *}

{* 区切り文字を省略（空文字列で連結） *}
{$arr|@join}     {* 出力: '123' *}

{* PHP7 互換のレガシー順: array|@join:separator *}
{$arr|@join:','} {* 出力: '1,2,3' *}

{* 文字列入力（そのまま返される） *}
{assign var='str' value='foo'}
{$str|join}      {* 出力: 'foo' *}
```

補足:

- `join` は `implode` に処理を委譲します。標準・レガシーの両方の引数順をサポートし、配列を第一引数に渡す場合は `@` を付けてください。

## json_decode

JSON 文字列をデコードして PHP の値に変換します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| assoc | Boolean | `true` のときはオブジェクトではなく連想配列として返す（任意、デフォルト `true`） |

**戻り値**

デコードされた値。デフォルトでは JSON オブジェクトを連想配列として返します。入力が文字列でない場合や JSON が無効な場合は `null` を返します。

#### 記載例

```smarty
{* 基本的な使用例 - デフォルトで連想配列を返す *}
{assign var='data' value='{"name":"John","age":30}'|json_decode}
{$data.name}  {* 出力: John *}

{* JSON 配列のデコード *}
{assign var='items' value='["apple","banana","orange"]'|json_decode}
{$items[0]}  {* 出力: apple *}

{* 配列ではなくオブジェクトとして返す *}
{assign var='obj' value='{"name":"John"}'|json_decode:false}
{$obj->name}  {* 出力: John *}
```

補足:

- PHP ネイティブの `json_decode()` と異なり、`assoc` のデフォルトは `true` で、連想配列として返します。
- 入力が文字列でない場合や JSON が不正な場合は `null` を返します。API レスポンスや DB に格納された JSON データを解析するのに便利です。

## kick_spider

WEBクローラー（スパイダー）を実行します。  
指定したスパイダー設定IDのクローラーを起動し、クロール履歴IDを返します。[バッチ処理](#batch)と組み合わせることで、定期的なクロールの自動実行が可能です。

**属性**

| Param | Type | Description |
| :--- | :--- | :--- |
| var | String | クロール履歴ID（spider_history_id）を格納する変数名（必須） |
| spider_settings_id | Integer | スパイダー設定ID（必須） |
| spider_history_id | Integer | 再実行する場合のスパイダー履歴ID |
| target_urls | Array | クロール対象URLの配列。指定した場合、スパイダー設定の開始URLの代わりにこのURLがクロールされます。 |

**記載例**

基本的な使用例:
```smarty
{kick_spider var='spider_history_id' spider_settings_id=1}
```

バッチ処理で自動実行する例:
```smarty
{kick_spider var='spider_history_id' spider_settings_id=1}
{if $spider_history_id}
    {logger msg1="Spider kicked successfully" msg2=$spider_history_id}
{/if}
```

特定のURLのみをクロールする例:
```smarty
{assign_array var='urls' values='https://example.com/page1,https://example.com/page2'}
{kick_spider var='spider_history_id' spider_settings_id=1 target_urls=$urls}
```

:::info
`kick_spider` でクロールを実行するには、対象のスパイダー設定のステータスが「有効」になっている必要があります。
:::

**関連ドキュメント**  
- [WEBクローラーの設定方法](/ja/docs/tutorials/setting-up-web-crawler/)
- [WEBクローラー](/ja/docs/management/spider-list/)

## logger

info.logに記録します。
[オペレーション]->[ログイ管理]->[カスタムログ]で確認できます。

**属性**  

Param | Type | Description
--- | --- | ---
msg1 | String | 文字列1(1KB以内)
msg2 | String | 文字列2(1KB以内)
msg3 | String | 文字列3(1KB以内)
msg4 | String | 文字列4(1KB以内)

**記載例**    
```smarty
{logger msg1=$log1 msg2=$log2}
```

## login

ログインします。

**属性**  

Param | Type | Description
--- | --- | ---
member_id | Integer | メンバーID
overwrite | Boolean | 既にログイン中の場合、現在のセッションを上書きするか（ログインし直すか）。

**記載例**    
```smarty
{login member_id=2 overwrite=false}
```

## logout

ログアウトします。

**属性**  
なし。

**記載例**    
```smarty
{logout}
```

## lottery

抽選関数。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
cnt | Integer | 抜きだすID数
duplicate | Integer | 重複数
ids | Array | 対象のID (必須)
exclude_ids | Array | 除くID

**記載例**    
```smarty
{lottery
    var='foo'
    cnt=3
    duplicate=0
    ids=$ids
    exclude_ids=$exclude_ids}
```

## lower

文字列を小文字に変換します。

#### 記載例

```smarty
{"HELLO"|lower}        {* hello *}
{$name|lower}
{"ABC123"|lower}       {* abc123 *}
```

補足:

- PHP の `strtolower()` をそのまま使用するためマルチバイト非対応です。UTF-8 を扱う場合は型ガード付きの `strtolower` モディファイアか、PHP の `mb_strtolower()` を利用してください。

## mb_truncate

指定された長さに文字列を切り詰めます（マルチバイト対応）。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| length | Integer | 最大長（任意、デフォルト `80`） |
| etc | String | 切り詰めたときに末尾に付与する文字列（任意、デフォルト `'...'`） |
| break_words | Boolean | 単語の途中で切るかどうか（任意、デフォルト `false`） |
| middle | Boolean | 真ん中で切り詰めるかどうか（任意、デフォルト `false`） |

**戻り値**

切り詰めた文字列。

#### 記載例

```smarty
{$long_text|mb_truncate:50}
{$text|mb_truncate:30:"...":true}
{$string|mb_truncate:100:"[more]":false:true}
```

補足:

- `mb_strlen`/`mb_substr` を使用しており、UTF-8 などマルチバイトエンコーディングでも安全に動作します。
- `etc` の長さは出力全体の長さに含まれます。`middle=true` の場合は先頭半分と末尾半分を残し、その間を `etc` でつなぎます。
- 文字列が `length` 以下の場合はそのまま返されます。`length=0` のときは即座に空文字列を返します。

## mbtruncate

マルチバイト文字対応で文字列を切り詰めます。内部的に `rcms_mbtruncate()` 関数に委譲します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| length | Integer | 結果の最大文字数（任意、デフォルト `80`） |
| etc | String | 切り詰め時に追加される接尾辞（任意、デフォルト `'...'`） |

**戻り値**

切り詰められた文字列を返します。切り詰めが発生した場合はオプションの接尾辞が付きます。

#### 記載例

```smarty
{* 基本的な使用例（デフォルト80文字、'...'接尾辞） *}
{$long_text|mbtruncate}

{* カスタム長さ *}
{$text|mbtruncate:50}

{* カスタム長さと接尾辞 *}
{$text|mbtruncate:100:'...more'}

{* 接尾辞なし *}
{$text|mbtruncate:50:''}
```

マルチバイト文字（日本語、中国語、韓国語など）を適切に処理し、マルチバイト文字の途中で切断することはありません。

## msgpack_pack

データをMessagePackバイナリ形式に変換します。

注意：配列に対する修飾子になるので、@をつける必要があります。スカラー値（文字列、数値など）もpackできますが、`msgpack_unpack`はデコード結果が配列またはオブジェクトの場合のみデータを返すため、unpcackできない点にご注意ください。

**属性**  

Position | Type | Description
--- | --- | ---
target | Mixed | 変換するデータ (必須)。null、スカラー値（int、float、bool、string）、配列、またはstdClassオブジェクトのみで構成されている必要があります。

**記載例**    
```smarty
{assign_array var='data' values="test,1234"}
{assign var='packed' value=$data|@msgpack_pack}
```

**戻り値**

成功した場合はMessagePackバイナリデータを返します。入力データに無効な型（リソースやカスタムオブジェクトなど）が含まれている場合、またはエンコードに失敗した場合は`false`を返します。

## msgpack_unpack

MessagePackバイナリデータを配列またはオブジェクトにデコードします。

注意：この修飾子はデコード結果が配列またはオブジェクトの場合のみデータを返します。元のpackされたデータがスカラー値（文字列、数値など）の場合は`false`が返されます。

**属性**  

Position | Type | Description
--- | --- | ---
target | String | デコードするMessagePackバイナリ (必須)

**記載例**    
```smarty
{assign_array var='data' values="test,1234"}
{assign var='packed' value=$data|@msgpack_pack}
{assign var='unpacked' value=$packed|msgpack_unpack}

{$data|@debug_print_var}
{$unpacked|@debug_print_var}
```

**戻り値**

成功した場合はデコードされたデータ（配列またはオブジェクト）を返します。入力が有効な文字列でない場合、デコードに失敗した場合、またはデコード結果が配列やオブジェクトでない場合は`false`を返します。

## nl2br

改行を HTML の `<br>` タグに変換します。

**戻り値**

各改行の前に `<br />` タグが挿入された文字列。

#### 記載例

```smarty
{$text|nl2br}
{"Line 1\nLine 2"|nl2br}
{* 出力: Line 1<br />
Line 2 *}
```

補足:

- PHP の `nl2br()` をそのまま使用しており、`\r\n`・`\r`・`\n` の前に `<br />` を挿入しますが、もとの改行文字はそのまま残します。
- 連続する改行はそれぞれが個別に `<br />` タグに変換されます。

## pg_dateformat

日付と時間をフォーマットに基づいて整形します。
フォーマットは[DateTimeInterface::format()](https://www.php.net/manual/ja/datetime.format.php) が受け入れるフォーマットを指定してください。
曜日や月の3文字表記は、現在のロケールによって各言語での表現に変換されます。

**属性** 

Position | Type | Description
--- | --- | ---
1 | String | フォーマット

**記載例**  

```smarty
{"2024-06-01 12:34:56"|pg_dateformat}
{"2024-06-01 12:34:56"|pg_dateformat:"Y-m-d(D) [H:i:s]"}
{"2024-05-01 12:34:56"|pg_dateformat:'M'}
{"-2 days"|pg_dateformat}
{"-1 hour"|pg_dateformat}
```

**出力結果**
```
2024/06/01(土) 12:34
2024-06-01(土) [12:34:56]
5月
2024/06/19(水) 15:31
2024/06/21(金) 14:31
```

## pg_dateformat2

日付と時間をフォーマットに基づいて整形します。
フォーマットは[DateTimeInterface::format()](https://www.php.net/manual/ja/datetime.format.php) が受け入れるフォーマットを指定してください。
曜日や月の3文字表記は、現在のロケールによって各言語での表現に変換されます。
また、対象の日時が24時間以内の場合には、HTML形式で `H:i:s(s秒前に更新)` という文字に変換されます。この変換が不要な場合はpg_dateformatをご利用ください。

**属性** 

Position | Type | Description
--- | --- | ---
1 | String | フォーマット

**記載例**  

```smarty
{"2024-06-01 12:34:56"|pg_dateformat2}
{"2024-06-01 12:34:56"|pg_dateformat2:"Y-m-d(D) [H:i:s]"}
{"2023-05-01 12:34:56"|pg_dateformat2:'M'}
{"-2 days"|pg_dateformat2}
{"-1 hour"|pg_dateformat2}
```

**出力結果**
```
2024/06/01(土) 12:34
2024-06-01(土) [12:34:56]
5月
2024/06/19(水) 15:31
<span style="color:#5FAF23;font-weight:bold;">14:31:42(1時間前に更新)</span>
```

## property_exists

オブジェクトまたはクラスにプロパティが存在するかどうかをチェックします。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| property | String | チェックするプロパティ名（必須） |

**戻り値**

プロパティが存在する場合は `true`、存在しない場合は `false`。プロパティ名が文字列でない場合や、第一引数がオブジェクトでも文字列（クラス名）でもない場合は `false` を返します。

#### 記載例

```smarty
{* オブジェクトにプロパティがあるかチェック *}
{if $object|property_exists:'name'}Object has name property{/if}

{* クラス名でチェック *}
{if 'MyClass'|property_exists:'staticProperty'}Class has static property{/if}
```

オブジェクトまたはクラス名を修飾子入力として渡し、プロパティ名はコロンの後に指定します。プロパティの値が `null` であっても存在チェックは `true` を返します。

## purge_cdn_cache

CDNキャッシュをパージ(削除)します。

**属性**  

Param | Type | Description
--- | --- | ---
api_endpoint | String | エンドポイントのURLを指定します。
module | String | モジュール名を指定します。現状、`topics` 、 `csvtable` と `all` に対応しています(必須)。
topics_group_id | int | モジュール名に`topics` を指定した場合、コンテンツ定義IDを指定します。
csvtable_id | int | モジュール名に`csvtable` を指定した場合、マスタのIDを指定します。

**記載例**  

```smarty
{purge_cdn_cache api_endpoint='/rcms-api/1/list'}
{purge_cdn_cache module='all'}
{purge_cdn_cache module='topics' topics_group_id=123}
{purge_cdn_cache module='csvtable' csvtable_id=123}
```

## put_file

ファイルをKurocoFilesまたはS3/GCS領域にアップロードします。

**属性**  

Param | Type | Description
--- | --- | ---
tmp_path | String | アップロードするファイル。一時フォルダにあるファイルを指定します。
path | String | アップロード先パス
value | String | ファイルに出力する内容
files_path | String | KurocoFiles上 のパス /files/(user\|ltd)/◯◯◯。tmp_path か files_path のどちらかを指定する必要があります。
bucket | String | アップロードする S3/GCSのバケット名

**記載例**    
```smarty
{put_file tmp_path=$tmp_path path=$upload_path}
```

## rcms_arsort

連想キーと要素との関係を維持しつつ配列を降順にソートします。

注意：配列に対する修飾子になるので、@をつける必要があります。

**属性**  
なし。

**記載例**    
```smarty
{assign var="result_arr" value=$input_arr|@rcms_arsort}
```

## rcms_asort

連想キーと要素との関係を維持しつつ配列を昇順にソートします。

注意：配列に対する修飾子になるので、@をつける必要があります。

**属性**  
なし。

**記載例**    
```smarty
{assign var="result_arr" value=$input_arr|@rcms_asort}
```

## rcms_encrypt

指定の文字列を暗号化キーを利用して暗号化/復号化できます。    
サイトキーの異なるサイトでencryptしたデータは、decryptすることができません。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (任意)
action | String | 'encrypt' または 'decrypt' (必須)
data | String | 暗号化/復号化するデータ文字列 (必須)
key | String | 暗号化キー (必須) - 基本的にはシークレットの値を利用してください。
sanitize | Boolean | 復号化されたデータをサニタイズするかどうか (デフォルト: true)

**記載例**    
```smarty
{secret var='secret_key' key='secret_key'}
{rcms_encrypt var='encrypted_value' action='encrypt' data=$plaintext key=$secret_key}
{rcms_encrypt var='decrypted_value' action='decrypt' data=$encrypted_value key=$secret_key}
```

## rcms_file_size

指定されたファイルサイズを戻します。

**属性**  

Position | Type | Description
--- | --- | ---
1 | Integer | 結果の書式タイプ (default=1) <ul><li>0: 値のみ表示</li><li>1: 適切な単位を付与して表示</li></ul>
2 | Integer | 小数での結果の精度 (default=2)

**記載例**    

```smarty
{$row.path|rcms_file_size}
```

## rcms_hash

ハッシュ関数を呼び出す。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
algo | String | アルゴリズム (default=sha256)
data | String | 対象文字列 (必須)
key | String | HMAC方式の場合は秘密鍵
binary | Boolean | true を指定すると、結果をバイナリで格納します。

**記載例**    
```smarty
{rcms_hash var='foo' data='hoge' key='salt'}
```

## rcms_in_array

in_arrayを使う際に、smarty上でのis_arrayの記述を省くためのプラグイン。

**属性**  

Position | Type | Description
--- | --- | ---
1 | Array | list

**記載例**    
```smarty
{assign_array var=fruits values="apple,banana,orange"}
{if 'beef'|rcms_in_array:$fruits}
    {assign var=message value='beef is fruits.'}
{else}
    {assign var=message value='beef is not fruits.'}
{/if}
```

## rcms_json_encode

値を Unicode サポート付きで JSON 形式にエンコードし、RCMS のコンテンツ境界マーカーに対する特別な処理を行います。

**戻り値**

エスケープされていない Unicode 文字を含む JSON エンコード文字列。

#### 記載例

```smarty
{* 基本的な使用例 *}
{$array|rcms_json_encode}

{* JavaScript で使用 *}
<script>
var data = {$data|rcms_json_encode};
</script>

{* オブジェクトのエンコード *}
{$user_data|rcms_json_encode}
```

`JSON_UNESCAPED_UNICODE` フラグを使い、日本語などのマルチバイト文字をそのまま保持します。文字列に `__RCMS_CONTENT_BOUNDARY__` マーカーが含まれている場合は、エンコード前に `explode2()` で自動的に配列へ分解されます。

## rcms_krsort

配列をキーで逆順にソートします。

注意：配列に対する修飾子になるので、@をつける必要があります。

**属性**  
なし。

**記載例**    
```smarty
{assign var="result_arr" value=$input_arr|@rcms_krsort}
```

## rcms_ksort

配列をキーでソートします。

注意：配列に対する修飾子になるので、@をつける必要があります。

**属性**  
なし。

**記載例**    
```smarty
{assign var="result_arr" value=$input_arr|@rcms_ksort}
```

## rcms_match

preg_match関数を呼び出す。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
pattern | String | 検索するパターンを表す文字列
subject | String | 入力文字列
flags | Integer | 以下のフラグの組み合わせを指定できます。<br/> `256` - PREG_OFFSET_CAPTURE : このフラグを設定した場合、各マッチに対応する文字列のオフセットも(バイト単位で)返されます。 var の値を配列に変更することに注意してください。 その配列のすべての要素は、 オフセット 0 で一致した文字列、 およびその文字列のオフセット 1 での subject へのオフセットからなります。<br/>`512` - PREG_UNMATCHED_AS_NULL : このフラグが渡されると、マッチしなかったサブパターンは null として通知されます。 渡されなかった場合、空の string として通知されます。
offset | Integer | 検索の開始位置。デフォルトは先頭から。

**記載例**    
```smarty
{rcms_match
    var='foo'
    pattern='/^ex+/'
    subject='example'
    flags=256}
{rcms_match
    var='foo'
    pattern='/^ex+/'
    subject='example'
    flags=512
    offset=2}
```

## rcms_match_all

preg_match_all関数を呼び出す。

**属性**  

Param | Type | Description
--- | --- | ---
var | Array | 結果を格納する変数名 (必須)
pattern | String | 検索するパターンを表す文字列
subject | String | 入力文字列
flags | Integer | 以下のフラグの組み合わせを指定できます。<br/> `1` - PREG_PATTERN_ORDER : varで指定された変数名を仮に`$matches`とすると、`$matches[0]` はパターン全体にマッチした文字列の配列、 `$matches[1]` は第 1 のキャプチャ用サブパターンにマッチした文字列の配列、 といった順番となります。<br/> `2` - PREG_SET_ORDER : `$matches[0]` は 1 回目のマッチングでキャプチャした値の配列、 `$matches[1]` は 2 回目のマッチングでキャプチャした値の配列、 といった順序となります。<br/> `256` - PREG_OFFSET_CAPTURE : このフラグを設定した場合、各マッチに対応する文字列のオフセットも(バイト単位で)返されます。 これは、matches の値を配列の配列に変更することに注意してください。 その配列のすべての要素は、 オフセット 0 で一致した文字列 およびその文字列のオフセット 1 での subject へのオフセットからなります。<br/> `512` - PREG_UNMATCHED_AS_NULL : このフラグが渡されると、 マッチしなかったサブパターンがあった場合 null として通知されます。 このフラグが渡されない場合、 空の string として通知されます。
offset | Integer | 検索の開始位置。デフォルトは先頭から。

**記載例**    
```smarty
{rcms_match_all
    var='matches'
    pattern='|<[^>]+>(.*)</[^>]+>|U'
    subject='<b>example: </b><div align=\"left\">this is a test</div>'
    flags=2}

{$matches|@debug_print_var}
```
**出力結果**
```
Array (2)
0 => Array (2)
    0 => "<b>example: </b>"
    1 => "example:"
1 => Array (2)
    0 => "<div align=\"left\">this is a test</div>"
    1 => "this is a test"
```

## rcms_rsort

配列を降順にソートします。

注意：配列に対する修飾子になるので、@をつける必要があります。

**属性**  
なし。

**記載例**    
```smarty
{assign var="result_arr" value=$input_arr|@rcms_rsort}
```

## rcms_sort

配列を昇順にソートします。

注意：配列に対する修飾子になるので、@をつける必要があります。

**属性**  
なし。

**記載例**    
```smarty
{assign var="result_arr" value=$input_arr|@rcms_sort}
```

## rcms_sort_by_key

連想配列を指定したキーの値でソートします。

**記載例**    
```smarty
{assign var="product_list" value=$product_list|@rcms_sort_by_key:'price':'asc'}
```

## rcms_strip_tags

文字列から HTML および PHP タグを取り除きます。

**記載例**    
```smarty
{assign var="output" value=$input|rcms_strip_tags:'<br>'}
```

## read_dir

KurocoFilesに存在するファイルの一覧を取得し、繰り返します。

**属性**  

Param | Type | Description
--- | --- | ---
name | String | read_dirブロックを識別する名前
file_var | Object | 取得した以下のファイル情報を格納するSmarty変数名<br/>・path:ファイルパス<br/>・size:ファイルサイズ (byte)<br/>・ctime:ファイル内容の変更日時 (タイムスタンプ)<br/>・mtime:ファイル属性(ファイル名など)の変更日時 (タイムスタンプ)<br/>・is_dir:ディレクトリかどうか
path | String | 取得対象ディレクトリのパス。/files/userまたは/files/ltd 配下を指定
pattern | String | ファイルパスでフィルタをかけたい場合、正規表現で指定
recursive | Boolean | true を指定すると、サブディレクトリの中身も再帰的に取得します。
name_only | Boolean | true を指定すると、file_varの変数がString形式でファイルパスのみ返すようになります。
type | String | 'file' か 'dir' を指定すると、それぞれファイルのみ、ディレクトリのみを対象として繰り返します。指定しなかった場合、両方が対象となります。

**記載例**    
```smarty
{read_dir name="hoge" file_var='file' path='/files/user'}
    {$file|@debug_print_var}
{/read_dir}
```

## read_file

ファイルを１行ずつ読み込み、繰り返します。

**属性**  

Param | Type | Description
--- | --- | ---
name | String | read_fileブロックを識別する名前
path | String | ファイルパスを相対パスで/files/から指定。<br/>参照できるディレクトリは以下になります。<ul><li>`/files/user/`</li><li>`/files/ltd/`</li><li>`/files/topics/`</li><li>`/files/member/`</li></ul>
row | String | 読み込んだ１行分の文字列を保存するSmarty変数名
type | String | ファイル形式。'txt' か 'csv' か 'jsonl'を指定してください。指定しなかった場合、デフォルトは 'txt' です。
ignore_permission | Boolean | `/files/topics/`, `/files/member/`のディレクトリを指定した場合に、true を指定するとファイルが保存されたコンテンツの公開状態や権限設定を無視します。

**記載例**    
```smarty
{read_file name="hoge" path='foo.txt' row="row"}
    {$row|escape}
{/read_file}
```

## refresh_cs

MemberCustomSearchを再設定します。

**属性**  

Param | Type | Description
--- | --- | ---
add | Array | 追加するメンバーカスタムサーチIDの配列

**記載例**    
```smarty
{refresh_cs}
```

```smarty
{assign_array var="custom_search_ids" values="1,2,3"}
{refresh_cs add=$custom_search_ids}
```

## regex_replace

変数に対して正規表現による検索・置換を行います。

**属性**  

Position | Type | Description
--- | --- | ---
1 | String | 置換するための正規表現
2 | String | この文字列に置換する

**記載例**    
```smarty
{assign var="string" value="This is KUROCO."}
{$string|regex_replace:"/kuroco/i":"Kuroco"}

{assign var="string" value="12,31,2023"}
{$string|regex_replace:'/(\d+),(\d+),(\d+)/':'$3-$1-$2'}

{assign var="string" value="本日は晴天なり"}
{$string|regex_replace:"/晴天/":"雨天"}
```

**出力結果**
```
This is Kuroco.

2023-12-31

本日は雨天なり
```

## remove_dir

ディレクトリを削除します。

**属性**  

Param | Type | Description
--- | --- | ---
path | String | 削除するディレクトリのパス
status_var | String | 削除の結果を格納するSmarty変数名

**記載例**    
```smarty
{remove_dir path='/files/user/hoge' status_var='status'}
```

## remove_file

ファイルを削除します。

**属性**  

Param | Type | Description
--- | --- | ---
path | String | 削除するファイルのパス
bucket | String | 削除するファイルが置かれているS3/GCSのバケット名
status_var | String | 削除の結果を格納するSmarty変数名

**記載例**    
```smarty
{remove_file path='/files/user/hoge.jpg' status_var='status'}
```

## rename_file

ファイルを移動します。

**属性**  

Param | Type | Description
--- | --- | ---
src_path | String | 移動元パス
dest_path | String | 移動先パス

**記載例**    
```smarty
{rename_file src_path=$src_path dest_path=$dest_path}
```

## replace

シンプルな文字列の検索・置換を行います。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| search | String/Array | 検索する文字列（必須） |
| replace | String/Array | 置換後の文字列（必須） |

**戻り値**

置換を適用した文字列。

#### 記載例

```smarty
{$text|replace:"old":"new"}
{$path|replace:"\\":"/"}
{"Hello World"|replace:"World":"Everyone"}
```

補足:

- PHP の `str_replace()` を使用しており、正規表現ではない大文字小文字を区別した置換を、出現箇所すべてに対して行います。大文字小文字を区別したくない場合は `regex_replace` を使用してください。
- `search`/`replace` に配列を渡すと、複数の置換を一度に行えます。

## return

カスタム関数を実行した結果とともに、カスタム関数を終了します。

**属性**  

Param | Type | Description
-- | -- | --
value | Mixed | コール元のカスタム関数に値を返します。

**記載例**    
カスタム関数「sub_funtion」に以下のように記述した場合、
```smarty
{return value="Hello"}
```
別のカスタム関数で以下のように「sub_function」をコールすると、
```smarty
{function name="sub_function" var="result"}
```
変数 `$result` には `"Hello"` が代入されます。

## save_file

ファイルで保存します。

**属性**  

Param | Type | Description
--- | --- | ---
value | String | 保存内容
var | String | 結果を格納する変数名

**記載例**    
```smarty
{save_file var='path' value=$value}
```

## secret

シークレットを呼び出す。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
key | String | シークレットのキー名 (必須)

**記載例**    
```smarty
{secret var='foo' key='hoge'}
```

## sendmail

メールを送信します。  
また、sendmailの引数に与えた変数はメッセージひな形のテンプレート内で利用できます。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名。成功したらtrue、失敗したら falseが格納されます。
to | String | 宛先<br/>カンマ区切りで複数指定ができます。<br/>例：`to="test1@example.com, test2@example.com`
to_member_id | Integer | 宛先にするメンバーID<br/>カンマ区切りで複数指定ができます。<br/>例：`to_member_id="1,2"`
subject | String | 件名
contents | String | 本文
from | String | FROMアドレス
from_nm | String | FROMの送信者名
cc | String | CCに指定するメールアドレス。複数指定する場合はカンマ区切りで指定します。
cc_member_id | Integer | CCに指定するメンバーID。複数指定する場合はカンマ区切りで指定します。
bcc | String | BCCに指定するメールアドレス。複数指定する場合はカンマ区切りで指定します。
bcc_member_id  | Integer | BCCに指定するメンバーID。複数指定する場合はカンマ区切りで指定します。
mail_template | String | メッセージひな形の識別子
sg_custom_args | Array | SendGridのcustom_argsに渡す連想配列です。最大5件まで指定できます。プラットフォーム予約済みキー（`site_id`, `region`, `magazine_id`, `magazine_send_mail_list_id`）は使用できません。 
任意の変数名|String|メッセージひな形のテンプレートに渡す変数を指定します。

**記載例1**  

```smarty
{sendmail
    var='result'
    to=$mail_to
    subject='testmail'
    contents="This is test."
    from="test@example.com"
    from_nm="test"}
```

**記載例2**  
以下のようにすると、メッセージひな形で$member_detailの変数が使用できます。

```smarty
{sendmail
    var=result 
    to=$mail_to
    subject='testmail' 
    mail_template='update_test' 
    member_detail=$member_detail
    from="noreply@kuroco-mail.app" 
    from_nm="test"}
```

**記載例3**   
SendGridのcustom_argsを指定する場合は、`{assign_array}`で連想配列を組み立ててから渡します。

```smarty
{assign_array var="args" keys="campaign_id,order_ref" values="summer-2026,order-12345"}
{sendmail
    var=result
    to="user@example.com"
    subject="Hello"
    contents="Body text"
    sg_custom_args=$args}
```

:::note
`sg_custom_args`で指定した値はSendGridのcustom_argsとして送信されます。トラッキングやメタデータの付与に利用できます。
:::

## set_memory

メモリ割り当てを増やします。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 指定するメモリ容量。`256M`,`512M`,`768M` のいずれかでなければなりません。

**記載例**    
```smarty
{set_memory memory_limit='256M'}
```

## site_sync

サイト間の同期をします。このプラグインで実行する場合は前回実施から6時間の間隔が必要です。

**属性**  

Param | Type | Description
--- | --- | ---
from_site_key | String | 同期元のサイトキー
to_site_key | String | 同期先のサイトキー<br/>指定が無い場合は自身のサイトに同期します。
sync_type | Integer | 1:アプリ同期 2:全同期 4:アプリ同期(タグを除く)

**記載例**    
```smarty
{site_sync from_site_key='from_example_key' to_site_key='to_example_key'  sync_type='1'}
```

## slack_get_message

Slackのメッセージを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名
channel | String | チャンネルID
ts | String | メッセージのタイムスタンプ値

**記載例**    
```smarty
{slack_get_message
    var='message'
    channel='XXXXXXXXX'
    ts='1675411163.005300'}
```

## slack_post_message

Slackにメッセージ送信します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名。成功したらtrue、失敗したら falseが格納されます。
channel | String | チャンネルID
users | Array | ユーザーIDの配列
text | String | メッセージ本文
thread_ts | String | スレッドの親メッセージのタイムスタンプ値

**記載例**    
```smarty
{slack_post_message
    channel='XXXXXXXXX'
    users=$users
    text='test'}
```

## slack_team_info

Slackのチーム情報を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | Array | 結果を格納する変数名。失敗したら falseが格納されます。
team | String | 検索条件

**記載例**    
```smarty
{slack_team_info var='team' team=$team}
```

## sleep

実行を遅延させます。
最短 100ms から最長 1000msまで遅延可能です。

**属性**  

Param | Type | Description
--- | --- | --
ms | Integer | ミリ秒単位の停止時間。100以上、1000以下の値でなければなりません<br/>範囲外の数値を指定した場合は、100ms または1000msとなります。

**記載例**    

```smarty
{sleep ms=300}
```

## sort_name

言語設定が 英語（'en'）の場合に姓と名を入れ替えて表示します。

**記載例**    

```smarty
{'Yamada'|sort_name:'Taro'}
// 言語設定が enの場合は Taro Yamada と表示される。
// 言語設定が en以外の場合は Yamada Taro と表示される。
```

## spacify

各文字の間にセパレータ（デフォルトはスペース）を挿入します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| spacify_char | String | 文字間に挿入する文字列（任意、デフォルト `' '`） |

**戻り値**

文字間にセパレータを挿入した文字列。

#### 記載例

```smarty
{"Hello"|spacify}      {* H e l l o *}
{$text|spacify:"-"}    {* H-e-l-l-o *}
{"Test"|spacify:"_"}   {* T_e_s_t *}
{"ABC"|spacify:" - "}  {* A - B - C *}
```

補足:

- セパレータには 1 文字だけでなく複数文字の文字列を指定できます。
- マルチバイト非対応 — バイト単位で分割するため、マルチバイト文字を途中で分断する可能性があります。

## split

区切り文字を使って文字列を配列に分割します。正規表現とリテラル区切り文字の両方をサポートします。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| string | String/Number | 分割する文字列（必須） |

**戻り値**

文字列の配列を返します。文字列が空 `""` または有効な型でない場合は空配列 `[]` を返します。

#### 記載例

```smarty
{* リテラル区切り文字での基本的な分割 *}
{','|split:$csv_string}

{* 正規表現パターンで分割（/で始まる必要あり） *}
{'/\s+/'|split:$text}  {* 空白で分割 *}

{* 数値の分割（自動的に文字列に変換） *}
{'-'|split:12345}
```

区切り文字を修飾子入力、文字列をコロンの後に指定します。区切り文字が `/` で始まり 3 文字以上ある場合は正規表現として `preg_split()` で処理し、それ以外は `explode2()` で分割します。

## storage_url

S3/GSC上のファイルを読み込む署名付きURLを取得します。

**属性**  

Param | Type | Description
--- | --- | --
var | String | 結果を格納する変数名
path | String | S3/GCS上のパス
expire | String | URLの有効期限。デフォルトは `'+167 hour'`

**記載例**    
```smarty
{storage_url path=$path var='url' expire="+1 hour" }
```

## string_format

`sprintf()` を使って文字列を整形します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| format | String | `sprintf` のフォーマット文字列（必須） |

**戻り値**

整形済みの文字列。

#### 記載例

```smarty
{$number|string_format:"%02d"}        {* 05 *}
{$price|string_format:"$%.2f"}        {* $19.99 *}
{$name|string_format:"Hello, %s!"}    {* Hello, John! *}
{$hex|string_format:"%08X"}           {* 0000FF00 *}
```

`%s`・`%d`・`%f`・`%e`・`%x`/`%X`・`%o`・`%b`・`%%` などの一般的な `sprintf` フォーマット指定子に対応しており、`%08d`・`%.2f`・`%-10s` のような幅・精度・パディング指定も使用できます。

## strip

囲まれた領域の改行削除と各行にtrimを掛けます。

**属性**  
なし。

**記載例**    
```smarty
{* 次の例は全て１行に出力されます  *}
{strip}
    {foreach from=$contents item=content name='loop1'}
        {if $content.topics_group_id == 1}
            {$content.subject}
        {/if}
        {if !$smarty.foreach.loop1.last}
            ,
        {/if}
    {/foreach}
{/strip}
```

## strip_tags

テキストから HTML タグを取り除きます。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| replace_with_space | Boolean | タグを除去する代わりに空白に置換するかどうか（任意、デフォルト `true`） |

**戻り値**

HTML タグを取り除いた文字列。

#### 記載例

```smarty
{$html|strip_tags}
{$html|strip_tags:false}
{"<p>Hello</p>"|strip_tags}           {* " Hello " with spaces *}
{"<p>Hello</p>"|strip_tags:false}     {* "Hello" no spaces *}
{"<b>A</b><i>B</i>"|strip_tags}       {* "A B" *}
{"<b>A</b><i>B</i>"|strip_tags:false} {* "AB" *}
```

補足:

- `replace_with_space=true`（デフォルト）の場合はすべてのタグを 1 つの空白に置換するため、隣接する語が連結されません（例: `<b>Hello</b><i>World</i>` は `HelloWorld` ではなく `Hello World` になります）。
- `replace_with_space=false` の場合は PHP の `strip_tags()` を使用し、タグを完全に削除します。いずれの場合もタグ間のコンテンツは保持されます。

## strtodate

日付を取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
timestamp | Int\|String | タイムスタンプ
format | String | フォーマット

**記載例**    
```smarty
{strtodate var='today' timestamp='today' format='Ymd'}
```

## strtolower

型チェック付きで文字列を小文字に変換します。

**戻り値**

小文字化された文字列。入力がスカラーでない場合は空文字列を返します。

#### 記載例

```smarty
{"HELLO WORLD"|strtolower}   {* hello world *}
{$name|strtolower}
{$array|strtolower}          {* returns empty string *}
```

補足:

- 配列・オブジェクト・`null` などの非スカラー値は空文字列になります。処理前に明示的に文字列へキャストされます。
- マルチバイト非対応 — UTF-8 を扱う場合は PHP の `mb_strtolower()` を利用してください。`lower` とほぼ同等ですが、非スカラー値を明示的にハンドリングする点が異なります。

## strtoupper

型チェック付きで文字列を大文字に変換します。

**戻り値**

大文字化された文字列。入力がスカラーでない場合は空文字列を返します。

#### 記載例

```smarty
{"hello world"|strtoupper}   {* HELLO WORLD *}
{$name|strtoupper}
{$array|strtoupper}          {* returns empty string *}
```

補足:

- 配列・オブジェクト・`null` などの非スカラー値は空文字列になります。処理前に明示的に文字列へキャストされます。
- マルチバイト非対応 — UTF-8 を扱う場合は PHP の `mb_strtoupper()` を利用してください。`upper` とほぼ同等ですが、非スカラー値を明示的にハンドリングする点が異なります。

## substr

型チェック付きで入力文字列から部分文字列を返します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| start | Integer | 開始位置（0 始まり、負の値も可）（必須） |
| length | Integer | 取り出す長さ（負の値も可、任意、デフォルト `null`） |

**戻り値**

部分文字列。入力がスカラーでない場合は空文字列を返します。

#### 記載例

```smarty
{"Hello World"|substr:0:5}  {* Hello *}
{$text|substr:6}            {* from position 6 to end *}
{$string|substr:-5:5}       {* last 5 characters *}
{$text|substr:0:-3}         {* all except last 3 characters *}
{$array|substr:0:5}         {* returns empty string *}
```

補足:

- 負の `start` は末尾からの位置を表し、負の `length` は末尾からその文字数を取り除きます。
- マルチバイト非対応 — バイト単位でカウントします。

## subtract

変数に数値を引き算します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
value | Int | 数値

**記載例**    
```smarty
{subtract var='i' value=5}
```

## sync_counter

コンテンツのカウンター拡張項目の値を同期します。

カウンター項目は、頻繁に更新される値をコンテンツ自体から分離して、更新を非同期的に行うことで高速化をしています。  
このプラグインを使用することで、非同期に更新されたカウンターの値をコンテンツの値に同期します。

**属性**  

Param | Type | Description
--- | --- | ---
ids | Array/String | 対象のコンテンツのID配列 (必須)。カンマ区切りの文字列でも指定可能です。

**記載例**    

```smarty
{sync_counter ids=1078}
```

```smarty
{sync_counter ids="1,2,3"}
```

## to_form_options
連想配列を、`[['key'=>$key, 'value'=>$value], ...]` のような形式に変換します。

**属性**  

Position | Type | Description
--- | --- | --
target | Array | 変換する配列 (必須)

**記載例**    
```smarty
{assign var='form_options' value=$options_array|@to_form_options}
```

```smarty
{assign var='form_options' value=$options_array|@to_form_options:'key':'label'}
```

## to_object

配列を、stdClassオブジェクトに変換します。

**属性**  

Position | Type | Description
--- | --- | --
target | Array | 変換する配列 (必須)

**記載例**    
```smarty
{assign var='foo' value=$bar|@to_object}
```

## truncate

指定した長さで文字列を切り詰めます（バイト単位）。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| length | Integer | 最大長（任意、デフォルト `80`） |
| etc | String | 切り詰めたときに末尾に付ける文字列（任意、デフォルト `'...'`） |
| break_words | Boolean | 単語の途中で切るかどうか（任意、デフォルト `false`） |
| middle | Boolean | 真ん中で切り詰めるかどうか（任意、デフォルト `false`） |

**戻り値**

切り詰められた文字列。

#### 記載例

```smarty
{$text|truncate:50}
{$long_string|truncate:30:"...":true}
{$text|truncate:100:"[more]":false:true}
```

補足:

- バイト単位の `strlen`/`substr` を使用するためマルチバイト非対応です。UTF-8 などマルチバイトエンコーディングを扱う場合は `mb_truncate` を使用してください。
- `break_words=false`（デフォルト）の場合は単語境界で切り詰めます。`middle=true` の場合は先頭と末尾の半分を残し、その間を `etc` で繋ぎます。

## twitter_post_message

X（旧Twitter）にメッセージを送信します。

**属性**  

Position | Type | Description
--- | --- | --
var | String | 結果を格納する変数名
text | String | メッセージ

**関連ドキュメント**  
このプラグインを使用するには、[チャネル] - [メッセージング] - [X]の各種項目を設定する必要があります。  
X（旧Twitter）との連携設定の具体的な手順については、[X（旧Twitter）と連携し、コンテンツ投稿時にXへ自動投稿する](/ja/docs/tutorials/setting-up-twitter-integration/) をご確認ください。

## unzip

Zipファイルを展開します。

**前提条件**  
unzipを利用するためには、Firebaseと連携が必要になります。
[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)を参考に連携してください。

:::info
保存先（`dest`）はGCSパス（`/files/g/`）である必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は保存先としてサポートされていません。
入力元（`src`）は`https://`から始まるURLか、GCSパス（`/files/g/`）である必要があります。KurocoFilesのパスは直接サポートされていませんが、KurocoFiles（公開）のファイルについては公開URLを使用することで指定可能です。
:::

**属性**

Position | Type | Description
--- | --- | --
src | String | 展開するzipファイルパス。`https://` から始まるURLか、GCSパス（`/files/g/`）である必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は直接サポートされていませんが、KurocoFiles（公開）のファイルについては公開URL（例: `https://[site].g.kuroco-img.app/files/user/...`）を使用することで指定可能です。
dest | String | 展開したファイルを格納するフォルダのパス。GCSパス（`/files/g/`）である必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は保存先としてサポートされていません。
bucket | String | バケット名。省略した場合は [外部システム連携] - [Firebase] で設定したStorageが利用されます。
callback_batch | String | Zip展開処理完了後にコールバックするバッチ処理名
data | Mixed | 任意のデータ。コールバックバッチに引き渡されます。
overwrite | Integer | 展開先フォルダに同名のファイルが存在した場合に上書きするかどうか。0または1。
detect_order| Array | 展開したファイルのファイル名の文字コードを判別する際の優先順位を指定します。デフォルトでは `["utf8", "cp932", "EUC-JP"]` となります。

**記載例**    
```smarty
{unzip
    src='/files/g/private/temp/zip/hoge.zip'
    dest='/files/g/private/temp/unzip/'
    overwrite=1
    callback_batch='batch1'
}
```

## update_counter

コンテンツのカウンター型の拡張項目の値を更新します。

**属性**  

Param | Type | Description
--- | --- | --
var| String | 結果をassignする変数名
value | Integer | セットする数値 (必須)
topics_group_id | Integer | コンテンツ定義ID (必須)
slug | String |  対象のコンテンツのID/Slug (必須)
ext_slug | String | 対象の項目のID/Slug (必須)
index | Integer | 0から始まる繰り返しの順番

**記載例**    
```smarty
{update_counter
    var='result'
    value=3
    topics_group_id=10
    slug='a-content'
    ext_slug='a_col_slug'
    index=0
}
```

## upper

文字列を大文字に変換します。

#### 記載例

```smarty
{"hello"|upper}        {* HELLO *}
{$name|upper}
{"abc123"|upper}       {* ABC123 *}
```

補足:

- PHP の `strtoupper()` をそのまま使用するためマルチバイト非対応です。UTF-8 を扱う場合は型ガード付きの `strtoupper` モディファイアか、PHP の `mb_strtoupper()` を利用してください。

## usage_price_format

`RCMS_Usage` のフォーマットシステムを使って使用量・価格を表示用に整形します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| edge_flg | Boolean | エッジフォーマットフラグ（小数点の扱いに影響）（任意、デフォルト `false`） |

**戻り値**

整形された価格文字列。入力が空文字列の場合は空文字列 `""` を返します。

#### 記載例

```smarty
{* 基本的な価格フォーマット *}
{$price|usage_price_format}

{* エッジフラグ有効 *}
{$price|usage_price_format:true}

{* 使用量コストの表示 *}
{$monthly_cost|usage_price_format}
```

実際のフォーマットは `RCMS_Usage::format_price()` に委譲されます。通貨記号、桁区切り、小数点桁数は `RCMS_Usage` の設定に依存します。

## uuid

uuidを取得します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 格納する変数名

**記載例**    
```smarty
{uuid var='foo'}
```

## wordwrap

テキストを指定した行幅で折り返します。

**属性**

| パラメータ | 型 | 説明 |
| :--- | :--- | :--- |
| length | Integer | 1 行の文字数（任意、デフォルト `80`） |
| break | String | 改行として挿入する文字列（任意、デフォルト `"\n"`） |
| cut | Boolean | 長い単語を強制的に折り返すかどうか（任意、デフォルト `false`） |

**戻り値**

改行が挿入された折り返し済みの文字列。

#### 記載例

```smarty
{$text|wordwrap:40}
{$long_text|wordwrap:60:"<br>"}
{$url|wordwrap:50:"\n":true}
{$code|wordwrap:120:"<br />":true}
```

補足:

- `cut=false`（デフォルト）では長い単語を分断せず、行幅を超える場合があります。`cut=true` では行幅ちょうどで強制的に折り返し、単語の途中でも改行します。
- 改行文字列は任意で、HTML の `<br>` などにも利用できます。入力にもとから含まれている改行は保持されます。

## write_file

ファイルにデータ書き込みます。

**属性**  

Position | Type | Description
--- | --- | --
path | String | ファイルパス。省略した場合は自動的にユニークなファイル名で一時領域にファイルを書き込みます。
var | String | 書き込んだ一時ファイルパスを格納する変数名（必須）
value | String \| Array | 書き込む内容。配列を指定した場合、CSV形式で書き込みます
is_append | Integer | 追記モード。0または1。追記モードの場合は、`path` を指定する必要があります。

**記載例**    
```smarty
{write_file var="path" value="hoge"}
{write_file path=$path value="foo" is_append=1}
{write_file path=$path value="var" is_append=1}
```

## xmltojson

XMLからJSONに変換します。

**属性**  

Param | Type | Description
--- | --- | ---
var | String | 結果を格納する変数名 (必須)
xml | String | XML
convert_namespace | Integer | 1を指定すると名前空間(namespace)を含む要素もJSONにエクスポートします。

**記載例**    
```smarty
{xmltojson var='json' xml='input'}
```

## zip

クラウドファイルをZip圧縮します。

**前提条件**  
zipを利用するためには、Firebaseと連携が必要になります。
[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)を参考に連携してください。

:::info
保存先（`dest`）はGCSパス（`/files/g/`）である必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は保存先としてサポートされていません。
各エントリの`url`はGCSパス（`/files/g/`）か`https://`から始まるURLである必要があります。KurocoFilesのパスは直接サポートされていませんが、KurocoFiles（公開）のファイルについては公開URLを使用することで指定可能です。
:::

**属性**

Position | Type | Description
--- | --- | --
entries | Array | 圧縮するファイルリスト。各エントリは`url`（ファイルのURLまたはGCSパス）と`name`（zip内のファイル名）を含む配列です。`url`はGCSパス（`/files/g/`）か`https://`から始まるURLである必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は直接サポートされていませんが、KurocoFiles（公開）のファイルについては公開URL（例: `https://[site].g.kuroco-img.app/files/user/...`）を使用することで指定可能です。
dest | String | zipファイルパス。GCSパス（`/files/g/`）である必要があります。KurocoFilesのパス（`/files/user/`、`/files/temp/`、`/files/ltd/`）は保存先としてサポートされていません。
bucket | String | バケット名。省略した場合は [外部システム連携] - [Firebase] で設定したStorageが利用されます。
callback_batch | String | Zip圧縮処理完了後にコールバックするバッチ処理名
data | Mixed | 任意のデータ。コールバックバッチに引き渡されます。

**記載例**    
```smarty
{assign_array var='entries' values=''}

{assign_array var='entry1' values=''}
{append var='entry1' index='name' value='name1'}
{append var='entry1' index='url' value='https://xxxx/xxxx.jpg'}
{append var='entries' value=$entry1}

{assign_array var='entry2' values=''}
{append var='entry2' index='name' value='name2'}
{append var='entry2' index='url' value='https://xxxx/yyyy.jpg'}
{append var='entries' value=$entry2}

{zip entries=$entries dest='/files/g/public/a.zip' bucket=$bucket}
```


---

# トリガーメールアドレス

> 元ページ: `reference/trigger-email-address` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/trigger-email-address/

Kurocoのメール送信機能では、送信先に「トリガーメールアドレス」を指定できます。  
トリガーメールアドレスは `(ローカル部)@(サービス名).r-cms.jp` 形式の特別なアドレスです。この宛先へのメールは実際のメールとしては送信されず、代わりにメール本文の外部サービスへの送信や、バッチ処理・AIエージェントの起動が行われます。

## 基本情報

| 項目 | 内容 |
| :--- | :--- |
| 種別 | メール送信先の指定形式 |
| 対象 | 通知メールやメルマガなどのメール送信機能 |
| 利用場面 | メール送信を契機に、外部サービスへのメッセージ送信やバッチ処理・AIエージェントの起動を行う場合 |

トリガーメールアドレスは、メールの送信先を指定できる箇所で利用できます。例として以下があります。

- フォームの[配送先メールアドレス]
- カスタム処理のメール送信（`sendmail`）

## トリガーメールアドレス一覧

| 送信先 | アドレス形式 | ローカル部（@より前）に指定する値 |
| :--- | :--- | :--- |
| Slack | `{channel}@slack.r-cms.jp` | 送信先チャンネル（チャンネルID または #チャンネル名） |
| LINE | `{LINE ID}@text.line.r-cms.jp` | 送信先のLINEユーザーID |
| テキスト メッセージ(SMS) | `{tel}@twilio.r-cms.jp` | 送信先の電話番号 |
| X（旧Twitter） | `{twitter_id}@tweets.twitter.r-cms.jp` | 使用されません |
| バッチ処理 | `{batch_id}@batch.r-cms.jp` | バッチID |
| AIエージェント | `{ai_agent_id}@agent.r-cms.jp` | エージェントID または Slug |

## Slack

メール本文をSlackの指定チャンネルに送信します。ローカル部には送信先チャンネル（チャンネルID または #チャンネル名）を指定します。

```text
{channel}@slack.r-cms.jp
```

Slack連携を有効にし、Bot User OAuth Tokenを設定しておく必要があります。  
トリガーメールアドレスは[チャネル] -> [メッセージング] -> [Slack]の画面に表示されます。

![Image from Gyazo](https://i.gyazo.com/734cfc5eda8daff4987e2717296861d9.png)

:::info
Slack連携の設定方法は[Slack](/ja/docs/management/slack/)を参照してください。  
Bot User OAuth Tokenの取得手順は[SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)を参照してください。
:::

## LINE

メール本文をLINEのユーザーに送信します。ローカル部には送信先のLINEユーザーIDを指定します。

```text
{LINE ID}@text.line.r-cms.jp
```

トリガーメールアドレスは[チャネル] -> [メッセージング] -> [LINE]の画面に表示されます。

![Image from Gyazo](https://i.gyazo.com/a9e9763acb157deb8a6846981779c82b.png)

:::info
LINE連携の設定方法と利用例は[LINE](/ja/docs/management/line/)および[LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)を参照してください。
:::

## テキスト メッセージ(SMS)

メール本文をSMSとして送信します。ローカル部には送信先の電話番号を指定します。

```text
{tel}@twilio.r-cms.jp
```

トリガーメールアドレスは[チャネル] -> [メッセージング] -> [テキスト メッセージ(SMS)]の画面に表示されます。

![Image from Gyazo](https://i.gyazo.com/61f8b0bccef0c5684ae05efdc3678358.png)

カスタム処理では、以下のように記述するとSMSが送信されます。

```smarty
{sendmail var=result to="(電話番号)@twilio.r-cms.jp" subject="Test" contents="This is Test"}
```

:::info
テキスト メッセージ(SMS)連携の設定方法と利用例は[テキスト メッセージ(SMS)](/ja/docs/management/twilio/)および[Twilioと連携してSMSを送信する](/ja/docs/tutorials/how-to-connect-to-twillio/)を参照してください。
:::

## X（旧Twitter）

メール本文をXへのポストとして投稿します。投稿先は設定したアクセストークンに紐づくアカウントになります（ローカル部は現在使用されません）。

```text
{twitter_id}@tweets.twitter.r-cms.jp
```

トリガーメールアドレスは[チャネル] -> [メッセージング] -> [X]の画面に表示されます。

![Image from Gyazo](https://i.gyazo.com/78a95ab2b595ca29af432e469c56846f.png)

:::info
X連携の設定方法と利用例は[Twitter](/ja/docs/management/twitter/)および[X（旧Twitter）と連携し、コンテンツ投稿時にXへ自動投稿する](/ja/docs/tutorials/setting-up-twitter-integration/)を参照してください。
:::

## バッチ処理

ローカル部に指定したバッチIDのバッチ処理を起動します。

```text
{batch_id}@batch.r-cms.jp
```

トリガーメールアドレスは、[オペレーション] -> [バッチテンプレート]から対象バッチの編集画面を開くと表示されます（バッチ登録後に表示されます）。

![Image from Gyazo](https://i.gyazo.com/ce95c5c672833a8f29c0dd877b6c122a.png)

:::info
バッチテンプレートの設定方法は[バッチテンプレート](/ja/docs/management/batch-template/)を参照してください。
:::

## AIエージェント

自律実行を有効にしたAIエージェントを起動します。受信したメールの件名・本文がエージェントへの指示として渡され、エージェントが内容に応じた対応を実行します。

```text
{ai_agent_id}@agent.r-cms.jp
```

ローカル部には、エージェントIDまたはエージェントに設定したSlugを指定します。

**Slugの仕様**

- トリガーメールアドレスのローカル部（@より前）に使用する識別子です。
- 半角英数字・ハイフン・アンダースコアが使用できます（数字のみは不可）。
- 大文字・小文字は区別されません。
- 未設定の場合はエージェントIDが使用されます。
- Slugを設定した場合も、エージェントID宛のアドレスは引き続き利用できます。

**前提条件**

- エージェントのステータスが有効になっていること
- エージェント編集画面の[自律実行]が有効になっていること

自律実行を有効にすると、人手の確認なしにエージェントを起動できます。実行時のツール操作はエージェントの権限ポリシー（Admin MCPの読み取り専用設定など）に従います。  
トリガーメールアドレスは、エージェント編集画面の[自律実行]欄およびエージェント一覧画面に表示されます。

![Image from Gyazo](https://i.gyazo.com/7791ab15d546ca81dd252b6048a2b81b.png)

:::caution
- 該当するエージェントが存在しない場合や、自律実行が無効な場合は、エージェントは起動されません。この場合もメールとしての送信は行われません。
- エージェントの実行に起因して送信されたメールは、ループ防止のため再度エージェントを起動しません。エージェントが行った操作をきっかけに別機能から送信される通知メール（例：エージェントが行った承認により送信されるワークフロー通知）は、新しいトリガーとして扱われます。
:::

## 注意事項

:::caution
- トリガーメールアドレス宛のメールは、実際のメールとしては送信されません。
- 各サービスへの送信・処理の起動には、対象サービスの連携設定が有効になっている必要があります。
:::

## 関連ドキュメント

- [Slack](/ja/docs/management/slack/)
- [LINE](/ja/docs/management/line/)
- [テキスト メッセージ(SMS)](/ja/docs/management/twilio/)
- [Twitter](/ja/docs/management/twitter/)
- [バッチテンプレート](/ja/docs/management/batch-template/)
- [LINEユーザーにメッセージを送付する](/ja/docs/tutorials/how-to-connect-to-line/)
- [Twilioと連携してSMSを送信する](/ja/docs/tutorials/how-to-connect-to-twillio/)
- [X（旧Twitter）と連携し、コンテンツ投稿時にXへ自動投稿する](/ja/docs/tutorials/setting-up-twitter-integration/)
