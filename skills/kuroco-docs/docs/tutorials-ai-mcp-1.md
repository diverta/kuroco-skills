# Kurocoドキュメント: チュートリアル / AI・MCP（1/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- コンテンツ更新時にAIで自動翻訳する（`ai-post-processing-translation`）
- Claude.ai での MCP コネクタの登録方法（`claude-ai-mcp-connector-setup`）
- Admin MCP でKuroco管理画面を操作する（`connect-to-admin-mcp`）
- DeepL APIを使用して、主言語に入力した文章を自動で翻訳し副言語に追加する（`deepl-api-auto-translation`）
- Model Context Protocol (MCP) と Kuroco の連携（`expose-a-kuroco-api-with-mcp`）
- AIによる回答を生成する（`generating-ai-responses`）
- あいまい検索用のベクトルテンプレートを用意する（`how-to-implement-vector-search`）
- Kuroco MCP サーバと Amazon Bedrock AgentCore Gateway の連携（`integrate-kuroco-mcp-with-amazon-bedrock-agentcore`）
- Kuroco の AI 機能ガイド（`kuroco-ai-features-guide`）


---

# コンテンツ更新時にAIで自動翻訳する

> 元ページ: `tutorials/ai-post-processing-translation` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/ai-post-processing-translation/
> 概要: KurocoのAI自動処理機能と多言語設定を使って、日本語で入力したコンテンツを保存時にAIが翻訳し、副言語（英語など）へ自動設定する方法を紹介します。

## 概要

KurocoのAI自動処理を使うと、コンテンツを保存したタイミングで自動的にAI処理を実行できます。  
このチュートリアルでは、多言語設定を有効にしたサイトで、日本語（主言語）で入力したコンテンツを保存すると同時に、AIが英語（副言語）へ翻訳して自動設定する機能を実装します。

さらに応用として、英語（副言語）を起点に、その他の副言語（韓国語・ポルトガル語など）へ翻訳を連鎖させる方法と、複数ルールを設定したときの実行順・実行条件についても説明します。

:::caution
AI自動処理による翻訳は「AI処理ユニット」項目に計上されます。多数のコンテンツや複数の副言語を一度に処理すると、その分だけAI処理ユニットの利用料が増えます。設定後はいきなり大量のコンテンツで実行せず、まずは少量のコンテンツで翻訳結果とAI処理ユニットの利用料を確認してから、本格的な運用に進むことをおすすめします。
:::

### 学べること

以下の手順でAI自動翻訳を実装します。

- [多言語設定を有効にする](#1-多言語設定を有効にする)
- [コンテンツ定義を作成する](#2-コンテンツ定義を作成する)
- [AI自動処理を設定する](#3-ai自動処理を設定する)
- [動作確認をする](#4-動作確認をする)
- [応用：英語から他の副言語へ翻訳する](#応用英語から他の副言語へ翻訳する)

### 前提条件

- Kurocoのサイトが作成済みであること
- 多言語設定を利用できること

## 1. 多言語設定を有効にする

副言語へAI翻訳を設定するために、あらかじめ多言語設定を有効にします。

[環境設定] -> [ローカライズ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9737d2b18c03dd08d3c60c7c3eab386.png)

[多言語設定]の[有効にする]をONにし、主言語と副言語を選択します。ここでは、以下のように設定します。

| 項目 | 値 |
| :--- | :--- |
| 主言語 | 日本語 |
| 副言語 | 英語 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f93b656e31bbb1f12c3762a99a4b40cc.jpg)

[更新する]をクリックして設定を保存します。

:::info
副言語を追加すると、コンテンツ編集画面で言語タブが表示され、言語ごとにデータを保存できるようになります。副言語の動作の詳細は[副言語について](/ja/docs/reference/secondary-language/)を参照してください。
:::

## 2. コンテンツ定義を作成する

翻訳対象の本文を持つコンテンツ定義を作成します。多言語設定を有効にすると、同じ項目に対して言語ごとの値を保存できます。

[コンテンツ定義]をクリックし、[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/90be5d48158a7067855f388d2fbf0d87.png)

以下のように入力します。

| 項目 | 値 |
| :--- | :--- |
| コンテンツ定義名 | 翻訳テスト |

次に、以下の拡張フィールドを追加します。

| Slug | 項目名 | 項目設定 |
| :--- | :--- | :--- |
| body | Body | テキストエリア |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d517d1dfa656b40edc82f2bc8dabff85.png)

[追加する]をクリックしてコンテンツ定義を保存します。

## 3. AI自動処理を設定する

作成したコンテンツ定義を開き、左サイドメニューの[AI自動処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4f28d60ff9c05994e870b386f17ee46c.png)

### AI自動処理を有効にする

[AI自動後処理]の[有効にする]をオンにします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fb9242317587ef3298b3b79989da2d6f.png)

### ルールを追加する

[ルールを追加]をクリックし、日本語から英語へ翻訳するルールを以下のように設定します。

| 項目 | 値 |
| :--- | :--- |
| プロンプト | 下記参照 |
| 実行タイミング | 新規作成・更新時 |
| 作成ステータス | 公開 |
| 入力言語 | 日本語 |
| 出力言語 | 英語 |

**プロンプトの入力例:**

```text
Translate the input text into natural English. Preserve all HTML tags and the existing line break structure exactly as they are, and translate only the text content. Return only the translated result, without any explanations or introductory text.
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5e6fc7dd1266f6e0001fb943cb5300aa.png)

[更新する]をクリックして設定を保存します。

:::info
翻訳先の言語は[入力言語][出力言語]で指定します。ここで指定した[入力言語]の内容を翻訳し、[出力言語]の副言語データとして保存します。
:::

## 4. 動作確認をする

設定したコンテンツ定義からコンテンツを新規作成します。

[コンテンツ定義]をクリックし、[翻訳テスト]の[一覧]をクリックします。[追加]をクリックします。

主言語（日本語）の`Body`フィールドに日本語テキストを入力し、[追加する]をクリックします。

| フィールド | 入力値（例） |
| :--- | :--- |
| タイトル |Kurocoについて|
| Body | Kurocoはヘッドレスコンテンツ管理システムです。 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f0bc03e81fa2c28b7af27060db54f60f.png)

保存後、コンテンツ編集画面の[英語]タブに遷移します。`Body`フィールドにAIが翻訳した英語テキストが自動設定されていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d9525611c0b24fe4e54812f8d0e38a56.png)

:::info
AI自動後処理は、コンテンツの保存後にバックグラウンドで実行されます。翻訳結果が反映されるまで、しばらく時間がかかる場合があります。
:::

以上でAI自動翻訳の実装は完了です。

## 応用：英語から他の副言語へ翻訳する

英語（副言語）を起点に、その他の副言語（韓国語・ポルトガル語など）へ翻訳を連鎖させることもできます。  
このとき、日本語から英語への翻訳結果が想定と異なる場合は、英語のみを手直ししてから、その他の副言語へ翻訳し直すことができます。

:::info
この構成を利用するには、[1. 多言語設定を有効にする](#1-多言語設定を有効にする)で、英語だけでなく翻訳先となる副言語（韓国語・ポルトガル語など）も追加しておく必要があります。
:::

### 副言語ごとにルールを追加する

[AI自動後処理]で[ルールを追加]をクリックし、**翻訳先の副言語ごとに1つずつ**ルールを登録します。1つのルールに複数の出力言語をまとめると、意図した翻訳にならない場合があります。

| 入力言語 | 出力言語 | 実行タイミング | 作成ステータス |
| :--- | :--- | :--- | :--- |
| 英語 | 韓国語 | 新規作成・更新時 | 公開 |
| 英語 | ポルトガル語(BR) | 新規作成・更新時 | 公開 |

**プロンプトの入力例（韓国語のルール）:**

```text
Translate the input text into natural Korean. Preserve all HTML tags and the existing line break structure exactly as they are, and translate only the text content. Return only the translated result, without any explanations or introductory text.
```

ポルトガル語のルールも同様に、プロンプトで翻訳先の言語を指定して登録します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ab0666475596e46a575a1f2877e86b94.jpg)

[更新する]をクリックして設定を保存します。

### ルールの実行順と実行条件

複数のルールを登録した場合、次の条件で実行されます。

- **保存した言語と一致する[入力言語]のルールだけが実行されます。** 日本語で保存したときは[入力言語]が日本語のルール（日本語→英語）のみが実行され、[入力言語]が英語のルールはこの時点では実行されません。
- **翻訳結果が[出力言語]の副言語として保存されると、その保存を起点に、次は[入力言語]がその言語のルールが実行されます。** 英語への翻訳結果が保存されると、続けて[入力言語]が英語のルール（英語→韓国語、英語→ポルトガル語）が実行されます。この連鎖によって、日本語→英語→その他の副言語という順序で翻訳が進みます。
- **一度翻訳元として使われた言語へは、再度翻訳されません。** これにより、同じ言語間で翻訳が繰り返される状態を防いでいます。したがって、[入力言語]と[出力言語]に同じ言語を指定しても、翻訳が無限に繰り返されることはありません。
- **入力内容が前回から変わっていないルールは、再実行されません。**

:::info
副言語への翻訳は、英語への翻訳が保存された後に順次実行されます。すべての副言語に反映されるまで、しばらく時間がかかる場合があります。
:::

## 関連ドキュメント

- [コンテンツ定義 — AI自動処理](/ja/docs/management/content-structure-topics-group/#ai自動処理)
- [ローカライズ](/ja/docs/management/localize/)
- [副言語について](/ja/docs/reference/secondary-language/)


---

# Claude.ai での MCP コネクタの登録方法

> 元ページ: `tutorials/claude-ai-mcp-connector-setup` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/claude-ai-mcp-connector-setup/
> 概要: Claude.ai に Kuroco MCP を接続し、Kuroco のナレッジを Claude.ai から参照できるようにする手順を説明します。

このページでは、Claude.ai に Kuroco MCP を接続する手順を説明します。

MCP を接続することで、Claude.ai 上で「Kuroco の認証設定の方法は？」などと質問するだけで、Kuroco に登録されたナレッジをもとに回答が得られるようになります。

## 用語の説明

**MCP（Model Context Protocol）とは**

AI（Claude.ai など）が外部のツールやデータに接続するための標準規格です。Kuroco は MCP サーバを提供しており、Claude.ai から Kuroco の API を直接呼び出せるようになります。

**コネクタとは**

Claude.ai で外部サービスと連携するための機能です。MCP サーバを登録することで、Claude.ai がそのサービスのツールを呼び出せるようになります。

## 前提条件

### Claude.ai のプラン

| プラン | コネクタの利用 |
|-------|--------------|
| **Free** | カスタムコネクタを **1 つまで** 追加できる |
| **Pro / Max** | 複数のカスタムコネクタを追加できる |
| **Team / Enterprise** | Organization のオーナー権限を持つメンバーが追加・管理する |

:::caution
Team / Enterprise プランの場合、オーナー権限がないとコネクタを追加できません。「コネクタ」メニューが表示されない場合は、ワークスペースのオーナーに追加を依頼してください。
:::

### Kuroco 側の準備

MCP サーバが有効になった Kuroco API エンドポイント（例: `https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp`）が必要です。

MCP サーバの設定がまだの場合は、先に [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) を参照して設定を完了させてください。

:::caution
コネクタ（OAuth）で接続する場合、対象 API のセキュリティは **動的アクセストークン**（または **Cookie**）に設定されている必要があります。セキュリティが静的アクセストークン・特権付き静的トークンの API は OAuth ではなくヘッダー認証を使用します。詳細は [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) を参照してください。
:::

## 手順 1: コネクタ画面を開く

1. Claude.ai の左サイドバーにある **「カスタマイズ」** をクリックします。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/6be7e65de22623f2babc4cb6797769da.png)

2. カスタマイズ画面が開くので、左メニューの **「コネクタ」** をクリックします。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/cb47be464cf16d82375043c907975b7d.png)

:::tip
左下のアカウントアイコン → **「設定」** → **「カスタマイズ」** → **「コネクタ」** からでも同じ画面に移動できます。
:::

## 手順 2: カスタムコネクタを追加する

1. コネクタ一覧画面の右上にある **「+」** ボタンをクリックします。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ebc23fe547bfc17c1a67df9919756d1.png)

2. メニューが表示されるので **「カスタムコネクタを追加」** をクリックします。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/143b0f04f42a9e1f0c0cc78870bddf88.png)

3. 「カスタムコネクタを追加」ダイアログが開きます。以下の項目を入力します。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/79a39d49afec5aa8b1c245bffb659051.png)

   | 項目 | 入力内容 | 入力例 |
   |------|---------|--------|
   | **名前** | コネクタの名前（任意） | `Kuroco` |
   | **リモート MCP サーバー URL** | Kuroco MCP エンドポイント URL | `https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp` |
   | **OAuth Client ID** | 後の手順で Kuroco から発行される Client ID | （後で入力） |
   | **OAuth クライアントシークレット** | 今回の設定では不要 | （空欄のまま） |

:::caution
この時点では「追加」を押さないでください。先に Kuroco 側で OAuth の設定を行う必要があります。ダイアログはこのまま開いておくか、一度閉じて後で再度開いても問題ありません。
:::

## 手順 3: Kuroco で OAuth Authorization Server を作成する

Kuroco 管理画面にログインし、以下の手順で OAuth Authorization Server を作成します。

:::tip
認可サーバーで **クライアント ID メタデータドキュメント（URL クライアント ID）** を有効化すると、手順 4 のクライアント登録と Client ID の入力を省略して接続できます（Claude は CIMD に対応しています）。詳細は [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) を参照してください。このページでは、クライアントを手動登録する手順を説明します。
:::

### 3-1. OAuth Authorization Server 一覧を開く

左メニューから **「外部システム連携」→「OAuth Authorization Server」** を開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d5d7952de830985aa8f3655f1a49912.png)

### 3-2. OAuth Authorization Server を追加する

右上の **「＋追加」** ボタンを押し、以下の通り設定します。

:::info
URL は自社の Kuroco ドメインに合わせて変更してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a255beb2f4c22cdc35842762f7054850.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/831e514a8701562735a34f6bfdf25654.png)

| 項目 | 設定値 |
|------|--------|
| 名前 | 任意（例：claude） |
| 用途 | **API** |
| 対応するグラントタイプ | **authorization_code**・**refresh_token** にチェック |
| アクセストークン有効期間 | `3600`（秒） |
| リフレッシュトークン有効期間 | `2592000`（秒） |
| 認可コード有効期間 | `60`（秒） |
| 有効 | **ON** |
| ログインページ URL | `https://{自社ドメイン}.g.kuroco-mng.app/management/login/login/` |

設定が完了したら **「追加する」** を押して保存します。

追加後、一覧画面に作成した認可サーバーが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8e489e0e68d82057342f3109a244a8b6.png)

:::tip
用途「API」の認可サーバーは 1 つにすることを推奨します。Kuroco では、初回利用時に用途「API」のデフォルト認可サーバー（**Kuroco MCP API (default)**）が自動作成されている場合があります。ChatGPT など他のサービス用の認可サーバーやデフォルト認可サーバーがすでに存在する場合は、新規作成せずその認可サーバーの「クライアントを管理」から claude 用クライアントを追加してください。
:::

## 手順 4: OAuth Authorization Server クライアントを追加する

### 4-1. クライアント一覧を開く

認可サーバー一覧画面で、作成した認可サーバーの行にある **「クライアントを管理」** を押します。

OAuth Authorization Server クライアント一覧が開くので、右上の **「＋追加」** ボタンを押します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/72ea5e9007a2c784b30ce409bd98ec53.png)

