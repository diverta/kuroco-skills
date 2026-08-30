# Kurocoドキュメント: チュートリアル / コンテンツ管理（1/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- コメント機能に階層構造を追加する（`add-depth-to-the-comment-function`）
- コンテンツ定義を作成する（`adding-a-topics`）
- コンテンツの更新時にGitHub Actionsを自動実行する（`auto-run-github-with-contents-update`）
- CSVでコンテンツを一括更新する（`bulk-upload-in-csv`）
- bulk_upsert APIを利用して、任意のCSVファイルをコンテンツにインポートする（`bulk-upload-using-api`）
- コンテンツカテゴリ毎にキャッシュがクリアされるリストのエンドポイントを作成する（`create-an-endpoint-that-clears-the-cache-by-content-category`）
- バッチ処理を使用して、CSVで日次データを保存する（`how-to-implement-batch-function-exports-csv`）
- キーワード検索用文字列を用意する（`how-to-implement-cutom-body-search`）
- カスタム処理を利用して、コンテンツ定義に独自のバリデーションを実装する（`how-to-implement-original-validation-in-contents-edit-by-using-function`）
- バッチ処理を利用し、PDFの1ページ目をサムネイル画像にする（`how-to-make-thumb-from-pdf`）
- アクティビティ機能で、特定ユーザーにしか見れないコメントを残す（`how-to-only-display-comments-that-are-addressed-to-a-specific-user`）
- how-to-use-ckeditor-placeholder-feature（`how-to-use-ckeditor-placeholder-feature`）


---

# コメント機能に階層構造を追加する

> 元ページ: `tutorials/add-depth-to-the-comment-function` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/add-depth-to-the-comment-function/
> 概要: アクティビティを利用したコメント機能で、階層構造を持ったコメントの追加とその取得方法について解説します。

## 概要
アクティビティを利用したコメント機能で、階層構造を持ったコメントの追加とその取得方法について解説します。  

### 学べること
以下の手順で階層構造を持ったコメントの追加と取得をします。
- [アクティビティ定義を設定する](#アクティビティ定義を設定する)
- [APIを設定する](#apiを設定する)
- [コンテンツに階層構造を持ったコメントを追加する](#コンテンツに階層構造を持ったコメントを追加する)
- [階層構造を持ったコメントを取り出す](#階層構造を持ったコメントを取り出す)

### 前提条件
このチュートリアルでは、コンテンツの作成とSwagger UI を利用した動作の確認までを行います。  

コメントを追加するコンテンツ(お知らせ)は作成済みであることを前提とするので、まだ作成していない場合は以下のチュートリアルを参考に作成ください。  
- [KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)

また、フロントエンドへの実装は[コンテンツにコメント機能を追加する](/ja/docs/tutorials/integrate-activity-comment/)を参考に対応をお願いします。


## アクティビティ定義を設定する
ダッシュボードから[アクティビティ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/195c87d69c291c8ee15d85a5cbb112ff.png)

アクティビティ定義一覧が表示されるので[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/34c6c43ebb885fe2ce45f7cbb9b86f64.png)

以下のように設定します。  

|項目|設定|
|:--|:--|
|モジュール|コンテンツ|
|タイトル|階層付きコメント機能|
|ステータス|運用中|
|APIリクエスト制限|閲覧：閲覧可<br/>投稿：即公開|
|階層機能|有効|

:::tip
権限設定は動作確認のため閲覧可/即公開としていますが、実際の利用の際には制限をかけることをお勧めします。  
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8560bd1d4ba9388f3adf70435168ff11.png)

設定ができたら[追加する]をクリックしてアクティビティ定義の追加は完了です。  
アクティビティ定義一覧の画面に遷移するので、追加したアクティビティ定義のIDをメモしておきます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea0d79328c8a4c61901b3bea6b18dc4a.png)

## APIを設定する
### APIの作成
未承認ユーザーからの操作を許可するために、新しくAPIを作成します。  
Kuroco管理画面のAPIより「追加」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2923f2c6c82454fb1b961104a3a2393.png)

API作成画面が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9757238971ca5ead28886be1d43bf9c6.png)

下記入力し「追加する」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a55cac3c189bfcf26acf66fadfd15892.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Comment depth test|
|版|1.0|
|説明|Comment depth test|

### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/054d231d742d612294ce446115a4d3ff.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。  
- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。  
- GET
- POST
- OPTIONS

設定できたら[保存する]をクリックし、CORSの設定が完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/be11972925e4580ab57ceb3fca238416.png)

### エンドポイントの作成
エンドポイントを作成します。今回は下記エンドポイントを作成します。

- comment/insert -> コメントの追加用
- comment/list -> コメントの取得用

Comment TestのAPIで「新しいエンドポイントの追加」をクリックし、それぞれ作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/703987df651bd4e91e1f0635e3e772a8.png)

#### comment/insertエンドポイントの作成
comment/insertエンドポイントを下記設定にて作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0cc547e92eb854de49d2235a67315409.jpg)

|項目|設定内容|
| :--- | :--- |
|パス|comment/insert|
|カテゴリー|アクティビティ|
|モデル|Comment|
|オペレーション|insert|
|APIリクエスト制限|**None**|
|id|アクティビティID(35)|

設定完了後、「追加する」をクリックしcomment/insertエンドポイント完成です。 

#### comment/listエンドポイントの作成
comment/listエンドポイントを下記設定にて作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d770fa7b79ec659549b48c1f77647c0e.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/57cc8fa0eba8936c0e292342efde3e93.png)

|項目|設定内容|
| :--- | :--- |
|パス|comment/list|
|カテゴリー|アクティビティ|
|モデル|Comment|
|オペレーション|list|
|APIリクエスト制限|**None**|
|id|アクティビティID(35)|
|module_type|topics|

設定完了後、「追加する」をクリックしcomment/listエンドポイント完成です。

## コンテンツに階層構造を持ったコメントを追加する
次にSwagger UIを利用して、コンテンツに階層構造コメントを作成します。   

今回はTopics_ID=12のコンテンツに、以下のサンプルコメントを追加します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ced9fde7493e4ac24914bc607fb2930.png)

```chart title="サンプルコメント構造"
       1            9       12     13
     /  \          / \            /
    2    3        10 11          14
  / | \  | \
 4  5  6 7  8
```

まずは、1, 9, 12, 13のコメントを追加します。  
以下のデータをpostしていきます。
```json
{
  "module_id": 12,
  "name": "My Name",
  "mail": "email@example.com",
  "note": "CommentN"
}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/27a987d5902fc5e527b21682545c36b3.gif)

次に、2,3のコメントを追加するため、親となるコメントのcomment_idを確認します。 

[アクティビティ]->[階層付きコメント機能]でアクティビティ一覧を開き、先ほど追加した[Comment1]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f716ac6e6c411f26f047642e2f5c8d8f.png)

アクティビティの編集画面が開くので、URLからcomment_idを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dc97e7e9d30451d666ed6483ca873416.png)

親になるcomment_idが確認出来たら、またSwagger UIでデータをPostします。  
```json
{
  "module_id": 12,
  "name": "My Name",
  "mail": "email@example.com",
  "note": "CommentN",
  "parent_comment_id": 1
}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/17a7ccc0abb98bc21673c390961e4469.gif)

同様に繰り返し、全てのコメントを追加します。  

:::tip
短時間に同じIPアドレスから複数のコメントをPostすると`"短時間に何回もコメントできません。暫くお待ちください。"`のエラーがレスポンスされます。  
その場合は時間をおいて再開ください。
:::


## 階層構造を持ったコメントを取り出す
<!-- textlint-disable -->
<!-- 理由:カンマ区切りの数が多いって事ですが対応難しいので無視 -->
階層構造を持ったコメントを自在に取り出すには、`cnt`,`pageID`,`children_cnt`,`children_pageID`,`root`,`depth`のパラメータを組み合わせて利用します。  
<!-- textlint-enable -->

|項目|説明|
|:--|:--|
|cnt|第一層になるコメントの1ページ当たりの数を指定します。|
|pageID|第一層になるコメントの表示するページを指定します。|
|children_cnt|子コメントの1ページ当たりの数を指定します。|
|children_pageID|子コメントの表示するページを指定します。|
|root|大元になるコメントを指定します。|
|depth|何世代までの子コメントを取得するか指定します。|

### Swagger UIによる動作確認
例として、cnt=2, pageID=1, depth=2 の設定でコメントを取得してみます。  

対象のAPIから[Swagger UI]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/85a13201ca0da24619d74bd9ba903cc9.png)

Comment::list のエンドポイントのTry it Outをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0435d8115d5a379001d3edaffc53caa0.png)

以下のようにcnt=2, pageID=1, depth=2, module_id=110 を設定して、[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/68033448b77d05a85a3559b4b9008b8e.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/811db08c4517ecc565fc89adcb946e82.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/980f18108809cbae1fcae63790e96a0b.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/733fcf5763ce869a5a76ac7912d5d537.png)

コメントのレスポンスが得られるので内容を確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a567b8b11974e6226a8ebcfb4d5aca6a.png)

以下のようにレスポンスが得られていることが分かりました。  

```json
"list": [
    {
      ・・・,
      "note": "Comment1",
      ・・・,
      "children": [
        {
          ・・・,
          "note": "Comment2",
          ・・・,
        },
        {
          ・・・,
          "note": "Comment3",
          ・・・,
        }
      ]
    },
    {
      ・・・,
      "note": "Comment9",
      ・・・,
      "children": [
        {
          ・・・,
          "note": "Comment10",
          ・・・,
        },
        {
          ・・・,
          "note": "Comment11",
          ・・・,
        }
      ]
    }
]
```

図で見ると以下のようになります。  
```chart title="cnt=2, pageID=1, and depth=2"
      1            9 
     / \          / \ 
    2   3        10 11 
```

コメントの階層機能追加と、Swagger UIでの動作確認は以上となります。  
こちらの動作をフロントエンドで実装することで、様々なタイプのコメント機能を実装できますのでぜひお試しください。

### パラメータと取得できるコメント構造の例
パラメータの設定と、取得できるコメント構造の例をいかに紹介しますので、設定の際の参考にしてください。  

```chart title="All data"
       1            9       12     13
     /  \          / \            /
    2    3        10 11          14
  / | \  | \
 4  5  6 7  8
```

```chart title="cnt=2 and pageID=1"
       1            9 
     /  \          / \ 
    2    3        10 11 
  / | \  | \
 4  5  6 7  8
```

```chart title="cnt=2 and pageID=2"
       12     13
             /
            14
```

```chart title="cnt=2, pageID=1, and depth=2"
      1            9 
     / \          / \ 
    2   3        10 11 
```

```chart title="cnt=2, pageID=1, and root=2"
    2   
  / | \  
 4  5  6 
```

```chart title="cnt=2, pageID=1, children_cnt=1, children_pageID=1"
      1       9 
     /       /   
    2       10 
   / 
  4
```

```chart title="cnt=2, pageID=1, children_cnt=1, children_pageID=2"
     1       9 
      \       \ 
       3      11 
        \
         8
```

## 関連ドキュメント
- [コンテンツにコメント機能を追加する](/ja/docs/tutorials/integrate-activity-comment/)


---

# コンテンツ定義を作成する

> 元ページ: `tutorials/adding-a-topics` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/adding-a-topics/

## コンテンツ定義とは何か
コンテンツ定義とは、コンテンツ投稿時の投稿フォームのことです。  
「ブログ」や「お知らせ」等様々なコンテンツ定義の作成が可能です。
コンテンツ定義ごとにフィールドの設定ができます。

## コンテンツ定義を作成する
今回は例として、「お知らせ」用のコンテンツ定義を作成します。

### 1. コンテンツ定義画面を開く
[コンテンツ定義]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cb4b4c49242bdf74fc0758aaa4f64fb.png)

コンテンツ定義一覧画面が表示されるので、画面右上の[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab21c7a9bdf5c9825b7bdb973018a60e.png)

コンテンツ定義追加画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/99bb3d55062d2bc9bba816112076d554.png)

### 2. コンテンツ定義を設定する  
次にコンテンツ定義を設定します。今回は下記記載します。
- 名前：お知らせ
- 概要：お知らせ用のコンテンツ定義です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/59f6cb8fb50fd50d610ae41e78ee9c81.png)

### 3. フィールドを追加する  
次にフィールドを追加します。 「項目設定」の[項目追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f073a24ad2105d5b68313789b897238.png)

するとフィールドの追加画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f335d6dcd466319bf337a10c83a02d15.png)

今回は下記フィールドを設定します。
- 項目名：イメージ画像
- 項目設定：画像(KurocoFilesにアップロード)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b99db84dfc128eb10a14eea0f241d4e0.png)

以上でコンテンツ定義の設定は完了です。

### 4. コンテンツ定義を保存する  
最後に設定した内容を保存します。画面下部の[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3fad4b3513f69a7e0d17ad90aca86de2.jpg)

完了メッセージが表示されますので、「お知らせ」用のコンテンツ定義が保存されました。

