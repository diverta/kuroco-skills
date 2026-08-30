# Kurocoドキュメント: FAQ / admin

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- コンテンツ編集画面に公開URLを開くボタンを追加できますか？（`can-i-add-a-button-to-open-the-public-url-from-the-content-edit-screen`）
- 管理画面の見た目をカスタマイズできますか？（`can-i-adjust-the-appearance-of-the-admin-panel`）
- 親サイトの変更はできますか？（`can-i-change-parent-site`）
- カスタムテンプレートの使い方を教えてください。（`can-i-customize-the-display-of-tables-on-the-conten-editing-screen`）
- コンテンツ編集画面の表示を変更できますか？（`can-i-modify-the-display-of-the-content-editor-screen`）
- Kurocofrontでプレビュー用のページを出力できますか？（`can-i-output-a-preview-page-with-kurocofront`）
- Internet Explorer11で管理画面を利用できますか？（`can-i-use-the-admin-panel-with-internet-explorer-11`）
- スーパーユーザーはサブサイトにもログインできますか？（`can-superuser-also-log-in-to-sub-sites`）
- Kurocoに登録したコンテンツを複数のサイトから利用できますか（`can-the-content-registered-in-kuroco-be-used-from-multiple-sites`）
- 日付は、和暦と西暦のどちらで管理していますか？（`does-kuroco-use-the-japanese-or-western-calendar-system`）
- 管理画面の言語はどこで変更できますか？（`how-do-i-change-the-language-of-the-admin-panel`）
- 管理画面トップページのウィジェットを編集できますか（`how-do-i-edit-the-widget-at-the-top-of-the-administration-screen`）
- 管理画面プラグインでCSSを複数ページに適用することはできますか？（`is-it-possible-to-apply-css-to-multiple-pages-using-the-admin-panel-plugin`）
- 管理画面の推奨環境を教えてください（`what-environments-do-you-recommend-for-the-admin-panel`）
- ログイン履歴の記録ロジックに関して教えてください（`what-is-the-logic-behind-the-login-history`）


---

# コンテンツ編集画面に公開URLを開くボタンを追加できますか？

> 元ページ: `faq/can-i-add-a-button-to-open-the-public-url-from-the-content-edit-screen` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-add-a-button-to-open-the-public-url-from-the-content-edit-screen/
> 概要: コンテンツ定義詳細設定のJavaScript、もしくは項目設定カスタムテンプレートで設定可能です。設定例は以下を参照してください。

コンテンツ定義詳細設定のJavaScript、もしくは項目設定カスタムテンプレートで設定可能です。
設定例は以下を参照してください。

## JavaScript
[コンテンツ定義]->[詳細設定]のJavaScript項目に以下を設定すると、プレビューボタンまたは更新ボタンの横に「フロントエンドで確認」のボタンが追加されます。

```js
{literal}
(function() {
  {/literal}
  //フロントエンドURLを取得
  var FRONTEND_BASE_URL = '{$smarty.const.ROOT_URL}';
  {literal}
  document.addEventListener('DOMContentLoaded', function() {
    // Slugの値を取得
    var slugInput = document.querySelector('input[name="slug"]');
    var slugValue = slugInput ? slugInput.value : '';
    
    // Slugが空の場合は何もしない
    if (!slugValue) return;
    
    // プレビューボタンまたは更新ボタンの横に追加
    var targetBtn = document.querySelector('#edit_action_preview_li') || document.querySelector('#edit_action_draft_li');
    if (!targetBtn) return;
    
    // フロントエンドリンク用のボタンを作成
    var frontendLinkDiv = document.createElement('div');
    frontendLinkDiv.className = 'col-auto';
    
    var frontendLinkBtn = document.createElement('a');
    frontendLinkBtn.className = 'btn btn-outline-primary';
    frontendLinkBtn.href = FRONTEND_BASE_URL + '/news/' + encodeURIComponent(slugValue);
    frontendLinkBtn.target = '_blank';
    frontendLinkBtn.innerHTML = '<i class="fa fa-external-link"></i> フロントエンドで確認';
    
    frontendLinkDiv.appendChild(frontendLinkBtn);
    targetBtn.parentNode.insertBefore(frontendLinkDiv, targetBtn.nextSibling);
  });
})();
{/literal}
```

## カスタムテンプレート
[コンテンツ定義]->[項目設定]でSlugのカスタムテンプレートに以下を設定すると、Slugの項目にフロントエンドで確認のリンクが追加されます。

