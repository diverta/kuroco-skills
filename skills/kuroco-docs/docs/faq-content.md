# Kurocoドキュメント: FAQ / コンテンツ管理

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- プレビュー機能で副言語の場合に_langのパラメータを付与できますか?（`can-i-add-a-_lang-parameter-for-sub-language-in-the-preview-function`）
- APIでのコンテンツ更新・追加時にワークフローは利用できますか？（`can-i-add-or-update-workflow-content-via-api`）
- コンテンツの更新後のトリガをCSVアップロードの場合にキャンセルできますか？（`can-i-cancel-the-trigger-after-updating-the-content-in-the-case-of-a-csv-upload`）
- コンテンツの所有者を変更できますか？（`can-i-change-the-content-owner`）
- プレビュートークンの有効期限を変更できますか（`can-i-change-the-expiration-date-of-the-preview-token`）
- コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？（`can-i-change-the-time-selection-interval-for-the-publication-settings`）
- 主言語のコンテンツを作らずに、副言語のコンテンツだけを作ることはできますか？（`can-i-create-content-in-the-secondary-language-only`）
- コンテンツ一覧に表示する項目をカスタマイズできますか？（`can-i-customize-the-items-displayed-in-the-content-list`）
- コンテンツ一覧の並び順を、任意の順序に変更できますか？（`can-i-freely-modify-the-order-of-the-content-list`）
- 日付に曜日の情報を持たせられますか？（`can-i-include-weekday-information-in-a-date`）
- コンテンツを作るコンテンツ定義を間違えてしまいました。コンテンツを他のコンテンツグループへ移動することはできますか？（`can-i-move-content-to-another-content-group`）
- WYSIWYGエディタに入力されたソースが自動変換されないように出来ますか？（`can-i-prevent-sources-entered-into-the-wysiwyg-editor-from-being-automatically-converted`）
- メンバーのグループ毎に、コンテンツ定義の表示を調整できますか？（`can-i-set-different-topic-group-displays-for-the-user-groups`）
- 「公開設定」の選択肢をデフォルトで「非公開」にできますか？（`can-i-set-the-public-settings-option-to-private-by-default`）
- 他のコンテンツと同じSlugを設定できますか？（`can-i-set-the-same-slug-as-other-content`）
- CSVによるコンテンツのアップロードはできますか？（`can-i-upload-topics-using-csv-files`）
- タグ名にスペースを含めたい（`can-i-use-spaces-in-tag-names`）
- 「２重送信の可能性があるので、更新をしませんでした。もう一度更新処理を行ってください。」というエラーメッセージが表示されてしまいます。（`i-received-the-error--update-process-was-interrupted`）
- バッチ処理が起動しているか確認することはできますか？（`is-it-possible-to-check-if-a-batch-process-is-running`）
- CSVダウンロードした多言語のコンテンツが文字化けします（`multilanguage-content-in-downloaded-csv-file-is-garbled`）
- フォーム項目設定の並び順がAPIに反映しません（`the-ordering-of-form-fields-is-not-reflected-in-the-api`）
- コンテンツのIDが飛んでしまっていたり、1から始まっていないことがあります。コンテンツのIDのカウントロジックを教えてください。（`what-is-the-counting-logic-behind-content-ids`）
- コンテンツ一覧のデフォルトの並び順は何ですか？（`what-is-the-default-sort-order-for-content-list`）
- カウンター項目の値が更新されません（`why-are-counter-field-values-not-updated`）
- コンテンツ定義の設定を変更した後で、過去の記事を表示すると、存在しないデータが入っていることがあるのはなぜですか？（`why-do-I-sometimes-see-nonexistent-data-in-past-articles-after-modifying-the-content-structure`）
- 郵便番号のバリデーションで文字が通るのはなぜですか？（`why-does-postal-code-validation-allow-letters`）
- コンテンツ更新後のトリガが二重に呼ばれるのはなぜですか？（`why-is-the-trigger-called-twice-after-content-update`）


---

# プレビュー機能で副言語の場合に_langのパラメータを付与できますか?

> 元ページ: `faq/can-i-add-a-_lang-parameter-for-sub-language-in-the-preview-function` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-add-a-_lang-parameter-for-sub-language-in-the-preview-function/
> 概要: コンテンツ定義編集の「プレビューの対象とするページのURL」の項目で、?_lang={$smarty.request._doc_lang}のようにパラメータを追加してURLを設定してください。

[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#項目説明-1)の「プレビューの対象とするページのURL」の項目で、
`/?_lang={$smarty.request._doc_lang}`
のようにパラメータを追加したURLを設定してください。  

副言語の編集ページからプレビューURLを呼び出した場合に`_lang`のパラメータが付与されます。  

## 設定箇所
[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#項目説明-1)の「プレビューの対象とするページのURL」  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d18db4d7d531e97813a26d6087d95575.png)

## URLの表示
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b0db27fc00366a96741183993fcedf38.png)

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)
- [多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)
- [副言語について](/ja/docs/reference/secondary-language/)
- [プレビュートークンの有効期限を変更できますか](/ja/docs/faq/can-i-change-the-expiration-date-of-the-preview-token/)


---

# APIでのコンテンツ更新・追加時にワークフローは利用できますか？

> 元ページ: `faq/can-i-add-or-update-workflow-content-via-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-add-or-update-workflow-content-via-api/
> 概要: 可能です。コンテンツの内容と合わせて、approvalflow_idで承認ワークフローのidをPOSTしてください。

可能です。  
コンテンツの内容と合わせて、`approvalflow_id`で承認ワークフローのidをPOSTしてください。

## 確認方法
まずは利用する承認ワークフローを確認します。  
後ほど利用するので、ワークフローのIDをメモしておきます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c00f203c83224dcfdc02c2ee8746c53b.png)

次に、コンテンツの追加をするエンドポイントを作成します。  

| 項目 | 設定 |
| :--- | :--- |
| カテゴリー | コンテンツ |
| モデル | Topics, v1 |
| オペレーション | insert |
| topics_group_id | 対象のコンテンツ定義ID |

:::tip
コンテンツの更新をする場合は、オペレーションがinsertではなくupdateになります。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd2a067e365312ffbcba1fca27a73196.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4084db3249c2c27ea303aae374b18841.png)

最後に、Swagger UIで以下のデータをエンドポイントにPOSTします。

```json [POSTデータ例]
{
  "subject": "Content Title",
  "contents": "Content",
  "open_flg": 1,
  "ymd": "2022-11-07",
  "approvalflow_id": 4
}
```

:::caution
`"approvalflow_id": 4`の部分はご自身のワークフローのIDを使用してください。
:::

コンテンツ一覧を確認すると、承認待ちのデータが追加されていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dd0ab573615bb453a936de1a27e4a0e5.png)

## 関連ドキュメント
- [承認ワークフロー](/ja/docs/management/workflow/)


---

# コンテンツの更新後のトリガをCSVアップロードの場合にキャンセルできますか？

> 元ページ: `faq/can-i-cancel-the-trigger-after-updating-the-content-in-the-case-of-a-csv-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-cancel-the-trigger-after-updating-the-content-in-the-case-of-a-csv-upload/
> 概要: webhookの送信は編集画面から更新したときにだけ有効にして、CSVアップロードで更新した場合はトリガの実行をキャンセルしたい場合は、「コンテンツのアップロード前」などのトリガで、グローバル変数をアサインし、その値を元にwebhookの送信をキャンセルするように記述してください。

