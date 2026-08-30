# Kurocoドキュメント: リファレンス / コンテンツ管理（3/3）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 副言語について（`secondary-language`）
- WYSIWYGエディタの使用方法（`wysiwyg`）
- WYSIWYG カスタムカラーの設定方法（`wysiwyg-custom-color-settings`）


---

# 副言語について

> 元ページ: `reference/secondary-language` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/secondary-language/
> 概要: 環境設定 -> ローカライズで多言語設定を有効にするとコンテンツに副言語の登録が可能です。本ドキュメントでは副言語を登録した際の動作について説明します。

[環境設定] -> [ローカライズ]で多言語設定を有効にするとコンテンツに副言語の登録が可能です。  
本ドキュメントでは副言語を登録した際の動作について説明します。

## APIパラメータ
エンドポイントで利用できる副言語に関するパラメータは以下になります。

|パラメータ|説明|
|:--|:--|
|`_lang`|レスポンスするコンテンツの言語を指定します。<br/><br/>※システムのメッセージは`ja`, `en`のみに対応しています。<br/>※意図して設定されたバリデーションエラーを除くシステムのエラーメッセージ(スキーマエラー等)は英語になります。|
|`filter_lang`|絞り込みに利用する言語を指定します。|
|`_doc_lang`|POST系のエンドポイントで、POSTの対象となる言語を指定します。|

## コンテンツ定義
コンテンツ定義に対する副言語の設定は、以下のように影響します。  

|項目|説明|
|:--|:--|
|全般-名前|APIからのレスポンスで言語毎の値を取得できます。また、日本語・英語に設定した名前は管理画面の言語設定に連動して管理画面上での表示にも使用されます。|
|全般-説明|APIからのレスポンスで言語毎の値を取得できます。|
|項目設定|言語毎のコンテンツデータに適用され、管理画面上では言語のタブを切り替えることで表示が変わります。<br/>選択形式の項目では言語毎にlabelを変更できますが、keyは共通になっている必要があります。|
|詳細設定|管理画面の言語設定に連動して、管理画面上での表示・動作に影響します。日本語・英語以外の言語については設定しても動作しません。|

<!--
https://github.com/diverta/Kuroco-opendev/issues/6882
-->

## コンテンツ
コンテンツに関する副言語データは、主言語のデータとセットで登録をする使い方を想定しています。  
そのため、コンテンツ内の項目に繰り返しを利用した場合の並び順は、主言語が基準となり、主言語の並び順の変更が副言語にも反映されます。

また、APIのレスポンスは管理画面の表示・並び順と同一になります。

1. 主言語の並び順を変更すると、それに対応して副言語の並び順も更新されます。  
  **管理画面：**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ac3bb62205a203b3256f7e94611dcc6.png)
  
  **レスポンス：**  
**主言語:**

  ```
    "ext_1": [
      "3",
      "1",
      "2"
    ]
  ```
  
**副言語:**

  ```
    "ext_1": [
      "3",
      "1",
      "2"
    ]
  ```
  

2. 副言語の繰り返し項目の一部にデータが登録されていない場合、主言語と同じ並び順に`""`のデータが返ります。  
  **管理画面：**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/0c995572c72fc6850224c8e5a36eae39.png)
  
  **レスポンス：**  
**主言語:**

  ```
    "ext_1": [
      "1",
      "2",
      "3"
    ]
  ```
  
**副言語:**

  ```
    "ext_1": [
      "",
      "2",
      "3"
    ]
  ```
  

3. 繰り返し項目のうち、主言語・副言語で共にデータがない順番の項目はAPIからレスポンスされません。  
  **管理画面：**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c61f2c05783ed21474f9ce53751636e.png)
  
  **レスポンス：**  
**主言語:**

  ```
    "ext_1": [
      "2",
      "3"
    ]
  ```
  
**副言語:**

  ```
    "ext_1": [
      "2",
      "3"
    ]
  ```
  