### 4-2. クライアントを追加する

以下の通り設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c9fb2a4be803eafa728e25124ecfe424.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/071a4fd9adb7b6880f4e4819b1d30665.png)

| 項目 | 設定値 |
|------|--------|
| クライアント名 | 任意（例：claude） |
| トークンエンドポイント認証方式 | **none（パブリッククライアント（PKCEのみ））** |
| リダイレクト URI | `https://claude.ai/api/mcp/auth_callback` |
| 対応するグラントタイプ | **authorization_code** にチェック |
| 有効 | **ON** |

**「追加する」** を押すと **クライアント ID** が自動で発行されます。クライアント一覧に表示される **クライアント ID** を手元に控えておいてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74704a880c4579abd50220c8b132dd5a.png)

:::note
認証方式を `none（PKCEのみ）` に設定しているため、Claude.ai 側への入力はクライアント ID のみで問題ありません。クライアントシークレットは不要です。
:::

## 手順 5: Claude.ai にクライアント ID を入力して接続する

1. 手順 2 の「カスタムコネクタを追加」ダイアログを開きます（まだ開いている場合はそのまま）。
2. 以下を入力します。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/f86fa19be543cfba8310472375d92c97.png)

   | 項目 | 入力内容 |
   |------|---------|
   | **名前** | 任意（例：`Kuroco`） |
   | **リモート MCP サーバー URL** | `https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp` |
   | **OAuth Client ID** | 手順 4 で控えたクライアント ID |
   | **OAuth クライアントシークレット** | 空欄のまま |

3. **「追加」** をクリックします。
4. コネクタ一覧に追加され、詳細画面に **「連携/連携させる」** ボタンが表示されます。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/68c4a2f7ae113871ebd0367752688b99.png)

5. **「連携/連携させる」** をクリックすると Kuroco のログイン画面が開きます。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/32f82fa0e77c35febf46990205d363b8.png)

6. Kuroco のアカウントでログインすると、アクセス許可の確認画面が表示されます。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/9a31cb0b1ac7585d53c52d60ec93497f.png)

7. 内容を確認して **「許可する」** をクリックすると認証が完了し、コネクタが接続済みの状態になります。

:::caution
ログインから「許可する」までは素早く操作してください。認可コードの有効期間（60秒）が切れると `Consent request is invalid or expired` エラーになります。その場合は Claude.ai 側から「連携/連携させる」をやり直してください。
:::

## 手順 6: 接続を確認する

### 6-1. ツール一覧の確認

コネクタ一覧で登録した Kuroco コネクタをクリックすると、利用可能なツールの一覧が表示されます。`knowledge_search` などのツール名が見えていれば接続成功です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/579ec9edc12c37aa982b4814c3e6df96.png)

### 6-2. チャットで使ってみる

1. 新しいチャットを開きます。
2. チャット入力欄の左下 **「+」** ボタンをクリックします。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/851a2d082500f92776c8aa1e7a010dfc.png)

3. **「コネクタ」** を選択し、Kuroco コネクタを **トグル ON** にします。

   ![Image from Gyazo](https://t.gyazo.com/teams/diverta/ae50286e0805fd82dbe9bd24d651dd41.png)

4. 以下のプロンプトを送って動作を確認します。

   「Kuroco に登録されているナレッジを 1 件だけ取得して」

接続が成功していれば、`knowledge_search` ツールが呼ばれたことが表示され、回答に Kuroco から取得した内容が含まれます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/027042f32388f8cb29daa71c016c30ef.png)

## 関連ドキュメント

- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) — Kuroco 側の MCP 設定ガイド


---

# Admin MCP でKuroco管理画面を操作する

> 元ページ: `tutorials/connect-to-admin-mcp` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/connect-to-admin-mcp/
> 概要: Kuroco の Admin MCP に Claude Code を接続し、AI エージェントから Kuroco 管理画面の操作を行う手順を説明します。

このページでは、Kuroco の Admin MCP に Claude Code を接続し、AI エージェントから Kuroco 管理画面の操作を行う手順を説明します。

接続の設定は、管理画面の[Admin MCP](/ja/docs/management/admin-mcp/)画面を起点に行います。この画面には、接続先のエンドポイントURLと、MCPクライアントごとの設定手順が表示されます。

:::info
前提条件

- Kuroco 管理画面にログインできる管理者アカウント
- 対象の操作を実行できる管理者権限（Admin MCP 経由で実行できるのは、その管理者が管理画面で実行できる操作の範囲内です）
- Claude Code がインストールされた環境（`claude` コマンドが実行できること）
- Admin MCP のアクセス制限（IPアドレス）を有効にしている場合は、接続元のIPアドレスが許可されていること
:::

## Admin MCP への接続の前提

Kuroco には MCP サーバーが2種類あり、このページで扱うのは管理操作向けの Admin MCP です。APIごとに公開する MCP サーバーとの違いは[Kuroco の AI 機能ガイド](/ja/docs/tutorials/kuroco-ai-features-guide/#mcp-連携)を参照してください。

MCP クライアントは、用途が`AdminMCP`の OAuth Authorization Server からアクセストークンを取得します。Kuroco では、[外部システム連携] -> [ID連携] -> [OAuth Authorization Server]の一覧画面を開いた時点で、Admin MCP 用の認可サーバー **Admin MCP (default)** が自動的に作成されます。通常はこの認可サーバーをそのまま使用し、新しい認可サーバーを追加する必要はありません。

:::caution
用途が`AdminMCP`の認可サーバーは、サイト内で有効にできるのは1つだけです。また、**Admin MCP (default)** を削除した場合、自動では再作成されません。削除した場合は、一覧画面の[追加]から用途に`AdminMCP`を指定して認可サーバーを作成してください。
:::

## Admin MCP に接続する

このページでは、クライアントの事前登録が不要な[CIMD（Client ID Metadata Documents）](/ja/docs/management/sso-oauth-idp/#cimd)を有効にする方法で接続します。

### 1. [Admin MCP]画面を開く

管理画面の右上に表示されている[Admin MCP]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/76369a67d857e981968517b2376a632b.png)

[Admin MCP]画面（`/management/rcms_api/admin_mcp_info/`）が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0bf75a5cdc369b3be5c4503df567a42.png)

### 2. CIMD を有効にする

[MCPクライアント設定手順]に[Client ID Metadata Documents（CIMD）が無効です]と表示されている場合は、[CIMDを有効にする]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/db6eb68d278a30c639467291de705f80.png)

**Admin MCP (default)** の編集画面が表示されるので、[Client ID Metadata Documents（CIMD）]を有効にして[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c34cb780abca9dcf03cccdecb367f43e.png)

:::caution
CIMD を有効にしている間は、事前登録なしにどのアプリケーションでも認可を要求できます。トークンが発行されるのは同意画面で[許可する]をクリックした場合のみですが、そのトークンに付与されうるスコープの上限は認可サーバーの[許可するスコープ]で決まります。必要なスコープだけを許可してください。

CIMDを無効にしたまま運用する場合は、[Admin MCP]画面の[OAuthクライアントを管理する]からクライアントシークレットを発行し、MCPクライアントにその`client_id`・`client_secret`を設定してください（詳細は[OAuth Authorization Server](/ja/docs/management/sso-oauth-idp/)を参照）。
:::

### 3. 接続するエンドポイントURLを確認する

エンドポイントURLの形式は次のとおりです。

```text
https://{サイトキー}.g.kuroco.app/direct/rcms_api/admin_mcp/x/all
```

[MCPクライアント設定手順]には、MCPクライアントごとの設定方法がタブで表示されます。[Claude Code]タブを選択します。エンドポイントは[全ツール]（初期状態で選択されています）のまま進めます。表示された内容を確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b7af2e8798950db55a3379d5f51c988.png)

`/x/` 以降で公開するモジュールを指定しています。書き込み系ツール（作成・更新・削除など）を除いた読み取り専用の接続にする場合は[読み取り専用]を選択します（URLの末尾に`/readonly`が付きます）。特定のモジュールに絞る場合は、[Admin MCP]画面の[エンドポイント]欄に表示される形式に合わせてURLを変更します。

:::caution
これらのURLは、それぞれ別個のOAuthリソースとして扱われます。アクセストークンは、取得時に指定したURLに紐付きます。別のURLに対して使用すると`401`で拒否されるため、URLを絞ることは実際に認可範囲を絞ることになります。
:::

### 4. Claude Code に登録して認証する

この接続はコマンドを実行したプロジェクト（ディレクトリ）単位で登録されます。ターミナルで、Claude Codeで利用したいプロジェクトのディレクトリに移動してから、[MCPクライアント設定手順]の[Claude Code]タブに表示されているコマンドを2行とも実行します。

コマンドの形式は次のとおりです（画面には実際のサイトキーとサーバー名が入った状態で表示されるため、そのまま使えます）。`{サーバー名}`は Claude Code 上での識別名で、任意の値を指定できます。

```bash
claude mcp add --transport http {サーバー名} https://{サイトキー}.g.kuroco.app/direct/rcms_api/admin_mcp/x/all
claude mcp login {サーバー名}
```

ブラウザで Kuroco の管理画面ログインと同意画面が表示されるので、認証を完了します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5dfe686014b6058b12403e2df847119d.png)

