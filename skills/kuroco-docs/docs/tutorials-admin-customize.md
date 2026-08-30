# Kurocoドキュメント: チュートリアル / 管理画面カスタマイズ

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する（`apply-css-to-a-kuroco-management-screen-with-the-plugin`）
- Kuroco管理画面のWYSIWYGエディタに任意のCSSを適用する（`apply-css-to-a-kuroco-management-screen-wysiwyg-editor`）
- 管理画面プラグインを利用して、コンテンツ編集画面に任意のVueコンポーネントを適用する（`apply-vue-to-a-kuroco-management-screen-with-the-plugin`）
- コンテンツ編集画面の表示を変更する（`change-the-display-of-the-content-editing-page`）
- 管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加する（`create-custom-pages-in-the-kuroco-admin-panel-using-the-admin-panel-plugin`）
- ダッシュボードのウィジェットを利用して管理画面の表示を編集する（`edit-the-dashboard-view`）
- how-to-customize-content-edit-using-vue（`how-to-customize-content-edit-using-vue`）


---

# 管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する

> 元ページ: `tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/

[管理画面プラグイン](/ja/docs/management/management-plugin/)では任意のCSSをKurocoの管理画面に適用できます。   
任意のページにCSSを記述できるので、項目を非表示にしたり、色を変更したり、様々な使い方が可能です。  
ここでは例として、フォームの[回答](/ja/docs/management/inquiry-answer/)のページから返信テーブルやボタンを非表示にし、フォームの回答を閲覧専用として利用する方法を紹介します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8090b681aac771d077910a661688288e.png)

## 1. CSSを準備する
まずはページに適用するCSSを作成します。  
ここでは例として下記のように記述したCSSファイルを作成しました。  
Kuroco管理画面のタグのidやクラスはデベロッパーツール等で確認してください。  

```css [nodisplay_reply_items_in_the_form.css]
#table_reply{display:none;}
.buttonbox{display:none;}
h3{display:none;}
```

## 2. CSSをKurocoFilesにアップロードする
次に作成したCSSをKurocoFilesにアップロードします。  

Kurocoの管理画面から[ファイルマネージャー]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/df3ffd66d2969dea2fa1ebb4c8aa244a.png)

KurocoFiles配下にCSSのフォルダを作成し、先ほど作成したCSSファイルをドラッグ&ドロップでアップロードします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2aca3607baa01112cee0a7220800637d.png)
アップロードが完了したら、[File Path]のボタンからファイルのPathを確認しておきます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/72b28dae666a8cfa79af162501fe1376.png)
## 3. 管理画面プラグインを設定する
[環境設定] -> [管理画面プラグイン]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6cad5f13b5f39854f4fb7f8505d0fc7c.png)

管理画面プラグインのページで[追加する]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ed35fe501b668a6548ced8244bac39e.png)

下記のように入力し、[追加する]をクリックします。

| 設定項目 | 設定 |  |
| :--- | :--- | :--- |
|ステータス|有効||
|プラグイン名|回答を閲覧専用にするプラグイン||
|タイプ|CSS||
|ソース|URL:|/files/user/CSS/nodisplay_reply_items_in_the_form.css|
|対象|ページURI:|/inquiry/inquiry_reply_edit/|
||スロット名:|head|

- SourceのURLにはアップロードしたCSSファイルのPathを入力します。
- TargetのPage UriにはCSSを適用するKuroco管理画面のURLを入力します。<br/>`/management`は省略し、相対URIで指定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/63b079b3984e62b35c11557acc684767.png)

## 4. 表示を確認する
[回答](/ja/docs/management/inquiry-answer/#回答内容の確認と返信)のページを参考にフォームの回答ページにアクセスします。  
下記のようにチュートリアル冒頭のキャプチャの赤枠部分が非表示になっていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7bcdeea71ba3b0b8601ae6b7a0117b64.png)

管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する方法の説明は以上となります。 

## 編集時の注意点
- 管理画面に関しては独自に設定されたCSS/JavaScriptのバージョンアップ後の動作保証はしておりません。
- CSS/JavaScriptでの調整を起因とした不具合に関しての調査は有償対応になります。

## 関連ドキュメント
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [カスタムテンプレートの使い方を教えてください。](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)
- [管理画面プラグインでCSSを複数ページに適用することはできますか？](/ja/docs/faq/is-it-possible-to-apply-css-to-multiple-pages-using-the-admin-panel-plugin/)


---

# Kuroco管理画面のWYSIWYGエディタに任意のCSSを適用する

> 元ページ: `tutorials/apply-css-to-a-kuroco-management-screen-wysiwyg-editor` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-wysiwyg-editor/
> 概要: Kuroco管理画面のWYSIWYGエディタにCSSファイルを読み込ませて任意のCSSを適用する手順を説明します。

## 概要
Kuroco管理画面のWYSIWYGエディタにCSSファイルを読み込ませることで、コンテンツに任意のCSSを適用できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/34fde86b667ceb8949aec34d243b0786.png)

### 学べること
以下の手順でWYSIWYGエディタに任意のCSSを適用する方法を学びます。
- [WYSIWYGエディタにHTMLを書く](#wysiwygエディタにhtmlを書く)
- [CSSファイルを作成する](#cssファイルを作成する)
- [CSSをエディタに適用する](#cssをエディタに適用する)
- [スタイルの適用を確認する](#スタイルの適用を確認する)

## WYSIWYGエディタにHTMLを書く
コンテンツ定義の項目設定でWYSIWYG項目を作成し、ソースモードでHTMLを書きます。この段階では、HTMLはただのテキストリンクとして表示されます。

`<a class="style-button" href="">Button</a>`

![Image from Gyazo](https://t.gyazo.com/teams/diverta/745e8f99b4791e4cfc68eaed1da38811.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/613d71d66debe2bda59476f23012488b.png)

## CSSファイルを作成する
`content-styles.css` というCSSファイルを作成します。ファイル名は自由に命名していただいて構いません。ただし、CSSセレクタの先頭には必ず .ck-content を付けてください。

:::danger
CSSセレクタの先頭に.ck-contentが無い場合、Kuroco管理画面の表示に影響を与える可能性があります。  
WYSIWYGエディタに適用するCSSには、必ず.ck-content を付与してください。  
参考：[CKEditor-Content styles](https://ckeditor.com/docs/ckeditor5/latest/installation/advanced/content-styles.html)
:::

```css
.ck-content .style-button {
    padding: 8px 16px;
    border-radius: 8px;
    background-color: #2C7BE5;
    color: #fff;
    text-decoration: none;
}
```
このCSSファイルをファイルマネージャーにアップします。ここでは `/styles/wysiwyg/` というフォルダを作成し、その中にCSSファイルをアップロードします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9ee13d3af0893085e699f223165426ec.png)

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/15654160e8b0344689b65d140c4af2b9.png)

## CSSをエディタに適用する
### 項目毎に設定する場合
CSSを読み込ませたいWYSIWYGエディタがあるコンテンツ定義編集ページに移動します。  
項目設定でWYSIWYG項目の[カスタムテンプレート]->[カスタマイズCSS]に `/files/user/styles/wysiwyg/content-styles.css` と入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7856d9ce99651a18fd4759d963e818db.png)

### 全てのWYSIWYGに対して設定する場合
コンテンツ編集画面の全てのWYSIWYGエディタにCSSを読み込ませる場合は、コンテンツ定義の[詳細設定]->[カスタマイズCSS]に `/files/user/styles/wysiwyg/content-styles.css` と入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/390ab0c3c35600371de26821e4961bed.png)

## スタイルの適用を確認する
WYSIWYGエディタに戻り、ソースモードで先ほどと同じHTMLを入力します。ソースモードから通常モードに切り替えると、ボタンに設定したスタイルが適用されていることが確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/745e8f99b4791e4cfc68eaed1da38811.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/34fde86b667ceb8949aec34d243b0786.png)

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [WYSIWYG カスタムカラーの設定方法](/ja/docs/reference/wysiwyg-custom-color-settings/)


---

# 管理画面プラグインを利用して、コンテンツ編集画面に任意のVueコンポーネントを適用する

> 元ページ: `tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/
> 概要: 管理画面プラグインを利用して、任意のVueコンポーネントをコンテンツ編集画面に適用する設定と開発の方法を説明します。