4. 主言語にデータが登録されていない繰り返し順で、副言語にデータが登録されている場合、該当の項目は主言語と副言語のセットから外れ、主言語に対する追加項目として扱われます。  
  そのため、主言語に登録が無いデータは副言語の並び順の最後に移動します。  
  **管理画面：**  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/f205ea31196046b449a0acafbc010104.png)
  
  **レスポンス：**  
**主言語:**

  ```
    "ext_1": [
      "2",
      "3"
    ]
  ```
  
**副言語:**

  ```
    "ext_1": [
      "2",
      "3",
      "1"
    ]
  ```
  

## 制限事項
### 主言語にしか設定できない項目
Slugや関連情報など、いくつかの項目はコンテンツに対しての設定となるため、主言語からしか設定できず、
APIから副言語のコンテンツを取得した場合、主言語と同じ情報がレスポンスされます。

主言語のみにデータを持つ項目は以下になります。

- topics_id
- ymd
- contents_type
- contents_type_cnt
- topics_flg
- regular_flg
- inst_ymdhi
- update_ymdhi
- topics_group_id
- post_time
- member_id
- Slug
- order_no
- カウンター
- 関連情報選択
- タグ(tag_nm, ext_col_XX は言語設定に連動)
- お気に入り
- コメント

これらの項目を主言語と副言語で別々に設定したい場合は、主言語の拡張項目に設定して利用します。