「[コンテンツの更新後](/ja/docs/reference/trigger-variables/#コンテンツの更新後)」「[コンテンツの追加後](/ja/docs/reference/trigger-variables/#コンテンツの追加後)」などのトリガはCSVアップロードによる更新/追加の場合にも動作します。  

そのため、コンテンツ更新後に別のエンドポイントにWebhookを送信する処理を記述した場合、
CSVアップロードで複数のコンテンツを一度に更新すると大量のWebhookが送信されることになります。

webhookの送信は編集画面から更新したときだけ有効にして、CSVアップロードで更新した場合はトリガの処理をキャンセルしたい場合は、
「[コンテンツのアップロード前](/ja/docs/reference/trigger-variables/#コンテンツのアップロード前)」などのトリガで、グローバル変数をアサインし、その値を元にwebhookの送信をキャンセルするように記述してください。

## 設定例
### コンテンツのアップロード前

```smarty
{assign_globals key='cancel_flag' value="1"}
```

### コンテンツの更新後

```smarty
{assign_globals var='cancel_flag' key='cancel_flag'}
{if $cancel_flag != "1"}
    <!--任意の処理-->
{/if}
```

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# コンテンツの所有者を変更できますか？

> 元ページ: `faq/can-i-change-the-content-owner` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-content-owner/
> 概要: CSVアップロード時にmember_id列を更新することで、コンテンツの所有者を変更できます。この操作はスーパーユーザーのみ利用可能です。

CSVアップロード時に`member_id`列を更新することで、コンテンツの所有者を変更できます。

:::caution
この操作は**スーパーユーザー**のみ利用可能です。スーパーユーザー以外のユーザーはCSVアップロードでコンテンツの所有者を変更できません。
:::

## コンテンツの所有者を変更する方法

1. コンテンツ定義の一覧画面より、対象のコンテンツ定義の[ダウンロード]リンクをクリックします。
2. `member_id`列を含むCSVファイルをダウンロードします。
3. `member_id`列を編集し、新しい所有者のメンバーIDを設定します。
4. 編集したCSVファイルを[アップロード]リンクからアップロードします。

### 注意事項

- `member_id`の値は数値のメンバーIDである必要があります。
- CSVで新規コンテンツを追加する際に`member_id`列が空の場合、アップロードを実行したユーザーがコンテンツの所有者として設定されます。
- CSVで新規コンテンツを追加する場合は、指定された`member_id`でコンテンツが追加されます。

## 関連ドキュメント
- [コンテンツアップロード/ダウンロード](/ja/docs/management/content-structure-topics-csv/)
- [CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)


---

# プレビュートークンの有効期限を変更できますか

> 元ページ: `faq/can-i-change-the-expiration-date-of-the-preview-token` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-expiration-date-of-the-preview-token/
> 概要: 定数の設定で対応可能です。「RCMS_API_PREVIEW_TOKEN_LIFESPAN」をセットして値に希望の秒数を設定してください。

通常、プレビュートークンの有効期限は24時間になっています。  
変更したい場合は[定数](/ja/docs/management/constants/)の設定で対応可能です。  
「RCMS_API_PREVIEW_TOKEN_LIFESPAN」をセットして値に希望の秒数を設定してください。

## 設定箇所
[環境設定]->[定数]で[追加]をクリックする。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7cb44cbf691ccc363c9527568bddf65b.png)

## 設定値
以下の値を設定します。  
- 名前：RCMS_API_PREVIEW_TOKEN_LIFESPAN
- 値：プレビュートークンの有効期限(秒)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4693f50a9c3adb0ea9996a92b64616f.png)

設定が完了すると、プレビュートークン発行時の`validUntil=********`のパラメータの値が更新されます。  

:::tip
値はUnixtimeになっているので、日時に変換して確認してください。
:::

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)
- [Kurocofrontでプレビュー用のページを出力できますか？](/ja/docs/faq/can-i-output-a-preview-page-with-kurocofront/)
- [プレビュー機能で副言語の場合に_langのパラメータを付与できますか?](/ja/docs/faq/can-i-add-a-_lang-parameter-for-sub-language-in-the-preview-function/)


---

# コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？