```smarty
<tr id="disp_topics_id" class="">
  <th class="rounded-0 bg-light">
    <label class="fw-bold">Slug</label>

    <span
      class="text-gray-600 ms-1"
      data-bs-toggle="tooltip"
      title=""
      data-bs-original-title="IDの代わりに識別子を指定できます。"
    >
      <i class="fe fe-help-circle"></i>
    </span>

    <span class="small text-gray-700 ms-2">(ID: {$formData.topics_id|escape})</span>
  </th>

  <td>
    <input
      type="text"
      name="slug"
      value="{$formData.slug|escape}"
      size="80"
      class="form-control"
    />

    {if $formData.slug}
      {assign var="newsId" value=$formData.slug}
    {elseif $formData.topics_id}
      {assign var="newsId" value=$formData.topics_id}
    {/if}

    {if $newsId}
      <span>フロントエンドで確認:</span>
      <a href="{$smarty.const.ROOT_URL}/news/{$newsId|escape:'url'}" target="_blank" rel="noopener noreferrer">
        <i class="fe fe-external-link me-1"></i>{$smarty.const.ROOT_URL}/news/{$newsId|escape}
      </a>
    {/if}
  </td>
</tr>
```

## 関連ドキュメント
- [カスタムテンプレートの使い方を教えてください。](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)


---

# 管理画面の見た目をカスタマイズできますか？

> 元ページ: `faq/can-i-adjust-the-appearance-of-the-admin-panel` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-adjust-the-appearance-of-the-admin-panel/
> 概要: 管理画面内の見た目に関しては、以下の内容が可能となっています。

管理画面内の見た目に関しては、以下の内容が可能となっています。
 
### 管理画面カラーの変更
 
管理画面の全体カラーを変更できます。  
[環境設定] -> [管理画面] -> [管理画面カラー]で色を選択して更新してください。  
ここで選択したカラーでファビコンのカラーも変更されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05d75e2b65de7f9db2a48532915515eb.png)

### 管理画面のロゴの変更

管理画面に表示されるロゴを変更できます。  
[環境設定] -> [管理画面] -> [ロゴURL]に表示したいロゴのURLを入力してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d8c34055b646acf79875d569901f303.png)

### 管理画面の言語の変更

管理画面右上の地球儀アイコンから、管理画面内の言語を[言語選択]で変更できます。  
この変更は管理画面内のみで、フロント画面への影響はありません。  
選択できる言語は、日本語、英語です。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/522356e1c49629a25822bd6cdb4d2e4f.png)
 
### 管理画面トップページのウィジェットの追加
 
独自のウィジェットを追加できます。  
[ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/)を参考に作成してください。 

### コンテンツ編集画面の表示内容の変更
コンテンツグループごとに、コンテンツ定義編集の「CSS」や「JavaScript」を利用して、編集画面の表示を調整できます。  
[コンテンツ編集画面の表示内容を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)を参考にご調整ください。

### 管理画面の任意のページにプラグイン適用

Kuroco管理画面の任意のページにCSSやVueコンポーネントを適用できます。  
以下のドキュメントを参考にご対応ください。

- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインを利用して、Kuroco管理画面に任意のVueコンポーネントを適用する](/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/)

## 関連ドキュメント
- [管理画面](/ja/docs/management/management-screen/)
- [管理画面プラグイン](/ja/docs/management/management-plugin/)
- [ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインを利用して、コンテンツ編集画面に任意のVueコンポーネントを適用する](/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)


---

# 親サイトの変更はできますか？

> 元ページ: `faq/can-i-change-parent-site` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-parent-site/
> 概要: ユーザー側では変更できません。ご希望の場合は調整いたしますので、以下の情報をフォームよりご連絡ください。