例えば副言語の更新日時を主言語と別に設定したい場合は、
[日付フォーマット](/ja/docs/reference/list-of-extra-column-available-on-content/#日付フォーマット)の項目を作成し、更新日時(EN)などを設定します。  

:::tip
特定の項目を自動で入力されるようにするには、[コンテンツの更新前](/ja/docs/reference/trigger-variables/#コンテンツの更新前)のトリガーや[カスタムテンプレート](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)を組み合わせて設定してください。
:::

### 並び替え
パフォーマンス維持のため、Orderクエリによる並び替えは主言語でしか実行できません。
主言語と副言語で並び順を変えたい場合は、並び替えに使いたいデータを主言語の拡張項目に設定します。

例：  
・並び順  
・並び順(EN)  

## 関連ドキュメント
- [多言語サイトを構築する](/ja/docs/tutorials/building-a-multi-language-site/)


---

# WYSIWYGエディタの使用方法

> 元ページ: `reference/wysiwyg` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/wysiwyg/
> 概要: KurocoのWYSIWYGエディタの使用方法を説明します。Kurocoで利用するWYSIWYGエディタは、Microsoft Wordのような直観的で、誰でも簡単にコンテンツを作成・編集することができます。

Kurocoで利用するWYSIWYGエディタは、Microsoft Wordのような直観的で、誰でも簡単にコンテンツを作成・編集できます。  
また、Sourceモードに切り替えると、直接HTMLを編集できますので、HTMLの知識がある方はより柔軟にコンテンツ制作が行えます。  
Sourceモードへの切替えはアイコンツールの[Source]のクリックで切り替わりますので、デザインやレイアウトを確認しながらHTML編集をスムーズに行うことができます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c18a2888511154433be35d3a00283f9e.png)

:::info
WYSIWYGエディタでは、空のタグが消される、scriptタグが消される、不明なタグが補完されるなど、HTMLのタグに自動で修正が入る場合があります。
HTMLを厳密に管理したい場合は[HTML](/ja/docs/reference/list-of-extra-column-available-on-content/#html)の項目を利用してください。
:::

## アイコンツールの説明

|項目   |説明  |
| :--- | :--- |
|![Image from Gyazo](https://t.gyazo.com/teams/diverta/2fe7885c70b33aa4b05afa72b4c90458.png)<br/>ソース|デザイン編集とHTML編集モードの切り替えを行います。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b06cfd6ad14623f42983d0a85e4353c3.png)<br/>FullScreen|WYSIWYGエディタをフルスクリーンモードにします。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/aafe2e2e823c00ad6f8c52c6f1b6f265.png)<br/>見出し|見出しタグを設定します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6bd418b102ddab3508e927d0c8571198.png)<br/>文字揃え|文章の[左揃え]、[右揃え]、[中央揃え]、[均等揃え]を制御します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/471fb7cc8057b2721462fa10b3253fc2.png)<br/>ボールド|太文字(B.png)を設定します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4a358b5b7e2e96715cefbde8aa32bb9e.png)<br/>イタリック|イタリック文字(I.png)を設定します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/78b9908b7dde184f768e593955c8d6a1.png)<br/>アンダーライン|下線(U.png)を設定します。|
|![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd3f8860338292975d38130136179858.png)<br/>取り消し線|取り消し線を設定します。`wysiwyg_options`に`strikethrough::1`を設定すると表示されます。|
|![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0f4bcc1183d4729f0ddf3909b089575.png)<br/>上付き/下付き|上付き文字（superscript）と下付き文字（subscript）を設定します。`wysiwyg_options`に`subscript::1`を設定すると表示されます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d7136bac6f4a83d7fedc0adb4426a897.png)<br/>画像やファイルの挿入|KurocoFilesに保存した画像を選択して挿入することができます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/56dc20f03a40c3f2f961ba79b982679f.png)<br/>画像挿入|直接自分のローカル（デスクトップ等）から画像を挿入します。挿入した画像は自動的にKurocoFilesの/fiese/user/topoics_img/配下もしくは「リソースを指定」で設定したディレクトリに保存されます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b4f77a48df55e4a613f17a20ec8e1561.png)<br/>メディアの挿入|動画を挿入します。アイコンをクリックすると下記のウィンドウが表示されますので、URLを入力してください。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/957b93bf67060b08e7352e87efa7b254.jpg)<br/>利用可能なMedia URLについては[CKEditorのドキュメント](https://ckeditor.com/docs/ckeditor5/latest/features/media-embed.html#media-providers.png)をご参照ください。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d952980c2163a5095d361c79c88908c5.png)<br/>リンク|リンクの挿入と編集を行います。リンクを設定したい文字列をドラッグし、アイコンをクリックしてください。リンクを設定する場合は、下記のウィンドウが表示されますので、URLを入力してください。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/58fae71fc209823748edf0af1f03247f.jpg)<br/>Open in a new tabを有効にすると、aタグに`target="_blank"`が設定されます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3ab58abf3a3ed03173ef05b2b0538bc7.png)<br/>表の挿入|表を挿入します。アイコンをクリックすると下記のウィンドウが表示されるので、行・列を指定します。<br/>![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fe4f28ad40de52e152ec21bb2c7975bd.png)|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fc34fc74b0d01e857aac5350ab428d8e.png)<br/>フォントサイズ|文字の大きさを変更できます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/514f8ae01bbacd7482fdd06b4cb78158.png)<br/>文字色|文字の色を設定します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8c195675e43d6bad0b64d77aff2cece8.png)<br/>背景色|文字の背景の色を設定します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ca13556f1e27711097fbd44dccb132ba.png)<br/>フォントファミリー|文字の種類（フォント）を変更できます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4177acb84ad445d4afe6732c3effa904.png)<br/>箇条書きリスト|文章をリスト形式で表示します。箇条書きにしたい文章をドラッグし、アイコンをクリックしてください。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d998943aea249210da54487e7640828a.png)<br/>番号付きリスト|文章を数字のリスト形式で表示します。箇条書きにしたい文章をドラッグし、アイコンをクリックしてください。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5ed3834d0237ae930aee6cebdb1d8e38.png)<br/>ブロッククオート（引用）|文書を引用する際に使用します（段落ごと引用する場合など）|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6438a2c7a1c8e9b2062f01b618717a73.png)<br/>コードブロックの挿入|コードブロックを追加します。コードブロックしたいソース部分をドラッグし、アイコンをクリックしてください。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/92e8b22d947b761bff1fe3994c397a26.png)<br/>元に戻す|行った編集作業を元に戻すことができます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/19502810ce053dd607f14a89be7a63ef.png)<br/>やり直し|元に戻した作業をやり直すことができます。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a793d8b1523f4ac18b23d0978a5b7719.png)<br/>検索して置換|検索と置換ができます。アイコンをクリックすると下記のウィンドウが表示されます。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/8cd938bf304f62f3898d50249d98ff32.png)|
|![Image from Gyazo](https://t.gyazo.com/teams/diverta/60927c2982f24d146604a25b3be3cada.png)<br/>Templates|事前に保存したWYSIWYGテンプレートを呼び出します。|
|![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c5776fe89346736e4d450ae9a839bb16.png)<br/>他の項目を表示|隠れているアイコンを表示します。|

## アイコンツールの編集方法

WYSIWYGエディタを拡張項目で設定する場合、表示するアイコンは[コンテンツ定義編集の拡張項目](/ja/docs/management/content-structure-topics-group/#%E6%8B%A1%E5%BC%B5%E9%A0%85%E7%9B%AE)で調整が可能です。  
設定可能な項目は主に以下になります。
- 横幅
- 縦幅
- 削除するプラグイン
- カスタムカラー
- 大きなカラーパレット
- シンプルなツールバー
- フォントサイズをpx指定
- 段落挿入ボタン

### 設定例
コンテンツ定義画面の拡張項目の項目設定で以下のように設定してください。

```
横幅:800
縦幅:500
削除するプラグイン:italic、underlineにチェック
大きなカラーパレット:有効にする
```

<a href="https://diverta.gyazo.com/58604ac3a601809de5d9fe01bffd54b9" className="no-zoom" target="_blank" rel="noopener noreferrer"><img src="https://t.gyazo.com/teams/diverta/65a825e664be4e98683b5ab8a10073ea.jpg" alt="Image from Gyazo" width="799"/></a>

### 表示例

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eefa2d03928d558105921a22032db777.png)

### 削除するプラグインで指定できる文字列の一覧

項目設定の「削除するプラグイン」で、削除したいツールバー項目のチェックボックスを選択することで、ツールバーより不要なアイコンを削除できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b7c9a245c9430807bfb9b4440c7deb0.png)

選択できるツールバー項目（チェックボックスに表示される値）は以下の通りです。

|項目   |値  |
| :--- | :--- |
|   ソース  |`sourceEditing`|
|   FullScreen  |`fullScreen`|
|   見出し |`heading`|
|   文字揃え  |`alignment`|
|   ボールド    |`bold`|
|   イタリック  |`italic`|
|   アンダーライン   |`underline`|
|   取り消し線    |`strikethrough`|
|   下付き文字    |`subscript`|
|   上付き文字    |`superscript`|
|   書式のクリア    |`removeFormat`|
|   フォントサイズ   |`fontSize`|
|   文字色  |`fontColor`|
|   背景色   |`fontBackgroundColor`|
|   フォントファミリー |`fontFamily`|
|   リンク    |`link`|
|   画像挿入    |`insertImage`|
|   画像やファイルの挿入  |`ckfinder`|
|   メディアの挿入    |`mediaEmbed`|
|   表の挿入    |`insertTable`|
|   箇条書きリスト   |`bulletedList`|
|   番号付きリスト   |`numberedList`|
|   ブロッククオート（引用） |`blockQuote`|
|   コードブロックの挿入   |`codeBlock`|
|   検索して置換    |`findAndReplace`|
|   元に戻す    |`undo`|
|   やり直し    |`redo`|
|   Templates | `templates`|
|   プレースホルダー | `placeholder`|

:::tip
プラグイン全体ではなく、プラグイン内の一部のボタンだけを非表示にしたい場合は、CSSを使って特定のボタンを隠すことができます。  
ボタンの`data-cke-tooltip-text`属性を指定して、`display: none !important;`を適用します。

例えば、番号付きリストの「小文字ローマ数字」ボタンだけを非表示にする場合は、以下のCSSを[管理画面のカスタムCSS](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-wysiwyg-editor/)に追加します。

```css
button[data-cke-tooltip-text="Lower–roman"] {
  display: none !important;
}
button[data-cke-tooltip-text="小文字ローマ数字"] {
  display: none !important;
}
```

`data-cke-tooltip-text`の値はブラウザの開発者ツールで対象のボタンを調べることで確認できます。英語と日本語の両方のツールチップに対応するため、両方の言語で指定することをお勧めします。
:::

### WYSIWYG オプションで追加できる項目

項目設定の「WYSIWYG オプション」フィールドに`キー::値`の形式で設定を記述することで、デフォルトでは表示されないツールバーボタンを追加できます。複数の設定を行う場合は改行で区切ります。

|設定値   |説明  |
| :--- | :--- |
|`strikethrough::1`|取り消し線ボタンを表示します。|
|`subscript::1`|上付き文字・下付き文字ボタンを表示します。|

#### 設定例

```
strikethrough::1
subscript::1
```

## 相対パスの補完

WYSIWYGエディタ内で`/files/`から始まる相対パスはAPIで取り出す際に、KurocoFilesドメイン(`kuroco-img.app`)が自動で付与されます。

## 関連ドキュメント
- [WYSIWYG カスタムカラーの設定方法](/ja/docs/reference/wysiwyg-custom-color-settings/)
- [Iframely自動変換を利用するには？](/ja/docs/faq/how-to-auto-convert-iframes/)
- [WYSIWYGエディタに入力されたソースが自動変換されないように出来ますか？](/ja/docs/faq/can-i-prevent-sources-entered-into-the-wysiwyg-editor-from-being-automatically-converted/)
- [コンテンツ定義で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-content/#wysiwyg)


---

# WYSIWYG カスタムカラーの設定方法

> 元ページ: `reference/wysiwyg-custom-color-settings` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/wysiwyg-custom-color-settings/
> 概要: Kurocoで利用するWYSIWYGのFont ColorやFont Background Colorの色を独自に設定する方法を説明します。

Kurocoで利用するWYSIWYGの[Font Color]や[Font Background Color]の色を、WYSIWYGごとに独自に設定できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e279f0ab305bf431909a973a5d9d212a.png)
## 設定方法

設定したい[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)の編集画面にて、色を変えたいWYSIWYGの項目設定を開きます。  
「カスタムカラー」にカンマ区切りでカラーコードを入力してください。  
入力したカラーコードの色をWYSIWYGで使用できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c6b18fa200a9c66d375699c8f655709.png)

