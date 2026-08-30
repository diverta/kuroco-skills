# API・データ取得プラグイン

## 目次

- [api_internal](#api_internal) - 内部API（同じKurocoサイト内）をリクエストします。
- [api](#api) - 外部APIをリクエストして、応答をassignします。
- [api_method](#api_method) - エンドポイントを作成せずにAPIメソッドを直接実行します。
- [api_mng](#api_mng) - 管理APIを内部的にリクエストします。
- [api_token](#api_token) - APIトークン（静的または動的）を取得します。
- [assign_topics_category_list](#assign_topics_category_list) - Retrieve categories for a topi...
- [assign_tag_list](#assign_tag_list) - Retrieve tags belonging to a s...
- [assign_tag_category_list](#assign_tag_category_list) - Retrieve the list of tag categ...
- [assign_new_comment_list](#assign_new_comment_list) - Retrieve the most recent comme...
- [assign_favorite_cnt](#assign_favorite_cnt) - Get the total number of favori...
- [assign_my_favorite_cnt](#assign_my_favorite_cnt) - Get the current user's favorit...
- [assign_relation_tag_list](#assign_relation_tag_list) - Retrieve tags associated with ...
- [assign_group_nm](#assign_group_nm) - Retrieve the display name of a...
- [assign_api_credential](#assign_api_credential) - API認証情報（署名、セッションID、JWT等）を生成します...

---

## api_internal

内部API（同じKurocoサイト内）をリクエストします。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | レスポンスを格納する変数名 |

### Return Value

指定した変数にAPIレスポンス（配列）が代入されます。status_varには成功時は1、失敗時は0が代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{api_internal endpoint='/rcms-api/1/sample' method='GET' query='ex=1&ex2=2' cache_time=20 var='response' status_var='status'}
{* 特定のメンバーとして実行 *}
{api_internal endpoint='/rcms-api/1/member/profile' method='GET' member_id=123 var='profile' status_var='status'}
{* 現在のセッションを使用 *}
{api_internal endpoint='/rcms-api/1/mypage' method='GET' use_current_session=true var='data' status_var='status'}
{* ダイレクトモード（GETのみ） *}
{api_internal endpoint='/rcms-api/1/public/list' method='GET' direct=true var='list' status_var='status'}
```

### Notes

- 同じKurocoサイト内のAPIを呼び出す際に使用します
- エンドポイントは `/rcms-api/<api_id>/...` の形式である必要があります
- 同じエンドポイントへの再帰呼び出しは自動的に防止されます
- `direct` オプションを使用するとネットワークを介さず直接実行できます（GETのみ、member_id指定不可）
- `member_id` で特定のメンバーとして実行する場合、APIは動的トークン認証（Dynamic Token）である必要があります
- キャッシュはGETリクエストかつmember_idなしの場合のみ有効です
- バリデーションモード（`_rcms_validate`）の場合、実際のAPIリクエストは実行されません

---

## api

外部APIをリクエストして、応答をassignします。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | レスポンスを格納する変数名 |

### Return Value

`var`に生のレスポンス、`json_var`にJSONデコード結果、`status_var`に成否が代入されます。

### Usage Example

```smarty
{* 基本的なGETリクエスト *}
{api endpoint='https://api.example.com/data' method='GET' var='response' status_var='status'}
{* クエリパラメータ付きリクエスト *}
{api endpoint='https://api.example.com/search' query='q=test&limit=10' cache_time=20 var='response'}
{* POSTリクエスト（JSON Body） *}
{api endpoint='https://api.example.com/create' method='POST' json_body=$data var='response' json_var='json_result'}
{* SSL証明書を使用したリクエスト *}
{api endpoint='https://secure.example.com/api' sslcert='client_cert' sslkey='client_key' var='response'}
```

### Notes

- `sslcert`と`sslkey`を使用する場合は両方必須です
- `cache_time`はGET/HEADメソッドのみ有効です
- `dl_flg=1`の場合、レスポンスはS3にアップロードされURLが返されます

---

## api_method

エンドポイントを作成せずにAPIメソッドを直接実行します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にAPIメソッドの実行結果が代入されます。モデルやメソッドが見つからない場合は `errors` キーにエラーメッセージが含まれます。

### Usage Example

```smarty
{* トピックス一覧を取得 *}
{api_method var="output" model="Topics" method="list" request_params=$req_params}
{* トピックス詳細を取得 *}
{api_method var="detail" model="Topics" method="details" method_params=['topics_id' => 123]}
{* メンバー情報を取得 *}
{api_method var="member" model="Member" method="details" method_params=['member_id' => 456]}
{* バージョンを指定 *}
{api_method var="output" model="Topics" method="list" version=2 request_params=$params}
{* 言語を指定してリクエスト *}
{assign_array var="req" keys="lang" values="en"}
{api_method var="output" model="Topics" method="list" request_params=$req}
```

### Notes

- `model` と `method` パラメータは必須です
- APIエンドポイントを作成せずに直接メソッドを呼び出せます
- `request_params` に `lang` パラメータを含めることで言語を指定できます
- 同一スレッド内で実行されるため、HTTPリクエストのオーバーヘッドがありません
- バリデーションモード（`_rcms_validate`）の場合、空配列が返されます

---

## api_mng

管理APIを内部的にリクエストします。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | レスポンスを格納する変数名 |

### Return Value

指定した変数に管理APIのレスポンスが代入されます。status_varには成功時は1、失敗時は0が代入されます。

### Usage Example

```smarty
{* GETリクエスト *}
{api_mng endpoint='/management/topics/topics_list/' method='GET' query='topics_group_id=1' var='response' status_var='status'}
{* POSTリクエスト *}
{api_mng endpoint='/management/member/member_edit/' method='POST' queries=$post_data var='response' status_var='status'}
{* ファイルアップロード *}
{api_mng endpoint='/management/topics/topics_edit/' method='POST' queries=$data files=$upload_files var='response' status_var='status'}
{* メンバーダウンロード（特殊処理） *}
{api_mng endpoint='/management/member/member_download_all/' method='GET' var='csv_data' status_var='status'}
```

### Notes

- 管理画面用のAPIを内部から呼び出す際に使用します
- エンドポイントは `/management/<module>/<action>/` の形式（5つのパス要素）である必要があります
- `member_id` で特定のメンバーとして実行できます
- リクエストには自動的に `Accept: application/json` ヘッダーが追加されます
- 認証情報（API credentials）は自動的に追加されます
- タイムアウトは20秒に設定されています
- バリデーションモード（`_rcms_validate`）の場合、実際のリクエストは実行されません

---

## api_token

APIトークン（静的または動的）を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | トークンを代入する変数名 |

### Return Value

`var` パラメータで指定した変数にAPIトークン文字列が代入されます。パラメータが不正な場合は `null` が代入されます。

### Usage Example

```smarty
{* 静的トークンを取得 *}
{api_token var="static_token" type="static" api_id=1}
{* 動的トークンを取得（有効期限1時間） *}
{api_token var="dynamic_token" type="dynamic" api_id=1 expires=3600}
{* メモ付きの静的トークンを取得 *}
{api_token var="token" type="static" api_id=2 memo="Batch process token"}
{* トークンと有効期限を同時に取得 *}
{api_token var="token" type="dynamic" api_id=1 expires=3600 expires_var="token_expires"}
Token: {$token}
Expires at: {$token_expires|date_format:"%Y-%m-%d %H:%M:%S"}
```

### Notes

- `var`, `type`, `api_id` パラメータは必須です
- `type` は `static` または `dynamic` のみ有効です
- 不正なパラメータの場合、Smartyエラーがトリガーされます
- `static` トークンは永続的に有効です
- `dynamic` トークンは `expires` で指定した秒数後に無効になります
- バリデーションモード（`_rcms_validate`）の場合、`null` が代入されます
- `expires_var` は Unix タイムスタンプ（整数）を受け取ります。トークン生成に失敗した場合、`_rcms_validate` の場合は `null` です

---

## assign_topics_category_list

Retrieve categories for a topics group with multi-language support.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the result array |

### Return Value

Array of category objects assigned to the specified variable.

### Usage Example

```smarty
{assign_topics_category_list topics_group_id=1 var='categories'}
<nav class="category-nav">
  {foreach $categories as $cat}
    <a href="/topics/category/{$cat.topics_category_id}/">{$cat.topics_category_nm}</a>
  {/foreach}
</nav>
{assign_topics_category_list topics_group_id=1 lang='en' var='en_categories'}
```

### Notes

- Returns false if database connection is unavailable
- Only returns published categories (open_flg = 1)
- Supports multi-language when USE_MULTILANG is enabled

---

## assign_tag_list

Retrieve tags belonging to a specific tag category.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the result array |

### Return Value

Array of tag objects assigned to the specified variable.

### Usage Example

```smarty
{assign_tag_list category_id=2 var='genre_tags'}
<div class="tag-cloud">
  {foreach $genre_tags as $tag}
    <a href="/tag/{$tag.tag_id}/" class="tag">
      {$tag.tag_nm}
      <span class="count">({$tag.open_contents_cnt})</span>
    </a>
  {/foreach}
</div>
{assign_tag_list category_id=2 order='open_contents_cnt:desc' var='popular_tags'}
```

### Notes

- Only returns published tags (open_flg = 1)
- The open_contents_cnt is useful for tag cloud weighting
- Uses Tag::getTagList() internally

---

## assign_tag_category_list

Retrieve the list of tag categories for organizing and filtering tags.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the result array |

### Return Value

Array of tag category objects assigned to the specified variable.

### Usage Example

```smarty
{assign_tag_category_list var='categories'}
<select name="tag_category">
  <option value="">All Categories</option>
  {foreach $categories as $cat}
    <option value="{$cat.tag_category_id}">{$cat.tag_category_nm}</option>
  {/foreach}
</select>
{assign_tag_category_list tree_flg=true var='category_tree'}
```

### Notes

- Returns false if database connection is unavailable
- Only returns published categories (open_flg = 1)
- Categories are sorted by list_order field

---

## assign_new_comment_list

Retrieve the most recent comments for a specific content item.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | 'new_comment_list' | Variable name to store results |

### Return Value

Array of comment objects assigned to the specified variable.

### Usage Example

```smarty
{assign_new_comment_list module_id=$topics.topics_id module_type='topics' cnt=5 var='comments'}
{foreach $comments as $comment}
  <div class="comment">
    <strong>{$comment.name1}</strong>
    <p>{$comment.comment|escape|nl2br}</p>
    <time>{$comment.insert_date|pg_dateformat:'Y/m/d H:i'}</time>
  </div>
{/foreach}
```

### Notes

- Returns false if database connection is unavailable
- Different from assign_comment_list which supports pagination
- Uses Comment::getCommentNewList() internally

---

## assign_favorite_cnt

Get the total number of favorites (likes) for a specific content item across all users.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the count |

### Return Value

Integer count of total favorites assigned to the specified variable.

### Usage Example

```smarty
{* Get favorite count for a topic *}
{assign_favorite_cnt module_type='topics' module_id=$topics.topics_id var='favorite_cnt'}
<span class="likes">{$favorite_cnt} likes</span>
{* Display count directly *}
{assign_favorite_cnt module_type='topics' module_id=123 var='cnt' print_flg=1}
{* Count for a specific action type *}
{assign_favorite_cnt module_type='topics' module_id=$id action_type=1 var='bookmark_cnt'}
```

### Notes

- Returns false if database connection is unavailable
- Returns early if system error (PAGE_NOTICE_KEY == "SYS_ERR")
- Counts ALL users' favorites for the item (site-wide total)
- For current user's favorite count, use assign_my_favorite_cnt instead
- The action_type parameter allows different types of engagement tracking
- Uses Favorite::favoriteCount() internally

---

## assign_my_favorite_cnt

Get the current user's favorite count for their favorites list.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the count |

### Return Value

Integer count of the current user's favorites assigned to the specified variable.

### Usage Example

```smarty
{assign_my_favorite_cnt module_type='topics' var='my_favorites'}
<p>You have {$my_favorites} favorite articles</p>
{assign_my_favorite_cnt module_type='topics' module_id=$topics.topics_id var='is_fav'}
{if $is_fav > 0}
  <span class="favorited">Favorited</span>
{/if}
{assign_my_favorite_cnt module_type='topics' topics_group_id=5 var='news_favorites'}
```

### Notes

- Returns 0 if user has no favorites matching criteria
- When module_id is omitted, counts all user's favorites of that type
- Cookie-based favorites are useful for guest users

---

## assign_relation_tag_list

Retrieve tags associated with a specific content item.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the result array |

### Return Value

Array of tag objects assigned to the specified variable.

### Usage Example

```smarty
{assign_relation_tag_list module="topics" module_id=$topics.topics_id var="tags"}
{if $tags}
  <div class="tags">
    {foreach $tags as $tag}
      <a href="/tag/{$tag.tag_id}/" class="tag">{$tag.tag_nm}</a>
    {/foreach}
  </div>
{/if}
```

### Notes

- Returns false if database connection is unavailable
- Only returns published tags (open_flg = 1) by default
- Uses Tag::getTagRelation() internally

---

## assign_group_nm

Retrieve the display name of a member group by its ID.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | Variable name to store the group name |

### Return Value

Group name string assigned to the specified variable.

### Usage Example

```smarty
{assign_group_nm group_id=100 var='group_name'}
<p>Group: {$group_name}</p>
{assign_group_nm id=$member.group_id var='member_group'}
{foreach $members as $member}
  {assign_group_nm id=$member.group_id var='grp_nm'}
  <tr>
    <td>{$member.name1}</td>
    <td>{$grp_nm}</td>
  </tr>
{/foreach}
```

### Notes

- Returns false if database connection is unavailable
- The id parameter is an alias for group_id (either works)
- Supports multi-language group names when USE_MULTILANG is enabled
- Uses Group::getNameList() internally

---

## assign_api_credential

API認証情報（署名、セッションID、JWT等）を生成します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数に認証情報の連想配列が代入されます。member_id指定時は session_id, X-RCMS-API-ACCESS-TOKEN, jwt を含み、api_key指定時は signature, DG_CODE, sid, jwt を含みます。

### Usage Example

```smarty
{* APIキーを使用して認証情報を生成 *}
{assign_api_credential api_key=$api_key dg_key="topics_edit_api" dg_id="0" var=credentials}
{* 特定メンバーの認証情報を生成 *}
{assign_api_credential member_id=123 expire=300 var=credentials}
{* JWTに追加データを含める *}
{assign_api_credential member_id=123 jwt_data=$custom_data var=credentials}
```

### Notes

- ログインが必要です（member_id指定時を除く）
- `member_id` を指定した場合は、そのメンバーの認証情報が生成されます
- `api_key` を指定した場合は、現在のログインユーザーの認証情報が生成されます
- 生成されたJWTには `member_id`, `credentials`, `data` が含まれます
- データベース接続がない場合やシステムエラー時は `false` を返します

