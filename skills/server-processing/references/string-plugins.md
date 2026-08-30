# 文字列処理プラグイン

## 目次

- [escape](#escape) - Escape string according to spe...
- [truncate](#truncate) - Truncate string to specified l...
- [mb_truncate](#mb_truncate) - Truncate string to specified l...
- [mbtruncate](#mbtruncate) - マルチバイト文字対応で文字列を切り詰めます。内部的に `rc...
- [date_format](#date_format) - Format datestamps using PHP da...
- [translate](#translate) - Translate a string.
- [nl2br](#nl2br) - Convert newlines to HTML `<br>...
- [replace](#replace) - Simple string search and repla...
- [regex_replace](#regex_replace) - Search and replace using regul...
- [strip_tags](#strip_tags) - Remove HTML tags from text.
- [rcms_strip_tags](#rcms_strip_tags) - Remove HTML tags from a string...
- [capitalize](#capitalize) - Capitalize first letter of eac...
- [lower](#lower) - Convert string to lowercase.
- [upper](#upper) - Convert string to uppercase.
- [strtolower](#strtolower) - Convert string to lowercase (w...
- [strtoupper](#strtoupper) - Convert string to uppercase (w...
- [substr](#substr) - Return substring from input st...
- [cat](#cat) - Concatenate a value to a varia...
- [spacify](#spacify) - Add spaces (or custom string) ...
- [wordwrap](#wordwrap) - Wrap text to specified line le...
- [indent](#indent) - Indent lines of text.
- [string_format](#string_format) - Format string using sprintf.
- [rcms_number_format](#rcms_number_format) - Format a number (extended vers...
- [rcms_replace](#rcms_replace) - Replace a string using regular...
- [rcms_match](#rcms_match) - 正規表現マッチング（preg_match）を行います。
- [rcms_match_all](#rcms_match_all) - 正規表現で全マッチを取得します（preg_match_all...
- [pg_dateformat](#pg_dateformat) - Format a PostgreSQL date.
- [pg_dateformat2](#pg_dateformat2) - Format a PostgreSQL date (alte...
- [strtodate](#strtodate) - タイムスタンプまたは日付文字列をフォーマットして日付を取得し...
- [default](#default) - Provide default value for empt...
- [strip](#strip) - Replace all repeated whitespac...
- [count_characters](#count_characters) - Count number of characters in ...
- [count_paragraphs](#count_paragraphs) - Count number of paragraphs in ...
- [count_sentences](#count_sentences) - Count number of sentences in t...
- [count_words](#count_words) - Count number of words in text.

---

## escape

Escape string according to specified type.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Escaped string

### Usage Example

```smarty
{$html|escape}
{$html|escape:"html"}
{$url|escape:"url"}
{$js_string|escape:"javascript"}
{$email|escape:"mail"}
```

### Notes

- Escape types: html (htmlspecialchars with ENT_QUOTES), htmlall (htmlentities with ENT_QUOTES), url (rawurlencode), urlpathinfo (rawurlencode but preserve '/'), quotes (escape unescaped single quotes), hex (convert each char to %XX hex), hexentity (convert each char to &#xXX;), decentity (convert each char to &#NN;), javascript (escape for JS strings), mail (replace @ and . with [AT] and [DOT]), nonstd (escape non-standard chars >= 126)
- Null values return empty string
- Non-scalar values (arrays, objects) return empty string
- Values are cast to string before processing
- JavaScript mode escapes: `\\`, `\'`, `\"`, `\r`, `\n`, `</` (to `<\/`)
- Mail mode useful for displaying emails on web pages safely
- Default charset is UTF-8
- Unknown escape types return the original string unchanged
- `urlpathinfo` is useful for URL paths where `/` should not be encoded

---

## truncate

Truncate string to specified length (byte-based).

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Truncated string

### Usage Example

```smarty
{$text|truncate:50}
{$long_string|truncate:30:"...":true}
{$text|truncate:100:"[more]":false:true}
```

### Notes

- Uses byte functions (`strlen`, `substr`) - NOT multibyte-safe
- For multibyte strings (UTF-8, etc.), use `mb_truncate` instead
- If `length=0`, returns empty string immediately
- The "etc" string length is subtracted from the maximum length (uses `min($length, strlen($etc))` to prevent negative lengths)
- When `break_words=false` (default) and `middle=false`, truncates at word boundary using `/\s+?(\S+)?$/` pattern
- When `middle=true`, keeps first half and last half: `first_half + etc + last_half`
- If string length is less than or equal to specified length, returns original string unchanged

---

## mb_truncate

Truncate string to specified length (multibyte-safe).

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Truncated string

### Usage Example

```smarty
{$long_text|mb_truncate:50}
{$text|mb_truncate:30:"...":true}
{$string|mb_truncate:100:"[more]":false:true}
```

### Notes

- Uses multibyte functions (`mb_strlen`, `mb_substr`) - safe for UTF-8 and other encodings
- If `length=0`, returns empty string immediately
- The "etc" string length is subtracted from the maximum length before truncation
- When `break_words=false` (default) and `middle=false`, truncates at word boundary using `/\s+?(\S+)?$/` pattern
- When `middle=true`, keeps first half and last half: `first_half + etc + last_half`
- Length includes the "etc" string in the final output
- If string length is less than or equal to specified length, returns original string unchanged

---

## mbtruncate

マルチバイト文字対応で文字列を切り詰めます。内部的に `rcms_mbtruncate()` 関数に委譲します。

### Parameters

|-----------|------|----------|---------|-------------|
| (modifier input) | String | Yes | - | 切り詰める文字列 |

### Return Value

切り詰められた文字列を返します。切り詰めが発生した場合はオプションの接尾辞が付きます。

### Usage Example

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

### Notes

- マルチバイト文字（日本語、中国語、韓国語など）を適切に処理します。マルチバイト文字の途中で切断しません。

---

## date_format

Format datestamps using PHP date() format.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Formatted date string, or nothing (void) if both input and default are empty

### Usage Example

```smarty
{$timestamp|date_format}
{$date|date_format:"%Y-%m-%d"}
{$datetime|date_format:"Y-m-d H:i:s"}
{"2024-01-15"|date_format:"F j, Y"}
{$maybe_empty|date_format:"Y-m-d":"2024-01-01"}
```

### Notes

- Uses `smarty_make_timestamp()` to parse input (supports timestamps, date strings, MySQL format)
- Returns nothing if both input string and default_date are empty
- Supports strftime format codes (converted to PHP date() format): %a->D, %A->l, %w->w, %d->d, %b->M, %B->F, %m->m, %y->y, %Y->Y, %H->H, %I->h, %p->A, %M->i, %S->s, %f->u, %j->z, %W->W
- Strftime conversion only occurs if format contains `%` character
- Uses PHP `date()` function for final formatting

---

## translate

Translate a string.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | Translation key |

### Return Value

Translated string for the current language.

### Usage Example

```smarty
{$key|translate}
{'/label/submit'|translate}
```

### Notes

- Looks up the translation key in the i18n database
- Returns the localized string for the current language
- Keys typically start with a forward slash (e.g., '/label/submit')

---

## nl2br

Convert newlines to HTML `<br>` tags.

### Return Value

String with `<br>` tags inserted before newlines

### Usage Example

```smarty
{$text|nl2br}
{"Line 1\nLine 2"|nl2br}
{* Output: Line 1<br />
Line 2 *}
```

### Notes

- Uses PHP `nl2br()` function directly
- Converts `\r\n`, `\r`, and `\n` by inserting `<br />` BEFORE the newline
- Does NOT remove original newlines (they remain after the `<br />` tag)
- In PHP 5.3+, produces XHTML-compatible `<br />` by default
- For multiple consecutive newlines, each gets its own `<br />` tag

---

## replace

Simple string search and replace.

### Parameters

|-----------|------|----------|---------|-------------|
| replace | String/Array | Required | - | Replacement string(s) |

### Return Value

Modified string with replacements applied

### Usage Example

```smarty
{$text|replace:"old":"new"}
{$path|replace:"\\":"/"}
{"Hello World"|replace:"World":"Everyone"}
```

### Notes

- Uses PHP `str_replace()` directly
- NOT regex - performs literal string replacement
- Case-sensitive (use `regex_replace` with `i` flag for case-insensitive)
- Replaces ALL occurrences, not just the first
- Can accept arrays for search and replace (per `str_replace()` behavior)

---

## regex_replace

Search and replace using regular expressions.

### Parameters

|-----------|------|----------|---------|-------------|
| replace | String/Array | Required | - | Replacement string(s) |

### Return Value

Modified string

### Usage Example

```smarty
{$text|regex_replace:"/\s+/":" "}
{$html|regex_replace:"/<.*?>/":""}
{$text|regex_replace:$patterns:$replacements}
```

### Notes

- Uses PHP `preg_replace()`
- Security features: The `e` modifier (eval) is automatically removed for security, Null bytes (`\0`) in search patterns cause truncation at that point, Pattern modifiers are parsed and sanitized
- Supports array of patterns/replacements for multiple substitutions
- Both search and replace can be arrays (must match in structure)
- Internal helper function `_smarty_regex_replace_check()` sanitizes each pattern

---

## strip_tags

Remove HTML tags from text.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

String without HTML tags

### Usage Example

```smarty
{$html|strip_tags}
{$html|strip_tags:false}
{"<p>Hello</p>"|strip_tags}           {* " Hello " with spaces *}
{"<p>Hello</p>"|strip_tags:false}     {* "Hello" no spaces *}
{"<b>A</b><i>B</i>"|strip_tags}       {* "A B" *}
{"<b>A</b><i>B</i>"|strip_tags:false} {* "AB" *}
```

### Notes

- When `replace_with_space=true` (default): Uses regex `!<[^>]*?>!` to replace ALL tags with a single space
- When `replace_with_space=false`: Uses PHP `strip_tags()` which completely removes tags
- Replacing with space prevents word concatenation (e.g., `<b>Hello</b><i>World</i>` becomes `Hello World` not `HelloWorld`)
- The regex pattern matches any tag including self-closing tags and tags with attributes
- Does NOT strip content between tags - only the tags themselves

---

## rcms_strip_tags

Remove HTML tags from a string.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | HTML content |

### Return Value

String with HTML tags removed.

### Usage Example

```smarty
{$html|rcms_strip_tags}
```

### Notes

- Removes all HTML and PHP tags from a string
- Useful for creating plain text excerpts from HTML content
- Use allowable_tags parameter to preserve certain tags

---

## capitalize

Capitalize first letter of each word.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Capitalized string

### Usage Example

```smarty
{$title|capitalize}
{"hello world"|capitalize}               {* Hello World *}
{"test 123abc hello"|capitalize}         {* Test 123abc Hello *}
{"test 123abc hello"|capitalize:true}    {* Test 123Abc Hello *}
{"it's a test"|capitalize}               {* It's A Test *}
```

### Notes

- Respects apostrophes at word start (doesn't capitalize words starting with `'`)
- By default, doesn't capitalize words starting with digits
- When `uc_digits=true`, capitalizes words even if they start with digits
- Uses word boundaries (`\b`) for matching, so handles punctuation correctly
- Words containing apostrophes (like "it's") are kept together
- Uses `ucfirst()` to capitalize the first character of each matched word
- Uses static variable to pass `uc_digits` setting to callback function

---

## lower

Convert string to lowercase.

### Return Value

Lowercase string

### Usage Example

```smarty
{"HELLO"|lower}        {* hello *}
{$name|lower}
{"ABC123"|lower}       {* abc123 *}
```

### Notes

- Uses PHP `strtolower()` directly
- NOT multibyte-safe - only works correctly with ASCII characters
- For UTF-8 or other multibyte encodings, use `strtolower` modifier (with non-scalar handling) or PHP's `mb_strtolower()`
- Numbers and special characters pass through unchanged

---

## upper

Convert string to uppercase.

### Return Value

Uppercase string

### Usage Example

```smarty
{"hello"|upper}        {* HELLO *}
{$name|upper}
{"abc123"|upper}       {* ABC123 *}
```

### Notes

- Uses PHP `strtoupper()` directly
- NOT multibyte-safe - only works correctly with ASCII characters
- For UTF-8 or other multibyte encodings, use `strtoupper` modifier (with non-scalar handling) or PHP's `mb_strtoupper()`
- Numbers and special characters pass through unchanged
- Equivalent to `strtoupper` modifier (both use the same underlying PHP function)

---

## strtolower

Convert string to lowercase (with type checking).

### Return Value

Lowercase string (empty string if input is non-scalar)

### Usage Example

```smarty
{"HELLO WORLD"|strtolower}   {* hello world *}
{$name|strtolower}
{$array|strtolower}          {* returns empty string *}
```

### Notes

- Uses PHP `strtolower()` after type checking
- Non-scalar values (arrays, objects, null) return empty string
- Values are explicitly cast to string before processing with `(string)$string`
- NOT multibyte-safe - only works correctly with ASCII characters
- For UTF-8, consider using `mb_strtolower()` in PHP code
- Similar to `lower` modifier but with explicit non-scalar handling

---

## strtoupper

Convert string to uppercase (with type checking).

### Return Value

Uppercase string (empty string if input is non-scalar)

### Usage Example

```smarty
{"hello world"|strtoupper}   {* HELLO WORLD *}
{$name|strtoupper}
{$array|strtoupper}          {* returns empty string *}
```

### Notes

- Uses PHP `strtoupper()` after type checking
- Non-scalar values (arrays, objects, null) return empty string
- Values are explicitly cast to string before processing with `(string)$string`
- NOT multibyte-safe - only works correctly with ASCII characters
- For UTF-8, consider using `mb_strtoupper()` in PHP code
- Similar to `upper` modifier but with explicit non-scalar handling

---

## substr

Return substring from input string (with type checking).

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Substring (empty string if input is non-scalar)

### Usage Example

```smarty
{"Hello World"|substr:0:5}  {* Hello *}
{$text|substr:6}            {* from position 6 to end *}
{$string|substr:-5:5}       {* last 5 characters *}
{$text|substr:0:-3}         {* all except last 3 characters *}
{$array|substr:0:5}         {* returns empty string *}
```

### Notes

- Uses PHP `substr()` after type checking
- Non-scalar values (arrays, objects, null) return empty string
- Values are explicitly cast: string to `(string)`, start and length to `(int)`
- If length is `null` or omitted, returns from start to end of string
- Negative start: counts from end of string (e.g., -5 = 5 characters from end)
- Negative length: omits that many characters from the end
- NOT multibyte-safe - counts bytes, not characters

---

## cat

Concatenate a value to a variable.

### Parameters

|-----------|------|----------|---------|-------------|
| cat | Mixed | Optional | "" | Value to append |

### Return Value

Concatenated string

### Usage Example

```smarty
{$name|cat:" Smith"}
{"Hello"|cat:" World"}
{$path|cat:".txt"}
{$count|cat:" items"}
```

### Notes

- Both the input string and the cat parameter are checked with `is_scalar()`
- Non-scalar values (arrays, objects, null) are converted to empty string for both operands
- Booleans are converted to PHP standard: `true` -> `"1"`, `false` -> `""`
- Safe for arrays/objects - they contribute empty string instead of causing errors
- Values are explicitly cast to string before concatenation

---

## spacify

Add spaces (or custom string) between each character.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Spacified string with separator between each character

### Usage Example

```smarty
{"Hello"|spacify}      {* H e l l o *}
{$text|spacify:"-"}    {* H-e-l-l-o *}
{"Test"|spacify:"_"}   {* T_e_s_t *}
{"ABC"|spacify:" - "}  {* A - B - C *}
```

### Notes

- Uses `preg_split('//', $string, -1, PREG_SPLIT_NO_EMPTY)` to split into individual characters
- Uses `implode($spacify_char, ...)` to join with separator
- The separator can be multiple characters, not just a single char
- NOT multibyte-safe - splits on bytes, which may break multibyte characters
- Empty strings return empty string (no separators)

---

## wordwrap

Wrap text to specified line length.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Wrapped string with line breaks inserted

### Usage Example

```smarty
{$text|wordwrap:40}
{$long_text|wordwrap:60:"<br>"}
{$url|wordwrap:50:"\n":true}
{$code|wordwrap:120:"<br />":true}
```

### Notes

- Uses PHP `wordwrap()` function directly
- If `cut=false` (default): Long words that exceed the width are NOT broken and will exceed line length
- If `cut=true`: Forces break at specified width, even in the middle of words
- Break string can be any string (not just single character) - useful for HTML `<br>` tags
- Existing line breaks in the input are preserved

---

## indent

Indent lines of text.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Indented string

### Usage Example

```smarty
{$code|indent}
{$text|indent:8}
{$html|indent:2:"\t"}
```

### Notes

- Indents at beginning of each line (including first line)
- Uses regex `!^!m` with multiline flag to match all line starts
- Uses `str_repeat()` to build indentation string
- Useful for code formatting or nested content
- Works with any character, not just spaces (e.g., tabs)

---

## string_format

Format string using sprintf.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Formatted string

### Usage Example

```smarty
{$number|string_format:"%02d"}        {* 05 *}
{$price|string_format:"$%.2f"}        {* $19.99 *}
{$name|string_format:"Hello, %s!"}    {* Hello, John! *}
{$hex|string_format:"%08X"}           {* 0000FF00 *}
```

### Notes

- Uses PHP `sprintf()` directly
- Common format specifiers: `%s` (string), `%d` (signed decimal integer), `%f` (floating point), `%e` (scientific notation), `%x`/`%X` (hexadecimal lower/upper), `%o` (octal), `%b` (binary), `%%` (literal percent sign)
- Supports width, precision, and padding (e.g., `%08d`, `%.2f`, `%-10s`)

---

## rcms_number_format

Format a number (extended version).

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | Number | Required | - | Number to format |

### Return Value

Formatted number string.

### Usage Example

```smarty
{$num|rcms_number_format:2:'.':','}
```

### Notes

- Extended version of number_format with more control
- Allows customization of decimal places and separators

---

## rcms_replace

Replace a string using regular expression.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | Original string |
| replace | String | Required | - | Replacement string |

### Return Value

String with replacements made.

### Usage Example

```smarty
{$str|rcms_replace:'/old/':'new'}
```

### Notes

- Uses preg_replace for pattern matching
- Search parameter should be a valid regex pattern

---

## rcms_match

正規表現マッチング（preg_match）を行います。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数に以下のいずれかが代入されます: マッチした場合はマッチ結果の配列、マッチしなかった場合は 0、エラーの場合は false。

### Usage Example

```smarty
{* 基本的な使用例 *}
{rcms_match var="matches" pattern="/\d+/" subject="Price: 1000 yen"}
{if $matches}
    <p>数値が見つかりました: {$matches.0}</p>
{/if}
{* キャプチャグループを使用 *}
{rcms_match var="result" pattern="/(\d{4})-(\d{2})-(\d{2})/" subject="Date: 2024-01-15"}
{* オフセット位置も取得 *}
{rcms_match var="pos" pattern="/test/" subject="This is a test string" flags=$smarty.const.PREG_OFFSET_CAPTURE}
```

### Notes

- `var` パラメータは必須です。`pattern` は文字列、`subject` はスカラー値である必要があります。最初のマッチのみを返します（すべてのマッチを取得するには `rcms_match_all` を使用）。

---

## rcms_match_all

正規表現で全マッチを取得します（preg_match_all）。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数に以下のいずれかが代入されます: マッチした場合はすべてのマッチ結果の配列、マッチしなかった場合は 0、エラーの場合は false。

### Usage Example

```smarty
{* 基本的な使用例 - すべての数値を取得 *}
{rcms_match_all var="numbers" pattern="/\d+/" subject="価格: 100円, 送料: 500円, 合計: 600円"}
{if $numbers}
    {foreach from=$numbers.0 item=num}
        <p>数値: {$num}</p>
    {/foreach}
{/if}
{* キャプチャグループを使用 *}
{rcms_match_all var="dates" pattern="/(\d{4})-(\d{2})-(\d{2})/" subject="Dates: 2024-01-15, 2024-02-20"}
```

### Notes

- `var` パラメータは必須です。`pattern` は文字列、`subject` はスカラー値である必要があります。`rcms_match` と異なり、すべてのマッチを返します。

---

## pg_dateformat

Format a PostgreSQL date.

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | PostgreSQL date/timestamp |

### Return Value

Formatted date string.

### Usage Example

```smarty
{$date|pg_dateformat:'%Y-%m-%d'}
```

### Notes

- Parses PostgreSQL date/timestamp format
- Format string uses strftime-style placeholders

---

## pg_dateformat2

Format a PostgreSQL date (alternative version).

### Parameters

|-----------|------|----------|---------|-------------|
| (input) | String | Required | - | PostgreSQL date/timestamp |

### Return Value

Formatted date string.

### Usage Example

```smarty
{$date|pg_dateformat2:'Y-m-d'}
```

### Notes

- Alternative implementation of PostgreSQL date formatting
- May use different format string syntax than pg_dateformat

---

## strtodate

タイムスタンプまたは日付文字列をフォーマットして日付を取得します。

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Yes | - | 結果を代入する変数名 |

### Return Value

`var` パラメータで指定した変数にフォーマットされた日付文字列が代入されます。

### Usage Example

```smarty
{* 今日の日付を取得 *}
{strtodate var=today timestamp="today" format="Y-m-d"}
{* 現在時刻を取得 *}
{strtodate var=now format="Y-m-d H:i:s"}
{* タイムスタンプから変換 *}
{strtodate var=date timestamp=1704067200 format="Y年m月d日"}
```

### Notes

- `var` パラメータは必須です。`timestamp` を省略した場合は "now"（現在時刻）が使用されます。`timestamp` が数値の場合はUNIXタイムスタンプ、文字列の場合は `strtotime()` でパースされます。

---

## default

Provide default value for empty variables.

### Parameters

|-----------|------|----------|---------|-------------|
| default | Mixed | Optional | '' | Default value if empty |

### Return Value

Original value or default if empty

### Usage Example

```smarty
{$name|default:"Anonymous"}
{$count|default:0}
{$message|default:"No message"}
```

### Notes

- Considers empty string (`''`) as empty
- Considers unset/null (`!isset()`) as empty
- Zero (`0`), `false`, and other falsy non-empty-string values are NOT considered empty
- Uses strict comparison: `$string === ''`
- Different from PHP's `empty()` function which considers `0` and `false` as empty

---

## strip

Replace all repeated whitespace with a single character.

### Parameters

|-----------|------|----------|---------|-------------|
| replace | String | Optional | ' ' | Replacement string for whitespace sequences |

### Return Value

String with all whitespace sequences replaced

### Usage Example

```smarty
{$text|strip}
{$text|strip:"&nbsp;"}
{"Hello    World"|strip}        {* Hello World *}
{"Line1\nLine2\tLine3"|strip}  {* Line1 Line2 Line3 *}
```

### Notes

- Uses regex pattern `!\s+!` to match one or more whitespace characters
- Replaces spaces, tabs, newlines, carriage returns, form feeds with the replacement string
- Default replaces all whitespace sequences with a single space
- Can use `&nbsp;` for non-breaking space in HTML output

---

## count_characters

Count number of characters in text.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Integer count

### Usage Example

```smarty
{"Hello World"|count_characters}       {* 10 *}
{"Hello World"|count_characters:true}  {* 11 *}
{"Tab\there"|count_characters}         {* 7 - excludes tab *}
```

### Notes

- Default behavior (include_spaces=false): Uses `preg_match_all("/[^\s]/", ...)` to count non-whitespace characters only
- When include_spaces=true: Uses `strlen()` to count all characters including whitespace
- Whitespace characters excluded by default: space, tab, newline, carriage return, form feed, vertical tab
- NOT multibyte-safe - counts bytes, not characters (use with ASCII or single-byte encodings)

---

## count_paragraphs

Count number of paragraphs in text.

### Return Value

Integer count

### Usage Example

```smarty
{$article|count_paragraphs}
{"First paragraph\n\nSecond paragraph"|count_paragraphs}  {* 2 *}
{"Line1\nLine2\nLine3"|count_paragraphs}                  {* 3 *}
{"Single line"|count_paragraphs}                          {* 1 *}
```

### Notes

- Uses `preg_split('/[\r\n]+/', $string)` to split on one or more newline characters
- Counts the resulting array elements
- Counts lines separated by `\r`, `\n`, or `\r\n` (any newline sequence)
- A single line without newlines returns 1
- Empty string returns 1 (array with single empty element)
- Multiple consecutive newlines are treated as a single separator

---

## count_sentences

Count number of sentences in text.

### Return Value

Integer count

### Usage Example

```smarty
{$text|count_sentences}
{"Hello. How are you? I'm fine."|count_sentences}  {* 3 *}
{"Mr. Smith went home."|count_sentences}           {* 1 - "Mr." not counted *}
{"End of line."|count_sentences}                   {* 1 *}
```

### Notes

- Uses pattern `/[^\s]\.(?!\w)/` with `preg_match_all()`
- Pattern requirements: Non-whitespace character immediately before the period, Period, NOT followed by a word character (negative lookahead)
- Ignores abbreviations like "Dr.", "Mr.", "etc." when followed by more text
- Only counts periods, not question marks or exclamation points
- Period at end of string or before whitespace/punctuation is counted

---

## count_words

Count number of words in text.

### Return Value

Integer count

### Usage Example

```smarty
{$text|count_words}
{"Hello world 123"|count_words}     {* 3 *}
{"   spaces   only   "|count_words} {* 2 *}
{"!!!"|count_words}                 {* 0 - no alphanumerics *}
```

### Notes

- First splits text on whitespace using `preg_split('/\s+/', $string)`
- Then filters using `preg_grep('/[a-zA-Z0-9\\x80-\\xff]/', ...)` to count only elements with alphanumerics
- Pattern matches ASCII letters (a-z, A-Z), ASCII digits (0-9), and Extended ASCII / multibyte characters (0x80-0xff)
- Pure punctuation sequences are not counted as words
- Leading/trailing whitespace elements are handled by the split/filter approach