## 概要

[管理画面プラグイン](/ja/docs/management/management-plugin/)を利用すると、任意のVueコンポーネントをKurocoの管理画面に適用できます。本チュートリアルでは、その設定と開発の方法について説明します。

### 学べること

- [管理画面プラグインを設定する](#管理画面プラグインを設定する)
    - サンプルリポジトリを利用して、管理画面プラグインを設定する方法を説明します。
- [管理画面プラグインを開発する](#管理画面プラグインを開発する)
    - ローカル環境で管理画面プラグインのVueコンポーネントを開発する方法を説明します。

### 前提条件
管理画面プラグインのVueコンポーネントを設定・開発するためには、次の前提条件が必要となります。

- npmコマンドの基本的な操作方法がわかること
- [Vue.js(v2.x)](https://jp.vuejs.org/v2/guide/)を利用してコンポーネントを開発できること
## 管理画面プラグインを設定する

次のサンプルリポジトリ上のVueコンポーネントを用いて、管理画面プラグインを設定する方法を説明します。
[diverta/management-vue-plugin-sample](https://github.com/diverta/management-vue-plugin-sample)

今回は、コンテンツ定義ID:1のコンテンツ定義にテキスト形式の拡張項目を設定し、入力フォームに[ContentsColorPickerInput](https://github.com/diverta/management-vue-plugin-sample/tree/master/packages/ContentsColorPickerInput)プラグインを適用します。`<input type="text" />`の入力フォームを次のようなカラーピッカーに差し替え、選択した色のカラーコードを設定できるようにします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3aa48f7aa7f3dc1420eeaf5bb4140e38.png)


### コンテンツの拡張項目を設定する
まずはコンテンツ定義設定にて、「テキスト」型の拡張項目を次のように設定します。

|設定項目| 値 |
| :-- | :-- |
| ID | 01 |
| 項目名 | カラーピッカー |
| 項目設定 | テキスト |

コンテンツ設定  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f23503bf013ac0d2508bb9a9bf8d9fb8.png)

コンテンツ編集  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/88e078b3bcf1742a15d7fb92eef53160.png)

### サンプルコンポーネントをインストールする

サンプルリポジトリをクローンし、カラーピッカーのパッケージが配置されているディレクトリに移動します。
```
git clone git@github.com:diverta/management-vue-plugin-sample.git
cd management-vue-plugin-sample/packages/ContentsColorPickerInput
```

次のコマンドを実行し、依存関係をインストールします。
```js
npm install
```

### コンポーネントをビルドする

次のコマンドを実行し、コンポーネントをビルドします。
```
npm run lint:fix
npm run build
```

ビルド処理が完了すると、`dist/`ディレクトリの配下にWebpackでバンドルされた次のようなファイルが出力されます。ファイル名のハッシュは、ビルドの度に異なる値が付与されます。
```
manifest.json
vendors.43ede78aa5d8feb80b64.js
ContentsColorPickerInput.b584f61c71a18c07edb8.js
```

### コンポーネントをデプロイする

生成されたファイルをデプロイし、外部からアクセスできるようにします。ファイルの配置先には任意のホスティングサービスやストレージを利用できますが、今回はファイルマネージャーの下記ディレクトリにアップロードします。

- `/files/user/mng_vue_components`

サイドメニューより[ファイルマネージャ]を開き、[KurocoFiles]を右クリックして「新しいフォルダを作成」を選択します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/984bcd7729e4920b17f9eb179391b0a7.png)

フォルダ名に`mng_vue_components`を入力し、[OK]をクリックして保存します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2357fa30c3e1080bb80eadb8b8d48e46.png)

`mng_vue_components`ディレクトリを選択した状態で[アップロード]をクリックし、先ほど生成したファイルをすべてアップロードします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f3ff78f9b6495c3bd2882ef9f36ed70a.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9539e5d69779792666a7f71ba6a380e0.png)

### 管理画面プラグインの設定を追加する

ファイルマネージャに配置したバンドルファイルを、管理画面上で読み込めるように設定します。

[環境設定] -> [管理画面プラグイン]をクリックし、設定画面を表示します。  
[追加する]をクリックし、プラグインの編集モーダルを表示します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5485bd1aa04bee9dbc168b66a458c859.png)

下記のように入力し、[追加する]をクリックします。