## 作成したコンテンツ定義を確認する
次に作成したコンテンツ定義を確認してみましょう。  
Kuroco管理画面のグローバルメニューより[コンテンツ定義]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3cb4b4c49242bdf74fc0758aaa4f64fb.png)
コンテンツ定義一覧に、先ほど追加した「お知らせ」が表示されています。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e2a2fda4b7b9d3f2b4fcf16dae056e81.png)
## コンテンツを作成する
作成したコンテンツ定義「お知らせ」のコンテンツを追加したい場合は、コンテンツ定義一覧画面より、お知らせの[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d99e1bd02ac61d07ec37ed7647f98b97.png)

すると、お知らせ用のコンテンツ投稿画面が表示されますので、こちらからコンテンツが作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a303768683f71e0874a57681f53b82a.png)
## 参考
コンテンツ定義では、アクセス制限やバリデーション等細かい設定が可能となります。  
詳しくは管理画面マニュアルの[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)を参照ください。

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ](/ja/docs/management/content-structure-topics/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# コンテンツの更新時にGitHub Actionsを自動実行する

> 元ページ: `tutorials/auto-run-github-with-contents-update` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/auto-run-github-with-contents-update/
> 概要: このチュートリアルでは、コンテンツの更新時に GitHub Actionsを自動実行する方法を説明します

## 概要

このチュートリアルでは、コンテンツの更新時に GitHub Actionsを自動実行する方法を説明します。  
手動でコンテンツを更新した場合のほか、承認ワークフローを利用した場合とAPIを使用してコンテンツを更新した場合についても説明します。

### 学べること

コンテンツの更新時にGitHub Actionsを実行方法を学びます。
流れは以下の通りです。

- [GitHub Workflowの設定](#github-workflowの設定)
- [GitHub Actionsを使用してコンテンツを作成する](#github-actionsを使用してコンテンツを作成する)
- [承認ワークフローを使用してコンテンツを作成する](#承認ワークフローを使用してコンテンツを作成する)
- [APIを使用してコンテンツを作成する](#apiを使用してコンテンツを作成する)

### 前提条件

:::info
このページはKurocoとNuxt.jsでのプロジェクトが構築済みであり、コンテンツ一覧のページが作成されていることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
[KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
:::

## GitHub Workflowの設定

GitHubと接続し、リポジトリを設定すると、GitHubの設定画面は以下のようになります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7ded27bac16b51557d16fb6fb48ab05.png)

:::caution
GitHub Actionsを実行するには、Kuroco管理画面のGitHubページでワークフローを設定する必要があります。設定されていない場合、コンテンツ更新時にワークフロー連携を有効にしていてもGitHub Actionsが実行されません。
:::

ここでワークフローと対象ブランチを設定する必要があります。GitHubリポジトリに基づいて対応する項目を選択し、[更新する]をクリックしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f41aa26f859467a8e67b710e1a2e43f.png)

## GitHub Actionsを使用してコンテンツを作成する

[コンテンツ] -> [コンテンツ名] に移動して、[追加] をクリックして新しいコンテンツを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/987c09c2f1363fe7d2411886e21376b9.png)

ワークフローを「有効」にします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bdba30d223ad5de9454e2b64632b4fc9.png)

ワークフローを「有効」に設定してコンテンツを追加または更新すると、自動でGitHub Actionsが実行されます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/60e4abe78c8d71a89b74646a9e72bbd4.png)

ワークフローの設定を有効にして更新すると、次回更新時にもワークフローの設定はデフォルトで有効がチェックされた状態になります。  

## 承認ワークフローを使用してコンテンツを作成する

GitHub Actionsは、コンテンツが更新されたときに自動的に実行されます。  
承認ワークフローがそのコンテンツに設定されている場合は、すべてのグループが承認し、コンテンツが公開/更新されたときにGitHub Actionsが実行されます。

### 1. 承認ワークフローの作成

承認ワークフローを作成するには、サイドメニューで[オペレーション] -> [承認ワークフロー]に遷移します。ここで新しいワークフローを追加するか、既に作成されている場合は編集します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a132100af44a2955c9ceb3442023820.png)

必要な情報を入力し、承認ワークフローを作成してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/91c321d5619a3a731cb5131c4234b4f0.png)

### 2. フロー設定をする
コンテンツの作成/更新から公開までのフロー設定をします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4b18e4bbbafb733a984722690d84a601.png)

フロー設定が完了したら、コンテンツの編集にすすみます。

### 3. 新しいトピックを作成する
[コンテンツ] > [コンテンツ名] に移動して、[追加] をクリックして新しいコンテンツを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/987c09c2f1363fe7d2411886e21376b9.png)

### 4. GitHubワークフローと承認ワークフローを設定する
コンテンツが公開された後にGitHub Actionsが実行されるようGitHubのワークフロー設定を有効にします。承認ワークフローの設定も合わせて実施します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e6562c353f237e1c77a1de0d28b580cb.png)

### 5. コンテンツを更新する

コンテンツに承認フローワークフローが設定されている場合は承認待ちに移行します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/99f4b777dbc39cafd0a7b2c385f7fac5.png)

### 6. GitHub Actionsが実行されることを確認する
Contentの設定後、GitHubアクションが実行されます。 GitHub の [アクション] タブで確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a18df754f1bf9dc9e91f810353bdc2eb.png)  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6c6b814bb31224e4d6284d910ca9284a.png)

## APIを使用してコンテンツを作成する

API経由でコンテンツが更新された場合でもGitHubアクションを実行するように設定できます。このチュートリアルでは簡単化のため、承認フローを使用せずにContents APIを使用します。

承認フローを使用したコンテンツの追加方法については、[こちら](/ja/docs/faq/can-i-add-or-update-workflow-content-via-api/)を参照してください。

### 1. コンテンツ挿入APIの作成

サイドメニューからエンドポイント一覧のページに遷移します。追加をクリックし、以下のエンドポイントを追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/85123322a06e5b32aed42bdfb635bea8.png)

| 設定 | 値 |
| :--- | :--- |
| パス | エンドポイントのパス。必要に応じて入力してください。 |
| カテゴリー  | 「コンテンツ」を選択します。 |
| モデル     | Topics　v1 |
| オペレーション | コンテンツで実行する操作を選択します。(insert or update) |
| topics_group_id   | コンテンツ定義IDを入力します。|


### 2. リクエストを送信する

エンドポイントの動作はSwagger UIで確認します。  
新しく作成したエンドポイントを選択して、[Try it out]をクリックします。  
ここで、`dispatch_github_workflow`を1で渡すと、コンテンツが公開されたときにGitHub Actionsが実行されます。

承認ワークフローが使用されている場合、GitHub Actionsは承認ワークフローが完了した後に実行されます。
また、コンテンツが非公開に設定された場合や、後日公開されるように日時指定がされた場合、GitHub Actionsはコンテンツが公開されたときに実行されます。

このチュートリアルでは簡単化のため、`open_flg`を1で渡し、コンテンツを挿入するとすぐに公開されるようにします。これにより、コンテンツの追加時にすぐにGitHub Actionsが実行されます。  

コンテンツの内容を入力し、[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/674a4ea57daea71d92b736b27751d57a.png)

レスポンスでコンテンツが正常に追加されたことを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1af8abff8a5c887f3a56fb888073b6b2.png)

コンテンツ一覧に遷移し、コンテンツが追加されていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f7752d7f18a4a9a471183c78067a2e00.png)

### 3. GitHub Actionsの実行を確認する

GitHubリポジトリのActionsタブに遷移すると、GitHub Actionsが実行されたことを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8058a89201a49bd18fb1a21a6a7a0ac2.png)

## 関連ドキュメント
- [GitHub](/ja/docs/management/github/)
- [承認ワークフロー](/ja/docs/management/workflow/)
- [GitHubからKurocoFrontへソースをデプロイする方法](/ja/docs/tutorials/connect-to-github-with-kuroco-front/)
- [APIでのコンテンツ更新・追加時にワークフローは利用できますか？](/ja/docs/faq/can-i-add-or-update-workflow-content-via-api/)
- [コンテンツ更新以外の任意のタイミングでGitHubActionsを使ったdeployを行うには？](/ja/docs/faq/how-can-i-deploy-with-githubactions-at-any-time/)
- [SSGにしています。コンテンツ更新後すぐにフロントに反映させるにはどうしたらいいですか？](/ja/docs/faq/how-do-i-reflect-updated-ssg-contents-on-the-frontend/)
- [GitHubを使用せずにKurocoFrontにデプロイできますか？](/ja/docs/faq/can-i-deploy-kurocofront-without-using-github/)


---

# CSVでコンテンツを一括更新する

> 元ページ: `tutorials/bulk-upload-in-csv` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/bulk-upload-in-csv/

CSVをアップロードすることにより、コンテンツ定義単位でコンテンツを一括更新できます。
ここでは、コンテンツのCSVアップロード手順をお伝えします。

## CSVでコンテンツを一括更新する方法
### CSVファイルをダウンロードする 
まずはCSVファイルをダウンロードします。  
コンテンツ定義の一覧画面より、対象のコンテンツ定義の[ダウンロード]リンクをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/502efd73bfde6dd67970ea3e5301610b.png)

すると、ダウンロードの設定画面が表示されるので、詳細を設定し[CSVファイルをダウンロードする]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c9c88e96c2ad4bcbd42085e97718547f.png)

:::tip
ダウンロード設定画面の詳細は、[管理画面マニュアル コンテンツダウンロード](/ja/docs/management/content-structure-topics-csv/#コンテンツダウンロード)をご覧ください。
:::

### CSVファイルを編集する
次に、ダウンロードしたファイルを修正します。  
CSVファイル修正の際は、下記に注意して修正してください。

#### 必須項目  
下記は必須項目となります。
- 更新の場合
  - コンテンツID

- 新規追加の場合
  - 日付
  - カテゴリ(複数カテゴリが存在する場合は必須)
  - タイトル

#### 新規・更新・削除の挙動  
コンテンツIDにより、コンテンツの挙動が以下の通り変わります。 
- コンテンツIDが空の場合は、新規追加になります。
- コンテンツIDが存在している場合は、更新になります。
- コンテンツIDを指定して、削除フラグに1を入れると、削除になります。

#### 初期値推奨項目 
下記項目は、ダウンロードしたままの状態で修正せずにアップロードすることを推奨しています。
- グループ名

#### 画像ファイルのアップロード 
画像ファイルをアップロードする場合は、画像の項目に下記のように記述し、アップロードするファイルをzipファイルでまとめてCSVファイルと一緒にアップロードします。
- PATH::ファイル名

画像の説明を入れる場合は画像の記入欄に、次のように記入してください。
- PATH::ファイル名<br/>画像の説明のテキスト

#### 画像ファイルの削除
既存の画像ファイルを削除する場合は、画像の項目に下記のように記述します。
- PATH::DELETE

### CSVファイルをアップロードする
作成したCSVファイルをアップロードします。

コンテンツ定義の一覧画面より、CSVアップロードを実行するコンテンツ定義の[アップロード]リンクをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a5960565a7c1781c654a25ade1cc7708.png)

アップロードの設定画面が表示されるので、詳細設定し[アップロードする]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6d5dcc0306dcba78e89a615e5397d2c.png)