:::note
CIMD で接続したクライアントは Kuroco 側にクライアントとして登録されないため、同意画面には[このサイトに未登録のアプリケーション]という警告が表示されます。これはアプリケーションが危険であることを示すものではありません。詳細は[同意画面に表示される「このサイトに未登録のアプリケーション」](/ja/docs/management/sso-oauth-idp/#cimd-unregistered-application)を参照してください。
:::

:::note
ここで許可したアクセスレベルと、ログインしたメンバーの権限によって、Claude Codeから実行できる操作が制限されます。CIMDを無効にして接続している場合は、これに加えてOAuthクライアントの[許可するスコープ]も上限になります。
:::

### 5. Kuroco Skills をインストールする(推奨)

[Kuroco Skills](/ja/docs/tutorials/kuroco-skills-overview/) は Claude Code をはじめとする AI エージェント向けの Agent Skills パッケージです。Kuroco の仕様やベストプラクティスに加え、Admin MCP の利用方法（`kuroco-admin-mcp`スキル）が含まれるため、インストールしておくと Admin MCP のツールを使った指示を実行しやすくなります。

手順4を実行したプロジェクトのディレクトリで、次のコマンドを実行します。

```bash
npx skills add diverta/kuroco-skills
```

インストール後、Claude Code を再起動するとスキルが有効になります。`/plugin`コマンドを使う方法や、リポジトリを直接クローンする方法は[Kuroco Skills の使い方](/ja/docs/tutorials/kuroco-skills-overview/#インストール方法)を参照してください。

### 6. 動作確認

Claude Code で`/mcp`を実行し、登録した MCP サーバーの状態が接続済みになっていること、Admin MCP のツールが一覧に表示されることを確認します。状態が`needs authentication`のままの場合は、`claude mcp login {サーバー名}`で認証を実行します。

ツールが利用できることを確認できたら、[指示の例](#指示の例)を試してください。接続できない場合は[うまく接続できない場合](#うまく接続できない場合)を参照してください。

## 指示の例

次のような指示を Claude Code に与えて、Admin MCP のツールが呼び出されることを確認できます。

### 調査・棚卸し（読み取りのみ）

読み取り専用のURLでも実行できます。

```text
エンドポイントの設定にセキュリティ上の問題がないか調査してください。
```

```text
リクエスト数の利用状況を確認して、Kuroco利用料を抑えられるポイントがないか調べてください。
```

```text
NEWSのコンテンツで、公開中なのに本文が空のものを一覧にしてください。
```

### 一括更新（書き込みを伴う）

書き込み系ツールを含むURL（`/readonly`なし）と、[読み書き]以上の権限レベルが必要です。

```text
NEWSのコンテンツのすべてのslugをnews-{topics_id}に更新してください。
```

```text
2020年以前に公開したお知らせを非公開にしてください。まず対象件数を確認してから実行してください。
```

毎回同じ前提を指示に含める必要がある場合は、[Admin MCP]画面の[Admin MCP サイト固有の指示]に記載しておくと、接続した AI クライアントに共通の前提として渡せます。

## うまく接続できない場合

| エラー | 主な原因 | 対処 |
| :--- | :--- | :--- |
| `invalid_target: resource is not permitted for this client` | クライアントの[対象リソース]と、MCP クライアントに設定したURLが一致していません。 | どちらかに揃えます。`/readonly`の有無も一致させます。 |
| `invalid_scope: scope '...' not allowed for this client` | 認可サーバーまたはクライアントで許可されていないスコープを要求しています。 | 認可サーバーとクライアントの編集画面を開き、[許可するスコープ]の権限レベルを選択して[更新する]をクリックします。MCP クライアントが以前のメタデータを保持している場合は、登録を削除して再度追加します。 |
| `redirect_uri does not match a registered URI` | クライアントの[リダイレクトURI]に、MCP クライアントのコールバックURLが登録されていません。 | ブラウザのアドレスバーに表示されている認可URLの`redirect_uri`パラメータの値を確認し、クライアントの[リダイレクトURI]に登録します。 |
| `401` で拒否される | トークンを取得したURLと異なるURLに接続しています。 | MCP クライアントに設定したURLと、接続時に決めたエンドポイントURLを一致させ、再度認証します。 |
| `403` で拒否される | Admin MCP のアクセス制限（IPアドレス）で接続元が許可されていません。 | [環境設定] -> [管理画面]の「Admin MCPのアクセス制限(IPアドレス)」に接続元のIPアドレスを追加します。 |

クライアントの設定（[対象リソース]・[許可するスコープ]・[リダイレクトURI]など）を変更した場合は、MCP クライアント側で再認証してください。

## 補足

- 参照だけを行う用途では、`/readonly`を付けたエンドポイントURLと、クライアントの権限レベル[読み取り専用]を組み合わせてください。書き込み系ツールが除外され、トークンに書き込み権限も付与されません。
- [読み書き]で委譲される権限の上限は、[Admin MCP]画面の[mcp:tools.write が委譲する権限]でモジュールごとに確認できます。より広く委譲する場合は[全操作（委譲先メンバーの権限の範囲）]を選択します。
- サイト固有の運用ルールを AI クライアントに伝える場合は、[Admin MCP]画面の[Admin MCP サイト固有の指示]に記載します。この指示でトークンの権限が広がることはなく、AI クライアント側の解釈に依存するため、アクセス制御の代わりには使えません。
- Claude Code 以外のクライアント（Claude、ChatGPT、Codex CLI、Cursor、VS Code、n8n、Dify、Slackbot など）の設定手順は、[Admin MCP]画面の各タブと[MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)を参照してください。

## 関連ドキュメント

- [Admin MCP](/ja/docs/management/admin-mcp/)
- [Kuroco Skills の使い方](/ja/docs/tutorials/kuroco-skills-overview/)
- [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/)
- [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)
- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)
- [OAuth Authorization Server](/ja/docs/management/sso-oauth-idp/)
- [Client ID Metadata Documents（CIMD）](/ja/docs/management/sso-oauth-idp/#cimd)


---

# DeepL APIを使用して、主言語に入力した文章を自動で翻訳し副言語に追加する

> 元ページ: `tutorials/deepl-api-auto-translation` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/deepl-api-auto-translation/
> 概要: DeepL APIを利用して、新規追加したコンテンツを自動で翻訳し副言語のコンテンツとして登録する方法を紹介します。DeepL APIを使用することでHTMLタグの構成をそのままに文章のみの翻訳が可能です。

## 概要
Kurocoはカスタム処理を利用して、任意の処理を管理画面に追加できます。
このチュートリアルでは、例としてDeepL APIを利用して、新規追加したコンテンツを自動で翻訳し副言語のコンテンツとして登録する方法を紹介します。  

DeepL APIを使用することでHTMLタグの構成をそのままに文章のみの翻訳が可能です。  
また、DeepLの用語集の機能を利用して、翻訳の結果をチューニングします。

### 学べること
以下の流れで自動翻訳機能を実装します。
- [認証キーの取得・登録をする](#認証キーの取得登録をする)
- [多言語の設定をする](#多言語の設定をする)
- [コンテンツ定義を作成する](#コンテンツ定義を作成する)
- [APIを作成する](#apiを作成する)
- [カスタム処理を作成する](#カスタム処理を作成する)
- [動作確認をする](#動作確認をする)

### 前提条件
:::info
機能はDeepL APIのドキュメントを元に作成しています。  
DeepL APIの仕様は[公式ドキュメント - DeepL API](https://www.deepl.com/ja/docs-api)を参照してください。
:::

## 認証キーの取得・登録をする
### DeepL APIの申込をして認証キーを取得する
まずは[DeepL API](https://www.deepl.com/ja/pro-api?cta=header-pro-api)にアクセスし、DeepLに登録します。

1か月に500,000文字までの翻訳であれば、無料版で構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94e9073d5e47f0d8051be50fba05d9b9.png)

登録が完了したら[DeepL Proのアカウント情報ページ](https://www.deepl.com/ja/account/summary)にアクセスします。  
アカウント情報下部にDeepL APIで使用する認証キーが表示されているので、これをコピーします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d6ecbe5ab18e5d724f670d42b073889a.png)

### Kuroco管理画面に認証キーを登録する
Kurocoの管理画面にアクセスし、[環境設定] -> [シークレット]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/25b831fd4835ad993f02298629b9e8cf.png)

[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c51de1ecc8ead6fa837c6492757a7276.png)

以下のように入力して、[追加する]をクリックします。

|項目|値|
|:--|:--|
|名前|DEEPL_API_KEY|
|値|DeepL APIで使用する認証キー|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3aee2f0fe65a192c9abf1ad69115fe8a.png)

以上でDeepL APIを利用する準備が整いました。

## 多言語の設定をする
Kurocoの管理画面にアクセスし、[環境設定] -> [ローカライズ]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7b8b41455b6d4e342e25ebad0317fbc1.png)

本チュートリアルでは、主言語を日本語[ja]、副言語を英語[en]として進めます。  
以下の設定をして、[更新する]をクリックします。

|項目|値|
|:--|:--|
|有効にする|チェックを入れる|
|主言語|日本語[ja]|
|副言語|英語[en]|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f488d477a79d1c6d9c0f39209882c0fc.png)

以上で多言語の設定は完了です。  

## コンテンツ定義を作成する
翻訳の結果をチューニングするための用語集を登録するコンテンツ定義と、自動翻訳の対象となるコンテンツ定義を登録します。  
コンテンツ定義一覧ページで[追加]をクリックして、以下2つのコンテンツ定義を作成します。

### 用語集
用語集を使って語句の訳し方を指定すれば、翻訳後の編集に時間をかけなくても一貫性のある訳文を作成できます。  
https://www.deepl.com/ja/blog/translate-your-way-with-the-deepl-glossary  

DeepLの用語集をKurocoのコンテンツで管理するため、用語集のコンテンツ定義を作成します。  
用語集のコンテンツ定義では、日本語と英語のペアの繰り返し項目と、DeepLの用語集IDを登録するテキスト項目を登録します。
以下のようになります。

|ID|親項目|項目名|項目設定|
|:--|:--|:--|:--|
|1|親項目名:Language pairs<br/>親項目識別子:glossary<br/>繰り返し回数:30|項目名:JA<br/>識別子:source_lang|テキスト|
|2|JAを選択|項目名:EN<br/>識別子:target_lang|テキスト|
|3|選択なし|項目名:glossary_id<br/>識別子:glossary_id|テキスト|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d4e8bc576e7d3700dc66b1a02fea1fea.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe26b3080ba052474023e71622f85a06.png)

:::tip
グループの設定はコンテンツ定義追加時にできませんので、一度各項目を追加した後に親項目と繰り返し回数の設定をしてください。
:::

:::tip
項目の繰り返し回数はデフォルトで30が最大値となりますが、[管理画面](/ja/docs/management/management-screen/)で最大99まで変更可能です。
:::

また、用語集は1つのコンテンツを更新して使うため、元となるコンテンツを1つ登録しておきます。  

コンテンツ一覧ページで[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d08dfe96ce6d7c6de4ba2ebc9ced9cec.png)


例として以下のように登録します。  
ここで設定した言語のペアがDeepLに翻訳リクエストを送る際の語句の訳し方の指定になります。  

例えば記事という単語は通常、Articleと訳されますが、これにより、Contentと訳すように指定できます。  

|項目|値|
|:--|:--|
|Slug|glossary|
|タイトル|用語集|
|Language pairs 1|JA:記事<br/>EN:Content|
|Language pairs 2|JA:副言語<br/>EN:Secondary languages|
|glossary_id |空欄|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d17c88ffbb70c88a1ab7fda770a6cd7.jpg)

入力ができたら[追加する]をクリックして、コンテンツを登録します。  

### 自動翻訳コンテンツ
自動翻訳の対象となるコンテンツ定義は、Wysiwygのみのシンプルな設定にします。  
以下のようになります。  

|ID|親項目|項目名|項目設定|
|:--|:--|:--|:--|
|1|選択なし|項目名:WYSIWYG<br/>識別子:source_text|WYSIWYG|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ec67fd31092eeac5135f452898020e9.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88401ba23bda7a962240787e5bbe89a2.png)

## APIを作成する
### 内部処理用のAPI作成
Kuroco内部でのみ利用するエンドポイントはAPIを分けておくことをお勧めします。  
そこで、まずは内部利用のためのAPIを新規で作成します。  
既に追加済みの場合は次のステップに進んで構いません。  

#### APIの作成
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c341acced8d685e67ec1da1e85abac.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|Internal|
|版|1.0|
|ディスクリプション|内部処理用のAPI|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c04c600fc74102913e9e668ae5cca0e.png)

#### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bc5cb1beb28c74ede6aeca89715a647.png)

セキュリティを[動的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/62aaa225db5d12ee84ccc6d5a52411fe.png)

セキュリティを[動的アクセストークン]に設定後、`Login::token`のエンドポイントが無い場合、利用をお勧めされますが、内部利用のみの場合は無視して構いません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0bb1efe099bdae8f1c0481037416a5d9.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/74cd7a36fd926dbc20b04812553072c7.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET  
- POST
- OPTIONS

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f2bc3744fe6a2ab042456fa8c635195c.png)

問題なければ [保存する] をクリックします。 

### エンドポイントの作成
エンドポイントは「用語集を取得するエンドポイント」「用語集を更新するエンドポイント」「副言語を更新するエンドポイント」の3つを作成します。  

InternalのAPIから[新しいエンドポイントの追加]をクリックしてそれぞれ作成します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bfc5c05d2cc1c6daf4740f6787a467f.png)

#### 用語集を取得するエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|get_glossary|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|details|
|topics_group_id|用語集のコンテンツ定義ID(8)|
|ext_group|チェックを入れる|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3706e9755046199fe8bfa6fccf38d396.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8c11699eb64e3cb336689b15d4098d00.png)

#### 用語集を更新するエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|update_glossary|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|update|
|topics_group_id|用語集のコンテンツ定義ID(8)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aaff4f80434e2559b42d211eb41dac14.png)  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5816bf53b774093dfedbe4cb3e36421.png)

#### 副言語を更新するエンドポイント

|項目|設定内容|
| :--- | :--- |
|パス|update_content|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|update|
|topics_group_id|自動翻訳コンテンツのコンテンツ定義ID(9)|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/401490e1e912dd5eeeadbbaefefd2999.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/746967c5ce5a77794b75dc4faa869167.png)

