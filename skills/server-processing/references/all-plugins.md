# 全Smartyプラグイン一覧

Kurocoで使用可能な全151個のSmartyプラグインのアルファベット順索引です。

## カテゴリ別リファレンス

| カテゴリ | ファイル |
|---------|----------|
| API・データ取得プラグイン | [api-plugins.md](./api-plugins.md) |
| 文字列処理プラグイン | [string-plugins.md](./string-plugins.md) |
| 配列操作プラグイン | [array-plugins.md](./array-plugins.md) |
| フォーム・UIプラグイン | [form-plugins.md](./form-plugins.md) |
| 認証・セキュリティプラグイン | [auth-plugins.md](./auth-plugins.md) |
| 外部サービス連携プラグイン | [integration-plugins.md](./integration-plugins.md) |
| ファイル操作プラグイン | [file-plugins.md](./file-plugins.md) |
| Vue.js・テンプレート連携プラグイン | [vue-plugins.md](./vue-plugins.md) |

---

## プラグイン一覧（アルファベット順）

### A

| プラグイン | 説明 |
|-----------|------|
| add | 変数に数値を加算します。 |
| ai_completion | OpenAIを使用したAI補完（チャット）を行います。 |
| ai_embeddings | OpenAIを使用してテキストのAI埋め込み（Embeddings）を作成・保存... |
| api | 外部APIをリクエストして、応答をassignします。 |
| api_internal | 内部API（同じKurocoサイト内）をリクエストします。 |
| api_method | エンドポイントを作成せずにAPIメソッドを直接実行します。 |
| api_mng | 管理APIを内部的にリクエストします。 |
| api_token | APIトークン（静的または動的）を取得します。 |
| array_key_exists | Checks if a key exists in an array. This... |
| assign | Assign a value to a template variable at... |
| assign_api_credential | API認証情報（署名、セッションID、JWT等）を生成します。 |
| assign_array | 配列をテンプレート変数に代入します。 |
| assign_array_diff | 2つの配列の差分を取得します。 |
| assign_array_get | 配列からキーで値を取得します。 |
| assign_array_intersect | 2つの配列の共通部分を取得します。 |
| assign_array_pick | 配列から特定のキーを抽出します。 |
| assign_array_set | 配列に値を設定します。 |
| assign_array_unset | 配列からキーを削除します。 |
| assign_favorite_cnt | Get the total number of favorites (likes... |
| assign_group_nm | Retrieve the display name of a member gr... |
| assign_my_favorite_cnt | Get the current user's favorite count fo... |
| assign_new_comment_list | Retrieve the most recent comments for a ... |
| assign_pager | 配列をページ分割し、そのページ分のデータとページ情報を代入します。 |
| assign_relation_tag_list | Retrieve tags associated with a specific... |
| assign_session | セッションに値を代入します。 |
| assign_tag_category_list | Retrieve the list of tag categories for ... |
| assign_tag_list | Retrieve tags belonging to a specific ta... |
| assign_topics_category_list | Retrieve categories for a topics group w... |

### B

| プラグイン | 説明 |
|-----------|------|
| backup | バックアップジョブを開始します。 |
| backup_delete | バックアップを削除します。 |
| batch | バッチ処理を登録・実行します。 |

### C

| プラグイン | 説明 |
|-----------|------|
| capitalize | Capitalize first letter of each word. |
| cat | Concatenate a value to a variable. |
| conv_bool | Converts a value to a boolean using the ... |
| copy_s3_temp_file | files-temp_upload_urlでS3TEMPBUCKETにアップロー... |
| count | Counts the number of elements in an arra... |
| count_characters | Count number of characters in text. |
| count_paragraphs | Count number of paragraphs in text. |
| count_sentences | Count number of sentences in text. |
| count_words | Count number of words in text. |

### D

| プラグイン | 説明 |
|-----------|------|
| date | Generate and assign a formatted date str... |
| date_format | Format datestamps using PHP date() forma... |
| debug | Output debug console showing template va... |
| debug_print_var | Format variable contents for display in ... |
| default | Provide default value for empty variable... |
| detect_document_text | PDF/TIFFファイルからテキストを検出（OCR）します。 |

### E

| プラグイン | 説明 |
|-----------|------|
| empty | Checks whether a value is empty, with en... |
| escape | Escape string according to specified typ... |
| explode | Splits a string into an array using a de... |

### F

| プラグイン | 説明 |
|-----------|------|
| fileupload | File upload component supporting both S3... |
| function | 静的コンテンツで定義されたSmarty関数を実行します。 |

### G

| プラグイン | 説明 |
|-----------|------|
| gcloud_functions_token | Google Cloud Functionsトークンを取得します。 |
| gcloud_pubsub_publish | Google Cloud Pub/Subにメッセージを発行します。 |
| generate_pdf | URLからPDFを生成し、クラウドストレージに保存します。 |
| get_file | ファイルを取得します。 |
| github_deploy | GitHubデプロイを実行します。 |
| googleanalytics | Google Analyticsからデータを取得し、Topicsのカウンター拡張... |

### H

| プラグイン | 説明 |
|-----------|------|
| head_include | Queue a template file to be included in ... |
| html5_check | HTML5チェックを行います。 |

### I

| プラグイン | 説明 |
|-----------|------|
| implode | Joins array elements into a string using... |
| in_array | Checks if a value exists in an array. PH... |
| include | テンプレートをインクルードします。 |
| indent | Indent lines of text. |
| inquiry_input | Replace placeholder comments in content ... |

### J

| プラグイン | 説明 |
|-----------|------|
| join | Joins array elements into a string using... |
| json_decode | Decodes a JSON string into a PHP value. |

### L

| プラグイン | 説明 |
|-----------|------|
| lower | Convert string to lowercase. |

### M

| プラグイン | 説明 |
|-----------|------|
| make_pdf_thumb | PDFのサムネイルを作成します。 |
| math | Perform mathematical calculations in tem... |
| mb_truncate | Truncate string to specified length (mul... |
| mbtruncate | マルチバイト文字対応で文字列を切り詰めます。内部的に `rcms_mbtrunc... |
| msgpack_pack | データをMessagePack形式バイナリに変換します。 |
| msgpack_unpack | MessagePackエンコードされたデータをPHPの値に復元します。 |

### N

| プラグイン | 説明 |
|-----------|------|
| nl2br | Convert newlines to HTML `<br>` tags. |

### P

| プラグイン | 説明 |
|-----------|------|
| pager | Generate pagination navigation links for... |
| pg_dateformat | Format a PostgreSQL date. |
| pg_dateformat2 | Format a PostgreSQL date (alternative ve... |
| property_exists | オブジェクトまたはクラスにプロパティが存在するかチェックします。 |
| purge_cdn_cache | CDNおよびイメージCDNのキャッシュをパージ（削除）します。 |
| put_file | ファイルをクラウドストレージまたはKurocoFilesにアップロードします。 |
| put_file_zip | ファイルをZip圧縮してアップロードする |

### R

| プラグイン | 説明 |
|-----------|------|
| raw | Output without escaping. |
| rcms_arsort | Sort an array by values in descending or... |
| rcms_asort | Sort an array by values in ascending ord... |
| rcms_auth | Show or hide content based on user resou... |
| rcms_encrypt | データの暗号化および復号を行います。 |
| rcms_file_exists | Check if a file exists at the specified ... |
| rcms_file_mtime | Get the last modification time of a file... |
| rcms_file_size | Get the file size. |
| rcms_hash | ハッシュを生成します。 |
| rcms_in_array | Check if a value exists in an array. |
| rcms_json_encode | 値をUnicodeサポート付きでJSON形式にエンコードし、RCMSコンテンツ境... |
| rcms_krsort | Sort an array by key in reverse order. |
| rcms_ksort | Sort an array by key. |
| rcms_match | 正規表現マッチング（preg_match）を行います。 |
| rcms_match_all | 正規表現で全マッチを取得します（preg_match_all）。 |
| rcms_number_format | Format a number (extended version). |
| rcms_pathinfo | Get path information. |
| rcms_replace | Replace a string using regular expressio... |
| rcms_rsort | Sort an array in reverse order. |
| rcms_sort | Sort an array. |
| rcms_sort_by_key | Sort an array of associative arrays by a... |
| rcms_strip_tags | Remove HTML tags from a string. |
| rcms_vue_component | Load and mount a Vue.js component within... |
| read_dir | KurocoFiles内のディレクトリを読み込み、ファイルリストを繰り返し処理し... |
| read_file | ファイルを1行ずつ読み込み、各行を繰り返し処理します。 |
| refresh_cs | メンバーカスタム検索（MemberCustomSearch）のセッション情報をリ... |
| regex_replace | Search and replace using regular express... |
| remove_dir | ディレクトリを削除します。 |
| remove_file | ファイルを削除します。 |
| rename_file | S3/GCS上のファイルを移動（リネーム）します。 |
| replace | Simple string search and replace. |
| return | テンプレートのコンパイル時に 'return' 文を生成します。オプションで値を... |

### S

| プラグイン | 説明 |
|-----------|------|
| save_file | 一時ファイルとしてコンテンツを保存します。 |
| secret | シークレット値を取得します。 |
| sendmail | メールを送信します。 |
| set_memory | PHPのメモリ制限を増加させます。 |
| site_sync | マルチサイト環境でサイト間の同期ジョブをキックします。 |
| slack_get_message | Slackから特定のメッセージを取得します。 |
| slack_post_message | Slackにメッセージを投稿します。 |
| slack_team_info | Slackのチーム情報を取得します。 |
| sleep | 指定されたミリ秒数だけ実行を一時停止します。 |
| sort_name | サイトの言語設定に基づいて姓名を適切な順序でフォーマットします。 |
| spacify | Add spaces (or custom string) between ea... |
| split | 区切り文字を使用して文字列を配列に分割します。正規表現とリテラル区切り文字の両方... |
| storage_url | クラウドストレージ上のファイルへの署名付きURLを取得します。 |
| string_format | Format string using sprintf. |
| strip | Replace all repeated whitespace with a s... |
| strip_tags | Remove HTML tags from text. |
| strtodate | タイムスタンプまたは日付文字列をフォーマットして日付を取得します。 |
| strtolower | Convert string to lowercase (with type c... |
| strtoupper | Convert string to uppercase (with type c... |
| substr | Return substring from input string (with... |
| subtract | 変数から数値を減算します。 |
| sync_counter | コンテンツのカウンター値を同期します。 |

### T

| プラグイン | 説明 |
|-----------|------|
| teams_post_message | Microsoft Teamsにメッセージを投稿します。 |
| to_form_options | 連想配列をフォームセレクト/オプション要素に適した形式に変換します。 |
| to_object | 配列をstdClassオブジェクトに変換します。 |
| translate | Translate a string. |
| truncate | Truncate string to specified length (byt... |
| twitter_post_message | Twitter（X）にツイートを投稿します。 |

### U

| プラグイン | 説明 |
|-----------|------|
| unzip | ZIPファイルを解凍してクラウドストレージにアップロードします。 |
| update_counter | コンテンツのカウンター項目を指定した値に更新します。 |
| upper | Convert string to uppercase. |
| usage_price_format | RCMS_Usageフォーマットシステムを使用して使用量/価格値を表示用にフォー... |
| uuid | UUIDを生成します。 |

### V

| プラグイン | 説明 |
|-----------|------|
| var | Fetch template content from a global PHP... |

### W

| プラグイン | 説明 |
|-----------|------|
| wordwrap | Wrap text to specified line length. |
| write_file | ファイルにデータを書き込みます（一時ファイルまたは指定パス）。 |

### X

| プラグイン | 説明 |
|-----------|------|
| xmltojson | XMLをJSONに変換します。 |

### Z

| プラグイン | 説明 |
|-----------|------|
| zip | クラウドファイルをZIP圧縮してクラウドストレージにアップロードします。 |