:::tip
アップロード設定画面の詳細は、[管理画面マニュアル コンテンツアップロード](/ja/docs/management/content-structure-topics-csv/#コンテンツアップロード)をご覧ください。
:::

ファイルがアップロードされ、コンテンツが更新されます。 

## ファイルアップロード時の注意点
以下、ファイルアップロード時の注意点となります。下記に注意してファイルアップロードをお願いします。

### アップロードできる項目について
以下の項目のみ更新できます。GCS・S3・Vimeo項目の更新には対応していません。

- 画像（KurocoFilesにアップロード）
- ファイル（KurocoFilesにアップロード）

### アップロード時の上限容量について
アップロード時の上限容量は80MBとなります。
容量が80MB以上の場合は、CSVファイルを分けて複数回アップロードを実行してください。  
また、処理時間が30秒以上になると自動的に処理がキャンセルされます。処理時間が30秒以上になる場合は、バッチ処理をご利用ください。

:::info
チュートリアル -> [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
:::

### 改行コードについて
CSVファイルの改行コードは「LF」または「CR/LF」を指定してください。

### テキストエンコーディングついて
CSVの文字コードとアップロードの設定画面で選択する文字コードが一致している必要があります。

CSVを`Shift-JIS`でダウンロードした場合は`Shift-JIS`、`UTF-8`でダウンロードした場合は`UTF-8`を指定してください。
また、CSVの編集時に文字コードが書き換わってしまわないようにご注意ください。

## 関連ドキュメント
- [コンテンツアップロード/ダウンロード](/ja/docs/management/content-structure-topics-csv/)
- [bulk_upsert APIを利用して、任意のCSVファイルをコンテンツにインポートする](/ja/docs/tutorials/bulk-upload-using-api/)
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [CSVによるコンテンツのアップロードはできますか？](/ja/docs/faq/can-i-upload-topics-using-csv-files/)
- [CSVダウンロードした多言語のコンテンツが文字化けします](/ja/docs/faq/multilanguage-content-in-downloaded-csv-file-is-garbled/)


---

# bulk_upsert APIを利用して、任意のCSVファイルをコンテンツにインポートする

> 元ページ: `tutorials/bulk-upload-using-api` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/bulk-upload-using-api/
> 概要: bulk_upsertは、複数のコンテンツを一括で更新するためのAPIオペレーションです。これを利用して、任意のフォーマットのCSVファイルをコンテンツにインポートする方法を説明します。

bulk_upsertは、複数のコンテンツを一括で更新するためのAPIオペレーションです。  
これを利用して、任意のフォーマットのCSVファイルをコンテンツにインポートする方法を説明します。

## 前提条件

CSVファイルは、次のような前提条件に基づいてインポートするものとします。

1. 対象のCSVファイルはKurocoFilesに手動でアップロードする
2. バッチ処理で毎日0:00にインポート処理を実行する
3. 前日0:00からバッチ実行開始までの間にファイルの更新があった場合にインポート処理を実行する
4. 対象のコンテンツが既に存在する場合は更新、存在しない場合は新規追加する
5. 対象のCSVファイルはUTF-8の文字コードで保存されている

## CSVファイルを用意する

まずはインポート対象のCSVデータを用意します。今回は、以下のようなモバイル端末のリストを利用します。

| item_number | item_name | category | description | status | item_color | release_date | is_public |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 00000001 | SmartPhone | SP | スマートフォン | 1 | black,white,red,blue | 2020/12/10 | TRUE |
| 00000002 | SmartPhone Lite | SP | 廉価版スマートフォン | 1 | black,white | 2021/12/10 | TRUE |
| 00000003 | Tablet | TB | タブレット | 0 | silver | 2020/1/15 | FALSE |
| 00000004 | Tablet 2 | TB | タブレット (第2世代) | 1 | silver | 2022/1/15 | TRUE |

各カラムの項目定義は以下の通りです。

| 項目名 | 項目内容 | 値 |
| :-- | :-- | :-- |
| item_number | 製品番号 | 製品毎に一意となる8桁の数値 |
| item_name | 製品名 | 任意のテキスト |
| category | 製品種別 | テキスト<br/>SP: スマートフォン<br/>TB: タブレット |
| description | 製品概要 | 任意のテキスト |
| status | 販売状況 | 数値<br/>0: 販売終了<br/>1: 販売中 |
| item_color | 製品カラー | テキスト (カンマ区切りで複数設定可)<br/>black: 黒<br/>white: 白<br/>silver: シルバー<br/>red: 赤<br/>blue: 青 |
| release_date | 発売日 | 日付 (yyyy/mm/dd) |
| is_public | 公開/非公開 | テキスト<br/>TRUE: 公開<br/>FALSE: 非公開 |

## コンテンツ定義を設定する

### 1. 項目を設計する
CSVの各行をコンテンツとしてインポートできるようにするため、まずはコンテンツ定義の項目設計をします。  

対応するデフォルト項目が存在する場合はデフォルト項目を使います。  
それ以外のものは拡張項目にマッピングし、CSVの項目と同名のSlugを設定します。

| CSV項目名 | Kuroco項目名(管理画面) | Kuroco項目名(API) | 項目形式  | 説明 |
| :-- | :-- | :-- | :-- | :-- |
| item_number | Slug | slug | - | bulk_upsertエンドポイントへのリクエスト時に使用します。<br/>オリジナルの項目は数値形式ですが、Slugにはテキスト形式の値を設定する必要があるため、次のように接頭辞を付与します。<br/>`ITEM-%%item_number%%` |
| item_name | タイトル | subject | - |  |
| category | カテゴリ | contents_type | - |  |
| release_date | 日付 | ymd | - |  |
| is_public | 公開設定 | open_flg | - |  |
| item_number | 拡張項目1 | item_number | テキスト | Slugにも同一の項目をマッピングしていますが、ここでは接頭辞のないオリジナルの値を設定します。 |
| description | 拡張項目2 | description | テキストエリア |  |
| status | 拡張項目3 | status | 単一選択 | 下記の選択肢を設定します。<br/>`0::販売終了`<br/>`1::販売中` |
| item_color | 拡張項目4 | item_color | 複数選択可 | 下記の選択肢を設定します。<br/>`black::黒`<br/>`white::白`<br/>`silver::シルバー`<br/>`red::赤`<br/>`blue::青` |

### 2. コンテンツ定義を新規作成する

各項目の設計が終わったら、CSVのインポート先となるコンテンツ定義を作成します。  
詳しい作成方法については、[コンテンツ定義を作成する
](/docs/tutorials/adding-a-topics/)を参照ください。

まずは次のように設定をします。その他の項目については、デフォルト設定のままとします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f7bff0b94228303a5a14ef95e30b6629.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fef5de4ce7dc6d12933c24b320880262.png)

| 設定項目名 | 値 | 説明 |
| :-- | :-- | :-- |
| 名前 | モバイル端末 |  |
| 更新履歴を残さない | 有効にする | 更新履歴を残さない代わりに、コンテンツの取得・更新時のパフォーマンスを向上させることができます。<br/>今回のように日次でデータを更新する必要がある場合は、設定することを推奨します。 |

次に、「1. 項目を設計する」で定義した通りに拡張項目を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe1e0b793a399932fd71a5d1dfedde4b.jpg)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c209c14feefb8dfae6eb5b177d5bd9d.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9d86fa4019b9fcd5d87859fda878f5da.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/10a54b375b87990b1959f3226f5efec3.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/515a736cb355a9ea295ab08265147304.jpg)

以上の設定が完了したら、[追加する]ボタンをクリックし、コンテンツ定義を新規追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a30d3561fa38ad0d7935af8dcd75744.png)

### 3. カテゴリを作成する

最後にコンテンツのカテゴリを作成し、category項目をマッピングできるようにします。  
詳しい設定方法については、[コンテンツカテゴリ](/ja/docs/management/content-structure-topics-category/) を参照ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/78230834ea5dfc018d0a9c6945d95fd3.png)

| カテゴリID | カテゴリ名 | 拡張項目 01 |
| :-- | :-- | :-- |
| 21 (自動採番) | スマートフォン | SP |
| 22 (自動採番) | タブレット | TB |

カテゴリIDは新規作成時に自動採番されるため、自身の環境で設定された値に置き換えてください。  
拡張項目には、インポート元CSVのカテゴリ値を設定しておきます。

## バックエンド処理の実行メンバーを設定する
バックエンド処理の実行者となるメンバーを設定します。ここで設定したメンバーIDは、後ほどバッチ処理を記述する際に利用します。

### メンバーを新規作成する

[メンバー編集](/ja/docs/management/member/#メンバーの編集)の画面にアクセスし、バックエンド処理の実行者となるメンバーを新規作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad98cfe12d99ccd7d32ae87f37e498ac.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5317c6b3d2bb8ecffb1f83f2ad15aa0a.png)

| 項目名 | 値 | 説明 |
| :-- | :-- | :-- |
| 名前 | system | バックエンド用途であることを判別しやすい値を設定します。 |
| ログインID | system | バックエンド用途であることを判別しやすい値を設定します。 |
| パスワード | (パスワード値) | 他で利用していない強固なパスワードを設定してください。 |
| グループ | Admin | ユーザー種別が「スーパーユーザー」のグループを設定します。今回は、サイト作成時にデフォルトで存在するグループ(グループID: 1)を利用します。 |

### 定数を設定する

[定数](/ja/docs/management/constants/) 画面にアクセスし、バッチ処理から参照するための定数を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2269e6c2d22f16264af601936bea31ff.png)

| 項目名 | 値 | 説明 |
| :-- | :-- | :-- |
| 名前 | SYSTEM_MEMBER_ID |  |
| 値 | 4 | 先ほど新規作成したメンバーのIDを設定します。IDは自動採番されるため、自身の環境で設定された値に置き換えてください。 |

## APIを設定する

### APIを新規作成する

[API](/ja/docs/management/api-list/)画面にアクセスし、バックエンド処理用のエンドポイントを設定するためのAPIを新規作成します。  

:::tip
同一のAPIに用途の異なるエンドポイント(フロントエンド用・バックエンド用など)を混在させると、認証の設定が複雑化します。
セキュリティ上のリスクが高まる可能性があるため、API設定は用途別に分けることを推奨します。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/806a92d175c7aabc72acfae8c267edd7.png)

| 項目名 | 値 | 説明 |
| :-- | :-- | :-- |
| タイトル | Internal API | バックエンド用途であることを判別しやすい値を設定します。 |
| 版 | 1.0 |  |
| ディスクリプション | Internal API for Backend Process |  |

APIの作成が完了したら、[セキュリティ] をクリックし、「動的アクセストークン」を選択して保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c3cb5da62f744617987511cc23bacdb7.png)

### APIエンドポイントを追加する

[新しいエンドポイントの追加] ボタンをクリックし、先ほど設定したAPIにbulk_upsertのエンドポイントを追加します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cf607c4f17cd83787d774e7297d79e07.png)

| 項目名 | 値 | 説明 |
| :-- | :-- | :-- |
| パス | mobile_devices/bulk_upsert |  |
| モデル | カテゴリー: コンテンツ<br/>モデル: Topics (v1)<br/>オペレーション: bulk_upsert |  |
| APIリクエスト制限 | GroupAuth (Admin) | [メンバーを新規作成する](#メンバーを新規作成する) で作成したメンバーが所属するグループを設定します。 |

基本設定と詳細設定には下記の値を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d31e5a270c63ef057a360205c5a5de91.png)

| パラメータ名 | 値 | 説明 |
| :-- | :-- | :-- |
| topics_group_id | 13 | 更新対象となるコンテンツ定義のIDです。事前に作成したコンテンツ定義「モバイル端末」に採番されたIDを設定します。 |
| id_reference_allow_list | slug | コンテンツ更新時のキーとして指定可能な項目を設定します。詳しくは後述します。 |
| ignore_errors | true | バリデーションエラーが発生した行を無視し、有効なコンテンツのみを追加・更新することができます。 |

**id_reference_allow_listパラメータについて**

bulk＿upsert APIで既存のコンテンツを更新する際には、対象のコンテンツを特定するためのキーとなる`topics_id`を指定する必要があります。通常であれば、以下のようにKurocoで自動採番された数値を指定します。
```
{
    "topics_id": 1,
    "slug": "ITEM-00000001",
    "subject": "Smartphone",
    ...
}
```

ここで問題になるのは、更新対象となる`topics_id`をどのように特定するかです。

他の項目についてはCSVファイルから値を変換できますが、`topics_id`はKurocoでのみ保持しているデータです。この値を特定するためには、あらかじめlist APIを呼び出して、既存のコンテンツを取得しておく処理を行う必要があります。しかし、これを実装することには以下のような問題があります。

- プログラムが複雑になる
- 処理時間が増加する

`id_reference_allow_list`は、上記を解決するために用意されたパラメータです。設定すると、topics_idの代わりに任意の項目をキーとしてコンテンツを追加・更新できます。例えば今回のように`slug`を設定した場合、次のようなリクエストが指定可能になります。

```
{
    "topics_id": "slug",
    "slug": "ITEM-00000001",
    "subject": "Updated Title",
    ...
}
```

上記のデータを送信した場合、`slug = "ITEM-00000001"`のコンテンツが既に存在すれば更新し、存在しなければ新規追加する挙動になります。これによって、Kuroco側で採番された`topics_id`を考慮せずに、元データのIDのみを利用してコンテンツを追加できるようになります。

## バッチ処理を実装する

ここまでに設定した内容を利用して、日次でインポートを行うバッチ処理を実装します。

まずは[バッチ処理編集](/ja/docs/management/batch/#バッチ処理編集)画面にアクセスし、次の内容を入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5edecba3dd5c91c3e627ce77361d830.png)

| 項目名 | 値 |
| :-- | :-- |
| タイトル | upsert_mobile_devices |
| 識別子 | upsert_mobile_devices |
| タイプ | 毎日/00:00 |

完了したら「実行内容」のエディタ上に次の処理を入力し、新規追加します。

:::caution
`{login}`や`{api_internal}`の`member_id`に変数や定数（`$smarty.const.SYSTEM_MEMBER_ID`など）を指定したテンプレートは、スーパーユーザー以外のユーザーでは保存・テスト実行ができません。また、スーパーユーザーのメンバーIDを数値で直接指定することもできません。
そのため、以下のバッチ処理はスーパーユーザー権限を持つユーザーで設定してください。
:::

```smarty
{*
    前処理
*}
{* 定数に設定したメンバーidで認証 *}
{login member_id=$smarty.const.SYSTEM_MEMBER_ID overwrite=true}

{* CSVファイルが配置されているかを確認 *}
{assign var='uploaded_csv_path' value='/files/ltd/bulk_upsert/mobile_devices.csv'}
{if !$uploaded_csv_path|rcms_file_exists}
    {logger msg1='upsert_mobile_devices' msg2='CSV file is not found'}
    {return}
{/if}
{* CSVファイルの更新日時を確認 *}
{assign var='csv_updated_at' value=$uploaded_csv_path|rcms_file_mtime}
{if $csv_updated_at < '-1 day 0:00:00'|strtotime}
    {logger msg1='upsert_mobile_devices' msg2='CSV file is not updated'}
    {return}
{/if}

{* %% bulk_upsert %% *}
```

続いて、上記コードのコメント箇所`{* %% bulk_upsert %% *}`を、実際のコンテンツ更新処理に置き換えます。

まずは[Swagger UI](/ja/docs/management/api-list/#swagger-ui)画面を開き、先ほど作成したエンドポイント `mobile_devices/bulk_upsert` を選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9eaeb310ad26ac60b390d9823ffd89d3.png)

[Request body] -> [Schema] をクリックし、 bulk_upsertエンドポイントが受け取れるリクエスト ボディの定義を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dbe337aa2a21a241b405f14ae7579928.png)

bulk_upsert APIは、以下2種類の形式でリクエスト ボディを指定できます。
今回はJSON形式を利用して処理を進めて行きます。

| 形式 | リクエスト ボディ |
| :-- | :-- |
| JSON |`{"list": [{...}]}` |
| CSVファイル | `{"file": {...}, "encoding": "..."}` |


### JSON形式で更新する場合

Request bodyのスキーマから`list`プロパティを展開すると、各項目の詳細な定義を確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/79115afeee438b9916a41d6b2bbfff7a.png)

