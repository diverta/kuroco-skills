# Kurocoドキュメント: FAQ / smarty

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Smartyで、7日前の日付を取得することはできますか？（`can-i-obtain-the-date-and-time-stamp-at-different-points-in-smarty`）
- バッチ処理の実行を指定の日時や週次に設定できますか？（`can-i-schedule-batch-processing-at-specific-dates-or-weekly`）
- Iframely自動変換を利用するには？（`how-to-auto-convert-iframes`）
- カスタム処理からKurocoのAPIを呼び出せますか？（`how-to-request-kuroco-api-from-smarty-function`）
- Smartyのマニュアルはありますか？（`where-can-i-find-the-manual-for-smarty`）


---

# Smartyで、7日前の日付を取得することはできますか？

> 元ページ: `faq/can-i-obtain-the-date-and-time-stamp-at-different-points-in-smarty` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-obtain-the-date-and-time-stamp-at-different-points-in-smarty/
> 概要: 可能です。dateのSmartyプラグインを利用してください。

可能です。dateのSmartyプラグインを利用してください。  
 
**7日前**

```
{date var='date' time='-7 day' format='Y/m/d'}
```

**1年前**

```
{date var='date' time='-1 year' format='Y/m/d'}
```
    
**30日後**

```
{date var='date' time='30 day' format='Y/m/d'}
```
 
**今日**

```
{date var='date' time='today' format='Y/m/d'}
```

**現在の日時**

```
{date var='date' time='now' format='Y/m/d H:i:s'}
```

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/#date)


---

# バッチ処理の実行を指定の日時や週次に設定できますか？

> 元ページ: `faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly/
> 概要: バッチ処理の実行タイミングを「毎日」に設定し、dateのSmartyプラグインを使い特定の条件以外は処理をスキップすることで実現できます。

バッチ処理の実行タイミングを「毎日」に設定し、`date`のSmartyプラグインを使って現在の日付や曜日を判定することで、特定の条件に一致しない場合は処理をスキップできます。

以下に設定例を紹介します。

## 毎週月曜日に実行

```smarty
{date var='day_of_week' time='now' format='N'}
{* N: 曜日の数値表現 (1=月曜日, 7=日曜日) *}
{if $day_of_week != 1}
    {* 月曜日以外はスキップ *}
    {return}
{/if}

{* ここに月曜日に実行したい処理を記述 *}
```

`format='N'`は曜日を数値で返します（1=月曜日、2=火曜日、...、7=日曜日）。  
月曜日以外の場合は`{return}`で処理を終了し、月曜日のみ後続の処理が実行されます。

## 毎月1日に実行

```smarty
{date var='day_of_month' time='now' format='d'}
{* d: 日の2桁表現 (01〜31) *}
{if $day_of_month != '01'}
    {* 1日以外はスキップ *}
    {return}
{/if}

{* ここに毎月1日に実行したい処理を記述 *}
```

`format='d'`は日付を2桁の数値で返します（01〜31）。  
1日以外の場合は`{return}`で処理を終了し、毎月1日のみ後続の処理が実行されます。

## 特定の日付のみ実行

```smarty
{date var='today' time='now' format='Y-m-d'}
{if $today != '2026-03-15'}
    {* 指定日付以外はスキップ *}
    {return}
{/if}