## カスタム処理を作成する
コンテンツとエンドポイントの準備ができたら、DeepLと連携して翻訳する処理をカスタム処理に書いていきます。  

[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45a3b82e8fec3d1ad46a72c0bf8d394b.png)

[追加]をクリックして、「用語集の登録・削除をするカスタム処理」と、「コンテンツの翻訳をして副言語に登録するカスタム処理」の2つを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/471bc146570ff60efb362ece59b7fbe1.png)
  

### 用語集の登録・削除をするカスタム処理
DeepLに登録する用語集は更新が許可されていないので、都度、削除・更新をする運用となります。  

先ほど作成した`用語集`のコンテンツ更新をトリガにして、DeepLの既存用語集を削除し、更新された翻訳のペアを再登録する処理とします。

以下のように設定します。

|項目|値|
|:--|:--|
|タイトル|deepl_manage_glossary|
|識別子|deepl_manage_glossary|
|トリガ|コンテンツの更新後/用語集のコンテンツ定義ID(8)|
|処理|以下の内容|

```smarty reference title="deepl_manage_glossary"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/trigger/deepl_manage_glossary.txt
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c1f34196005bd41e47b030845e87b4e.png)

:::caution
`/rcms-api/3/get_glossary/`の部分はご自身のエンドポイントのURLに置き換えてください。
:::

:::tip
トリガがループするような使い方をする場合は、処理がループすることを防ぐため、以下のコードをカスタム処理の先頭に記述します。
```
{if $smarty.server.HTTP_RCMS_X_API_REQUEST_CNT > 0}
    {return}
{/if}
```

APIの無限ループ対策が実施されているため、この記述がなくてもループは停止しますが、設定されている制約により、トリガは2回作動します。  
詳しくは[コンテンツ更新後のトリガが二重に呼ばれるのはなぜですか？](/ja/docs/faq/why-is-the-trigger-called-twice-after-content-update/)を参照してください。
:::

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

### コンテンツの翻訳をして副言語に登録するカスタム処理
コンテンツの翻訳をして副言語に登録するカスタム処理は、コンテンツの追加をトリガとして動作させます。  
追加されたコンテンツをDeepLに送り、翻訳されたHTMLを副言語に追加します。  

:::info
tag_handlingパラメータをhtmlに設定してDeepLにリクエストを送ることで、HTMLタグを考慮した翻訳をしています。  
詳しくは[HTML Handling](https://www.deepl.com/ja/docs-api/html/splitting-on-newlines)を参照してください。
:::

:::info
Kurocoの副言語を更新する場合は、`_doc_lang`パラメータをクエリで指定します。  
:::

以下のように設定します。

|項目|値|
|:--|:--|
|タイトル|deepl_translate|
|識別子|deepl_translate|
|トリガ|コンテンツの追加後/自動翻訳コンテンツのコンテンツ定義ID(9)|
|処理|以下の内容|

```smarty reference title="deepl_translate"
https://github.com/diverta/kuroco-documents/blob/main/sample_code/custom_function/trigger/deepl_translate.txt
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53619e780236e0f6904d57bdc2a029b0.png)

入力ができたら[追加する]をクリックしてカスタム処理を追加します。

## 動作確認をする
以上で自動翻訳の設定は完了です。コンテンツを更新・追加して動作の確認をします。  

### 用語集
まずは、用語集のコンテンツを更新します。  
任意のLanguage pairsを追加し、glossary_id は空のまま更新します。  
更新後、glossary_idが自動で追加され、カスタムログに用語集追加完了のログが残ります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bf6632b1096dc9e717468c83a9e7cc96.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d421cb81dd93f53e2c9675729088f1d8.png)

以降の更新もglossary_idは手動で編集する必要はありません。
DeepLの用語集登録時に自動で更新されます。  

:::tip
glossary_idは手動で更新しないので、実際の運用時は[コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)を参考に非表示にするCSSを適用するのも有効です。
:::

### コンテンツの自動翻訳
次に、コンテンツの自動翻訳の動作を確認します。  
自動翻訳コンテンツ一覧のページから[追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73d18b324efe42410b45ac59544fe8b1.png)

任意の日本語のコンテンツを入力し、[追加する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f4ebcb98f890ba48e3767745501b9c0a.png)

追加後のコンテンツを確認すると、副言語のコンテンツが同時に追加されていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/347c43f658475b8772fdfa0e550a83b8.png)

また、翻訳の内容を確認すると用語集で登録した通り、記事をContent、副言語をSecondary languagesと訳していることが分かります。  

以上で、DeepL APIを利用した自動翻訳機能の実装方法の紹介を終わります。  
DeepL APIはPDFやWordファイルをそのまま翻訳する[Translate Documents](https://www.deepl.com/ja/docs-api/documents)の機能も持っていますので、本ドキュメントを参考にトライしてみてください。 

## 関連ドキュメント
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)


---

# Model Context Protocol (MCP) と Kuroco の連携

> 元ページ: `tutorials/expose-a-kuroco-api-with-mcp` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/
> 概要: Kuroco が Model Context Protocol (MCP) を実装し、HTTP トランスポートを使用して公開 API エンドポイントを LLM クライアントにシームレスに公開する方法を学びます。

Kuroco は Model Context Protocol (MCP) を実装しており、LLM クライアントが HTTP 経由で公開 API エンドポイントを呼び出せます。このガイドでは、Kuroco エンドポイントを MCP 経由で公開する方法を 2 つのパートで解説します：
- Kuroco のデータを提供して LLM のレスポンスを充実させる
- LLM を使ってコンテンツを作成・更新する

AI クライアント向けに Kuroco ツールを公開する際の詳細なリファレンスとしてご活用ください。

## Kuroco における Model Context Protocol (MCP) とは

MCP は AI クライアントをツールサーバーに接続するためのオープンプロトコルです。Kuroco は MCP サーバーを公開しており、Claude、ChatGPT、IDE アシスタントなどのクライアントが型付きツールとして API を検出し、構造化された入力で呼び出せます。どの API 操作も MCP で公開できます。このドキュメントでは、コンテンツの読み取り・書き込み操作に焦点を当てます。

### 主な特徴

- **HTTP トランスポート**: Kuroco の MCP は [MCP 仕様](https://modelcontextprotocol.io/specification)の Streamable HTTP トランスポートに準拠しています（レスポンスはストリーミングではなく、単一の JSON レスポンスとして返されます）。
- **高度なカスタマイズ性**: Kuroco API とカスタム関数を組み合わせて、多様なユースケースに対応したツールを公開できます。
- **既存のエンドポイントで動作**: 既存の Kuroco API エンドポイントをそのまま LLM ツールとして公開できます。

### 制限事項

- **認証**: LLM クライアントは公開 API およびアクセストークンで保護されたエンドポイントを利用できますが、すべてのクライアントがヘッダーへのトークン設定をサポートしているわけではありません。各クライアントの対応状況は [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)を参照してください。

## 前提条件

### Kuroco 環境

- セキュリティを特権付き静的トークンに設定した API 定義で、MCP サーバーの設定が有効になっていること
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/0e853b7a257dfee913860d8ca8b0421f.png)

- LLM のレスポンスで表示したい、または LLM に作成・更新させたいコンテンツ定義が存在すること

### サポートされている LLM クライアント

クライアントの対応状況と設定手順は [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) を参照してください。


## Kuroco コンテンツで LLM のレスポンスを充実させる

読み取り専用エンドポイント（例：コンテンツリスト・詳細、ニュースリストなど）を MCP ツールとして公開し、LLM が会話中に Kuroco のコンテンツを取得できるようにします。

### データスキーマの作成

MCP を有効にしたエンドポイントには入力データ定義の設定が必須です。スキーマを設定することで、LLM が渡せるパラメータを明示的に定義でき、必要なパラメータのみに絞ることができます。

これは JSON または Zod スキーマを使用して実現できます。Kuroco 全体で使用できるデータスキーマを作成するには、[オペレーション] → [データ定義] タブにアクセスします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9b7caa1e47a9683e04556efd668538f0.png)

スキーマを手書きするのは手間がかかるため、「Zod schema」バリデーターの使用を推奨します。JSON・Zod スキーマいずれにも対応しており、Zod スキーマは自動的に変換されます。
データ定義の追加をクリックし、ページ下部の「Zod AI ジェネレーター」をクリックしてツールを開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d3ff795fac1b9564bd18b60499652b5.png)

ここでは、filterクエリを使用して subject フィールド内の文字列を検索できるようにしたいので、AI に次のように指示します：
`add a field named filter that should contain "subject contains" followed by any string`

生成されたスキーマを適用しZod定義を確認すると、入力文字列を subject フィールドに対して正規表現でマッチさせるスキーマが正しく生成されています。ツール右上の「保存して適用」ボタンをクリックすると、生成されたスキーマがKurocoのデータ定義編集画面に反映されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/119098d4904c123c9fcc66b05da575ac.png)

最後に、ページ下部の [追加する] をクリックしてデータ定義を追加します。

このチュートリアルで設定した値は以下になります。

|項目|値|
| :--- | :--- |
|Name|`Tutorial`|
|Slug|`(空)`|
|Schema type|`Zod schema`|
|Schema|`z.object({filter: z.string().regex(/^subject contains .+/).describe('Filter that contains the phrase "subject contains" followed by any string')})`|

### 読み取りエンドポイントの作成

エンドポイント一覧画面で [追加] をクリックし、以下を設定します。

| フィールド | 入力 |
| :--- | :--- |
| Path | `list` |
| Category → Model → Operation | Content → Topics (v1) → list |
| Parameters | `topics_group_id`: (対象グループ ID)<br/>`filter_request_allow_list`：subject |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b05179575e6f9cde1b9519613d7db07.png)

### 読み取りエンドポイントで MCP を有効化する

1. エンドポイントの設定を開き、MCP 設定セクション/タブに移動します。
2. [ツール名]に一意でわかりやすい名前を入力します。（例：`search_topics_by_subject`）
3. [入力データ定義]で前の手順で作成したスキーマを選択します。出力データ定義はオプションです（このチュートリアルでは使用しません）。
4. [ステータス]のトグルをオンにしてツールを公開します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bf55d5be57d8b90c24b58925251c63c4.png)

:::tip ヒント
- ツール名は何をするかが名前から分かるように具体的にしてください（例：`search_topics_by_subject`）。
- 一覧取得・詳細取得など用途が異なる場合は、それぞれ個別のエンドポイントに MCP を設定してください。
:::

:::info
最適な結果を得るために、エンドポイントのサマリーと説明を整備してください。
:::

## LLM を使用してコンテンツを作成・更新する

書き込み可能なエンドポイント（例：コンテンツ作成/更新）を MCP ツールとして公開し、対応クライアントからコンテンツを作成・編集できるようにします。

### データスキーマの作成

GET エンドポイントと同様の手順で、コンテンツ定義に適したスキーマを生成します。
データ定義を以下のように登録します。

```ts
z.object({
  subject: z.string(),
  open_flg: z.number().int().gte(0).lte(1),
  ext_1: z.string()
});
```

### 書き込みエンドポイントの作成

#### コンテンツ追加エンドポイント

エンドポイント一覧画面で [追加] をクリックし、以下を設定します。

| フィールド | 入力 |
| :--- | :--- |
| Path | `topics-create` |
| Category → Model → Operation | Content → Topics (v1) → insert |
| Parameters | `topics_group_id`: (対象グループ ID) |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8c1a4bbb4bfd8ba8c5171f4c76d95a1.png)

[追加] をクリックして保存します。

#### コンテンツ更新エンドポイント

エンドポイント一覧画面で [追加] をクリックし、以下を設定します。

| フィールド | 入力 |
| :--- | :--- |
| Path | `topics-update/{topics_id}` |
| Category → Model → Operation | Content → Topics (v1) → update |
| Parameters | `topics_group_id`: (対象グループ ID) |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e9bbea6b093eebac9fa3f41013f2cbfa.png)


### 書き込みエンドポイントで MCP を有効化する

1. エンドポイントの設定を開き、MCP 設定セクション/タブに移動します。
2. [ツール名]に一意でわかりやすい名前を入力します。（例：`create_blog_post`、`update_blog_post`）。
3. [入力データ定義]で前の手順で作成したスキーマを選択します。出力データ定義はオプションです（このチュートリアルでは使用しません）。
4. [ステータス]のトグルをオンにしてツールを公開します。。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/239708a2fd587fad0579b19f1603cb31.png)

:::caution
書き込み操作には認証が必要です。使用する LLM クライアントが MCP 設定でリクエストヘッダーを設定できることを確認してください。対象クライアント用のトークンを API の Swagger UI で生成し、クライアント側の設定でヘッダーに指定します。
:::

:::info
最適な結果を得るために、エンドポイントのサマリーと説明を整備してください。
:::

## Claude Code を使用した MCP サーバーのテスト

Claude Code はリモート HTTP トランスポートとヘッダー認証に対応しており、読み取り・書き込み操作を手軽にテストできます。

まず、API のトークンを生成します。対象 API の Swagger UI にアクセスし、ページ右上の [生成] ボタンをクリックして必要な情報を入力し、生成されたトークンをコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9edf765daae4a44c00da6963e1ffc5d4.png)