ユーザー側では変更できません。  
ご希望の場合は弊社にて調整いたしますので、以下の情報を[問い合わせフォーム](https://kuroco.zendesk.com/)よりご連絡ください。

- 親にしたいサイトのサイトキー  
- 子にしたいすべてのサイトのサイトキー  

:::caution
Kuroco利用料をクレジットカードでお支払い頂いている場合、親サイトの変更後にカード情報の再設定が必要です。  
クレジットカードの登録がなく無料枠を超えてご利用されているサイトは、深夜帯に実行される日次バッチ処理でメンテナンスモードになります。  
無料枠を超えてご利用中の場合は、変更当日に必ずカード情報の再設定を行ってください。
:::

サイトキーの変更を目的として親サイトを変更する場合は、「[全同期](/ja/docs/reference/sync-site-data/)」機能をご活用ください。  
なお、KurocoFrontなど全同期の対象外機能については、親サイト変更後に個別に調整をお願いします。

## 関連ドキュメント
- [サイト一覧](/ja/docs/management/site-list/)
- [同期項目一覧](/ja/docs/reference/sync-site-data/)
- [請求情報](/ja/docs/management/site-payment/)
- [Kuroco利用料の支払方法を教えてください](/ja/docs/faq/how-do-i-pay-the-kuroco-fee/)


---

# カスタムテンプレートの使い方を教えてください。

> 元ページ: `faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/
> 概要: コンテンツ定義の設定で、テンプレート編集の項目にHTMLを記述することで、対象の項目を任意のHTMLに置き換えることができます。

[コンテンツ定義](/ja/docs/management/content-structure-topics-group/#項目設定)の設定で、テンプレート編集の項目にHTMLを記述することで、対象の項目を任意のHTMLに置き換えることができます。  
項目に注釈を入れたり、背景色を変更したり、任意のクラスを追加するのにご利用ください。  

## 設定箇所 
設定したい[コンテンツ定義](/ja/docs/management/content-structure-topics-group/#項目設定)の編集画面にて、内容を変更したい項目の、「編集」ボタンをクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aef8272a5958ee9ec2fa8aa25e05a321.png)

項目設定が開くので[カスタムテンプレート]->[テンプレート編集]に記述します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/322739b3e23a3fe8cd8926aae2810e63.png)

## 設定例
### Slug
例えば以下の記述をSlugのカスタムテンプレートに入力すると、フロントエンドへのリンクを追加できます。

```smarty
<tr id="disp_topics_id" class="">
  <th class="rounded-0 bg-light">
    <label class="fw-bold">Slug</label>

    <span
      class="text-gray-600 ms-1"
      data-bs-toggle="tooltip"
      title=""
      data-bs-original-title="IDの代わりに識別子を指定できます。"
    >
      <i class="fe fe-help-circle"></i>
    </span>

    <span class="small text-gray-700 ms-2">(ID: {$formData.topics_id|escape})</span>
  </th>

  <td>
    <input
      type="text"
      name="slug"
      value="{$formData.slug|escape}"
      size="80"
      class="form-control"
    />

    {if $formData.slug}
      {assign var="newsId" value=$formData.slug}
    {elseif $formData.topics_id}
      {assign var="newsId" value=$formData.topics_id}
    {/if}

    {if $newsId}
      <span>フロントエンドで確認:</span>
      <a href="{$smarty.const.ROOT_URL}/news/{$newsId|escape:'url'}" target="_blank" rel="noopener noreferrer">
        <i class="fe fe-external-link me-1"></i>{$smarty.const.ROOT_URL}/news/{$newsId|escape}
      </a>
    {/if}
  </td>
</tr>
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4f16920f52cea930c3685415599f7403.png)

:::danger
テーブル構成と、フォーム部品(name、id)などは変更しないでください。  
:::

:::caution
項目設定で設定した他の設定は反映されなくなります。
:::

### タイトル
例えば以下の記述をタイトルのカスタムテンプレートに入力すると、タイトルの項目名を変更できます。  

```smarty
<tr id="topics_subject">
    <th class="bg-light"><label class="fw-bold">議題</label><span class="badge bg-secondary ms-1">必須</span></th>
    <td>
        {if !$docmeta.is_primary && $primaryRow.subject!=''}
            <p class="major_language">
                <span class="step">{$primaryRow.subject|escape}</span>
            </p>
        {/if}
        <input type="text" id="subject" name="subject" value="{$formData.subject|escape}" size="100" class="form-control"/>
        <br>
        <span class="hint">現在の議題：{$formData.subject|escape}の変更は注意深くしてください。</span><br>
        <span class="hint">変更が必要な場合は、前回のタイトルとの違いに留意してください。</span><br>
    </td>
</tr>
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd567f042b809ffd6c274046e72bba86.png)

:::danger
テーブル構成と、フォーム部品(name、id)などは変更しないでください。  
:::

:::caution
項目設定で設定した他の設定は反映されなくなります。
:::

### テキスト
#### 入力後に変更を禁止する
例えば以下の記述をテキスト項目のカスタムテンプレートに入力すると、一度入力して更新したテキストの変更ができなくなります。

```smarty
<th class="bg-light">
    <label class="fw-bold">
        テキスト
    </label>
    <code class="small text-gray-600 ms-2">ext_col_02</code>
</th>
<td>
    <div class="ext_item_0" data-ext_type="0" data-default_value="">
        {if $cols.0.value != ''}
        <div><input type="text" name="ext_col_02" value="{$cols.0.value}" size="80" class="form-control" readonly></div>
        {else}
        <div><input type="text" name="ext_col_02" value="" size="80" class="form-control"></div>
        {/if}
    </div>