{* ここに指定日付に実行したい処理を記述 *}
```

`format='Y-m-d'`は日付を`年-月-日`の形式で返します。  
指定した日付と一致しない場合は`{return}`で処理を終了し、該当日のみ後続の処理が実行されます。

:::tip
複数の日付を指定したい場合は、以下のように条件を組み合わせることもできます。

```smarty
{date var='today' time='now' format='Y-m-d'}
{if $today != '2026-03-15' && $today != '2026-06-01' && $today != '2026-12-25'}
    {return}
{/if}
```
:::

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/#date)
- [バッチ処理が起動しているか確認することはできますか？](/ja/docs/faq/is-it-possible-to-check-if-a-batch-process-is-running/)
- [管理画面マニュアル: バッチ一覧](/ja/docs/management/batch/)


---

# Iframely自動変換を利用するには？

> 元ページ: `faq/how-to-auto-convert-iframes` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-auto-convert-iframes/
> 概要: Kurocoでは<oembed>のタグをIframelyで自動変換して、iframeのコードに自動変換する機能を持っています。

Kurocoでは`<oembed>`のタグをIframelyで自動変換して、iframeのコードに自動変換する機能を持っています。  
通常、Wysiwyg(CKEditor)で付与される`<oembed>`のタグはフロントエンド側で適切なiframeタグに変換するよう実装する必要がありますが、こちらを利用することでWysiwygのInsert Mediaで挿入した外部メディアを容易に表示させることができます。  

## 利用方法
### Kurocoの設定
設定したい[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)の編集画面にて、WYSIWYGの項目設定を開きます。  
下記、「編集」ボタンをクリックしてください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ddfd5317b0f91c54e320d5cf4d277642.png)

項目設定が開きますので、「API出力時にiframelyを利用するコードに自動変換」にチェックをいれて、保存・更新ください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/082a36bc371411217c4881fb66c98531.png)

:::tip
コンテンツ定義編集画面への遷移方法、WYSIWYGの項目設定方法については、以下のドキュメントを参照ください。  
[コンテンツ定義](/ja/docs/management/content-structure-topics-group/#%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E5%AE%9A%E7%BE%A9%E7%B7%A8%E9%9B%86)  
[コンテンツ定義で利用できる拡張項目一覧（WYSIWYG）](/ja/docs/reference/list-of-extra-column-available-on-content/#wysiwyg)
:::

### フロントエンドの設定
利用するページで以下のScriptを読み込んでください。  
`<script async charset="utf-8" src="https://iframely.kuroco-front.app/embed.js?cancel=0" ></script>`

Nuxt.jsの場合は以下のコードで表示の確認が可能です。  

```markup
<template>
  <div v-if="response">
    <h1 class="title">{{ response.details.subject }}</h1>
    <!-- eslint-disable-next-line vue/no-v-html -->
    <div class="post" v-html="response.details.ext_01"></div>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, params }) {
    return {
      response: await $axios.$get(
        `/rcms-api/26/test/253`
      ),
    }
  },
  data() {
    return {
      response: null,
    }
  },
  head() {
    return {
      script: [
        {
          async: true,
          charset: 'utf-8',
          src: 'https://iframely.kuroco-front.app/embed.js?cancel=0',
        },
      ],
    }
  },
}
</script>

<style>
.post figure.media {
  display: block;
}
</style>

```

:::caution
`/rcms-api/26/test/253`の部分はご自身のエンドポイントのURLに変更してください。  
スタイル部分はご自身の環境に合わせて調整ください。
:::

## 利用料金
`https://iframely.kuroco-front.app/api/iframe`へのリクエスト毎にキャッシュされたAPIリクエスト(44円/10,000hit)と同等の課金がされます。  
ただし、Kuroco管理画面からのリクエストについては課金されません。  

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [WYSIWYGエディタに入力されたソースが自動変換されないように出来ますか？](/ja/docs/faq/can-i-prevent-sources-entered-into-the-wysiwyg-editor-from-being-automatically-converted/)


---

# カスタム処理からKurocoのAPIを呼び出せますか？

> 元ページ: `faq/how-to-request-kuroco-api-from-smarty-function` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/
> 概要: カスタム処理からKurocoのAPIを呼び出したい場合は「api_internalプラグインを利用する」と「api_methodプラグインを利用する」の２種類の方法があります。それぞれの対応方法をご説明します。

カスタム処理からKurocoのAPIを呼び出したい場合は、下記2つの方法がございます。

- api_internalプラグインを利用する
- api_methodプラグインを利用する

それぞれの方法について説明します。

## api_internalプラグインを利用する

api_internalプラグインを利用することで、[API](/ja/docs/management/api-list/)画面で設定した任意のエンドポイントを呼び出し、実行結果を取得できます。  
以下に利用方法例を紹介します。

### 例1. GETメソッド (認証なし)

```smarty
{* クエリパラメータ *}
{assign_array var='queries'        values=''}
{assign       var='queries.filter' value='ext_col_01 = "1"'}
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/1/topics'
    method='GET'
    queries=$queries}
```

