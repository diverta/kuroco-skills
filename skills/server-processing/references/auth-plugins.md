# 認証・セキュリティプラグイン

## 目次

- [rcms_auth](#rcms_auth) - Show or hide content based on ...
- [assign_session](#assign_session) - セッションに値を代入します。
- [rcms_encrypt](#rcms_encrypt) - データの暗号化および復号を行います。
- [rcms_hash](#rcms_hash) - ハッシュを生成します。
- [secret](#secret) - シークレット値を取得します。

---

## rcms_auth

Show or hide content based on user resource permissions.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Returns block content if user has permission (or lacks permission when not=true). Returns empty string if permission check fails.

### Usage Example

```smarty
{* Basic read permission check *}
{rcms_auth target="read:/topics/"}
  <a href="/topics/">View Topics</a>
{/rcms_auth}
{* Check for insert OR update permission *}
{rcms_auth target="insert|update:/topics/"}
  <a href="/topics/edit/">Edit Topics</a>
{/rcms_auth}
{* Inverted check - show when NO permission *}
{rcms_auth target="insert|update:/topics/" not=true}
  <p>You do not have edit permission for topics.</p>
{/rcms_auth}
```

### Notes

- Uses RCMSUser::getResourceAuth($action, $path) for permission checking
- The || separator creates OR conditions between targets
- The | separator within actions means user needs ANY of those actions
- If target contains no :, defaults to "read" action
- When not=true, returns content only if ALL conditions fail

---

## assign_session

セッションに値を代入します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | 変数名 |

### Return Value

valueを指定した場合は値がセッションに設定され、varを指定した場合はセッションから値が取得されます。

### Usage Example

```smarty
{assign_session key="key1" value="bar"}
{assign_session var="foo" key="key1"}
{assign_session key="key1" unset=true}
```

### Notes

- `$_SESSION["smarty_session"]`に保存されます
- 最大300KB
- セッション間でデータを保持できます

---

## rcms_encrypt

データの暗号化および復号を行います。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | No | - | 結果を代入する変数名 |

### Return Value

`var` パラメータを指定した場合、暗号化/復号されたデータが変数に代入されます。失敗時は false が代入されます。

### Usage Example

```smarty
{* シークレットキーを取得 *}
{secret var="encryption_key" key="MY_ENCRYPTION_KEY"}
{* データを暗号化 *}
{rcms_encrypt var="encrypted" action="encrypt" data=$sensitive_data key=$encryption_key}
{* データを復号 *}
{rcms_encrypt var="decrypted" action="decrypt" data=$encrypted key=$encryption_key}
```

### Notes

- `action`、`data`、`key` の3つのパラメータは必須です。`action` は `encrypt` または `decrypt` のいずれかである必要があります。内部的に `encSecret()` と `decSecret()` 関数を使用します。

---

## rcms_hash

ハッシュを生成します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にハッシュ値が代入されます。

### Usage Example

```smarty
{* 基本的なハッシュ（SHA-256） *}
{rcms_hash var='hash' data='hello world'}
{* MD5ハッシュ *}
{rcms_hash var='hash' data=$data algo='md5'}
{* HMAC-SHA256（秘密鍵付き） *}
{rcms_hash var='hmac' data=$message key=$secret_key algo='sha256'}
{* バイナリ出力 *}
{rcms_hash var='binary_hash' data=$data binary=true}
```

### Notes

- `var`, `algo`, `data` が必須です（いずれかが欠けている場合は何も実行されません）。`key` を指定した場合、HMAC（Hash-based Message Authentication Code）が生成されます。

---

## secret

シークレット値を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にシークレット値が代入されます。

### Usage Example

```smarty
{* シークレット値を取得 *}
{secret var='api_key' key='EXTERNAL_API_KEY'}
{* 取得した値を使用 *}
{secret var='db_password' key='DB_PASSWORD'}
{api endpoint='https://api.example.com' headers=['Authorization: Bearer '|cat:$api_key] var='response'}
```

### Notes

- `var` と `key` パラメータは必須です（未指定の場合はSmartyエラーがトリガーされます）。Kuroco管理画面のシークレット設定で登録した値を取得します。