</td>
```

:::danger
テーブル構成と、フォーム部品(name、id)などは変更しないでください。  
:::

:::caution
項目設定で設定した他の設定は反映されなくなります。
:::

#### URL入力項目に外部リンクを表示
例えば以下の記述をテキスト項目のカスタムテンプレートに入力すると、URLを入力した際に外部リンクが表示されるようになります。

```smarty
<th class="bg-light">
  <label class="fw-bold" for="demo_url_input">デモURL</label>
  <code class="small text-gray-600 ms-2">demo_url</code>
</th>

<td>
  <div class="ext_item_0" data-ext_type="0" data-default_value="">
    <div>
      <input type="text" id="demo_url_input" name="ext_2" class="form-control" value="{$cols.0.value}">
      {if $cols.0.value}
        <div class="mt-2">
          <a href="{$cols.0.value}" target="_blank" rel="noopener noreferrer" class="small text-primary">{$cols.0.value}</a>
        </div>
      {/if}
    </div>
  </div>
</td>
```

:::danger
テーブル構成と、フォーム部品(name、id)などは変更しないでください。
:::

:::caution
項目設定で設定した他の設定は反映されなくなります。
:::

## 関連ドキュメント
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [コンテンツ編集画面に公開URLを開くボタンを追加できますか？](/ja/docs/faq/can-i-add-a-button-to-open-the-public-url-from-the-content-edit-screen/)


---

# コンテンツ編集画面の表示を変更できますか？

> 元ページ: `faq/can-i-modify-the-display-of-the-content-editor-screen` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/
> 概要: コンテンツ定義ごとに、[コンテンツ定義編集]の「CSS」や「JavaScript」を利用して、編集画面の表示を調整できます。

コンテンツ定義ごとに、[コンテンツ定義編集の詳細設定](/ja/docs/management/content-structure-topics-group/#詳細設定)にある「CSS」や「JavaScript」を利用して、編集画面の表示を調整できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/493d680651753679294c658971fd05a0.png)

## CSS

設定例：詳細設定の項目を非表示にする
```css
{literal}
#section-topics-edit-details{display:none;}
{/literal}
```

:::tip
詳細な設定方法は、[コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/) をご参照ください。
:::

## JavaScript

設定例：ext_1のチェック状態に基づいて、ext_2,ext_3の表示/非表示を切り替える
```js
{literal}
window.addEventListener('load', function() {
    // チェックボックスの状態に基づいて input 要素の表示を制御する関数
    function toggleInputVisibility() {
        // id="ext_1__1" のチェックボックスを取得
        var checkbox1 = document.getElementById('ext_1__1');
        // input[name="ext_2"] 要素を取得
        var inputText2 = document.querySelector('input[name="ext_2"]');
        if (inputText2) {
            // id="ext_1__1" のチェックボックスがチェックされているか確認
            inputText2.style.display = checkbox1.checked ? '' : 'none'; // チェックされていれば表示、そうでなければ非表示
        }

        // id="ext_1__2" のチェックボックスを取得
        var checkbox2 = document.getElementById('ext_1__2');
        // input[name="ext_3"] 要素を取得
        var inputText3 = document.querySelector('input[name="ext_3"]');
        if (inputText3) {
            // id="ext_1__2" のチェックボックスがチェックされているか確認
            inputText3.style.display = checkbox2.checked ? '' : 'none'; // チェックされていれば表示、そうでなければ非表示
        }
    }

    // ページ読み込み時に一度実行して初期状態を設定
    toggleInputVisibility();

    // チェックボックスの状態変更にも反応するようにイベントリスナーを設定
    document.body.addEventListener('change', function(event) {
        // 変更された要素が id="ext_1__1" または id="ext_1__2" のチェックボックスであるか確認
        if (event.target.id === 'ext_1__1' || event.target.id === 'ext_1__2') {
            toggleInputVisibility();
        }
    });
});
{/literal}
```

設定例：GitHub Actionsワークフローを強制的に有効にする
```js
{literal}
// GitHub Actions ワークフローを強制的に有効にする
var radio = document.querySelector('input[name="dispatch_github_workflow"][value="1"]');
if (radio) radio.checked = true;
{/literal}
```

## 編集時の注意点
- Smartyが有効になっているので、`{ }`を使用する場合は、`{literal} {/literal}`で囲むように記述してください。
- 管理画面に関しては独自に設定されたCSS/JavaScriptのバージョンアップ後の動作保証はしておりません。
- CSS/JavaScriptでの調整を起因とした不具合に関しての調査は有償対応になります。

## 関連ドキュメント
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [カスタムテンプレートの使い方を教えてください。](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)
- [コンテンツ編集画面に公開URLを開くボタンを追加できますか？](/ja/docs/faq/can-i-add-a-button-to-open-the-public-url-from-the-content-edit-screen/)


---

# Kurocofrontでプレビュー用のページを出力できますか？

> 元ページ: `faq/can-i-output-a-preview-page-with-kurocofront` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-output-a-preview-page-with-kurocofront/
> 概要: PRを作って/kuroco stageとコメントするとプレビュー用のデプロイが実行されます。

可能です。連携したGitHubでPRを作って、`/kuroco stage`とコメントするとプレビュー用のデプロイが実行されます。  
必要な設定(YAMLファイルの記述)はKuroco管理画面に表示されるサンプルコードに含まれるので、特別な対応不要ですぐにご利用いただけます。

デプロイしないと確認できない機能の検証や、クライアントへの報告、社内レビューなどにご活用ください。  

## プレビューデプロイの実行手順
### PRを作成する
GitHubで、変更内容を含めたPRを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d43216d2defda21b8b4eb0776562ed6.png)

### PRにコメントを入れる

PullRequest画面下部のコメント欄に、`/kuroco stage`と入力し、[Comment]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb2301d837284c03d5662ba4040eac0f.png)

コメントがされたのを確認した後、[Actions]タブをクリックしてみると、GithubActionsが`/kuroco stage`のコメントに反応し、プレビューデプロイを開始していることが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e418ce8668741af1028ec8e5a1e6f571.png)

### 発行されたURLにアクセスする

PullRequestの画面に戻り、しばらく後に画面更新をすると、プレビューデプロイのリンクが発行されています。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75a0ac2f3728fd934658696bc8a959a2.png)

リンクにアクセスして、PullRequestの内容がデプロイされていることを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f652d02b27fc9120c4e9d3a6d69fa974.png)

:::tip
プレビューデプロイで発行される仮URL上から操作したとき、CORSエラーが発生する場合、ワイルドカードで仮URLからのアクセスを許可する指定をしてください。  
仮URLは`https://ハッシュ値-サイトキー.g.kuroco-front.app`の様に発行されるため、  
`https://*-サイトキー.g.kuroco-front.app`という指定をすることで、CORSエラーを回避できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/37dd46e77bc289ad77a83018e259866f.png)
:::

