# Kurocoドキュメント: リファレンス / API（2/3）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- エンドポイント 基本設定/詳細設定一覧（`endpoint-parameters`）
- エンドポイント 設定項目一覧（`endpoint-settings`）


---

# エンドポイント 基本設定/詳細設定一覧

> 元ページ: `reference/endpoint-parameters` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/endpoint-parameters/
> 概要: API画面では、APIエンドポイントの追加/更新ができます。各エンドポイントにはその動作を制御するためのパラメータが設定可能です。ここでは、エンドポイントに設定できるパラメータについて説明します

[API](/ja/docs/management/api-list/)画面では、APIエンドポイントの追加/更新ができます。  
各エンドポイントにはその動作を制御するためのパラメータが設定可能です。

ここでは、エンドポイントに設定できるパラメータについて説明します。  

## エンドポイントの設定画面
エンドポイントの設定で、モデルを選択すると、選択したモデルに設定できるパラメータが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f549f65462148d9bf322f6bd24fdfedd.png)

## 認証
### Login
#### login_challenge
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|login_method|認証方式を選択します。選択可能値: `api_key/signature`（APIキーとシグネチャによる認証）。未設定の場合はメールアドレスとパスワードによる認証になります。|
||twofactor_method|二要素認証を有効にする場合、その方式を選択します。選択可能値: `code`（TOTP）, `email`（メール）, `SMS`（SMS）|
|詳細設定|use_recaptcha|チェックを入れると、ログイン時にreCAPTCHAを使用します。|

#### login_challenge_mfa
設定できるパラメータなし。

#### token
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|use_refresh_token|チェックを入れるとリフレッシュトークンを利用します。|
||access_token_lifespan|アクセストークンが有効である秒数を設定します。|
||refresh_token_lifespan|リフレッシュトークンが有効である秒数を設定します。|

#### file_access_token
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|access_token_lifespan|ファイルアクセストークンが有効である秒数を設定します。デフォルトは300秒（5分）です。|

#### alias_login
設定できるパラメータなし。

#### logout
設定できるパラメータなし。

#### reminder
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|password_reset_page_url|ユーザーのメールに表示されるパスワードリセットページのURL。トークンはクエリパラメータとして自動的に追加されます。|
|詳細設定|token_fragment_flg|チェックを入れると、トークンをURLフラグメントの形式で渡します。(デフォルトではクエリパラメータを利用)|
||use_recaptcha|チェックを入れると、リマインドメール送信時にreCAPTCHAを使用します。詳しくは[reCAPTCHAを利用したパスワードリマインダーを作成する](/ja/docs/tutorials/using-recaptcha-for-password-reminders/)を参照してください。|

#### reset_password
設定できるパラメータなし。

#### profile
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|basic_info|取得するユーザ情報の属性を指定します。(複数可能) 例) email,nickname|

#### gcs_info
設定できるパラメータなし。

#### firebaseToken
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|firebaseConfig|`add`を選択すると、firebaseConfigの情報をレスポンスに追加します。|

### LoginHistory
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|cnt|1ページの表示件数を指定します。|
||allowed_group_ids|閲覧を許可するグループIDを指定します。指定したグループに所属するメンバーのログイン履歴のみが対象になります。|
||self_only|チェックを入れると、自分自身のログイン履歴のみを対象にします。|
||from_date|検索する開始日を指定します。|
||to_date|検索する終了日を指定します。|
||login_type|ログインの種類を指定します。|
||member_id|対象のメンバーIDを指定します。|
||add_member_info_cols|取得したいメンバー属性を指定します。(複数可能) 例) email,nickname|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

### LoginFailed
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|cnt|1ページの表示件数を指定します。|
||allowed_group_ids|閲覧を許可するグループIDを指定します。指定したグループに所属するメンバーのログイン失敗履歴のみが対象になります。|
||self_only|チェックを入れると、自分自身のログイン失敗履歴のみを対象にします。|
||from_date|検索する開始日を指定します。|
||to_date|検索する終了日を指定します。|
||member_id|対象のメンバーIDを指定します。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

### TwofactorMethod
#### reserve
設定できるパラメータなし。

#### regist
設定できるパラメータなし。

#### reminder
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|use_sms|チェックを入れると、二要素認証のリセットコードをSMSで送信します。|

#### reset
設定できるパラメータなし。

#### delete
設定できるパラメータなし。

## コンテンツ
### Topics
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||contents_type|表示するカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_lang|フィルターの言語を指定します。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|
||cnt|1ページの表示件数を指定します。|
||order_query|並び順を指定します。<br/>例）`topics_id:asc`、`topics_id:desc` <br/>指定可能な項目： topics_id, order_no, ymd, post_time, contents_type, subject, regular_flg, inst_ymdhi, update_ymdhi, topics_group_id, favorite_cnt, comment_cnt|
||groupBy|カテゴリ毎にグルーピングをする場合、categoryを選択します。|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|type|グルーピングの種類を選択します。(array or object), default: array|
||group_by_category_id|カテゴリでグルーピングした場合に、絞り込むカテゴリIDを指定します。|
||show_empty_categories|カテゴリでグルーピングした場合にチェックを入れると、コンテンツが存在しないカテゴリも表示します。|
||order_by_category_count|カテゴリでグルーピングした場合にチェックを入れると、カテゴリごとの件数で並べ替えます。|
||has_permissions|エンドポイントにアクセスするユーザーが、パラメータに設定した権限('insert', 'update', 'delete')を有する場合にのみレスポンスを返します。例えば、has_permissions=deleteが設定されているエンドポイントに、コンテンツの更新権限のみを持つ編集ユーザーがアクセスした場合は権限が無いので0件でレスポンスされます。|
||category_grouping_type|カテゴリのグルーピングのキーの形式を選択します。選択可能値: `object`|
||category_grouping_type_use_slug|カテゴリグルーピングでスラッグをキーとして利用します。|
||max_distance|最大距離を指定します。（位置情報による検索に使用）|
||category_parent_id|絞り込む親カテゴリを指定します。|
||exclude_category_parent_id|表示しないカテゴリIDを指定します。|
||ext_column|拡張項目の値で一覧を絞りこみます。<br/>指定した値で絞り込む例：`ext_column=ext_col_02:15`<br/>指定した値以外で絞り込む例：`ext_column=ext_col_02!:15`|
||ymd_sort_change|コンテンツの並び順を日付の昇順に変更したい場合、`ymd_sort_change=on`を入力します。（デフォルトは降順です。）|
||shuffle|ランダム表示にするかどうか(yes/no) 通常はランダムではありません。|
||target_col_for_keyword|キーワード検索の対象カラムを指定します。 設定がない場合はタイトル、本文、カテゴリ、拡張項目が対象になります。 補足) subject,contents,contents_typeまたは拡張項目no(ext_col_01,ext_col_10など)を設定します。|
||use_target_col_for_keyword_from_request|リクエストでキーワード検索の対象項目の絞り込むを利用する。|
||topics_keyword_cond|topics_keywordによる検索でキーワード毎の絞り込み方を変える。(デフォルト：AND)|
||full_text_search_cond|全文検索のキーワード毎の絞り込み方を変えます。選択可能値: `AND`, `OR`|
||tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||exclude_tag_category_id|表示対象から除外するタグカテゴリIDを指定します。|
||tag_id|表示対象になるタグIDを指定します。|
||exclude_tag_id|表示対象から除外するタグIDを指定します。|
||tag_cond|タグの絞り込み方を変える(デフォルト：OR)|
||topics_id|表示するコンテンツIDを設定します。|
||order_by_id|topics_idで並び順を指定できます。指定したtopics_idのデータが上位表示されます。|
||exclude_topics_id|除外するコンテンツIDを指定します。|
||get_comment_cnt|チェックを入れるとレスポンスにコメント数が追加されます。|
||get_unlisted_data|チェックを入れるとレスポンスに一覧に載せないデータも含まれるようになります。|
||comment_cond_date|コメント数を取得する際の日付条件を設定します。（例：7日前の場合「-7 day」）|
||get_favorite_cnt|チェックを入れるとレスポンスにお気に入り数が追加されます。|
||get_last_favorite_ymdhi|チェックを入れるとレスポンスに各コンテンツが最後にお気に入りされた日時（`last_favorite_ymdhi`）が追加されます。`favorite_action_type`を併用した場合は種別ごとの日時も取得できます。`last_favorite_ymdhi`での並べ替え（`order_query`）にも対応しています。|
||my_favorite_list|チェックを入れると自分のお気に入りでコンテンツを絞り込みます。|
||my_comment_list|チェックを入れると自分のコメントしたコンテンツを絞り込みます。|
||my_own_list|チェックを入れると自分の所有コンテンツを絞り込みます。|
||add_owner_info_cols|取得したいコンテンツ所有者属性を指定します。(複数可能) 例: email,nickname|
||required_param|必須にしたいクエリパラメータを指定します。|
||add_my_favorite_flg|チェックを入れると、エンドポイントを呼び出したユーザーが対象のコンテンツをお気に入り登録しているかがレスポンスに追加されます。<br/>お気に入り登録している=>"my_favorite_flg": true<br/>お気に入り登録していない=>"my_favorite_flg": false|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||favorite_action_type|my_favorite_listを有効にした場合、お気に入りのアクションタイプを指定してさらに詳しく絞り込みます。|
||exclude_favorited_topics|お気に入り済みのデータを対象外とします。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||get_tag_order_by_tag_category|get_tag_flgが有効な場合にチェックを入れると、カテゴリ毎にタグを並べます。|
||ignore_open_flg|チェックを入れると非公開コンテンツをレスポンスに含めます。|
||ignore_category_open_flg|チェックを入れると非公開カテゴリのコンテンツもレスポンスに含めます。|
||ignore_tag_open_flg|チェックを入れると非公開タグのコンテンツもレスポンスに含めます。|
||central_id|取得の中心にするIDを指定します。|
||add_open_ymdhi|チェックを入れると公開開始・終了日時をレスポンスに含めます。|
||ignore_restrict_flg|チェックを入れるとアクセス制限を無視します。|
||use_pre_embedding_text|チェックを入れると事前に生成されたembeddingテキストを使用します。|
||max_list_chars|一覧表示時の最大文字数を指定します。0の場合は制限なし。|
||langs_open_flg|チェックを入れると、各コンテンツに全設定言語の公開状態を示す`langs_open_flg`オブジェクト（例: `{"en":1,"ja":0}`）がレスポンスに追加されます。言語ごとに個別のAPIリクエストを行わずに言語切替の表示が可能になります。|