上記のスキーマと、今回の更新対象となる項目を照らし合わせると、次のようなリクエスト ボディを指定すればいいことがわかります。

```js
{
    "list": [
        {
            "topics_id": "slug",
            "slug": "ITEM-00000001",
            "subject": "SmartPhone",
            "contents_type": 78,
            "open_flg": 1,
            "ymd": "2020-12-10",
            "item_number": "00000001",
            "description": "スマートフォン",
            "status": "1",
            "item_color": ["black", "white", "red", "blue"]
        },
        {
            "topics_id": "slug",
            "slug": "ITEM-00000001",
            // ...
        },
        // ...
    ]
}
```

エンドポイントに渡すべきリクエスト ボディの形式がわかったため、バッチ処理を実装します。先ほど作成したバッチ処理に以下のコードを追記し、[更新]ボタンをクリックしてください。

```smarty
{*
    必要な変数の初期化
*}
{* bulk_upsertエンドポイントに渡すjson body ({"list": []}) *}
{assign_array var='bulk_upsert_body'      values=''}
{assign_array var='bulk_upsert_body.list' values=''}

{assign_array   var='csv_header' values=''}{* CSVヘッダー ([]) *}
{assign         var='chunk_unit' value=1000}{* 分割アップロードする単位 *}

{*
    処理対象CSVの総行数を事前に取得
*}
{assign var='last_index' value=-1}
{read_file name='uploaded_csv' row='csv_row' type='csv' path=$uploaded_csv_path}
    {assign var='last_index' value=$last_index+1}
    {logger msg1="last_index取得処理" msg2=$last_index}
{/read_file}

{*
    更新処理
*}
{* 処理中の行を示すインデックス *}
{assign var='i' value=0}
{* CSVファイルの読み取り *}
{read_file name='uploaded_csv' row='csv_row' type='csv' path=$uploaded_csv_path}
    {if !$csv_row|@is_array}
        {logger msg1='upsert_mobile_devices' msg2='Invalid csv row' msg3=$csv_row}
    {elseif $i === 0}
        {* CSVヘッダーの取得 *}
        {assign var='csv_header' value=$csv_row}
        {$csv_header|@rcms_json_encode}
        {logger msg1="CSVヘッダーの取得" msg2=$csv_row}
    {else}
        {logger msg1="CSV内容の取得"}
        {* CSV行の変換 *}
        {assign_array var='topics'           values=''}
        {assign       var='topics.topics_id' value='slug'}{* slugをキーとして追加/更新 *}
        {foreach from=$csv_row key='k' item='v'}
            {assign var='col_name'   value=$csv_header[$k]}{* CSVの項目名を取得 *}
            {if     $col_name == 'item_number'}
                {* 製品番号 *}
                {assign var='topics.slug'        value="ITEM-`$v`"}
                {assign var='topics.item_number' value=$v}
            {elseif $col_name == 'item_name'}
                {* 製品名 *}
                {assign var='topics.subject' value=$v}
            {elseif $col_name == 'category'}
                {* カテゴリ *}
                {if     $v == 'SP'}
                    {assign var='topics.contents_type' value=78}
                {elseif $v == 'TB'}
                    {assign var='topics.contents_type' value=79}
                {/if}
            {elseif $col_name == 'item_color'}
                {* カラー *}
                {assign var='topics.item_color' value=','|explode:$v}
            {elseif $col_name == 'release_date'}
                {* 発売日 *}
                {strtodate var='topics.ymd' format='Y-m-d' timestamp=$v}
            {elseif $col_name == 'is_public'}
                {* 公開/非公開 *}
                {if $v == 'TRUE'}
                    {assign var='topics.open_flg' value=1}
                {else}
                    {assign var='topics.open_flg' value=0}
                {/if}
            {else}
                {* その他 *}
                {assign var="topics.`$col_name`" value=$v}
            {/if}
        {/foreach}
        {* JSON bodyに追記 ({"list": [..., {...}]}) *}
        {assign var='bulk_upsert_body.list.' value=$topics}
    {/if}
    {* $chunk_unitで定義した件数毎に分割して更新 *}
    {if $bulk_upsert_body|@count === $chunk_unit ||
        ($i === $last_index && $bulk_upsert_body|@count > 0)}
        {* bulk_upsertエンドポイントへのリクエスト (_async=trueパラメータを付与し、バッチ処理で実行) *}
        {api_internal
            var='bulk_upsert_response'
            status_var='bulk_upsert_status'
            endpoint='/rcms-api/23/mobile_devices/bulk_upsert?_async=true'
            method='POST'
            queries=$bulk_upsert_body
            use_current_session=1}
        {* 失敗した場合ログに出力 *}
        {if !$bulk_upsert_status || $bulk_upsert_response.errors}
            {logger msg1='upsert_mobile_devices' msg2='Request failed' msg3="index: `$i`" msg4=$bulk_upsert_response}
        {/if}
        {* JSON bodyの初期化 ({"list": []}) *}
        {assign_array var='bulk_upsert_body.list' values=''}
    {/if}
    {logger msg1=$i msg2=$last_index msg3=$topics msg4=$csv_row}
    {assign var='i' value=$i+1}
{/read_file}
```

<!-- textlint-disable -->
<!-- 理由:1文の文字数警告がでるがURL部分のせいなので無視 -->

:::caution
`/rcms-api/23/mobile_devices/bulk_upsert`の部分はご自身のエンドポイントのURLを使用してください。
`{assign var='topics.contents_type' value=78}`、`{assign var='topics.contents_type' value=79}`の部分は自身のカテゴリIDを使用してください。
:::
<!-- textlint-enable -->
処理の内容について補足します。

**CSVファイルの読み取りについて**

`read_file`は、テキストデータを1行ごとに読み取るためのプラグインです。`type`パラメータに`csv`を指定すると、CSVファイルの読み取りに利用できます。  
`read_file`で読み取れる文字コードはUTF-8のみです。  

```smarty
{read_file name='uploaded_csv' row='csv_row' type='csv' path=$uploaded_csv_path}
    {* ... *}
{/read_file}
```

CSVの行データは`row`パラメータで指定した変数名`$csv_row`にアサインされます。`{read_file}{/read_file}`のブロック内に次の処理を記述することで、データの内容を確認できます。
```smarty
{$csv_row|@rcms_json_encode}
```

出力されるのは以下のような配列データです。これらの値を項目定義に基づいて変換することで、リクエスト ボディを生成しています。
```
["00000001", "SmartPhone", "SP", "スマートフォン", "1", "black,white,red,blue", "2020/12/10", "TRUE"]
```

**コンテンツの追加・更新について**

コンテンツの追加・更新をする`bulk_upsert`エンドポイントの呼び出しには、`api_internal`プラグインを利用します。詳しい利用方法については、[オリジナル処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)を参照ください。

```smarty
{api_internal
    var='bulk_upsert_response'
    status_var='bulk_upsert_status'
    endpoint='/rcms-api/23/mobile_devices/bulk_upsert?_async=true'
    method='POST'
    queries=$bulk_upsert_body
    use_current_session=1}
```

エンドポイントのパスには、APIの処理を非同期で実行するための`_async=true`パラメータを付与しています。

通常、エンドポイントの呼び出しは同期的に行われます。リクエストの送信後は処理が完了するまで待つ必要があります。しかし、bulk_upsert APIは大量のコンテンツを一括で扱う都合上、CSVのデータ数によっては処理の完了までに時間が掛かり、タイムアウトが発生します。

`_async=true`パラメータを利用すると、リクエスト時には追加・更新処理を実行せず、バッチ処理の登録のみを行い即時にレスポンスを返します。呼び出したAPIの処理は呼び出し元とは別のプロセス上で実行されるため、タイムアウトの問題を回避できます。更新対象データの件数が多い場合に指定してください。

## 動作の確認をする
以上で、設定は完了したので動作の確認をします。  
まずはCSVファイル(`mobile_devices.csv`)をバッチ処理で指定したディレクトリ(`/ltd/bulk_upsert`)に設置します。
KurocoFiles(Private)のフォルダが`ltd`になるので配下に`bulk_upsert`のフォルダを作成し、CSVファイルを設置ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9cf8603faace864ed3669f67d9b807e2.png)

次に、先ほど作成したバッチ処理にアクセスし、[すぐに実行する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6caeef67abb1ea4ed8369e5d1169e678.png)

「モバイル端末」のコンテンツ一覧を確認すると、CSVからコンテンツが登録されていることが分かります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7c75029d47b579d623c9a3e39384d37c.png)

以上で動作の確認が完了です。

## 関連ドキュメント
- [バッチ](/ja/docs/management/batch/)
- [定数](/ja/docs/management/constants/)
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？](/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/)


---

# コンテンツカテゴリ毎にキャッシュがクリアされるリストのエンドポイントを作成する

> 元ページ: `tutorials/create-an-endpoint-that-clears-the-cache-by-content-category` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/create-an-endpoint-that-clears-the-cache-by-content-category/
> 概要: このチュートリアルでは、API::api_request エンドポイントで Topics::list をラップし、コンテンツカテゴリごとにキャッシュがクリアされる仕組みを持つリスト用エンドポイントの作成方法を解説します。

## 概要
管理画面からコンテンツを更新すると、同じコンテンツ定義IDが設定されたTopicsのエンドポイントのキャッシュがクリアされます。
そのため、Topics::listのエンドポイントは、コンテンツが更新されるたびにキャッシュがクリアされ、常に最新のデータが取得される仕組みです。

しかし、キャッシュをそこまで頻繁にクリアする必要がない場合や、同一カテゴリ内でのみキャッシュをクリアしたい場合には、
API::api_request エンドポイントで Topics::list をラップする方法が有効です。これにより、コンテンツの更新時にキャッシュがクリアされなくなり、キャッシュのヒット率を高めることができます。
（ただし、この方法を採用する場合は、キャッシュの管理を独自に設計・設定する必要がある点に留意してください。）

たとえば、Topics::list を使用してカテゴリ（content_type）を指定している場合でも、コンテンツ定義IDが同じであれば、別のカテゴリのコンテンツ更新によってもキャッシュがクリアされてしまいます。

このチュートリアルでは、API::api_request エンドポイントで Topics::list をラップし、コンテンツカテゴリごとにキャッシュがクリアされる仕組みを持つリスト用エンドポイントの作成方法を解説します。

### 学べること
以下の手順で独自にキャッシュの制御を行うエンドポイントを作成します。
- [Topics::listをラップするエンドポイントを作成する](#topicslistをラップするエンドポイントを作成する)
- [キャッシュのクリアをするトリガーを設定する](#キャッシュのクリアをするトリガーを設定する)

### 前提条件
- Topics::listのエンドポイントが無い場合は事前に作成してください。
- コンテンツカテゴリは1コンテンツに1つ設定する運用を想定します。

## Topics::listをラップするエンドポイントを作成する
### カスタム処理を作成する

まず、Topics::listをラップするためのカスタム処理を作成します。
[オペレーション] -> [カスタム処理] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

画面右上の [追加] ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

カスタム処理編集画面で以下の設定を行います：

| 項目 | 入力値 |
| :--- | :--- |
| タイトル | `get_topics_list_by_category` |
| 識別子 | `get_topics_list_by_category` |
| 処理 | 以下の内容 |

```smarty
{api_internal
    endpoint='/rcms_api/1/topics/list/1'
    method='GET'
    query="contents_type[]=`$smarty.request.data_id`"
    direct=true
    var='response'
    status_var='status'}

{assign var="data" value=$response}
```

:::caution
エンドポイントはご自身の環境で利用するTopics::listのエンドポイントを指定してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a66b41d87f9bcc0c2f00eb4bbc671c80.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1f1e226038de72afeab84efefb3f9805.png)

[追加する] ボタンをクリックしてカスタム処理を追加します。

### エンドポイントを作成する

次に、作成したカスタム処理を呼び出すAPI::api_requestエンドポイントを作成します。

ご利用のエンドポイント一覧画面に遷移します。  
ここでは、[API] -> [Default] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6f8cae1d30e40c100cf114feb8f9944.png)

[追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e4d1bcc9d51961220ec5fa934c66b266.png)

エンドポイント設定ダイアログで以下を設定し、[追加する] をクリックして保存します。

| 項目 | 設定内容 |
| :--- | :--- |
|パス|	topics/list/wrapper |
|カテゴリー| API |
|モデル| Api |
|オペレーション| request_api |
|キャッシュ|86400|
|name|カスタム処理の識別子(get_topics_list_by_category)|
|use_path_param|有効にする|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4b05d6ada682c741dd4e36d1be28415e.png)


### 動作確認

作成したエンドポイントの動作を確認します。
API一覧画面で [Swagger UI] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c1f7b355a07ff160d5c5cbcb71720706.png)

