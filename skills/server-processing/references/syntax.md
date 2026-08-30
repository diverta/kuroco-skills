# Smarty構文リファレンス

KurocoのSmartyテンプレートエンジンの基本構文、制御構造、組み込み変数のリファレンス。

## 概要

KurocoはSmarty 2.6.28をベースとした独自拡張テンプレートエンジン「Smarty_RCMS」を使用。

- **ベースバージョン**: Smarty 2.6.28
- **拡張クラス**: `Smarty_RCMS` (`nfs/lib/core/Smarty_RCMS.php`)
- **テンプレートディレクトリ**: `nfs/templates/`
- **プラグインディレクトリ**:
  - `plugins/` (標準)
  - `plugins/kuroco/` (Kuroco固有)
  - `plugins/rcms/` (RCMS共通)

## 基本構文

### テンプレートタグ

```smarty
{* コメント *}
{$variable}
{$array.key}
{$array[0]}
{$object->property}
```

### 変数の出力

```smarty
{* 基本出力 *}
{$title}

{* エスケープ付き *}
{$title|escape}
{$title|escape:'html'}
{$title|escape:'url'}

{* デフォルト値 *}
{$title|default:'タイトルなし'}
```

### 修飾子（Modifier）

```smarty
{* 単一修飾子 *}
{$text|upper}

{* 複数修飾子のチェーン *}
{$text|strip_tags|truncate:50:'...'}

{* パラメータ付き *}
{$date|date_format:'%Y年%m月%d日'}
{$number|number_format:0:'.':','}
```

### 変数代入

```smarty
{assign var="name" value="値"}
{assign var="array" value=$existingArray}
```

## セキュリティ設定

Smarty_RCMSでは厳格なセキュリティ設定が適用されている。

### 許可されたIF関数 (IF_FUNCS)

```
is_null, NULL, null, false, FALSE, true, TRUE,
count, is_array, in_array, isset, is_object
```

### 許可された修飾子関数 (MODIFIER_FUNCS)

```
pathinfo, http_build_query, htmlspecialchars_decode, escape, nl2br, join,
preg_replace, sprintf, round, wordwrap, number_format, date_format, count,
strip_tags, str_replace, nl2br, substr, array_values, array_keys, array_pop,
trim, ltrim, rtrim, implode, explode, array_unique, json_encode, json_decode,
floor, ceil, array_slice, sort, array_merge, strtotime, ucfirst, strtolower,
strtoupper, array_reverse, intval, floatval, strval, boolval, preg_match,
array_key_exists, array_filter, array_sum, array_column, max, min, abs,
str_pad, substr_count, strlen, mb_strlen, mb_substr, date
```

### セキュリティで無効化されている機能

- PHPタグの直接使用 (`{php}...{/php}`)
- 任意のPHP関数呼び出し
- ファイルシステムへの直接アクセス

## 制御構造

### 条件分岐 (if/elseif/else)

```smarty
{if $user.logged_in}
    ようこそ、{$user.name}さん
{elseif $guest_mode}
    ゲストモードです
{else}
    ログインしてください
{/if}
```

### 比較演算子

| 演算子 | 別名 | 説明 |
|--------|------|------|
| == | eq | 等しい |
| != | ne, neq | 等しくない |
| > | gt | より大きい |
| < | lt | より小さい |
| >= | gte, ge | 以上 |
| <= | lte, le | 以下 |
| === | - | 厳密等価 |
| ! | not | 否定 |
| % | mod | 剰余 |

### 論理演算子

```smarty
{if $a && $b}      {* AND *}
{if $a || $b}      {* OR *}
{if !$a}           {* NOT *}
{if $a and $b}     {* AND (別名) *}
{if $a or $b}      {* OR (別名) *}
```

### ループ (foreach)

```smarty
{foreach from=$items item=item key=key name=loop}
    {$smarty.foreach.loop.index}: {$item.name}
    {if $smarty.foreach.loop.first}最初{/if}
    {if $smarty.foreach.loop.last}最後{/if}
{foreachelse}
    データがありません
{/foreach}
```

### ループ (section)

```smarty
{section name=i loop=$items}
    {$smarty.section.i.index}: {$items[i].name}
{sectionelse}
    データがありません
{/section}
```

### キャプチャ (capture)

```smarty
{capture name=sidebar}
    <div class="sidebar">サイドバーコンテンツ</div>
{/capture}

{* 後で使用 *}
{$smarty.capture.sidebar}
```

### リテラル (literal)

```smarty
{literal}
<script>
    var data = {key: "value"};  // Smartyとして解釈されない
</script>
{/literal}
```

## 組み込み変数

### $smarty変数