HTTPリクエストを経由して対象のAPIを呼び出し、`var`で指定した変数にレスポンスをアサインします。

`status_var`で指定した変数には、リクエストの成否がアサインされます。
成功した場合は`1`を、ネットワークエラーなどの要因で失敗した場合には`0`を返します。

上記サンプルコードの実行内容は、次のようなJavaScriptのコードに相当します。エンドポイント `/rcms-api/1/topics` のクエリパラメータに`ext_col_01 = "1"`のfilter条件を指定し、リクエストを送信しています。

```js
let queries = {};
queries.filter = 'ext_col_01 = "1"';

fetch(
  'https://your-site-key.g.kuroco.app/rcms-api/1/topics?' + (new URLSearchParams(queries)).toString(),
  // => https://your-site-key.g.kuroco.app/rcms-api/1/topics?filter=ext_col_01+%3D+%221%22
  {
    method: 'GET',
  }
);
```

:::tip
filterの利用方法については、下記ドキュメントをご参照ください。  
チュートリアル -> [検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)  
リファレンス -> [Filter検索のパラメータ](/ja/docs/reference/filter-query/)  
:::

### 例2. POSTメソッド (認証あり)
```smarty
{* リクエスト ボディ *}
{assign_array var='body'            values=''}
{assign       var='body.subject'    value='Title'}
{assign       var='body.ext_col_01' value='2'}

{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/2/topics/insert'
    method='POST'
    queries=$body
    use_current_session=1}
```
`use_current_session=1`を渡すと、現在ログインしているメンバーが認証された状態でリクエストを実行できます。特定のメンバーとして実行する場合は、`member_id`パラメータに数値を直接指定します。  

:::caution
`member_id`パラメータを指定できるのは、対象のAPIの認証方式が「動的アクセストークン」に設定されている場合に限ります。利用する場合は、内部処理用のAPIを別途作成することを推奨します。  
動的アクセストークンについては、[APIセキュリティ -> 動的アクセストークン](/ja/docs/management/api-security/#動的アクセストークン) をご確認ください。
:::

:::caution
`member_id`に変数や定数（`$smarty.session.member_id`など）を指定したカスタム処理は、スーパーユーザー以外は保存・テスト実行ができません。また、スーパーユーザーのメンバーIDは指定できません。ログイン中のメンバーとして実行する場合は`use_current_session=1`を利用してください。
:::

上記サンプルコードの実行内容は、次のようなJavaScriptのコードに相当します。

```js
let body = {};
body.subject = 'Title';
body.ext_col_01 = '2';

fetch(
  'https://your-site-key.g.kuroco.app/rcms-api/2/topics/insert',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      // 指定したmember_idを元にアクセストークンを生成し、自動的に付与します
      'X-RCMS-API-ACCESS-TOKEN': '********',
    },
    body: JSON.stringify(body),
  }
);
```

### 例3. GETメソッド (サーバー上での直接実行)

```smarty
{assign_array var='queries'        values=''}
{assign       var='queries.filter' value='ext_col_01 = "1"'}
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/1/topics'
    method='GET'
    queries=$queries
    direct=1}
```

例1・例2の処理はHTTPリクエストを経由して対象のエンドポイントを呼び出します。しかしながら、ネットワークの状況によっては以下の問題が発生する可能性もあります。
- 結果の取得に時間がかかる
- 結果の取得に失敗する

そこで、`direct=1`をパラメータに指定すると、HTTPリクエストを経由せずサーバー上で直接エンドポイントの処理を実行できます。  
安定して結果を取得できるのが利点ですが、レスポンスのキャッシュが効かないため、利用料金を考慮の上ご利用ください。

:::caution
`direct=1`をパラメータに指定できるのは、対象エンドポイントのHTTPメソッドがGETの場合に限ります。また、member_idの指定はできません。
:::

### 例4. GETメソッド (セッション状態を引き継いだリクエスト)

```smarty
{* クエリパラメータ *}
{assign_session key='my_session_name' value=true}

{assign_array var='queries'        values=''}
{assign       var='queries.filter' value='ext_col_01 = "1"'}
{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/1/topics'
    method='GET'
    queries=$queries
    direct=1
    use_current_session=1}
```

通常であれば、api_internalプラグインの呼び出し元と呼び出し先では別々のセッションが生成されます。  
しかしながら、`direct=1`と`use_current_session=1`を同時に指定すると、呼び出し元のセッションを引き継いだまま対象エンドポイントの処理を実行できます。  
そのため、ログイン状態を引き継いだまま直接実行をしたい場合や、assign_sessionプラグインを利用して独自のセッション変数を管理するような場合に有効です。

呼び出し先のエンドポイントの前処理、または後処理に以下の記述をすることで、呼び出し元とセッション状態が同一であることを確認できます。

```smarty
{* $my_session_value に呼び出し元で設定したセッションがアサインされます *}
{assign_session var='my_session_value' key='my_session_name'}

{* 呼び出し元のログイン状態が引き継がれます *}
{assign var='member_id' value=$smarty.session.member_id}
```

## api_methodプラグインを利用する

api_methodプラグインを利用した場合、エンドポイントを作成せずにAPIの機能を直接呼び出すことができます。

api_internalプラグインを`direct=1`パラメータ付きで呼び出した場合と同様、HTTPリクエストを経由せずにサーバー上で処理を実行します。呼び出したAPI機能は、呼び出し元と同じセッション状態を自動的に引き継ぎます。

:::caution
api_methodで呼び出せるのは、対象機能のHTTPメソッドがGETの場合に限ります。例えば、Topicsのlistやdetailsは呼び出せますが、insertやupdateは呼び出せません。POSTメソッドを実行する必要がある場合は、予めエンドポイントを作成し、api_internalプラグインを経由して呼び出してください。
:::

### api_methodプラグイン利用例

```smarty
{*  エンドポイント設定パラメータ *}
{assign_array var='method_params'                 values=''}
{assign_array var='method_params.topics_group_id' values='1'}
{assign       var='method_params.cnt'             value=10}
{* クエリパラメータ *}
{assign_array var='request_params'        values=''}
{assign       var='request_params.filter' value='ext_col_01 = "1"'}
{api_method
    var='topics'
    model='Topics'
    method='list'
    version='1'
    method_params=$method_params
    request_params=$request_params}
```

`var`で指定した変数に実行結果がアサインされます。

上記の例で`$topics`変数にアサインされるデータは、[API](/ja/docs/management/api-list/)画面で次のようなエンドポイントを設定し、リクエストを実行した場合の結果と同一になります。

**エンドポイント設定**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/97dae826de17d2488d499afb6d3c006e.jpg)