#### details
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||contents_type|表示するカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_lang|フィルターの言語を指定します。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|category_parent_id|絞り込む親カテゴリを指定します。|
||exclude_category_parent_id|表示しないカテゴリIDを指定します。|
||ext_column|拡張項目の値で一覧を絞り込みます。<br/>指定した値で絞り込む例：`ext_column=ext_col_02:15`<br/>指定した値以外で絞り込む例：`ext_column=ext_col_02!:15`|
||target_col_for_keyword|キーワード検索の対象カラムを指定します。設定がない場合はタイトル、本文、カテゴリ、拡張項目が対象になります。 補足) subject,contents,contents_typeまたは拡張項目no(ext_col_01,ext_col_10など)を設定します。|
||use_target_col_for_keyword_from_request|リクエストでキーワード検索の対象項目の絞り込みを利用する。|
||topics_keyword_cond|キーワード検索のキーワード毎の絞り込み方を変える。（デフォルト：AND)|
||full_text_search_cond|全文検索のキーワード毎の絞り込み方を変えます。選択可能値: `AND`, `OR`|
||tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||exclude_tag_category_id|表示対象から除外するタグカテゴリIDを指定します。|
||tag_id|表示対象になるタグIDを指定します。|
||exclude_tag_id|表示対象から除外するタグIDを指定します。|
||tag_cond|タグの絞り込み方を変える（デフォルト：OR)|
||exclude_topics_id|除外するコンテンツIDを指定します。|
||get_comment_cnt|チェックを入れるとレスポンスにコメント数が追加されます。|
||get_unlisted_data|チェックを入れるとレスポンスに一覧に載せないデータも含まれるようになります。|
||comment_cond_date|コメント数を取得する際の日付条件を設定します。（例：7日前の場合「-7 day」）|
||get_favorite_cnt|チェックを入れるとレスポンスにお気に入り数が追加されます。|
||my_favorite_list|チェックを入れると自分のお気に入りでコンテンツを絞り込みます。|
||my_comment_list|チェックを入れると自分のコメントしたコンテンツを絞り込みます。|
||my_own_list|チェックを入れると自分の所有コンテンツを絞り込みます。|
||add_owner_info_cols|取得したいコンテンツ所有者属性を指定します。(複数可能) 例) email,nickname|
||required_param|必須にしたいクエリパラメータを指定します。|
||add_my_favorite_flg|チェックを入れると、エンドポイントを呼び出したユーザーが対象のコンテンツをお気に入り登録しているかがレスポンスに追加されます。<br/>お気に入り登録している=>"my_favorite_flg": true<br/>お気に入り登録していない=>"my_favorite_flg": false|
||favorite_action_type|my_favorite_listを有効にした場合、お気に入りのアクションタイプを指定してさらに詳しく絞り込みます。|
||exclude_favorited_topics|お気に入り済みのデータを対象外とします。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||get_tag_order_by_tag_category|get_tag_flgが有効な場合にチェックを入れると、カテゴリ毎にタグを並べます。|
||ignore_open_flg|チェックを入れると非公開コンテンツをレスポンスに含めます。|
||ignore_category_open_flg|チェックを入れると非公開カテゴリのコンテンツもレスポンスに含めます。|
||ignore_tag_open_flg|チェックを入れると非公開タグのコンテンツもレスポンスに含めます。|
||add_open_ymdhi|チェックを入れると公開開始・終了日時をレスポンスに含めます。|
||ignore_restrict_flg|チェックを入れるとアクセス制限を無視します。|
||use_pre_embedding_text|チェックを入れると事前に生成されたembeddingテキストを使用します。|
||max_list_chars|一覧表示時の最大文字数を指定します。0の場合は制限なし。|
||langs_open_flg|チェックを入れると、各コンテンツに全設定言語の公開状態を示す`langs_open_flg`オブジェクト（例: `{"en":1,"ja":0}`）がレスポンスに追加されます。言語ごとに個別のAPIリクエストを行わずに言語切替の表示が可能になります。|

#### preview
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||contents_type|表示するカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_lang|フィルターの言語を指定します。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|category_parent_id|絞り込む親カテゴリを指定します。|
||exclude_category_parent_id|表示しないカテゴリIDを指定します。|
||ext_column|拡張項目の値で一覧を絞り込みます。<br/>指定した値で絞り込む例：`ext_column=ext_col_02:15`<br/>指定した値以外で絞り込む例：`ext_column=ext_col_02!:15`|
||target_col_for_keyword|キーワード検索の対象カラムを指定します。設定がない場合はタイトル、本文、カテゴリ、拡張項目が対象になります。 補足) subject,contents,contents_typeまたは拡張項目no(ext_col_01,ext_col_10など)を設定します。|
||use_target_col_for_keyword_from_request|リクエストでキーワード検索の対象項目の絞り込みを利用する。|
||topics_keyword_cond|キーワード検索のキーワード毎の絞り込み方を変える。（デフォルト：AND)|
||full_text_search_cond|全文検索のキーワード毎の絞り込み方を変えます。選択可能値: `AND`, `OR`|
||tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||exclude_tag_category_id|表示対象から除外するタグカテゴリIDを指定します。|
||tag_id|表示対象になるタグIDを指定します。|
||exclude_tag_id|表示対象から除外するタグIDを指定します。|
||tag_cond|タグの絞り込み方を変える（デフォルト：OR)|
||exclude_topics_id|除外するコンテンツIDを指定します。|
||get_comment_cnt|チェックを入れるとレスポンスにコメント数が追加されます。|
||get_unlisted_data|チェックを入れるとレスポンスに一覧に載せないデータも含まれるようになります。|
||comment_cond_date|コメント数を取得する際の日付条件を設定します。（例：7日前の場合「-7 day」）|
||get_favorite_cnt|チェックを入れるとレスポンスにお気に入り数が追加されます。|
||get_last_favorite_ymdhi|チェックを入れるとレスポンスに各コンテンツが最後にお気に入りされた日時（`last_favorite_ymdhi`）が追加されます。`favorite_action_type`を併用した場合は種別ごとの日時も取得できます。`last_favorite_ymdhi`での並べ替え（`order_query`）にも対応しています。|
||my_favorite_list|チェックを入れると自分のお気に入りでコンテンツを絞り込みます。|
||my_comment_list|チェックを入れると自分のコメントしたコンテンツを絞り込みます。|
||my_own_list|チェックを入れると自分の所有コンテンツを絞り込みます。|
||add_owner_info_cols|取得したいコンテンツ所有者属性を指定します。(複数可能) 例) email,nickname|
||required_param|必須にしたいクエリパラメータを指定します。|
||add_my_favorite_flg|チェックを入れると、エンドポイントを呼び出したユーザーが対象のコンテンツをお気に入り登録しているかがレスポンスに追加されます。<br/>お気に入り登録している=>"my_favorite_flg": true<br/>お気に入り登録していない=>"my_favorite_flg": false|
||favorite_action_type|my_favorite_listを有効にした場合、お気に入りのアクションタイプを指定してさらに詳しく絞り込みます。|
||exclude_favorited_topics|お気に入り済みのデータを対象外とします。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||get_tag_order_by_tag_category|get_tag_flgが有効な場合にチェックを入れると、カテゴリ毎にタグを並べます。|
||ignore_open_flg|チェックを入れると非公開コンテンツをレスポンスに含めます。|
||ignore_category_open_flg|チェックを入れると非公開カテゴリのコンテンツもレスポンスに含めます。|
||ignore_tag_open_flg|チェックを入れると非公開タグのコンテンツもレスポンスに含めます。|
||add_open_ymdhi|チェックを入れると公開開始・終了日時をレスポンスに含めます。|
||ignore_restrict_flg|チェックを入れるとアクセス制限を無視します。|
||use_pre_embedding_text|チェックを入れると事前に生成されたembeddingテキストを使用します。|
||max_list_chars|一覧表示時の最大文字数を指定します。0の場合は制限なし。|

#### insert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|追加するコンテンツ定義IDを指定します。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|validate_only|入力チェックのみを行い、実際のデータ更新は行いません。|
||lightweight_mode|軽量モード: 有効な場合、後処理バッチの実行をスキップしますが、代わりにパフォーマンスが向上します。|
||upsert_by_columns|指定したカラムにpostされた値があれば、その値を持つレコードを更新します。|
||compare_by_columns|指定したカラムの値を比較し、変更がある場合のみ更新します。|

#### update
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|更新するコンテンツ定義IDを指定します。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|validate_only|入力チェックのみを行い、実際のデータ更新は行いません。|
||lightweight_mode|軽量モード: 有効な場合、後処理バッチの実行をスキップしますが、代わりにパフォーマンスが向上します。|

#### delete
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|削除するコンテンツ定義IDを指定します。|

#### draft_list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||self_only|ログインしているユーザー（自分のデータ）に対応するデータのみを返す／更新可能|
||cnt|1ページの表示件数を指定します。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|

#### draft_detail
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||self_only|ログインしているユーザー（自分のデータ）に対応するデータのみを返す／更新可能|
||ext_group|グループ化された拡張項目をまとめる。|

#### draft_save
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||topics_id|draft_save時に、対象にするtopics_idを指定します。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|upsert_by_columns|指定したカラムにpostされた値があれば、その値を持つレコードを更新します。|
||compare_by_columns|指定したカラムの値を比較し、変更がある場合のみ更新します。|

#### draft_delete
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|

#### draft_update
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||topics_id|対象にするコンテンツIDを指定します。|

#### waiting_for_approval_list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||self_only|ログインしているユーザー（自分のデータ）に対応するデータのみを返す／更新可能|
||cnt|1ページの表示件数を指定します。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|
||get_workflow_info|チェックを入れるとワークフロー情報をレスポンスに追加します。|

#### waiting_for_approval_details
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||self_only|ログインしているユーザー（自分のデータ）に対応するデータのみを返す／更新可能|
||ext_group|グループ化された拡張項目をまとめる。|