作成した `topics/list/wrapper` エンドポイントを選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/57763f36d1f49f3c166e49a498f40098.png)

[Try it out] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d7ab203317ef292d6eb5fa3311af6e17.png)

data_idに任意のカテゴリIDを入力し、[Execute] をクリックして実行します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/793f07a7268588d66a5380ad942fde78.png)

レスポンスコードが200で正常に応答されること、また、2回目以降のリクエストに対してはレスポンスヘッダーの Age に値が設定されており、キャッシュが利用されていることを確認してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5f605f113883308235f776e2a6caeabb.png)

## キャッシュのクリアをするトリガーを設定する

### カスタム処理を作成する

コンテンツ更新時に特定のURLのエンドポイントのみキャッシュクリアをするトリガー用のカスタム処理を作成します。  
[オペレーション] -> [カスタム処理] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

画面右上の [追加] ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)

カスタム処理編集画面で以下の設定を行います：

| 項目 | 入力値 |
| :--- | :--- |
| タイトル | `clear_wrapped_endpont_cash` |
| 識別子 | `clear_wrapped_endpont_cash` |
|トリガー|<ul><li>モジュール：コンテンツ</li><li>トリガー：コンテンツの更新後</li><li>対象：任意のコンテンツ定義</li></ul>|
| 処理 | 以下の内容 |

```smarty
{assign_topics_detail var='topics_data' topics_id=$topics_id }
{purge_cdn_cache api_endpoint="/rcms-api/1/topics/list/wrapper/`$topics_data.contents_type`"}
```

:::caution
エンドポイントはご自身の環境で利用するTopics::listのエンドポイントを指定してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ba67d58e6e08df9f29498584367be5dc.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7913ac54895aa3b7c0fc44bd4ea5465d.png)

[追加する] ボタンをクリックしてカスタム処理を追加します。

### 動作確認

トリガーの動作を確認します。  
対象のコンテンツ定義でコンテンツを更新します。

更新後、該当カテゴリのエンドポイントのキャッシュがクリアされていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fd2a96e8bb6cc93fe6a3098cd2520e00.png)

他のカテゴリのキャッシュは影響を受けていないことを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6afaf5efbb3825e9fa22543a96957552.png)


以上で、Topics::list をラップし、コンテンツカテゴリごとにキャッシュがクリアされる仕組みを持つリスト用エンドポイントの作成は環境です。
本チュートリアルでは、コンテンツの更新時にのみキャッシュクリアを実行しています。コンテンツの追加時など、別のタイミングでもキャッシュをクリアしたい場合は、必要なトリガーを設定したカスタム処理を作成してください。

## 関連ドキュメント

- [エンドポイントの設定方法](/docs/tutorials/configure-endpoint/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/docs/tutorials/creating-a-custom-function-endpoint/)
- [APIキャッシュクリアのタイミングと範囲](/docs/reference/cache-clear-operation/)
- [カスタム処理に利用できるトリガと変数の一覧](/docs/reference/trigger-variables/)
- [Smartyプラグイン](/docs/reference/smarty-plugin/)


---

# バッチ処理を使用して、CSVで日次データを保存する

> 元ページ: `tutorials/how-to-implement-batch-function-exports-csv` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-batch-function-exports-csv/
> 概要: バッチ処理は時間のかかる処理や定期的に実行したい処理に使用します。今回は、日次でコンテンツをCSVに保存する処理を実装します。

## 概要
バッチ処理は時間のかかる処理や定期的に実行したい処理に使用します。  
今回は、日次でコンテンツをCSVに保存する処理を実装します。

### 前提条件
このチュートリアルでは以下の条件でCSVを保存します。
- 毎日00:00にバッチ処理が動作します。
- `topics_group_id=5` に所属し、前日に更新されたコンテンツを取得します。
- 保存する内容はコンテンツID、タイトル、本文、拡張項目1、最終更新日です。
- 取得したコンテンツは日毎にファイルを作成し、 /files/user/topics_log/topics_yyyy-mm-dd.csv に保存します。

## バッチ処理を作成する
それではバッチ処理を作成します。

### 1. バッチ処理の一覧画面を表示する  
メニューの[オペレーション] -> [バッチ処理] をクリックします。 
![Image from Gyazo](https://t.gyazo.com/teams/diverta/590ab86b5450b6f31d6d035f4137a2ae.png)


### 2. バッチ処理の編集画面を表示する 
バッチ処理一覧画面の右上の [追加] をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5cc6b43be0c38cdd8a98ef3886f74d64.png)

すると、バッチ処理編集画面が表示されます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c871fd93afebf3eee702aca26673f79.png)

### 3. タイトル・識別子を記入する
それではバッチ処理を作成していきます。  
まずはタイトルと識別子に記入します。今回は下記のように記入します。

- タイトル：日次コンテンツ出力
- 識別子：sample1_export_topics
- バッチ: 毎日 00:00
- メンバーID: 未指定

:::tip
タイトル・識別子は他のバッチ処理と重複できません。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/69ac2a36346ae3bf157a4bec475b8b7a.png)

### 4. コンテンツ保存処理を記述する
次に、実際の処理を記述します。

エディタ内にデータを追加する処理を記述していきます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/48d13fbf6692cd5590fc71e8c3164d87.png)

**ヘッダーを出力する**  
まずはCSVのヘッダー行を一時ファイルに出力します。

エディタに下記記入します。

:::caution
２行目の`topics_group_id value=5` は、ご自身のサイトに存在するコンテンツ定義のIDと置き換えて下さい。
:::

```smarty
{assign var=empty_array value='[]'|json_decode:1}
{assign var=topics_group_id value=5}

{* 管理者として実行 *}
{login member_id=1}

{* コンテンツ定義の取得 *}
{capture name=method_params}{ldelim}
"topics_group_id": [{$topics_group_id}],
"ext_config_flg": true
{rdelim}
{/capture}
{assign var=method_params value=$smarty.capture.method_params|json_decode:1}
{api_method
    var=topics_group
    model="TopicsGroup"
    method="details"
    version="1"
    method_params=$method_params
}

{* ヘッダー行の作成 *}
{assign var=header_columns value=$empty_array}
{append var=header_columns index=topics_id    value="コンテンツID"}
{append var=header_columns index=subject      value="タイトル"}
{append var=header_columns index=contents     value="本文"}
{* 拡張項目 *}
{foreach from=$topics_group.ext_config item=config}
    {if $config.ext_col_nm eq 'ext_1'}
        {append var=header_columns index=$config.ext_col_nm value=$config.title}
    {/if}
{/foreach}
{append var=header_columns index=update_ymdhi value="最終更新日"}

{write_file var=path value=$header_columns}
{write_file path=$path value="\n" is_append=1}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/77219ae693ecbc775c3c57e5eda0a8f5.png)

**コンテンツを取得する処理を記述する**  
続いて、コンテンツを取得してヘッダー行に続けて書き込みます。

エディタに下記記入します。
```smarty
{* 昨日更新されたコンテンツの取得 *}
{assign var=from_date value="-2 day"|strtotime|date_format:"%Y-%m-%d"}
{assign var=to_date value="-1 day"|strtotime|date_format:"%Y-%m-%d"}
{capture name=method_params}{ldelim}
    "topics_group_id": [{$topics_group_id}],
    "cnt": 100,
    "filter": "update_ymdhi <= \"{$to_date}\" AND update_ymdhi > \"{$from_date}\""
{rdelim}{/capture}
{assign var=method_params value=$smarty.capture.method_params|json_decode:1}
{api_method
    var=topics_list
    model="Topics"
    method="list"
    version="1"
    method_params=$method_params
}

{if $topics_list.errors|@count eq 0 && $topics_list.pageInfo.totalPageCnt > 0}
    {section name=pager loop=$topics_list.pageInfo.totalPageCnt}
        {assign var=request_params value=$empty_array}
        {append var=request_params index=pageID value=$smarty.section.pager.iteration}
        {api_method
            var=topics_list
            model="Topics"
            method="list"
            version="1"
            method_params=$method_params
            request_params=$request_params
        }
        {foreach from=$topics_list.list item=topics}
            {assign var=row value=$empty_array}
            {foreach from=$header_columns item=_v key=index}
                {append var=row index=$index value=$topics.$index}
            {/foreach}
            {write_file path=$path value=$row is_append=1}
            {write_file path=$path value="\n" is_append=1}
        {/foreach}
    {/section}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/13975995f946142b23ab438b30211409.png)

:::tip
バッチ処理内部であっても一度に多数の件数を取得するとメモリオーバーとなることがあります。
ページング機能を利用することを推奨します。
:::

**データを保存する**  
最後に、一時ファイルをアクセス可能なディレクトリに保存します。

エディタに下記記入します。

```smarty
{put_file tmp_path=$path path="/files/user/topics_log/topics_"|cat:$to_date|cat:".csv"}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4e85e15ac6362ef1be14240b9635df8.png)

### 6. バッチ処理を保存する 
処理の記述が完了したら、[追加する] ボタンをクリックして保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f4dcd6847496332b8adf3ac53ea1ffe6.jpg)

以上でバッチ処理の完成です。

### 7. ファイルを確認する
バッチ処理の実行時刻以降、ファイルマネージャーからCSVファイルを取得できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94de3e61ccffad0694db44aefbed4409.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c49edd0043c6e13bf44f7ab348424cda.png)

## 関連ドキュメント
- [カスタム処理を利用して、CSV出力されるデータ構造を変更する](/ja/docs/tutorials/how-to-implement-original-function-into-the-postprocess/)
- [APIをJSON以外のフォーマットでレスポンスできますか？](/ja/docs/faq/how-can-i-response-csv-format)


---

# キーワード検索用文字列を用意する

> 元ページ: `tutorials/how-to-implement-cutom-body-search` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-cutom-body-search/
> 概要: コンテンツの項目とは別に、キーワード検索で検索対象となる文字列を用意することが可能です。今回はコンテンツに紐づいたメンバーのプロフィールが検索対象となるように設定します。

## 概要
コンテンツの項目とは別に、全文検索用の文字列を用意できます。  
全文検索用の文字列はコンテンツ定義のキーワードテンプレートでSmartyを使って設定できるため、登録されたコンテンツの中から検索に使う文字列を追加・削除したり、関連情報でコンテンツに紐づく別のコンテンツやメンバー情報を検索用の文字列に追加したりできます。  
また、キーワード検索時にこのテンプレートのみを利用するようになるため、検索のパフォーマンスが向上します。

今回は講演会のスケジュールをテーマに、コンテンツに紐づいたメンバーのプロフィールが検索対象となるように設定します。

### 学べること
以下の手順でキーワードテンプレートの設定と確認をします。  
- [コンテンツの準備をする](#コンテンツの準備をする)
- [検索対象の文字列を設定する](#検索対象の文字列を設定する)
- [動作の確認をする](#動作の確認をする)

## コンテンツの準備をする
コンテンツとメンバーに必要な項目を設定します。

### コンテンツ定義の作成
[コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)を参考に、全文検索対象とするコンテンツ定義を作成します。  
今回は講演会のスケジュールを想定し、以下の通りコンテンツ定義を作成しました。

基本項目

|項目名|内容|
|:---|:---|
|名前|講演会|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1f9ce0f6e35171e043fd3d30287437ae.png)


項目設定

|項目名|項目設定|項目設定オプション|
|:---|:---|:---|
|登壇者|関連情報選択|モジュール: メンバー|
|開催日時|日付フォーマット|時間(hh:mm)も設定する|
|テーマ|テキスト||
|オンライン配信|streaming|単一選択<br/>0: オンライン配信なし<br/>1: オンライン配信あり<br/>入力制限: 入力必須<br/>カスタムテンプレート: ラジオボタンを利用する|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7a2d448f49109f71ca2f01ab1ec1db07.png)

内容

![Image from Gyazo](https://t.gyazo.com/teams/diverta/52f6e9e6871062c1bd72aa6315878362.png)

登壇者

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eca819de7f9e44de864f02e5c7b4a442.png)

開催日時

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e78876c2a76432d4d2956ecf257f135.png)

テーマ

![Image from Gyazo](https://t.gyazo.com/teams/diverta/620d458b6e6488e495d0927f6447612f.png)

オンライン配信

![Image from Gyazo](https://t.gyazo.com/teams/diverta/986ec9d6cbbb425f498ad521e91856e3.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ee67dd45284f983c0de22d3e4ab3f2c.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a7cd6c756ce9719d77ef16039ea5f0a.png)

### メンバー拡張項目の設定
[拡張項目設定](/ja/docs/management/extra-information/)及び[メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)を参考に、項目を設定します。
今回は講演会の登壇者を想定し、以下の通り拡張項目を追加しました。

フィールド

|項目名|識別子|設定|
|:---|:---|:---|
|公開プロフィール|publish_profile|テキストエリア|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8b03fa29cc46d7adfe3e23fbaf70d0f3.png)

## 検索対象の文字列を設定する

### 検索対象文字列テンプレートの確認
デフォルトでは、
- topics_id
- slug
- タイトル
- 内容
- カテゴリ
- 全ての拡張項目のテキスト部分
が検索対象となるテンプレートが入力されています。

:::info
初期状態に戻したい場合は空で更新することで、自動的にデフォルトテンプレートが入力されます。
:::

#### リファレンス
利用できる変数は以下の通りです。

|変数名|型|説明|
|:---|:---|:---|
|$details|Object|コンテンツ詳細|
|$ext_config|Object|コンテンツ拡張設定|

Smartyの記述によって出力された文章が全文検索の対象となります。


### 検索対象文字列テンプレートの修正
「[コンテンツ定義の作成](#コンテンツ定義の作成)」で追加したコンテンツ定義のテンプレートを変更します。
今回の例では、以下を検索対象文字列に含むように追加しています。
- タイトル
- 関連情報に紐づくメンバー情報の名前と公開プロフィール
- 開催日時をフォーマットしたもの
- テーマ
- オンライン配信のラベル部分

関連情報に紐づくメンバー情報の取得については、[カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)を参考にしてください。

デフォルトの設定はすべて削除して、以下のように記述します。

```Smarty
{* タイトル *}
{$details.subject|escape}