## 関連ドキュメント
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/#kurocofrontへプレビューデプロイする手順)


---

# Internet Explorer11で管理画面を利用できますか？

> 元ページ: `faq/can-i-use-the-admin-panel-with-internet-explorer-11` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-the-admin-panel-with-internet-explorer-11/
> 概要: Kurocoの管理画面でのInternet Explorer 11（以下 IE11）のご利用については「非推奨」とさせていただいております。APIの動作に関しては、その仕組み上、特にブラウザのバージョンは影響を受けませんが、フロントエンド側のフレームワーク側でのサポートが切れてる場合もありますのでご注意ください。

Kurocoの管理画面でのInternet Explorer 11（以下 IE11）のご利用については「非推奨」とさせていただいております。
APIの動作に関しては、その仕組み上、特にブラウザのバージョンは影響を受けませんが、フロントエンド側のフレームワーク側でのサポートが切れてる場合もありますのでご注意ください。

現在IE11をご利用の場合にはIEの後継ブラウザの [Microsoft Edge](https://www.microsoft.com/ja-jp/edge) や、その他のブラウザをご利用くださいますようお願いいたします。
なお、IE11以前のバージョンも全て非推奨とさせていただいております。

## IE11を非推奨とする背景
IE11でも動作する可能性はありますが、以下の理由から推奨環境には含めておりません。
- 既にMicrosoftの公式サポートが切れている
- 上記の理由から社内での動作テストはしていない
- 一部機能が動作しない場合に技術的に対応ができない場合もある

:::info
[2016年1月12日より、Internet Explorer のサポートポリシーが変わります](https://blogs.windows.com/japan/2015/11/11/iesupport/)  
[お使いの環境が対象かどうかを調べる](https://security.yahoo.co.jp/news/tls12.html)
:::

なお、Internet Explorer / Microsoft Edgeの互換モードでは正しく動作しませんので、互換モードを無効にしてご利用ください。

## Microsoft社の公開情報
Internet Explorerの今後について等の情報がMicrosoft社から公開されております。

- [Internet Explorerの今後について](https://social.msdn.microsoft.com/Forums/ja-JP/47290e24-fc66-4d3e-a2de-429643758d40/)
- [Windows10に搭載される2つのWebブラウザ、Microsoft Edge と Internet Explorer 11](https://blogs.windows.com/japan/2015/08/24/evaeyeedge/)
- [Microsoft365アプリ のInternet Explorer 11 のサポート終了と Windows 10 での Microsoft Edge レガシー版のサービス終了](https://techcommunity.microsoft.com/t5/microsoft-365-blog/microsoft-365-apps-say-farewell-to-internet-explorer-11-and/ba-p/1591666)

IE11をご利用中のお客様にはご不便をおかけすることとなり誠に申し訳ございませんが、何卒ご理解賜りますようお願いいたします。  

## 関連ドキュメント
- [管理画面の推奨環境を教えてください](/ja/docs/faq/what-environments-do-you-recommend-for-the-admin-panel/)
- [PCブラウザのバージョンの確認方法を教えてください](/ja/docs/faq/how-do-i-check-my-browser-version/)
- [最新のOSへの対応状況を教えてください](/ja/docs/faq/what-is-kurocos-support-status-for-my-os-version/)
- [管理画面](/ja/docs/management/management-screen/)


---

# スーパーユーザーはサブサイトにもログインできますか？

> 元ページ: `faq/can-superuser-also-log-in-to-sub-sites` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-superuser-also-log-in-to-sub-sites/
> 概要: はい。スーパーユーザーの権限を持っている場合、サイト一覧にSSOのリンクが表示されますので、そちらからサブサイトにログインが可能です。

はい。スーパーユーザーの権限を持っている場合、サイト一覧にSSOのリンクが表示されますので、そちらからサブサイトにログインが可能です。

## SSOのリンク場所
[環境設定]->[[サイト一覧](/ja/docs/management/site-list/)]

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6be5a25d8a442810d33617ba0b2956b5.png)

:::info
スーパーユーザーの権限を持つユーザーのみがSSOを利用可能です。
:::

## SSO時の挙動
SSOによるログイン時の挙動は以下になります。

- メインサイトでログインしているメールアドレスと同じメールアドレスでサブサイトにログインします。
- サブサイトに該当するメールアドレスがない場合には、group_id=1(スーパーユーザー)を付与したメンバーを新規に追加してログインします。
- すでにサブサイトにスーパーユーザーではないが、同じメールアドレスが追加されている場合は、その権限でログインをすることになります。
  (スーパーユーザーへの昇格はしません。)

## 関連ドキュメント
- [サイト一覧](/ja/docs/management/site-list/)
- [サブサイトをプレビューサイトにする](/ja/docs/tutorials/make-the-subsite-a-preview-site/)
- [親サイトの変更はできますか？](/ja/docs/faq/can-i-change-parent-site/)


---

# Kurocoに登録したコンテンツを複数のサイトから利用できますか

> 元ページ: `faq/can-the-content-registered-in-kuroco-be-used-from-multiple-sites` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-the-content-registered-in-kuroco-be-used-from-multiple-sites/
> 概要: KurocoのAPIはセキュリティ対策として、許可されたCORS（Cross-Origin Resource Sharing）元からのリクエストのみを受け付けます。そのため、CORS_ALLOW_ORIGINSにリクエスト元のドメインを登録し、APIリクエストを許可してください。

はい、可能です。  
KurocoのAPIはセキュリティ対策として、許可されたCORS（Cross-Origin Resource Sharing）元からのリクエストのみを受け付けます。  
そのため、[API](/ja/docs/management/api-list/)ページのCORS設定で`CORS_ALLOW_ORIGINS` にリクエスト元のドメインを登録し、APIリクエストを許可してください。

関連サイトなど複数のサイトから共通のコンテンツを利用するシーンを想定しています。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bdc549dc2390f6f8aef2e14c094b141.png)

:::tip
コンテンツの変更を通知したい場合は、更新後にWebhookやメールによる通知を設定することが可能です。
- [カスタム処理を利用して、コンテンツ追加時にメールを送信する](/ja/docs/tutorials/how-to-implement-original-function-into-the-middle-of-processing-by-using-function/)
:::

## 関連ドキュメント
- [API](/ja/docs/management/api-list/)
- [カスタム処理を利用して、コンテンツ追加時にメールを送信する](/ja/docs/tutorials/how-to-implement-original-function-into-the-middle-of-processing-by-using-function/)
- [CORS設定の変更が反映されません。](/ja/docs/faq/i-changed-cors-but-it-is-not-reflected/)


---

# 日付は、和暦と西暦のどちらで管理していますか？

> 元ページ: `faq/does-kuroco-use-the-japanese-or-western-calendar-system` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/does-kuroco-use-the-japanese-or-western-calendar-system/
> 概要: Kurocoでは、日付等は全て西暦で管理をしています。

Kurocoでは、日付等は全て西暦で管理をしています。

## 関連ドキュメント
- [日付に曜日の情報を持たせられますか？](/ja/docs/faq/can-i-include-weekday-information-in-a-date/)
- [Smartyで、7日前の日付を取得することはできますか？](/ja/docs/faq/can-i-obtain-the-date-and-time-stamp-at-different-points-in-smarty/)


---

# 管理画面の言語はどこで変更できますか？

> 元ページ: `faq/how-do-i-change-the-language-of-the-admin-panel` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-change-the-language-of-the-admin-panel/
> 概要: 管理画面の言語は、管理画面トップの右側にあるアイコンから変更できます。

管理画面の言語は、管理画面トップの右側にあるアイコンから変更できます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/81feb87d9694f35d3a4b9097eecad0c3.png)

## 関連ドキュメント
- [アカウント設定](/ja/docs/management/account/)
- [管理画面](/ja/docs/management/management-screen/)


---

# 管理画面トップページのウィジェットを編集できますか

> 元ページ: `faq/how-do-i-edit-the-widget-at-the-top-of-the-administration-screen` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-edit-the-widget-at-the-top-of-the-administration-screen/
> 概要: ウィジェットの編集にはいくつかの方法があります。以下を参考に編集ください。

ウィジェットの編集にはいくつかの方法があります。以下を参考に編集ください。

## 独自のウィジェットを作成する

[環境設定] -> [ダッシュボードのウィジェット]から独自のウィジェットを作成可能です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c792bbdad2221e3073a150fe243e15bf.png)

新規作成したウィジェットは、管理画面トップページの左上に表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b34a2df53e25616b20bdeca18bdc505a.png)

設定方法の詳細は「[ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/#通常版の管理画面を編集する)」を参照してください。

## デフォルトのウィジェットを非表示にする
### 編集権限を設定する
ダッシュボードの表示されるウィジェットはユーザーの所属するグループの権限と連動します。  
そのため、[メンバー管理]->[グループ]のグループ編集で権限を調整すると、対象ユーザーのダッシュボードに表示さえるウィジェットが変わります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6082f9c5a31423da7f6034d9beb1ac88.png)

### 管理画面プラグインでCSSを適用する
管理画面プラグインの機能で管理画面の任意のページにCSSを適用できます。  
ウィジェット毎に固有のIDが振られているので、こちらを利用してウィジェットを非表示にしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/935478f936df6265e3d59fc51b96402d.png)

