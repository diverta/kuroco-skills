# ファイル操作プラグイン

## 目次

- [write_file](#write_file) - ファイルにデータを書き込みます（一時ファイルまたは指定パス）...
- [read_file](#read_file) - ファイルを1行ずつ読み込み、各行を繰り返し処理します。
- [read_dir](#read_dir) - KurocoFiles内のディレクトリを読み込み、ファイルリ...
- [put_file](#put_file) - ファイルをクラウドストレージまたはKurocoFilesにア...
- [get_file](#get_file) - ファイルを取得します。
- [save_file](#save_file) - 一時ファイルとしてコンテンツを保存します。
- [remove_file](#remove_file) - ファイルを削除します。
- [remove_dir](#remove_dir) - ディレクトリを削除します。
- [rename_file](#rename_file) - S3/GCS上のファイルを移動（リネーム）します。
- [zip](#zip) - クラウドファイルをZIP圧縮してクラウドストレージにアップロ...
- [unzip](#unzip) - ZIPファイルを解凍してクラウドストレージにアップロードしま...
- [storage_url](#storage_url) - クラウドストレージ上のファイルへの署名付きURLを取得します...
- [rcms_file_exists](#rcms_file_exists) - Check if a file exists at the ...
- [rcms_file_mtime](#rcms_file_mtime) - Get the last modification time...
- [rcms_file_size](#rcms_file_size) - Get the file size.
- [generate_pdf](#generate_pdf) - URLからPDFを生成し、クラウドストレージに保存します。
- [make_pdf_thumb](#make_pdf_thumb) - PDFのサムネイルを作成します。
- [detect_document_text](#detect_document_text) - PDF/TIFFファイルからテキストを検出（OCR）します。

---

## write_file

ファイルにデータを書き込みます（一時ファイルまたは指定パス）。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Conditional | - | 書き込んだファイルパスを格納する変数名（新規作成時は必須） |

### Return Value

`var` パラメータで指定した変数にファイルパスが代入されます。`status_var` パラメータを指定した場合、書き込みの成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{* 新規一時ファイルに書き込み *}
{write_file var=path value="Hello World"}
{* 指定パスに書き込み *}
{write_file path="myfile.txt" value="Content here"}
{* ファイルに追記 *}
{write_file path=$existing_path value="New line" is_append=1}
{* 配列をCSV形式で書き込み *}
{write_file var=csv_path value=$row_array encoding="UTF-8"}
{* 結果を取得 *}
{write_file var=path value="Hello World" status_var="result"}
{if $result}
    <p>書き込み成功</p>
{else}
    <p>書き込み失敗</p>
{/if}
```

### Notes

- 新規作成時で `path` が未指定の場合、`var` パラメータは必須です。追記モード時は `path` が必須です。`value` が配列の場合、CSV形式の文字列に変換されます。

---

## read_file

ファイルを1行ずつ読み込み、各行を繰り返し処理します。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

各行が `row` 変数に代入されて繰り返されます。`txt` タイプは文字列、`csv` タイプは配列（`fgetcsv()` でパース）、`jsonl` タイプは配列/オブジェクト（JSONデコード）。

### Usage Example

```smarty
{* テキストファイルを読み込み *}
{read_file name="log" path='/files/user/data.txt' row="line"}
    {$line|escape}
{/read_file}
{* CSVファイルを読み込み *}
{read_file name="csv" path='/files/user/data.csv' row="row" type="csv"}
    {$row[0]} - {$row[1]} - {$row[2]}
{/read_file}
{* JSON Linesファイルを読み込み *}
{read_file name="jsonl" path='/files/user/data.jsonl' row="item" type="jsonl"}
    {$item.name}: {$item.value}
{/read_file}
```

### Notes

- 最大10万行まで読み込み（無限ループ防止）。NULL文字を含むバイナリファイルは拒否されます。`name` パラメータは一意である必要があります。

---

## read_dir

KurocoFiles内のディレクトリを読み込み、ファイルリストを繰り返し処理します。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

各ファイル/ディレクトリが `file_var` 変数に代入されて繰り返されます。`name_only=false`（デフォルト）の場合は `path`、`size`、`ctime`、`mtime`、`is_dir` を含む連想配列。`name_only=true` の場合は相対パス文字列のみ。

### Usage Example

```smarty
{* 基本的なディレクトリリスト *}
{read_dir name="files" file_var='file' path='/files/user/uploads'}
    {$file.path} - {$file.size} bytes
{/read_dir}
{* ファイルタイプフィルタ付き再帰リスト *}
{read_dir name="images" file_var='f' path='/files/user/images' recursive=true type='file'}
    <img src="{$f.path}" />
{/read_dir}
{* 正規表現パターンでフィルタ *}
{read_dir name="pdfs" file_var='doc' path='/files/user/docs' pattern='/\.pdf$/i'}
    <a href="{$doc.path}">{$doc.path}</a>
{/read_dir}
```

### Notes

- `/files/user` または `/files/ltd` 配下のパスのみ許可されます（`is_public_file()` で検証）。`name` パラメータは一意である必要があります。隠しファイル/フォルダは自動的にフィルタされます。

---

## put_file

ファイルをクラウドストレージまたはKurocoFilesにアップロードします。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

`status_var` パラメータを指定した場合、アップロードの成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{* 一時ファイルをアップロード *}
{put_file tmp_path=$tmp_path path="/files/user/uploaded.txt"}
{* 直接コンテンツを書き込み *}
{put_file value="File content here" path="/files/user/new_file.txt"}
{* KurocoFilesから別の場所にコピー *}
{put_file files_path="/files/user/source.txt" path="/files/ltd/dest.txt"}
{* 外部S3バケットにアップロード *}
{put_file tmp_path=$tmp_path path="/custom/path/file.txt" bucket="my-custom-bucket"}
{* クラウドストレージパスにアップロード *}
{put_file value=$content path="/files/g/private/data.json"}
{* 結果を取得 *}
{put_file tmp_path=$tmp_path path="/files/user/uploaded.txt" status_var="result"}
{if $result}
    <p>アップロード成功</p>
{else}
    <p>アップロード失敗</p>
{/if}
```

### Notes

- `tmp_path` と `files_path` は同時に指定できません（エラーになります）。アップロード先として許可されているパス: クラウドストレージパス（`isCloudFilePath()` でチェック）、`/files/user/` 以下、`/files/temp/` 以下、`/files/ltd/` 以下。バリデーションモード（`_rcms_validate`）の場合、実際のアップロードは実行されません。
- KurocoFilesへのアップロード時、ソースファイルの内容が空の場合は書き込みを行わず、`status_var` には false が代入されます。

---

## get_file

ファイルを取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | 結果変数 |

### Return Value

`var`パラメータで指定した変数にファイル内容が代入されます。`status_var` パラメータを指定した場合、取得の成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{get_file path="/files/user/data.txt" var="content"}
{* 結果を取得 *}
{get_file path="/files/user/data.txt" var="content" status_var="result"}
{if $result}
    <p>取得成功</p>
{else}
    <p>取得失敗</p>
{/if}
```

### Notes

- KurocoFilesまたはS3からファイルを取得します
- bucketパラメータで別のS3バケットを指定できます

---

## save_file

一時ファイルとしてコンテンツを保存します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 保存したファイルのパスを代入する変数名 |

### Return Value

`var` パラメータで指定した変数に、保存された一時ファイルのパス（TEMP_DIR2からの相対パス）が代入されます。`status_var` パラメータを指定した場合、保存の成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{save_file var="file_path" value="Hello, World!"}
<p>保存先: {$file_path}</p>
{* 変数の内容を保存 *}
{save_file var="csv_path" value=$csv_content}
{* 保存したファイルをS3にアップロード *}
{save_file var="temp_path" value=$file_content}
{put_file tmp_path=$temp_path path="/files/user/uploaded.txt"}
{* 結果を取得 *}
{save_file var="file_path" value="Hello, World!" status_var="result"}
{if $result}
    <p>保存成功: {$file_path}</p>
{else}
    <p>保存失敗</p>
{/if}
```

### Notes

- `var` パラメータは必須です（未指定の場合は何も実行されません）。ファイルは TEMP_DIR2 ディレクトリに一時ファイルとして保存されます。

---

## remove_file

ファイルを削除します。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

`status_var` パラメータを指定した場合、削除の成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{remove_file path="/files/user/old_data.txt"}
{* 結果を取得 *}
{remove_file path="/files/user/temp.txt" status_var="result"}
{if $result}
    <p>ファイルを削除しました</p>
{else}
    <p>削除に失敗しました</p>
{/if}
{* 外部S3バケットのファイルを削除 *}
{remove_file path="/custom/path/file.txt" bucket="my-custom-bucket" status_var="result"}
```

### Notes

- 削除可能なパス: クラウドストレージパス（S3/GCS）、/files/user/、/files/temp/、/files/ltd/ 以下。

---

## remove_dir

ディレクトリを削除します。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

`status_var` パラメータを指定した場合、削除の成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{remove_dir path="/files/user/temp_folder"}
{* 結果を取得 *}
{remove_dir path="/files/user/old_directory" status_var="result"}
{if $result}
    <p>ディレクトリを削除しました</p>
{else}
    <p>削除に失敗しました</p>
{/if}
```

### Notes

- 削除可能なパス: /files/user/、/files/temp/、/files/ltd/ 以下。ディレクトリは空である必要があります（PHPの `rmdir()` を使用するため）。

---

## rename_file

S3/GCS上のファイルを移動（リネーム）します。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

`status_var` パラメータを指定した場合、移動の成功（true）または失敗（false）が変数に代入されます。

### Usage Example

```smarty
{* 基本的なファイル移動 *}
{rename_file src_path="/files/user/old_name.txt" dest_path="/files/user/new_name.txt"}
{* ディレクトリ間の移動 *}
{rename_file src_path="/files/temp/uploaded.pdf" dest_path="/files/user/documents/final.pdf"}
{* 動的なパスを使用 *}
{rename_file src_path=$temp_file_path dest_path="/files/user/{$user_id}/profile.jpg"}
{* 結果を取得 *}
{rename_file src_path="/files/user/old_name.txt" dest_path="/files/user/new_name.txt" status_var="result"}
{if $result}
    <p>移動成功</p>
{else}
    <p>移動失敗</p>
{/if}
```

### Notes

- 内部的に `RCMS_AWSClient::moveS3File()` を使用してS3/GCS上のファイルを移動します。バリデーションモード（`_rcms_validate`）の場合、実際の移動は実行されません。

---

## zip

クラウドファイルをZIP圧縮してクラウドストレージにアップロードします。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

`zip_dest` 変数にZIPファイルの出力パスが自動的に代入されます。

### Usage Example

```smarty
{* ファイルリストを作成 *}
{assign var=entries value=[]}
{assign var=entry value=['url' => '/files/g/public/doc1.pdf', 'name' => 'document1.pdf']}
{append var=entries value=$entry}
{* ZIPファイルを作成 *}
{zip entries=$entries dest='/files/g/public/archive.zip'}
{* 出力パスを使用 *}
<a href="{$zip_dest}">Download ZIP</a>
```

### Notes

- `entries` 配列の各要素は `url`（ファイルURL）と `name`（ZIP内でのファイル名）を含む連想配列である必要があります。`dest` を省略すると一時ファイルが自動生成されます。処理はGoogle Cloud Pub/Subを使用して非同期で実行されます。

---

## unzip

ZIPファイルを解凍してクラウドストレージにアップロードします。

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

なし（ファイルが展開されます）

### Usage Example

```smarty
{* 基本的な使用例 *}
{unzip src='/files/g/public/archive.zip' dest='/files/g/public/extracted/'}
{* 上書きモードで解凍 *}
{unzip src='/files/g/public/archive.zip' dest='/files/g/public/extracted/' overwrite=1}
{* コールバック付きで解凍 *}
{unzip src='/files/g/public/archive.zip' dest='/files/g/public/extracted/' callback_batch='process_files' data=$metadata}
```

### Notes

- 展開先として許可されているパスは `/files/g/public/`、`/files/g/private/` 以下です。処理はGoogle Cloud Pub/Subを使用して非同期で実行されます。Firebase認証情報とPub/Sub認証情報が必要です。

---

## storage_url

クラウドストレージ上のファイルへの署名付きURLを取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数に署名付きURLが代入されます。ファイルが存在しない場合（`chk_file_exists=true` の時）は null が代入されます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{storage_url var="url" path="/files/user/document.pdf"}
<a href="{$url}">ダウンロード</a>
{* 有効期限を指定 *}
{storage_url var="url" path="/files/user/image.jpg" expire="+1 hour"}
{* ファイル存在チェックを無効化 *}
{storage_url var="url" path="/files/temp/generated.pdf" chk_file_exists=false}
```

### Notes

- `var` と `path` の両方が必須です。`chk_file_exists=true`（デフォルト）の場合、ファイルが存在しないと null が代入されます。内部的に `RCMS_AWSClient::getS3Url()` を使用します。

---

## rcms_file_exists

Check if a file exists at the specified path.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | File path to check |

### Return Value

Boolean: true if file exists, false otherwise.

### Usage Example

```smarty
{* Check if image exists before displaying *}
{if $image_path|rcms_file_exists}
  <img src="{$image_path}" alt="Image">
{else}
  <img src="/images/placeholder.png" alt="No image">
{/if}
```

### Notes

- Wrapper around PHP's file_exists() function
- Returns false for empty/null input
- Works with both files and directories
- Does not check if file is readable, only existence
- Useful for graceful fallbacks and conditional includes

---

## rcms_file_mtime

Get the last modification time of a file as a Unix timestamp.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | File path to check |

### Return Value

Integer Unix timestamp of the file's last modification time, or false if file doesn't exist.

### Usage Example

```smarty
{* Cache busting for CSS/JS files *}
<link rel="stylesheet" href="/css/style.css?v={"/css/style.css"|rcms_file_mtime}">
{* Display last updated date *}
{assign var='mtime' value=$file_path|rcms_file_mtime}
{if $mtime}
  <p>Last updated: {$mtime|date_format:'%Y-%m-%d %H:%M'}</p>
{/if}
```

### Notes

- Wrapper around PHP's filemtime() function
- Returns false if file doesn't exist (check with rcms_file_exists first)
- Timestamp is in server's timezone
- Combine with date_format modifier for human-readable dates
- Useful for cache busting without manual version numbers

---

## rcms_file_size

Get the file size.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | File path |

### Return Value

File size in bytes.

### Usage Example

```smarty
{$path|rcms_file_size}
```

### Notes

- Returns the file size in bytes
- Use with number_format for human-readable output

---

## generate_pdf

URLからPDFを生成し、クラウドストレージに保存します。

### Parameters

|-----------|------|----------|---------|-------------|
| sleep | Integer | No | - | レンダリング前の待機時間（ミリ秒） |

### Return Value

PDF生成はPub/Sub経由で非同期実行されます。`callback_batch`で完了を検知できます。

### Usage Example

```smarty
{* 基本的な使用例 *}
{generate_pdf url="/invoice/123/" path="files/invoices/invoice_123.pdf"}
{* フルオプション *}
{generate_pdf
  url="https://example.com/report"
  path="files/reports/report.pdf"
  bucket="my-bucket"
  overwrite=1
  callback_batch="pdf_complete"
  browser_width=1200
  format="A4"
}
```

### Notes

- PDF生成はGoogle Cloud Pub/Sub経由で非同期実行されます
- pubsub_credential.jsonの設定が必要です
- 出力パスはクラウドストレージの有効なパスである必要があります

---

## make_pdf_thumb

PDFのサムネイルを作成します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 結果を代入する変数名 |

### Return Value

`var`パラメータで指定した変数にサムネイル作成結果が代入されます。

### Usage Example

```smarty
{make_pdf_thumb path="/files/user/document.pdf" output="/files/user/thumb.png" var="result"}
```

### Notes

- PDFの最初のページからサムネイル画像を生成します

---

## detect_document_text

PDF/TIFFファイルからテキストを検出（OCR）します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var`パラメータで指定した変数に検出されたテキストが代入されます。type='text'の場合は文字列、type='array'の場合は配列。

### Usage Example

```smarty
{* ファイル名で指定 *}
{detect_document_text var="text" dir="/files/d" file_nm="document.pdf"}
{* モジュールIDで指定 *}
{detect_document_text var="text" dir="/files/topics" module_id=123 ext_id=1}
{* 配列形式で取得 *}
{detect_document_text var="pages" dir="/files/d" file_nm="document.pdf" type="array"}
```

### Notes

- PDF/TIFFファイルからOCRでテキストを抽出します
- Google Cloud Vision APIを使用します
- バッチ処理またはテストモードでのみ実行可能です