![Image from Gyazo](https://t.gyazo.com/teams/diverta/5da04b3f2ad3009a9c9994d0467ba1f8.png)

| 親項目 | 子項目 | 値 | 説明 |
| :--- | :--- | :--- | :--- |
| ステータス | - | 有効 | - |
| プラグイン名 | - | Color Picker Input | 任意のプラグイン名を指定します。 |
| タイプ | - | Vue | - |
| ソース | コンポーネント名 | ContentsColorPickerInput | サンプルリポジトリ上のコンポーネント名と合わせます。 |
|| URL | /files/user/mng_vue_components | コンポーネントの配置先URLを入力します。パスを変更する場合は、[rcms-js.config.js](https://github.com/diverta/management-vue-plugin-sample/blob/master/packages/ContentsColorPickerInput/rcms-js.config.js)の`publicPath`を編集し、本項目と設定内容を合わせます。<br/>Kurocoの外部にファイルを配置している場合は、絶対URL形式(`https://**`)で指定します。 |
|| マニフェストキー | vendors.\*;ContentsColorPickerInput.\* | 読み込み対象ファイルのmanifest.jsonキーを次の形式で指定します。<br/>`vendors.*;ComponentName.*` |
|対象| ページURI | /topics/topics_edit/ | コンテンツ編集画面のパスを指定します。/management/は省略する必要があります。 |
||スロット名| ext_1 | プラグイン適用対象の拡張項目の名称を、次の形式で指定します。<br/>`ext_{拡張項目ID(数値形式)}`<br/>ここでは、[コンテンツの拡張項目を設定する](#コンテンツの拡張項目を設定する)で設定した拡張項目(01)の名称を入力します。 |
||スロットパラメータ| topics_group_id=1 | プラグイン適用対象のコンテンツ定義IDを指定します。<br/>ここでは、[コンテンツの拡張項目を設定する](#コンテンツの拡張項目を設定する)で設定したコンテンツ定義のID(1)を入力します。 |
|プロップス| - | `{"defaultColor":"#000000"}` | コンポーネントに渡すpropsを指定します。<br/>指定の必要がない場合は、空欄とします。<br/>ここでは、カラーピッカーのデフォルト値を`defaultColor`として設定します。 |

### 表示・動作を確認する
コンテンツ編集画面を表示し、設定したVueコンポーネントが正しく表示されていることを確認します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3aa48f7aa7f3dc1420eeaf5bb4140e38.png)

続いて、任意の色を選択した状態でコンテンツを新規追加し、設定したカラーコードが保存されることを確認してください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d15871c1879c1668aa06ff932106b39.png)

## 管理画面プラグインを開発する

次に、管理画面プラグインの開発方法について学びます。先ほど設定したContentsColorPickerInputのソースコードをローカル環境で編集し、動作確認する手順を説明します。

管理画面プラグインを開発するためには、開発者ツールを有効化する必要があります。これを利用すると、管理画面をローカル環境の開発サーバーと同期し、コンポーネントの編集と動作確認を行うことができます。

### 開発者ツールを有効化する

[環境設定] -> [管理画面プラグイン]をクリックして、設定画面を表示します。続いて[設定する]をクリックし、プラグインの設定モーダルを開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/63955ac8d94f6e851314600aec37c7f4.png)

各項目を次のように設定し、[更新する] をクリックして保存します。

| 項目 | 値 | 説明 |
| :-- | :-- | :-- |
| 開発者ツール | 有効 | 開発者ツールを有効化します。 |
| 開発者グループ | 未選択 | 開発者ツールを利用可能なグループを指定します。<br/>管理者グループは常に利用可能となるため、その他のグループを許可する場合に設定します。今回は未選択とし、管理者のみを許可します。 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3e7a27cc9d7f27a854d581e0e42c915a.png)

保存が完了したら、画面を一度リロードします。開発者ツールが有効化されている場合、管理画面のヘッダーに開発者ツールの起動ボタンが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0932fe9b189d731b06d37849ad7b7760.png)
### 開発者ツールを設定する

[コンテンツの拡張項目を設定する](#コンテンツの拡張項目を設定する)で設定したコンテンツ定義の編集画面に移動します。

開発者ツールの起動ボタン[ `<>` ]をクリックし、設定モーダルを表示します。画面上に管理画面プラグインを設定している場合、検知されたコンポーネントの一覧が表示されます。

各項目を次のように設定し、[更新する]をクリックして保存します。

| 項目 | 値 | 説明 |
| :-- | :-- | :-- |
| 有効 | チェック | 選択したコンポーネントを開発対象として設定します。 |
| ホスト | `https://127.0.0.1:26787` | 開発サーバーのホスト名を設定します。 |
| 開発モードを有効にする | チェック | 開発者モードを有効化します。 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a05003e66d7683e1a91160b3436d526.png)

:::caution
次のように「プラグインが見つかりませんでした。」と表示される場合、プラグインの表示設定が誤っている可能性があります。[管理画面プラグインの設定を追加する](#管理画面プラグインの設定を追加する)に戻り、設定が正しいかを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6700ee58c08d157754133ca54a1e1a84.png)
:::

### 開発サーバーを起動する

ContentsColorPickerInputのディレクトリに移動し、次のコマンドを実行して開発サーバーを起動します。

```
cd management-vue-plugin-sample/packages/ContentsColorPickerInput
npm run serve:https
```

次のように実行結果が出力され、ローカル環境の`https://127.0.0.1:26787/`にWebpackの開発サーバーが立ち上がります。
```
> contents-color-picker-input@1.0.0 serve:https .../management-vue-plugin-sample/packages/ContentsColorPickerInput
> cross-env WEBPACK_DEV_SERVER=true RCMS_JS_HTTPS=true webpack-dev-server

ℹ ｢wds｣: Project is running at https://127.0.0.1:26787/
ℹ ｢wds｣: webpack output is served from /files/user/mng_vue_components

...

ℹ ｢wdm｣: Compiled successfully.
```

開発サーバーの下記URLにアクセスし、manifest.jsonを表示します。  
`https://127.0.0.1:26787/files/user/mng_vue_components/manifest.json`


SSL証明書が未設定のためエラーが発生しますが、無視できるエラーのため、このまま「127.0.0.1 にアクセスする」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9511e6e9acf96a7ac7e2896beb0715e.png)

以下のようにmanifest.jsonが表示されることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/904656f21ef7b7a7b0fd2fa34fe8d5d5.png)


:::tip
SSLエラーを無視した状態でも開発の継続は可能ですが、これを解消する場合は、ローカル環境に自己署名証明書を設定する必要があります。下記の「開発サーバーにSSL証明書を設定する」を参考に設定してください。
:::

#### 開発サーバーにSSL証明書を設定する
SSLエラーを解消した状態で開発を進める場合は、[mkcert](https://github.com/FiloSottile/mkcert)のようなツールを利用して自己署名証明書を設定します。

任意のディレクトリに移動し、`127.0.0.1` に対する自己署名証明書を作成してください。
```
mkcert -key-file rcms_js_key.pem -cert-file rcms_js_cert.pem 127.0.0.1
```

生成した証明書のパスを環境変数に設定し、`npm run serve:https`を実行することで、証明書を開発サーバーに適用できます。

```
export RCMS_JS_HTTPS_KEY_FILE=path/to/rcms_js_key.pem
export RCMS_JS_HTTPS_CERT_FILE=path/to/rcms_js_cert.pem
export RCMS_JS_HTTPS_CA_FILE=path/to/rcms_js_cert.pem
npm run serve:https
```

:::tip
Windowsの場合は、`export`の代わりに`set`を使用して以下のようになります。
:::

```
set RCMS_JS_HTTPS_KEY_FILE=(path)/rcms_js_key.pem
set RCMS_JS_HTTPS_CERT_FILE=(path)/rcms_js_cert.pem
set RCMS_JS_HTTPS_CA_FILE=(path)/rcms_js_cert.pem
npm run serve:https
```

または、以下のようにワンライナーでの変数指定も可能です。

```
RCMS_JS_HTTPS_KEY_FILE=path/to/rcms_js_key.pem RCMS_JS_HTTPS_CERT_FILE=path/to/rcms_js_cert.pem RCMS_JS_HTTPS_CA_FILE=path/to/rcms_js_cert.pem npm run serve:https
```

### コンポーネントを開発する

コンテンツ編集画面に戻り、一度リロードしてから、Vue.jsのDevToolsを表示します。ローカル環境との同期が成功している場合、検知されたコンポーネントが以下のように表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfd78fe09660c14eb2c794d3c24774b1.png)