| 変数 | 説明 |
|------|------|
| `$smarty.now` | 現在のUNIXタイムスタンプ |
| `$smarty.const.CONSTANT` | PHP定数へのアクセス |
| `$smarty.capture.name` | キャプチャした内容 |
| `$smarty.config.var` | 設定ファイルの変数 |
| `$smarty.section.name.*` | セクションループ変数 |
| `$smarty.foreach.name.*` | foreachループ変数 |
| `$smarty.template` | 現在のテンプレート名 |
| `$smarty.version` | Smartyバージョン |
| `$smarty.ldelim` | 左デリミタ `{` |
| `$smarty.rdelim` | 右デリミタ `}` |

### リクエスト変数

| 変数 | 説明 |
|------|------|
| `$smarty.get.var` | $_GET変数 |
| `$smarty.post.var` | $_POST変数 |
| `$smarty.request.var` | $_REQUEST変数 |
| `$smarty.cookies.var` | $_COOKIE変数 |
| `$smarty.session.var` | $_SESSION変数 |
| `$smarty.server.var` | $_SERVER変数 |
| `$smarty.env.var` | $_ENV変数 |

### foreachループ変数

```smarty
{foreach from=$items item=item name=loop}
    {$smarty.foreach.loop.index}      {* 0から始まるインデックス *}
    {$smarty.foreach.loop.iteration}  {* 1から始まるカウンタ *}
    {$smarty.foreach.loop.first}      {* 最初の要素でtrue *}
    {$smarty.foreach.loop.last}       {* 最後の要素でtrue *}
    {$smarty.foreach.loop.total}      {* 総要素数 *}
{/foreach}
```

## ベストプラクティス

### セキュリティ

```smarty
{* ユーザー入力は必ずエスケープ *}
{$user_input|escape:'html'}

{* URLパラメータのエスケープ *}
<a href="?q={$query|escape:'url'}">検索</a>

{* JavaScript内での使用 *}
<script>
var data = {$json_data|@json_encode};
</script>
```

### パフォーマンス

```smarty
{* キャッシュの活用: {cache}というプラグインは無い。API呼び出し系プラグインの cache_time 引数（分）を使う *}
{api_internal endpoint='/rcms-api/1/sidebar' method='GET' cache_time=60 var='sidebar'}

{* 不要な処理を避ける *}
{if $show_detail}
    {assign_topics_detail var="topics" topics_id=$topics_id}
{/if}
```

### 保守性

```smarty
{* コメントで意図を明確に *}
{* ログイン状態によって表示を切り替え *}
{if $member.member_id}
    {* 会員向けコンテンツ *}
{else}
    {* 非会員向けコンテンツ *}
{/if}

{* 複雑な条件は変数に代入 *}
{assign var="is_premium" value=$member.group_id|in_array:$premium_groups}
{if $is_premium}
    プレミアムコンテンツ
{/if}
```

### よくあるパターン

#### API呼び出しとデータ表示

```smarty
{api_internal endpoint="/rcms-api/1/topics" var="result"}

{if $result.list}
    {foreach from=$result.list item=topic}
        <article>
            <h2>{$topic.subject|escape}</h2>
            <p>{$topic.contents|strip_tags|truncate:100}</p>
        </article>
    {/foreach}
{else}
    <p>記事がありません</p>
{/if}
```

#### 権限による表示制御

`target` は `"アクション:リソースパス"` の順（アクションが先）。アクションのORは `|`、条件全体のORは `||` で連結する。

```smarty
{rcms_auth target="read:/topics/"}
    {* 閲覧権限がある場合のみ表示 *}
    <a href="/topics/">記事一覧</a>
{/rcms_auth}

{rcms_auth target="insert|update:/topics/"}
    {* 作成または更新権限がある場合 *}
    <a href="/topics/edit/">編集</a>
{/rcms_auth}
```

#### 多言語対応

```smarty
{* 翻訳キーの使用 *}
<h1>{'/label/welcome'|translate}</h1>

{* パラメータ付き翻訳 *}
<p>{'/msg/items_found'|translate:$count}</p>
```

#### ファイルアップロード

`file_type` は拡張子のカンマ区切り、`max_file_size` はMB単位。`hidden_nm`（値を格納するhidden inputの名前）と `url`（アップロード先）は必須。

```smarty
{fileupload id="image" hidden_nm="image_url" url=$upload_url file_type="jpg,png,gif" max_file_size=5}
{/fileupload}
```

## プラグイン種別

### 関数プラグイン (Function)

出力を生成または処理を実行する関数。

```smarty
{function_name param1="value1" param2="value2"}
```

### 修飾子プラグイン (Modifier)

変数の値を変換・加工する。パイプ（`|`）で連結可能。

```smarty
{$variable|modifier1|modifier2:param}
```

### ブロックプラグイン (Block)

開始タグと終了タグで囲まれた範囲を処理。

```smarty
{block_name param="value"}
  コンテンツ
{/block_name}
```