> 元ページ: `faq/can-i-change-the-time-selection-interval-for-the-publication-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/
> 概要: コンテンツの公開日時の設定は、[定数]の設定で変更可能です。

コンテンツの公開日時の設定は、[定数](/ja/docs/management/constants/)の設定で変更可能です。  
定数より下記を追加すると、時間の選択間隔を変更できます。

- 名前：OPEN_TIME_OPTION_INTERVAL
- 値：希望の時間選択単位[分]

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9b269f6a1072cd1c7fcf8c37913fedb.png)
定数を設定すると、公開時間の設定が5分単位に変更されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e210df1c576648e8d4f1e2f79042424c.png)

:::caution
公開は厳密には数十秒遅れる可能性があるため、1分単位の場合、狙いの時間とのずれが大きくなる場合もあります。<br/>また、UIの問題で、時間の選択ボックスのスクロールが長くなる点はご了承ください。
:::

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [コンテンツを公開したまま、指定の日時に更新する](/ja/docs/tutorials/scheduling-updates-for-published-contents/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)


---

# 主言語のコンテンツを作らずに、副言語のコンテンツだけを作ることはできますか？

> 元ページ: `faq/can-i-create-content-in-the-secondary-language-only` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-create-content-in-the-secondary-language-only/
> 概要: Kurocoでは主言語・副言語のセットで多言語のコンテンツの編集ができるようになっています。そのため副言語は主言語よりも前に作成することが原理上できません。しかしながら、主言語の公開の前に副言語でのコンテンツを公開したい場合も考えられます。その場合は、下記いずれかにて対応できます。

Kurocoでは主言語・副言語のセットで多言語のコンテンツの編集ができるようになっています。
そのため副言語は主言語よりも前に作成することが原理上できません。

しかしながら、主言語の公開の前に副言語でのコンテンツを公開したい場合も考えられます。その場合は、下記いずれかにて対応できます。

## 主言語の公開前に、副言語のコンテンツを公開する

[コンテンツの公開設定](/ja/docs/management/content-structure-topics/#公開設定)にて、下記設定をすることで副言語のコンテンツのみ公開となります。

- 主言語：非公開
- 副言語：公開

## 承認ワークフローを利用する
承認ワークフローを利用して運用している場合は、都度、承認ワークフローを通す必要がありますが、非公開の主言語のコンテンツは承認ワークフローを通さずに作成が可能です。   
以下の設定がされているコンテンツ定義は、作成するコンテンツが非公開であれば、承認権限を持っていなくても新規コンテンツを追加できるようになります。

**設定箇所**  
[コンテンツ定義](/ja/docs/management/content-structure-topics-group)設定の「申請権限での非公開・下書き保存許可」で、副言語のコンテンツを作成するコンテンツ定義を選択してください。
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/aeaffb2d78e8216241a073fc9df065f3.png)

## 関連ドキュメント
- [副言語について](/ja/docs/reference/secondary-language/)
- [多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [承認ワークフロー](/ja/docs/management/workflow/)
- [多言語サイトを構築する際に気をつけることを教えてください](/ja/docs/faq/what-should-i-take-note-of-when-building-a-multilanguage-site/)


---

# コンテンツ一覧に表示する項目をカスタマイズできますか？

> 元ページ: `faq/can-i-customize-the-items-displayed-in-the-content-list` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-customize-the-items-displayed-in-the-content-list/
> 概要: 一覧ページから設定する方法とトリガーを設定する方法の2通りがあります。要件に応じてご対応ください。

可能です。2通りの設定方法がありますので要件に応じてご対応ください。


## 歯車マークから設定する
コンテンツ一覧右上の歯車マークをクリックすると、表示項目設定が表示され、コンテンツ一覧に表示する項目を設定できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/11aa07a2d8b12b6979bbae1590ad5a49.png)

デフォルトの項目は非表示にできません。
また、こちらの設定はユーザー毎に保持されます。

デフォルト項目を変更したい場合や、全ユーザーを対象に表示を変更したい場合、項目名を変更したい場合などは[コンテンツの表示（管理画面）]のトリガーを利用してください。

## トリガーで設定する

[コンテンツの表示（管理画面）](/ja/docs/reference/trigger-variables/#コンテンツの表示管理画面)のトリガーで、
`$disable_columns`、`$default_columns`の変数にキーの設定をすることで一覧表示の項目を設定できます。

### disable_columns
削除する項目を指定する設定です。以下のように非表示にしたい項目を配列で指定してください。

**disable_columnsの設定例**

```smarty
{* Use disable_columns*}
{assign_array var="disable_columns" values="ymd,update_ymdhi"}
```

**表示例**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a67496a2b04a22cae70ad1cc8b1fe3fe.png)

### default_columns
表示する項目をいちから指定する方法です。以下のように表示したい項目のキー名、表示名、ソートの有無を指定してください。

**default_columnsの設定例**

```smarty
{*Use default_columns*}
{assign_array var="default_columns" values=""}

{assign_array var="topics_id" values=""}
{assign var="topics_id.key_name" value="topics_id"}
{assign var="topics_id.disp_name" value="TOPICS ID"}
{assign var="topics_id.sortable" value=false}

{assign_array var="subject" values=""}
{assign var="subject.key_name" value="subject"}
{assign var="subject.disp_name" value="SUBJECT"}
{assign var="subject.sortable" value=false}

{assign_array var="slug" values=""}
{assign var="slug.key_name" value="slug"}
{assign var="slug.disp_name" value="URL"}
{assign var="slug.sortable" value=false}