次に、MCP サーバーの URL を確認します。MCP サーバーを有効にした API 設定画面を開き、表示されている URL をコピーします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/49597ec5dc8e5cf6d770e1501788b5dd.png)

次のコマンドで Kuroco MCP サーバーを Claude Code に登録します：

```bash
claude mcp add --transport http kuroco https://your-kuroco-domain.com/rcms-api/{api_id}/mcp --header "X-RCMS-API-ACCESS-TOKEN: <your-token>"
```

登録後、Claude Code のチャットから Kuroco のコンテンツを取得したり、コンテンツの作成・更新ができます。

読み取りの例：
```
北海道の食べ物について教えてください。
```

書き込みの例：
```
タイトルが「テスト投稿」、ext_1 が「これはテスト投稿です」の記事を作成してください。
```

:::tip
エンドポイントのサマリーと説明が適切に設定されていれば、「Kuroco のデータから」などと明示しなくても、Claude Code は自動的に適切な MCP ツールを選択して呼び出します。
:::

MCP ツールが正しく登録されているか確認するには：

```bash
claude mcp list
```

テスト後に MCP サーバーを削除するには：

```bash
claude mcp remove kuroco
```

## クライアント設定

各クライアントの詳細な設定手順は以下を参照してください。
[MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)

主要なチャット・コーディング系クライアント（Claude、ChatGPT Apps、Copilot、Codex / Cursor / Zed、GitHub Copilot、Jan、カスタム実装）向けの設定手順をまとめています。

Claude.ai のコネクタ機能（OAuth 認証）で接続する場合は、[Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/) を参照してください。

## 関連ドキュメント
- [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)
- [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/)
- [API](/ja/docs/management/api-list/)
- [API セキュリティ](/ja/docs/management/api-security/)
- [静的アクセストークンによるAPIアクセス制限の方法](/ja/docs/tutorials/restricting-api-access-with-statictoken/)


---

# AIによる回答を生成する

> 元ページ: `tutorials/generating-ai-responses` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/generating-ai-responses/
> 概要: KurocoのAI機能では、ChatGPTのように質問に回答するAIを容易に利用できます。[AI] -> [ベクトルデータ]のAIを有効にするだけですぐに利用開始できます。

## 概要
KurocoのAI機能では、ChatGPTのように質問に回答するAIを容易に利用できます。
また、AIの回答時に登録したコンテンツを参照させたり、事前に登録したAI辞書で置換するなどにより、回答の調整が可能です。

本チュートリアルでは、KurocoのAPIを通して、AIによる回答を得る方法と、回答の精度を上げる設定について紹介します。

### 学べること
本チュートリアルでは以下の手順でKurocoのAPIを利用して、AIによる回答を得る方法を学びます。  

- [AIの準備をする](#aiの準備をする)
- [AIの回答をKurocoのAPIから得る](#aiの回答をkurocoのapiから得る)
- [回答の精度を上げる](#回答の精度を上げる)


## AIの準備をする
### AIを有効にする
[AI] -> [ベクトルデータ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e47d56cef62185748d29321b79ba79d.png)

AIの項目を有効にして、[更新する]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e166aac6a92486724a8354f73504e7d4.png)

### エンドポイントを設定する
エンドポイント一覧のページから[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1c774d38f6c1b50bac7e7e08845708ca.png)

以下のエンドポイントを作成します。

|項目|設定内容|
| :--- | :--- |
|パス|ai/chat|
|カテゴリー|AI|
|モデル|OpenAI|
|オペレーション|chat|
|model|auto|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1fe68ea7b57ed2c0cf6f74026b023bc7.png)

## AIの回答をKurocoのAPIから得る
`text`の名前でリクエストボディにAIへの質問を設定して、エンドポイントにリクエストを送ると、質問に対する回答のレスポンスが返ってきます。  

APIのページから[SwaggerUI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a29ed36beb5d900833fd272709a947dd.png)

以下のようにtext項目に「Kurocoについて教えてください。」と入力し、[Execute]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9be1c71e167d8ecdf02e046d24d6f755.png)

以下の回答がレスポンスされました。  

> `Kuroco（クロコ）は、主に日本で提供されているクラウド型のデータベース管理システムやバックエンドサービスの一つです。Kurocoは、開発者がアプリケーションやウェブサービスを迅速に構築できるように設計されており、特にモバイルアプリやウェブアプリのバックエンドを簡単に構築・管理するための機能を提供しています。\n\n### Kurocoの主な特徴\n\n1. **ノーコード/ローコード開発**: Kurocoは、プログラミングの知識が少ないユーザーでも使いやすいインターフェースを提供しており、迅速なアプリケーション開発を可能にします。\n\n2. **データベース管理**: データの管理や操作が簡単に行えるように設計されており、データのCRUD（作成、読み取り、更新、削除）操作が直感的に行えます。\n\n3. **APIの自動生成**: Kurocoは、データベースの設計に基づいて自動的にAPIを生成する機能を持っており、フロントエンドとバックエンドの連携がスムーズに行えます。\n\n4. **セキュリティ**: ユーザー認証やデータのアクセス制御など、セキュリティに関する機能も充実しており、安全なアプリケーション開発が可能です。\n\n5. **スケーラビリティ**: クラウドベースのサービスであるため、トラフィックの増加に応じてスケールアップが容易です。\n\n6. **多様なインテグレーション**: 他のサービスやツールとの連携が可能で、開発者は必要に応じて機能を拡張できます。\n\nKurocoは、特にスタートアップや中小企業にとって、迅速にプロトタイプを作成したり、MVP（Minimum Viable Product）を開発したりする際に非常に有用なツールです。`

![Image from Gyazo](https://t.gyazo.com/teams/diverta/66bfc5d0d01b8ce2d9c048ea643e63d4.png)

## 回答の精度を上げる
以上の設定だけで簡単に、AIからの回答を得ることができますが、AIの回答が間違っていることも多いです。
特にAIが知らない内容については内容を予測して回答してきますので、回答に利用する情報を予め学習させます。

### AIが回答に利用する情報を予めコンテンツに登録する
#### コンテンツ定義を追加する
[コンテンツ定義一覧](/ja/docs/management/content-structure-topics-group/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ec5be190619828fb06182069a8ced69c.png)

以下の内容で設定をします。  

**全般**

|項目|設定|
|:--|:--|
|名前|AIに利用させるコンテンツ|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cab52b604c3bf5ac2871160511c08f5.png)

**項目設定**

|項目|設定|
|:--|:--|
|ext_1|項目名：テキスト<br/>項目設定：テキストエリア<br/>繰り返し回数：1|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b4b95d6f14350e2513dc76c9e7284f1.png)

**検索設定**

|項目|設定|
|:--|:--|
|ベクトルデータに変換する|有効にする|
|その他|デフォルト設定を利用|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b06016149163eee24733676b339f7f76.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。 

#### コンテンツを追加する
AIが利用する為の情報をコンテンツに登録します。    

[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1a4e135e98ca7613521c6114d047e485.png)

以下を入力し、[追加する]をクリックします。 

|項目|値|
|:--|:--|
|タイトル|Kurocoとは？|
|テキスト|Kurocoは株式会社ディバータが提供するヘッドレスCMSです。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bee89d5b7b8097db59c46dfb6bf11b7d.png)

コンテンツの内容を参照して回答を生成する場合は、OpenAI::chat_contents_search のエンドポイントを使用します。
以下のエンドポイントを作成します。  

|項目|設定内容|
| :--- | :--- |
|パス|ai/chat_contents_search|
|カテゴリー|AI|
|モデル|OpenAI|
|オペレーション|chat_contents_search|
|model|auto|
|topics_group_id|参照するコンテンツのコンテンツ定義ID|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a4d6af7b937cbe32ef2dd9bb7e53c63.png)

準備が追加できたら、SwaggerUIを開き、エンドポイントに「Kurocoについて教えてください。」とリクエストを送ります。  
すると今度は以下のような回答が得られました。  

> Kurocoは株式会社ディバータが提供するヘッドレスCMSです。\n

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c88f7bc69c72f4936d304df5f7fc5bdf.png)

### AIの回答内容に指示を出す。
また、回答の際に選択する言葉遣いや内容の調整については、エンドポイントの`prompt`のパラメータで渡します。  

エンドポイント一覧のページから先ほど作成したエンドポイントの[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50aa909d3272c12f9fd25034ae9cb4c3.png)

以下の設定を追加して[更新する]をクリックします。    

|項目|値|
|:--|:--|
|prompt|あなたは株式会社ディバータの営業です。Kurocoについて質問がきたらミーティングに繋がるように回答してください。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e68f548f08866d1a135f3026776a000.png)

この状態で再度SwaggerUIを開き、エンドポイントに「Kurocoについて教えてください。」とリクエストを送ります。  
すると今度は以下のような回答が得られました。 

> Kurocoについてですね！ありがとうございます。\n\nKurocoは株式会社ディバータが提供するヘッドレスCMSで、コンテンツをAPI経由で様々なデバイスに配信できます。Webサイトはもちろん、モバイルアプリ、デジタルサイネージなど、多様なチャネルでコンテンツを一元管理できるのが強みです。\n\n例えば、Webサイトとモバイルアプリでそれぞれ別々にコンテンツを管理するのは大変ですよね。Kurocoを使えば、一つのプラットフォームでコンテンツを作成・編集するだけで、全てのチャネルに反映されるので、運用コストを大幅に削減できます。\n\nその他にも、柔軟なAPI連携、多言語対応、ワークフロー機能など、様々な機能が備わっています。\n\nもしKurocoにご興味をお持ちでしたら、貴社の課題や要件に合わせてより詳しい情報をご提供し、最適なソリューションをご提案できます。具体的なお話やデモのご希望がありましたら、ぜひお気軽にお問い合わせください。ミーティングを設定させて頂き、Kurocoがどのように貴社のビジネスに貢献できるかをご説明させていただきます。いかがでしょうか？\n

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c01eba25cd2bbf7d264d0310bf9864b6.png)

<!--設定が無くなったので非表示-->
<!--
### temperatureを調整する
OpenAIのエンドポイントは生成された回答にランダム性を加えるために、生成プロセス中にtemperatureと呼ばれるパラメータを使用します。
具体的には、temperatureを小さくすると回答に曖昧さがなくなり、temperatureを大きくするとより多様でランダムな回答が生成されます。

回答の精度を上げるためには、適切なtemperature値を選択することが重要です。一般的には、temperature値が高すぎると、回答が不自然になり、低すぎると回答が繰り返しがちになるため、中間の値を選択することが望ましいです。また、特定のタスクに応じて、最適なtemperature値が異なることもあります。


### top_pを調整する
OpenAIのエンドポイントは生成された回答にランダム性を加えるために、生成プロセス中にtop_pと呼ばれるパラメータを使用します。
具体的には、top_pを小さくすると参照するコンテンツの探索が厳密になり、top_pを大きくするとより多様でランダムな回答が生成されます。

回答の精度を上げるためには、適切なtop-p値を選択することが重要です。一般的には、top-p値が高すぎると、コンテンツの探索が緩くなるため、生成された回答が不自然であったり、誤った回答になる可能性があります。一方、値が低すぎると、回答が非常に制限され、登録したコンテンツを元にした反復的な回答が生成されます。

### 関連コンテンツがない場合は回答させない
`no_contents_no_answer` のパラメータを有効にすると、関連コンテンツが無い場合は、以下のようにnot_foundのエラーを返すようになります。  
不確実な回答をさせたく無い場合に設定してください。
また、 `min_score`を大きく設定すると、関連コンテンツとしての判定が厳しくなりますので合わせて設定ください。  

```json
{
  "errors": [
    {
      "code": "not_found",
      "message": "質問に関連する適切なコンテンツが見つかりませんでした。"
    }
  ],
  "x-rcms-request-id": "23f3ca66-aa8b-4a34-891c-9c1f958a0eab"
}
```
-->

以上のようにKurocoのAPIを利用することで、AIによる回答を簡単に得ることができます。  

AIを効果的に活用するには、AIが必要とする情報を正確に登録し、適切にpromptを設定することが不可欠です。回答の精度を上げるための設定にも注目して、KurocoとAIを利用した機能を実装してみましょう。  

## 関連ドキュメント
- [ベクトルデータ](/ja/docs/management/vector-data/)
- [クイックスタート](/ja/docs/management/ai-quickstart/)
- [AI辞書](/ja/docs/management/ai-dictionary/)
- [AIモデル一覧](/ja/docs/management/ai-models/)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)
- [あいまい検索用のベクトルテンプレートを用意する](/ja/docs/tutorials/how-to-implement-vector-search/)


---

# あいまい検索用のベクトルテンプレートを用意する

> 元ページ: `tutorials/how-to-implement-vector-search` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-implement-vector-search/
> 概要: コンテンツをベクトルデータに変換することで、あいまい検索を実装できます。検索キーワードとベクトルデータ化されたコンテンツとのベクトル間距離を利用することで、関連度の高い順にコンテンツをレスポンスします。