[ContentsColorPickerInput.vue](https://github.com/diverta/management-vue-plugin-sample/blob/master/packages/ContentsColorPickerInput/src/pages/ContentsColorPickerInput.vue)の`mounted()`に次のコードを追加します。

```js
console.log('Successfully connected to dev server!');
```

コンテンツ編集画面をリロードすると、追加したログがブラウザのコンソール上に出力されることを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/505dc9015bcc1f1cf75f1155e32da3e6.png)

先ほど追加した`console.log()`を削除し、テンプレートのinput要素を次のように編集して保存します。

```markup
<!-- `:style="{ color: colorCode }"`を追加し、テキストのカラーを変更 -->
<input
    type="text"
    :name="extConfig[0].ext_col_nm"
    :value="colorCode"
    size="60"
    :style="{ color: colorCode }"
/>
```

コンポーネントのパッケージにはeslintとprettierによるコードの静的解析機能を導入しています。ファイルの保存後、ターミナル上に構文エラーが表示された場合は、次のコマンドを実行し修正してください。

```
npm run lint:fix
```

コンテンツ編集画面をリロードし、カラーピッカーで色を選択して、テキストフォームの色が変更されることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/08b1a13a14b6464ed641548174cde93f.png)

コンポーネントの編集が完了したら、以下のステップを再度実行し、変更内容を管理画面に反映します。
- [コンポーネントをビルドする](#コンポーネントをビルドする)
- [コンポーネントをデプロイする](#コンポーネントをデプロイする)

反映後、開発サーバーとの同期を解除します。開発者ツールを表示し、「開発者モードを有効にする」のチェックを外して[更新する]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9f3bfd8ba978da1d507f39e37bedf7d.png)

画面をリロードし、編集した内容が反映されていることを確認します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/96562c980f09a64b6a5d479298a69cb0.png)

## 参考情報

本チュートリアルでは、コンテンツ編集画面の拡張項目に管理画面プラグインを適用しました。プラグインは他の画面に対しても適用できますが、その設定方法は適用対象の画面要素(スロット)によって異なります。

利用可能なスロットとその設定内容については、[管理画面プラグインで利用可能なスロット一覧](/ja/docs/reference/management-plugin-slot/) を参照してください。

## 関連ドキュメント
- [管理画面プラグイン](/ja/docs/management/management-plugin/)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加する](/ja/docs/tutorials/create-custom-pages-in-the-kuroco-admin-panel-using-the-admin-panel-plugin/)
- [管理画面プラグインで利用可能なスロット一覧](/ja/docs/reference/management-plugin-slot/)
- [管理画面プラグインから認証が必要なエンドポイントにリクエストを送るにはどうしたらいいですか？](/ja/docs/faq/how-can-i-request-an-authenticated-endpoint-from-the-admin-plugin/)


---

# コンテンツ編集画面の表示を変更する

> 元ページ: `tutorials/change-the-display-of-the-content-editing-page` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/change-the-display-of-the-content-editing-page/

管理画面のコンテンツ編集画面の表示は、コンテンツ定義の「CSS」を設定することで変更が可能です。  
任意のCSSを記述できるので、非表示にしたり、色を変更したりできます。  
ここでは例としてコンテンツ編集画面の「詳細設定」を消す方法を説明します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eae282ff4587ec2c07e3eb66c14774e3.jpg)
## 不要な項目を非表示にする
### 1. コンテンツ編集画面にアクセスする
まずは表示を変更したい管理画面のページにアクセスします。  
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/96fe09be89f3ee84e0dcca1b85ba1680.png)

表示を編集したいコンテンツの[追加]をクリックします。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/e006e378e0ae322af51d8798d117eac8.png)
### 2. 消したい項目のidを確認する
次に消したい項目、ここでは「その他の設定」のidを確認します。  
デベロッパーツールを開くと、下記のように、その他の設定は`id ="section-topics-edit-details"`になっていることがわかります。  
デベロッパーツールは、Google Chromeの場合は[右クリック] -> [検証]で開くことができます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/43bd0119b7f8a7bb08d791bf6073e64e.png)
ちなみにコンテンツ編集画面の各項目は次のidで消すことができます。

|項目   |説明  |
| :--- | :--- |
|詳細設定|section-topics-edit-details|
|タグ|section-topics-edit-tags|
|公開時連携の設定|section-topics-edit-open-tab|
|公開設定|open_date_box|
|GitHub|github_workflow|
|承認ワークフロー|workflow_box|

### 3. コンテンツ定義編集のページにアクセスする 
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/96fe09be89f3ee84e0dcca1b85ba1680.png)

編集を行うコンテンツの[名前]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/569a46da17374d13357115b63f74212f.png)

コンテンツ定義編集の詳細設定にCSSが確認できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb3d76c1a2e509d88e76f2b28c0b98ce.jpg)

### 4. CSSを入力する
CSSの入力欄ではSmartyを利用しているため、テンプレートのデリミタとして解釈されないよう`{literal} {/literal}`で囲むように記述する必要があります。 
ここでは以下のように入力して、[更新する]をクリックします。

