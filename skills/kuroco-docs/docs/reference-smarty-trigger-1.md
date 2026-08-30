# Kurocoドキュメント: リファレンス / Smarty・トリガー・バッチ（1/3）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- KurocoのSmarty基本構文（`basic-syntax-kuroco-smarty`）
- デフォルトのバッチ処理 一覧（`batch-list`）
- Kurocoで利用可能な定数一覧（`constant-variables`）
- メッセージひな形に利用できる変数一覧（`mail-variables`）
- 後処理（`post-processing`）
- 前処理（`pre-processing`）
- KurocoのSmartyで利用可能なPHP関数（`smarty-php-function`）


---

# KurocoのSmarty基本構文

> 元ページ: `reference/basic-syntax-kuroco-smarty` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/basic-syntax-kuroco-smarty/
> 概要: Kurocoのカスタム処理やバッチ処理で使用するSmartyの基本構文について説明します。

Kurocoでは、カスタム処理やバッチ処理のテンプレートエンジンとしてSmartyを使用しています。このドキュメントでは、KurocoのSmarty実装を扱う上で必要な基本的な構文要素について説明します。

## 制御構造

### if/else/elseif文

`{if}`文は条件に基づいた処理の分岐を可能にします。`{else}`と`{elseif}`を使用して複数の条件を処理できます。

**構文**
```smarty
{if 条件}
    条件が真の場合の処理
{elseif 条件2}
    条件2が真の場合の処理
{else}
    すべての条件が偽の場合の処理
{/if}
```

**例**
```smarty
{if $member.status == 'active'}
    おかえりなさい！
{else}
    アカウントが無効です。
{/if}
```

**if文で使用可能なPHP関数**

`{if}`文内で使用できるPHP関数は以下に限定されています。リストにない関数を条件式で呼ぶと、コンパイル時にエラーとなります。

- `is_null()` - 変数がnullかどうかをチェック
- `count()` - 配列の要素数をカウント
- `is_array()` - 変数が配列かどうかをチェック
- `in_array()` - 値が配列内に存在するかチェック
- `isset()` - 変数が宣言されており、nullでないかチェック
- `is_object()` - 変数がオブジェクトかどうかをチェック

なお、`null` / `NULL`、`true` / `TRUE`、`false` / `FALSE` は裸の語として条件式に書けます。これ以外の判定が必要な場合は、事前に `{assign}` やモディファイアで真偽値を計算し、その結果を `{if}` で評価してください。

詳細は[KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)を参照してください。

## ループ構造

### foreach文

`{foreach}`文は、配列やオブジェクトを反復処理します。

**基本構文**
```smarty
{foreach from=$array item="item"}
    {$item}
{/foreach}
```

**インデックス付き**
```smarty
{foreach from=$array item="item" key="key"}
    {$key}: {$item}
{/foreach}
```

**ループカウンター付き**
```smarty
{foreach from=$array item="item" name="loop1"}
    {$item}
    {if !$smarty.foreach.loop1.last}
        ,
    {/if}
{/foreach}
```

**例**
```smarty
{foreach from=$topics_list.list item="topics"}
    {logger msg1=$topics.subject}
{/foreach}
```

**foreachのプロパティ**

`name`属性を使用すると、以下のプロパティにアクセスできます：

- `$smarty.foreach.name.first` - 最初の反復でtrue
- `$smarty.foreach.name.last` - 最後の反復でtrue
- `$smarty.foreach.name.index` - 現在の配列インデックス（0から開始）
- `$smarty.foreach.name.iteration` - 現在の反復回数（1から開始）
- `$smarty.foreach.name.total` - 反復の総数

**複雑な例**
```smarty
{capture name="emailBody"}
{$member.name1} 様

お知らせがあります。
{/capture}

{foreach from=$members item="member" name="memberLoop"}
    {sendmail
        var='result'
        to=$member.email
        subject='お知らせ'
        contents=$smarty.capture.emailBody
        from="noreply@example.com"
        from_nm="システム"}
    {logger msg1="送信完了" msg2=$member.email msg3=$smarty.foreach.memberLoop.iteration}
    {if $smarty.foreach.memberLoop.last}
        {logger msg1="全送信完了" msg2=$smarty.foreach.memberLoop.total}
    {/if}
{/foreach}
```

### section文

`{section}`文は、代替のループ構造です。

**基本構文**
```smarty
{section name="name" loop=$array}
    {$array[name]}
{/section}
```

**例**
```smarty
{section name="i" loop=$topics_list.list}
    {logger msg1=$topics_list.list[i].subject}
{/section}
```

**sectionのプロパティ**

- `$smarty.section.name.first` - 最初の反復でtrue
- `$smarty.section.name.last` - 最後の反復でtrue
- `$smarty.section.name.index` - 現在のインデックス
- `$smarty.section.name.iteration` - 現在の反復回数
- `$smarty.section.name.total` - 反復の総数

### ループ制御

**break**

ループを即座に終了します。

```smarty
{foreach from=$items item="item"}
    {if $item.id == $target_id}
        見つかりました: {$item.name}
        {break}
    {/if}
{/foreach}
```

**continue**

現在の反復で残りのコードをスキップし、次の反復に移動します。

```smarty
{foreach from=$items item="item"}
    {if $item.status == 'draft'}
        {continue}
    {/if}
    {logger msg1=$item.title}
{/foreach}
```

## capture文

`{capture}`文は、出力を表示する代わりに変数にキャプチャします。

**基本構文**
```smarty
{capture name="varname"}
    キャプチャする内容
{/capture}
```

**実用例**
```smarty
{capture name="emailBody"}
{$member.name1} {$member.name2} 様

ご登録ありがとうございます。
会員IDは {$member.member_id} です。

よろしくお願いいたします。
{/capture}

{sendmail
    var='result'
    to=$member.email
    subject='登録完了'
    contents=$smarty.capture.emailBody
    from="noreply@example.com"
    from_nm="システム"}
```

## コメント

**単一行コメント**
```smarty
{* これはコメントです *}
```

**複数行コメント**
```smarty
{*
    これは
    複数行の
    コメントです
*}
```

## 変数

### 変数の呼び出し方

#### シンプルな変数
```smarty
{$variable_name}
```

**例**
```smarty
{assign var="greeting" value="こんにちは、世界！"}
{$greeting}
```

#### 配列要素へのアクセス

ブラケット記法を使用して配列要素にアクセスします。

```smarty
{$array[index]}
{$array['key']}
```

**例**
```smarty
{$topics_list.list[0].subject}
{$topics_list.list[1].ymd}
{$members.list[0].email}
```

#### ハイフンを含むキーへのアクセス

Smartyの識別子（変数名・配列キー）にはハイフン（`-`）を使用できません。これはSmartyの言語仕様によるものです。たとえばドット記法で `$request.load-debug` と記述した場合、`load` から `debug` を減算する式として解釈され、意図したキーにはアクセスできません。

ハイフンを含むキーにアクセスする場合は、ブラケット記法で文字列キーとして指定します。

```smarty
{$request['load-debug']}
```

#### 組み合わせのアクセス例

```smarty
{* ループ内でオブジェクトのプロパティにアクセス *}
{foreach from=$topics_list.list item="topics"}
    {logger msg1=$topics.subject msg2=$topics.ymd}
{/foreach}

{* ネストされたオブジェクトと配列インデックス *}
{logger msg1=$topics_list.list[0].subject msg2=$topics_list.pageInfo.totalCnt}

{* ループカウンターとプロパティの組み合わせ *}
{foreach from=$members.list item="member" name="loop"}
    {logger msg1=$smarty.foreach.loop.iteration msg2=$member.name1 msg3=$member.email}
{/foreach}
```

#### 文字列中での変数展開

文字列の中で変数を展開するには、変数をバッククォート（`` ` ``）で囲みます。

```smarty
{api_internal
    var='topics'
    status_var='status'
    endpoint="/rcms-api/3/topics/details/`$topics_id`"
    method='GET'
    member_id="1"}
```

特に、ダブルクォート文字列の中でその変数に `.`・`[`・`]`・`->` など Smartyが識別子として扱わない文字が含まれている場合は、変数全体をバッククォートで囲む必要があります。囲まないと、ドット記法・ブラケット・アロー演算子の式が文字列中で解析できず、コンパイルエラーになります。これはSmarty標準の「埋め込み変数（embedded variables）」の構文です（[Smartyマニュアル](https://www.smarty.net/docsv2/en/language.variables.tpl) 参照）。

```smarty
{* OK：単純な $ 変数をダブルクォート属性に入れる *}
{assign var="aa" value="$arg"}

{* OK：バッククォートで囲むと文字列中でも完全な式として展開される *}
{assign var="aa" value="`$arg.name`"}
{assign var="aa" value="`$item[0].title`"}
{assign var="aa" value="`$obj->prop`"}

{* OK：クォートを使わず、式を直接値として渡す *}
{assign var="aa" value=$arg.name}

{* NG：ダブルクォート文字列内の .付き変数をバッククォートで囲んでいない
       — Smartyが構文エラーを出してテンプレートのコンパイルに失敗する *}
{assign var="aa" value="$arg.name"}
```

見落とされやすく、AIやエディタの構文ハイライトでも誤読されやすいので、ダブルクォートの属性値の中で `.`・`[]`・`->` を含む変数式を書くときは、必ずバッククォート形式を使ってください。

`"` を含む文字列をアサインするときは、バックスラッシュでエスケープします。バッククォートによる変数展開と組み合わせることもできます。

```smarty
{assign var="email" value="example@diverta.co.jp"}
{assign var="filter" value="from_mail = \"`$email`\" and receive_date >:relatively \"`$from_date`\""}
```

#### 未定義の変数と配列のキー

未定義の変数や未定義の配列のキーにアクセスした場合、`null`として扱われます。

```smarty
{assign_array var="member" values=""}
{append var="member" index="age" value=48}
{if $member.name === null}
    $member.name is null
{else}
    $member.name is not null
{/if}

{if $undefined === null}
    $undefined is null
{else}
    $undefined is not null
{/if}
```

上記の例では、`$member.name`と`$undefined`の両方が`null`として扱われるため、条件分岐により「$member.name is null」と「$undefined is null」が出力されます。

また、未定義の変数のキーにアクセスしようとした場合（例：`{$undefined.attr}`）、未定義の部分で評価が打ち切られ、`null`として扱われます。これはJavaScriptのオプショナルチェーン演算子（`?.`）のように振る舞います。

```smarty
{if $undefined.attr === null}
    $undefined.attr is null
{else}
    $undefined.attr is not null
{/if}
```

上記の例では、`$undefined`が未定義のため、`$undefined.attr`へのアクセスは評価が打ち切られ、`null`として扱われるため、「$undefined.attr is null」が出力されます。

:::caution
この安全な配列アクセスには例外があります。参照を取るタイプのモディファイア（`|@sort`、`|@rsort`、`|@asort`、`|@arsort`、`|@ksort`、`|@krsort`、`|@array_push`、`|@array_pop`、`|@array_shift`、`|@shuffle`）がチェーンの**先頭**に来る場合、この安全装置は**適用されません**。これらを使うときは、変数が定義済みであることを呼び出し側で保証してください。
:::

### 変数の作り方

#### シンプルな代入

`{assign}`を使用して変数を作成または更新します。

```smarty
{assign var="variable_name" value="value"}
```

**例**
```smarty
{assign var="title" value="ようこそ"}
{assign var="count" value=10}
{assign var="price" value=1500}
{assign var="is_active" value=true}
```

**既存の変数を使用**
```smarty
{assign var="full_name" value=$member.name1|cat:" "|cat:$member.name2}
```

#### 配列の作成

`{assign_array}`を使用して配列を作成します。

**空の配列**
```smarty
{assign_array var="my_array" values=""}
```

**値を持つ配列**
```smarty
{assign_array var="fruits" values="apple,banana,orange"}
{assign_array var="numbers" values="1,2,3,4,5"}
```

**カスタム区切り文字**
```smarty
{assign_array var="items" values="item1;item2;item3" delimiter=";"}
```

**連想配列**
```smarty
{assign_array var="person" keys="name,age,email" values="John,25,john@example.com"}
```

#### オブジェクトの作成（連想配列）

`{assign_array}`で空のオブジェクトを作成し、`{append}`でプロパティを追加します。

**基本的なオブジェクト作成**
```smarty
{assign_array var="member" values=""}
{append var="member" index="name" value="山田太郎"}
{append var="member" index="age" value=30}
{append var="member" index="email" value="yamada@example.com"}

{* プロパティへのアクセス *}
{$member.name}
{$member.age}
{$member.email}
```

**ネストされたオブジェクト**

次のようなJSONを作りたいとします。

```json
{
  "name": "山田太郎",
  "address": {
    "city": "東京",
    "zip": "100-0001"
  }
}
```

内側の `address` オブジェクトを先に作成し、外側のオブジェクトに追加します。

```smarty
{* 住所オブジェクトを作成 *}
{assign_array var="address" values=""}
{append var="address" index="city" value="東京"}
{append var="address" index="zip" value="100-0001"}

{* ネストされた住所を持つ人物オブジェクトを作成 *}
{assign_array var="person" values=""}
{append var="person" index="name" value="山田太郎"}
{append var="person" index="address" value=$address}

{* ネストされたプロパティへのアクセス *}
{$person.name}
{$person.address.city}
{$person.address.zip}
```


#### 配列の変更

**要素の追加**
```smarty
{assign_array var="list" values=""}
{append var="list" value="最初の項目"}
{append var="list" value="2番目の項目"}
{append var="list" value="3番目の項目"}
```

Kurocoの独自拡張として、`{assign}`を使用して要素を追加することもできます：

```smarty
{assign_array var="list" values=""}
{assign var="list." value="最初の項目"}
{assign var="list." value="2番目の項目"}
{assign var="list." value="3番目の項目"}
```

**インデックス付きで要素を追加**
```smarty
{assign_array var="settings" values=""}
{append var="settings" index="theme" value="dark"}
{append var="settings" index="language" value="ja"}
{append var="settings" index="notifications" value=true}
```

Kurocoの独自拡張として、`{assign}`を使用してインデックス付きで要素を追加することもできます（ドット記法によるネストは4階層まで対応しています）：

```smarty
{assign_array var="settings" values=""}
{assign var="settings.theme" value="dark"}
{assign var="settings.language" value="ja"}
{assign var="settings.notifications" value=true}
```

#### 実用例：APIリクエストパラメータの構築