{append var="default_columns" value=$topics_id}
{append var="default_columns" value=$subject}
{append var="default_columns" value=$slug}
```

**表示例**

![Image from Gyazo](https://t.gyazo.com/teams/diverta/863e650a19b04ffcf05cfebe24512d68.png)

:::tip
管理画面プラグインでCSSを適用し、歯車マークを非表示にすると、各ユーザーで同じ一覧表示にし、ユーザー側での変更もさせないという設定が可能です。
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
:::

### filters
コンテンツ一覧のデフォルトの並び順を変更したい場合は、`$filters` の `order` キーに並び順を指定します。
ユーザーが手動でソートしていない場合に、ここで指定した並び順がデフォルトとして適用されます。

**filtersの設定例（`order_no` の昇順で表示する場合）**

```smarty
{assign_array var="filters" values=""}
{assign var="filters.order" value="order_no=ASC"}
```

`order` の値の指定方法（カラム名や `ASC`/`DESC` の指定など）の詳細は、[Filter検索のパラメータ](/ja/docs/reference/filter-query/)を参照してください。

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/#コンテンツの表示管理画面)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)


---

# コンテンツ一覧の並び順を、任意の順序に変更できますか？

> 元ページ: `faq/can-i-freely-modify-the-order-of-the-content-list` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-freely-modify-the-order-of-the-content-list/
> 概要: コンテンツの並び順は[API]メニューの「エンドポイントの設定」で調整できます。エンドポイント一覧画面より並び順を変更したいエンドポイントの[更新]をクリックし、並び順を変更してください。

コンテンツの並び順は[API]メニューの「エンドポイントの設定」で調整できます。  
エンドポイント一覧画面より並び順を変更したいエンドポイントの[更新]をクリックし、並び順を変更してください。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/523a4e6b195b4624220e4daa30cd437c.jpg)
## 並び順の設定方法
1.「Configure Endpoint」の編集画面の「モデル」を次のように選択する。
- カテゴリー：コンテンツ  
- モデル：Topics  
- オペレーション：list  

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/f36369f708078534991f22825a82940b.png)
2.「Parameters」の「order_query」を設定する （指定可能なフィールド等は後述します）  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/aab729b9aaa98d710da996a38364101f.png)
### 指定可能なフィールドと並び順  
#### フィールド
- topics_id（コンテンツID）
- order_no（並び順）
- ymd（日付）
- post_time（投稿時間）
- contents_type（カテゴリ）
- subject（タイトル）
- regular_flg（上位表示する）
- inst_ymdhi（作成日時）
- update_ymdhi（最終更新日時）
- topics_group_id（記事グループID）
- open_flg（公開フラグ）
- slug（スラッグ）
- contents_type_nm（カテゴリ名）
- contents_type_nm_2（カテゴリ名2）
- contents_type_nm_3（カテゴリ名3）
- open_sta_date（公開開始日）
- open_end_date（公開終了日）
- favorite_cnt（お気に入り数）
- favoriteX_cnt（アクションタイプ毎のお気に入り数）
- comment_cnt（コメント数）
- vector_distance（ベクトル距離）
- ext_col_nn（拡張項目フィールド ※nnは拡張項目のID）

**注意事項**
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/#項目説明-1)の「日付を利用しない」の設定によって、ymd(無効時)とorder_no(有効時)のどちらが利用できるかが変わります。<br/>また、post_timeは「投稿時間も設定する」が有効な場合に利用可能です。
- favorite_cntはAPIのパラメータ設定でget_favorite_cntが設定されている場合に利用可能です。
- comment_cntはAPIのパラメータ設定でget_comment_cntが設定されている場合に利用可能です。
- open_sta_date / open_end_dateはAPIのパラメータ設定でadd_open_ymdhiが有効な場合に利用可能です。
- vector_distanceはvector_searchまたはsimilar_search_idのクエリパラメータを使用したベクトル検索時に利用可能です。

#### 複数のコンテンツ定義を指定した場合
1つのエンドポイントで複数のコンテンツ定義（記事グループ）を対象にしている場合、`order_query`で指定できるフィールドには次の制限があります。

- 拡張項目（`ext_col_nn`）で並び替える場合、[複数のコンテンツ定義をまたぐ検索](/ja/docs/tutorials/implement-a-search-function/#参考複数のコンテンツ定義をまたぐ検索を実装する)と同様に、対象のコンテンツ定義すべてで「項目設定の種類」「コンテンツ項目のSlug」「コンテンツ項目のID」が同一になっている必要があります。いずれかが異なる拡張項目は並び替えの対象になりません。
- 「日付を利用しない」の設定が異なるコンテンツ定義が混在している場合（`ymd`を利用する定義と`order_no`を利用する定義が混在している場合）、`ymd`・`post_time`・`order_no`はいずれも並び替えキーとして利用できません。この場合は`update_ymdhi`など、対象のコンテンツ定義に共通するフィールドで並び替えてください。

#### 並び順
- asc（昇順、小さい順） 
- desc（降順、大きい順）
 
#### 記述例
topics_idの昇順で表示したい場合、以下のように記入してください。

`topics_id:asc`

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a14d221c25b54a3f34d4b7e0f466792b.png)
:::caution
項目が繰り返しを利用している場合は、うまく動作しない可能性があります。
:::

:::info
`order_query`を指定しない場合のデフォルトの並び順については[コンテンツ一覧のデフォルトの並び順は何ですか？](/ja/docs/faq/what-is-the-default-sort-order-for-content-list/)を参照してください。
:::

## 関連ドキュメント
- [API](/ja/docs/management/api-list/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [位置情報による並び替え](/ja/docs/reference/order-by-location/)
- [コンテンツ一覧のデフォルトの並び順は何ですか？](/ja/docs/faq/what-is-the-default-sort-order-for-content-list/)


---

# 日付に曜日の情報を持たせられますか？

> 元ページ: `faq/can-i-include-weekday-information-in-a-date` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-include-weekday-information-in-a-date/
> 概要: 後処理の出力変換リストで対応できます。

APIのレスポンスの場合、後処理の[出力変換リスト](/ja/docs/reference/post-processing/#%E5%87%BA%E5%8A%9B%E5%A4%89%E6%8F%9B%E3%83%AA%E3%82%B9%E3%83%88)で対応できます。  
たとえば Date FormatにY-m-d lを指定すると2023-05-25 Thursday がレスポンスされます。  

## 設定例

![Image from Gyazo](https://t.gyazo.com/teams/diverta/499dc478b38574ebf932e74073ff1dca.png)

|処理|値|出力例|
|:--|:--|:--|
|Date Format|`Y-m-d l`|`2023-05-25 Thursday`|
|Locale Date Format|`%Y-%m-%d(%%w%%)`|`2023-05-25(木)`|
|Locale Date Format|`%Y-%m-%d %%w%%曜日`|`2023-05-25 木曜日`|

## 関連ドキュメント
- [後処理](/ja/docs/reference/post-processing/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [Smartyで、7日前の日付を取得することはできますか？](/ja/docs/faq/can-i-obtain-the-date-and-time-stamp-at-different-points-in-smarty/)
- [日付は、和暦と西暦のどちらで管理していますか？](/ja/docs/faq/does-kuroco-use-the-japanese-or-western-calendar-system/)


---

# コンテンツを作るコンテンツ定義を間違えてしまいました。コンテンツを他のコンテンツグループへ移動することはできますか？

> 元ページ: `faq/can-i-move-content-to-another-content-group` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-move-content-to-another-content-group/
> 概要: 「コンテンツ定義１」で作成したコンテンツを、「コンテンツ定義２」へ移動するといった動作は出来ません。

「コンテンツ定義１」で作成したコンテンツを、「コンテンツ定義２」へ移動するといった動作は出来ません。  
コンテンツ作成時に間違えてしまった場合は、正しいコンテンツ定義で新しくコンテンツを作成してください。

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)


---

# WYSIWYGエディタに入力されたソースが自動変換されないように出来ますか？

> 元ページ: `faq/can-i-prevent-sources-entered-into-the-wysiwyg-editor-from-being-automatically-converted` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-prevent-sources-entered-into-the-wysiwyg-editor-from-being-automatically-converted/
> 概要: WYSIWYGエディタに入力されたソースが自動変換される現象は、使用しているエディタ(CKEditor)側の仕様に起因しています。そのため、Kurocoのシステム側での調節が難しい箇所になっています。

WYSIWYGエディタに入力されたソースが自動変換される現象は、使用しているエディタ(CKEditor)側の仕様に起因しています。そのため、Kurocoのシステム側での調節が難しい箇所になっています。
 
ソースコードを意図通りに入力したい場合には、WYSIWYGエディタではなく、拡張項目の「HTML」の利用をお勧めいたします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/681d15bc00c8e1fff4eaddbc17823cd0.png)

## 関連ドキュメント
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# メンバーのグループ毎に、コンテンツ定義の表示を調整できますか？

> 元ページ: `faq/can-i-set-different-topic-group-displays-for-the-user-groups` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-different-topic-group-displays-for-the-user-groups/
> 概要: コンテンツ定義編集の詳細設定にある「編集制限」で、どのグループに表示を許可するか設定できます。選択されなかったグループのメンバーの画面には、このコンテンツ定義は表示されません。

コンテンツ定義編集の詳細設定にある「編集制限」で、どのグループに表示を許可するか設定できます。  
選択されなかったグループのメンバーの画面には、このコンテンツ定義は表示されません。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/076c8d916f37d05b8048268267d8a07f.png)
## 編集制限をかけたときの表示の違い
今回はコンテンツ定義「お知らせ」に編集制限をかけています。

### 許可されているグループの画面
「お知らせ」が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f19854944e8e9c303a14540e69b8cb58.png)
### 許可されていないグループの画面
「お知らせ」が表示されません。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b28dae0e9a1f3a724f984becb1e6e7a5.png)
## メンバー単位で編集制限をかけたい場合は
編集制限はグループ単位でしかかけることができません。  
そのため、メンバー毎に編集制限をかけたい場合は、メンバー毎にグループを作成する必要があります。

## グループの設定方法
所属グループはメンバー編集画面で変更できます。[メンバー編集](/ja/docs/management/member/#%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AE%E7%B7%A8%E9%9B%86)をご参照ください。

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [グループ](/ja/docs/management/group/)
- [メンバー](/ja/docs/management/member/)
- [同じグループのメンバーが作成したコンテンツのみ表示・編集を可能にする](/ja/docs/tutorials/allow-only-the-display-and-editing-of-content-created-by-same-group-members/)


---

# 「公開設定」の選択肢をデフォルトで「非公開」にできますか？

> 元ページ: `faq/can-i-set-the-public-settings-option-to-private-by-default` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-the-public-settings-option-to-private-by-default/
> 概要: 定数の設定で対応可能です。「DEFAULT_OPEN_TYPE」をセットして値をcloseにしてください。

[定数](/ja/docs/management/constants/)の設定で対応可能です。  
「DEFAULT_OPEN_TYPE」をセットして値をcloseにしてください。

## 設定箇所
[環境設定]->[定数]で[追加]をクリックする。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7cb44cbf691ccc363c9527568bddf65b.png)
## 設定値
以下の値を設定します。  
- 名前：DEFAULT_OPEN_TYPE
- 値：close

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7686eb2713fd3d7fe14715c0cba71e8.png)
設定が完了すると、コンテンツ追加時のデフォルトの公開設定が「非公開にする」になります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/55a050ffa7a4acaad480771c8f5a304d.png)

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)
- [コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？](/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/)


---

# 他のコンテンツと同じSlugを設定できますか？

> 元ページ: `faq/can-i-set-the-same-slug-as-other-content` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-set-the-same-slug-as-other-content/
> 概要: Slugは、同一サイト内で同じものを設定することができません。コンテンツグループをまたいでのチェックになるため、Slugはサイト内でユニークとしてください。

## コンテンツのバリデーション
コンテンツに設定するSlugは、同一サイト内で同じものを設定することができません。  
コンテンツ定義をまたいでのチェックになるため、Slugはサイト内でユニークとしてください。

## 拡張項目のバリデーション 
コンテンツの拡張項目に設定する識別子は同コンテンツ定義内で同じものを設定することができません。  
親項目・子項目を含めて同じ識別子は利用できませんのでご注意ください。

## Slugの再利用について
他のコンテンツに設定していたSlugを別のコンテンツで再利用したい場合は、既存のコンテンツに設定したSlugを削除・変更ください。
対応後、他のコンテンツで使用していたSlugを設定できます。

**例(コンテンツ)：**  
1. 設定済み記事（トピックスID：100、Slug：kuroco）をページ削除もしくはSlug変更。
2. 別の記事（トピックスID：101）に、Slug：kurocoを設定しなおす。

## 関連ドキュメント
- [使用できないURLを教えてください](/ja/docs/faq/what-urls-cannot-be-used/)
- [コンテンツのidを指定したり変更することはできますか？](/ja/docs/faq/can-i-specify-or-change-topic-ids/)


---

# CSVによるコンテンツのアップロードはできますか？

> 元ページ: `faq/can-i-upload-topics-using-csv-files` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-upload-topics-using-csv-files/
> 概要: CSVによるコンテンツのアップロードは可能です。

CSVによるコンテンツのアップロードは可能です。  
CSVを作成後、コンテンツ定義の[アップロード](/ja/docs/management/content-structure-topics-csv/)よりご対応ください。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00842c75200cbe64d0a259adc4204b7f.png)

:::info
詳しい手順は、[CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/) をご参照ください。
:::

## 関連ドキュメント
- [コンテンツアップロード/ダウンロード](/ja/docs/management/content-structure-topics-csv/)
- [CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)
- [bulk_upsert APIを利用して、任意のCSVファイルをコンテンツにインポートする](/ja/docs/tutorials/bulk-upload-using-api/)
- [コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？](/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/)
- [CSVダウンロードした多言語のコンテンツが文字化けします](/ja/docs/faq/multilanguage-content-in-downloaded-csv-file-is-garbled/)


---

# タグ名にスペースを含めたい

> 元ページ: `faq/can-i-use-spaces-in-tag-names` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-spaces-in-tag-names/
> 概要: タグ名にスペースを含めることはできません。タグの拡張項目（項目1〜10）にスペースを含む正式名称を登録し、フロント側ではその値を表示用に利用してください。

タグ名にスペースを含めることはできません。タグのスペースは区切りとして扱われるため、意図的に利用を制限しています。

スペースを含むラベルを画面上に表示したい場合は、**タグの拡張項目**（項目1〜10）をご利用ください。タグの編集画面にはタイトルのほかに項目1〜10という拡張項目が用意されており、APIレスポンスから取得できます。

## 運用方法

1. Kuroco上では、タグ名（タイトル）にスペースを含めず、仕様に沿った形式で登録します。
2. タグの編集画面で、拡張項目（項目1〜10）のいずれかにスペースを含む正式名称を登録します。
3. フロント側では、タグ名の代わりに拡張項目の値を表示用として参照します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6c66eacff4adbebfccc0bb7ba242b41.png)

### 登録例

| 項目 | 登録値 |
| :--- | :--- |
| タイトル（タグ名） | `new-york` |
| 項目1（表示用の正式名称） | `New York` |

### APIレスポンス例

タグの拡張項目は `ext_col_01` 〜 `ext_col_10` としてAPIレスポンスに含まれます。フロント側では `tag_nm`（タグ名）ではなく、拡張項目の値を参照して表示してください。

```json
{
  "tags": [
    {
      "tag_id": 1,
      "tag_nm": "new-york",
      "ext_col_01": "New York"
    }
  ]
}
```

## 関連ドキュメント
- [タグ](/ja/docs/management/tag/)


---

# 「２重送信の可能性があるので、更新をしませんでした。もう一度更新処理を行ってください。」というエラーメッセージが表示されてしまいます。

> 元ページ: `faq/i-received-the-error--update-process-was-interrupted` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/i-received-the-error--update-process-was-interrupted/
> 概要: コンテンツが正常に送信できていない場合にこちらのエラーメッセージが表示されます。

コンテンツが正常に送信できていない場合にこちらのエラーメッセージが表示されます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d4fea2749b8992ec3c9406196befe37d.png)
    エラーが発生しました。
    ２重送信の可能性があるので、更新をしませんでした。もう一度更新処理を行ってください。

理由としては、下記が考えられます。
- コンテンツの投稿や更新の際に、更新ボタンを続けて2度クリックした
- 一度更新したコンテンツをブラウザバックして更新をした

こちらのエラーが発生した場合、コンテンツの編集内容は保存されていません。再度更新作業をお願いします。

## 関連ドキュメント
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [APIリクエストの2重送信制御について](/ja/docs/faq/how-do-i-prevent-duplicate-api-requests/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)


---

# バッチ処理が起動しているか確認することはできますか？

> 元ページ: `faq/is-it-possible-to-check-if-a-batch-process-is-running` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-check-if-a-batch-process-is-running/
> 概要: はい、確認可能です。オペレーション -> バッチ一覧にて、バッチ処理の機動状況が確認できます。

はい、確認可能です。  
オペレーション -> バッチ一覧にて、バッチ処理の機動状況が確認できます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1dd6200e719e3e6ca4115d819238c925.png)
画面の詳細は、管理画面マニュアルの[バッチ一覧](/ja/docs/management/batch/#batch-list)をご確認ください。

## 関連ドキュメント
- [バッチ処理](/ja/docs/management/batch/)
- [バッチログ](/ja/docs/management/batch-log-list/)
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [デフォルトのバッチ処理 一覧](/ja/docs/reference/batch-list/)
- [バッチ処理の実行を指定の日時や週次に設定できますか？](/ja/docs/faq/can-i-schedule-batch-processing-at-specific-dates-or-weekly/)


---

# CSVダウンロードした多言語のコンテンツが文字化けします

> 元ページ: `faq/multilanguage-content-in-downloaded-csv-file-is-garbled` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/multilanguage-content-in-downloaded-csv-file-is-garbled/
> 概要: エクセルでCSVファイルを開いた際の読込形式の問題の可能性があります。UTF-8の形式でKurocoからCSVファイルをダウンロードして、テキストで開いて確認ください。

エクセルでCSVファイルを開いた際の読込形式の問題の可能性があります。  
UTF-8の形式でKurocoからCSVファイルをダウンロードして、テキストで開いて確認ください。  

また、エクセルのデータの取得の機能で、UTF-8の形式でインポートしても確認ができます。  
[データ]->[データの取得]->[ファイルから]->[テキストまたはCSVから]をクリックして、元のファイルの形式を「65001: Unicode (UTF-8)」に設定します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/80368dce847ba3f1a21c2ef1c9a1d204.png)
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/35e896ffde253dfdc1859ed1d394e7d0.png)


上記で解決しない場合は[サポート](/ja/docs/about/support/)をご確認のうえ、お問い合わせください。

## 関連ドキュメント
- [コンテンツアップロード/ダウンロード](/ja/docs/management/content-structure-topics-csv/)
- [CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)
- [多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)
- [副言語について](/ja/docs/reference/secondary-language/)
- [CSVによるコンテンツのアップロードはできますか？](/ja/docs/faq/can-i-upload-topics-using-csv-files/)


---

# フォーム項目設定の並び順がAPIに反映しません

> 元ページ: `faq/the-ordering-of-form-fields-is-not-reflected-in-the-api` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/the-ordering-of-form-fields-is-not-reflected-in-the-api/
> 概要: フォームの項目を出力するcolsのレスポンスはデフォルトの出力がobjectになっています。エンドポイントの詳細設定でcols_typeの設定をarrayに指定してください。並び順が考慮された出力になります。

フォームの項目を出力するcolsのレスポンスはデフォルトの出力がobjectになっています。  
エンドポイントの詳細設定でcols_typeの設定をarrayに指定してください。  
並び順が考慮された出力になります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/564009496845a6a9bbf75bae8c5e0331.png)

## cols_typeパラメータがobjectの場合
cols_typeパラメータが未設定もしくはobjectの場合、
colsは順序を保証しないオブジェクト形式で出力されます。  
```json
{
    "cols": {
        "ext_1": {...},
        "ext_2": {...},
        "email": {...},
        "name": {...},
        ...
    }
}
```

また、ordered_keys に並び替えられたキー名が出力されます。  
こちらを利用して、フロント側で並び順の値の順番で表示するよう実装可能です。  
```json
{
    "cols": {
        ...
    },
    "ordered_keys": [
        "ext_1",
        "email",
        "ext_2",
        "name",
        ...
    ]
}
```

## cols_typeパラメータがarrayの場合
cols_typeパラメータがarrayの場合、
colsは順序を考慮する配列形式で出力されます。  
```json
{
    "cols": [
        {"key": "ext_1", ...},
        {"key": "email", ...},
        {"key": "ext_2", ...},
        {"key": "name", ...},
        ...
    ]
}
```

ordered_keys は出力されません。

## 関連ドキュメント
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [エンドポイント 基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [フォーム定義で利用できるフォーム項目一覧](/ja/docs/reference/form-field-list/)


---

# コンテンツのIDが飛んでしまっていたり、1から始まっていないことがあります。コンテンツのIDのカウントロジックを教えてください。

> 元ページ: `faq/what-is-the-counting-logic-behind-content-ids` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-the-counting-logic-behind-content-ids/
> 概要: コンテンツのIDは、作成順にカウントアップされます。

コンテンツのIDは、作成順にカウントアップされます。

## IDが１から始まらない理由
Kurocoは仕組み上、常に既存サイトをコピーして新規サイトを作成します。そのため、IDは1から始まらないことがあります。  

## IDが飛んでいる理由
IDはコンテンツ定義を跨いでカウントアップします。そのため、コンテンツ定義毎に見るとID番号が飛んでいるように見えます。  

なお、新規コンテンツ(A)を途中保存した状態で、更に新規コンテンツ(B)を作成して保存をすると、新規コンテンツ(B)のIDは新規コンテンツ(A)の分を飛ばした番号で登録されます。

## 関連ドキュメント
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [コンテンツのidを指定したり変更することはできますか？](/ja/docs/faq/can-i-specify-or-change-topic-ids/)


---

# コンテンツ一覧のデフォルトの並び順は何ですか？

> 元ページ: `faq/what-is-the-default-sort-order-for-content-list` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-the-default-sort-order-for-content-list/
> 概要: コンテンツ一覧APIでorder_queryを指定しない場合のデフォルトの並び順について説明します。

コンテンツ一覧APIで`order_query`を指定しない場合、以下の優先順位で降順にソートされます。

| 優先順位 | ソートキー | 説明 |
| :--- | :--- | :--- |
| 1 | 上位表示する（`regular_flg`） | 「上位表示する」が有効なコンテンツが先に表示されます。 |
| 2 | 日付（`ymd`）または 並び順（`order_no`） | [コンテンツ定義](/ja/docs/management/content-structure-topics-group/#項目説明-1)の項目設定で「日付を使う」を選択した場合は日付、「並び順を使う」を選択した場合は並び順が使用されます。 |
| 3 | 投稿時間（`post_time`） | コンテンツ定義で「投稿時間も設定する」が有効な場合のみ、日付に続いて投稿時間でもソートされます。 |
| 4 | 最終更新日時（`update_ymdhi`） | コンテンツの最終更新日時でソートされます。 |
| 5 | コンテンツID（`topics_id`） | 上記がすべて同じ場合、コンテンツIDでソートされます。 |

:::info
`order_query`を指定すると、上記のデフォルトの並び順は適用されず、指定した条件のみでソートされます。  
`order_query`の指定方法については[コンテンツ一覧の並び順を、任意の順序に変更できますか？](/ja/docs/faq/can-i-freely-modify-the-order-of-the-content-list/)を参照してください。
:::

## 関連ドキュメント
- [コンテンツ一覧の並び順を、任意の順序に変更できますか？](/ja/docs/faq/can-i-freely-modify-the-order-of-the-content-list/)
- [エンドポイント基本設定/詳細設定一覧](/ja/docs/reference/endpoint-parameters/)
- [コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#項目説明-1)


---

# カウンター項目の値が更新されません

> 元ページ: `faq/why-are-counter-field-values-not-updated` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/why-are-counter-field-values-not-updated/
> 概要: カウンター項目は、パフォーマンス向上のためにコンテンツデータとは別に値を管理しています。同期されるまでの間、表示用の値と並び替え用の値にずれが生じる場合があります。

カウンター項目は、パフォーマンス向上のためにコンテンツデータとは別に値を管理しています。同期されるまでの間、表示用の値と並び替え用の値にずれが生じる場合があります。

## カウンター項目の仕組み

カウンター項目は、アクセス数やいいね数など頻繁に更新される値を扱うために設計されています。パフォーマンスを向上させるため、Kurocoではカウンターの値をコンテンツ自体から分離し、非同期的に更新を行っています。

具体的には、カウンターの値は以下の2箇所で管理されています。

1. **カウンターテーブル**：最新のカウンター値。カウンター操作が行われると即座に更新されます。
2. **コンテンツテーブル**：コンテンツデータと一緒に保存されたカウンター値のキャッシュ。APIレスポンスでの表示や並び替えに使用されます。

## どのような場合に値が分離するか

以下のようなケースでカウンターテーブルの値が更新され、コンテンツテーブルの値との間にずれが生じます。

- **[`{increment_counter}`](/ja/docs/reference/smarty-plugin#increment_counter) または [`{update_counter}`](/ja/docs/reference/smarty-plugin#update_counter) Smartyプラグインを使用した場合**：これらのプラグインは同期をとらずに直接カウンターテーブルを更新します。
- **[`{googleanalytics}`](/ja/docs/reference/smarty-plugin#googleanalytics) Smartyプラグインでアクセス数を更新した場合**：プラグインはカウンターテーブルに新しい値を書き込みますが、その時点ではコンテンツテーブルは更新されません。

APIのリスト取得で使用される並び替え用の値はコンテンツテーブルから読み取られるため、同期されるまではカウンター項目での並び替えが期待通りの結果にならない場合があります。

## カウンター値を同期する方法

### コンテンツ編集画面からの更新

コンテンツ編集画面で**カウンターの更新**チェックボックスにチェックを入れて保存することで、カウンターテーブルとコンテンツテーブルを同時に更新し、値を同期した状態にできます。

### Topics::increment による更新

`Topics::increment`エンドポイントでカウンターをインクリメントした場合、カウンターテーブルは即座に更新され、コンテンツテーブルを同期するための`sync_counter`バッチ処理がスケジュールされます。  
このバッチ処理は、カウンターテーブルから最新の値を読み取り、コンテンツテーブルに書き戻すことで2つの値を同期します。そのため、コンテンツテーブルへの反映は一時的に遅延しますが、バッチが完了すると解消します。

### sync_counter Smartyプラグインによる手動同期

[`{sync_counter}`](/ja/docs/reference/smarty-plugin#sync_counter) Smartyプラグインを使用して手動で同期を実行できます。 `{increment_counter}` や `{update_counter}` を使用した後、任意のタイミングで値を同期したい場合に有効です。

```smarty
{sync_counter ids="1,2,3"}
```

### googleanalyticsと組み合わせたバッチ処理での同期

[\{googleanalytics\}](/ja/docs/reference/smarty-plugin#googleanalytics) Smartyプラグインの例では、同じバッチ処理内でgoogleanalyticsプラグインの後にsync_counterバッチを呼び出すことで、カウンター値を同期しています。

```smarty
{googleanalytics
    var="result"
    update_column_slug="pv"
    update_target_dimension="customEvent:slug"
    updated_topics_ids='updated_topics_ids'
    topics_group_id=1}