```css
{literal}
#section-topics-edit-details{display:none;}
{/literal}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/07c588ea4b750889c7e26530891fd4f3.png)

また、条件分岐も可能です。
例えば、グループIDが**10**のグループのみにCSSを適用したい場合は、以下のように入力できます。

```css
{if '10'|rcms_in_array:$smarty.session.arrGroup_id}
{literal}
#section-topics-edit-details{display:none;}
{/literal}
{/if}
```

## コンテンツ編集画面の表示を確認する
[コンテンツの編集](/ja/docs/management/content-structure-topics/#コンテンツの編集)を参考に記事の編集ページにアクセスすると、下記のように「詳細設定」が非表示になっていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7d648cca06c26710d06f8838b1bbf3e.jpg)

コンテンツ編集画面の表示を変更する方法の説明は以上となります。  

## 編集時の注意点
- Smartyが有効になっているので、`{ }`を使用する場合は、`{literal} {/literal}`で囲むように記述してください。
- 管理画面に関しては独自に設定されたCSS/JavaScriptのバージョンアップ後の動作保証はしておりません。
- CSS/JavaScriptでの調整を起因とした不具合に関しての調査は有償対応になります。

## 関連ドキュメント
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)
- [カスタムテンプレートの使い方を教えてください。](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)
- [コンテンツ編集画面に公開URLを開くボタンを追加できますか？](/ja/docs/faq/can-i-add-a-button-to-open-the-public-url-from-the-content-edit-screen/)


---

# 管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加する

> 元ページ: `tutorials/create-custom-pages-in-the-kuroco-admin-panel-using-the-admin-panel-plugin` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/create-custom-pages-in-the-kuroco-admin-panel-using-the-admin-panel-plugin/
> 概要: 管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加します。用意されたKurocoの管理画面で対応できないような処理や表示を実装したい場合にご活用ください。

## 概要
管理画面プラグインを利用して、Kuroco管理画面に任意のページを追加します。
用意されたKurocoの管理画面で対応できないような処理や表示を実装したい場合にご活用ください。

本チュートリアルでは導入の例として、サンプルプロジェクトの使い方からKuroco管理画面での設定までを説明します。

### 学べること
以下の手順で、Kuroco管理画面に任意のページを追加します。

- [Vueプラグインの準備](#vueプラグインの準備)
  - [サンプルプロジェクトをクローンする](#サンプルプロジェクトをクローンする)
  - [プロジェクトのページを更新する](#プロジェクトのページを更新する)
  - [コンポーネントをビルドする](#コンポーネントをビルドする)
- [Kuroco管理画面の設定](#kuroco管理画面の設定)
  - [APIの準備](#apiの準備)
  - [ファイルの保存](#ファイルの保存)
  - [管理画面プラグインの設定](#管理画面プラグインの設定)
- [表示の確認](#表示の確認)

### 前提条件
管理画面プラグインのVueコンポーネントを設定・開発するためには、次の前提条件が必要となります。

- npmコマンドの基本的な操作方法がわかること
- [Vue.js(v2.x)](https://jp.vuejs.org/v2/guide/)を利用してコンポーネントを開発できること

## Vueプラグインの準備
### サンプルプロジェクトをクローンする
すぐに利用できるよう以下にサンプルプロジェクトの準備があります。

リポジトリ：https://github.com/diverta/management-vue-plugin-sample  
パッケージ：https://github.com/diverta/management-vue-plugin-sample/tree/master/packages/VueSample

まずはこちらをクローンし、管理画面に任意のページを追加するパッケージが配置されているディレクトリに移動します。

```
git clone git@github.com:diverta/management-vue-plugin-sample.git
cd management-vue-plugin-sample/packages/VueSample
```

次のコマンドを実行し、依存関係をインストールします。
```js
npm install
```

### プロジェクトのページを更新する
次にKurocoの管理画面に表示される内容を調整します。

パッケージの `/management-vue-plugin-sample/packages/VueSample/src/pages/VueSample.vue` を開いて以下のように更新します。

```markup title="/management-vue-plugin-sample/packages/VueSample/src/pages/VueSample.vue"
<template>
    <div class="vue-sample">
        <h1>Vue Sample</h1>
        <ul>
            <li v-for="item in items" :key="item.topics_id">
                <a :href="`/management/topics/topics_edit/?topics_id=${item.topics_id}`">{{ item.subject }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
import Vue from 'vue';
window.rcmsJS.vue.registerVM(Vue, rcms_js_config.publicPath); // eslint-disable-line
const axios = require('axios').default;

export default {
    components: {},
    props: {
        root_api_url: {
            type: String,
            default: '',
        },
        endpoint: {
            type: String,
            default: '',
        },
    },
    created: function() {},
    mounted: async function() {
        const resp = await axios.get(this.root_api_url + this.endpoint);
        this.items = resp.data.list ? resp.data.list : [];
    },
    data() {
        return {
            items: [],
        };
    },

    computed: {},
};
</script>

<style scoped>
.vue-sample h1 {
    font-size: 24px;
    color: #007bff;
    margin-bottom: 10px;
}
</style>
```

### コンポーネントをビルドする

更新ができたら次のコマンドを実行し、コンポーネントをビルドします。
```
npm run lint:fix
npm run build
```

ビルド処理が完了すると、`/dist/`ディレクトリの配下にWebpackでバンドルされた次のようなファイルが出力されます。ファイル名のハッシュは、ビルドの度に異なる値が付与されます。

```
manifest.json
VueSample.e99068643c574d4f2040.css
vendors.43ede78aa5d8feb80b64.js
VueSample.a06fd9bd33de1d5ae13b.js
```

:::tip
ビルドは以下の方法で実行しても構いません。  
`npm run watch` を実行した状態で編集：ソースが変わると自動的にビルドされる。  
:::

以上でKurocoに読み込むVueプラグインの準備ができました。


## Kuroco管理画面の設定
### APIの準備

上記のVueプラグインはKurocoのTopics::listのエンドポイントにリクエストを送り、コンテンツの一覧を表示するように書かれています。
Vueプラグインで利用するエンドポイントの準備がない場合は以下のエンドポイントを作成します。

簡易化のためAPIリクエストに制限をかけないエンドポイントを想定しています。

|項目|設定内容|
|:--|:--|
|セキュリティ|Cookie|
|パス|topics|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|list|
|APIリクエスト制限|制限無し|
|topics_group_id|APIリクエスト制限をかけていない任意のコンテンツ定義|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b542a4021fd81726428456127b626623.png)

### ファイルの保存

生成されたファイルを外部からアクセスできるようにします。ファイルの配置先には任意のホスティングサービスやストレージを利用できますが、今回はファイルマネージャーの下記ディレクトリにアップロードします。

- `/files/user/mng_vue_components/vue-sample/`

サイドメニューより[ファイルマネージャ]を開き、[KurocoFiles]を右クリックして「新しいフォルダを作成」を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/984bcd7729e4920b17f9eb179391b0a7.png)

フォルダ名に`mng_vue_components`を入力し、[OK]をクリックして保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2357fa30c3e1080bb80eadb8b8d48e46.png)

同様に`mng_vue_components`配下に`vue-sample`のフォルダを作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c514db4e0afe1c9e3e1a6cc1690a18e3.png)

`vue-sample`ディレクトリに[Vueプラグインの準備](#vueプラグインの準備)で作成した4つのファイルを保存します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/42a75d2f11df25125c3f1a7710bcd91f.png)

### 管理画面プラグインの設定

ファイルマネージャに配置したファイルを、管理画面上で読み込むように設定します。

[環境設定] -> [管理画面プラグイン]をクリックし、設定画面を表示します。  
[追加]をクリックし、プラグインの編集モーダルを表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d857d65c09a2c08197b8820053982109.png)

下記のように入力し、[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5feecf5da18ddefdd55a134e85bc8dfa.png)

| 親項目 | 子項目 | 値 | 説明 |
| :--- | :--- | :--- | :--- |
| ステータス | - | 有効 | - |
| プラグイン名 | - | Color Picker Input | 任意のプラグイン名を指定します。 |
| タイプ | - | Vue | - |
| ソース | コンポーネント名 | VueSample | サンプルリポジトリ上のコンポーネント名と合わせます。 |
|| URL | `/files/user/mng_vue_components/vue-sample` | コンポーネントの配置先URLを入力します。パスを変更する場合は、[rcms-js.config.js](https://github.com/diverta/management-vue-plugin-sample/blob/master/packages/VueSample/rcms-js.config.js)の`publicPath`を編集し、本項目と設定内容を合わせます。<br/>Kurocoの外部にファイルを配置している場合は、絶対URL形式(`https://**`)で指定します。 |
|| マニフェストキー | `vendors.*;VueSample.*` | 読み込み対象ファイルのmanifest.jsonキーを次の形式で指定します。<br/>`vendors.*;ComponentName.*` |
|対象| ページURI | `/sample/topics_list/` | 2階層以上の任意パスを指定します。<br/>1階層のみの場合は/menu/menu/にリダイレクトされますのでご注意ください。 |
|プロップス| - | <code>&#123;<br/>"root_api_url":"CONST::ROOT_API_URL",<br/>"endpoint":"/rcms-api/1/topics"<br/>&#125;</code> | コンポーネントに渡すpropsを指定します。<br/>指定の必要がない場合は、空欄とします。<br/>ここでは、APIドメインと利用するエンドポイントのURLを設定します。<br/>管理画面プラグインに渡せるプロップスは[管理画面プラグインで利用可能なスロット一覧](/ja/docs/reference/management-plugin-slot/#プロップス)を参照してください。 |
|Add to menu|-|チェックを入れる|ページURIに任意のパスを指定してチェックを入れると、サイドメニューにリンクが追加されます。|

## 表示の確認

設定が完了すると、Kuroco管理画面のサイドメニューに追加したページURIへのリンクが表示されます。  
また、アクセスすると、`/rcms-api/1/topics`のエンドポイントで取得したコンテンツの一覧とその編集画面へのリンクが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/acd1fa0524a983c244c28495a1460dcf.png)