```smarty
{* API用のクエリパラメータを作成 *}
{assign_array var="method_params" values=""}
{assign_array var="method_params.topics_group_id" values="1"}

{assign_array var="request_params" values=""}
{assign var="request_params.cnt" value=20}
{assign var="request_params.pageID" value=1}

{api_method
    var="topics_list"
    model="Topics"
    method="list"
    version="1"
    method_params=$method_params
    request_params=$request_params}

{foreach from=$topics_list.list item="topics"}
    {$topics.subject}
{/foreach}
```

#### 配列を作るときのベストプラクティス

Smarty 2には配列リテラルの構文がないため、Kurocoテンプレートでは少数のヘルパープラグインを組み合わせて配列を構築します。データ形状に応じて以下のパターンから選んでください。

##### 1. 初期化してからpush（最も一般的）

定番パターン：[`assign_array`](/ja/docs/reference/smarty-plugin/#assign_array) で空配列を宣言してから、[`append`](/ja/docs/reference/smarty-plugin/#append) で1要素ずつ追加します。Kuroco内のテンプレートで最もよく見られる形です。

```smarty
{assign_array var=items values=""}
{append var=items value="first"}
{append var=items value="second"}
{append var=items value=$dynamic_value}
```

連想配列にしたい場合は `{append}` に `index` を渡します：

```smarty
{assign_array var=person values=""}
{append var=person index="name" value="Katoh"}
{append var=person index="age"  value=28}
```

##### 2. 区切り文字列から一発で生成

静的な値であれば、1つのタグで配列を生成できます：

```smarty
{* リスト *}
{assign_array var=colors values="red,green,blue"}

{* 区切り文字を変更（値にカンマが含まれるとき） *}
{assign_array var=paths values="/a;/b;/c" delimiter=";"}

{* 連想配列（keysとvaluesの個数を一致させる） *}
{assign_array var=opts keys="host,port,ssl" values="example.com,443,true"}
```

##### 3. ドット記法でネスト構造を作る

`{assign}` タグは、変数名にドットを含めることでネスト構造を1ステップで生成できます（4階層まで）：

```smarty
{assign var="user.profile.name" value="Katoh"}
{assign var="user.profile.age"  value=28}
{assign var="user.roles."        value="admin"}   {* 末尾ドットは $user.roles へのpush *}
{assign var="user.roles."        value="editor"}
```

結果:

```
user => Array
    profile => Array (name=Katoh, age=28)
    roles   => Array ("admin", "editor")
```

##### 4. イミュータブル版 — 元の配列を変更しない

`{append}` は `var` を破壊的に更新します。元の配列をそのまま残して別の配列を派生させたい場合は [`assign_array_set`](/ja/docs/reference/smarty-plugin/#assign_array_set) を使用します：

```smarty
{assign_array_set var=updated from=$original key="status" value="done"}
{* $original は変更されず、$updated にだけキーが追加される *}
```

##### パターンの選び方

| 形状 | 推奨パターン |
| :--- | :--- |
| インデックス配列、要素が静的に決まる | `{assign_array values="a,b,c"}` |
| インデックス配列、ループ中に追加する | `{assign_array values=""}` + `{append}` |
| 1階層の連想配列 | `{assign_array keys=... values=...}` または `{append index=...}` |
| ネストした構造（オブジェクト風） | `{assign var="a.b.c" value=...}` のドット記法 |
| 元の配列を保持したまま派生させる | `{assign_array_set}` |

##### 配列に関する注意点

- **配列以外の値に対するインデックスアクセスを当てにしない。** [未定義の変数と配列のキー](#未定義の変数と配列のキー) の挙動により、`{$x[0]}` のアクセスは配列でなくても警告を出さずに `null` を返します。意図しない値を「値あり」と誤読しやすいので、要素アクセスする前に `{assign_array}` で配列として明示的に初期化してください。
- **`{append}` を呼ぶ前に必ず配列として初期化する。** リストを作るときはまず `{assign_array var=foo values=""}` で受け側を配列として確定させてから `{append}` を呼んでください。未初期化の変数やスカラー値が入った変数に `{append}` を行うと、特に `{include}` をまたいだ場合に想定通りの配列にならないことがあります。

## 変数修飾子

変数は、パイプ（`|`）文字を使用して修飾子を適用できます。

**基本構文**
```smarty
{$variable|modifier}
{$variable|modifier:parameter}
{$variable|modifier1|modifier2}
```

**よく使われる例**
```smarty
{* 文字列を切り詰める *}
{$description|truncate:100}

{* 日付のフォーマット *}
{$date|date_format:"Y-m-d"}

{* 数値のフォーマット *}
{$price|number_format}

{* 複数の修飾子 *}
{$text|strip_tags|truncate:50}
```

**配列の修飾子**

配列全体を1つの値として修飾子に渡す場合は `@` を付けます：

```smarty
{* 配列要素数をカウント *}
{$items|@count}

{* 配列の値を取得 *}
{assign var="values" value=$array|@array_values}

{* 配列をソート *}
{assign var="sorted" value=$array|@rcms_sort}

{* JSONエンコード *}
{assign var="json" value=$array|@json_encode}
```

:::info
`@` プレフィックスはSmarty標準の意味（「配列要素ごとに適用」ではなく「配列全体を1つの値として渡す」）であり、Kuroco独自のマーカーではありません。
:::

**モディファイアの2つの系統**

Kuroco テンプレートで利用できるモディファイアには2つの系統があり、どちらに属しているかを意識しておく必要があります。

1. **モディファイアプラグイン** — `modifier.count.php`、`modifier.empty.php`、`modifier.in_array.php`、`modifier.split.php`、`modifier.to_object.php` などのファイル単位で実装されたモディファイアです。PHP 関数の許可リストとは**無関係に動作**します。例: `{$arr|@count}`、`{$user|empty}`、`{$item|to_object}`。利用可能なプラグインの一覧は [Smartyプラグイン](/ja/docs/reference/smarty-plugin/) を参照してください。
2. **PHP 関数の通過呼び出し** — Kuroco の `MODIFIER_FUNCS` 許可リストに含まれる PHP 関数は、専用のプラグインファイルが存在しなくても、そのままモディファイアとして呼び出せます。呼び出しは型検証ラッパーを経由するため、引数の型が関数シグネチャと合わない場合は `null` が返り（バリデーション以外のモードでは Kuroco のエラーパイプライン経由でエラーが通知されます）、PHPのfatalエラーにはなりません。利用可能な関数の一覧は [KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/) を参照してください。

```smarty
{$text|strlen}              {* PHP 関数の通過呼び出し *}
{$arr|@count}               {* modifier.count.php プラグインで処理される *}
{$value|intval}             {* PHP 関数の通過呼び出し *}
```

参照を取る関数（sort、push 等）は、前述の[未定義の変数と配列のキー](#未定義の変数と配列のキー)の安全な配列アクセスの例外と連動します。

**デフォルトモディファイアの抑止（`|smarty:nodefaults` / `|raw`）**

グローバルにデフォルトモディファイアが設定されている環境では、`|smarty:nodefaults`（またはエイリアスの `|raw`）を付けるとその変数だけデフォルト処理を回避できます。

```smarty
{$html_content|raw}              {* デフォルトのエスケープ等を回避 *}
{$untrusted|smarty:nodefaults}   {* 同じ意味 *}
```

## 日付処理

### 日付のフォーマット

`date_format`修飾子を使用して、日付を指定した形式でフォーマットできます。

**基本構文**
```smarty
{$date|date_format:"format"}
```

**例**
```smarty
{$date|date_format:"Y-m-d"}
{$date|date_format:"Y年m月d日"}
{$date|date_format:"H:i:s"}
```

### 日付フォーマット指定子

Kurocoの`date_format`では、PHPの`date()`関数の指定子を使用できます。フォーマット文字列に `%` が含まれている場合、strftime形式のコードをPHPの`date()`用の書式に内部で変換してから整形されます。

#### PHP date()関数の指定子（推奨）

| 指定子 | 説明 | 例 |
|--------|------|-----|
| `Y` | 4桁の年 | 2024 |
| `y` | 2桁の年 | 24 |
| `m` | 月（01-12） | 01, 12 |
| `n` | 月（1-12） | 1, 12 |
| `d` | 日（01-31） | 01, 31 |
| `j` | 日（1-31） | 1, 31 |
| `H` | 時（00-23） | 00, 23 |
| `h` | 時（01-12） | 01, 12 |
| `i` | 分（00-59） | 00, 59 |
| `s` | 秒（00-59） | 00, 59 |
| `w` | 曜日（0-6、0=日曜日） | 0, 6 |
| `D` | 曜日の短縮形 | Mon, Sun |
| `l` | 曜日の完全形 | Monday, Sunday |
| `M` | 月の短縮形 | Jan, Dec |
| `F` | 月の完全形 | January, December |
| `A` | 午前/午後（大文字） | AM, PM |
| `a` | 午前/午後（小文字） | am, pm |

**よく使われるフォーマット例**
```smarty
{* YYYY-MM-DD形式 *}
{$date|date_format:"Y-m-d"}

{* YYYY年MM月DD日形式 *}
{$date|date_format:"Y年m月d日"}

{* YYYY-MM-DD HH:MM:SS形式 *}
{$date|date_format:"Y-m-d H:i:s"}
```

:::tip
`$smarty.now` は現在時刻のタイムスタンプを返します。カスタム処理の先頭に以下のコードを記載すると、月曜日のみ処理が実行されるようになります。

```smarty
{if $smarty.now|date_format:"D" != "Mon"}{return}{/if}
```

月曜日以外に実行された場合は `{return}` で即座に処理を終了するため、バッチ処理のスケジュールを毎日に設定しつつ、実際の処理は月曜日だけに限定する、といった使い方ができます。
:::

#### strftimeの指定子

strftimeの指定子（`%Y`、`%m`、`%d`など）も使用できます。`%` を含むフォーマット文字列は、内部でPHPの`date()`用の書式に自動変換されて処理されます。

### 相対的な日付の処理

PHPの`strtotime`関数を使用して、相対的な日付文字列を処理できます。

**基本構文**
```smarty
{$date_string|strtotime|date_format:"format"}
```

**例**
```smarty
{* 来月の最終日 *}
{assign var="day" value="last day of next month"|strtotime|date_format:"Y-m-d"}
```

## 関数呼び出し

### function文

`{function}`文を使用して、別のカスタム処理を呼び出すことができます。

**基本構文**
```smarty
{function name="function_name" var="result_variable" param1="value1" param2="value2"}
```

呼び出し元と呼び出し先は**別のスコープ**になります。呼び出し先に値を渡すには引数として指定し、結果は`{return}`で返します。

**例**
```smarty
{* 呼び出し元 *}
{function name="send_notification" var="send_result" to=$member.email subject="登録完了" message=$greeting}

{if $send_result}
    メール送信に成功しました
{else}
    メール送信に失敗しました
{/if}
```

詳細は[Smartyプラグイン](/ja/docs/reference/smarty-plugin/#function)を参照してください。

## Kuroco固有のSmarty挙動と制限

### `{php}` ブロックは使用不可

Smarty 2標準の `{php}...{/php}` ブロックや、テンプレート中の生の `<?php ?>` タグは Kuroco では使えません。Kuroco は Smarty をセキュリティモードで動作させており、テンプレートから生のPHPを実行することを許可していません。代わりに、プラグインタグ（`{assign}`、`{assign_array}`、`{append}`、`{api}` など）と、許可リストにある関数呼び出しを利用してください。

### `$smarty.*` のKuroco固有挙動

| 参照 | Kurocoでの挙動 |
| :--- | :--- |
| `$smarty.cookies` | **無効化**。常に `null`。Cookieはサーバー側で読み取ってください。 |
| `$smarty.env` | **無効化**。常に `null`。 |
| `$smarty.server` | 参照可能ですが、`DOCUMENT_ROOT`、`SCRIPT_FILENAME`、`SERVER_SOFTWARE`、`SERVER_ADDR`、`SERVER_PORT`、`REMOTE_PORT`、`REDIRECT_STATUS` などの機密性の高いキーはテンプレートに渡される前に除外されます。それ以外のキーは通常通り参照できます。 |
| `$smarty.rcms_validate` | **Kuroco独自**。テンプレートがバリデーションモードで実行されているときに真値となります。ドライラン実行時に副作用のある処理をスキップする用途で利用します。 |

```smarty
{if !$smarty.rcms_validate}
    {* バリデーション実行中はスキップ *}
    {api endpoint="..." method="POST" var=resp}
{/if}
```

## 関連ドキュメント

- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# デフォルトのバッチ処理 一覧

> 元ページ: `reference/batch-list` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/batch-list/

Kurocoでは以下のバッチ処理がデフォルトで用意されています。バッチ処理が実行されると従量課金のコンピューティングが課金されます。  
実行内容をまとめておりますので従量課金のマネジメントの参考にしてください。  

:::info
実行前のバッチや定期実行のバッチは、[バッチ処理](/ja/docs/management/batch/)画面で確認できます。
:::

## EC
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|ec_process_download|ダウンロード商品の注文があれば、15分毎|ダウンロード商品の売上処理を行い、該当商品のダウンロードに必要な一連の処理を行います。|
|ec_auto_sale_regular|定期購読商品の注文があれば、15分毎|定期購読商品の売上処理を行います。|
|ec_order_expire_cancel|毎日午前3時|支払い期限切れの注文のキャンセルを行います。|
|ec_regular_delivery_download|定期購入ダウンロード商品の注文があれば、毎日午前2時|定期購入ダウンロード商品の売上処理を行います。|
|ec_fix_point|EC > ポイント設定表示後、確定出来る仮ポイントがあれば、毎日午前1時|仮ポイントを確定状態にする。|
|ec_expire_point|EC > ポイント設定表示後、ポイント期限切れのポイントがあれば、毎日午前1時|ポイントを期限切れにする。|

## API
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|cache_update|[APIのメニューリスト](/ja/docs/management/api-list/#メニューリスト)表示後、毎日午前5時<br/>それ以外にもAPIの設定変更時、API設定のキャッシュクリアするボタン押下時<br/> ![Image from Gyazo](https://t.gyazo.com/teams/diverta/f78dcd8665ec2a1c2550e0342d5af836.jpg)にも即時実行されます|API設定キャッシュのクリアを行います。|
|api_exec|APIが非同期でリクエストされた時(非同期呼び出しが許可されているAPIでのみ可能です)<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/5348bee079d6260c03a1ad0479a16a2b.png)|指定されたバッチ処理を実行します。|

## コンテンツ
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|topics_cleanup_update_history|[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#項目説明-1)の、更新履歴を残さないチェックボックスが有効して更新された時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/2012588e08dcce0b381a15b294eecb31.jpg)|コンテンツの更新履歴削除を行います。|
|topics_bulk_postprocess|コンテンツ一括アップロード処理後|コンテンツ一括アップロード処理後に必要な処理を行います。(関連タグ数の再計算など)|
|sync_counter|APIでカウンターをインクリメントした時|カウンター項目の値をコンテンツテーブルに同期する処理を行います。|
|topics_group_settings_postupdate|コンテンツ定義編集更新後|コンテンツ定義編集更新後に必要な処理を行います。(DBのindex再構築など)|
|topics_upload|[コンテンツアップロード](/ja/docs/management/content-structure-topics-csv/#項目説明)の [バッチ処理で実行する]押下時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/88854fc7b28c35696f067d2a05fcaf29.jpg)|コンテンツのアップロードを行います。[バッチ処理で実行する]を選択すると動作します。|
|topics_download|[コンテンツダウンロード](/ja/docs/management/content-structure-topics-csv/#項目説明-1)の[バッチ処理で実行する]押下時及び[バッチ処理でファイルダウンロード実行する]押下時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/23d07398f7ac1f10aba6f7224193bfbf.png)|コンテンツのダウンロードを行います。[バッチ処理で実行]を選択すると動作します。|
|topics_keyword|「キーワード検索にテンプレートを利用する」または「ベクトルデータに変換する」にチェックが入っている場合、1時間毎|キーワードテンプレート / キーワードテンプレート(OpenAI)の内容を元にキーワード検索用のデータを更新する。<br/>OpenAI用キーワード検索を利用する場合には合わせて`ai_embeddings`バッチも即時実行する。|

## マイページ
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|vaddy|[VAddy](/ja/docs/management/vaddy/)の設定を[更新する]ボタンで保存後、毎日午前3時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/8afefb172ab3e40a272cb84fc0243c95.jpg)|外部API vaddyを使用して脆弱性診断を行います。<br/>参考：[VAddyと連携してAPIエンドポイントに対する自動診断を設定する。](/ja/docs/tutorials/integrating-with-vaddy/)|

## メンバー
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|member_provisional_upload|[仮メンバーアップロード](/ja/docs/management/pre-members-upload/)の[バッチ処理で実行する]押下時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cff06fa9b3305c911951d94a3529806.jpg)|仮メンバー一括アップロードを行います。　|
|member_lump|[メンバーアップロード](/ja/docs/management/member-upload/)の[バッチ処理で実行する]押下時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/115bd9cbc4f22a26f82e1f47e7341fe3.jpg)|メンバーのアップロードを行います。[バッチ処理で実行]を選択すると動作します。|
|loginid_remainder_to_user|[メンバー編集](/ja/docs/management/member/#項目説明-1)の、ログイン許可の有効期限が30日前になった時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9e24d916865dfe837ff60669bd8ee31.jpg)| ユーザーのログインID有効期限が1ヶ月前なるとメールで通知を行います。|

## 配信
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|magazine_sendmail_bat|[配信メッセージ編集](/ja/docs/management/notification-message-editor/#配信-メッセージ作成)の、送信設定日時を指定時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/2dfb81a9502df2e8abd7c486654ab133.jpg)|Email編集で送信日時を指定して、送信待ちにすると、その時間でバッチ処理が設定されます。|

## フォーム
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|inquiry_bn_download|フォームの[回答ダウンロード](/ja/docs/management/inquiry-answer/#ダウンロード)で、[CSVのダウンロードリンクを生成する]押下時 [ファイルのダウンロードリンクを生成する]押下時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/6040351af90c10106d01b05b8b6c2fde.png)|回答データのダウンロードリンク生成を行います。|

## バッチ処理
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|openflgSetting|[コンテンツ編集の公開設定](/ja/docs/management/content-structure-topics/#公開設定)で、コンテンツ公開設定日時を指定時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7ea5c57088b6104fcec3bfbd8ad4283.png)|公開日時をもとに、コンテンツの公開非公開設定を行います。コンテンツの公開日時を指定すると、その日時でバッチ処理が設定されます。|

## 承認ワークフロー
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|scheduled_publish|[コンテンツ編集](/ja/docs/management/content-structure-topics/#編集方法)の、承認フロー公開設定日時を指定時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/3e3a1e4e914b26224875277c2a0f78e2.png)|時限設定された承認待ちデータを承認済みにします。|
|approval_alert|[承認ワークフロー基本設定](/ja/docs/management/workflow/#項目説明-1)でメール通知を通知するに設定し、設定したアラート期限日数を過ぎた時<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f041415adffe9a7fdb4e0f30fa48d87e.png)|承認待ちデータがある場合、承認者に承認依頼通知メールを送信します。|

## 外部システム連携
|タイトル|実行タイミング|実行内容|
| :--- | :--- |:--- |
|ai_embeddings|OpenAIの連携設定をした際、1時間毎|各コンテンツのOpenAI向けVectorデータの更新|

## 関連ドキュメント
- [バッチ処理](/ja/docs/management/batch/)
- [バッチテンプレート](/ja/docs/management/batch-template/)
- [バッチログ](/ja/docs/management/batch-log-list/)
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [バッチ処理の実行を指定の日時や週次に設定できますか？](/ja/docs/faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly/)
- [バッチ処理が起動しているか確認することはできますか？](/ja/docs/faq/is-it-possible-to-check-if-a-batch-process-is-running/)


---

# Kurocoで利用可能な定数一覧

> 元ページ: `reference/constant-variables` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/constant-variables/

定数は `$smarty.const.[定数名]` という記法によって呼び出すことができます。
いくつかの定数は定数の設定を追加することで変更が可能です。詳しくは[ユーザー側で設定できる定数](#ユーザー側で設定できる定数)を参照してください。

## 定数一覧

| 定数名 | 説明 |
| :--- | :--- |
| SITE_TITLE | サイトのタイトル |
| SITE_KEY | 登録時に指定したサイトキー |
| ROOT_URL | KurocoフロントのURL |
| ROOT_MNG_URL | Kuroco管理画面のURL | 
| ROOT_API_URL | KurocoAPIのURL|
| ROOT_IMG_URL | KurocoFilesのURL|
| S3BUCKET | 設定されているS3のバケット |
| S3BUCKET_DOMAIN | 設定されているS3リージョンのドメイン |
| SITE_EMAIL | 管理者メール。サイト管理画面で設定できる。 |
| INQUIRY_OPERATE_LIMIT_TYPE_NONE | 問い合わせの「管理画面のアクセス制限」が「制限無し」であることを表す定数 |
| INQUIRY_OPERATE_LIMIT_TYPE_GROUP | 問い合わせの「管理画面のアクセス制限」が「制限有り」であることを表す定数 |
| INQUIRY_OPERATE_LIMIT_TYPE_OWNCONTENTS | 問い合わせの「管理画面のアクセス制限」が「ログインユーザが登録したコンテンツからの問合せしか操作できない」であることを表す定数 |
| INQUIRY_TEXT_FORMAT | 問い合わせ項目の種別が「100文字までの短文」であることを表す整数値 |
| INQUIRY_TEXT_AREA_FORMAT | 問い合わせ項目の種別が「400文字までの長文」であることを表す整数値 |
| INQUIRY_RADIO_BUTTON_FORMAT | 問い合わせ項目の種別が「単一選択(ラジオボタン)」であることを表す整数値 |
| INQUIRY_SELECT_BOX_FORMAT | 問い合わせ項目の種別が「単一選択(セレクトボックス)」であることを表す整数値 |
| INQUIRY_CHECK_BOX_FORMAT | 問い合わせ項目の種別が「複数選択(セレクトボックス)」であることを表す整数値 | 
| INQUIRY_DATE_FORMAT | 問い合わせ項目の種別が「日付」であることを表す整数値 |
| INQUIRY_FILE_FORMAT | 問い合わせ項目の種別が「ファイル」であることを表す整数値 |
| INQUIRY_MATRIX_FORMAT | 問い合わせ項目の種別が「マトリックス」であることを表す整数値 |
| INQUIRY_FILE_GCS_FORMAT | 問い合わせ項目の種別が「GCSファイル」であることを表す整数値 |
| INQUIRY_FILE_S3_FORMAT | 問い合わせ項目の種別が「S3ファイル」であることを表す整数値 |
| GROUP_POLICY_ALLOW | グループのメンバー情報閲覧制限基本方針が「制限なし」であることを表す整数値 |
| GROUP_POLICY_DENY | グループのメンバー情報閲覧制限基本方針が「制限あり」であることを表す整数値 |
| COMMENT_STATUS_RUN | コメントのステータスが「運用中」であることを表す整数値 |
| COMMENT_STATUS_STOP | コメントのステータスが「休止中」であることを表す整数値 |
| MAGAZINE_RUN | 配信のステータスが「運用中」であることを表す整数値 | 
| MAGAZINE_STOP | 配信のステータスが「休止中」であることを表す整数値 |
| MEMBER_CSV_OUTPUT_OFFSET | ダウンロードされるCSVの1ファイルあたりの行数 |
| EC_POINT_STATUS_FIXED | ポイントのステータスが「確定」であることを表す整数値 |
| EC_POINT_STATUS_TEMP | ポイントのステータスが「未確定」であることを表す整数値 |
| EC_POINT_STATUS_EXPIRED | ポイントのステータスが「期限切れ」であることを表す整数値 |
| EC_EXT_GROUP_LOOP | SKU拡張項目数を表す整数値 |
| EC_PAYMENTMETHOD_CREDIT_CARD | 決済方法が「クレジットカード」であることを表す整数値 |
| EC_PAYMENTMETHOD_CONVENIENCE_STORE | 決済方法が「コンビニ決済」であることを表す整数値 |
| EC_PAYMENTMETHOD_MONTHLY | 決済方法が「月次カード」であることを表す整数値 |
| EC_PAYMENTMETHOD_AMAZON_PAYMENT_MONTHLY | 決済方法が「Amazonペイメント(月次)」であることを表す整数値 |
| EC_PAYMENTMETHOD_PAY_EASY | 決済方法が「ATM決済（Pay-easy）」であることを表す整数値 |
| EC_PAYMENTMETHOD_SP_CAREER_SB | 決済方法が「SPキャリア継続決済」であることを表す整数値 |
| EC_WITHDRAW_ON_PURCHASE | 支払いオプションが「月単位支払い＋購入時支払い」であることを表す整数値 |
| EC_SERIAL_CODE_GROUP_TYPE_FREE_CODE | ECのシリアルコードのクーポン値のタイプが「無料コード」に設定されていることを表す値 |
| EC_SERIAL_CODE_GROUP_TYPE_DISCOUNT_CODE | ECのシリアルコードのクーポン値のタイプが「割引コード」に設定されていることを表す値 |
| EC_SERIAL_CODE_DISCOUNT_AMOUNT | ECのシリアルコードのクーポン値のタイプが「値引き額」に設定されていることを表す値 |
| EC_SERIAL_CODE_DISCOUNT_PERCENTAGE | ECのシリアルコードのクーポン値のタイプが「%」に設定されていることを表す値 |
| EC_CONVENI_TYPE_SEVENELEVEN | コンビニエンスストアが「セブンイレブン」であることを表す整数値 |
| EC_CONVENI_TYPE_LAWSON | コンビニエンスストアが「ローソン」であることを表す整数値 |
| EC_CONVENI_TYPE_FAMIMA | コンビニエンスストアが「ファミリーマート」であることを表す整数値 |
| EC_CONVENI_TYPE_SEICOMART | コンビニエンスストアが「セイコーマート」であることを表す整数値 |
| EC_CONVENI_TYPE_CIRCLEK_SUNKUS | コンビニエンスストアが「サークルK・サンクス」であることを表す整数値 |
| EC_CONVENI_TYPE_MINISTOP | コンビニエンスストアが「ミニストップ」であることを表す整数値 |
| EC_CONVENI_TYPE_YAMAZAKI | コンビニエンスストアが「ミニストップ」であることを表す整数値 |
| EC_SPCAREER_TYPE_DOCOMO | キャリアが「ドコモ」であることを表す整数値 |
| EC_SPCAREER_TYPE_AU | キャリアが「au」であることを表す整数値 |
| EC_SPCAREER_TYPE_SOFTBANK | キャリアが「ソフトバンク」であることを表す整数値 |
| EC_EXT_TYPE_TEXT | EC拡張項目の種別が「テキスト」であることを表す整数値 |
| EC_EXT_TYPE_TEXT_AREA | EC拡張項目の種別が「テキストエリア」であることを表す整数値 |
| EC_EXT_TYPE_WYSIWYG | EC拡張項目の種別が「Wysiwyg」であることを表す整数値 |
| EC_EXT_TYPE_SELECT_BOX | EC拡張項目の種別が「単一選択」であることを表す整数値 |
| EC_EXT_TYPE_MULTIPLE_CHOICE_CHECKBOX | EC拡張項目の種別が「複数選択(チェックボックス)」であることを表す整数値 |
| EC_EXT_TYPE_IMAGE | EC拡張項目の種別が「画像」であることを表す整数値 |
| EC_EXT_TYPE_LINK | EC拡張項目の種別が「リンク」であることを表す整数値 |
| EC_EXT_TYPE_DATE | EC拡張項目の種別が「日付フォーマット」であることを表す整数値 |
| EC_EXT_TYPE_TDFK | EC拡張項目の種別が「都道府県」であることを表す整数値 |
| EC_EXT_TYPE_FILE | EC拡張項目の種別が「ファイル」であることを表す整数値 |
| EC_EXT_TYPE_HTML | EC拡張項目の種別が「html」であることを表す整数値 |
| EC_EXT_TYPE_FILEMANGER | EC拡張項目の種別が「ファイルマネージャ」であることを表す整数値 |
| EC_EXT_TYPE_GCSFILE | EC拡張項目の種別が「GCSファイル」であることを表す整数値 |
| DEFAULT_OPEN_TYPE | コンテンツ編集画面で設定されている公開設定の初期値<br/>コンテンツ以外の編集画面で設定されている公開設定の初期値<br/>※デフォルトでは"open"、定数の設定で変更可能です。 |
| DEFAULT_OPEN_TYPE2 | コンテンツ編集画面で設定されている公開設定の初期値 |
| OPEN_TIME_OPTION_INTERVAL | 公開設定で指定できる時刻の選択肢の間隔 |
| LOGIN_URL_FOR_LTD | 制限付きファイルの閲覧時、未ログイン状態だった場合に遷移するログイン画面のURL |
| APPROVALFLOW_APPROVAL_STATUS_1 | 承認ワークフロー上のコンテンツの承認状態が「待機中」であることを表す整数値 |
| APPROVALFLOW_APPROVAL_STATUS_2 | 承認ワークフロー上のコンテンツの承認状態が「承認待ち」であることを表す整数値 |
| APPROVALFLOW_APPROVAL_ALERT_TIME | 承認ワークフローの承認待ちアラートの送信時刻 |
| MAGAZINE_MAIL_UNSENT | 配信メールのステータスが「送信待ち」であることを表す整数値 |
| MAGAZINE_MAIL_SENDING | 配信メールのステータスが「送信中であることを表す整数値 |
| MAGAZINE_MAIL_SENT | 配信メールのステータスが「送信済み」であることを表す整数値 |
| MAGAZINE_MAIL_ROUGH | 配信メールのステータスが「下書き」であることを表す整数値 |
| BATCH_TYPE_EVERYDAY | バッチ処理の種別が「毎日」であることを表す整数値 |
| BATCH_STATUS_UNDONE | バッチ処理の状態が「開始前」であることを表す整数値 |
| BATCH_STATUS_DISABLE | バッチ処理の状態が「無効」であることを表す整数値 |
| BATCH_TYPE_TEMPLATE | バッチ処理の種別が「バッチテンプレート」であることを表す整数値 |
| APPROVALFLOW_MEMBER_TYPE_1 | 承認ワークフローの承認者設定が「グループ」であることを表す整数値 |
| APPROVALFLOW_MEMBER_TYPE_2 | 承認ワークフローの承認者設定が「メンバー」であることを表す整数値 |
| LOGIN_INFO | ログイン画面の文言 |
| RCMS_DATEFORMAT | 日付の書式設定 |
| RCMS_CURRENCY | 使用する通貨単位 |
| RCMS_TIMEZONE | タイムゾーン設定 |
| TAG_MAX_EXTENSION | タグの拡張項目数 |
| TOPICS_CONTENTS_TYPE_CNT | コンテンツに設定できるカテゴリ数の最大値 |
| TOPICS_MAX_EXTENSION | コンテンツに設定できる拡張項目の最大数 | 
| TOPICS_EXT_GROUP_LOOP | コンテンツの拡張項目の繰り返し回数の最大値 | 
| TOPICS_EXT_TYPE_GCSFILE | 記事拡張項目の種別が「GCSファイル」であることを表す整数値 | 
| TOPICS_EXT_TYPE_TEXT | 記事拡張項目の種別が「テキスト」であることを表す整数値 | 
| TOPICS_EXT_TYPE_AUTOCOMPLETE | 記事拡張項目の種別が「テキスト(オートコンプリート)」であることを表す整数値 | 
| TOPICS_EXT_TYPE_SELECT_BOX | 記事拡張項目の種別が「単一選択」であることを表す整数値 | 
| TOPICS_EXT_TYPE_TEXT_AREA | 記事拡張項目の種別が「テキストエリア」であることを表す整数値 | 
| TOPICS_EXT_TYPE_MULTIPLE_CHOICE_CHECKBOX | 記事拡張項目の種別が「複数選択(チェックボックス)」であることを表す整数値 | 
| TOPICS_EXT_TYPE_CSVTABLE | 記事拡張項目の種別が「マスタ形式」であることを表す整数値 | 
| TOPICS_EXT_TYPE_RELATION | 記事拡張項目の種別が「関連情報選択」であることを表す整数値 | 
| TOPICS_EXT_TYPE_DATE | 記事拡張項目の種別が「日付フォーマット」であることを表す整数値 | 
| TOPICS_EXT_TYPE_WYSIWYG | 記事拡張項目の種別が「Wysiwyg」であることを表す整数値 | 
| TOPICS_EXT_TYPE_IMAGE | 記事拡張項目の種別が「画像」であることを表す整数値 | 
| TOPICS_EXT_TYPE_LINK | 記事拡張項目の種別が「リンク」であることを表す整数値 | 
| TOPICS_EXT_TYPE_FILE | 記事拡張項目の種別が「ファイル」であることを表す整数値 | 
| TOPICS_EXT_TYPE_TABLE | 記事拡張項目の種別が「表組み(テーブル)」であることを表す整数値 | 
| TOPICS_EXT_TYPE_LOCATION | 記事拡張項目の種別が「地図」であることを表す整数値 | 
| TOPICS_EXT_TYPE_HTML | 記事拡張項目の種別が「html」であることを表す整数値 | 
| TOPICS_EXT_TYPE_S3FILE | 記事拡張項目の種別が「S3ァイル」であることを表す整数値 | 
| TOPICS_EXT_TYPE_FILEMANGER | 記事拡張項目の種別が「ファイルマネージャ」であることを表す整数値 | 
| RCMS_DEFAULT_TOPICS_MAX_EXTENSION | 記事拡張項目の個数の上限(規定値)を表す整数。サイトごとに独自に設定している場合、この変数の代わりに `TOPICS_MAX_EXTENSION` を使用すること。 | 
| RCMS_DEFAULT_MEMBER_MAX_EXTENSION | メンバー拡張項目の個数の上限(規定値)を表す整数 |
| GEO_REGION | Fastlyのリージョン<br/>※API呼び出しでのみ呼び出し可能 |
| GEO_COUNTRY_CODE | Fastlyの国コード<br/>※API呼び出しでのみ呼び出し可能  |
| GEO_CONN_SPEED | Fastlyの接続速度<br/>※API呼び出しでのみ呼び出し可能  |
| OEM_CURRENCY | 使用する通貨単位<br/>※ダッシュボードのウィジェットでのみ呼び出し可能 |
| RCMS_SESSION_GC_MAXLIFETIME | ログインした状態でのアクセス後、自動的にログアウトされるまでの時間 | 

## PHPのデフォルト定数

[KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)で利用することを目的に、以下の定数が利用可能です。  
これらの定数はKurocoのSmartyで利用可能なPHP関数で利用する目的以外に利用しないでください。  

指定の方法はKurocoの定数と同様に`$smarty.const.[定数名]`となります。  
定数の説明は[PHPのドキュメント](https://www.php.net/manual/ja/string.constants.php)を参照ください。  

- ENT_COMPAT
- ENT_QUOTES
- ENT_NOQUOTES
- ENT_HTML401
- ENT_XML1
- ENT_XHTML
- ENT_HTML5
- JSON_FORCE_OBJECT
- JSON_HEX_QUOT
- JSON_HEX_TAG
- JSON_HEX_AMP
- JSON_HEX_APOS
- JSON_INVALID_UTF8_IGNORE
- JSON_INVALID_UTF8_SUBSTITUTE
- JSON_NUMERIC_CHECK
- JSON_PARTIAL_OUTPUT_ON_ERROR
- JSON_PRESERVE_ZERO_FRACTION
- JSON_PRETTY_PRINT
- JSON_UNESCAPED_LINE_TERMINATORS
- JSON_UNESCAPED_SLASHES
- JSON_UNESCAPED_UNICODE
- JSON_BIGINT_AS_STRING
- FILTER_VALIDATE_BOOLEAN
- FILTER_VALIDATE_BOOL
- FILTER_VALIDATE_DOMAIN
- FILTER_VALIDATE_EMAIL
- FILTER_VALIDATE_FLOAT
- FILTER_VALIDATE_INT
- FILTER_VALIDATE_IP
- FILTER_VALIDATE_MAC
- FILTER_VALIDATE_REGEXP
- FILTER_VALIDATE_URL
- FILTER_SANITIZE_EMAIL
- FILTER_SANITIZE_ENCODED
- FILTER_SANITIZE_ADD_SLASHES
- FILTER_SANITIZE_NUMBER_FLOAT
- FILTER_SANITIZE_NUMBER_INT
- FILTER_SANITIZE_SPECIAL_CHARS
- FILTER_SANITIZE_FULL_SPECIAL_CHARS
- FILTER_SANITIZE_URL
- FILTER_UNSAFE_RAW
- FILTER_FLAG_STRIP_LOW
- FILTER_FLAG_STRIP_HIGH
- FILTER_FLAG_STRIP_BACKTICK
- FILTER_FLAG_ALLOW_FRACTION
- FILTER_FLAG_ALLOW_THOUSAND
- FILTER_FLAG_ALLOW_SCIENTIFIC
- FILTER_FLAG_NO_ENCODE_QUOTES
- FILTER_FLAG_ENCODE_LOW
- FILTER_FLAG_ENCODE_HIGH
- FILTER_FLAG_ENCODE_AMP
- FILTER_NULL_ON_FAILURE
- FILTER_FLAG_ALLOW_OCTAL
- FILTER_FLAG_ALLOW_HEX
- FILTER_FLAG_EMAIL_UNICODE
- FILTER_FLAG_IPV4
- FILTER_FLAG_IPV6
- FILTER_FLAG_NO_PRIV_RANGE
- FILTER_FLAG_NO_RES_RANGE
- FILTER_FLAG_GLOBAL_RANGE
- FILTER_FLAG_SCHEME_REQUIRED
- FILTER_FLAG_HOST_REQUIRED
- FILTER_FLAG_PATH_REQUIRED
- FILTER_FLAG_QUERY_REQUIRED
- FILTER_REQUIRE_SCALAR
- FILTER_REQUIRE_ARRAY
- FILTER_FORCE_ARRAY
- PHP_URL_SCHEME
- PHP_URL_HOST
- PHP_URL_PORT
- PHP_URL_USER
- PHP_URL_PASS
- PHP_URL_PATH
- PHP_URL_QUERY
- PHP_URL_FRAGMENT
- STR_PAD_LEFT
- STR_PAD_RIGHT
- STR_PAD_BOTH

## ユーザー側で設定できる定数
Kurocoで利用できる定数のいくつかは、定数のページで設定をすることでユーザーの任意の値に上書きできます。
これによりKuroco管理画面の動作の変更が可能です。

ここではユーザー側で設定できる定数の一覧を紹介します。

| 定数名 |設定例| 説明 |
| :--- | :--- |:--- |
|DEFAULT_OPEN_TYPE              | `open`, `close`|コンテンツ及びコンテンツ以外の編集画面で設定されるデフォルトの公開設定 |
|LOGIN_URL_FOR_LTD              |`https://www.example.com/`|閲覧権限のないファイルへアクセスした場合のリダイレクト先URL|
|OPEN_TIME_OPTION_INTERVAL      | `5` |公開設定で指定できる時刻の選択肢の間隔 |
|RCMS_API_PREVIEW_TOKEN_LIFESPAN|`864000`|プレビュートークンの有効期限(秒)|
|RETURN_SELF_PAGE_TOPICS_EDIT   |`1`|コンテン更新後に一覧へ遷移せず編集画面にとどまる|
|TWOFACTOR_CODE_EXPIRES         |`300`|Login::login_challenge の2段階認証の機能で送信される認証コードの有効期限(秒)|
|USE_APILIST_UI_V2              |`1`|エンドポイント一覧画面の新UIを適用する|
|USE_OLD_POSTPROCESS_DATEFORMAT |`1`|出力変換リストのRCMS Date Formatを[pg_dateformat2関数](/ja/docs/reference/smarty-plugin/#pg_dateformat2)として使用する|
|STRICT_VALIDATE_EMAIL |`1`|メールアドレスの検証をRFC準拠モードに変更します。|
|OTP_CODE_INTERVAL |`60`|二要素認証コードの再送信が可能になるまでの間隔(秒)|
|REJECT_MFA_LOGIN_IF_SEND_FAILED |`0`|`0`に設定すると、Email/SMSの送信に失敗した場合でも二要素認証コードなしでログインを許可します。デフォルトではログイン失敗となります。|
|USE_SAFE_SVG_TAGS |`1`|有効にすると、HTMLおよびWYSIWYG項目でSVGタグが利用可能になります。サニタイズ処理を維持したまま安全なSVGタグのみを許可するため、「全てのタグを許可する」オプションより安全です。|
|USE_BLOCK_EDITOR_EASY_API |`1`|有効にすると、ブロックエディタのAPIレスポンス形式が簡略化されます。各ブロックが `type` と `value` のキーを持つオブジェクトとして返されるため、レスポンスデータの取り扱いが容易になります。|
{/*
|USE_AI_POSTPROCESS |`1`|有効にすると、コンテンツの追加・更新時にAIによる後処理(AI Post-Processing)が利用可能になります。[コンテンツ定義編集画面](/ja/docs/management/content-structure-topics-group/#ai-post-processing)にAI Post-Processingの設定が表示され、コンテンツの保存後にAIによる自動処理を実行できます。|
*/}
{/*
|BATCH_PHYSICALLY_DELETE_DAYS |削除されたコンテンツの物理削除を実行すまでの日数|
*/}

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？](/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/)
- [「公開設定」の選択肢をデフォルトで「非公開」にできますか？](/ja/docs/faq/can-i-set-the-public-settings-option-to-private-by-default/)
- [APIにアクセス元の国や都道府県を追加する](/ja/docs/tutorials/how-to-add-region-data/)
- [閲覧権限のないファイルへアクセスした場合に任意のページにリダイレクトさせることはできますか？](/ja/docs/faq/is-it-possible-to-redirect-to-any-page-when-accessing-files-in-the-ltd-directory/)
- [プレビュートークンの有効期限を変更できますか](/ja/docs/faq/can-i-change-the-expiration-date-of-the-preview-token/)


---

# メッセージひな形に利用できる変数一覧

> 元ページ: `reference/mail-variables` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/mail-variables/

[メッセージひな形](/ja/docs/management/email-template/)のテンプレートフィールドでは変数を利用できます。  
変数を利用することで、各ユーザーに対し動的にデータを取得できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca7d862687615d8e108f9f97f074c52b.jpg)

利用できる変数はテンプレートにより異なります。
メッセージひな形の識別子に対して利用できる変数をまとめましたので下記参照ください。

![Ima+B87e from Gyazo](https://t.gyazo.com/teams/diverta/418d913a45007ccb8488be6132890c9a.png)

## 承認ワークフロー

<!--未使用のためコメントアウト-->
<!--
### approvalflow/approve_please
|変数名   |説明 |
| :--- | :--- |
| $apply_date | 申請日 |
| $apply_member_nm | 申請者名 |
| $publish_ymdhi | 承認の反映日時 |
| $comment | 更新コメント |
| $ext_columns | 対象モジュール拡張項目 |
| $apply_diff | 未承認で新規追加のものと既存のものの差分 |
| $link | 申請データへのURL |
| $title | 申請データ先タイトル |
| $onetime_link | プレビュー閲覧用の一時更新権限URL |
| $site_url | サイトURI |
| $module_data | 未承認で新規追加のモジュールの詳細 |
-->

### approvalflow/approval_alert
**送信タイミング**  
approval_alertバッチ実行時（1日1回7時実行）
承認ワークフロー基本設定のメール通知でアラート期限を入力している場合に有効になります。

**宛先**  
承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $row.span | 申請されてからの経過日数 |
| $row.link | 編集画面へのURL |
| $row.module_type | モジュールタイプ |
| $row.target_type | ターゲットタイプ |
| $row.langName | 申請言語名 |
| $row.alert_day_span | アラート期限日数 |
| $row.mail_subject | メール件名 |
| $row.mail_body | メール本文 |
| $row.mail_addresses | 通知先メールアドレス |
| $row.module_nm | モジュール名 |
| $row.module_id | モジュールID |
| $row.apply_language | 申請言語 |

### approvalflow/approve_finish
**送信タイミング**  
承認ワークフローの承認完了時

**宛先**  
申請者、ワークフロー承認者、承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $apply_member_id | 申請者メンバーID |
| $apply_member_nm | 申請者名 |
| $apply_date | 申請日 |
| $apply_comment | 申請時コメント |
| $approve_member_id | 最後の承認の承認者ID |
| $approve_member_nm | 最後の承認の承認者名 |
| $approve_date | 最後の承認の承認日 |
| $approve_comment | 最終承認済みデータの承認時コメント |
| $publish_ymdhi | 承認の反映日時 |
| $link | 申請データへのURL |
| $title | 申請データ先タイトル |
| $draft_detail | 下書き詳細 |
| $site_uri | サイトURI |
| $module_data | 未承認で新規追加のモジュールの詳細 |

### approvalflow/approve_reject
**送信タイミング**  
承認ワークフローの差し戻し完了時

**宛先**  
申請者、ワークフロー承認者、承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $apply_member_id | 申請者メンバーID |
| $apply_member_nm | 申請者名 |
| $apply_date | 申請日 |
| $comment | 更新コメント（差し戻し理由） |
| $reject_date | 差し戻し日時 |
| $reject_member_id | 差し戻し実行者のメンバーID |
| $reject_member_nm | 差し戻し実行者名 |
| $draft_id | 下書きID |
| $draft_details | 下書き詳細情報 |
| $link | 申請データへのURL |
| $title | 申請対象タイトル |
| $module_data | モジュールデータ |
| $module_nm | モジュール名 |
| $module_id | モジュールID |
| $publish_ymdhi | 承認の反映日時 |

### approvalflow/approve_reject_phase
**送信タイミング**  
承認ワークフローの中間段階への差し戻し時

**宛先**  
差し戻し先の承認段階の承認者、承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $reject_member_nm | 差し戻し実行者名 |
| $apply_member_nm | 申請者名 |
| $apply_date | 申請日 |
| $publish_ymdhi | 承認の反映日時 |
| $comment | 更新コメント（差し戻し理由） |
| $reject_date | 差し戻し日時 |
| $to_approval_group_nm | 差し戻し先の承認グループ名 |
| $link | 申請データへのURL |
| $title | 申請対象タイトル |
| $onetime_link | フロントエンドの下書きプレビューURL |

:::note
`$onetime_link` は以下の条件をすべて満たす場合のみ値がセットされます。条件を満たさない場合は空になります。
- モジュールが `topics`
- 差し戻し先の承認段階のメンバー設定で「ワンタイムURL通知」が有効な承認者が1人以上いる
:::

### approvalflow/approve_flow_move
**送信タイミング**  
承認ワークフローの別のワークフローへの差し戻し時

**宛先**  
申請者、差し戻し先のワークフロー第1段階の承認者、承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $reject_date | 差し戻し日時 |
| $reject_member_nm | 差し戻し実行者名 |
| $from_flow_nm | 差し戻し元のワークフロー名 |
| $to_flow_nm | 差し戻し先のワークフロー名 |
| $apply_date | 申請日 |
| $publish_ymdhi | 承認の反映日時 |
| $apply_member_nm | 申請者名 |
| $comment | 更新コメント |
| $link | 申請データへのURL |
| $title | 申請対象タイトル |
| $onetime_link | フロントエンドの下書きプレビューURL |

:::note
`$onetime_link` は申請者宛メールでは常に空です。承認者宛メールでは以下の条件をすべて満たす場合のみ値がセットされます。
- モジュールが `topics`
- 差し戻し先ワークフローの第1段階のメンバー設定で「ワンタイムURL通知」が有効な承認者が1人以上いる
:::

### approvalflow/approve_withdraw
**送信タイミング**  
承認ワークフローの申請取り下げ時

**宛先**  
ワークフロー承認者（現在の承認待ち段階）、承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $apply_member_id | 申請者メンバーID |
| $apply_member_nm | 申請者名 |
| $apply_date | 申請日 |
| $comment | 取り下げコメント |
| $withdraw_date | 取り下げ日時 |
| $withdraw_member_nm | 取り下げ実行者名 |
| $publish_ymdhi | 承認の反映日時 |
| $draft_id | 下書きID |
| $draft_details | 下書き詳細情報 |
| $link | 申請データへのURL |
| $title | 申請対象タイトル |
| $module_data | モジュールデータ |
| $module_nm | モジュール名 |
| $module_id | モジュールID |

### approvalflow/scheduled_publish
**送信タイミング**  
承認完了したコンテンツが、承認の反映日時になり承認内容が反映されたタイミング

**宛先**  
申請者、ワークフローの最終承認者、承認ワークフロー基本設定のメール通知宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $apply_member_id | 申請者メンバーID |
| $apply_member_nm | 申請者名 |
| $apply_date | 申請日 |
| $apply_comment | 申請時コメント |
| $approve_comment | 最終承認済みデータの承認時コメント |
| $approve_date | 最後の承認の承認日 |
| $approve_member_id | 最後の承認の承認者ID |
| $approve_member_nm | 最後の承認の承認者名 |
| $publish_ymdhi | 承認の反映日時 |
| $link | 申請データへのURL |
| $title | 申請対象タイトル |
| $module_data | モジュールデータ |
| $module_nm | モジュール名 |
| $module_id | モジュールID |

## EC

### ec/AlertLimitPayment_Conveni
コンビニ振込の料金が、入金締切日のN日前になっても未入金状態の場合に送信されます。

|変数名   |説明 |
| :--- | :--- |
| $order | 注文情報 |
| $orderDetails | 注文詳細情報 |
| $products | 注文した商品の商品情報 |

### ec/NoticeExpirePremiumMembership
有料会員期限期限切れ通知メール  
デフォルト設定では有効期限が切れる30日前に通知されるメールです。

|変数名   |説明 |
| :--- | :--- |
| $name1 | 注文者の姓(注文時) |
| $name2 | 注文者の名(注文時) |
| $email | 注文者のEメールアドレス(注文時) |
| $product_content | 注文の商品一覧 |
| $inquiry_url | 問い合わせページのURL |
| $from_name | サイトのタイトル |

### ec/Membership_Cancel
ユーザーがプレミアム会員登録を解除した時に送信されます。

|変数名   |説明 |
| :--- | :--- |
| $name1 | 注文者の姓(注文時) |
| $name2 | 注文者の名(注文時) |
| $email | 注文者のEメールアドレス(注文時) |
| $product_content | 取り消した注文の商品一覧 |
| $inquiry_url | 問い合わせページのURL |
| $from_name | サイトのタイトル |

### ec/Shipping_guest
管理画面の「売上/配送管理」から商品の発送操作を行ったときにユーザーへ通知されるメール（未ログインユーザー宛）

|変数名   |説明 |
| :--- | :--- |
| $name1 | 注文者の姓(注文時) |
| $name2 | 注文者の名(注文時) |
| $email | 注文者のEメールアドレス(注文時) |
| $product_content | 注文の商品一覧 |
| $inquiry_url | 問い合わせページのURL |
| $from_name | サイトのタイトル |

### ec/Shipping_member
管理画面の「売上/配送管理」から商品の発送操作を行ったときにユーザーへ通知されるメール（ログインユーザー宛）

|変数名   |説明 |
| :--- | :--- |
| $name1 | 注文者の姓(注文時) |
| $name2 | 注文者の名(注文時) |
| $email | 注文者のEメールアドレス(注文時) |
| $product_content | 注文の商品一覧 |
| $order_history_url | 購入履歴のURL |
| $inquiry_url | 問い合わせページのURL |
| $from_name | サイトのタイトル |

## フォーム

### inquiry/inquiry_contact_simple
**条件**  
フォーム基本設定の配信先メールアドレスが「入力内容全て通知」になっており、ZIPパスワードが入力されている場合

**送信タイミング**  
`InquiryMesage::send` のエンドポイントでフォームに回答が追加されたタイミング

**宛先**  
配信先メールアドレスに入力したメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $inquiryHeader | 問い合わせフォームのヘッダ情報 |
| $inquiryHeader.inquiry_name | 問い合わせフォームのタイトル |
| $inquiry_id | 問い合わせフォームのID |
| $parent_inquiry_bn_id | 振り分ける本問い合わせのID |
| $inquiry_bn_id | 問い合わせのID |

### inquiry/inquiry_contact

**条件**  
- フォーム基本設定の配信先メールアドレスが「通知する」になっている場合  
- フォーム基本設定の配信先メールアドレスが「入力内容全て通知」になっており、ZIPパスワードが入力されていない場合

**送信タイミング**  
`InquiryMesage::send` のエンドポイントでフォームに回答が追加されたタイミング

**宛先**  
配信先メールアドレスに入力したメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $file_flg | 添付ファイルがあるなら1を、そうでないなら0をとるフラグ |
| $inquiryHeader | 問い合わせフォームのヘッダ情報 |
| $inquiryHeader.inquiry_name | 問い合わせフォームのタイトル |
| $inquiryHeader.contact_flg | フォーム設定の`配信先メールアドレス`にある「通知しない」、「通知する」、「入力内容全て通知」の設定です<br/> 「入力内容全て通知(INQUIRY_CONTACT_ALL)」が指定された場合、フォームの入力内容をメール中に記載します。 |
| $inquiry_id | 問い合わせフォームのID |
| $parent_inquiry_bn_id | 振り分ける本問い合わせのID |
| $inquiry_bn_id | 問い合わせのID |
| $items | ユーザーの問い合わせ情報<br/> 問い合わせ項目をkeyとし、項目に対する回答内容をvalueとする連想配列 |

## ログイン

### login/reset_password

**送信タイミング**  
- `/management/login/reminder/` のページでパスワードリセットのメール送信時
- `Login::reminder` のエンドポイント使用時

**宛先**  
入力した(POSTした)メールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $url | パスワード設定画面のURL |
| $name | ユーザーの氏名 |
| $login_id | ユーザーのログインID |
| $email | ユーザーのEメールアドレス |
| $temp_pwd | 仮パスワード |
| $token | 認証用トークン<br/>URLのパラメータに設定されます。 |
| $name1 | ユーザーの姓<br/> login/reminderのAPI経由時にのみ設定されます。 |
| $name2 | ユーザーの名<br/> login/reminderのAPI経由時にのみ設定されます。 |
| $member | 対象メンバー情報<br/> login/reminderのAPI経由時にのみ設定されます。 |

<!--未使用のためコメントアウト-->
<!--
### login/login_reminder

**送信タイミング**  
- `/management/login/reminder/` のページでパスワードリセットのメール送信時
- `Login::reminder` のエンドポイント使用時

**備考**  
`login/reset_password` と同じテンプレートを使用します。

**宛先**  
入力した(POSTした)メールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $url | パスワード設定画面のURL |
| $name | ユーザーの氏名 |
| $login_id | ユーザーのログインID |
| $email | ユーザーのEメールアドレス |
| $temp_pwd | 仮パスワード |
| $token | 認証用トークン<br/>URLのパラメータに設定されます。 |
| $name1 | ユーザーの姓 |
| $name2 | ユーザーの名 |
| $member | 対象メンバー情報 |
-->

<!--未使用のためコメントアウト-->
<!--
### login/login_check_mail
### ログイン通知メール
|変数名   |説明 |
| :--- | :--- |
| $row | ユーザー情報 |
| $row.name1 | ユーザーの姓 |
| $row.login_id | ユーザーのログインID |
| $row.email | ユーザーのEメールアドレス |
-->

### login/password_changed

**条件**  
[環境設定]->[サイト管理]で「パスワード変更完了通知メールを送信する」が有効になっている

**送信タイミング**  
- 管理画面のパスワードリマインダー機能でパスワード変更完了時
- `Login::reset_password` のエンドポイントでパスワード変更完了時

**宛先**  
パスワードが変更されたメンバーのメールアドレス宛

**備考**  
管理画面のメンバー編集からパスワード変更した場合や、`Member::update` のエンドポイントでパスワード変更した場合は送信されません。

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $name | ユーザーの氏名 |
| $name1 | ユーザーの姓 |
| $name2 | ユーザーの名 |
| $email | ユーザーのEメールアドレス |
| $member | ユーザーのメンバー情報 |

### login/authentication_code
**条件**  
`Login::login_challenge`のエンドポイントで`twofactor_method=email`を設定

**送信タイミング**  
`Login::login_challenge`のエンドポイントで`email`,`password`による認証が完了したタイミング

**宛先**  
ログインしたメンバーのメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $name1 | ユーザーの姓 |
| $name2 | ユーザーの名 |
| $nickname | ユーザーのニックネーム |
| $code | 認証コード（6桁の英数字） |
| $login_code_duration | 認証コードの有効期間（秒） |
| $login_code_expires | 認証コードの有効期限（Unix timestamp） |

### login/sms_authentication_code
**条件**  
- Twilioと連携済み
- メンバー情報に電話番号が登録済み（日本の携帯電話番号のみ対応）
- `Login::login_challenge`のエンドポイントで`twofactor_method=sms`を設定

**送信タイミング**  
`Login::login_challenge`のエンドポイントで`email`,`password`による認証が完了したタイミング

**宛先**  
ログインしたメンバーの電話番号宛（SMS送信）

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $name1 | ユーザーの姓 |
| $name2 | ユーザーの名 |
| $nickname | ユーザーのニックネーム |
| $code | 認証コード（6桁の英数字） |
| $login_code_duration | 認証コードの有効期間（秒） |
| $login_code_expires | 認証コードの有効期限（Unix timestamp） |

**宛先**  
ログインしたメンバーのメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
-->

## メンバー

### memberregist/invite

**送信タイミング**  
管理画面からのメンバー招待時

**宛先**  
招待者宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $key | 認証用トークン |
| $name1 | 招待者の姓 |
| $name2 | 招待者の名 |
| $message | 招待者からのメッセージ |
| $regist_url | ユーザー本登録画面のURL |
| $basic_auth_id | Basic認証のユーザー名<br/>Basic認証ありのサイトでのみ設定されます。 |
| $basic_auth_pwd | Basic認証のパスワード<br/>Basic認証ありのサイトでのみ設定されます。 |

### member/pre_regist_thanks

**送信タイミング**  
`member/invite` のエンドポイントで、仮メンバーの登録完了時

**宛先**  
仮メンバーのメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $ext_info | APIで設定した追加情報 |
| $email | 仮メンバーのEメールアドレス |
| $preregist_key | 認証用トークン<br/>URLのパラメータに設定されます。 |

<!--未使用のためコメントアウト-->
<!--
### member/loginid_remainder_to_user
ログインIDの有効期限が1ヶ月前になった人へ送信されます。

|変数名   |説明 |
| :--- | :--- |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
-->

### member/regist_thanks

:::info
このテンプレートは登録シーンによってそれぞれ利用出来る変数が異なります。
:::

<!--
#### 招待からの登録時 //があるはず。
-->

#### 管理画面からの登録時（個別登録 / 招待 / CSVアップロード）
**条件**  
[メンバー]->[メンバー詳細設定]->[メール通知]の登録時ユーザー宛を有効にしている

**タイミング**  
管理画面からのメンバー新規登録時（個別登録・招待からの登録・CSVアップロードによる新規登録）

**宛先**  
会員登録が完了したユーザー宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $name | メンバーの氏名 |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
| $email | メンバーのEメールアドレス |
| $member_id | メンバーID |
| $password | パスワード（自動生成時は平文表示、それ以外は「あなたが登録したパスワード」の固定文言） |
| $show_password | パスワード表示フラグ（1: 平文 / 0: 固定文言） |

#### APIからの登録時
**条件**  
`Member::insert`のエンドポイントで`send_email_flg`のパラメータを有効にしている

**タイミング**  
APIからのメンバー登録時

**宛先**  
会員登録が完了したユーザー宛

**利用できる変数** 

|変数名   |説明 |
| :--- | :--- |
| $to_name | メンバーの姓 |
| $name | メンバーの氏名 |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
| $email | メンバーのEメールアドレス |
| $data | フォームデータ |
| $form_data | フォームデータ |
| $member_id | メンバーID |
| $password | パスワード（自動生成時は平文表示、それ以外は「あなたが登録したパスワード」の固定文言） |
| $show_password | パスワード表示フラグ（1: 平文 / 0: 固定文言） |
| $site_title | サイト名 |
| $site_url | サイトのURL |
| $preregist_key | 仮登録キー |

### member/regist_alert

**送信タイミング**  
管理画面から招待を送ったメンバーの会員登録完了時

**宛先**  
招待を送ったユーザー宛

**利用できる変数** 

|変数名   |説明 |
| :--- | :--- |
| $name | メンバーの氏名 |
| $email | メンバーのEメールアドレス |
| $friend_nm | 招待者の氏名 |
| $site_title | サイト名 |
| $site_url | サイトのURL |

### member/complete_delete
**条件**  
[環境設定]->[サイト管理]で退会完了通知が有効になっている

**送信タイミング**  
`Member::delete` のエンドポイントでメンバー削除完了時

**宛先**  
削除されたメンバーのメールアドレス宛

**備考**  
管理画面のメンバー編集からの削除の場合はメール送信されません。

**利用できる変数** 

|変数名   |説明 |
| :--- | :--- |
| $to_name | メンバーの姓 |
| $name | メンバーの氏名 |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
| $email | メンバーのEメールアドレス |
| $site_title | サイト名 |
| $site_url | サイトのURL |

### member/update_thanks
**条件**  
[メンバー]->[メンバー詳細設定]->[メール通知]で、編集時ユーザー宛を有効にしている

**送信タイミング**  
- 管理画面からのメンバー個別編集完了時
- `Member::update`のエンドポイントによるメンバー編集完了時

**備考**  
CSVアップロードおよび`Member::bulk_upsert`のエンドポイントによるメンバー編集時には送信されません。

**宛先**  
編集されたメンバーのメールアドレス宛

|変数名   |説明 |
| :--- | :--- |
| $name | メンバーの氏名 |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
| $email | メンバーのEメールアドレス |
| $password | メンバーのログインパスワード |
| $arrGroup_nm | メンバーの所属するグループのリスト |
| $form_data | フォームデータ |
| $memberExtensionColumns | メンバー拡張情報 |
| $original_data | 更新前の会員情報 |
| $column_diff | 会員情報の差分 |

### memberregist/edit_notice
**条件**  
[メンバー]->[メンバー詳細設定]->[メール通知]で、編集時送信アドレスを通知するにしている

**送信タイミング**  
- 管理画面からのメンバー個別編集完了時
- `Member::update`のエンドポイントによるメンバー編集完了時

**備考**  
CSVアップロードおよび`Member::bulk_upsert`のエンドポイントによるメンバー編集時には送信されません。

**宛先**  
編集時送信アドレスに入力されたメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $name | メンバーの氏名 |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
| $email | メンバーのEメールアドレス |
| $password | メンバーのログインパスワード |
| $arrGroup_nm | メンバーの所属するグループのリスト |
| $form_data | フォームデータ |
| $memberExtensionColumns | メンバー拡張情報 |
| $original_data | 更新前の会員情報 |
| $column_diff | 会員情報の差分 |

<!--未使用のためコメントアウト-->
<!--
### memberregist/mail_receive
会員登録時の空メールに対する返信として送信されます。

|変数名   |説明 |
| :--- | :--- |
| $qs | リンク |
| $se | 認証用トークン<br/>URLのパラメータに設定されます。 |
| $ref | 認証用トークン<br/>URLのパラメータに設定されます。 |
-->

### memberregist/regist_notice
ユーザーが会員登録を完了したとき、管理者に送信されます。

**条件**  
[メンバー]->[メンバー詳細設定]->[メール通知]で、登録時送信アドレスを通知するにしている

**送信タイミング**  
- 管理画面からのメンバーの会員登録完了時(招待・編集・CSVアップロード)
- `Member::update`、`Member::bulk_upsert`のエンドポイントによるメンバー登録完了時

**宛先**  
登録時送信アドレスに入力されたメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $name | メンバーの氏名 |
| $name1 | メンバーの姓 |
| $name2 | メンバーの名 |
| $email | メンバーのEメールアドレス |
| $password | パスワード |
| $arrGroup_nm | メンバーの所属するグループのリスト |
| $form_data | フォームデータ |
| $memberExtensionColumns | メンバー拡張情報 |

<!--未使用のためコメントアウト-->
<!--
## メニュー

### menu/rcms_cant_login_remind
サイトの有効期限が切れる30日前(1ヶ月前)・90日前(3ヶ月前)に管理者へ送信されます。

|変数名   |説明 |
| :--- | :--- |
| $site | サイト情報 |
| $site.name1 | メンバーの姓 |
| $site.name2 | メンバーの名 |
| $site.site_nm | サイト名 |
| $site.site_url | フロントサイトのホスト名 |
| $site.mng_url | 管理サイトのホスト名 |
| $site.cant_login_ymd | サイトの有効期限 |
| $month | 有効期限が切れるまでの月数 |

### menu/notice
コンテンツがお気に入りリストに追加されたとき、通知メールとして送信されます。<br/>
あらかじめ、環境設定 > サイト管理 の 「お気に入り機能メール通知」にチェックが入っている必要があります。

|変数名   |説明 |
| :--- | :--- |
| $bookmark_date | ブックマーク日付 |
| $data | お気に入りに追加されたコンテンツの情報<br/> data_titleはコンテンツのタイトル、data_idはコンテンツのIDを表す |
-->

<!--未使用のためコメントアウト-->
<!--
## Menu

### menu/chatwork

**備考**  
テンプレートファイルは存在しますが、現在のコードベースでは使用されていません。

**利用できる変数**  

| 変数名 | 説明 |
| :--- | :--- |
| $mailfrom | 送信者メールアドレス |
| $mailfrom_nm | 送信者名 |
| $subject | 件名 |
| $contents | メッセージ内容 |

### menu/twilio

**備考**  
テンプレートファイルは存在しますが、現在のコードベースでは使用されていません。

**利用できる変数**  

| 変数名 | 説明 |
| :--- | :--- |
| $contents | メッセージ内容 |

### menu/slack

**備考**  
テンプレートファイルは存在しますが、現在のコードベースでは使用されていません。

**利用できる変数**  

| 変数名 | 説明 |
| :--- | :--- |
| $mailfrom | 送信者メールアドレス |
| $mailfrom_nm | 送信者名 |
| $subject | 件名 |
| $contents | メッセージ内容 |
-->

## 期限付き一時メンバー

### onetime/account
**送信タイミング**  
[メンバー管理]->[期限付き一時メンバー編集]で期限付き一時メンバーの追加、及びパスワードの再生成を行った際

**宛先**  
期限付き一時メンバーのメールアドレス宛

**利用できる変数**  

|変数名   |説明 |
| :--- | :--- |
| $memberInfo | ユーザーのメンバー情報 |
| $message | アカウント発行者からのメッセージ |
| $memberInfo.login_id | ユーザーのアカウントID(ログインID) |
| $memberInfo.login_pwd | ユーザーのログインパスワード |
| $memberInfo.expire | ワンタイムメンバーの有効期限 |

<!--未使用のためコメントアウト-->
<!--
## その他

### rcms_api/rcms_thanks

**備考**  
この識別子はデータベースのフィールド名として存在しますが、メールテンプレートとしては使用されていません。
-->

## 関連ドキュメント
- [メッセージひな形](/ja/docs/management/email-template/)
- [メール送信](/ja/docs/management/inquiry-send-mail/)
- [お礼メールをカスタマイズできますか？](/ja/docs/faq/can-i-customize-my-thank-you-e-mail/)
- [問い合わせのお礼メールに、お客様が入力した内容を転載することはできますか？](/ja/docs/faq/how-do-i-include-inquiry-details-in-the-thankyou-email/)
- [カスタム処理やメッセージひな形でインデントが空白で反映されてしまいます](/ja/docs/faq/indentation-is-reflected-as-spaces-in-custom-functions-or-message-templates/)


---

# 後処理

> 元ページ: `reference/post-processing` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/post-processing/
> 概要: 後処理は、APIエンドポイントのメイン処理が実行された後にエンドポイントの力に対して行われるユーザー定義のカスタム処理です。

後処理は、APIエンドポイントのメイン処理が実行された後にエンドポイントの力に対して行われるユーザー定義のカスタム処理です。  
設定したエンドポイントに対し、アプリケーションに固有の後処理を適用できます。  

:::tip
Post-processingに実装した処理は、API情報(Swagger UI)の画面やOpenAPIのopenapi.jsonファイルに反映されないため、表示されている情報と実際の仕様に差異が生じる可能性もあります。そのため、カスタマイズ箇所の仕様については、[エンドポイントの説明の項目](/ja/docs/reference/endpoint-settings/)に記載することを推奨します。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/712dc9c39f274398ea09960a320c2b16.png)

## 後処理の設定方法
後処理はブロック毎に設定を定義します。
各ブロックは、直前のブロックの実行結果を入力として受け取りながら、定義した順番に実行されます。  

処理ブロックの数に制限はありません。  
[追加する]をクリックすると、新しい空のブロックがシリーズの最後に追加されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/497be3d3af76dcf0c5b3123a62728aa6.png)

:::info
出力許可リストは、他の処理（カスタム処理など）の手前で実行するとSQLなどの内部処理にも効果があります。  
パフォーマンスの向上が期待できますので、可能な場合は出力許可リストを最上位に設定することをお勧めします。
:::

### 後処理の種類
現在、Kurocoは以下の3種類の処理をサポートしています。

| 後処理の種類 | 説明 |
| :--- | :--- |
| 出力許可リスト | ホワイトリスト型のフィルターです。出力に残すフィールドのリストを定義し、他のすべてのフィールドは削除されます。|
| 出力変換リスト | 指定したフィールドに対して、フィールドの削除、キー名の変更、Kurocoで定義済みの関数適用ができます。 |
| カスタム処理 | カスタム処理で独自に記述したプログラムをエンドポイントにリンクさせます。|

それぞれの処理について、以下で詳細を説明します。

### 出力許可リスト
`list` や `details` のAPI は多くの情報を返しますが、その中の特定のフィールドをユーザーから隠したりオプションにしたい場合があります。  

出力許可リストは設定したフィールドのみが返されるようになる、ホワイトリスト型のフィルターとして利用します。
レスポンスとして得たいすべてのフィールドを設定してください。

:::tip
ブラックリスト型のフィルターを適用したい場合は[出力変換リスト](#出力変換リスト)を利用してください。
:::

#### 設定方法

JSON 出力のフィールドへのフルパスを、ルートから順に指定します。配列はスキップして、オブジェクトのみを指定します
(フィルターは、配列内のすべてのオブジェクトに適用されます。)

:::tip
許可リストにフィールドが指定されていない場合やパス名に誤りがある場合、エンドポイントは空のJSONオブジェクトを出力します。
:::

#### 設定例

```json [Original Output]
{
  "list": [
    {
      "subject": "First article",
      "contents": "The contents of the first article",
      "sponsors": ["Company X"]
    },
    {
      "subject": "Second article",
      "contents": "The contents of the second article",
      "sponsors": ["Company Y"]
    }
  ],
  "pageInfo": {
    "totalCnt": 7,
    "pageNo": 1,
    ...
  }
}
```

例えば、上記のAPIレスポンスから、`sponsors`だけを削除したいとします。  
残すフィールドは以下の3つです。

- `list.subject` 
- `list.contents`
- `pageInfo`

以下のように設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4909b580440f3ea39d2e84aea0fbb7e0.png)

:::tip
- ネストされたJSONオブジェクトは必ず `.` で表し、配列はすべて無視します。  
- ワイルドカードで指定する場合は、`list.images-*`のように設定します。
:::

出力許可リストは容易に設定できますが、柔軟性に欠ける場合があります。より詳細なカスタマイズが必要な場合は、[出力変換リスト](#出力変換リスト) や [カスタム処理](#カスタム処理) を利用してください。

### 出力変換リスト
出力変換リストでは、各フィールドに対して処理の内容を設定できます。

[処理を追加する]をクリックすると、特定のフィールドの処理を設定するサブブロックが追加されます。出力変換リストには2種類の[削除]機能があり、右側の[削除する]ボタンは対応するサブブロックの行を削除し、下側の[削除する]ボタンはブロック全体を削除します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ae9a59173a7d7872e9fcab5292be1b3.png)

#### 項目設定

| フィールド | 説明 |
| :--- | :--- |
| フィールド | 対象フィールドのパスは許可リストと同様の方法で指定します。配列をスキップし、ネストされたオブジェクトはドット区切りで指定してください。<br/>フィルタは指定したフィールド内のすべての要素に適用されます。<br/>存在しないフィールドを入力した場合、「名称」に入力した名前の新しいフィールドが作成されます。こちらを利用して、任意の静的データをAPIに簡単に追加することができます。|
| フィールドのコピー・削除 | <ul><li>削除：削除にチェックを入れると、レスポンスから指定したフィールドが削除されます。</li><li>コピー：コピーにチェックを入れて、「名称」を記入すると、指定したフィールドをコピーして、名称に記入したフィールド名で新しいフィールドが作成されます。<br/>元のフィールドと値は保存されます。</li></ul> |
| 名称 | フィールドの新しい名前を指定します。新しいフィールドは、元のフィールドと同じ階層に追加されます。<br/>**注意:** パスの指定はできませんので、ドット記法を使って元のフィールドと異なるネスト構造を設定することはできません。|
| 処理 | フィールドに適用する任意の処理を1つ以上選択します。複数の処理がある場合は、選択した順番に適用されます。各処理の具体的な動作は[変換処理](#変換処理)を参照してください。<br/>[-]をクリックすると処理の削除ができます。|
| 削除 | 対象のサブブロックの行を削除します。 |

#### 変換処理

| 処理名 | 動作 |
| :--- | :--- |
| Null | 元の値をそのままコピーします。 |
| Truncate | 指定した最大文字以下になるよう左から値を切り詰めます。<br/>例：値=`あいうえお`、最大長=3 ⇒ `あいう`<br/>空白のまま (または `0` に設定) にすると、最大長はデフォルトで 10 になります。|
| Trim | 文字列の先頭と末尾からすべてのスペース/タブを削除します。<br/>**注意：** この関数は、値を文字列形式に変換します。|
| Strtotime | PHPの[strtotime関数](https://www.php.net/manual/ja/function.strtotime.php)を値に適用します。|
| Date format | PHPの[data関数](https://www.php.net/manual/ja/function.date.php)を値に適用し、Unixタイムスタンプにフォーマットします。|
| Locale Date Format |値に[pg_dateformat関数](/ja/docs/reference/smarty-plugin/#pg_dateformat)を適用します。|
| Uppercase | すべての文字を、大文字に変換します。 |
| Lowercase | すべての文字を、小文字に変換します。 |
| Sprintf |値にPHPの[sprintf関数](https://www.php.net/manual/ja/function.sprintf.php)を適用します。既存の値が第二引数として使用され、%s やその他の指定子を使ってアクセスすることができます。|
| Nl2br | 文字列内の全ての改行(`\n`, `\r`, `\r\n`) の前に `<br />`を挿入します。htmlにレンダリングするときに便利です。|
| FileSize | 指定されたパスにファイルが存在する場合、そのファイルのバイトサイズを取得します。 |
| ImageSize | 指定されたパスに画像が存在する場合、そのバイトサイズを取得します。 |

#### 設定例

```json [Original Output]
{
  "list": [
    {
      "subject": "First article",
      "contents": "The contents of the first article",
      "sponsors": ["Company X"]
    },
    {
      "subject": "Second article",
      "contents": "The contents of the second article",
      "sponsors": ["Company Y"]
    }
  ],
  "pageInfo": {
    "totalCnt": 7,
    "pageNo": 1,
    ...
  }
}
```

例えば、上記のAPIレスポンスで`subject`の文字列を全て大文字にし、`title` という名称の新しいフィールドを追加したいとします。  
フィールドの設定は以下のようになります。

| 項目 | 設定 |
| :--- | :--- |
| フィールド | `list.subject` |
| フィールドのコピー・削除 | [コピー]をチェックします。 |
| 名称 | `title` |
| 処理 | Uppercase |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9be41b54b69bfc5a01b3c846d7a52369.png)

処理が実行された新しいAPIレスポンスは以下になります。

```json [Filtered Output]
{
"list":
  [
    {
      "subject": "First article",
      "contents": "The contents of the first article",
      "sponsors": [
        "Company X"
      ],
      "title": "FIRST ARTICLE"
    },
    {
      "subject": "Second article",
      "contents": "The contents of the second article",
      "sponsors": [
        "Company Y"
      ],
      "title": "SECOND ARTICLE"
    }
  ],
"pageInfo":
  {
    "totalCnt": 7,
    "pageNo": 1
  }
}
```

### カスタム処理

もし、より複雑な機能を持ちたい場合は、データをどのように変換するかを定義したカスタム処理を作成し、それをエンドポイントにリンクさせる事で対応可能です。

#### カスタム処理の作成

[カスタム処理]を参考に、後処理で利用するカスタム処理を作成してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd5aa3aa781410f063d6234959bfb470.png)
カスタム処理は、他のモジュールで使用されているカスタム処理との混同を避けるため、以下のように設定することをお勧めします。

- あらかじめ後処理用の[カスタム処理カテゴリ](/ja/docs/management/function-category/)を作成し、それを関数のカテゴリとして設定する。
- カスタム関数のタイトルとエンドポイントのパス名を一致させる。

#### カスタム処理を対象のエンドポイントと紐づける

1. 左サイドバーメニューの[API]をクリックし、対象の[エンドポイント一覧画面](/ja/docs/management/api-list)を選択します。
2. リストから対象のエンドポイントを選択し、[後処理]をクリックします。
3. ドロップダウンリストから[カスタム処理]を選択し、カテゴリーを選択して、リスト表示さた他カスタム処理を選択する。
4. [保存]をクリックします

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05085deba926556df84200a11e3675fa.png)

:::caution
選択したカスタム処理が間違っていると、エンドポイントが期待通りに動作しません。カスタム処理を正しくリンクしたことを再確認することをお勧めします。
:::

## 後処理の変数
後処理で利用する変数には、特別な意味を持つ予約語が存在します。これらの変数を利用することで、エンドポイントの挙動をカスタマイズできます。

| 変数名 | 種別 |
| :--- | :--- |
| `$json` | 参照 |
| `$processed_json` | API制御 |
| `$errors` | API制御 |
| `$http_code` | API制御 |


## 参照用の変数
### アサインされた変数
下記の変数は、後処理が動作する時、常にデフォルトでアサインされている参照用の変数です。 

| 変数名 | 型 | 説明 |
| :--- | :--- | :--- |
| `$json` | object | API のオリジナルの JSON 出力 |

### リクエスト変数
後処理内でリクエスト変数を扱うには以下のように記述します。

- GET変数 : `$smarty.get.hoge`
- POST変数 : `$smarty.post.foo`

また、上記をまとめたリクエスト変数も利用可能です。

- リクエスト変数 : `$smarty.request.piyo`

:::info
後処理で$smarty.requestを使用する場合、コンテンツの拡張項目はslugではなく、ext_Xでアサインされることがあります。
:::

## API制御用の変数

| 変数名 | 区分 |型 |説明 |
| :--- | :-- | :-- |:-- |
| `$processed_json` |必須|object|この変数にレスポンスになるJSONの値を代入します。 |
| `$errors` |任意|object|この変数に値を代入すると、エンドポイントがエラーを返します。代入した値はレスポンスのmessage項目になります。 |
| `$http_code` |任意|int|errorsに値が代入されている時、この変数に値を代入すると、元のHTTPコードを上書きします。 |

利用可能なHTTPコードは以下になります。

| コード | 名称 | 意味 |
|---|---|---|
| 400 | Bad Request | クライアントからのリクエストが不正 |
| 401 | Unauthorized | ユーザー認証が無い（未ログイン）ことによるリクエスト失敗 |
| 403 | Forbidden | コンテンツへのアクセス権が無いためにリクエスト失敗（401とは異なりユーザー認証は完了している） |
| 404 | Not Found | 指定されたエンドポイントのコンテンツが存在しないことによるリクエスト失敗 |
| 405 | Method Not Allowed | 許可されていないHTTPメソッドを使用した場合のエラー |
| 406 | Not Acceptable | リクエストの条件に合うレスポンスをサーバーが生成できない場合のエラー |
| 500 | Internal Server Error | クライアントからのリクエストは正しいが、サーバ側でエラーが発生した場合のエラー |

## 困ったときは
後処理が想定通りに動作しない場合は、下記のポイントを確認してください。

- APIの後処理とカスタム処理が関連付いているか
- 関連付いているカスタム処理が正しいか
- 変数名が正しいか
- 変数に格納したデータの形式が正しいか
- カスタム処理の構文が正しいか

## 関連ドキュメント
- [API 後処理](/ja/docs/management/api-postprocessing/)
- [カスタム処理](/ja/docs/management/function/)
- [カスタム処理を利用して、CSV出力されるデータ構造を変更する](/ja/docs/tutorials/how-to-implement-original-function-into-the-postprocess/)
- [前処理](/ja/docs/reference/pre-processing/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# 前処理

> 元ページ: `reference/pre-processing` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/pre-processing/
> 概要: 前処理は、APIエンドポイントのメイン処理が実行される前に呼び出されるユーザー定義のカスタム処理です。設定したエンドポイントに対し、アプリケーションに固有の前処理を適用できます。

前処理は、APIエンドポイントのメイン処理が実行される前に呼び出されるユーザー定義のカスタム処理です。  
設定したエンドポイントに対し、アプリケーションに固有の前処理を適用できます。

:::tip
前処理に実装した処理は、API情報(Swagger UI)の画面やopenapi.jsonファイルに反映されないため、表示されている情報と実際の仕様に差異が生じる可能性もあります。そのため、カスタマイズ箇所の仕様については、エンドポイントのディスクリプションに記載することを推奨します。 
::: 

## 前処理設定方法

前処理は下記手順で動作します。
1. カスタム処理にプログラムを記述
2. カスタム処理をエンドポイント設定と関連付ける

それぞれの設定方法について説明します。

### カスタム処理にプログラムを記述

[カスタム処理画面](/ja/docs/management/function/)にアクセスし、前処理を実装するためのカスタム処理を作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71239de3637a31c0f4d9879690cd2712.png)
他の目的で用意されたカスタム処理との混同を避けるために、下記の規則で設定することを推奨します。

- あらかじめ前処理用のカテゴリを作成しておき、カスタム処理のカテゴリに設定する
- カスタム処理のタイトルをエンドポイントのパス名と合わせる

### カスタム処理をエンドポイント設定と関連付ける
**1. API LIST画面にアクセスする**  

メニューよりAPI名を選択し、[API LIST画面](/ja/docs/management/api-list)にアクセスします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9047c4ed2e94ba65ad357a68d15d341e.png) 

**2. エンドポイントを選択する**  

実装対象のエンドポイントを選択し、[前処理] ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae2bd65d11a934a66afe2df5abc3dbda.png) 

**3. カスタム処理を関連付ける**  

カテゴリとタイトル(コンテンツ)を選択し、前処理のために作成したカスタム処理をエンドポイントに関連付けます。

:::caution
ここで関連付けるカスタム処理を間違えた場合、エンドポイントが想定通りに動作しなくなる可能性があるため、ご注意ください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0771d0d4b100cb24674b9f8c86124f4.png)

## 前処理の変数
前処理で利用する変数には、特別な意味を持つ予約語が存在します。これらの変数を利用することで、エンドポイントの挙動をカスタマイズできます。

| 変数名 | 種別 |
| :--- | :--- |
| $meta | 参照 |
| $url | 参照 |
| $body | 参照 |
| $errors | API制御 |
| $request | API制御 |


## 参照用の変数

下記の変数は、前処理が動作する時、常にデフォルトでアサインされている参照用の変数です。  
エンドポイントの情報や、渡されたリクエスト値を判定するために利用します。

| 変数名 | 用途 |
| :--- | :--- |
| [$meta](#meta) | エンドポイントのメタ情報 |
| [$url](#url) | URLの構成要素 |
| [$body](#body) | リクエスト ボディ |


### $meta

対象エンドポイントのメタ情報を参照するための変数です。

| 変数名 | 型  | 説明|
| :--- | :--- | :--- |
|$meta |object |エンドポイントのすべてのメタ情報|

下記の要素で構成されています。

| キー | 型  | 初期値 | 説明 |
| :--- | :--- | :--- | :--- |
|$meta.content_type | string |  | Content-type |
|$meta.mime | string |  | Content-type |
|$meta.mime.type | string |  | MIME タイプ |
|$meta.mime.subtype | string |  | MIME サブタイプ |
|$meta.output_format | string | "json" | クエリ パラメータに指定された_output_format  <br/> |
|$meta.lang | string | 次の優先度に基づき決定: <br/>[ブラウザの言語設定 > 主言語設定] | クエリ パラメータに指定された_lang |
|$meta.charset | string | "utf8" | クエリ パラメータに指定された_charset |
|$meta.http_code | string | null |  |
|$meta.api_header | object |  | API設定 |
|$meta.post_json | string | GET: null <br/> POST: "{}" | テキスト形式のJSON body |


### $url

クライアントから指定されたURLの構成要素を参照するための変数です。

| 変数名 | 型 | 説明|
| :--- | :--- | :--- |
| $url | object  | エンドポイントのパスとクエリパラメータのデータ |

下記の要素で構成されています。  
このうち、$url.queryについては、$smarty.getと同等の値を含みます。

| キー | 型 | 説明 |
| :--- | :--- | :--- |
| $url.path | string | エンドポイントのパス (クエリ パラメータを除く) |
| $url.query | object | クエリ パラメータを格納した連想配列 |

例) 下記のエンドポイントに対してリクエストを送信した場合、　
`/https://your-api-domain/rcms-api/1/endpoint_name?p1=VALUE1&p2[]=VALUE2_0&p2[]=VALUE2_1&p3[k1]=VALUE3_1&p3[k2]=VALUE3_2`  
$urlには下記値が設定されます。

```json title="$url"
{
  "path": "/rcms-api/1/endpoint_name"
  "query": {
    "p1": "VALUE1",
    "p2": [
        "VALUE2_0",
        "VALUE2_1"
    ],
    "p3": {
        "k1": "VALUE3_1",
        "k2": "VALUE3_2"
    }
  }
}
```
<br/>


### $body

クライアントから送信されたリクエスト ボディを参照するための変数です。  
$smarty.postと同等の値を含みます。

| 変数名 | 型 | 説明|
| :--- | :--- | :--- |
|$body |object | リクエスト ボディ|


## API制御用の変数

下記の変数は、前処理が動作した時点ではまだ宣言されていない変数です。  
これらの値を初期化し、値を入れ込むことで、エンドポイントの挙動を制御します。

| 変数名 | 用途 |
| :--- | :--- |
| [$http_code](#http_code) |HTTPレスポンスコードの制御|
| [$errors](#errors) | エラーの制御 |
| [$request](#request) | リクエスト値の制御 |

:::caution
前処理のカスタム処理内では、これらの変数を用途以外の目的で宣言しないでください。APIエンドポイントが意図しない挙動をする可能性があります。
:::

### $http_code

エンドポイントが出力するHTTPレスポンスコードを制御する為の変数です。

利用可能なHTTPコードは以下になります。

| コード | 名称 | 意味 |
|---|---|---|
| 400 | Bad Request | クライアントからのリクエストが不正 |
| 401 | Unauthorized | ユーザー認証が無い（未ログイン）ことによるリクエスト失敗 |
| 403 | Forbidden | コンテンツへのアクセス権が無いためにリクエスト失敗（401とは異なりユーザー認証は完了している） |
| 404 | Not Found | 指定されたエンドポイントのコンテンツが存在しないことによるリクエスト失敗 |
| 405 | Method Not Allowed | 許可されていないHTTPメソッドを使用した場合のエラー |
| 406 | Not Acceptable | リクエストの条件に合うレスポンスをサーバーが生成できない場合のエラー |
| 500 | Internal Server Error | クライアントからのリクエストは正しいが、サーバ側でエラーが発生した場合のエラー |

**コード サンプル**

```smarty
{if `エラー判定処理`}
  {assign var=http_code value=404}
  {assign_array var=errors values=''}
  {assign var=errors. value='コンテンツが存在しません'}
{/if}
```

### $errors

エンドポイントが出力するエラーを制御するための変数です。

入力値を判定し、結果のエラーメッセージを配列に格納することで、エンドポイントに独自のバリデーション処理を実装できます。

| 変数名 | 型 | 初期値 | 説明|
| :--- | :--- | :--- | :--- |
|$errors |object | null |テキスト配列|

**コード サンプル**

```smarty
{* 空配列で初期化 *}
{assign_array var='errors' values=''}
{* 入力値の判定 *}
{if $smarty.post.key_name === 'VALUE'}
  {* エラーメッセージを配列に追加 *}
  {assign var='errors.' value='エラーが発生しました。'}
{/if}
```
<br/>

**エラーレスポンスの形式**  

| HTTP status code | errors[].code | errors[].message |
| :--- | :--- | :--- |
| 422 | unprocessable_entity | errorsに格納したメッセージ |

```json title="SampleResponse"
// レスポンス サンプル
{
  "errors": [
    {
      "code": "unprocessable_entity",
      "message": "エラーが発生しました。"
    }
  ],
  "x-rcms-request-id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxx"
}
```
<br/>

$errors配列に1以上の要素が含まれる場合、レスポンスの形式は下記のようになります。  
```json title="errors"
[
  {"code": "unprocessable_entity", "message": "errorsに格納したメッセージ"}
]
```
<br/>

$errors配列が複数のエラー要素を含む場合、エラー個数分のオブジェクトが出力されます。
```json title="errors"
[
  {"code": "unprocessable_entity", "message": "エラーメッセージ1"},
  {"code": "unprocessable_entity", "message": "エラーメッセージ2"},
  // ...
]
```
<br/>


### $request
メイン処理に渡すリクエスト値を制御するための変数です。

| 変数名 | 型 | 初期値 | 説明 |
| :--- | :--- | :--- | :--- |
|$request |object | null | メイン処理に渡すリクエストボディ |

この変数に次の形式で値を設定することで、メイン処理に渡すリクエスト値(GET/POST)を追加、または上書きできます。

```smarty
{assign var='request.対象のキー名' value='値'}
```
<br/>

既に指定されているリクエスト値を元に値を設定するためには、以下の参照用変数を利用します。

| 変数名 | 備考 |
| :--- | :--- |
|$url.query | $smarty.get で代替可能 |
|$body | $smarty.post で代替可能 |

**コード サンプル**
```smarty
{* 空配列で初期化 *}
{assign_array var='request' values=''}

{* リクエスト値の有無を判定 *}
{if $url.query.filter}
  {* クエリパラメータの上書き *}
  {assign
    var='request.filter'
    value="`$url.query.filter AND topics_id in [1, 2, 3]"}
{/if}
```
<br/>

## 参考チュートリアル
前処理を利用したチュートリアルページです。
- [APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える](/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/)
- [ログインユーザーの情報でAPIのレスポンスを動的に変更する](/ja/docs/tutorials/change-the-api-response-with-the-logged-in-users-information/)

## 困ったときは
前処理が想定通りに動作しない場合は、下記のポイントを確認してください。
- APIの前処理とカスタム処理が関連付いているか
- 関連付いているカスタム処理が正しいか
- 変数名が正しいか
- 変数に格納したデータの形式が正しいか
- カスタム処理の構文が正しいか

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [カスタム処理を利用して、APIのメイン処理に渡すリクエスト値を書き換える](/ja/docs/tutorials/how-to-overwrite-request-for-api-main-process-by-using-function/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [後処理](/ja/docs/reference/post-processing/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# KurocoのSmartyで利用可能なPHP関数

> 元ページ: `reference/smarty-php-function` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/smarty-php-function/
> 概要: カスタム処理やバッチ処理にてSmartyプラグイン利用できます。変数の修飾子として利用可能なPHP関数をまとめます。

カスタム処理やバッチ処理にてSmartyプラグイン利用できます。
変数の修飾子として利用可能なPHP関数をまとめます。

## 利用可能なPHP関数
### if ステートメント

Kuroco のSmarty利用箇所において、`{if}` ステートメントで使用できる PHP 関数は以下の通りです。

PHP関数名 | 概要
--- | ---
is_null | 変数が null かどうか調べます
count | 配列または Countable オブジェクトに含まれるすべての要素の数を数えます
is_array | 変数が配列かどうかを検査します
in_array | 配列に値があるかチェックします
isset | 変数が宣言されていること、そして null とは異なることを検査します
is_object | 変数がオブジェクトかどうかを検査します

**記載例**  

```smarty
{if is_null($hoge)}
    $hogeはnullです。
{/if}
```

### 修飾子

Kuroco のSmarty利用箇所において、変数の修飾子として使用できる PHP 関数は以下の通りです。

PHP関数名 | 概要
--- | ---
array_column | 入力配列から単一のカラムの値を返します
array_diff | 配列の差（array1 にあって他の配列にない値）を計算します
array_filter | コールバック関数を使用して配列の要素をフィルタリングします
array_key_exists | 指定したキーまたは添字が配列にあるかどうかを調べます
array_keys | 配列のキーすべて、あるいはその一部を返します
array_merge | ひとつまたは複数の配列をマージします
array_pop | 配列の末尾から要素を取り除きます
array_push | 一つ以上の要素を配列の最後に追加します
array_reverse | 要素を逆順にした配列を返します
array_search | 指定した値を配列で検索し、見つかった場合に最初に対応するキーを返します
array_shift | 配列の先頭から要素を一つ取り出します
array_slice | 配列の一部を展開します
array_unique | 配列から重複した値を削除します
array_values | 配列の全ての値を返します
arsort | 連想キーと要素との関係を維持しつつ配列を降順にソートします
asort | 連想キーと要素との関係を維持しつつ配列を昇順にソートします
base64_decode | MIME base64 方式によりエンコードされたデータをデコードします
base64_encode | MIME base64 方式でデータをエンコードします
check_inner_uri | URLがKurocoサイトのホスト（内部URI）かどうかを判定します
defined | 名前を指定して定数が定義されているかどうかを調べます
escape | 指定したタイプで文字列をエスケープします（Smartyのescapeモディファイア）
escapeCSV | CSV出力用に文字列をエスケープします（ロケールに応じた文字コード変換を含む）
explode | 文字列を文字列により分割します
filter_var | 指定したフィルタでデータをフィルタリングします
floatval | 変数の浮動小数点数としての値を取得します
floor | 端数の切り捨て
getCountryFromIP | IPアドレスから国情報を取得します（Kurocoヘルパー）
html_entity_decode | HTML エンティティを対応する文字に変換します
htmlspecialchars_decode | 特殊な HTML エンティティを文字に戻します
http_build_query | URL エンコードされたクエリ文字列を生成します
implode | 配列要素を文字列により連結します
intval | 変数の整数としての値を取得します
is_array | 変数が配列かどうかを検査します
is_numeric | 変数が数字または数値形式の文字列であるかを調べます
json_decode | JSON 文字列をデコードします
json_encode | 値を JSON 形式にして返します
key | 配列からキーを取り出します
krsort | 配列をキーで降順にソートします
ksort | 配列をキーで昇順にソートします
max | 最大値を返します
mb_convert_encoding | ある文字エンコーディングの文字列を、別の文字エンコーディングに変換します
mb_convert_kana | カナを("全角かな"、"半角かな"等に)変換します
mb_strimwidth | 指定した幅で文字列を丸めます
mb_stripos | 大文字小文字を区別せず、 文字列の中で指定した文字列が最初に現れる位置を探します
mb_strlen | 文字列の長さを得ます
mb_strpos | 文字列の中に指定した文字列が最初に現れる位置を見つけます
mb_strwidth | 文字列の幅を返します
mb_substr | 文字列の一部を得ます
md5 | 文字列のmd5ハッシュ値を計算します
min | 最小値を返します
mt_rand | メルセンヌ・ツイスター乱数生成器を介して乱数値を生成します
nl2br | 改行文字の前に HTML の改行タグを挿入します
number_format | 数字を千の位毎にグループ化してフォーマットします
parse_url | URL を解釈し、その構成要素を返します
password_hash | パスワードのハッシュを生成します
password_verify | パスワードがハッシュと一致するかどうかを調べます
pathinfo | ファイルパスに関する情報を返します
property_exists | オブジェクトもしくはクラスにプロパティが存在するかどうかを調べます
range | ある範囲の整数を有する配列を作成します
rawurldecode | URL エンコードされた文字列をデコードします
round | 浮動小数点数を丸めます
rsort | 配列を降順にソートします
shuffle | 配列をシャッフルします
sort | 配列を昇順にソートします
str_pad | 文字列を固定長の他の文字列で埋めます
strip_tags | 文字列から HTML および PHP タグを取り除きます
stripos | 大文字小文字を区別せずに文字列が最初に現れる位置を探します
strlen | 文字列の長さを得ます
strpos |  文字列内の部分文字列が最初に現れる場所を見つけます
strstr | 文字列が最初に現れる位置を見つけます
strtolower | 文字列を小文字にします
strtotime | 英文形式の日付を Unix タイムスタンプに変換します
strtoupper | 文字列を大文字にします
strval | 変数の文字列としての値を取得します
substr | 文字列の一部分を返します
trim | 文字列の先頭および末尾にあるホワイトスペースを取り除きます
unset | 指定した変数の割当を解除します
urlencode | 文字列を URL エンコードします
string_format | `sprintf()` と同じ書式指定文字列で変数をフォーマットします（例：`$topics_id\|string_format:"%06d"` → `000123`）

- 関数の第一引数を変数とし、修飾子として関数名を指定します。第二引数以上の引数は修飾子の後ろにコロン(`:`)区切りで記載してください。
- 変数が配列の場合は、関数名の先頭にアットマーク(`@`)を記載してください。
- 関数に利用するPHPデフォルト定数は[Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/#phpのデフォルト定数)を参照してください。

**記載例 (array_column の場合)**  

```smarty
{* データベースから返ってきたレコードセットの例 *}
{assign_array var="records" values=""}

{assign_array var="record" values=""}
{append var="record" index="id" value=2135}
{append var="record" index="first_name" value="John"}
{append var="record" index="last_name" value="Doe"}
{append var="records" value=$record}

{assign_array var="record" values=""}
{append var="record" index="id" value=3245}
{append var="record" index="first_name" value="Sally"}
{append var="record" index="last_name" value="Smith"}
{append var="records" value=$record}

{assign_array var="record" values=""}
{append var="record" index="id" value=5342}
{append var="record" index="first_name" value="Jane"}
{append var="record" index="last_name" value="Jones"}
{append var="records" value=$record}

{assign_array var="record" values=""}
{append var="record" index="id" value=5623}
{append var="record" index="first_name" value="Peter"}
{append var="record" index="last_name" value="Doe"}
{append var="records" value=$record}

{* 関数の第一引数を変数とし、修飾子として関数名を指定します。第二引数以上の引数は修飾子の後ろにコロン(`:`)区切りで記載します *}
{* 変数が配列の場合は、関数名の先頭にアットマーク(`@`)を記載します *}
{assign var="first_names" value=$records|@array_column:'first_name'}

{$first_names|@debug_print_var}
```

**実行結果**  

```
Array (4)
0 => "John"
1 => "Sally"
2 => "Jane"
3 => "Peter"
```

**記載例 (str_pad の場合)**

```smarty
{assign var=input value="Alien"}
{assign var=output value=$input|str_pad:10:"_":$smarty.const.STR_PAD_BOTH}

{$input|debug_print_var}
{$output|debug_print_var}
```

**実行結果**

```
"Alien"
"__Alien___"
```

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [Smartyのマニュアルはありますか？](/ja/docs/faq/where-can-i-find-the-manual-for-smarty/)
- [Smarty エラーが発生しました。原因を教えてください。](/ja/docs/faq/how-do-i-handle-errors-in-smarty/)