設定方法の詳細は「[管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)」を参照してください。

## 関連ドキュメント
- [ダッシュボードのウィジェットを利用して管理画面の表示を編集する](/ja/docs/tutorials/edit-the-dashboard-view/)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)


---

# 管理画面プラグインでCSSを複数ページに適用することはできますか？

> 元ページ: `faq/is-it-possible-to-apply-css-to-multiple-pages-using-the-admin-panel-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-apply-css-to-multiple-pages-using-the-admin-panel-plugin/
> 概要: CSSファイルを適用するページを選択することはできませんが、ページURIの設定は前方一致になっているため、管理画面プラグインを特定ディレクトリ配下全体に適用し、クラス名を使用してCSSを書き分けることで対応できます。

CSSファイルを適用するページを選択することはできませんが、ページURIの設定は前方一致になっているため、
管理画面プラグインを特定ディレクトリ配下全体に適用し、クラス名を使用してCSSを書き分けることで対応できます。  
メインコンテンツ要素 (div.main-content) に各ページ固有のクラスが付与されているのでご利用ください。  

## クラス名の命名規則
各クラスの命名規則は、管理画面のパスと対応しています。  
(`content_` + /management/以降のパスを `_` で連結した値)

- コンテンツ一覧  
管理画面のパス: `/management/topics/topics_list/`  
class: `content_topics_topics_list`

- メンバー編集  
管理画面のパス: `/management/member/member_edit/`  
class: `content_member_member_edit`

また、対象がコンテンツの場合、コンテンツ定義IDを含むクラス名が含まれます。  
class: `topics_list_group1`

## 設定例
### コンテンツ一覧画面とメンバー編集画面にCSSを適用する
#### 管理画面プラグイン
ページURIに`/`を指定すると、/management/配下の全てのページにCSSが適用されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a279c1b203004278358368903f98bc5a.png)

#### CSS
コンテンツ一覧のダウンロードボタンと、メンバー編集ページの配信タブを非表示にするには以下のようにCSSを書きます。

```css
.content_topics_topics_list #downloadButton {
    display: none;
}