以上で、Kuroco管理画面に任意のページを作成できました。  
こちらのサンプルを元に任意の管理画面を実装してください。

## 関連ドキュメント
- [管理画面プラグインを利用して、コンテンツ編集画面に任意のVueコンポーネントを適用する](/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインから認証が必要なエンドポイントにリクエストを送るにはどうしたらいいですか？](/ja/docs/faq/how-can-i-request-an-authenticated-endpoint-from-the-admin-plugin/)


---

# ダッシュボードのウィジェットを利用して管理画面の表示を編集する

> 元ページ: `tutorials/edit-the-dashboard-view` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/edit-the-dashboard-view/
> 概要: Kurocoの管理画面は通常版と簡易版の2種類があります。どちらもダッシュボードのウィジェットで表示の編集ができますので、その方法について説明します。

## 概要
Kurocoの管理画面は通常版と簡易版の2種類があります。
どちらも[ダッシュボードのウィジェット](/ja/docs/management/dashboard-widget/)で表示の編集ができますので、その方法について説明します。

### 学べること
以下の手順でダッシュボードの表示を編集します。
- [ダッシュボードに表示するファイルを準備する](#ダッシュボードに表示するファイルを準備する)
- [通常版の管理画面を編集する](#通常版の管理画面を編集する)
- [簡易版の管理画面を編集する](#簡易版の管理画面を編集する)


### 前提条件
管理画面の通常版・簡易版は所属するグループの設定よって制御されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dbccdd81eb0a0b2daf164a13f78501a6.png)

また、それぞれのデフォルトの表示は以下です。
- 通常版(高機能)  
  メンバーが持つ権限の機能がすべて表示されます。  
  スーパーユーザーの場合は全ての機能が表示されます。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b4fe78b3436bc9f100c3848717e4833.png)

- 簡易版  
  ダッシュボードのウィジェットの機能を利用することを前提としているためデフォルトでは何も表示されません。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/7002d19b9bd36e872a95e2ec450b7aa6.png)

本チュートリアルを始める前提として、表示を確認するためのメンバー及びグループは事前に設定してあるものとします。

## ダッシュボードに表示するファイルを準備する
通常版・簡易版共に、システムの利用手順を示したPDFへのリンクを管理画面に表示します。  
そこでまずはKurocoのコンテンツに操作マニュアルを保存します。

### コンテンツ定義を追加する
[コンテンツ定義]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/28f823e4ee06b45d9484a1165a89adc3.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73ca9cae9408bf614888c825edde538a.png)

以下の内容を設定します。  

|項目|設定|
|:--|:--|
|名前|操作マニュアル|
|ID=1|項目設定：ファイル(Kurocofilesに保存)<br/>項目名：ファイル<br/>識別子：なし<br/>繰り返し回数：1|
|編集権限|管理者|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8da8e1456f61da6213ece72287f2d38b.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7fc435a3095ee73397ff3cb67d4bd393.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9467d3115181c3de8575b2a42113c95f.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3fae4b93d6cc322580b4a1d1695f0467.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。  
コンテンツ定義IDは後ほど使用するのでメモしておきます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b230d1ae4d8e589c51cb7132206a273.png)

### コンテンツを追加する
[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aca044ade15068a503b264e3c3c93153.png)

以下を入力し、[追加する]をクリックします。

|項目|内容|
|:--|:--|
|タイトル|任意のタイトル|
|ファイル|任意のPDFファイル|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fa094f92032807cfbe0b7e9fd0d6c4.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/72ca2599a82ca4044cd6a191d850967f.png)

同様にいくつかコンテンツを保存します。  
以上でファイルの設定は完了です。  
次のステップから通常版・簡易版のダッシュボードの編集方法を説明します。  

## 通常版の管理画面を編集する
Kuroco管理画面の表示は通常版(高機能)と簡易版があり、グループの機能でどちらを表示するかを設定できます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dbccdd81eb0a0b2daf164a13f78501a6.png)

通常版を選択した場合は、メンバーの持つ権限によって、ダッシュボード及び、サイドメニューの内容が変化します。  
そこで、ダッシュボードのウィジェットを追加する前に、権限の設定でサイドメニューの表示を調整する方法もあわせて紹介します。  

### グループの権限を調整する
通常版の管理画面の場合、サイドメニューの項目は自身が権限を持つ項目のみが表示されます。  
表示は自動で変わりますので、グループの権限を調整して、対象のメンバーの持つ権限を絞ります。  

[メンバー管理] -> [メンバー]をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/965f198812140a6c6d67b3c73124d982.png)


[メンバー一覧](/ja/docs/management/member/)からグループ名をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/58323aa4c16bb9dadca8e462df9473f1.png)

以下を設定し、[更新する]をクリックします。  

|項目|内容|
|:--|:--|
|名前|任意の名前|
|ユーザー種別|編集ユーザー|
|管理画面|通常版(高機能)|
|権限設定|以下の項目に「閲覧」「新規作成」「更新」「削除」の権限を与える。<ul><li>コンテンツ</li><li>フォーム</li><li>配信</li><li>メンバー</li><li>自分のメンバー情報</li><li>メールひな形編集</li><li>マイページ</li></ul>|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f90345287ab3eacf4ce81273c5c20e52.png)