#### history_list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
|詳細設定|diff_only|項目のみ取得する。(detail要素がレスポンスされない形になります。) ![Image from Gyazo](https://t.gyazo.com/teams/diverta/835eb46e745bdc28429924ccee55f89b.png)|

#### accept
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|validate_only|入力チェックのみを行い、実際のデータ更新は行いません。|

#### reject
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|

#### bulk_upsert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
||ext_group|チェックを入れるとグループ化された拡張項目をまとめる。|
|詳細設定|postprocess_min_after|更新の後処理バッチを何分後に登録するか (デフォルト: 1)|
||lightweight_mode|軽量モード: 有効な場合、後処理バッチの実行をスキップしますが、代わりにパフォーマンスが向上します。|
||id_reference_allow_list|外部システムのデータIDを指定します。|
||ignore_errors|エラーが発生しても無視して処理を続行します。|
||validate_only|入力チェックのみを行い、実際のデータ更新は行いません。|

#### bulk_download
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||file_type|ファイルタイプを選択します。(デフォルトはcsvです。ファイルダウンロードの場合はfileを選択してください)|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||order_query|並び順を指定します。例）`topics_id=ASC`|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||output_columns|出力する列を指定します。|

#### increment
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||ext_nm|対象の拡張項目名(ID/Slug)を指定します。|
||index|配列型の拡張項目の場合、対象のインデックスを指定します。|
|詳細設定|nums|増減できる数値の制限を指定します。|
||num|増減する固定数値を指定します。|
||use_recaptcha|チェックを入れると、reCAPTCHAを使用します。|

### TopicsCategory
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||contents_type|表示するカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||cnt|1ページの表示件数を指定します。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
|詳細設定|count_by_category|カテゴリごとの件数を取得する。取得しない:0(デフォルト) 取得する:1|
||count_by_category_method|カテゴリ件数の集計方法を選択します。親カテゴリのみの件数、または子カテゴリを含めた件数を指定できます。|
||order_by_count|カテゴリごとの件数で並べ替えます。|
||ignore_open_flg|チェックを入れると非公開カテゴリもレスポンスに含めます。|

### TopicsGroup
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||cnt|1ページの表示行数を指定します。|

#### details
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||ext_config_flg|拡張項目設定を取得するか指定します、取得した拡張情報は$extensions_configにassignされます。|
||ext_no_for_count|件数を取得したい選択系拡張番号を指定します。|

#### insert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|open_flg|公開フラグを設定します。|

## テーブル
### Master
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|csvtable_id|対象にするcsvテーブルIDを指定します。|
||key_idx|レスポンス時、key:valueのkeyになる要素のインデックスを指定します。|
||value_idx|レスポンス時、key:valueのvalueになる要素のインデックスを指定します。|
||multiple|key_idxの要素で多次元にするかを指定します。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
|詳細設定|outputAs|アウトプットフォーマットを指定します。選択可能値: `array`, `object`|
||groupBy|グルーピングの単位を指定します。|
||type|グルーピングの結果形式を指定します。選択可能値: `array`, `object`（デフォルト: `array`）|

#### insert
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|required_columns|アップロードするCSV/JSONのヘッダー行に必須のカラム名を指定します。指定したカラムがデータに含まれていない場合、400エラーが返されます。|
||allowed_columns|アップロードするCSV/JSONのヘッダー行に許可するカラム名を指定します。指定したカラム以外がデータに含まれている場合、400エラーが返されます。|

#### update
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|csvtable_id|対象にするcsvテーブルIDを指定します。|
||required_columns|アップロードするCSV/JSONのヘッダー行に必須のカラム名を指定します。指定したカラムがデータに含まれていない場合、400エラーが返されます。|
||allowed_columns|アップロードするCSV/JSONのヘッダー行に許可するカラム名を指定します。指定したカラム以外がデータに含まれている場合、400エラーが返されます。|

#### delete
設定できるパラメータなし。

## タグ
### Tag
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|
||order_query|並び順を指定します。例）`foo=ASC,bar=DESC`|
||tag_id|表示対象になるタグIDを指定します。|
||tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||cnt|1ページの表示件数を指定します。|
||order|並び順を設定します。例）`tag_id:asc`、`tag_id:desc` 指定可能な項目： tag_id, open_contents_cnt, tag_category_id, weight, tag_nm|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
|詳細設定|groupBy|グルーピングの単位を指定します。選択可能値: `module_id`, `category`|
||type|グルーピングの結果形式を指定します。選択可能値: `array`, `object`|
||shuffle|ランダム表示にするかどうか(yes/no) 通常はランダムではありません。|
||exclude_tag_category_id|表示対象から除外するタグカテゴリIDを指定します。|
||exclude_tag_id|表示対象から除外するタグIDを指定します。|
||ignore_open_flg|チェックを入れると非公開タグもレスポンスに含めます。|
||target_topics_group_id|フィルタリング対象のコンテンツ定義IDを指定します。|

#### insert
設定できるパラメータなし。

#### update
設定できるパラメータなし。

#### delete
設定できるパラメータなし。

### TagCategory
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||parent_tag_category_id|表示対象になる親タグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||without_tag_info|チェックを入れるとタグ情報を取得しません。|
|詳細設定|no_classified_flg|タグカテゴリごとのタグ一覧を取得する場合に、どのタグカテゴリにも属さないタグを無視します。デフォルトではタグカテゴリの存在しないタグは「未設定」というカテゴリの下に入れて返されます。|

## ファイル
### Files
#### upload
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|storage|アップロードしたファイルの一時保存先を選択します。選択可能値: `KurocoFiles`, `GCS`, `S3`。未設定・`GCS`・`S3`の場合で、かつサイトがGCS/S3と連携している場合、ファイルはGCS/S3（外部ストレージ）にアップロードされます。|
||access_control|アップロードしたファイルのアクセス制御を指定します。選択可能値: `public`, `private`。デフォルトは`public`です。この設定はGCS/S3にアップロードする場合（`storage`が未設定・`GCS`・`S3`で、かつサイトがGCS/S3と連携している場合）にのみ有効です。`public`の場合、外部ストレージ上のファイルに署名なしのURLで直接アクセスできます。`private`の場合、外部ストレージ上のファイルには署名付きURL（有効期限あり）でのみアクセスできます。`storage`が`KurocoFiles`の場合やGCS/S3連携が設定されていない場合は、ファイルは外部ストレージにアップロードされないため、この設定は影響しません。|
||max_size|最大アップロードファイルサイズ（MB）。最大5120MB（5GB）。未設定の場合は無制限です。5120MBを超える値は設定できません（エンドポイント設定の保存時にエラーになります）。 |
||size|【非推奨】最大アップロードファイルサイズ（バイト）。`max_size`（MB）の利用を推奨します。両方設定されている場合は`max_size`が優先されます。|
||types|アップロード許可する拡張子を指定します。|

#### create_temp_upload_url
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|max_size|最大アップロードファイルサイズ（MB）。最大5120MB（5GB）。未設定の場合は100MBになります。申告された`file_size`がこの値を超える場合は422エラーになります。5120MBを超える値は設定できません（エンドポイント設定の保存時にエラーになります）。 |
||types|アップロード許可する拡張子を指定します。申告された`ext`が許可されていない場合は422エラーになります。 |
||storage|一時ファイルのアップロード先を選択します。選択可能値: `KurocoTemp`, `S3`。未設定の場合は`KurocoTemp`（Kurocoの一時ファイル用ストレージ）です。`S3`を指定した場合はサイト自身のS3バケットにアップロードされます。S3連携が設定されていないサイトおよびGCS連携のサイトで`S3`を指定した場合は400エラーになります。 |

:::caution
HTTP PUTによるアップロードではS3側でファイルサイズを制限できないため、`max_size`と`types`はアップロードされたファイルを利用（コンテンツへの紐付けなど）するタイミングでも検証されます。実際にアップロードされたファイルのサイズや形式が設定値に合わない場合、そのファイルは利用されません。
:::

#### create_temp_upload_post
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|max_size|最大アップロードファイルサイズ（MB）。最大5120MB（5GB）。未設定の場合は100MBになります。申告された`file_size`がこの値を超える場合は422エラーになります。5120MBを超える値は設定できません（エンドポイント設定の保存時にエラーになります）。 |
||types|アップロード許可する拡張子を指定します。申告された`ext`が許可されていない場合は422エラーになります。 |
||storage|一時ファイルのアップロード先を選択します。選択可能値: `KurocoTemp`, `S3`。未設定の場合は`KurocoTemp`（Kurocoの一時ファイル用ストレージ）です。`S3`を指定した場合はサイト自身のS3バケットにアップロードされます。S3連携が設定されていないサイトおよびGCS連携のサイトで`S3`を指定した場合は400エラーになります。 |

:::note
`create_temp_upload_post`では`max_size`がアップロード用の署名に含まれるため、S3側でも最大サイズを超えるアップロードが拒否されます。
:::

#### temp_upload_url
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|max_size|最大アップロードファイルサイズ（MB）。最大5120MB（5GB）。未設定の場合は100MBになります。5120MBを超える値は設定できません（エンドポイント設定の保存時にエラーになります）。 |
||types|アップロード許可する拡張子を指定します。 |
||storage|一時ファイルのアップロード先を選択します。選択可能値: `KurocoTemp`, `S3`。未設定の場合は`KurocoTemp`（Kurocoの一時ファイル用ストレージ）です。`S3`を指定した場合はサイト自身のS3バケットにアップロードされます。S3連携が設定されていないサイトおよびGCS連携のサイトで`S3`を指定した場合は400エラーになります。 |

:::caution
`temp_upload_url`は非推奨のエンドポイントです。新規に実装する場合は`create_temp_upload_url`または`create_temp_upload_post`を利用してください。`temp_upload_url`ではリクエスト時の`file_size`・`ext`の申告がないため、`max_size`と`types`はアップロードされたファイルを利用するタイミングで検証されます。
:::

:::caution
既存の`temp_upload_url`のエンドポイントにも`max_size`の未設定時のデフォルト（100MB）が適用されます。100MBを超えるファイルを扱っている場合は、エンドポイントの`max_size`に`0`（無制限）または必要なサイズを設定してください。
:::

### FileManager
#### upload
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|storage|アップロードストレージの設定を選択します。選択可能値: `kurocofiles_public`, `kurocofiles_private`, `cloud_public`, `cloud_private`|
||max_size|最大アップロードファイルサイズ（バイト）。未設定の場合は無制限です。|
||types|許可する拡張子を指定します。|
||directory|ベースディレクトリを指定します。|
||allow_overwrite|ファイルの上書きを許可するかどうかを指定します。|

#### delete
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|storage|アップロードストレージの設定を選択します。選択可能値: `kurocofiles_public`, `kurocofiles_private`, `cloud_public`, `cloud_private`|
||directory|ベースディレクトリを指定します。|

#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|storage|アップロードストレージの設定を選択します。選択可能値: `kurocofiles_public`, `kurocofiles_private`, `cloud_public`, `cloud_private`|
||directory|ベースディレクトリを指定します。|

## API
### Api
#### bulk
設定できるパラメータなし。

#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### openapi_data
設定できるパラメータなし。

#### request_api
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|function_id|対象にするfunction_idを指定します。|
||name|対象にする識別子を指定します。|
||show_contents|有効にすると、テンプレートが出力した文字列をJSONとして解釈し、その値がレスポンス全体になります（`{"data": ...}`のエンベロープなし）。テンプレートはJSONを直接出力する必要があります。無効の場合は、テンプレートでassignした`data`変数を`{"data": ...}`形式で返します。|
||use_path_param|パスパラメータを使用する。|

#### request_api_post
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|function_id|対象にするfunction_idを指定します。|
||name|対象にする識別子を指定します。|
||show_contents|有効にすると、テンプレートが出力した文字列をJSONとして解釈し、その値がレスポンス全体になります（`{"data": ...}`のエンベロープなし）。テンプレートはJSONを直接出力する必要があります。無効の場合は、テンプレートでassignした`data`変数を`{"data": ...}`形式で返します。|
||use_path_param|パスパラメータを使用する。|
|詳細設定|use_recaptcha|reCAPTCHAを使用する。|

#### proxy
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|proxy_end_point|プロキシ先のエンドポイントを指定します。|
||add_headers|追加するリクエストヘッダーを指定します。|
||add_request_params|追加するリクエストパラメータを指定します。|
||proxy_read_timeout|タイムアウトの制限時間を指定します。(秒)|
||allow_request_params|許可するリクエストパラメータを指定します。|
||allow_proxy_params|許可するプロキシパラメータを指定します。|

#### proxy_post
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|proxy_end_point|プロキシ先のエンドポイントを指定します。|
||add_headers|追加するリクエストヘッダーを指定します。|
||add_request_params|追加するリクエストパラメータを指定します。|
||proxy_read_timeout|タイムアウトの制限時間を指定します。(秒)|
||allow_request_params|許可するリクエストパラメータを指定します。|
||allow_proxy_params|許可するプロキシパラメータを指定します。|

#### aggregate
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|endpoints|エンドポイントを指定します。|
||order_by_columns|カラムによる並び順を指定します。|
||from_date|集計開始日を指定します。|
||to_date|集計終了日を指定します。|
||cnt|1ページの表示件数を指定します。|

#### add_site
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|copy_from_site_key|コピー元のサイトキーを指定します。|
||callback_batch_nm|コールバックバッチ名を指定します。|
||init_batch_nm|初期化バッチ名を指定します。|
||sign_up_as_superuser|スーパーユーザーによるサインアップをする。(する:1、しない:0)|
||release_level|リリースレベルを選択します。(α版:0、β版:1、RC版:20、RC版:90、正式版:100)|
|詳細設定|use_recaptcha|reCAPTCHAを使用する。|

#### site_list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|cnt|1ページの表示件数を指定します。|

#### sso_credentials
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_keys|対象にするサイトキーを指定します。|
||emails|クレデンシャルを発行するメンバーのEメールを指定します。|
||member_ids|クレデンシャルを発行するメンバーのメンバーIDを指定します。|
||member_register_flg|クレデンシャル発行時にメンバー登録をする。|
||use_login_id_flg|クレデンシャル発行時にログインIDでユーザーの有無をチェックする。|
||sso_group_ids|クレデンシャル発行時に登録グループIDを指定します。|
||expire|有効期限を指定します。(秒)|

## API管理
### ApiManagement
#### insert
設定できるパラメータなし。

#### update
設定できるパラメータなし。

## AI
### OpenAI
#### chat
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|model|言語モデルを選択します。|
||prompt|モデルに与える入力テキストで、モデルが生成するテキストの出発点となります。モデルは、この入力に基づいて文脈に適した応答や続きを生成します。プロンプトは、質問の形式、指示、またはシナリオの形式で与えることができます。モデルは、プロンプトに関連する情報に基づいて、意味のあるテキストを生成しようとします。|
||schema|JSON Schemaを指定します。指定すると、AIの出力が指定したスキーマに従った構造化JSON形式で返されます。|
||max_tokens_out|出力の最大トークン数を指定します。|
||input_dict_sys_nm|入力辞書のシステム名を指定します。|
||output_dict_sys_nm|出力辞書のシステム名を指定します。|
||safe_check|入力テキストの安全性チェックを行う。|
||max_input_length|入力テキストの最大文字数を指定します。|

#### rag_search
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|model|言語モデルを選択します。|
||topics_group_id|対象にするコンテンツ定義IDを指定します。|
||cnt|1ページの表示件数を指定します。|
||prompt|モデルに与える入力テキストで、モデルが生成するテキストの出発点となります。モデルは、この入力に基づいて文脈に適した応答や続きを生成します。プロンプトは、質問の形式、指示、またはシナリオの形式で与えることができます。モデルは、プロンプトに関連する情報に基づいて、意味のあるテキストを生成しようとします。|
||max_distance|ベクトル検索の最大距離を指定します。|
||use_tags|タグ情報を検索条件に使用する。|
||ext_info|レスポンスに含める拡張項目を指定します。|
||skip_proper_noun_detection|固有名詞の検出をスキップする。|
||date_column|日付絞り込みに使用するカラムを指定します。|
||input_dict_sys_nm|入力辞書のシステム名を指定します。|
||max_list_chars|レスポンスに含まれるコンテンツの最大文字数を指定します。|
||data_title|データのタイトルを指定します。|
||max_input_length|入力テキストの最大文字数を指定します。|
||safe_check|入力テキストの安全性チェックを行う。|
||required_categories|カテゴリによる絞り込みを必須にする。|
||required_tags|タグによる絞り込みを必須にする。|
||filter|[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|フロントエンドからのリクエストで許可するfilterのキーを指定します。|


#### chat_contents_search
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|model|言語モデルを選択します。|
||topics_group_id|対象にするコンテンツ定義IDを指定します。|
||cnt|1ページの表示件数を指定します。|
||prompt|モデルに与える入力テキストで、モデルが生成するテキストの出発点となります。モデルは、この入力に基づいて文脈に適した応答や続きを生成します。プロンプトは、質問の形式、指示、またはシナリオの形式で与えることができます。モデルは、プロンプトに関連する情報に基づいて、意味のあるテキストを生成しようとします。|
||max_distance|ベクトル検索の最大距離を指定します。|
||use_tags|タグ情報を検索条件に使用する。|
||ext_info|レスポンスに含める拡張項目を指定します。|
||max_tokens_out|出力の最大トークン数を指定します。|
||skip_proper_noun_detection|固有名詞の検出をスキップする。|
||date_column|日付絞り込みに使用するカラムを指定します。|
||max_referenced_contents_length|参照コンテンツの最大文字数を指定します。|
||input_dict_sys_nm|入力辞書のシステム名を指定します。|
||output_dict_sys_nm|出力辞書のシステム名を指定します。|
||data_title|データのタイトルを指定します。|
||max_input_length|入力テキストの最大文字数を指定します。|
||safe_check|入力テキストの安全性チェックを行う。|
||required_categories|カテゴリによる絞り込みを必須にする。|
||required_tags|タグによる絞り込みを必須にする。|
||filter|[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|フロントエンドからのリクエストで許可するfilterのキーを指定します。|

#### routing_rules
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|ai_router_id|対象にするAIルーターIDを指定します。|

### AiAgent
#### create_session
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|ai_agent_id|対象にするAIエージェントIDを指定します。|

#### send_message
設定できるパラメータなし。

## WEB
### InquiryMessage
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|inquiry_id|対象にしたいフォームIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||order_query|並び順を指定します。 例) foo=ASC,bar=DESC|
||member_info|取得したい回答ユーザ情報の属性を指定します。(複数可能)<br/>例) email,nickname|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
|詳細設定|include_child|振り分け回答も取得する。|
||cnt|1ページの表示件数を指定します。|

#### details 
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|inquiry_id|対象にしたいフォームIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||member_info|取得したい回答ユーザ情報の属性を指定します。(複数可能) 例) email,nickname|