{* 登壇者 *}
{if $details.presenter.module_type eq 'member' && $details.presenter.module_id}
    {capture name=method_params}{ldelim}
        "filter": "member_id eq {$details.presenter.module_id}"
    {rdelim}{/capture}
    {assign var=method_params value=$smarty.capture.method_params|json_decode:1}
    {api_method
        var=member_list
        model="Member"
        method="list"
        version="1"
        method_params=$method_params
    }
    {foreach from=$member_list.list item=member}
        {* 氏名 *}
        {$member.name1|escape} {$member.name2|escape}
        {* 公開プロフィール *}
        {$member.publish_profile|escape}
    {/foreach}
{/if}

{* 開催日時 *}
{$details.date|strtotime|date_format:"Y/m/d H:i"}
{$details.date|strtotime|date_format:"Y年m月d日 H時i分"}

{* テーマ *}
{$details.thema|escape}

{* オンライン配信 *}
{if $details.streaming.key > 0}
    {$details.streaming.label}
{/if}

{* 内容 *}
{$details.contents|strip_tags|escape}

```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc8e9428ccde49c9bad834a2c757c2b7.jpg)

### 検索対象文字列テンプレートを保存する 
処理の記述が完了したら、[更新する] ボタンをクリックして保存します。
以上で設定は完了です。

コンテンツを追加・更新すると、テンプレートに基づいて自動的に検索対象文字列が保存されます。

:::caution
反映まで数分程度時間がかかる場合があります。
:::


## 動作の確認をする
コンテンツを追加して、Swagger UIから検索結果を確認します。

### コンテンツを追加する
[コンテンツ定義の作成]で作成したコンテンツ定義に従って、コンテンツを追加します。

フォームに内容を入力し、[追加する] ボタンをクリックしてコンテンツを追加します。
コンテンツを追加・更新すると、テンプレートに基づいて自動的に検索対象文字列が保存されます。

:::caution
反映まで数分程度時間がかかる場合があります。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e4a9bf45e89e0d36dbda35e7b31f8207.jpg)

### 検索対象文字列を確認する
追加されたコンテンツの編集画面で、[その他] ボタンをクリックして選択肢が表示します。
[キーワードテンプレート]をクリックすると、出力された検索対象文字列を確認することが出来ます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7c63e594bd37e6eab61e8a28907a69a2.png)

:::caution
反映完了まで[キーワードテンプレート]の選択肢が表示されません。
:::

今回の例では、表示された文字列は以下のようになります。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9956ca779839ec1fb3d46aa1d6ff1662.png)

:::tip
検索対象文字列にHTMLタグを含む場合、HTMLタグ自体も検索対象となります。
HTMLタグを除いて検索したい場合はstrip_tags修飾子の利用を検討ください。
- [KurocoのSmartyで利用可能なPHP関数](/ja/docs/reference/smarty-php-function/)
:::

:::info
- 生成できる検索対象文字列はコンテンツ毎に100MB(3byte想定のマルチバイト文字で3000万文字以上)までとなり、100MBを超える文字列はカットされます。
- テンプレートで生成する検索対象文字列内の半角英字は自動的に小文字になります。
:::

### 全文検索用エンドポイントを用意する
検索用のエンドポイントを用意します。

[エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)を参考に、エンドポイントを作成します。  

今回はパス・モデルを以下のように設定します。
- パス： search
- カテゴリー: コンテンツ
- モデル：Topics, v1
- オペレーション：list
- topics_group_id：58 ([コンテンツ定義の作成](#コンテンツ定義の作成)で採番されたID)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f969c8cb1375fb406f951ef26b045b9.png)

### Swagger UIで確認する
Swagger UI画面から[全文検索用エンドポイントを用意する]で追加したエンドポイントにリクエストします。
full_text_searchにキーワードを入力することで、全文検索文字列にキーワードを含むコンテンツのみが返却されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/545d3da14aa62b84ccc1ad83ae0f3a90.png)

:::tip
複数のキーワードをスペース区切りで指定した場合のAND/OR条件は`full_text_search_cond`パラメータで設定可能です。  
指定が無い場合はANDで動作します。
:::

## 関連ドキュメント
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [拡張項目設定](/ja/docs/management/extra-information/)
- [メンバー詳細設定で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-member-field-settings/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)


---

# カスタム処理を利用して、コンテンツ定義に独自のバリデーションを実装する

> 元ページ: `tutorials/how-to-implement-original-validation-in-contents-edit-by-using-function` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-original-validation-in-contents-edit-by-using-function/
> 概要: カスタム処理とTriggerを使用して、コンテンツ追加または編集に独自のバリデーション処理を実装する方法を解説します。この機能を利用すると、標準機能のみでは実現できない複雑な入力チェックを追加できます。

## 概要
カスタム処理とTriggerを使用して、コンテンツ追加または編集に独自のバリデーション処理を実装する方法を解説します。
この機能を利用すると、標準機能のみでは実現できない複雑な入力チェックを追加できます。

今回は、POSTされたメールアドレスが特定のドメインと一致しなければエラーを返すバリデーション処理を実装します。

### 学べること
以下の手順でコンテンツの追加・編集に独自のバリデーション処理を実装します。
- [事前準備](#事前準備)
- [カスタム処理を作成する](#カスタム処理を作成する)
- [バリデーション処理を記述する](#バリデーション処理を記述する)
- [カスタム処理にコンテンツ定義を関連付ける](#カスタム処理にコンテンツ定義を関連付ける)
- [バリデーションの動作を確認する](#バリデーションの動作を確認する)

## 事前準備
### バリデーションを適用するコンテンツ定義を作成する
まず、バリデーションを適用するコンテンツ定義を作成します。  

Kuroco管理画面のサイドメニューから[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6907f819b40433ca64ed43afdc2aeda1.png)

画面右上の[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f1613d2588759c77fb778177724d83e.png)

以下の通り入力します。
- 名前：カスタムバリデーション実装対象コンテンツ
- フィールド：以下の通り

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9a4e7cbe7c6502790a26d6ace73506ff.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/778e746a8d1b4f766b3bf00561e7e5c3.png)

設定後、[追加]をクリックしてコンテンツ定義を追加します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d9bd575721553e565407c224b5a9e15.png)

## カスタム処理を作成する
バリデーション処理を記述するためのカスタム処理を用意します。

メニューの[オペレーション] -> [カスタム処理] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05fc571fc550915a05f0c13d0508e9f6.png)

カスタム処理一覧画面の右上の [追加] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9998b0797d2ae3e08dd1c0ffde72420c.png)

### タイトル・カテゴリ等を入力する
カスタム処理のタイトル、カテゴリ、識別子とこれを使ったコンポーネントを入力します。 

今回は下記のように入力しました。
- タイトル：email_domain_validation
- 識別子：email_domain_validation

:::tip
同一カテゴリ内にタイトルが重複する処理を作成できないため、他と重複しないタイトルを命名してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88ae06f2394a8288e887b00e058f8d7f.png)

### バリデーション処理を記述する
次に、以下の手順でバリデーション処理を記述します。

#### エラー変数を初期化する
バリデーション結果を格納するための$errors変数を初期化します。  

| 変数名 | 型 | 説明|
| :--- | :--- | :--- |
|$errors |array |テキスト配列|

エディタに下記記入します。

```smarty
{* $errors = [] *}
{assign_array var="errors" values=""}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/edc8b806f4d747a688c61fe71fbdeb0d.png)

#### バリデーション処理を実装する
ユーザーの入力値をチェックし、errors変数に結果を代入します。  
入力値を参照するためには、下記のいずれかの変数を利用します。

| 変数名 | 説明 |
| :--- | :--- |
|$smarty.post | 画面から入力されたフォームデータ |