以上で、サイドメニューに表示される内容が変化します。  

### ダッシュボードのウィジェットを追加する
次にダッシュボードのウィジェットの機能で事前に作成したPDFへのリンクを表示します。  
[環境設定] -> [ダッシュボードのウィジェット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c792bbdad2221e3073a150fe243e15bf.png)
追加をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/984e7e0f8cba646c4facc45d1446f347.png)

以下のように設定します。  
 
|項目|内容|
|:--|:--|
|名前|任意の名前|
|HTML|以下のコード|
|アクセス制限|Developer|
|管理画面|通常版|
|公開設定|公開|

``` smarty
マニュアルはこちらからご確認いただけます。<br>
{capture name='manual_method_params'}
{ldelim}
"topics_group_id":[9]
{rdelim}
{/capture}
{api_method
  var='manual_topics'
  model="Topics"
  method="list"
  version="1"
  method_params=$smarty.capture.manual_method_params|json_decode}
{if !$manual_topics.list|@is_array||$manual_topics.errors|@count>0}
  <p>ファイルを取得できませんでした。</p>
{else}
  <ul class="manual_list">
  {foreach from=$manual_topics.list item='topics'}
    {if $topics.ext_1|@empty}
      {continue}
    {/if}
    <li><a href="{$topics.ext_1.url|escape}" target="_blank">
      {$topics.subject|escape}
    </a></li>
  {/foreach}
  </ul>
{/if}

{literal}
<style>
.manual_list {
    list-style-type: disc;
}
</style>
{/literal}
```

:::tip
ダッシュボードのウィジェットでは`style`タグでcssを書く事ができます。  
また、Smarty及び、KurocoのSmartyプラグインの利用も可能です。
:::

:::caution  
`"topics_group_id":[9]`の部分はご自身のコンテンツ定義IDを使用してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a1ee85a589fb085eeda996b0e5a6b95.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7d9ecf958b64fe3bfd21fb761051c017.png)

入力ができたら[追加する]をクリックしてダッシュボードのウィジェットを追加します。  
ここで追加した通常版向けのウィジェットはダッシュボード上の「管理メモ」の上部に表示されます。

### 管理画面の表示を確認する
対象のメンバーで管理画面にログインすると、設定した表示が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/79eab5234059c65fefbf5f979765b5eb.png)


## 簡易版の管理画面を編集する
簡易版の管理画面はダッシュボードのウィジェットを利用することを前提としており、デフォルトの状態では何も表示されません。  
その代わりに、自由にHTMLを記述して管理画面の表示を作成できます。

### ダッシュボードのウィジェットを追加する
[環境設定] -> [ダッシュボードのウィジェット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c792bbdad2221e3073a150fe243e15bf.png)
追加をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d91f41bcc67f6abbd92fd7fd41621c95.png)

以下のように設定します。  
 
|項目|内容|
|:--|:--|
|名前|任意の名前|
|HTML|以下のコード|
|アクセス制限|選択なし|
|管理画面|簡易版|
|公開設定|公開|

