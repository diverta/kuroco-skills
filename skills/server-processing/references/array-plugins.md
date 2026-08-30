# 配列操作プラグイン

## 目次

- [count](#count) - Counts the number of elements ...
- [in_array](#in_array) - Checks if a value exists in an...
- [rcms_in_array](#rcms_in_array) - Check if a value exists in an ...
- [array_key_exists](#array_key_exists) - Checks if a key exists in an a...
- [implode](#implode) - Joins array elements into a st...
- [join](#join) - Joins array elements into a st...
- [explode](#explode) - Splits a string into an array ...
- [split](#split) - 区切り文字を使用して文字列を配列に分割します。正規表現とリテ...
- [assign_array](#assign_array) - 配列をテンプレート変数に代入します。
- [assign_array_get](#assign_array_get) - 配列からキーで値を取得します。
- [assign_array_set](#assign_array_set) - 配列に値を設定します。
- [assign_array_unset](#assign_array_unset) - 配列からキーを削除します。
- [assign_array_diff](#assign_array_diff) - 2つの配列の差分を取得します。
- [assign_array_intersect](#assign_array_intersect) - 2つの配列の共通部分を取得します。
- [assign_array_pick](#assign_array_pick) - 配列から特定のキーを抽出します。
- [assign_pager](#assign_pager) - 配列をページ分割し、そのページ分のデータとページ情報を代入し...
- [rcms_sort](#rcms_sort) - Sort an array.
- [rcms_rsort](#rcms_rsort) - Sort an array in reverse order...
- [rcms_asort](#rcms_asort) - Sort an array by values in asc...
- [rcms_arsort](#rcms_arsort) - Sort an array by values in des...
- [rcms_ksort](#rcms_ksort) - Sort an array by key.
- [rcms_krsort](#rcms_krsort) - Sort an array by key in revers...
- [rcms_sort_by_key](#rcms_sort_by_key) - Sort an array of associative a...
- [json_decode](#json_decode) - Decodes a JSON string into a P...
- [rcms_json_encode](#rcms_json_encode) - 値をUnicodeサポート付きでJSON形式にエンコードし、...
- [to_object](#to_object) - 配列をstdClassオブジェクトに変換します。
- [to_form_options](#to_form_options) - 連想配列をフォームセレクト/オプション要素に適した形式に変換...
- [property_exists](#property_exists) - オブジェクトまたはクラスにプロパティが存在するかチェックしま...
- [empty](#empty) - Checks whether a value is empt...
- [conv_bool](#conv_bool) - Converts a value to a boolean ...

---

## count

Counts the number of elements in an array. This is a PHP7-compatible Smarty count modifier.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | Array | Required | - | The array to count |

### Return Value

Returns an integer representing the number of elements in the array. Returns `0` if the input is not an array.

### Usage Example

```smarty
{$array|count}
```

### Notes

- Works with both indexed and associative arrays
- Returns `0` for empty arrays
- Unlike PHP's native `count()`, this modifier returns `0` for non-array values instead of `1`
- PHP7-compatible: handles type checking before calling the native `count()` function

---

## in_array

Checks if a value exists in an array. PHP7-compatible with safe type handling.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | any | Required | - | The value to search for (needle) |

### Return Value

Returns `true` if the value is found in the array, `false` otherwise. Returns `false` if the haystack is not an array.

### Usage Example

```smarty
{* Basic usage *}
{if $value|in_array:$array}Value exists{/if}
{* With strict type comparison *}
{if $value|in_array:$array:true}Value exists (strict){/if}
{* Safe even if $array might not be an array *}
{if "apple"|in_array:$fruits}Apple is in the list{/if}
```

### Notes

- Safe type handling: Returns `false` if the haystack is not an array (instead of throwing an error)
- Performs a loose comparison by default (like PHP's `in_array()`)
- Set the third parameter to `true` for strict type comparison
- PHP7-compatible: validates the haystack is an array before calling native `in_array()`

---

## rcms_in_array

Check if a value exists in an array.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Mixed | Required | - | Value to search for |

### Return Value

Boolean indicating whether the value exists in the array.

### Usage Example

```smarty
{if $value|rcms_in_array:$array}Exists{/if}
```

### Notes

- Equivalent to PHP's in_array() function
- Performs a loose comparison by default

---

## array_key_exists

Checks if a key exists in an array. This is a PHP5-compatible Smarty modifier.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | String/Integer | Required | - | The key to check |

### Return Value

Returns `true` if the key exists in the array, `false` otherwise. Also returns `false` if the second parameter is not an array.

### Usage Example

```smarty
{if $key|array_key_exists:$array}Key exists{/if}
{* Check for numeric key *}
{if 0|array_key_exists:$array}First element exists{/if}
```

### Notes

- Checks for the existence of a key, not the value
- Returns `true` even if the value associated with the key is `null`
- Returns `false` if the second parameter is not an array (safe handling)
- PHP5-compatible: validates input types before calling the native `array_key_exists()` function

---

## implode

Joins array elements into a string using a delimiter. PHP7-compatible with flexible argument order.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Returns a string with all array elements joined by the delimiter. Returns an empty string `''` if the array is null or empty. Returns `null` if the arguments don't match any supported pattern.

### Usage Example

```smarty
{* Standard argument order: separator|implode:array *}
{assign var='arr' value='["1","2","3"]'|json_decode}
{','|implode:$arr}  {* Output: '1,2,3' *}
{* Omit separator (joins with empty string) *}
{$arr|@implode}     {* Output: '123' *}
{* Legacy PHP7-compatible order: array|@implode:separator *}
{$arr|@implode:','} {* Output: '1,2,3' *}
{* Separator with null array (returns empty string) *}
{','|implode:null}  {* Output: '' *}
```

### Notes

- Flexible argument order: Supports both standard and legacy (PHP7-compatible) argument orders
- Use `@` modifier when passing an array as the first argument to prevent Smarty from iterating over it
- Returns `null` if arguments don't match any of the supported patterns

---

## join

Joins array elements into a string using a delimiter. This is an alias for the `implode` modifier with identical functionality.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Returns a string with all array elements joined by the delimiter. Returns an empty string `''` if the array is null or empty. Returns `null` if the arguments don't match any supported pattern.

### Usage Example

```smarty
{* Standard argument order: separator|join:array *}
{assign var='arr' value='["1","2","3"]'|json_decode}
{','|join:$arr}  {* Output: '1,2,3' *}
{* Omit separator (joins with empty string) *}
{$arr|@join}     {* Output: '123' *}
{* Legacy PHP7-compatible order: array|@join:separator *}
{$arr|@join:','} {* Output: '1,2,3' *}
{* String input (returns the string as-is) *}
{assign var='str' value='foo'}
{$str|join}      {* Output: 'foo' *}
```

### Notes

- Alias for `implode`: Internally calls the `implode` modifier
- Flexible argument order: Supports both standard and legacy (PHP7-compatible) argument orders
- Use `@` modifier when passing an array as the first argument to prevent Smarty from iterating over it

---

## explode

Splits a string into an array using a delimiter. PHP8-compatible with safe type handling.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | String | Required | - | The delimiter to split by |

### Return Value

Returns an array of strings split by the delimiter. Returns an empty array `[]` if the string is empty or not a valid type.

### Usage Example

```smarty
{* Basic split *}
{','|explode:$csv_string}
{* Split path *}
{'/'|explode:$file_path}
{* Works with numeric input *}
{'-'|explode:12345}
```

### Notes

- Parameter order: Delimiter is the modifier input, string is passed after the colon
- Type coercion: Numeric types (int, float, double) are automatically converted to strings before splitting
- Type safety: Returns empty array for non-string/non-numeric input types (prevents PHP8 errors)
- Empty string handling: Returns empty array for empty strings
- Unlike `split`, this modifier only supports literal delimiters (no regex support)

---

## split

区切り文字を使用して文字列を配列に分割します。正規表現とリテラル区切り文字の両方をサポートします。

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | String | Yes | - | 分割に使用する区切り文字 |

### Return Value

文字列の配列を返します。文字列が空 `""`、または有効な型でない場合は空の配列 `[]` を返します。

### Usage Example

```smarty
{* リテラル区切り文字での基本的な分割 *}
{','|split:$csv_string}
{* 正規表現パターンで分割（/で始まる必要あり） *}
{'/\s+/'|split:$text}  {* 空白で分割 *}
{* 数値の分割（自動的に文字列に変換） *}
{'-'|split:12345}  {* 数値入力も動作 *}
```

### Notes

- パラメータの順序は、区切り文字が修飾子入力、文字列はコロンの後に渡します。区切り文字が `/` で始まり3文字以上の場合は正規表現として `preg_split()` を使用し、それ以外は `explode2()` を使用します。

---

## assign_array

配列をテンプレート変数に代入します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 配列を代入する変数名 |

### Return Value

`var` パラメータで指定した変数に配列が代入されます。`keys` を指定しない場合はインデックス配列、指定した場合は連想配列（既存の変数があれば追加/上書き）。

### Usage Example

```smarty
{* インデックス配列を作成 *}
{assign_array var="foo" values="bar1,bar2"}
{* 結果: ['bar1', 'bar2'] *}
{* カスタム区切り文字を使用 *}
{assign_array var="foo" values="bar1;bar2;bar3" delimiter=";"}
{* 結果: ['bar1', 'bar2', 'bar3'] *}
{* 連想配列を作成 *}
{assign_array var="foo" keys="key1,key2,key3" values="bar1,bar2,bar3"}
{* 結果: ['key1' => 'bar1', 'key2' => 'bar2', 'key3' => 'bar3'] *}
{* 単一のキーと値 *}
{assign_array var="foo" keys="key1" values="bar1"}
{* 結果: ['key1' => 'bar1'] *}
```

### Notes

- `var` と `values` パラメータは必須です
- `values` は文字列である必要があります（整数や小数は自動的に文字列に変換されます）
- `keys` を指定した場合、既存の変数が配列でなければ空配列から開始されます
- `keys` を指定した場合、既存の配列に対して追加/上書きが行われます

---

## assign_array_get

配列からキーで値を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 結果変数名 |

### Return Value

`var`パラメータで指定した変数に取得した値が代入されます。

### Usage Example

```smarty
{assign_array_get var="foo" key="bar1" from=$row}
```

### Notes

- 指定したキーが存在しない場合はnullが代入されます

---

## assign_array_set

配列に値を設定します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 変数名 |

### Return Value

`var`パラメータで指定した変数に更新された配列が代入されます。

### Usage Example

```smarty
{assign_array_set var="foo" key="bar1" value="bar2" from=$row}
```

### Notes

- 既存のキーがある場合は上書きされます
- 元の配列は変更されず、新しい配列が作成されます

---

## assign_array_unset

配列からキーを削除します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 変数名 |

### Return Value

`var`パラメータで指定した変数にキーが削除された配列が代入されます。

### Usage Example

```smarty
{assign_array_unset var="foo" value=$arr key=0}
{assign_array_unset var="foo" value=$arr key=['key1', 'key2']}
```

### Notes

- 複数のキーを配列で指定して一度に削除できます
- 元の配列は変更されず、新しい配列が作成されます

---

## assign_array_diff

2つの配列の差分を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 差分配列の変数名 |

### Return Value

`var`パラメータで指定した変数に差分配列が代入されます。

### Usage Example

```smarty
{assign_array_diff var="foo" array1=$array1 array2=$array2 diff_mode='normal'}
```

### Notes

- diff_mode='normal'は値の差分を取得します
- diff_mode='key'はキーの差分を取得します

---

## assign_array_intersect

2つの配列の共通部分を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 共通部分配列の変数名 |

### Return Value

`var`パラメータで指定した変数に共通部分の配列が代入されます。

### Usage Example

```smarty
{assign_array_intersect var="foo" array1=$array1 array2=$array2 intersect_mode='normal'}
```

### Notes

- intersect_mode='normal'は値の共通部分を取得します
- intersect_mode='assoc'はキーと値の両方が一致する要素を取得します
- intersect_mode='key'はキーの共通部分を取得します

---

## assign_array_pick

配列から特定のキーを抽出します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Required | - | 変数名 |

### Return Value

`var`パラメータで指定した変数に抽出された配列が代入されます。

### Usage Example

```smarty
{assign_array_pick var="foo" keys="bar1,bar2,bar3" from=$row}
```

### Notes

- 指定したキーのみを含む新しい配列を作成します
- 存在しないキーは無視されます

---

## assign_pager

配列をページ分割し、そのページ分のデータとページ情報を代入します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Conditional | - | ページ分のデータを代入する変数名（var_pageInfoなしの場合は必須） |

### Return Value

varに指定した変数へそのページ分の配列が、var_pageInfoに指定した変数へページ情報（totalCnt / perPage / totalPageCnt / pageNo / next_page_param など）が代入されます。

### Usage Example

```smarty
{* リクエストの pageID に従ってページ分割 *}
{assign_pager from=$rows perPage=10 var="page_rows" var_pageInfo="pageInfo"}
{foreach from=$page_rows item="row"}{$row.subject}{/foreach}
{* ページ番号を明示して取得 *}
{assign_pager from=$rows perPage=10 pageID=2 var="page_rows"}
{* カスタム処理をAPIとして公開する場合の例 *}
{assign_pager from=$notifications perPage=20 var="items" var_pageInfo="pageInfo"}
{assign_array var="response" values=""}
{append var="response" index="list" value=$items}
{append var="response" index="pageInfo" value=$pageInfo}
{$response|@rcms_json_encode}
```

### Notes

- ページ情報の形式は一覧APIの pageInfo と同じです
- 対象配列は全件がメモリ上に載るため、あらかじめ件数を絞った配列を渡してください
- pageIDが総ページ数を超える場合は最終ページに丸められます

---

## rcms_sort

Sort an array.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array to sort |

### Return Value

Sorted array.

### Usage Example

```smarty
{$array|@rcms_sort}
```

### Notes

- Equivalent to PHP's sort() function
- Sorts values in ascending order
- Keys are re-indexed
- Use the @ modifier for array operations

---

## rcms_rsort

Sort an array in reverse order.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array to sort |

### Return Value

Array sorted in descending order.

### Usage Example

```smarty
{$array|@rcms_rsort}
```

### Notes

- Equivalent to PHP's rsort() function
- Sorts values in descending order
- Keys are re-indexed
- Use the @ modifier for array operations

---

## rcms_asort

Sort an array by values in ascending order while maintaining key association.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array to sort |

### Return Value

Array sorted by values in ascending order with original keys preserved.

### Usage Example

```smarty
{* Sort array values ascending, keep keys *}
{$scores|@rcms_asort}
{* In a foreach loop *}
{foreach $scores|@rcms_asort as $name => $score}
  {$name}: {$score}<br>
{/foreach}
```

### Notes

- Equivalent to PHP's asort() function
- IMPORTANT: Use the @ prefix for array modifiers
- Without @, Smarty tries to apply the modifier to each element
- Returns the input unchanged if not an array
- Original array keys are preserved in the result

---

## rcms_arsort

Sort an array by values in descending order while maintaining key association.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array to sort |

### Return Value

Array sorted by values in descending order with original keys preserved.

### Usage Example

```smarty
{* Sort array values descending, keep keys *}
{$scores|@rcms_arsort}
{* In a foreach loop *}
{foreach $scores|@rcms_arsort as $name => $score}
  {$name}: {$score}<br>
{/foreach}
```

### Notes

- Equivalent to PHP's arsort() function
- IMPORTANT: Use the @ prefix for array modifiers
- Without @, Smarty tries to apply the modifier to each element
- Returns the input unchanged if not an array
- Original array keys are preserved in the result

---

## rcms_ksort

Sort an array by key.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array to sort |

### Return Value

Array sorted by keys in ascending order.

### Usage Example

```smarty
{$array|@rcms_ksort}
```

### Notes

- Equivalent to PHP's ksort() function
- Sorts array keys in ascending order
- Use the @ modifier for array operations

---

## rcms_krsort

Sort an array by key in reverse order.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array to sort |

### Return Value

Array sorted by keys in descending order.

### Usage Example

```smarty
{$array|@rcms_krsort}
```

### Notes

- Equivalent to PHP's krsort() function
- Sorts array keys in descending order
- Use the @ modifier for array operations

---

## rcms_sort_by_key

Sort an array of associative arrays by a specific key.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Array | Required | - | Array of arrays/objects to sort |

### Return Value

Array sorted by the specified key.

### Usage Example

```smarty
{$array|@rcms_sort_by_key:'name':'asc'}
```

### Notes

- Sorts an array of associative arrays by a specific key
- Useful for sorting lists of records
- Use the @ modifier for array operations

---

## json_decode

Decodes a JSON string into a PHP value.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | String | Required | - | The JSON string to decode |

### Return Value

Returns the decoded value. By default, objects in JSON are decoded as associative arrays. Returns `null` if the input is not a string or if the JSON is invalid.

### Usage Example

```smarty
{* Basic usage - returns associative array by default *}
{assign var='data' value='{"name":"John","age":30}'|json_decode}
{$data.name}  {* Output: John *}
{* Decode JSON array *}
{assign var='items' value='["apple","banana","orange"]'|json_decode}
{$items[0]}  {* Output: apple *}
{* Return as object instead of array *}
{assign var='obj' value='{"name":"John"}'|json_decode:false}
{$obj->name}  {* Output: John *}
```

### Notes

- Returns associative arrays by default (second parameter defaults to `true`)
- Type safety: Returns `null` if the input is not a string
- Invalid JSON will return `null`
- Useful for parsing JSON data received from APIs or stored in database fields

---

## rcms_json_encode

値をUnicodeサポート付きでJSON形式にエンコードし、RCMSコンテンツ境界の特別な処理を行います。

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | any | Yes | - | エンコードする値 |

### Return Value

エスケープされていないUnicode文字を含むJSONエンコード文字列を返します。

### Usage Example

```smarty
{* 基本的な使用例 *}
{$array|rcms_json_encode}
{* JavaScriptで使用 *}
<script>
var data = {$data|rcms_json_encode};
</script>
{* オブジェクトのエンコード *}
{$user_data|rcms_json_encode}
```

### Notes

- `JSON_UNESCAPED_UNICODE` フラグを使用してUnicode文字（日本語など）をエスケープせずに保持します。`__RCMS_CONTENT_BOUNDARY__` マーカーを含む文字列を自動的に `explode2()` で配列に分割する特別な処理があります。

---

## to_object

配列をstdClassオブジェクトに変換します。

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | Array | Yes | - | 変換する配列 |

### Return Value

配列のキーに対応するプロパティを持つstdClassオブジェクトを返します。

### Usage Example

```smarty
{* 配列をオブジェクトに変換 *}
{assign var='obj' value=['name' => 'John', 'age' => 30]|@to_object}
{$obj->name}  {* 出力: John *}
{* オブジェクトを期待するAPIに便利 *}
{assign var='request_body' value=$params|@to_object}
```

### Notes

- PHPの型キャスト `(object)$target` を使用します。連想配列のキーはオブジェクトプロパティになります。ネストした配列はネストしたオブジェクトには変換されません（浅い変換）。配列を渡す際は `@` 修飾子を使用してください。

---

## to_form_options

連想配列をフォームセレクト/オプション要素に適した形式に変換します。

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | Array | Yes | - | 変換する連想配列 |

### Return Value

`[['key' => $originalKey, 'value' => $originalValue], ...]` 形式の連想配列の配列を返します。入力が配列でない場合は空の配列を返します。

### Usage Example

```smarty
{* デフォルトでの基本的な使用例 *}
{assign var='options' value=['a' => 'Apple', 'b' => 'Banana']|@to_form_options}
{* 結果: [['key' => 'a', 'value' => 'Apple'], ['key' => 'b', 'value' => 'Banana']] *}
{* カスタムプロパティ名 *}
{assign var='options' value=$status_map|@to_form_options:'id':'label'}
{* 結果: [['id' => ..., 'label' => ...], ...] *}
```

### Notes

- キー/値のペアを名前付きプロパティを持つオブジェクトの配列に変換します。配列を渡す際は `@` 修飾子を使用してください。

---

## property_exists

オブジェクトまたはクラスにプロパティが存在するかチェックします。

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | Object or String | Yes | - | チェック対象のオブジェクトインスタンスまたはクラス名 |

### Return Value

プロパティが存在する場合は `true`、存在しない場合は `false` を返します。プロパティ名が文字列でない場合、または第一引数がオブジェクトでも文字列でもない場合も `false` を返します。

### Usage Example

```smarty
{* オブジェクトにプロパティがあるかチェック *}
{if $object|property_exists:'name'}Object has name property{/if}
{* クラス名でチェック *}
{if 'MyClass'|property_exists:'staticProperty'}Class has static property{/if}
```

### Notes

- パラメータの順序は、オブジェクト/クラスが修飾子入力、プロパティ名はコロンの後に渡します。プロパティの値に関係なく（nullでも）存在チェックを行います。

---

## empty

Checks whether a value is empty, with enhanced handling for stdClass objects.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | any | Required | - | The value to check |

### Return Value

Returns `true` if the value is empty, `false` otherwise.

### Usage Example

```smarty
{if $value|empty}Value is empty{/if}
{* Works with objects too *}
{if $object|empty}Object has no properties{/if}
```

### Notes

- Empty values include: empty string `""`, `0`, `null`, `false`, empty array `[]`
- Enhanced stdClass handling: Also returns `true` for empty stdClass objects (objects with no properties)
- This is different from PHP's native `empty()` which would return `false` for an empty stdClass
- Useful for conditional checks in templates, especially when dealing with API responses that may return empty objects

---

## conv_bool

Converts a value to a boolean using the internal `convBool()` function.

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | any | Required | - | The value to convert |

### Return Value

Returns a boolean value (`true` or `false`).

### Usage Example

```smarty
{$value|conv_bool}
{* Use in conditionals *}
{if $string_value|conv_bool}
    Value is truthy
{/if}
```

### Notes

- Delegates to the internal `convBool()` function for conversion
- Useful for normalizing various truthy/falsy values to strict booleans
- Helpful when working with form inputs or API responses where boolean values may be represented as strings

