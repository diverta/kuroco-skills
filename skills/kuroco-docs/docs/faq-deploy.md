# Kurocoドキュメント: FAQ / deploy

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- GitHub Actionsのビルド&デプロイに時間がかかってしまいます。解決方法はありますか？（`how-to-reduce-artifact-file-sizes`）
- GitHubリポジトリにpushした際にエラーが表示されます。エラー解決方法を教えてください。（`i-get-an-error-message-when-i-push-to-the-github-repository`）
- ビルドの際にNode.js 12 actions are deprecatedの警告が出ますが解消できますか？（`what-is-node-js-12-actions-are-deprecated`）


---

# GitHub Actionsのビルド&デプロイに時間がかかってしまいます。解決方法はありますか？

> 元ページ: `faq/how-to-reduce-artifact-file-sizes` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-reduce-artifact-file-sizes/
> 概要: GitHub Actionsのビルド&デプロイに時間がかかってしまう要因として、以下が考えられます。

GitHub Actionsのビルド&デプロイに時間がかかってしまう要因として、以下が考えられます。

- [GitHub ActionsのCPU性能とI/O性能](#github-actionsのcpu性能とio性能が影響している場合)
- [generateのinterval設定](#generateのinterval設定が影響している場合)
- [APIリクエスト数](#apiリクエスト数が影響している場合)
- [APIリクエストのレスポンス速度](#apiリクエストのレスポンス速度が影響している場合)
- [Artifactsのファイルサイズ](#artifactsのファイルサイズが影響している場合)

## GitHub ActionsのCPU性能とI/O性能が影響している場合
GitHub ActionsのCPU性能とI/O性能に関しては、変更が難しいものになりますが、以下のような制限があります。

:::info
[GitHub Docs -> GitHub Actions -> Workflow billing & limits -> 使用制限](https://docs.github.com/ja/actions/learn-github-actions/usage-limits-billing-and-administration#usage-limits)
:::

:::info
[GitHub Docs -> GitHub Actions -> 自分のランナーをホストする -> Usage limits](https://docs.github.com/ja/actions/hosting-your-own-runners/about-self-hosted-runners#usage-limits)
:::

## generateのinterval設定が影響している場合
Nuxt.jsの場合、nuxt.config.jsのgenerateプロパティでintervalを設定している場合は、intervalの値によってはgenerateの時間が増加します。

:::info
[Nuxt generate プロパティ](https://nuxtjs.org/ja/docs/configuration-glossary/configuration-generate#interval)
:::

## APIリクエスト数が影響している場合
SSGの場合、generateで各ページを生成する度にAPIリクエストを行うため、1ページを生成する際のAPIリクエスト数が多いと、生成するページが増える度にAPIリクエスト数が増えてしまい、generateの時間にも影響が発生します。  
以下のページで、SSGでgenerateする際にAPIリクエスト数を減少させるサンプルを紹介しておりますので、ご参照ください。

:::info
[Nuxt.jsのSSGで、ページの生成時にAPIリクエストを減らす方法はありますか？](https://kuroco.app/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)
:::

## APIリクエストのレスポンス速度が影響している場合
APIのレスポンス速度が遅い要因として以下が考えられます。

- APIのキャッシュ設定が有効になっていない
- APIレスポンスのデータサイズが大きい

### APIのキャッシュ設定が有効になっていない
APIのエンドポイントにキャッシュを設定することでAPIを高速に配信できます。  
エンドポイントのキャッシュ設定については以下のページをご参照ください。

:::info
[エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
:::

### APIレスポンスのデータサイズが大きい
必要のない項目などはAPIの後処理のホワイトリスト設定などで項目を絞りましょう。  
また、例えば、Kurocoのコンテンツ定義でWYSIWYGエディタを使用している場合に、テキストを貼り付けた際、文字の装飾がインラインのスタイル属性に記述されてしまうことが原因でデータが大きくなってしまう場合があります。

例：テキストをコピー＆ペーストした際に文字の装飾が引き継がれてしまい、インラインのスタイル属性に記述される
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5525bb8358afe6fbdaed3cf0ca850ab8.jpg)
Wordファイル、PDFファイル、外部サイト等からテキストをコピーすると、スタイルを引き継いでしまいます。一度、別のテキストエディタに貼り付けて文字の装飾を外す方法があります。もしくは、貼り付けのショートカットキーを以下の方法で行うと、文字の装飾を引き継がずにテキストを貼り付けることができます。

Windowsの場合  
`Shift + Control + V`

Macの場合  
`Shift + Command + V`

## Artifactsのファイルサイズが影響している場合
GitHub Actionsでgenerateが完了した際に生成されるArtifactsのファイルサイズが大きい場合、デプロイの時間が増加してしまいます。
以下にファイルサイズを削減する方法をご案内いたします。

### 静的なリソースファイルをKurocoFilesに移行する
KurocoFilesとは、管理画面から更新ができるファイルアップロード機能です。  
画像などの静的なリソースファイルをKurocoFilesに移行することで、ソースファイル全体のファイルサイズを削減できます。  
また、KurocoFilesにアップされているファイルはCDNキャッシュされているため、高速に配信されます。

### 参考 
- [KurocoFilesの利用方法について](/ja/docs/management/file-manager/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)

### HTMLファイルのファイルサイズを減らす
構築しているサイトがSSGの場合、HTMLファイルのファイルサイズを減らすことでArtifactsのファイルサイズを削減できます。  
また、APIから配信されるデータにWYSIWYGエディタの内容が含まれる場合、テキストにインラインのスタイル属性が記述されている場合があります。そのスタイル属性もHTMLに含まれてしまうため、HTMLファイルのファイルサイズ増加の影響になってしまいます。

:::info
[APIのデータサイズが大きい](#apiのデータサイズが大きい)
:::

### SVG Spriteをファイル化して読み込む
アイコンの表示にSVG Spriteを利用しており、SVGのコードをHTMLのソースに記載している場合、ビルドした際に生成されるページの全てにSVGのコードが記載されてしまうため、ページのサイズが肥大化してしまいます。  
その場合は、SVG Spriteのコードを`svg-sprite.svg`として読み込むことでHTMLのファイルサイズを削減することが出来ます。  

### 例
```html
<svg>
    <use xlink:href="/assets/svg/sprite.svg#icon-hoge"></use>
</svg>
```

## ページの内容を非同期処理で表示する
構築しているサイトがSSGの場合、サイト全体のページ数が多いとビルドの際に生成されるファイルの量も増えてしまいます。

一覧系ページの2ページ目以降のページを静的に生成している場合、`axios`を利用し非同期処理にて2ページ目以降を表示することで生成するページ数を少なくできます。

## 関連ドキュメント
- [ファイルマネージャー](/ja/docs/management/file-manager/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [画像の動的変換について](/ja/docs/reference/api-convert-image/)
- [Nuxt.jsのSSGを使用してAPIコール回数を削減できますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-reduce-api-calls/)
- [サイト内で利用している静的ファイル（画像、JS、CSSなど）はどこに配置するのが良いでしょうか？](/ja/docs/faq/how-to-place-static-files/)
- [GitHubのArtifactsを格納するStorageの容量を節約したいのですが、方法はありますか？](/ja/docs/faq/how-do-i-free-up-storage-space-for-github-artifacts/)


---

# GitHubリポジトリにpushした際にエラーが表示されます。エラー解決方法を教えてください。

> 元ページ: `faq/i-get-an-error-message-when-i-push-to-the-github-repository` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/i-get-an-error-message-when-i-push-to-the-github-repository/
> 概要: pushするファイルにGitHubActions用のymlファイルが含まれる場合、KurocoFrontにてデプロイの際に、GitHubActions用のymlファイルを利用します。そのため、下記設定の場合にpushするとエラーが表示されます。

## pushするファイルにGitHubActions用のymlファイルが含まれる場合

KurocoFrontにてデプロイの際に、GitHubActions用のymlファイルを利用します。  
そのため、下記設定の場合にpushするとエラーが表示されます。

**設定**  

- pushするファイルに「.github/workflows」ディレクトリ配下のファイルが存在する
- GitHubでPersonal access tokensを利用している
- Personal access tokensの設定でworkflowにチェックがついていない

**エラー内容**

```
! [remote rejected] main -> main (refusing to allow a Personal Access Token to create or update workflow `.github/workflows/build.yml` without `workflow` scope)
error: failed to push some refs to 'https://github.com/GitHubアカウント/kuroco_front_nuxt_auth.git'
```

上記エラーが発生した場合、下記をご確認ください。

## エラー解消方法
GitHubより「Settings」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ab0661727d3d423e20da5d40bc6f2fa8.png)

左サイドバーより「Developer settings」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0c68445888ed2fe83888d5db443730d9.png)
「Personal access tokens」をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/94a31638113d28926814da8177d886a3.png)
ご利用しているPersonal access tokensを編集します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/52c019e009a035c5afd7f254e344e6a9.png)
「workflow」にチェックを入れます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e113c041eaa63707cd927fbf5de9ca3b.png)
画面下部の「Update token」をクリックし更新します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3601b8289672d898548ee9ce7f1784a7.png)
以上で対応完了です。これでエラーが表示されずpushできるようになります。

## 参考
GitHubのPersonal access tokensの詳細は、[GitHub Docs 個人アクセストークンを使用する](https://docs.github.com/ja/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)をご確認ください。

## 関連ドキュメント
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [GitHub](/ja/docs/management/github/)
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)


---

# ビルドの際にNode.js 12 actions are deprecatedの警告が出ますが解消できますか？

> 元ページ: `faq/what-is-node-js-12-actions-are-deprecated` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-is-node-js-12-actions-are-deprecated/
> 概要: YAMLに記載の利用モジュールのバージョンが古いと警告が表示されます。[KurocoFront]->[Github]に表示されるYAMLファイルのサンプルは警告の出ないバージョンに更新済みですが、 YAMLファイルを作成したタイミングによって、警告が表示されている場合は 以下のようにYAMLファイルを更新して解消してください。

YAMLに記載の利用モジュールのバージョンを更新すると警告の解消ができます。  
[KurocoFront]->[[Github](/ja/docs/management/github/)]に表示されるYAMLファイルのサンプルは警告の出ないバージョンに更新済みですが、YAMLファイルを作成したタイミングによっては、以下のような警告が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/381014eb61c1b5157e9954284d50fa24.png)

警告が表示されている場合は以下のようにYAMLファイルを更新して解消してください。

## 修正方法
以下の記述部分をそれぞれ`@v3`に修正します。

```
actions/checkout@v2
actions/setup-node@v2
actions/upload-artifact@v2
```

### 修正箇所
各2箇所ずつで計6箇所に記述があります。  

```diff
       - name: Checkout Repo
-        uses: actions/checkout@v2
+        uses: actions/checkout@v3
         with:
           ref: ${{ steps.get_branch.outputs.branch }}
       - name: Use Node.js
-        uses: actions/setup-node@v2
+        uses: actions/setup-node@v3
         with:
           node-version: '16.x'
       - name: Install dependencies
```

```diff
         # - name: Zip artifact for upload
         #  run: cd dist && zip ../dist.zip . -r
       - name: Archive Production Artifact
-        uses: actions/upload-artifact@v2
+        uses: actions/upload-artifact@v3
         with:
           name: ${{ steps.get_branch.outputs.sha }}-${{ github.run_id }}
           path: dist
```

```diff
     runs-on: ubuntu-latest
     steps:
       - name: Checkout Repo
-        uses: actions/checkout@v2
+        uses: actions/checkout@v3
       - name: Use Node.js
-        uses: actions/setup-node@v2
+        uses: actions/setup-node@v3
         with:
           node-version: '16.x'
       - name: Install dependencies
```

```diff
         # - name: Zip artifact for upload
         #  run: cd dist && zip ../dist.zip . -r
       - name: Archive Production Artifact
-        uses: actions/upload-artifact@v2
+        uses: actions/upload-artifact@v3
         with:
           name: ${{ github.sha }}-${{ github.run_id }}
           path: dist
```

## 関連ドキュメント
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [GitHub Actionsワークフローのアクションを最新バージョンに保つ方法はありますか？](/ja/docs/faq/how-to-keep-github-actions-up-to-date/)