**リクエスト**

```js
fetch(
  "https://your-site-key.g.kuroco.app/rcms-api/{api_id}/topics?filter=" + encodeURIComponent('ext_col_01 = "1"'),
  {
    "method": "GET",
  }
);
```

Topics::details と同じレスポンスを取得する場合は以下のようになります。

```smarty
{assign_array var='method_params'           values=''}
{assign       var='method_params.ext_group' value=true}
{assign       var='method_params.topics_id' value=1234}
{api_method
    var='topics_details'
    model='Topics'
    method='details'
    version='1'
    method_params=$method_params}
```

## api_internalプラグインとapi_methodプラグインの使い分けについて

api_internalプラグインは既存のエンドポイントを呼び出す必要があり、api_methodプラグインはその必要がありません。

そのため、既存のエンドポイントを再利用したい場合は**api_internal**を、エンドポイントを利用する必要がない場合は**api_method**を利用することを推奨いたします。

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# Smartyのマニュアルはありますか？

> 元ページ: `faq/where-can-i-find-the-manual-for-smarty` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/where-can-i-find-the-manual-for-smarty/
> 概要: Smartyについては、[Smartyマニュアル]をご参照ください。

Smartyについては、[Smartyマニュアル](https://www.smarty.net/docsv2/ja/)をご参照ください。  

:::caution
セキュリティの問題等でKurocoでは利用できない場合もございます。
:::

Kurocoの独自のタグに関しては以下にドキュメントを配置しますので、こちらをご確認ください。
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)

## 関連ドキュメント
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)
- [カスタム処理](/ja/docs/management/function/)
- [Smarty エラーが発生しました。原因を教えてください。](/ja/docs/faq/how-do-i-handle-errors-in-smarty/)