## 概要
コンテンツをベクトルデータに変換することで、あいまい検索を実装できます。  
検索キーワードとベクトルデータ化されたコンテンツとのベクトル間距離を利用することで、関連度の高い順にコンテンツをレスポンスします。

これにより、使用する単語の揺れがある場合の検索や、文章による検索が可能になります。

本ドキュメントではコンテンツに登録した社内文書を、あいまい検索します。

### 学べること
以下の手順でベクトルテンプレートの設定と確認をします。  
- [コンテンツの準備をする](#コンテンツの準備をする)
- [ベクトルテンプレートを設定する](#ベクトルテンプレートを設定する)
- [動作の確認をする](#動作の確認をする)

## コンテンツの準備をする
### AIを有効にする
[AI] -> [ベクトルデータ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e47d56cef62185748d29321b79ba79d.png)

AIの項目を有効にして、[更新する]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e166aac6a92486724a8354f73504e7d4.png)

### コンテンツ定義を追加する
ベクトル検索をする対象となるコンテンツ定義を登録します。  
[コンテンツ定義一覧](/ja/docs/management/content-structure-topics-group/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/22303613bafe005dc86e92cf56be990c.png)

以下の内容で設定をします。  

**全般**

|項目|設定|
|:--|:--|
|名前|社内文書|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0cc31848ee9ca86944b8b271ceb4c25.png)

**項目設定**

|項目|Slug|項目名|項目設定|
|:--|:--|:--|:--|
|ext_1|なし|WYSIWYG|WYSIWYG|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ab3132fe663411dec3d1a0ac224d171.png)

**検索設定**

|項目|設定|
|:--|:--|
|ベクトルデータに変換する|有効にする|
|埋め込みモデル|text-embedding-3-small(OpenAI)|
|キーワードテンプレート(AI/Vector)|デフォルトのまま|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0d572136f7e498addbe1371a469374e.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。 

## ベクトルテンプレートを設定する

### テンプレートの確認
デフォルトでは、以下がベクトルデータへの変換対象となるテンプレートが入力されています。

- topics_id
- slug
- タイトル
- 内容
- カテゴリ
- 全ての拡張項目のテキスト部分

:::info
初期状態に戻したい場合は空で更新することで、自動的にデフォルトテンプレートが入力されます。
:::

:::caution
ファイル項目に保存されたファイル（PDF、Word など）の内容は、ベクトルデータの変換対象に含まれないためRAGで読み込まれません。
ファイルの内容をRAGで参照させるには、カスタム処理などでファイルからテキストを抽出し、テキストエリアやWYSIWYGなどのテキスト項目に保存しなおす必要があります。
:::

### テンプレートの修正

任意の項目をテンプレートから除外したり、関連するメンバー情報をテンプレートに追加したりしたい場合は、テンプレートを修正します。  

本チュートリアルではデフォルトのまま進めます。  

#### リファレンス
利用できる変数は以下の通りです。

|変数名|型|説明|
|:---|:---|:---|
|$details|Object|コンテンツ詳細|
|$ext_config|Object|コンテンツ拡張設定|

Smartyの記述によって出力された文章がベクトルテンプレートとなります。

:::info
修正の例は以下のドキュメントも参照してください。
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/#検索対象文字列テンプレートの修正)
:::


## 動作の確認をする
コンテンツを追加して、Swagger UIから検索結果を確認します。

### コンテンツを追加する

[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e09864c6c8ab391e1195725ef096f607.png)

ここでは例として以下の3コンテンツを追加しました。  

**リモートワークガイドライン**  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b53d8c1ea95d854992ffbe3ea9f093ea.png)

**福利厚生ガイドブック**  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d442635a9c6af986e7c1a5693102002f.png)

**連絡先**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbf70948f9b5c00bc80e8e363f951309.png)

### ベクトルテンプレートを確認する
追加されたコンテンツの編集画面で、[その他] ボタンをクリックして選択肢が表示します。
[ベクトルテンプレート]をクリックすると、出力されたテンプレートを確認することが出来ます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d08505df37efae4cb212603d45206128.png)

:::caution
反映完了まで[ベクトルテンプレート]の選択肢が表示されません。
:::

テンプレート、サマリー、インデックスの確認ができます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fae388f9234dcab0edad77198f89c349.png)

### ベクトル検索用エンドポイントを用意する

[エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)を参考に、ベクトル検索用のエンドポイントを作成します。  

今回はパス・モデルを以下のように設定します。
- パス： vector_search
- カテゴリー: コンテンツ
- モデル：Topics, v1
- オペレーション：list
- topics_group_id：42 ([コンテンツ定義を追加する](#コンテンツ定義を追加する)で採番されたID)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ddde95e949dee04b17b46b06c7660cdb.png)

### Swagger UIで確認する
Swagger UI画面から[ベクトル検索用エンドポイントを用意する]で追加したエンドポイントにリクエストします。  
vector_searchの項目に`在宅勤務`と入力し、Executeをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c0d3f94fd9d19b3fbed9adc7ecd5104.png)

コンテンツには`在宅勤務`の文字は登録されていませんが、関連度の高いリモートワークガイドラインのドキュメントがリストの最初にレスポンスされます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c6b429093b0f9b33394fdd915e459251.png)

:::tip
vector_distanceの項目が検索文字列とのベクトル間距離を表し、小さい順にレスポンスされます。  
:::

## 関連ドキュメント
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [拡張項目設定](/ja/docs/management/extra-information/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)


---

# Kuroco MCP サーバと Amazon Bedrock AgentCore Gateway の連携

> 元ページ: `tutorials/integrate-kuroco-mcp-with-amazon-bedrock-agentcore` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrate-kuroco-mcp-with-amazon-bedrock-agentcore/
> 概要: OAuth 2.0 の client_credentials グラントを使って、Kuroco MCP サーバを Amazon Bedrock AgentCore Gateway に接続する手順を説明します。

このチュートリアルでは、OAuth 2.0 の `client_credentials` 認証を使って、Kuroco MCP サーバを Amazon Bedrock AgentCore Gateway に接続する手順を説明します。

この連携は、大きく次の 3 つのパートで構成されます。

1. Kuroco の OAuth Authorization Server を設定し、`client_credentials` 用のクライアントを登録する。
2. そのクライアントを、Amazon Bedrock AgentCore にアウトバウンドの OAuth クライアントプロバイダーとして登録する。
3. AgentCore Gateway を作成し、Kuroco MCP サーバを MCP ターゲットとして追加する。

最終的なフローは次のとおりです。

```text
クライアントまたはエージェント
    → Amazon Bedrock AgentCore Gateway
    → client_credentials を使った Kuroco OAuth Authorization Server
    → Kuroco MCP サーバ
```

## 1. Kuroco の OAuth Authorization Server を設定する

この連携は、Kuroco に組み込まれた **OAuth Authorization Server** を利用します。OAuth Authorization Server は、Amazon Bedrock AgentCore が Kuroco MCP サーバを呼び出す際に使用するアクセストークンを発行します。

このセクションでは、次の作業を行います。

1. 用途が `API` の OAuth Authorization Server を作成（または既存のものを再利用）する。
2. `client_credentials` グラントに対応したコンフィデンシャルクライアントを登録する。
3. 後で Amazon Bedrock AgentCore に入力する値を収集する。

### 1.1 前提条件

- MCP サーバが有効になっており、かつ API セキュリティが `none` 以外の値に設定されている Kuroco API エンドポイント。

  `client_credentials` グラントは、Kuroco MCP サーバが OAuth を通じて検証するベアラートークンを発行します。

対象 API の MCP 設定から、その API の MCP エンドポイント URL を取得します。URL は次の形式です。

```text
https://{your-site}.g.kuroco.app/rcms-api/{api_id}/mcp
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73c6ce8a01d2b2bfd57f84135d70a557.jpg)

エンドポイントで MCP サーバがまだ有効化されていない場合は、先に MCP サーバを設定してください（エンドポイントの MCP 設定: ツール名、入力スキーマ、ステータス）。

:::note
このチュートリアルでは、**Client API MCP サーバ**（`/rcms-api/{api_id}/mcp`）を使用します。これは用途が `API` の OAuth Authorization Server に紐付いています。管理系の操作を公開したい場合は、用途が `AdminMCP` の OAuth Authorization Server に紐付く **Admin MCP サーバ**（`/direct/rcms_api/admin_mcp/`）を使って、同じ流れで設定できます。設定手順は同様ですが、用途・スコープ・オーディエンスが異なります。
:::

### 1.2 OAuth Authorization Server を作成する

:::note
新規に作成する代わりに、用途が `API` の既存の認可サーバー（Kuroco が **Kuroco MCP API (default)** という名前でデフォルトの認可サーバーを自動作成している場合があります）を再利用できます。再利用する場合は、その **対応するグラントタイプ** に `client_credentials` が含まれていること、および **許可するスコープ** に `api:read`（必要に応じて `api:write`）が含まれていることを確認してください。グラントタイプはクライアントごとに選択されるため、共有する認可サーバーで `client_credentials` を有効にしても、他のグラントを使う既存のクライアントには影響しません。
:::

Kuroco 管理画面で **「外部システム連携」→「OAuth Authorization Server」** を開き、**「＋追加」** をクリックして、次のとおり設定します。

| 項目 | 設定値 |
|---|---|
| 名前 | 任意のラベル（例: `Bedrock AgentCore`）。 |
| 用途 | `API`（`/rcms-api/{api_id}/mcp` で公開されるコンテンツ API を保護します）。**この値は作成後に変更できません。** |
| 対応するグラントタイプ | **client_credentials** を有効にします。（この連携では `authorization_code` / `refresh_token` は不要です。） |
| 許可するスコープ | **api:read** を有効にします（クライアントで書き込み操作を行う場合は **api:write** も有効にします）。 |
| アクセストークン有効期間 | `3600`（秒。デフォルト）。 |
| リフレッシュトークン有効期間 | `2592000`（秒。デフォルト）。 |
| 認可コード有効期間 | `60`（秒。デフォルト）。 |
| ログインページ URL | デフォルト（`https://{your-domain}.g.kuroco-mng.app/management/login/login/`）のままにします。この項目は用途が `API` の認可サーバーでは必須ですが、`client_credentials` フローでは使用されません。 |
| 有効 | **ON** |

**「追加」** をクリックして保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b16317575dc9555ffec291c65650ba0c.png)

保存後、作成した認可サーバーを再度開きます。後で必要になる 2 つの読み取り専用の値が表示されます。

- **発行元 (Issuer) URL**。次の形式です。

  ```text
  https://{your-site}.g.kuroco.app/direct/login/oauth_idp/{id}
  ```

- **メタデータ URL**。次の形式です。

  ```text
  https://{your-site}.g.kuroco.app/.well-known/oauth-authorization-server/direct/login/oauth_idp/{id}
  ```

### 1.3 OAuth クライアントを登録する

認可サーバー一覧で、作成した認可サーバーの行にある **「クライアントを管理」** をクリックし、続いて **「＋追加」** をクリックして、クライアントを次のとおり設定します。

| 項目 | 設定値 |
|---|---|
| クライアント名 | 任意のラベル（例: `Bedrock AgentCore`）。 |
| トークンエンドポイント認証方式 | **client_secret_basic**。このチュートリアルでは `client_secret_basic` を使用しますが、`client_secret_post` も利用できます。Amazon Bedrock AgentCore 側と同じ方式を選択してください。`none` にすることはできません。`client_credentials` にはコンフィデンシャルクライアントが必要です。 |
| 対応するグラントタイプ | **client_credentials** を有効にします。 |
| サービスメンバー | 発行されるトークンが振る舞うメンバーを選択します。Gateway からのすべての MCP 呼び出しはこのメンバーの権限で実行されるため、必要最小限の権限を持つメンバーを選択してください。このメンバーはトークンを生成できる必要があります。この項目は `client_credentials` を選択した場合に必須です。 |
| デフォルト API | このトークンの対象となる、MCP が有効な API を選択します。これによりトークンのオーディエンス（RFC 8707 の resource）が設定されます。**この連携では必須です。** Amazon Bedrock AgentCore は `resource` パラメータを送信しないため、デフォルト API を設定しないと、トークンエンドポイントはリクエストを `invalid_target` で拒否します。 |
| 許可するスコープ | **api:read** を選択します（書き込み操作を行う場合は **api:write** も選択します）。少なくとも 1 つの機能スコープが必要です。 |
| リダイレクト URI | 空欄のままにします。リダイレクト URI は `authorization_code` グラントでのみ必要ですが、この連携では使用しません。 |
| 有効 | **ON** |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fb1608430ced537aef46d1943c27b5bb.png)

**「追加」** をクリックすると、次のようになります。

- **クライアント ID** が自動的に生成されます。
- 認証方式が `none` ではないため、**クライアントシークレット** が生成され、**一度だけ** 表示されます。再表示はできないため、すぐに控えてください（紛失した場合は、クライアント編集画面から再生成できます）。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1589d50358bc30dcf3dca3928fb275d8.png)

### 1.4 Amazon Bedrock AgentCore 用の値を収集する {#14-collect-the-values-for-amazon-bedrock-agentcore}