```smarty
{assign_array var="errors" values=""}

{* [例] POSTされたメールアドレスが特定のドメインと一致しなければエラーを返す *}
{if $smarty.post.ext_1|strpos:'@example.com' === false}
  {* $errors = ["メールアドレスが不正です。"] *}
  {assign var="errors." value="メールアドレスが不正です。"}
{/if}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfed7d309f422826dd11ecb3a5744075.png)


#### 保存する
処理の記述が完了したら、[追加] ボタンをクリックし保存してください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/98ffd9dd3fb6393dbd09df39f739838e.png)


## カスタム処理にコンテンツ定義を関連付ける
次にコンテンツ定義をカスタム処理に関連付けます。  

### コンテンツ定義リスト画面で、関連付けるコンテンツ定義のIDを確認する
[コンテンツ定義] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6907f819b40433ca64ed43afdc2aeda1.png)

事前準備で作成したコンテンツ定義のIDを確認します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c03e167af024f2f676e2a32d37c2f7e9.png)

### コンテンツ定義IDカスタム処理に関連付ける

コンテンツ定義IDを作成したカスタム処理に関連付けます。

- これを使ったコンポーネント：コンテンツのバリデーション前
- 値：カスタム処理を適用するコンテンツ定義ID
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4fcc294ba59df7971d0d937f99891819.png)

#### 保存する
コンテンツ定義IDの入力が完了したら、[更新する] ボタンをクリックし保存してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdd128a4f2f5cafbb30306da8b4ee7de.png)

## バリデーションの動作を確認する
コンテンツ編集画面からリクエストを行い、バリデーション処理の動作を確認します。

### コンテンツ編集を表示する
事前準備で作成したコンテンツの一覧画面で[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9e2b7cd3ab4554079587acfde0767728.png)

### エラーが出力される値を入力する
下記の通り、エラーが出力される値を[email]に入力します。　  
入力が完了したら、[追加する] ボタンをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4b042472cb3b76bb1dd80d4f521d40fe.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e5f71ba2fa8ff61e809738187db2305.png)

### エラー内容を確認する
想定通りのエラーが出力されることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b449837f4ef1fcb52a0a7bff645287b2.png)

以上でカスタム処理とコンテンツ定義の関連付けが完了です。  

## バリデーションエラーが発生しない場合の確認ポイント
入力チェックが想定通りに行われない場合は、下記のポイントを確認してください。
- 関連付いているカスタム処理が正しいか
- 変数名(errors)が正しいか
- チェック対象の項目名が正しいか
- バリデーション処理のロジックが正しいか

## コード例の紹介
カスタム処理に利用できるコード例を紹介します。

| 変数名 | 説明 |
| :--- | :--- |
|$smarty.get | クエリパラメータ |
|$smarty.post | 画面から入力されたフォームデータ |
|$smarty.request | クエリパラメータ & 画面から入力されたフォームデータ |


### 特定の文字列を含むかどうかをチェックする

```smarty
{if $smarty.post.column_name|strpos:"期待する文字列" === false}
  {assign var="errors." value="column_nameが不正です。"}
{/if}
```

### 数値かどうかをチェックする

```smarty
{if !$smarty.post.parameter_name|is_numeric}
  {assign var="errors." value="parameter_nameは数値で入力してください。"}
{/if}
```

### 特定の項目に依存した入力チェックを行う

```smarty
{*
    [例] ext_1に1が入力された場合のみ、ext_2を必須項目とする
    ext_1: セレクト項目 ('', '1', '2')
    ext_2: テキスト項目
*}
{if $smarty.post.ext_1 === '1' || (
  !$smarty.post.ext_1|@empty &&
  $smarty.post.ext_1.key === '1'
)}
  {if !isset($smarty.post.ext_2) || $smarty.post.ext_2 === ''}
    {assign var="errors." value="テキスト項目は必須項目です。"}
  {/if}
{/if}
```

### 特定のグループに所属するメンバーにのみ入力チェックを適用する

```smarty
{*
  member_group_id=1は管理者権限グループになります。
*}
{assign var="member_group_id" value="1"}
{if $member_group_id|rcms_in_array:$smarty.session.arrGroup_id}
  {if !isset($smarty.post.ext_1)}
    {assign var="errors." value="ext_1は必須項目です。"}
  {/if}
{/if}
```

### 削除対象のコンテンツが他コンテンツの関連情報選択に設定されている場合にエラーを返す

```smarty
{*
  topics_group_idに関連情報選択を持つコンテンツ定義のIDを指定します。
*}
{if $smarty.request.MODE|lower === 'delete'}
  {assign_array var="method_params" values=""}
  {assign_array var="method_params.topics_group_id" values="9,20"}
  {assign_array var="method_params.filter_request_allow_list" values=":q|topics:[topics_id]"}
  {assign var="method_params.filter" value=":R(topics:q|topics_id eq `$topics_id`|)"}
  {assign var="method_params.cnt" value=1}
  {api_method
      var='related_topics'
      model='Topics'
      method='list'
      version='1'
      method_params=$method_params}
  {if $related_topics.list|@count > 0}
    {assign var="errors." value="このコンテンツは他のコンテンツの関連情報に設定されているため、削除できません。"}
  {/if}
{/if}
```

:::tip
CSVアップロード時にバリデーションをかける場合は`$smarty.post`の代わりに`$uploaded_row`の変数で行データを参照してください。
:::

## 関連ドキュメント
- [カスタム処理に利用できる変数一覧](/ja/docs/reference/trigger-variables/)


---

# バッチ処理を利用し、PDFの1ページ目をサムネイル画像にする

> 元ページ: `tutorials/how-to-make-thumb-from-pdf` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-make-thumb-from-pdf/
> 概要: コンテンツでPDFを登録した際に、PDFの1ページ目を自動でサムネイル画像にする方法を説明します。

バッチ処理を利用し、コンテンツでPDFを登録した際にPDFの1ページ目を自動でサムネイル画像にする方法を説明します。

## 前提条件
サムネイル画像の保存はGCSに保存されます。そのため、事前にFirebaseとの連携が必要になります。
[Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)を参考に、Firebaseの連携をお願いします。


## コンテンツ定義作成
まずはPDFを登録するコンテンツ定義を作成します。  
メニューより[コンテンツ定義]をクリックしコンテンツ定義一覧画面を開き、[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/82c255a46f5fd368be2e54ab5a5ad69b.png)

コンテンツ定義作成画面が開きます。
今回は下記で作成します。

| 項目名 | 設定内容 |
| :--- | :--- |
|名前| 自動サムネイル作成 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/233a64e34dd4067b224f30e91907395b.png)
また、下記2つのフィールドを追加します。

| ID | 項目名 | 識別子 | 項目設定 |
| :--- | :--- | :--- | :--- |
|1|サムネイル画像|image|画像(KurocoFilesにアップロード)|
|2|PDFファイル|pdf|ファイル(KurocoFilesにアップロード)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ec8284c29d1538e0040edcfddd2abe6c.png)

設定したら、[追加する]をクリックしコンテンツ定義を保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5df1447dbf037cafa4793515f702f7ff.png)

:::tip
コンテンツ定義の作成方法の詳細は、チュートリアル -> [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)をご確認ください。
:::

## APIの設定
次にPDFを画像に変換するためのAPIを設定します。  
メニューより[API] -> [Default]をクリックしエンドポイント一覧画面を開き、[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3132eb6b7e51cdd05a2842ecfcfc8f52.png)

API追加画面が表示されるので、以下のように設定し、[追加]をクリックします。

| 項目 | 設定 |
| :--- | :--- |
|タイトル| pdf-to-thumbs |
|版| 1.0 |
|ディスクリプション| 自動サムネイル作成API |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c22dfb04ada320c81ec1cee3a9dbf43.png)
作成したAPIのエンドポイント一覧画面が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a44373c8cd951c48a49f44221cbc6f04.png)
### API セキュリティの設定
APIセキュリティを設定します。  
今回作成するAPIは外部からリクエストされないように「動的アクセストークン」を選択します。

エンドポイント一覧画面より、[セキュリティ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6dba7b8246e10d8c923a807baefd350f.png)
セキュリティより「動的アクセストークン」を選択し、[保存する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad46f64cc412632ec93cf6fd38592b27.png)
以上でセキュリティの設定は完了です。

### エンドポイントの作成
次にエンドポイントを作成します。今回は下記2つのエンドポイントを作成します。

- サムネイル画像が未登録のコンテンツを取得する
- サムネイル画像を更新する

「サムネイル画像が未登録のコンテンツを取得する」にてコンテンツにサムネイル画像の登録有無を確認し、登録がない場合「サムネイル画像を更新する」にてサムネイル画像をコンテンツに登録します。

#### エンドポイント「サムネイル画像が未登録のコンテンツを取得する」の作成
まずは「サムネイル画像が未登録のコンテンツを取得する」のエンドポイントを作成します。
エンドポイント一覧画面より「新しいエンドポイントの追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/079cee81fe01e7151c2aad58dc77a024.png)
今回は下記で作成します。

|項目  | |内容  |
| :--- | :--- | :--- |
|パス | | no-thumb-list |
|カテゴリー | |コンテンツ |
|モデル| |Topics|
|オペレーション| |list|
|基本設定|filter|image="" and pdf!=""<br/>（注意:PDFファイル名/画像の説明部分のテキスト有無を検索条件にしています）|
|基本設定|topics_group_id| 先ほど作成した「自動サムネイル作成」のidを記載 |
|基本設定 | ctn | 0 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/475c220d7b1bec81f9e1a258103ce18b.png)

設定後、画面下部の[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d46c58badffc7f8378eb3670336154ca.png)
#### エンドポイント「サムネイル画像を更新する」の作成
次に「サムネイル画像を更新する」のエンドポイントを作成します。
同様にエンドポイント一覧画面より「新しいエンドポイントの追加」をクリックし、下記で作成します。

|項目  | |内容  |
| :--- | :--- | :--- |
|パス | | thumb-update |
|カテゴリー | |コンテンツ |
|モデル| |Topics|
|オペレーション| |update|
|基本設定|topics_group_id|先ほど作成した「自動サムネイル作成」のidを記載|
|基本設定 | use_columns | image |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee2dad1dc3482cb8920842ff72380d64.png)

設定後、画面下部の[追加する]をクリックします。

以上でエンドポイントの作成完了です。

## 一時保存先フォルダの作成
次に、画像の保存先フォルダを作成します。
このフォルダは、PDFをサムネイル画像に保存したあとの一時保存先になります。

メニューより[ファイルマネージャ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed477ef9fdc85bd2f02a892743178cad.png)

[GCS(Private)]をクリックし、[新しいフォルダを作成]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/00d5dbe6dcc3db3ab2f6538dab0c93f1.png)
フォルダ名に「pdf_thumb」と記入し、[OK]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/425770514e1ed35232670996a51fc12a.png)
pdf_thumb フォルダが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a86ab71bb4dbffff6afdefdff75a2043.png)
## バッチ処理の作成
次にPDFを画像化するためのバッチ処理を作成します。今回は下記2つのバッチを作成します。

- PDFからサムネイル画像を生成する  
  PDFの先頭ページを画像化するバッチ処理です。
- 生成したサムネイル画像をコンテンツに登録する  
  作成されたサムネイル画像を対象のコンテンツに登録するバッチ処理です。

### バッチ処理「PDFからサムネイル画像を生成する」の作成

まずは「PDFからサムネイル画像を生成する」のバッチ処理を作成します。  
[オペレーション] -> [バッチ処理]より[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3d989ba34e3922ad7fd3b823511e74d5.png)

バッチ処理追加画面が表示されるので、以下のように設定します。

| 項目 | 設定 |
| :--- | :--- |
|タイトル| PDFからサムネイル画像作成 |
|識別子| create_thumb |
|バッチ| 1時間毎 |

また、実行内容には下記を記入してください。

```smarty
{*PDF登録有りでサムネイル未設定のコンテンツ一覧を取得*}
{api_internal member_id=1 endpoint='/rcms-api/2/no-thumb-list' query='' method='GET' var='contents_list' status_var='status'}
{if $status == 1 && $contents_list.list|@count > 0}
    {foreach from=$contents_list.list key=idx item=item}
        {if !$item.image.url && $item.pdf.url}{*画像未設定*}
            {get_file url=$item.pdf.url var=temp_path save=1}
            {if $temp_path}
                {assign var=gcp_pdf_path value='files/g/private/pdf_thumb/'|cat:$item.topics_id|cat:'.pdf'}
                {assign var=gcp_img_path value='files/g/private/pdf_thumb/'|cat:$item.topics_id|cat:'.png'}
                {*PDFファイルをGCS上のテンポラリディレクトリに保存*}
                {put_file tmp_path=$temp_path path=$gcp_pdf_path}
                {assign var=data value=null}
                {assign_array var=data values=''}
                {assign var=data.topics_id value=$item.topics_id}
                {assign var=data.pdf value=$item.pdf}
                {*CloudFunctionsの機能を利用してサムネイル生成*}
                {make_pdf_thumb pdfPath=$gcp_pdf_path destPath=$gcp_img_path callback_batch='update_pdf_thumb_bat' data=$data}
            {/if}
        {/if}
    {/foreach}
{/if}
```

:::caution
`/rcms-api/2/no-thumb-list` の`2`には、先ほど作成したAPIのidに変更してください。
APIのIDはエンドポイント一覧ページのURLより確認できます。  
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c93e6ff3170db67f8605a0d08828a470.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/835577330c766b45c495eb0108c84b8a.jpg)

設定したら、[追加する]をクリックしバッチ処理を保存します。

### バッチ処理「生成したサムネイル画像をコンテンツに登録する」の作成

次に、「生成したサムネイル画像をコンテンツに登録する」バッチ処理を作成します。
同様に、バッチ作成画面より以下のように追加します。

| 項目 | 設定 |
| :--- | :--- |
|タイトル| 画像をコンテンツに登録 |
|識別子| update_pdf_thumb_bat |
|バッチ| バッチテンプレート |

また、実行内容には下記を記入してください。

```smarty
{*CloudFunction側から取得したデータを設定*}
{assign var=topics_id value=$ext_data.data.topics_id}
{assign var=image_name value=$ext_data.data.pdf.desc|replace:'.pdf':''}
{assign var=dest_path value=$ext_data.destPath}
{assign var=file_id value='files/temp/pdf_thumb/'|cat:$topics_id|cat:'.png'}
{assign var=save_path value='/files/temp/pdf_thumb/'|cat:$topics_id|cat:'.png'}

{*GCSから画像ファイルをfiles/tempに取得*}
{get_file path=$dest_path save_path=$save_path save=1}