#### send
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|id|対象にしたいフォームIDを指定します。|
||assign_status|回答に割り当てるステータスを指定します。|
|詳細設定|validate_only|入力チェックする。|
||member_info_flg|ログインしているメンバー情報を取得してメッセージテンプレートで$member_infoとしてアサインする。|
||allow_parent_inquiry_bn_id|リクエストボディでの親回答ID(parent_inquiry_bn_id)の指定を許可する。|
||use_recaptcha|reCAPTCHAを使用する。|

#### update
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|id|対象にしたいフォームIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||use_columns|利用する項目を指定します。|
|詳細設定|validate_only|入力チェックする。|

#### delete
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|id|対象にしたいフォームIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|

#### bulk_upsert
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|id|対象にしたいフォームIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||permission|許可するオペレーションを選択します。(insert or update)|

### InquiryForm
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|inquiry_id|対象にしたいフォームIDを指定します。|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||cnt|1ページの表示件数を指定します。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
|詳細設定|cols_type|カラムタイプを選択します。|
||show_all_status|全てのステータスを表示する。|

#### details
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|target_inquiry_id|対象にしたいフォームIDを指定します。|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
|詳細設定|cols_type|カラムタイプを選択します。|
||show_all_status|全てのステータスを表示する。|

#### insert
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|validate_only|入力チェックする。|

#### update
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|validate_only|入力チェックする。|

#### delete
設定できるパラメータなし。

#### report
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|inquiry_id|対象にしたいフォームIDを指定します。|

### KurocoFront
#### deploy
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|artifact_url|デプロイするアーティファクト（zipファイル）のURLを指定します。files-upload または files-temp_upload_url でKurocoにアップロードしたファイルのURLのみ指定できます。外部ホスト上のURLは指定できません。|
||domain|デプロイ先のドメインを指定します。|
||hash|デプロイのハッシュ識別子を指定します。（英数字7文字以上）|
||is_preview|プレビューデプロイとして実行する。|

### SpiderHistory
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|spider_settings_id|対象にするスパイダー設定IDを指定します。|

#### detail
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|spider_settings_id|対象にするスパイダー設定IDを指定します。|

#### logs
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|spider_settings_id|対象にするスパイダー設定IDを指定します。|

### Spider
#### insert
設定できるパラメータなし。

#### update
設定できるパラメータなし。

#### webhook
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|spider_settings_id|対象にするスパイダー設定IDを指定します。|
||spider_history_id|対象にするスパイダー履歴IDを指定します。|
||target_urls|クロール対象のURLを指定します。|

## メール
### Email
#### send
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|to|あて先メールアドレスを指定します。|
||subject|件名を指定します。|
||body|テキスト本文を指定します。|
||body_html|HTML本文を指定します。|
||from_email|送信者アドレスを指定します。サイト設定の送信ドメインに含まれるアドレスのみ指定できます。|
||from_name|送信者名を指定します。|
||type|メールのタイプを指定します。選択可能値: `text`, `html`|
||cc|Ccを指定します。|
||bcc|Bccを指定します。|
||reply_to|Reply-Toを指定します。|
||attachments|添付ファイルを指定します。|
||member_id|あて先をメンバーIDで指定します。指定した場合、`to`の代わりに該当メンバーのメールアドレスへ送信されます。利用にはメンバーの参照権限が必要です。|

## メッセージング
### Line
#### send
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|to|送信先IDを指定します。|

### Teams
#### send
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|conversation_id|Teams 会話IDを指定します。|
||service_url|Teams serviceUrlを指定します。|
||reply_to_id|Teams 返信先Activity IDを指定します。|

### Slack
#### send
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|channel|送信先のSlackチャンネルを指定します。|
||thread_ts|スレッド返信にする場合、親メッセージのタイムスタンプ（`1234567890.123456`形式）を指定します。|

#### get
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|channel|取得対象のSlackチャンネルを指定します。|
||ts|取得するメッセージのタイムスタンプ（`1234567890.123456`形式）を指定します。|

## 一括配信
### MagazineInfo
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|magazine_id|対象にする配信IDを指定します。|
||exclude_magazine_id|除外する配信IDを指定します。|
||cnt|1ページの表示件数を指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