これで AgentCore の設定に必要なものがそろいました。次の値を収集します。

- **クライアント ID** と **クライアントシークレット**（登録したクライアントから取得）。
- **発行元 (Issuer)**、**認可エンドポイント**、**トークンエンドポイント**。

各エンドポイントを取得するには、セクション 1.2 の **メタデータ URL** を開きます。この URL は OAuth 2.0 Authorization Server Metadata ドキュメント（RFC 8414）を返します。JSON から次の値を取得します。

| メタデータのフィールド | 値の例 |
|---|---|
| `issuer` | `https://{your-site}.g.kuroco.app/direct/login/oauth_idp/{id}` |
| `authorization_endpoint` | `https://{your-site}.g.kuroco.app/direct/login/oauth_idp/{id}/authorize` |
| `token_endpoint` | `https://{your-site}.g.kuroco.app/direct/login/oauth_idp/{id}/token` |

:::note
`client_credentials` は認可エンドポイントを使用しませんが、Amazon Bedrock AgentCore ではこの項目が必須のため、控えておいてください。
:::

## 2. Amazon Bedrock AgentCore で Kuroco OAuth クライアントを設定する {#2-configure-the-kuroco-oauth-client-in-amazon-bedrock-agentcore}

Gateway を作成する前に、[セクション 1.4](#14-collect-the-values-for-amazon-bedrock-agentcore) で収集した値を使って、Kuroco の OAuth Authorization Server を AgentCore Identity にアウトバウンドの OAuth クライアントプロバイダーとして登録します。

Kuroco はメタデータ URL で OAuth 2.0 Authorization Server Metadata ドキュメント（RFC 8414）を公開していますが、AgentCore の自動検出は OpenID Connect のディスカバリドキュメントを想定しており、Kuroco はこのエンドポイントではそれを公開していません。**Manual config** を使用し、各エンドポイントを手動で入力してください。

### 2.1 AgentCore Identity に OAuth クライアントを追加する

AWS コンソールで、次の操作を行います。

1. **Amazon Bedrock AgentCore** を開きます。
2. **Identity** を開きます。
3. アウトバウンド認証のセクションに移動します。
4. 新しい OAuth クライアントを追加します。
5. カスタム OAuth プロバイダーを選択します。
6. **Manual config** を選択します。

プロバイダーを次のとおり設定します。

| 項目 | 設定値 |
|---|---|
| Client authentication method | `Client secret basic`（Kuroco クライアントに設定した **トークンエンドポイント認証方式** と一致させる必要があります。`Client secret post` も利用できます） |
| Issuer | Kuroco のメタデータ URL の `issuer` の値 |
| Authorization endpoint | Kuroco のメタデータ URL の `authorization_endpoint` の値 |
| Token endpoint | Kuroco のメタデータ URL の `token_endpoint` の値 |
| Client ID | Kuroco でクライアントを登録したときに生成された Client ID |
| Client secret | Kuroco でクライアントを登録したときに生成された Client secret |

`Client secret basic` は、AgentCore が HTTP Basic 認証を使って Kuroco のトークンエンドポイントに認証することを意味します。

```http
Authorization: Basic base64(client_id:client_secret)
```

トークンリクエストは `client_credentials` グラントを使用し、Kuroco のトークンエンドポイント（メタデータ URL の `token_endpoint` の値。`https://{your-site}.g.kuroco.app/direct/login/oauth_idp/{id}/token` の形式）に送信されます。

```http
POST /direct/login/oauth_idp/{id}/token
Content-Type: application/x-www-form-urlencoded
Authorization: Basic base64(client_id:client_secret)

grant_type=client_credentials
```

AgentCore でスコープを設定する必要はありません。トークンのスコープは、Kuroco クライアントに設定した **許可するスコープ**（`api:read` / `api:write`）に由来します。トークンリクエストが `scope` パラメータを省略した場合、Kuroco はそのクライアントに設定されたスコープを付与します。

同様に、トークンのオーディエンスも AgentCore では設定しません。オーディエンスは、Kuroco クライアントに設定した **デフォルト API** に由来します。リクエストが `resource` パラメータを送信しない場合、Kuroco はこのデフォルト API を RFC 8707 の resource として使用します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5caf75150619a4934978c5546a0e108e.png)

この時点で、OAuth の設定は完了です。Kuroco の OAuth Authorization Server が `client_credentials` を使って Amazon Bedrock AgentCore に接続されました。

この OAuth クライアントの設定は、対応する Kuroco MCP サーバに接続する必要があるすべての AgentCore Gateway で再利用できます。

## 3. Amazon Bedrock AgentCore Gateway を作成する

AWS コンソールで、次の操作を行います。

1. **Amazon Bedrock AgentCore** を開きます。
2. **Gateways** を開きます。
3. **Create Gateway** を選択します。

作成ウィザードは 4 つのステップで構成されます。

### ステップ 1 — Gateway の詳細を定義する

デフォルト値のまま変更しなくてかまいません。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5dd0cc49e648b445c21fd8d7a301ba67.png)

生成された Gateway 名やその他のデフォルト設定を確認し、**Next** をクリックします。

### ステップ 2 — インバウンド ID を設定する

インバウンド認証は、クライアントが AgentCore Gateway を呼び出す際にどのように認証するかを制御します。

ニーズに応じて認証方式を選択してください。利用できるオプションは次のとおりです。

- IAM 認証
- JWT ベースの認証
- 認証なし（一時的な隔離されたテスト専用）

インバウンド認証は、AgentCore Gateway と Kuroco の間で使用されるアウトバウンドの OAuth 認証とは別のものです。

```text
クライアント → AgentCore Gateway
    インバウンド認証

AgentCore Gateway → Kuroco MCP サーバ
    OAuth client_credentials
```

:::caution
本番環境では、認証ありのインバウンド設定を使用してください。インバウンド認証のない、公開状態でアクセス可能な Gateway を放置しないでください。
:::

インバウンド ID を設定したら、**Next** をクリックします。

### ステップ 3 — ターゲットを追加する

Kuroco MCP サーバを Gateway のターゲットとして追加します。

ターゲットを次のとおり設定します。

| 項目 | 設定値 |
|---|---|
| Target Protocol | `MCP Target` |
| Target type | `MCP Server` |
| MCP endpoint | 追加したい Kuroco MCP サーバのエンドポイント |
| Outbound Auth | `OAuth client` |
| OAuth client | [セクション 2](#2-configure-the-kuroco-oauth-client-in-amazon-bedrock-agentcore) で作成した OAuth クライアントを選択します |

残りの設定はすべてデフォルト値のままでかまいません。

MCP endpoint には、Kuroco MCP サーバの完全な公開 HTTPS エンドポイントを指定します。次の形式です。

```text
https://{your-site}.g.kuroco.app/rcms-api/{api_id}/mcp
```

トークンのオーディエンスと呼び出し先の resource が一致するように、Kuroco クライアントで **デフォルト API** として選択したものと同じ API の MCP エンドポイントを使用してください。

ターゲットを設定したら、**Next** をクリックします。

### ステップ 4 — 確認して作成する

Gateway とターゲットの設定内容を確認し、**Create Gateway** をクリックします。

AgentCore が Gateway を作成し、先ほど設定した OAuth クライアントを使って、ターゲットを Kuroco MCP サーバに接続します。

## 4. Gateway をテストする

Gateway の詳細ページから Gateway URL をコピーします。URL は `/mcp` で終わっているはずです。

インバウンド認証なしで作成した Gateway は、`curl` でテストできます。

```bash
curl -i -X POST 'YOUR_GATEWAY_URL' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
  }'
```

接続に成功すると、レスポンスには Kuroco MCP サーバが公開しているツールが含まれます。

ツールを呼び出すには、`tools/list` が返した正確なツール名と入力スキーマを使用します。

```bash
curl -i -X POST 'YOUR_GATEWAY_URL' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "YOUR_TOOL_NAME",
      "arguments": {}
    }
  }'
```

IAM または JWT のインバウンド認証を使用する Gateway の場合は、Gateway を呼び出す際に対応する認証を付与してください。

これで Gateway を任意の MCP クライアントに接続でき、Kuroco MCP サーバを利用できるようになります。

## 関連ドキュメント

- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) — このチュートリアルの前提となる、Kuroco API エンドポイントで MCP サーバを有効にする方法
- [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/) — Client API MCP サーバと Admin MCP サーバのエンドポイント、認証方式、ツール構造
- [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) — 他の MCP クライアント向けの OAuth Authorization Server の設定（CIMD とクライアントの手動登録）
- [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/) — Kuroco の OAuth Authorization Server とクライアントを登録するもう 1 つの手順。`client_credentials` ではなく `authorization_code` グラントを使用します
- [API セキュリティ](/ja/docs/management/api-security/) — このチュートリアルの前提条件で参照している API セキュリティ設定の詳細


---

# Kuroco の AI 機能ガイド

> 元ページ: `tutorials/kuroco-ai-features-guide` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kuroco-ai-features-guide/
> 概要: Kuroco が提供する AI 機能（MCP 連携、AIエージェント、コンテンツ定義のAI自動処理、RAG・ベクトル検索など）の全体像と、それぞれの詳細ドキュメントへの入り口をまとめたガイドです。

Kuroco は、コンテンツ管理や API に AI を組み込むための複数の機能を提供しています。
このページでは、Kuroco の AI 機能の全体像と、それぞれの詳細ドキュメントへの入り口をまとめています。個々の設定手順は各リンク先のドキュメントを参照してください。

## Kuroco の AI 機能の全体像