{*取得した画像をコンテンツにアップロード*}
{assign_array var=post_data values=''}
{assign_array var=post_data.image values=''}
{assign var=post_data.image.file_id value=$file_id}
{assign var=post_data.image.file_nm value=$image_name|cat:'.png'}
{assign var=post_data.image.desc value=$image_name}
{api_internal endpoint='/rcms-api/2/thumb-update/'|cat:$topics_id member_id=1 method='POST' queries=$post_data var='resp' status_var='status'}
{if $status==1}
    {*処理成功時にはPDFとサムネイルを削除する*}
    {remove_file path='/'|cat:$dest_path}
    {remove_file path='/'|cat:$dest_path|replace:'.png':'.pdf'}
{/if}
```

:::caution
`/rcms-api/2/thumb-update` の`2`には、先ほど作成したAPIのidに変更してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0330c3a338bdff2f5a4dc80485d30cef.jpg)

以上でバッチ処理の設定が完了です。

## 動作確認
最後に、設定内容の動作確認をします。

作成したコンテンツ定義「自動サムネイル作成」よりコンテンツを投稿します。
その際に、画像はアップロードせずPDFのみアップロードします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6f6a96337e9dac254aed33e77b4ab1f.jpg)
PDFをアップロードしたら、[追加する]をクリックしコンテンツを投稿します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d57400da00a8c4ce5569c7d6f4ef1278.png)
次に、バッチ処理を実行します。
今回の設定ではバッチ処理が1時間毎に実行するように設定しましたが、テストのため手動で実行します。

バッチ処理より、先ほど作成した「PDFからサムネイル画像作成」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a311257dca7d529f2f790a7dad6b0510.png)
タイトル横の[すぐに実行する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6774cf3ed198b06fb641186333c83814.png)
アラートが表示されるので、[OK]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d5263b5328a39aeff51ad784c2b9449.png)
バッチが実行されました。

次に、コンテンツに画像がアップロードされているかを確認します。

[コンテンツ定義]をクリックし、自動サムネイル作成の[一覧]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e1abdf8d535200f8bf2e115abf353156.png)

先ほど作成したコンテンツをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/497fe7ee03b297068ccc772fa20f777c.png)
「サムネイル画像」フィールドに画像が登録されていることが確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/abaa1df3e4a619ed7a98e70e312a5886.png)
:::tip
画像作成されるまで、数分かかる場合があります。画像が登録されていない場合、時間を置いてから再度ご確認ください。
:::

## 関連ドキュメント
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [バッチ処理](/ja/docs/management/batch/)
- [Kurocoのバッチ処理を利用する](/ja/docs/tutorials/how-to-use-batch/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)


---

# アクティビティ機能で、特定ユーザーにしか見れないコメントを残す

> 元ページ: `tutorials/how-to-only-display-comments-that-are-addressed-to-a-specific-user` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-only-display-comments-that-are-addressed-to-a-specific-user/
> 概要: ここでは、アクティビティでコメントを残すエンドポイントで、特定のユーザーに向けたコメントを追加する方法を説明します。特定のユーザーに向けたコメントは、対象のユーザーにのみ表示されます。

## 概要
ここでは、アクティビティでコメントを残すエンドポイント(`Comment::insert`)で、特定のユーザーに向けたコメントを追加する方法を説明します。  
特定のユーザーに向けたコメントは、対象のユーザーにのみ表示されます。  
ここでは例として、HP上でサポートとプライベートチャットができるスペースの作成を想定し、SwaggerUIで動作の確認までを実施します。  

### 学べること
以下の手順でKuroco管理画面内での動作確認をします。
- [アクティビティ定義の作成](#アクティビティ定義の作成)
- [コンテンツの作成](#コンテンツの作成)
- [エンドポイントの作成](#エンドポイントの作成)
- [Swagger UIで動作の確認](#swagger-uiで動作の確認)

### 前提条件
事前に、次のようなユーザーを準備しておきます。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c7bf904e1cead23ded17afd77d064234.png)

Diverta TaroとDiverta Supportがお互いにコメントを残し、Diverta Taroにはコメントが表示され、Diverta Jiroからは表示されないことを確認します。

## アクティビティ定義の作成
まずはアクティビティ定義を作成します。    
[アクティビティ定義]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b73cbe0b67685431b15982c5100fcba2.png)

[追加する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9455096bc95c8c1b8f7349696f4bb206.png)

未ログインメンバーの権限を`閲覧不可`、`受け付けない`に設定、その他のグループの権限を`閲覧可`、`即公開`として[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d4c214ea27c7aed8a649a335ed24ad2.png)

後ほど利用するので、作成したアクティビティIDをメモしておきます。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc89e2ddd79925992af7178285aab6fe.png)

## コンテンツの作成
次にコメントを追加する対象となるコンテンツを作成します。

任意のコンテンツ定義を選択し、[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c00936a8fe3ab46e654a8903f531096d.png)

以下を入力し、[追加する]をクリックします。 

|項目|値|
|:--|:--|
|タイトル|Kurocoチャットサポート|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1a8b5aa88241562df59ab5d70865b5b.png)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/72ca2599a82ca4044cd6a191d850967f.png)

追加したコンテンツIDは後ほど利用するためメモします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f5b7c678685589a0632cebeb647292c3.png)

## エンドポイントの作成
以下のように、自分宛のコメント一覧を表示するエンドポイント（`comments`）と、コメントを送信するためのエンドポイント（`comments/insert`）の2つを作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/912ba70295cce97fe68656fb41d1dbc3.png)


### commentsエンドポイント
`comments`エンドポイントでは、`id` のパラメータにアクティビティIDを設定し、`to_me_list`と`my_list` のパラメータにチェックを入れます。  
`to_me_list` のパラメータにチェックを入れると、エンドポイントにリクエストを送ったユーザーを対象としたコメントが返されるようになります。  
また、`my_list` のパラメータにチェックを入れると、自分の送ったコメントが返されるようになります。

| 項目 | 設定内容 |
| :--- | :--- |
| パス | `comments` |
| カテゴリー | アクティビティ |
| モデル | Comment |
| オペレーション | list |
| id | `37` (作成したアクティビティ定義のID) |
| module_id | `1144` (作成したコンテンツのID)|
| my_list | チェックを入れる |
| to_me_list | チェックを入れる |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9fb1604fa00483de95642cdf9f142b1.png)  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/df683d3a72cde336ca5c12470f0262ac.png)  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50bfe5a565f41d37bdde90607162cf19.png)  


### comments/insertエンドポイント
`comments/insert`エンドポイントでは、`id` のパラメータにアクティビティIDを設定します。

| 項目 | 設定内容 |
| :--- | :--- |
| パス | `comments/insert` |
|カテゴリー | アクティビティ |
| モデル | Comment |
| オペレーション | insert |
| id | `37`(作成したアクティビティ定義のID) |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b64bd90b70f30c2ee1a9fa1cd9fa1cb4.png)

## Swagger UIで動作の確認
### コメントを残す
準備ができたら、Swagger UIで動作を確認します。  

まずはDiverta Taro(27)のアカウントでログインします。

:::tip
APIのセキュリティをCookieに設定しておくと、メンバーIDを入力してログイン状態のセッションを作成できます。  
ログインのエンドポイントを作成して、IDとパスワードでログインしても構いません。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3226607f15605850f9fece5822add028.gif)
:::

次に、`comments/insert`エンドポイントを開き、[Try it out]をクリックし、レスポンスボディに以下のコードを貼り付けて実行します。

```json
{
  "module_id": 1144,
  "name": "Diverta Taro",
  "note": "Kurocoについて教えてください。",
  "delkey": "",
  "to_member_ids": [
    30
  ]
}
```

:::caution
`"module_id": 1144` の部分は作成したコンテンツのIDを指定してください。
`"to_member_ids": [30]` の部分はコメントのあて先(今回はDiverta Support)のメンバーIDを指定してください。
:::

:::tip
`to_member_ids`は以下のように複数のユーザー指定も可能です。
:::

```
{
  "to_member_ids": [
    1,
    2,
    3
  ]
}
```

200のレスポンスコードと、"コメントの書き込みが終了しました。"のメッセージが表示されたらコメントの追加は完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e87c62398d22df24e4deca437835502f.png)

### 返信コメントを残す
同様にDiverta Support(30)のアカウントでログインして以下のコメントを残します。

```json
{
  "module_id": 1144,
  "name": "Diverta Support",
  "note": "KurocoはAPIファーストのヘッドレスCMSです。",
  "delkey": "",
  "to_member_ids": [
    27
  ]
}
```

:::caution
`"module_id": 1144` の部分は作成したコンテンツのIDを指定してください。
`"to_member_ids": [27]` の部分はコメントのあて先(今回はDiverta Taro)のメンバーIDを指定してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/05b7b41ff1366a4823fb4f2d95407e1d.png)

### コメントを確認する
Diverta Taro（メンバーID = 27）でログインをして、`comments`エンドポイントにリクエストを送ると、上記2つのコメントがレスポンスされます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cdf41329f9810a2848063e3807f5e963.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c237c8bce180b9e805265836ff092f15.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b0dd6d4dc6c053e4a112babc35e0d05f.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0af6aea615de94a224ccc112ce1f835.png)

:::info
表示項目の簡易化のため、上記キャプチャではエンドポイントの後処理に出力許可リストを設定しています。
:::

しかし、他のユーザ（Diverta Jiro、メンバーID = 22）でログインをして、`comments`エンドポイントにリクエストを送っても、レスポンスは得られません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4c6bad1355fcec395f4c023027148f39.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c237c8bce180b9e805265836ff092f15.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b0dd6d4dc6c053e4a112babc35e0d05f.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e914a73201571559ae878444b4295260.png)

以上で動作の確認が完了です。
SuwaggerUIで確認した動作をフロントエンドで実装すると、HP上でサポートとプライベートチャットができるスペースを実装できます。  

Diverta Support(30)でログインをすると、Diverta Jiro(22)とのチャット内容も表示されますので、企業側の表示は必要に応じて調整ください。

## 関連ドキュメント
- [コンテンツにコメント機能を追加する](/ja/docs/tutorials/integrate-activity-comment/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [アクティビティ定義](/ja/docs/management/comment-module-list/)
- [アクティビティ](/ja/docs/management/comment-list/)


---

# how-to-use-ckeditor-placeholder-feature

> 元ページ: `tutorials/how-to-use-ckeditor-placeholder-feature` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-ckeditor-placeholder-feature/

--- 
title: WYSIWYGエディターのプレースホルダー機能を実装する
description: このチュートリアルでは、WYSIWYGプレースホルダー機能、API、およびカスタム処理を使用して、複数のコンテンツにまたがる共通のテキストを設定する方法を説明します。
---

## 概要
WYSIWYGプレースホルダーの機能は柔軟でカスタマイズ可能なコンテンツを作成するための便利なツールです。これを使用することで、予め設定した文書を簡単にコンテンツへ登録できます。  
また、複数のコンテンツにまたがる共通のテキスト設定も可能です。

このチュートリアルでは、WYSIWYGプレースホルダー機能、API、およびカスタム処理を使用して、複数のコンテンツにまたがる共通のテキストを設定する方法を説明します。  
2つのプレースホルダー、`my_name`と`my_address`を使用し、これらのプレースホルダーが、APIリクエスト時に予設定したテキストへ動的に置換されます。  

### 学べること
以下の手順でWYSIWYGプレースホルダーの機能を設定する方法を学びます。

- [コンテンツ定義を準備する](#コンテンツ定義を準備する)
- [コンテンツを作成する](#コンテンツを作成する)
- [カスタム処理を作成する](#カスタム処理を作成する)
- [APIエンドポイントを作成する](#apiエンドポイントを作成する)
- [結果を確認する](#結果を確認する)

## コンテンツ定義を準備する
[コンテンツ定義一覧](/ja/docs/management/content-structure-topics-group/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea26ddc511181a0ab07f4f4813feb686.png)

以下の内容で設定をします。  

|項目||設定|
|:--|:--|:--|
|全般|名前|My Content Structure|
|項目設定|項目設定|項目名：WYSIWYG<br/>項目設定：WYSIWYG<br/>WYSIWYGプレースホルダー：my_name,my_address|

:::tip
プレースホルダーはカンマ区切りで入力し、カンマの後ろにスペースは入れないことに注意してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc7e53239131cbf974ffbaa5edeafeae.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5de5d7511acb282b622a195b0e42117b.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/36f808196c076fcc8f85ba1e4a7e90ec.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。  

## コンテンツを作成する
前のステップで作成したコンテンツ定義に2つのコンテンツを作成し、プレースホルダーをコンテンツに入れます。

コンテンツ一覧の画面から[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc8f424f26265344a22f4f807d0ab1d8.png)

以下を入力し、[追加する]をクリックします。

|項目|設定|
|:--|:--|
|タイトル|My First Content|
|WYSIWYG|`My name`と`My Address`を利用した任意の文章。<br/>プレースホルダーを設定すると、WYSIWYGエディターの機能に`Placeholder`が追加されるのでこちらからプレースホルダーを設定してください。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d84f1589e0b9bf2944b0c7f9743a759e.png)

以下を入力し、[追加する]をクリックします。

|項目|設定|
|:--|:--|
|タイトル|My Second Content|
|WYSIWYG|`My name`と`My Address`を利用した任意の文章。<br/>プレースホルダーを設定すると、WYSIWYGエディターの機能に`Placeholder`が追加されるのでこちらからプレースホルダーを設定してください。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/804bcff214d3229e83a837a1bc31fca8.png)

## カスタム処理を作成する
次に、`my_name`と`my_address`プレースホルダーを設定したテキストに置換するカスタム処理を作成します。

[オペレーション] -> [カスタム処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f1cb672eab47b968ed24ca1e961223a2.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7ced588e888224446baaccbb70d4557.png)

以下のように入力します。

|項目|設定|
|:--|:--|
|タイトル|Replase placeholders in content|
|識別子|replase_placeholders_in_content|
|処理|以下のコード|

```smarty
{* For every contents in the list *}
{foreach from=$json.list item='row' key='key'} 
    {* Replace placeholder my_name with "Diverta" *}
    {assign var=json.list.$key.content 
            value=$json.list.$key.content|replace:"<span class=\"placeholder\">`$smarty.ldelim`my_name`$smarty.rdelim`</span>":'Diverta'}
    {* Replace placeholder my_address with the real address value *}
    {assign var=json.list.$key.content 
            value=$json.list.$key.content|replace:"<span class=\"placeholder\">`$smarty.ldelim`my_address`$smarty.rdelim`</span>":'Central Plaza 6F 1-1 Kaguragashi Shinjuku-ku, Tokyo, Japan'}
{/foreach}

{$json|@json_encode:$smarty.const.JSON_UNESCAPED_UNICODE}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ca76781a89e4c87c93901e7c08444b3f.jpg)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

## APIエンドポイントを作成する
Contentカテゴリ、モデルトピック、オペレーションリストを持つ1つのAPIエンドポイントを作成します。前のステップで作成したコンテンツ定義のIDを「topics_group_id」パラメータに設定します。

### エンドポイントを追加する
エンドポイント一覧のページから、[新しいエンドポイントの追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21a2261325607482db947c28667d0057.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|my-content|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|list|
|topics_group_id|作成したコンテンツ定義のID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e536c391d49a751f2149424fbbee8e6c.png)

設定ができたら[追加する]をクリックしてエンドポイントを追加します。  

### エンドポイントに後処理を追加する
前のステップで作成したカスタム処理をエンドポイントの後処理に設定します。  
エンドポイント一覧のページから[後処理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b3a8af6823af91069d7430d6c6bdb4e8.png)

APIのレスポンスを簡素化するために、「出力許可リスト」ポストプロセスも追加し、以下のように設定します。  

|項目|設定内容|
| :--- | :--- |
|出力許可リスト|`list.subject`<br/>`list.content`|
|カスタム処理|Replase placeholders in content|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6ce62cc17f4dd03b9386574ce8296b1.png)

設定ができたら[保存する]をクリックして後処理の設定を保存します。  

## 結果を確認する
SwaggerUIでAPIエンドポイントを取得し、結果を確認します。

エンドポイント一覧のページから[SwaggerUI]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1395a3802d9adeedb916c8b51816a444.png)

作成したエンドポイントの[Try it out]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a509f70678e00bee171e8620f9f056c8.png)

[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0021b5a2b3dffe5f0863dba380cdaaf.png)

以下のように、プレースホルダーを設定した部分が、カスタム処理で設定したテキストに置き換わっていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c435b61daa8b4626a315ac14ddedc49.jpg)

## 関連ドキュメント
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [後処理](/ja/docs/reference/post-processing/)