### MagazineSubscriber
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|magazine_id|対象にする配信IDを指定します。|
||cnt|1ページの表示件数を指定します。|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### subscribe
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|購読許可するIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|

#### unsubscribe
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|購読解除許可するIDを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||required_key|購読者キーを要求する。|

### Magazine
#### send
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|送信許可する配信IDを指定します。|
||destination_id|送信するカスタムメンバーフィルターIDを指定します。|
||allow_destination_id|送信許可するカスタムメンバーフィルターIDを指定します。|
||mail_type|mail_typeを選択します。0:テキストメール 1:HTMLメール 3:モバイルメール|
||mail_template_name|HTML用メールテンプレート名を指定します。|
||mail_text_template_name|テキストメール用テンプレート名を指定します。|
||subject|件名を指定します。|

#### delete
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|削除許可する配信IDを指定します。|

#### subscribe
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|購読許可する配信IDを指定します。|

#### unsubscribe
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|購読解除許可する配信IDを指定します。|

#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|allow_magazine_id|閲覧許可する配信IDを指定します。|
||cnt|1ページの表示件数を指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||order_query|並び順を指定します。 例) foo=ASC,bar=DESC|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

## アクティビティ
### Comment
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|id|対象にするアクティビティIDを指定します。|
||module_id|モジュールIDを指定して下さい。|
||module_type|モジュールタイプを指定して下さい。例) topics or ec_product or tag or member or comment or csvtable|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||order_query|並び順を指定します。 例) foo=ASC,bar=DESC|
||cnt|1ページの表示件数を指定します。|
|詳細設定|groupBy|グルーピングの単位を選択します。|
||type|グルーピングの種類を選択します。(array or object), デフォルト: array|
||new_order_flg|新着順に表示する。|
||my_list|自分がしたコメント一覧を取得する。|
||to_me_list|自分宛のコメント一覧を取得する。|
||from_date|コメント抽出期間を指定します。（開始）（例：「2020－01－01」形式、または過去1ヶ月分を指定したい場合は「-1 month」と設定可能）|
||to_date|コメント抽出期間を指定します。（終了）（例：「2020－01－01」形式、または過去1ヶ月前までと指定したい場合は「-1 month」と設定可能）|
||member_info|取得したいコメントユーザ情報の属性を指定します。(複数可能) 例) email,nickname|
||to_member_info|取得したい被コメントユーザ情報の属性を指定します。(複数可能) 例) email,nickname|
||root|ツリー階層の親コメントIDを指定します。|
||depth|コメントの階層数を指定します。|
||children_cnt|子コメントの表示件数を指定します。|
||children_pageID|取得したい子コメントのpageID(何ページ目のデータ)を指定します。|
||flatten_hierarchy|ツリー構造をフラット構造に変換する。|
||explain_reason_hidden|レスポンスオブジェクトに、コメントを非表示にする理由を説明するフィールドを追加する。|
||show_hidden_comments|レスポンスオブジェクトに非表示のコメントを表示する。|

#### insert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|id|対象にするアクティビティIDを指定します。|
||order_desc_flg|初期投稿日時降順で表示します。|
|詳細設定|use_recaptcha|reCAPTCHAを使用する。|

#### update
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|id|対象にするアクティビティIDを指定します。|
||order_desc_flg|初期投稿日時降順で表示します。|

#### delete
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|id|対象にするアクティビティIDを指定します。|
||order_desc_flg|初期投稿日時降順で表示します。|

## お気に入り
### Favorite
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|action_type|対象にするアクション種別を指定します。数値またはスラッグ名で指定可能です。(デフォルト:0)|
||filter|データを絞り込むクエリパラメータです。詳しくは[こちら](/ja/docs/reference/filter-query/)を確認してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は :ALL を設定します。)|
||module_type|対象にするモジュールタイプを指定します。(デフォルト:topics)|
||cnt|1ページの表示件数を指定します。|
||order|並び順を指定します。例) inst_ymdhi:desc|
||self_only|自分の情報のみにAPIリクエストできます。|
|詳細設定|groupBy|グルーピングの単位を選択します。|
||type|グルーピングの種類を選択します。(array or object), デフォルト: array|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||my_list|ログインしているユーザーのお気に入り一覧を取得する。|
||member_info|取得したいユーザ情報の属性を指定します。(複数可能) 例) email,nickname|

#### insert
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|action_type|対象にするアクション種別を数値で指定します。(デフォルト:0)|
||module_type|対象にするモジュールタイプを指定します。(デフォルト:topics)|
|詳細設定|skip_cache_clear_on_favorite|お気に入り登録時にCDNキャッシュのパージをスキップする。|
||use_recaptcha|reCAPTCHAを使用する。|

#### delete
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|action_type|対象にするアクション種別を指定します。数値またはスラッグ名で指定可能です。(デフォルト:0)|
||module_type|対象にするモジュールタイプを指定します。(デフォルト:topics)|
||identify_by|リソースの識別方法を選択します。(favorite_id or body)|
|詳細設定|skip_cache_clear_on_favorite|お気に入り削除時にCDNキャッシュのパージをスキップする。|

## メンバー
### Member
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||cnt|1ページの表示件数を指定します。|
||order_query|並び順を指定します。|
|詳細設定|response_ec_data|チェックを入れるとEC関連データをレスポンスに含めます。|
||custom_search_id|対象にするメンバーのカスタムメンバーフィルターIDを指定します。|
||group_id|対象にするメンバーのグループIDを指定します。|
||member_id|対象にするメンバーIDを指定します。|
||assign_group_flg|チェックを入れるとグループ情報をレスポンスに含めます。|
||open_by_group|チェックを入れるとグループ権限で表示を絞り込みます。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||check_login_lock|チェックを入れるとログインロック状態を確認します。|

#### details
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||order_query|並び順を指定します。|
|詳細設定|response_ec_data|チェックを入れるとEC関連データをレスポンスに含めます。|
||custom_search_id|対象にするメンバーのカスタムメンバーフィルターIDを指定します。|
||group_id|対象にするメンバーのグループIDを指定します。|
||assign_group_flg|チェックを入れるとグループ情報をレスポンスに含めます。|
||open_by_group|チェックを入れるとグループ権限で表示を絞り込みます。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||check_login_lock|チェックを入れるとログインロック状態を確認します。|

#### invite
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|default_group_ids|メンバーが最初に所属するグループIDを指定します。ここでのグループID指定は、メンバー管理機能の初期グループ設定より優先されます。|
||admin_regist_ok|管理者(スーパーユーザー)として登録する。|
|詳細設定|use_recaptcha|チェックを入れると、reCAPTCHAを使用します。|

#### insert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|default_group_id|メンバーが最初に所属するグループIDを指定します。ここでのグループID指定は、メンバー管理機能の初期グループ設定より優先されます。|
||not_login_after_insert|チェックを入れると登録後にログインを行いません。|
||login_ok_flg|チェックを入れるとログインを許可します。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
|詳細設定|validate_only|入力チェックのみを行い、実際のデータ更新は行いません。|
||send_email_flg|チェックを入れるとメンバー情報登録完了時にユーザーへメール送信します。|
||ignore_force_chpwd|チェックを入れると初回ログイン時のパスワード変更をスキップします。|
||use_recaptcha|チェックを入れると、reCAPTCHAを使用します。|
||allow_ec_point|ec_pointパラメータによる確定ポイントの設定・更新を許可します。self_onlyが有効な場合は許可されません。|

#### update
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|allowed_group_ids|更新許可するグループを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|
|詳細設定|validate_only|入力チェックのみを行い、実際のデータ更新は行いません。|
||send_email_flg|チェックを入れるとメンバー情報更新完了時にユーザーへメール送信します。|
||check_current_pwd|チェックを入れると現在のパスワードの確認を行います。|
||keep_without_allowed_group_ids|チェックを入れると許可グループ外のメンバーも更新対象に含めます。|
||allow_ec_point|ec_pointパラメータによる確定ポイントの設定・更新を許可します。self_onlyが有効な場合は許可されません。|

#### delete
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|allowed_group_ids|削除許可するグループを指定します。|
||self_only|自分の情報のみにAPIリクエストできます。|

#### bulk_upsert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|init_group_id|メンバーが最初に所属するグループIDを指定します。ここでのグループID指定は、メンバー管理機能の初期グループ設定より優先されます。|
||allow_set_group|CSVに入力した「グループID」での登録を有効にする。|
||use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を設定する。|
||require_columns|必須項目を指定する。|
||login_ok_flg|ログイン許可する。|


### MemberProvisional
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|registration_status|登録状況によるフィルタを選択します。選択可能値: `registered`, `unregistered`|
||cnt|1ページの表示件数を指定します。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### insert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|default_group_ids|メンバー登録時、設定されるメンバーグループIDを指定します。|
||admin_regist_ok|管理者(スーパーユーザー)として登録する。|

#### update
設定できるパラメータなし。

#### delete
設定できるパラメータなし。

### MemberCustomSearch
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|cnt|1ページの表示件数を指定します。|
||share_type|共有区分を選択します。(1: 全体、2: 自分のみ、3: グループ指定)|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### details
設定できるパラメータなし。

#### insert
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|member_allow_list|メンバーのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||inquiry_allow_list|お問い合わせのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||ec_allow_list|ECのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||staticcontents_allow_list|静的コンテンツのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|

#### update
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|member_allow_list|メンバーのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||inquiry_allow_list|お問い合わせのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||ec_allow_list|ECのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|
||staticcontents_allow_list|静的コンテンツのfilterリクエストに指定可能な項目のリスト (デフォルト: 対象項目なし / 全項目を許可したい場合は`:ALL`を設定してください)|

#### delete
設定できるパラメータなし。

#### identify
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|
|詳細設定|use_recaptcha|チェックを入れると、reCAPTCHAを使用します。|

### MemberForm
#### details
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|use_columns|利用する項目を指定します。|
||unuse_columns|利用しない項目を指定します。|
||require_columns|必須項目を指定します。|

### MemberGroup
#### list
|項目   |パラメータ   |説明  |
| :--- | :--- | :--- |
|基本設定|group_ids|表示したいグループIDを指定します。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||exclude_group_ids|除外したいグループIDを指定します。指定したグループIDはレスポンスに含まれません。|

## 非同期タスク
### Batch
#### webhook
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|batch_id|対象にするバッチIDを指定します。|
||identifier|バッチの識別子を指定します。|

#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|詳細設定|only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### check_batch
設定できるパラメータなし。

## 承認ワークフロー
### Approvalflow
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|module_type|対象にするモジュールタイプを指定します。(対応しているモジュールはtopicsだけになります。)|
||module_id|対象にするモジュールIDを指定します。|

#### details
設定できるパラメータなし。

#### insert
設定できるパラメータなし。

#### update
設定できるパラメータなし。

#### update_flow_settings
設定できるパラメータなし。

#### delete
設定できるパラメータなし。