.content_member_member_edit #sub_tab_mailmaga {
    display: none;
}

```

### コンテンツ定義ID=7,8のコンテンツ一覧にのみCSSを適用する
#### 管理画面プラグイン
ページURIに`/topics/topics_list/`を指定すると、全てのコンテンツ一覧ページにCSSが適用されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/530616e60f36eaff2bad95f0c48e1f60.png)

#### CSS
コンテンツ定義ID=7,8 のコンテンツ一覧でギアアイコンを消すには以下のようにCSSを書きます。

```css
.content_topics_topics_list.topics_list_group7 button[title="表示項目設定"],
.content_topics_topics_list.topics_list_group8 button[title="表示項目設定"] {
    display: none;
}
```

## 編集時の注意点
- 管理画面に関しては独自に設定されたCSS/JavaScriptのバージョンアップ後の動作保証はしておりません。
- CSS/JavaScriptでの調整を起因とした不具合に関しての調査は有償対応になります。

## 関連ドキュメント
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)


---

# 管理画面の推奨環境を教えてください

> 元ページ: `faq/what-environments-do-you-recommend-for-the-admin-panel` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-environments-do-you-recommend-for-the-admin-panel/
> 概要: 以下の内容はKurocoの管理画面の推奨環境です。フロントエンド側の推奨環境やアプリ、IoT等でのご利用はAPIを利用しますので、以下の制約はございません。フロントエンドの構築をされた方にご確認ください。

以下の内容は**Kurocoの管理画面の推奨環境**です。フロントエンド側の推奨環境やアプリ、IoT等でのご利用はAPIを利用しますので、以下の制約はございません。フロントエンドの構築をされた方にご確認ください。

## PCからの利用
下記ブラウザの最新版での利用を推奨しております。  
- Google Chrome 最新版
- Mozilla Firefox 最新版
- Microsoft Edge 最新版

※上記推奨環境でなくても利用可能な場合がありますが、動作を保証するものではありません。

**Internet Explorer 11での動作について**  
※Internet Explorer 11でも動作する可能性はありますが、以下の理由から推奨環境には含めておりません。
- 既に主なOSでMicrosoftの公式サポートが切れております。
- 上記の理由から社内での動作テストはしておりません。
- 一部機能が動作しない場合に技術的に対応できない場合があります。

:::info
[Microsoft|Windows Blogs](https://blogs.windows.com/japan/2015/11/11/iesupport/)  
[Yahoo! JAPAN|セキュリティーセンター](https://security.yahoo.co.jp/news/tls12.html)  
※Internet Explorer / Microsoft Edgeの互換モードでは正しく動作いたしませんので、互換モードを無効にしてご利用ください。
:::

## スマートフォン、タブレットからの利用
スマートフォンやタブレットはPC向け管理画面にてご利用いただけますが、一部機能が動作しない可能性もあります。  
フロントエンド側の推奨環境は構築されたアプリケーションに依存します。

## モバイル（フィーチャーフォン）からの利用
管理画面はフィーチャーフォンでの利用は想定しておりません。  
フロントエンド側の推奨環境は構築されたアプリケーションに依存します。

## 関連ドキュメント
- [管理画面](/ja/docs/management/management-screen/)
- [Internet Explorer11で管理画面を利用できますか？](/ja/docs/faq/can-i-use-the-admin-panel-with-internet-explorer-11/)
- [最新のOSへの対応状況を教えてください](/ja/docs/faq/what-is-kurocos-support-status-for-my-os-version/)
- [PCブラウザのバージョンの確認方法を教えてください](/ja/docs/faq/how-do-i-check-my-browser-version/)


---

# ログイン履歴の記録ロジックに関して教えてください

> 元ページ: `faq/what-is-the-logic-behind-the-login-history` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-the-logic-behind-the-login-history/
> 概要: 基本的にログイン処理が入った場合に1カウントされます。オートログイン機能が有効の場合、ログイン画面を経由していなくてもログイン処理は走りますので、記録されます。ブラウザを開いて操作しない時間が2時間以上経過するか、ブラウザを閉じると、ログイン状態は解除されます。

## ログインのカウントに関して
- 基本的にログイン処理が入った場合に1カウントされます。
- オートログイン機能が有効の場合、ログイン画面を経由していなくてもログイン処理は走りますので、記録されます。
- ブラウザを開いて操作しない時間が2時間以上経過するか、ブラウザを閉じると、ログイン状態は解除されます。
 
## ログアウトのカウントに関して
- ログアウトボタンをクリックするなど、明示的にログアウトの処理を行った場合のみ記録されます。

## 関連ドキュメント
- [ログインログ](/ja/docs/management/login-log-list/)
- [オートログインの有効期間について教えてください](/ja/docs/faq/what-is-the-validity-period-for-auto-logins/)
- [セッションの有効期限は変更できますか？](/ja/docs/faq/can-i-change-the-session-timeout-duration/)
- [ログインロックについて教えてください。](/ja/docs/faq/what-causes-accounts-to-be-locked/)