Kuroco の AI 機能は、コンテンツの取り込みや AI による処理、ユーザーへの返信など、次の機能で構成されています。表は以降のセクションの順に沿って主な機能をまとめています（最後の「チャネルへの返信」は[機能を組み合わせてできること](#機能を組み合わせてできること)で扱います）。

| 領域 | 主な機能 | できること |
| :--- | :--- | :--- |
| コンテンツ定義のAI自動処理 | AI自動後処理 / AIバリデーション | コンテンツの保存時に、AIによるフィールドの自動生成・加工や、内容の妥当性チェックを実行します。 |
| コンテンツの自動取り込み（AI への入力データ） | メール受信 / クローリング / Slack / LINE / Microsoft Teams | メール・Webページ・チャットメッセージをコンテンツとして自動登録し、AI 処理やベクトル検索の入力データにできます。 |
| AIエージェント | AIエージェント（自律実行）/ トリガーメール | Kuroco 内のデータを利用してタスクを実行させます。メール受信を契機に自律実行することもできます。 |
| MCP 連携 | Client API の MCP / Admin MCP | 公開 API や管理 API を MCP ツールとして LLM クライアントに公開し、AIから呼び出させます。 |
| Claude Code からの開発・管理操作 | Kuroco Skills / Admin MCP | Claude Code から Kuroco の管理操作や開発を行えます。 |
| RAG・ベクトル検索・AIモデル | ベクトルデータ / RAG / OpenAI エンドポイント / AI辞書 / AIモデル一覧 | コンテンツをベクトル化して検索・RAG に利用したり、AI 系エンドポイントで応答を生成します。 |
| チャネルへの返信 | Slack / LINE / テキスト メッセージ(SMS) / X | AI で処理した結果を、トリガーメールアドレス経由で各チャネルからユーザーに返せます。 |

以下、それぞれの領域について概要と関連ドキュメントを説明します。

## コンテンツ定義のAI自動処理

コンテンツ定義の[拡張機能]にある[AI自動処理]タブでは、コンテンツが保存されたタイミングでAIを自動で動かす設定ができます。目的の異なる 2 つの機能があります。

| 機能 | 目的 |
| :--- | :--- |
| **AI自動後処理** | コンテンツ保存後にAIがフィールドを自動加工・生成します。 |
| **AIバリデーション** | コンテンツ保存時にAIが内容の妥当性をチェックします。 |

どちらもプロンプト（AI自動後処理では AI への指示、AIバリデーションでは AI に渡す判定基準）を記述し、実行するタイミングや AI に渡す[入力フィールド]を設定します。実行タイミングの選択肢は機能ごとに異なります。AI自動後処理では、加えて処理結果を書き込む[出力フィールド]や、処理を[モデルを使用]（LLMに直接任せる）と[AIエージェントを使用]のどちらで行うかを設定します。

AIバリデーションには次の動作仕様があります。

- 各ルールは独立して評価され、却下したすべてのルールがそれぞれエラーを返します。
- 通常のバリデーション（必須チェックなど）が通過した後、最後に実行されます。
- **フェイルクローズ**：AIリクエスト自体が失敗した場合は、未検証の内容を通さず保存をブロックします。
- 承認も含め、各判定はアプリケーションログに記録されます。

:::info
設定項目の詳細は[コンテンツ定義の拡張機能 — AI自動処理](/ja/docs/management/content-structure-extensions/#ai自動処理)を参照してください。実装例として、保存時に本文を自動翻訳する手順を[コンテンツ更新時にAIで自動翻訳する](/ja/docs/tutorials/ai-post-processing-translation/)で解説しています。
:::

## コンテンツの自動取り込み（AI への入力データ）

コンテンツ定義には、外部からの入力をコンテンツとして自動登録する機能があります。取り込んだコンテンツは、前述のAI自動後処理・AIバリデーションや、ベクトルデータへの変換（RAG）、AIエージェントの処理対象として活用できます。

いずれもコンテンツ定義編集画面の[全般]にある「データ種別」を選択すると、対応する設定タブが表示されます。

| データ種別 | 取り込む内容 |
| :--- | :--- |
| メール | 設定した受信アドレスへのメールを受信し、コンテンツとして自動登録します。 |
| クローリング | クロールで取得した Web ページのデータ（URL・コンテンツ・言語など）を格納します。 |
| Slack | Slack の受信 webhook イベントと送信 API メッセージを、1 メッセージ 1 レコードで保存します。 |
| LINE | LINE Messaging API から受信した Webhook イベントを、1 メッセージ 1 レコードで保存します。 |
| Microsoft Teams | Microsoft Teams Bot Framework から受信した message activity を、1 メッセージ 1 レコードで保存します。 |

:::info
各データ種別の設定項目は[コンテンツ定義の拡張機能](/ja/docs/management/content-structure-extensions/)の[メール受信](/ja/docs/management/content-structure-extensions/#メール受信)・[クローリング](/ja/docs/management/content-structure-extensions/#クローリング)・[Slack](/ja/docs/management/content-structure-extensions/#slack)・[LINE](/ja/docs/management/content-structure-extensions/#line)・[Microsoft Teams](/ja/docs/management/content-structure-extensions/#microsoft-teams)の各セクションを参照してください。クローラーの設定は[WEBクローラー](/ja/docs/management/spider-list/)、Microsoft Teams 連携の手順は[Microsoft Teams と連携する](/ja/docs/tutorials/microsoft-teams-setup/)を参照してください。
:::

## AIエージェント 

AIエージェントは、Kuroco 内のデータを利用してさまざまなタスクを実行させる機能です。エージェント編集画面で[自律実行]を有効にすると、人手の確認なしにエージェントを起動できます。

エージェントの起動には、**トリガーメールアドレス**を利用できます。`{ai_agent_id}@agent.r-cms.jp` 形式のアドレス（ローカル部はエージェントID または Slug）宛にメールを送信すると、実際のメールとしては送信されず、代わりにエージェントが起動します。受信したメールの件名・本文がエージェントへの指示として渡されます。

実行時のツール操作は、エージェントの権限ポリシー（Admin MCP の読み取り専用設定など）に従います。

また、管理画面では、対応する画面の[AIエージェント]からサイドバーを開き、表示中のページについてエージェントに質問や依頼ができます（AIエージェントアシスト）。

:::caution
- エージェントを起動するには、エージェントのステータスが有効で、かつエージェント編集画面の[自律実行]が有効になっている必要があります。
- エージェントの実行に起因して送信されたメールは、ループ防止のため再度エージェントを起動しません。ただし、エージェントが行った操作をきっかけに別機能から送信される通知メール（例：エージェントが行った承認により送信されるワークフロー通知）は、新しいトリガーとして扱われます。
:::

:::info
- トリガーメールアドレスの仕様（Slug のルールや前提条件を含む）は[トリガーメールアドレス — AIエージェント](/ja/docs/reference/trigger-email-address/#aiエージェント)を参照してください。
- 管理画面のサイドバーの使い方は[AIエージェントアシスト](/ja/docs/management/ai-agent-assist/)を参照してください。
- エージェントから GitHub リポジトリへアクセスするための GitHub Personal Access Token (PAT) の設定は[GitHub](/ja/docs/management/github/)を参照してください。
:::

## MCP 連携

Kuroco は Model Context Protocol (MCP) を実装しており、Claude、ChatGPT、IDE アシスタントなどの LLM クライアントが、HTTP 経由で Kuroco の API を型付きツールとして呼び出せます。用途に応じて 2 種類の MCP サーバがあります。

| MCP サーバ | エンドポイント | 用途 |
| :--- | :--- | :--- |
| Client API の MCP | `/rcms-api/{id}/mcp` | 公開 API エンドポイントをツールとして公開し、LLM のレスポンスを充実させたり、コンテンツを作成・更新させます。 |
| Admin MCP | `/direct/rcms_api/admin_mcp/` | 管理 API（admin_api）を MCP サーバとして公開します。Bearer トークン認証に対応し、無人エージェントやスコープ／読み取り専用のアクセス制御に適しています。 |

Client API の MCP を有効にするには、セキュリティを特権付き静的トークンに設定した API 定義で、MCP サーバーの設定を有効にします。MCP を有効にしたエンドポイントには入力データ定義の設定が必須です。

:::info
- 公開 API を MCP ツールとして公開する手順は[Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)を参照してください。
- クライアント別の設定方法は[MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)を参照してください。OAuth を利用できないクライアントなどでリクエストヘッダーによる認証を使う場合は[認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/)を参照してください。
:::

## Kuroco Skills と管理操作

[Kuroco Skills](https://github.com/diverta/kuroco-skills) は、[Claude Code](https://code.claude.com/docs/ja/overview) をはじめとする AI エージェント向けの Agent Skills パッケージです。Kuroco の API 連携、コンテンツ管理、フロントエンド統合、バッチ処理などに関するベストプラクティスを AI エージェントに提供します。

AI エージェントから管理操作を行う場合は Admin MCP サーバを使用します。MCP 対応クライアントに直接登録でき、Bearer トークンで認証します。無人エージェント、OAuth ベースの認可、スコープ／読み取り専用のアクセス制御に対応しています。

:::info
- インストール方法と基本的な使い方は[Kuroco Skills の使い方](/ja/docs/tutorials/kuroco-skills-overview/)を参照してください。
- 各スキルの詳細と Admin MCP サーバのリファレンスは[Kuroco Skills リファレンス](/ja/docs/reference/kuroco-skills-detail/)を参照してください。
:::

## RAG・ベクトル検索・AIモデル

Kuroco は、コンテンツをベクトルデータに変換して検索・RAG に利用する機能や、AI 系のエンドポイントを提供しています。管理画面の[AI]メニューから設定します。

![Image from Gyazo](https://i.gyazo.com/9f13ade415ed6e27182a828a08122fe1.png)

| 画面 | できること |
| :--- | :--- |
| [AI] -> [クイックスタート] | Kuroco AI API のレスポンスを確認します（RAG の動作確認）。 |
| [AI] -> [ベクトルデータ] | AI の機能の有効化と、コンテンツをベクトル化するバッチ処理のステータスを確認します。 |
| [AI] -> [AI辞書] | 置換や禁止ワードなどの AI辞書の確認・追加・更新を行います。 |
| [AI] -> [AIモデル一覧] | 利用可能な Embedding モデル・Completions モデルと価格・トークン数を確認します。 |

:::info
- RAG の初期設定の手順は[Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)、動作確認は[クイックスタート](/ja/docs/management/ai-quickstart/)、ベクトルデータの設定は[ベクトルデータ](/ja/docs/management/vector-data/)を参照してください。
- チュートリアルとして[AIによる回答を生成する](/ja/docs/tutorials/generating-ai-responses/)、[あいまい検索用のベクトルテンプレートを用意する](/ja/docs/tutorials/how-to-implement-vector-search/)があります。
- 辞書とモデルの設定項目は[AI辞書](/ja/docs/management/ai-dictionary/)、[AIモデル一覧](/ja/docs/management/ai-models/)を参照してください。
- OpenAI モデルの API エンドポイント（`chat` / `rag_search` / `chat_contents_search` など）の一覧は[エンドポイント 設定項目一覧 — AI](/ja/docs/reference/endpoint-settings/#ai)を参照してください。
- Kuroco AI API のリクエスト履歴は[KurocoRAGログ](/ja/docs/management/vector-search-log-list/)で確認できます。
:::

## 機能を組み合わせてできること

Kuroco の AI 機能は組み合わせて利用できます。代表的な例を紹介します。

### 承認ワークフローの承認をAIに実行させる

トリガーメールアドレスは、フォームの[配信先メールアドレス]やカスタム処理のメール送信（`sendmail`）など、メールの送信先を指定できる箇所で利用できます。ここに AIエージェントのトリガーメールアドレスを指定することで、メール送信を契機に AIエージェントを組み込めます。

自律実行を有効にした AIエージェントをトリガーメールアドレス（`{ai_agent_id}@agent.r-cms.jp`）で起動し、承認ワークフローの承認・却下といった管理操作を実行させられます。エージェントが行った承認により送信されるワークフロー通知メールは、新しいトリガーとして扱われるため、通知を起点に次の処理へつなげることもできます。

### 問い合わせ（フォーム）の通知をAIエージェントで処理する

フォームの通知先メールアドレス（[配信先メールアドレス]）には、トリガーメールアドレスを指定できます。ここに AIエージェントのトリガーメールアドレスを設定すると、フォーム送信を契機にエージェントが起動し、送信内容を指示として受け取って対応を実行できます。

:::info
フォームの通知先の設定は[フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)、トリガーメールアドレスを送信先に指定できる箇所は[トリガーメールアドレス](/ja/docs/reference/trigger-email-address/)を参照してください。
:::

### コンテンツ保存時にAIで自動翻訳する

コンテンツ定義の[AI自動後処理]を使うと、日本語で入力した本文を保存したタイミングで、AIが英語に翻訳して別フィールドへ自動入力する、といった処理を実行できます。手順は[コンテンツ更新時にAIで自動翻訳する](/ja/docs/tutorials/ai-post-processing-translation/)で解説しています。

### AIの処理結果をチャネル経由でユーザーに返す

AI で処理した結果は、チャネルのメッセージング機能を通じてユーザーに返せます。メール送信先にチャネルごとのトリガーメールアドレスを指定すると、実際のメールとしては送信されず、対応するチャネルへメッセージが送信されます。

| 送信先 | アドレス形式 |
| :--- | :--- |
| Slack | `{channel}@slack.r-cms.jp` |
| LINE | `{LINE ID}@text.line.r-cms.jp` |
| テキスト メッセージ(SMS) | `{tel}@twilio.r-cms.jp` |
| X（旧Twitter） | `{twitter_id}@tweets.twitter.r-cms.jp` |

各チャネルへの送信には、対象チャネルの連携設定が有効になっている必要があります。

:::info
各チャネルの設定は[Slack](/ja/docs/management/slack/)・[LINE](/ja/docs/management/line/)・[テキスト メッセージ(SMS)](/ja/docs/management/twilio/)・[Twitter](/ja/docs/management/twitter/)、送信先の指定形式は[トリガーメールアドレス](/ja/docs/reference/trigger-email-address/)を参照してください。
:::

## 課金に関する注意

:::caution
Admin MCP が利用する `/direct/rcms_api/admin_mcp/` へのリクエストは、`/direct/` 経由として Kuroco の課金対象となります。AI エージェントが自律的に操作を繰り返す場合、意図せず多数のリクエストが発生する可能性があります。読み取り中心のエージェントには `/readonly` を付与し、公開するモジュールの範囲を必要な分に絞ることを推奨します。

また、Kuroco の費用・利用状況（課金項目「AI処理ユニット」を含む）は[利用状況](/ja/docs/management/usage/)で確認できます。費用の最適化については[Kuroco利用料の最適化](/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/)を参照してください。
:::

## 関連ドキュメント

- [コンテンツ定義の拡張機能](/ja/docs/management/content-structure-extensions/)
- [コンテンツ更新時にAIで自動翻訳する](/ja/docs/tutorials/ai-post-processing-translation/)
- [WEBクローラー](/ja/docs/management/spider-list/)
- [Microsoft Teams と連携する](/ja/docs/tutorials/microsoft-teams-setup/)
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [トリガーメールアドレス](/ja/docs/reference/trigger-email-address/)
- [AIエージェントアシスト](/ja/docs/management/ai-agent-assist/)
- [GitHub](/ja/docs/management/github/)
- [Slack](/ja/docs/management/slack/)
- [LINE](/ja/docs/management/line/)
- [テキスト メッセージ(SMS)](/ja/docs/management/twilio/)
- [Twitter](/ja/docs/management/twitter/)
- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)
- [MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/)
- [認証ヘッダーによる MCP クライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration-authentication-header/)
- [Claude.ai での MCP コネクタの登録方法](/ja/docs/tutorials/claude-ai-mcp-connector-setup/)
- [Kuroco Skills の使い方](/ja/docs/tutorials/kuroco-skills-overview/)
- [Kuroco Skills リファレンス](/ja/docs/reference/kuroco-skills-detail/)
- [クイックスタート](/ja/docs/management/ai-quickstart/)
- [ベクトルデータ](/ja/docs/management/vector-data/)
- [AI辞書](/ja/docs/management/ai-dictionary/)
- [AIモデル一覧](/ja/docs/management/ai-models/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [KurocoRAGログ](/ja/docs/management/vector-search-log-list/)
- [利用状況](/ja/docs/management/usage/)
- [Kuroco利用料の最適化](/ja/docs/tutorials/how-to-optimize-kuroco-usage-costs/)