#### review
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|module_type|対象にするモジュールタイプを指定します。(対応しているモジュールはtopicsだけになります。)|

#### list_pending
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|module_type|対象にするモジュールタイプを指定します。(対応しているモジュールはtopicsだけになります。)|

#### pending_detail
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|module_type|対象にするモジュールタイプを指定します。(対応しているモジュールはtopicsだけになります。)|

## カスタム処理
### CustomProcessing
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|static_category_id|対象にするカスタム処理のカテゴリIDを指定します。（複数指定可能）|

#### details
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|static_category_id|対象にするカスタム処理のカテゴリIDを指定します。（複数指定可能）指定したカテゴリ以外のカスタム処理は取得できません。|

#### insert
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|static_category_id|対象にするカスタム処理のカテゴリIDを指定します。|

#### update
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|static_category_id|対象にするカスタム処理のカテゴリIDを指定します。|

#### delete
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|static_category_id|対象にするカスタム処理のカテゴリIDを指定します。|

#### validate
設定できるパラメータなし。

## EC
### ECOrderSubscription
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### details
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|

#### insert
設定できるパラメータなし。

#### auth_sp_career
設定できるパラメータなし。

### ECOrder
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### details
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|

#### total
設定できるパラメータなし。

#### purchase
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|validate_only|入力チェックする。|

#### cancel
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|self_only|自分の情報のみにAPIリクエストできます。|
||send_mail|メール送信する。|

#### insert
設定できるパラメータなし。

#### auth_sp_career
設定できるパラメータなし。

### ECDelivery
#### list
設定できるパラメータなし。

#### details
設定できるパラメータなし。

### ECCart
#### details
設定できるパラメータなし。

#### add
設定できるパラメータなし。

#### update
設定できるパラメータなし。

### ECShop
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|show_email_properties|問い合わせ受付などのEメールプロパティの表示・非表示オプション。|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### details
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|show_email_properties|問い合わせ受付などのEメールプロパティの表示・非表示オプション。|

### ECProduct
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||contents_type|表示するカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|
||cnt|1ページの表示件数を指定します。|
||order_query|並び順を指定します。<br/>例）`topics_id:asc`、`topics_id:desc` <br/>指定可能な項目： topics_id, order_no, ymd, post_time, contents_type, subject, regular_flg, inst_ymdhi, update_ymdhi, topics_group_id, favorite_cnt, comment_cnt|
||product_id|表示する商品ID、設定がない場合は全ての商品が対象となる。|
||ec_ext_options_search|商品一覧を拡張項目のオプションで絞り込むか指定します。指定する:1 指定しない:0|
||my_order_flg|自分が購入した商品を表示する。|
||ignore_product_open_flg|非公開商品を表示する。|
|詳細設定|category_parent_id|親カテゴリで絞り込む。絞り込む親カテゴリを指定します。|
||exclude_category_parent_id|表示しないカテゴリIDを指定します。|
||ext_column|拡張項目の値で一覧を絞り込む。 例 指定した値で絞り込む場合）ext_column=ext_col_02:15 例 指定した値以外で絞り込む場合) ext_column=ext_col_02!:15|
||ymd_sort_change|コンテンツの並び順を日付の昇順に変更したい場合、`ymd_sort_change=on`を入力します。（デフォルトは降順です。）|
||shuffle|ランダム表示にするかどうか(yes/no) 通常はランダムではありません。|
||target_col_for_keyword|キーワード検索の対象カラムを指定します。 設定がない場合はタイトル、本文、カテゴリ、拡張項目が対象になります。 補足) subject,contents,contents_typeまたは拡張項目no(ext_col_01,ext_col_10など)を設定します。|
||use_target_col_for_keyword_from_request|リクエストでキーワード検索の対象項目の絞り込むを利用する。|
||topics_keyword_cond|キーワード検索のキーワード毎の絞り込み方を変える。（デフォルト：AND)|
||full_text_search_cond|全文検索のキーワード毎の絞り込み方を変えます。選択可能値: `AND`, `OR`|
||tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||exclude_tag_category_id|表示対象から除外するタグカテゴリIDを指定します。|
||tag_id|表示対象になるタグIDを指定します。|
||exclude_tag_id|表示対象から除外するタグIDを指定します。|
||tag_cond|タグの絞り込み方を変える（デフォルト：OR)|
||topics_id|表示するコンテンツIDを設定します。|
||order_by_id|topics_idで並び順を指定できます。指定したtopics_idのデータが上位表示されます。|
||exclude_topics_id|除外するコンテンツIDを指定します。|
||get_comment_cnt|コメント数を取得する。|
||get_unlisted_data|一覧に載せないデータも取得する。|
||comment_cond_date|コメント数を取得する際の日付条件を設定する。（例：7日前の場合「-7 day」）|
||get_favorite_cnt|お気に入り数を取得する。|
||my_favorite_list|自分のお気に入りでコンテンツ絞り込む。|
||my_comment_list|自分のコメントしたコンテンツで絞り込む。|
||my_own_list|自分の所有コンテンツで絞り込む。|
||add_owner_info_cols|取得したいコンテンツ所有者属性を指定します。(複数可能) 例) email,nickname|
||required_param|必須にしたいクエリパラメータを指定します。|
||add_my_favorite_flg|チェックを入れると、エンドポイントを呼び出したユーザーが対象のコンテンツをお気に入り登録しているかがレスポンスに追加されます。<br/>お気に入り登録している=>"my_favorite_flg": true<br/>お気に入り登録していない=>"my_favorite_flg": false|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||favorite_action_type|my_favorite_listを有効にした場合、お気に入りのアクションタイプを指定してさらに詳しく絞り込みます。|
||exclude_favorited_topics|お気に入り済みのデータを対象外とする。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||get_tag_order_by_tag_category|get_tag_flgが有効な場合にチェックを入れると、カテゴリ毎にタグを並べます。|
||ignore_open_flg|チェックを入れると非公開コンテンツをレスポンスに含めます。|
||ignore_category_open_flg|チェックを入れると非公開カテゴリのコンテンツもレスポンスに含めます。|
||ignore_tag_open_flg|チェックを入れると非公開タグのコンテンツもレスポンスに含めます。|
||central_id|取得の中心にするIDを指定します。|
||add_open_ymdhi|チェックを入れると公開開始・終了日時をレスポンスに含めます。|
||ignore_restrict_flg|チェックを入れるとアクセス制限を無視します。|
||use_pre_embedding_text|チェックを入れると事前に生成されたembeddingテキストを使用します。|
||max_list_chars|一覧表示時の最大文字数を指定します。0の場合は制限なし。|

#### details
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|topics_group_id|対象にするコンテンツ定義IDを指定します。|
||contents_type|表示するカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||filter|データを絞り込むクエリパラメータです。詳しくは[検索機能の使い方](/ja/docs/reference/filter-query/)を参照してください。|
||filter_lang|フィルターの言語を指定します。|
||filter_request_allow_list|filterリクエストに指定可能な項目を指定します。指定が無い場合はクエリによるフィルタはできません。全項目を許可したい場合は`:ALL`を設定してください。|
||cnt|1ページの表示件数を指定します。|
||order_query|並び順を指定します。<br/>例）`topics_id:asc`、`topics_id:desc` <br/>指定可能な項目： topics_id, order_no, ymd, post_time, contents_type, subject, regular_flg, inst_ymdhi, update_ymdhi, topics_group_id, favorite_cnt, comment_cnt|
||ec_ext_options_search|商品一覧を拡張項目のオプションで絞り込むか指定します。指定する:1 指定しない:0|
||my_order_flg|自分が購入した商品を表示する。|
||ignore_product_open_flg|非公開商品を表示する。|
|詳細設定|category_parent_id|親カテゴリで絞り込む。絞り込む親カテゴリを指定します。|
||exclude_category_parent_id|表示しないカテゴリIDを指定します。|
||ext_column|拡張項目の値で一覧を絞り込む。 例 指定した値で絞り込む場合）ext_column=ext_col_02:15 例 指定した値以外で絞り込む場合) ext_column=ext_col_02!:15|
||ymd_sort_change|コンテンツの並び順を日付の昇順に変更したい場合、`ymd_sort_change=on`を入力します。（デフォルトは降順です。）|
||shuffle|ランダム表示にするかどうか(yes/no) 通常はランダムではありません。|
||target_col_for_keyword|キーワード検索の対象カラムを指定します。 設定がない場合はタイトル、本文、カテゴリ、拡張項目が対象になります。 補足) subject,contents,contents_typeまたは拡張項目no(ext_col_01,ext_col_10など)を設定します。|
||use_target_col_for_keyword_from_request|リクエストでキーワード検索の対象項目の絞り込むを利用する。|
||topics_keyword_cond|キーワード検索のキーワード毎の絞り込み方を変える。（デフォルト：AND)|
||full_text_search_cond|全文検索のキーワード毎の絞り込み方を変えます。選択可能値: `AND`, `OR`|
||tag_category_id|表示対象になるタグカテゴリIDを指定します。設定がない場合はすべてのカテゴリが対象になります。|
||exclude_tag_category_id|表示対象から除外するタグカテゴリIDを指定します。|
||tag_id|表示対象になるタグIDを指定します。|
||exclude_tag_id|表示対象から除外するタグIDを指定します。|
||tag_cond|タグの絞り込み方を変える（デフォルト：OR)|
||topics_id|表示するコンテンツIDを設定します。|
||order_by_id|topics_idで並び順を指定できます。指定したtopics_idのデータが上位表示されます。|
||exclude_topics_id|除外するコンテンツIDを指定します。|
||get_comment_cnt|コメント数を取得する。|
||get_unlisted_data|一覧に載せないデータも取得する。|
||comment_cond_date|コメント数を取得する際の日付条件を設定する。（例：7日前の場合「-7 day」）|
||get_favorite_cnt|お気に入り数を取得する。|
||my_favorite_list|自分のお気に入りでコンテンツ絞り込む。|
||my_comment_list|自分のコメントしたコンテンツで絞り込む。|
||my_own_list|自分の所有コンテンツで絞り込む。|
||add_owner_info_cols|取得したいコンテンツ所有者属性を指定します。(複数可能) 例) email,nickname|
||required_param|必須にしたいクエリパラメータを指定します。|
||add_my_favorite_flg|チェックを入れると、エンドポイントを呼び出したユーザーが対象のコンテンツをお気に入り登録しているかがレスポンスに追加されます。<br/>お気に入り登録している=>"my_favorite_flg": true<br/>お気に入り登録していない=>"my_favorite_flg": false|
||only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|
||favorite_action_type|my_favorite_listを有効にした場合、お気に入りのアクションタイプを指定してさらに詳しく絞り込みます。|
||exclude_favorited_topics|お気に入り済みのデータを対象外とする。|
||get_tag_flg|チェックを入れるとレスポンスにタグ情報が追加されます。|
||get_tag_order_by_tag_category|get_tag_flgが有効な場合にチェックを入れると、カテゴリ毎にタグを並べます。|
||ignore_open_flg|チェックを入れると非公開コンテンツをレスポンスに含めます。|
||ignore_category_open_flg|チェックを入れると非公開カテゴリのコンテンツもレスポンスに含めます。|
||ignore_tag_open_flg|チェックを入れると非公開タグのコンテンツもレスポンスに含めます。|
||central_id|取得の中心にするIDを指定します。|
||add_open_ymdhi|チェックを入れると公開開始・終了日時をレスポンスに含めます。|
||ignore_restrict_flg|チェックを入れるとアクセス制限を無視します。|
||use_pre_embedding_text|チェックを入れると事前に生成されたembeddingテキストを使用します。|
||max_list_chars|一覧表示時の最大文字数を指定します。0の場合は制限なし。|