{assign_array var=ext_data values=''} 
{assign var=ext_data.topics_ids value=$updated_topics_ids} 
{batch module='topics' name='sync_counter' ext_data=$ext_data}
```

## 代替手段：カウンター項目の代わりに数値項目を使う

値を常にコンテンツと同期した状態で保持したい場合や、非同期の高頻度更新が不要な場合は、カウンター項目の代わりに**数値項目**の使用を検討してください。数値項目はコンテンツテーブルに直接値を保存するため、表示用の値と並び替え用の値にずれが生じることはありません。

## 関連ドキュメント
- [GoogleAnalyticsのPV数を元にアクセスランキングを実装する方法](/ja/docs/tutorials/how-to-implement-ranking-with-google-analytics/)
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# コンテンツ定義の設定を変更した後で、過去の記事を表示すると、存在しないデータが入っていることがあるのはなぜですか？

> 元ページ: `faq/why-do-I-sometimes-see-nonexistent-data-in-past-articles-after-modifying-the-content-structure` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/why-do-I-sometimes-see-nonexistent-data-in-past-articles-after-modifying-the-content-structure/
> 概要: コンテンツの更新履歴は、コンテンツ定義編集やコンテンツカテゴリの更新履歴と連動していません。そのため、更新履歴で過去の記事を表示するときに、コンテンツ定義編集やカテゴリの設定では最新のデータを利用してしまい、存在しないデータが入るといった現象が発生する場合もあります。

コンテンツの更新履歴は、コンテンツ定義編集やコンテンツカテゴリの更新履歴と連動していません。  
そのため、更新履歴で過去の記事を表示するときに、コンテンツ定義編集やカテゴリの設定では最新のデータを利用してしまい、存在しないデータが入るといった現象が発生する場合もあります。

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [コンテンツカテゴリ](/ja/docs/management/content-structure-topics-category/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)


---

# 郵便番号のバリデーションで文字が通るのはなぜですか？

> 元ページ: `faq/why-does-postal-code-validation-allow-letters` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/why-does-postal-code-validation-allow-letters/
> 概要: 郵便番号のバリデーションは、海外の郵便番号に対応するため文字列も許可されています。日本の郵便番号のフォーマットに制限する場合は正規表現で[0-9]{3}-[0-9]{4}と制限してください。

郵便番号のバリデーションは、海外の郵便番号に対応するため文字も許可されています。  

日本の郵便番号のフォーマット（例: 123-4567）に制限する場合は正規表現で  
`[0-9]{3}-[0-9]{4}`  
と制限してください。

## 関連ドキュメント
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [カスタム処理を利用して、APIに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-api-by-using-function/)
- [フォーム定義で利用できるフォーム項目一覧](/ja/docs/reference/form-field-list/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# コンテンツ更新後のトリガが二重に呼ばれるのはなぜですか？

> 元ページ: `faq/why-is-the-trigger-called-twice-after-content-update` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/why-is-the-trigger-called-twice-after-content-update/
> 概要: トリガの処理内に自身のトリガの実行条件を満たす処理を書いた場合、つまり、トリガのループを作る処理を書いた場合にトリガが2回呼ばれることがあります。

トリガの処理内に自身のトリガの実行条件を満たす処理を書いた場合、つまり、トリガのループを作る処理を書いた場合にトリガが2回呼ばれることがあります。  
以下に無限ループに対するKurocoの制約と、トリガが2回呼ばれる理由について説明します。  

## 無限ループについて
「Api::request_api のエンドポイントに設定したカスタム処理内で自身のエンドポイントを呼ぶ」、「後処理に設定したカスタム処理で自身のエンドポイントを呼ぶ」など、誤った実装をしてしまった場合、関連するアクションが連続的に実行され、プログラムが終了しない状態となります。  
無限ループは、サーバーの負荷を高め、リソースの浪費を引き起こすため、重大な問題です。  

## APIに設定されたループに関する制約
Kurocoでは無限ループへの対策としてAPIに以下の制限を設けています。 

### 自身のエンドポイントへのリクエストを禁止
カスタム処理では、自身を呼び出したエンドポイントに対してリクエストを送ることができません。  
この制約により、以下の実装をした場合は、エンドポイントへのリクエストがキャンセルされ、処理が終了します。  

- Api::request_api/Api::request_api_post のエンドポイントに設定したカスタム処理内で自身のエンドポイントを呼ぶ
- 前処理/後処理に設定したカスタム処理で自身のエンドポイントを呼ぶ

など。

### 多段APIの禁止

KurocoではAPIを多段で呼び出すことを禁止されています。例えば `{api_internal}` プラグインからAPIを呼び出し、そのAPI実行時さらに `{api_internal}` が実行されるとエラーとなります。

## トリガをベースにした処理ループ
### ループ終了までのプロセス
トリガをベースにしたループを作成した場合、例えばコンテンツ編集後のトリガ内でコンテンツ編集を行うAPIを呼び出した場合、1回目のトリガにおけるAPI呼び出しは管理画面コンテンツ編集画面が呼び出し元となるため、上記の[自身のエンドポイントへのリクエストを禁止](#自身のエンドポイントへのリクエストを禁止)による制約は受けず、APIによるコンテンツ編集が行われ２回目のトリガが実行されます。  
２回目のトリガでのAPI呼び出しは自身のエンドポイントが呼び出し元になるため、APIリクエストがキャンセルされてループが終了します。

```
コンテンツ更新(管理画面)
↓
トリガ実行(1回目)
コンテンツ更新のAPIリクエスト(1回目)
↓
コンテンツ更新(API)
↓
トリガ実行(2回目)
コンテンツ更新のAPIリクエストは制約によりキャンセル
↓
処理終了
```

### トリガのループを1回で終了する記述
コンテンツ更新後のトリガを利用して、同じコンテンツ定義のコンテンツを更新する際、トリガの実行を1回で終了させたい場合は以下のコードをカスタム処理の先頭に記述してください。

```smarty
{if $smarty.server.HTTP_RCMS_X_API_REQUEST_CNT > 0}
    {return}
{/if}
```

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [後処理](/ja/docs/reference/post-processing/)
- [コンテンツの更新後のトリガをCSVアップロードの場合にキャンセルできますか？](/ja/docs/faq/can-i-cancel-the-trigger-after-updating-the-content-in-the-case-of-a-csv-upload/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