:::info
コンテンツ定義編集画面への遷移方法、WYSIWYGの項目設定方法については、  
「[コンテンツ定義](https://kuroco.app/ja/docs/management/content-structure-topics-group/#%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E5%AE%9A%E7%BE%A9%E7%B7%A8%E9%9B%86)」「[コンテンツ定義で利用できる拡張項目一覧（WYSIWYG）](https://kuroco.app/ja/docs/reference/list-of-extra-column-available-on-content/)」をご確認ください。
:::

### 設定例

下記のように設定した場合。
```
#000000,#FFFFFF,#EEEEEE,#CBFFD3,#FFFFDD,#DDFFFF,#FFDDFF,#EE0000
```
下記の表示となり、色が変わっていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44f30d139a5a5f3aebf3d8ff5c3dfe74.png)

### 注意点

- 使用している全てのWYSIWYGの項目設定に、設定して頂く必要があります。1つの記事グループ内で複数のWYSIWYGを使用している場合は注意してください。
- 1つのWYSIWYG内では同じ設定となります。例えば、[Font Color]と[Font Background Color]の色を1つのWYSIWYG内で変えることはできません。

## 16色以上の色を使用したい場合
項目設定のWYSIWYGでは、「大きなカラーパレット」を有効にすると、15色以上のカラーコードの設定が可能になります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c55b6a73a6e8979dc42d7f4bc5ad874.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9e2ff218b502a163cf63584004743ef4.png)

## 「内容」のWYSIWYGを変更する場合
[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)の[カスタムテンプレート][wysiwyg_options]に、`customColors::カラーコード1,カラーコード2,カラーコード3,,,`と記載をしてください。  

:::tip
15色までカラーコードの設定が可能です。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a675dc0bf3063350f5dcec12c0dd308.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a0b52d6f848898f95af85c668af8905.png)

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [WYSIWYG専用テンプレート](/ja/docs/management/wysiwygtemplate/)
- [Kuroco管理画面のWYSIWYGエディタに任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-wysiwyg-editor/)