### ECPayment
#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### details
設定できるパラメータなし。

## Payments
### Stripe
#### checkout
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|products_list|StripeのPrice ID。同じPrice IDが複数ある場合は、それに応じて課金されます。|
||return_url|決済成功時のURLを設定します。|
||return_err_url|決済失敗時のURLを設定します。|
||trial_end|( 定期購入 ) 試用終了時期を設定します。|
||trial_period_days|( 定期購入 ) 試用期間の日数を指定します。|

#### cancel_order
設定できるパラメータなし。

## Site
### Site
#### update_site
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|use_columns|更新対象のカラムを指定します。|

#### list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|only_count|パフォーマンス向上のため検索結果データを含まない結果件数のみを返します。|

#### create_backup
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_id|対象にするサイトIDを指定します。|

#### get_backup_list
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_id|対象にするサイトIDを指定します。|

#### generate_backup_download_url
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_id|対象にするサイトIDを指定します。|

#### delete_backup
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_id|対象にするサイトIDを指定します。|

#### get_env_edit_data
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_id|対象にするサイトIDを指定します。|

#### add_site
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|copy_from_site_key|コピー元のサイトキーを指定します。|
||callback_batch_nm|コールバックバッチ名を指定します。|
||init_batch_nm|初期化バッチ名を指定します。|
||sign_up_as_superuser|スーパーユーザーによるサインアップをする。(する:1、しない:0)|
||release_level|リリースレベルを選択します。(RC版:20、RC版:90、正式版:100)|
|詳細設定|use_recaptcha|reCAPTCHAを使用する。|

#### update_env_info
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|site_id|対象にするサイトIDを指定します。|
||use_columns|更新対象のカラムを指定します。|

#### close_site
設定できるパラメータなし。

#### sync_sites
設定できるパラメータなし。

#### backup_site
設定できるパラメータなし。

#### sync_topics
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|topics_sync_source_site_id|同期元のサイトIDを指定します。|
||topics_sync_target_site_id|同期先のサイトIDを指定します。|
||topics_sync_group|同期対象のコンテンツ定義IDを指定します。|

#### get_mng_data
設定できるパラメータなし。

#### update_mng
|項目 |パラメータ |説明 |
| :--- | :--- | :--- |
|基本設定|use_columns|更新対象のカラムを指定します。|

## 関連ドキュメント
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [API](/ja/docs/management/api-list/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント設定後の注意点](/ja/docs/tutorials/points-to-note-after-endpoint-configuration/)
- [エンドポイントに送るパラメータについて、フロントエンドからクエリでリクエストするのと、Kurocoの管理画面で設定するのとで違いがありますか？](/ja/docs/faq/what-is-the-difference-between-requesting-endpoint-parameters-via-a-query-and-setting-them-in-kuroco-admin-panel/)


---

# エンドポイント 設定項目一覧