```smarty
<div class="row">
  <div class="col-12">
    <div class="card">
      <div class="card-header">
        <!-- Title -->
        <h2 class="card-header-title fw-bold h4">
          コンテンツ更新メニュー
        </h2>
      </div>

      <div class="card-body">
        <div class="row">
          <div class="col-12 col-lg-6 col-xl-4 mb-6">
            <div class="row d-flex align-items-center mb-2 px-2">
              <div class="col-auto">
                <!-- Avatar -->
                <div class="avatar avatar-sm">
                  <div class="avatar-title font-size-lg bg-primary-soft rounded-circle text--primary">
                    <i class="fe fe-edit"></i>
                  </div>
                </div>
              </div>
              <div class="col ms-n3">
                <h3 class="d-inline h4 fw-bold mb-0 text-secondary">
                  コンテンツ
                </h3>
              </div>
            </div>
            <hr />
            <ul class="list-group list-group-flush my-n3">
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">資料</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="/management/topics/topics_edit/?topics_group_id=7">
                      <i class="fe fe-plus me-1"></i>追加
                    </a>
                    <a class="btn btn-sm btn-outline-primary"
                      href="/management/topics/topics_list/?topics_group_id=7&contents_type=15">
                      <i class="fe fe-list me-1"></i>
                      一覧
                    </a>
                  </div>
                </div>
              </li>
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">動画</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="#!">
                      <i class="fe fe-plus me-1"></i>追加
                    </a>
                    <a class="btn btn-sm btn-outline-primary"
                      href="/management/topics/topics_list/?topics_group_id=7&contents_type=17">
                      <i class="fe fe-list me-1"></i>
                      一覧
                    </a>
                  </div>
                </div>
              </li>
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">記事</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="#!">
                      <i class="fe fe-plus me-1"></i>追加
                    </a>
                    <a class="btn btn-sm btn-outline-primary"
                      href="/management/topics/topics_list/?topics_group_id=7&contents_type=18">
                      <i class="fe fe-list me-1"></i>
                      一覧
                    </a>
                  </div>
                </div>
              </li>
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">お知らせ</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="/management/topics/topics_edit/?topics_group_id=1">
                      <i class="fe fe-plus me-1"></i>追加
                    </a>
                    <a class="btn btn-sm btn-outline-primary" href="/management/topics/topics_list/?topics_group_id=1">
                      <i class="fe fe-list me-1"></i>
                      一覧
                    </a>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <div class="col-12 col-lg-6 col-xl-4 mb-6">
            <div class="row d-flex align-items-center mb-2 px-2">
              <div class="col-auto">
                <!-- Avatar -->
                <div class="avatar avatar-sm">
                  <div class="avatar-title font-size-lg bg-primary-soft rounded-circle text--primary">
                    <i class="fe fe-send"></i>
                  </div>
                </div>
              </div>
              <div class="col ms-n3">
                <h3 class="d-inline h4 fw-bold mb-0 text-secondary">
                  キャンペーン
                </h3>
              </div>
            </div>
            <hr />
            <ul class="list-group list-group-flush my-n3">
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">フォーム</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="/management/inquiry/inquiry_edit/?inquiry_id=1">
                      <i class="fe fe-settings me-1"></i>設定
                    </a>
                    <a class="btn btn-sm btn-outline-primary" href="/management/inquiry/inquiry_bn_list/?inquiry_id=1">
                      <i class="fe fe-list me-1"></i>
                      回答
                    </a>
                  </div>
                </div>
              </li>
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">配信</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="/management/magazine/magazine_edit/?magazine_id=1">
                      <i class="fe fe-settings me-1"></i>設定
                    </a>
                    <a class="btn btn-sm btn-outline-primary" href="/management/magazine/magazine_sendmail_list/?magazine_id=1">
                      <i class="fe fe-list me-1"></i>
                      一覧
                    </a>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <div class="col-12 col-lg-6 col-xl-4 mb-6">
            <div class="row d-flex align-items-center mb-2 px-2">
              <div class="col-auto">
                <!-- Avatar -->
                <div class="avatar avatar-sm">
                  <div class="avatar-title font-size-lg bg-primary-soft rounded-circle text--primary">
                    <i class="fe fe fe-user"></i>
                  </div>
                </div>
              </div>
              <div class="col ms-n3">
                <h3 class="d-inline h4 fw-bold mb-0 text-secondary">
                  メンバー管理
                </h3>
              </div>
            </div>
            <hr />
            <ul class="list-group list-group-flush my-n3">
              <li class="list-group-item px-2">
                <div class="row">
                  <div class="col d-flex align-items-center">
                    <h3 class="d-inline h4 mb-0">メンバー</h3>
                  </div>
                  <div class="col-auto">
                    <a class="btn btn-sm btn-primary" href="/management/memberregist/memberregist_column_setting/">
                      <i class="fe fe-settings me-1"></i>設定
                    </a>
                    <a class="btn btn-sm btn-outline-primary" href="/management/member/member_list/">
                      <i class="fe fe-list me-1"></i>
                      一覧
                    </a>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <div class="col-12">
            <div class="row d-flex align-items-center mb-2 px-2">
              <div class="col-auto">
                <!-- Avatar -->
                <div class="avatar avatar-sm">
                  <div class="avatar-title font-size-lg bg-primary-soft rounded-circle text--primary">
                    <i class="fe fe-mail"></i>
                  </div>
                </div>
              </div>
              <div class="col ms-n3">
                <h3 class="d-inline h4 fw-bold mb-0 text-secondary">
                  メールひな形
                </h3>
                <small class="d-block text-muted mt-1">システムから送信するメールの文面を編集できます。</small>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="list-group list-group-flush my-n3">
                  <div class="list-group-item px-2">
                    <h3 class="h5 fw-bold mb-0">
                      ログイン・リマインダー
                    </h3>
                  </div>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=62"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">
                      ログイン時のセキュリティ通知
                    </h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=77"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">
                      リマインダー 仮パスワード発行
                    </h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=76"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">
                      リマインダー パスワード変更の完了
                    </h3>
                  </a>
                </div>
              </div>
              <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="list-group list-group-flush my-n3">
                  <div class="list-group-item px-2">
                    <h3 class="h5 fw-bold mb-0">メンバー</h3>
                  </div>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=83"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">アカウント登録の完了</h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=84"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">アカウント情報編集の完了</h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=80"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">アカウント削除の完了</h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=82"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">
                      <span class="badge bg-secondary-soft me-2 p-2">管理者宛</span>アカウント登録通知
                    </h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=85"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">
                      <span class="badge bg-secondary-soft me-2 p-2">管理者宛</span>アカウント情報編集通知
                    </h3>
                  </a>
                </div>
              </div>
              <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="list-group list-group-flush my-n3">
                  <div class="list-group-item px-2">
                    <h3 class="h5 fw-bold mb-0">フォーム</h3>
                  </div>
                  <a href="/management/inquiry/inquiry_edit/?inquiry_id=1" class="list-group-item px-2">
                    <h3 class="h5 mb-0">自動返信</h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=75"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">
                      <span class="badge bg-secondary-soft me-2 p-2">管理者宛</span>新着通知
                    </h3>
                  </a>
                </div>
              </div>
              <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="list-group list-group-flush my-n3">
                  <div class="list-group-item px-2">
                    <h3 class="h5 fw-bold mb-0">メールマガジン</h3>
                  </div>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=78"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">登録の完了</h3>
                  </a>
                  <a href="/management/mailtemplateedit/mailtemplateedit_edit/?mailtemplateedit_id=79"
                    class="list-group-item px-2">
                    <h3 class="h5 mb-0">退会の完了</h3>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-12">
            <div class="row d-flex align-items-center mb-2 px-2">
              <div class="col-auto">
                <!-- Avatar -->
                <div class="avatar avatar-sm">
                  <div class="avatar-title font-size-lg bg-primary-soft rounded-circle text--primary">
                    <i class="fe fe-book-open"></i>
                  </div>
                </div>
              </div>
              <div class="col ms-n3">
                <h3 class="d-inline h4 fw-bold mb-0 text-secondary">
                  マニュアル
                </h3>
                <small class="d-block text-muted mt-1">以下のリンクから操作マニュアルをご覧いただけます。</small>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="list-group list-group-flush my-n3">

                {capture name='manual_method_params'}
                  {ldelim}
                  "topics_group_id":[9]
                  {rdelim}
                {/capture}
                {api_method
                 var='manual_topics'
                 model="Topics"
                 method="list"
                 version="1"
                 method_params=$smarty.capture.manual_method_params|json_decode}

                {if !$manual_topics.list|@is_array||$manual_topics.errors|@count>0}
                  <p>ファイルを取得できませんでした。</p>
                  {else}
                    {foreach from=$manual_topics.list item='topics'}
                      {if $topics.ext_1|@empty}
                        {continue}
                      {/if}
                      <a href="{$topics.ext_1.url|escape}" target="_blank" class="list-group-item px-2">
                        <h3 class="h5 mb-0">
                          {$topics.subject|escape}
                        </h3>
                      </a>
                    {/foreach}
                {/if}
                </div>
              </div>      
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

{literal}
<style>
h2 {
  font-size: 20px;
}
</style>
{/literal}
```

:::tip
ダッシュボードのウィジェットでは`style`タグでcssを書く事ができます。  
また、Smarty及び、KurocoのSmartyプラグインの利用も可能です。 
管理画面に適用されているCSSはデベロッパーツール等でご確認ください。
:::

:::caution
`"topics_group_id":[9]`の部分はご自身のコンテンツ定義IDを使用してください。  
:::


![Image from Gyazo](https://t.gyazo.com/teams/diverta/a96b1b2a3673e388783867764abaae05.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/386503cf1c6283049dd7cde81692fa99.png)

入力ができたら[追加する]をクリックしてダッシュボードのウィジェットを追加します。  

### 管理画面の表示を確認する
対象のメンバーで管理画面にログインすると、設定した表示が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/87a2e2be128294168b9632fdd27a2fb6.png)


## 関連ドキュメント
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)


---

# how-to-customize-content-edit-using-vue

> 元ページ: `tutorials/how-to-customize-content-edit-using-vue` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-customize-content-edit-using-vue/

準備中です。
ご不便をおかけして申し訳ございませんが、英語のドキュメントをご参照ください。

## 関連ドキュメント
- [管理画面プラグイン](/ja/docs/management/management-plugin/)
- [管理画面プラグインを利用して、コンテンツ編集画面に任意のVueコンポーネントを適用する](/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [管理画面プラグインを使ってKuroco管理画面に任意のCSSを適用する](/ja/docs/tutorials/apply-css-to-a-kuroco-management-screen-with-the-plugin/)
- [管理画面プラグインで利用可能なスロット一覧](/ja/docs/reference/management-plugin-slot/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)