> 元ページ: `reference/endpoint-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/endpoint-settings/

[API](/ja/docs/management/api-list/)画面では、APIエンドポイントの追加/更新ができます。  
クライアントがKurocoのデータにアクセスするには、対象のリソースを操作するためのエンドポイントを設定する必要があります。

ここでは、エンドポイントの全般設定項目と、利用できるエンドポイントのモデル一覧について説明します。  
各エンドポイントの基本設定・詳細設定で利用できるパラメータについては、[エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)を参照してください。

## エンドポイントの作成画面
[新しいエンドポイントの追加]をクリックすると、エンドポイントを新規作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/124bd97df0fdc6857d4a30d01fddbb55.png)

### 全般
<a><img src="https://t.gyazo.com/teams/diverta/02855cbbd800d453ab2edcf21753e5a9.png" style={{ width: 400, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/d75aaa2f1a45864e42b6b3ae9294a799.png" style={{ width: 400, maxHeight: 'none' }} /></a>


|項目   |説明  |
| :--- | :--- |
|パス|先頭の /rcms_api/xxx/ の部分は変更不可です。`/rcms_api/{api_id}/`の形式で固定値が設定されます。<br/>基本的にはモデル+動作など、使用方法に応じたパスを命名してください。<br/>例: `login`, `content/news`, `member/insert`|
|モデル|各カテゴリ/モデル/オペレーションの詳細な説明は、[エンドポイントで設定可能なカテゴリー一覧](#エンドポイントで設定可能なカテゴリー一覧)に記載します。<br/>モデル名の横に表示しているプルダウンの「v1」等の値は、各APIモデルのバージョン名を示します。|
|サマリー|APIの概要を記載してください。<br/>記載した内容はエンドポイント一覧/Swagger UIに表示されます。|
|説明|必要に応じてAPIの使用方法など、詳細な説明を記載してください。<br/>ここでは[CommonMark](https://commonmark.org/help/)の記法を利用することができます。<br/>記述した内容は、Swagger UI画面の各エンドポイントにも表示されます。|
|APIリクエスト制限|下記3種類より選択できます。<ul><li>None</li><li>GroupAuth</li><li>MemberCustomSearchAuth</li></ul>GroupAuthもしくはMemberCustomSearchAuthを選択すると、APIの使用時にログインユーザーの権限をチェックし、合致した場合にのみリクエストを許可します。|
|キャッシュ|APIレスポンスをキャッシュする期間を秒単位で設定します。<br/>Kurocoでは従量課金で費用がかかるため、メディアサイトなど多量のリクエストが見込まれる用途でご利用される場合は、設定することを推奨します。<br/>キャッシュ期間は1日・1週間等をお勧めしております。<br/>コンテンツ・メンバー等、取得対象のデータに更新があった場合、キャッシュは自動的にクリアされます。|
|Stale-While-Revalidate|APIのキャッシュにstale-while-revalidate（秒）を付与します。高頻度のアクセスがあるAPIの場合に設定すると、APIパフォーマンス向上に効果があります。（例: 86400）<br/>キャッシュ期間を設定している場合に表示されます。|
|Stale-If-Error|APIのキャッシュ再取得中にエラーが発生した場合、エラーを出力する代わりに古いレスポンスを返す期限（秒）を設定できます。（例: 600）<br/>キャッシュ期間を設定している場合に表示されます。|
|キャッシュ単位|[グループの組み合わせ単位でキャッシュする]を有効にすると、キャッシュの単位を「ログインセッション単位」から「リクエスト会員の所属グループの組み合わせ単位」に切り替えます。同じグループ構成の会員間でCDNキャッシュを共有でき、ヒット率が向上します。<br/>この設定はキャッシュ期間を設定している場合に有効です。<br/>以下の条件をすべて満たすエンドポイントでのみ表示されます。<ul><li>モデルが Topics、オペレーションが list または details であること</li><li>認証方式が動的アクセストークンまたはCookieであること</li><li>APIリクエスト制限が None または GroupAuth であること（MemberCustomSearchAuth では表示されません）</li></ul>|
|流量制限|最大3600秒内で許可するリクエスト数をセットできます。制限を超えた場合は 429 Too Many Requests をレスポンスします。<br/>流量制限の状況はレスポンスヘッダーで確認可能です。<ul><li>制限数：x-rcms-ratelimit-limit:xxx</li><li>残りのリクエスト可能数：x-rcms-ratelimit-remaining:yyy</li><li>リセットされるまでの残り時間：x-rcms-ratelimit-reset: zzz</li></ul>|

## エンドポイントで設定可能なカテゴリー一覧

カテゴリー一覧を説明します。

![Image from Gyazo](https://i.gyazo.com/46507bd4655be0b3dba433a6d489704b.png)
### 認証
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Login|login_challenge|ログイン|
||login_challenge_mfa|2要素認証（MFA）のワンタイムパスワードでのログイン|
||token|アクセストークンの取得|
||file_access_token|ファイルアクセス用のアクセストークンを取得|
||alias_login|代理ログイン（別のメンバーとしてログイン）|
||logout|ログアウト|
||reminder|パスワード再設定メールの送信・パスワードの再設定<br/>(現在のパスワードを忘れた場合に利用)|
||reset_password|パスワードの変更<br/>(現在のパスワードを覚えている場合に利用)|
||profile|ログインユーザーの情報を取得|
||gcs_info|サイトと連携したGCS(Cloud Storage for Firebase)の情報を取得|
||firebaseToken|サイトと連携したFirebaseの認証トークンを取得|
|LoginHistory|list|ログイン履歴を取得|
|LoginFailed|list|ログイン失敗履歴の一覧を取得|
|TwofactorMethod|reserve|2要素認証用のシークレットキーを生成（仮登録）|
||regist|2要素認証の登録を確定|
||reminder|2要素認証のリセット用コードを送信|
||reset|2要素認証の設定をリセット|
||delete|2要素認証の設定を削除|

### コンテンツ
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Topics|list|コンテンツ一覧の取得|
||details|コンテンツ詳細の取得|
||preview|コンテンツのプレビューを取得|
||insert|コンテンツの新規追加|
||update|コンテンツの更新|
||delete|コンテンツの削除|
||draft_list|途中保存一覧の取得|
||draft_details|途中保存詳細の取得|
||draft_save|途中保存の新規追加|
||draft_delete|途中保存の削除|
||draft_update|途中保存の更新|
||waiting_for_approval_list|承認ワークフロー申請中データの一覧を取得|
||waiting_for_approval_details|承認ワークフロー申請中データの詳細を取得|
||history_list|コンテンツの変更履歴一覧を取得|
||accept|コンテンツのワークフローの承認|
||reject|コンテンツのワークフローの差し戻し|
||bulk_upsert|コンテンツをバッチで更新|
||bulk_download|コンテンツをバッチでダウンロード|
||increment|コンテンツに設定したカウンターの項目の値を増減|
|TopicsCategory|list|カテゴリ一覧の取得|
|TopicsGroup|list|コンテンツ定義の一覧を取得|
||details|コンテンツ定義の詳細を取得|
||insert|コンテンツ定義の新規追加|

### テーブル
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Master|list|マスタ一覧の取得|
||insert|マスタの新規追加|
||update|マスタの更新|
||delete|マスタの削除|

### タグ
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Tag|list|タグ一覧の取得|
||insert|タグの新規追加|
||update|タグの更新|
||delete|タグの削除|
|TagCategory|list|タグカテゴリ一覧の取得|

### ファイル
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Files|upload|ファイルのアップロード|
||create_temp_upload_url|HTTP PUTでファイルを直接S3にアップロードするための一時URLを取得。リクエストボディで`file_size`・`ext`の申告が必須です。 |
||create_temp_upload_post|S3のpresigned POSTでファイルを直接アップロードするための情報を取得。リクエストボディで`file_size`・`ext`の申告が必須です。 |
||temp_upload_url|【非推奨】HTTP PUTでファイルを直接S3にアップロードするための一時URLを取得|
|FileManager|upload|ファイルマネージャーへのファイルのアップロード|
||delete|ファイルマネージャーのファイルまたはディレクトリの削除|
||list|ファイルマネージャーのファイルおよびディレクトリ一覧の取得|

### API
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Api|bulk|APIエンドポイントの一括実行|
||list|API一覧の取得|
||openapi_data|APIのopenapi.jsonを取得|
||request_api|カスタム処理で作成したAPIの実行 (GETメソッド)|
||request_api_post|カスタム処理で作成したAPIの実行 (POSTメソッド)|
||proxy|リクエストとレスポンスをプロキシ (GETメソッド)|
||proxy_post|リクエストとレスポンスをプロキシ (POSTメソッド)|
||aggregate|複数のリクエストとレスポンスをプロキシする。レスポンスは統合されて返される(GETメソッド)|
||add_site|Kurocoサイトの新規追加|
||site_list|Kurocoサイト一覧|
||sso_credentials|Kuroco site間でのSSOに必要な認証情報を提供します|

### API管理
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|ApiManagement|insert|APIの新規追加|
||update|APIの更新|

### AI
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|OpenAI|chat|OpenAIによる回答の生成。サイト設定でAI機能を有効にする必要があります。|
||rag_search|RAGを使ってコンテンツを検索し、OpenAIによる回答を生成。サイト設定でAI機能を有効にする必要があります。また、対象のコンテンツ構造でRAG（埋め込みモデル）が有効になっている必要があります。|
||chat_contents_search|登録されたコンテンツを参照して、OpenAIによる回答を生成。サイト設定でAI機能を有効にする必要があります。また、対象のコンテンツ構造でRAG（埋め込みモデル）が有効になっている必要があります。|
||routing_rules|AIルーターのルーティングルール設定を取得。サイト設定でAI機能を有効にする必要があります。|
|AiAgent|create_session|AIエージェントのセッションを作成。`ai_agent_id` で対象のAIエージェントを指定します。事前にAIエージェントの作成が必要です。|
||send_message|AIエージェントのセッションにメッセージを送信。`create_session` で取得した `ai_session_id` と `message` を指定します。セッションが処理中の場合は400が返るため、時間をおいて再試行してください。|

### WEB
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|InquiryMessage|list|フォーム回答済み情報の一覧を取得|
||details|フォーム回答情報の詳細を取得|
||send|フォーム回答情報を送信|
||update|フォーム回答情報を更新|
||delete|フォーム回答情報を削除|
||bulk_upsert|フォーム回答をバッチで更新|
|InquiryForm|list|フォーム一覧の取得|
||details|フォームの詳細を取得|
||insert|フォームの新規追加|
||update|フォームの更新|
||delete|フォームの削除|
||report|フォームの回答レポートを取得|
|KurocoFront|deploy|アーティファクトURLからKuroco Frontへデプロイ|
|SpiderHistory|list|WEBクローラー実行履歴一覧の取得。Spider機能はサイト設定でAI機能を有効にすると利用可能になります。|
||details|WEBクローラー実行詳細の取得|
||logs|WEBクローラー実行ログの取得|
|Spider|insert|WEBクローラー設定の新規作成|
||update|WEBクローラー設定の更新|
||webhook|WEBクローラー処理の実行|

### メール
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Email|send|メールの送信|

### メッセージング
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Line|send|LINEメッセージの送信。サイト設定でLINE連携を有効にする必要があります。|
|Teams|send|Microsoft Teamsへのメッセージ送信。サイト設定でMicrosoft Teams連携を有効にする必要があります。|
|Slack|send|Slackへのメッセージ送信。サイト設定でSlack連携を有効にする必要があります。|
||get|Slackのメッセージを取得。サイト設定でSlack連携を有効にする必要があります。|

### 一括配信
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|MagazineInfo|list|配信一覧の取得|
|MagazineSubscriber|list|配信購読者一覧の取得|
||subscribe|購読者の登録|
||unsubscribe|購読者の削除|
|Magazine|send|配信の送信|
||delete|配信メッセージを削除|
||subscribe|購読者の登録<br/>**※Magazine::subscribe の使用は非推奨になります。代わりに、self_only パラメータまたは required_key パラメータを設定した MagazineSubscriber::subscribe を使用することを推奨します。**|
||unsubscribe|購読者の削除<br/>**※Magazine::unsubscribe の使用は非推奨になります。代わりに、self_only パラメータまたは required_key パラメータを設定した MagazineSubscriber::unsubscribe を使用することを推奨します。**|
||list|配信メッセージ一覧の取得|

### アクティビティ
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Comment|list|アクティビティ一覧の取得|
||insert|アクティビティの新規追加|
||update|アクティビティの更新|
||delete|アクティビティの削除|

### お気に入り
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Favorite|list|お気に入り一覧の取得|
||insert|お気に入りの新規追加|
||delete|お気に入りの削除|

### メンバー
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Member|list|メンバー一覧の取得|
||details|メンバー詳細の取得|
||invite|メンバーの招待|
||insert|メンバーの新規追加<br/>`allow_ec_point`を有効にすると`ec_point`（確定ポイント）を設定できます。参考：[ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)|
||update|メンバーの更新<br/>`allow_ec_point`を有効にすると`ec_point`（確定ポイント）を更新できます。参考：[ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)|
||delete|メンバーの削除|
||bulk_upsert|メンバーの一括追加・更新|
|MemberProvisional|list|仮メンバー一覧の取得|
||insert|仮メンバー一覧の新規追加|
||update|仮メンバー一覧の更新|
||delete|仮メンバー一覧の削除|
|MemberCustomSearch|list|メンバーカスタム検索条件の一覧を取得|
||details|メンバーカスタム検索条件の詳細を取得|
||insert|メンバーカスタム検索条件の新規追加|
||update|メンバーカスタム検索条件の更新|
||delete|メンバーカスタム検索条件の削除|
||identify|メンバー情報に合致するカスタム検索条件の取得|
|MemberForm|details|メンバー項目設定の詳細を取得|
|MemberGroup|list|グループの一覧を取得|

### 非同期タスク
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Batch|webhook|バッチ処理の呼び出し|
||list|バッチ処理一覧の取得|
||check_batch|バッチ処理ステータスの取得|

### 承認ワークフロー
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Approvalflow|list|承認ワークフロー一覧の取得|
||details|承認ワークフロー詳細の取得|
||insert|承認ワークフローの追加|
||update|承認ワークフロー基本設定の更新|
||update_flow_settings|承認ワークフローフロー設定の更新|
||delete|承認ワークフローの削除|
||review|指定したモジュールタイプの承認ワークフロー申請中データの承認・差し戻し<br/>対応中のモジュールタイプは以下<ul><li>コンテンツ</li></ul>**※Approvalflow::review の使用は非推奨になります。代わりに、Topics::accept/reject を使用することを推奨します。**|
||list_pending|指定したモジュールタイプの承認ワークフロー申請中データの一覧を取得<br/>対応中のモジュールタイプは以下<ul><li>コンテンツ</li></ul>**※Approvalflow::list_pending の使用は非推奨になります。代わりに、Topics::waiting_for_approval_list を使用することを推奨します。**|
||pending_detail|指定したモジュールタイプの承認ワークフロー申請中データの詳細を取得<br/>対応中のモジュールタイプは以下<ul><li>コンテンツ</li></ul>**※Approvalflow::pending_detail の使用は非推奨になります。代わりに、Topics::waiting_for_approval_details を使用することを推奨します。**|

### カスタム処理
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|CustomProcessing|list|カスタム処理一覧の取得|
||details|カスタム処理の詳細を取得|
||insert|カスタム処理の新規追加|
||update|カスタム処理の更新|
||delete|カスタム処理の削除|
||validate|カスタム処理のバリデーションとテスト実行|

### EC
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|ECOrderSubscription|list|継続注文情報の一覧を取得|
||details|継続注文情報の詳細を取得|
||insert|継続注文情報を追加|
||auth_sp_career|キャリア決済のユーザー認証|
|ECOrder|list|注文情報の一覧を取得|
||details|注文情報の詳細を取得|
||total|注文の総計を取得|
||purchase|商品の購入|
||cancel|注文のキャンセル|
||insert|注文情報の新規追加|
||auth_sp_career|キャリア決済のユーザー認証|
|ECDelivery|list|配送情報の一覧を取得|
||details|配送情報の詳細を取得|
|ECCart|details|カート詳細を取得|
||add|カートに商品を追加|
||update|カート内の商品を更新|
|ECShop|list|ショップ一覧を取得|
||details|ショップ詳細を取得|
|ECProduct|list|商品一覧を取得|
||details|商品詳細を取得|
|ECPayment|list|支払い方法の一覧を取得|
||details|支払い方法の詳細を取得|
|ECPoint|update|メンバーのポイントを更新（付与・消費）<br/>参考：[ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)|
||history|メンバーのポイント履歴と残高を取得<br/>参考：[ECポイントの仕様とポイント更新・履歴取得API](/ja/docs/reference/ec-point/)|

### Payments
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Stripe|checkout|サブスクリプションの支払いURL作成|
||cancel_order|サブスクリプションの解除|

### Site
|モデル   |オペレーション   |説明  |
| :--- | :--- | :--- |
|Site|update_site|サイト設定の更新|
||list|サイト一覧の取得|
||create_backup|バックアップの作成|
||get_backup_list|バックアップ一覧の取得|
||generate_backup_download_url|バックアップのダウンロードURLを生成|
||delete_backup|バックアップの削除|
||get_env_edit_data|サイト設定の詳細を取得|
||add_site|Kurocoサイトの新規追加|
||update_env_info|サイト設定情報の更新|
||close_sites|複数サイトを一括クローズ|
||sync_sites|複数サイトを一括同期|
||backup_sites|複数サイトを一括バックアップ|
||sync_topics|サイト間でコンテンツを同期|
||get_mng_data|管理設定情報の取得|
||update_mng|管理設定情報の更新|

## 関連ドキュメント
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [API](/ja/docs/management/api-list/)
- [API セキュリティ](/ja/docs/management/api-security/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント設定後の注意点](/ja/docs/tutorials/points-to-note-after-endpoint-configuration/)
- [APIのキャッシュについて](/ja/docs/reference/api-cache/)
