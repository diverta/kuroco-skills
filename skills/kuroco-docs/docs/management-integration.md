# Kurocoドキュメント: 管理画面 / 外部サービス連携

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- AIエージェント（`ai-agent`）
- 環境一覧（`ai-environment`）
- AIモデル一覧（`ai-models`）
- クイックスタート（`ai-quickstart`）
- Microsoft Teams（`microsoft-teams`）
- reCAPTCHA（`recaptcha`）
- Slack（`slack`）
- WEBクローラー（`spider-list`）
- テキスト メッセージ(SMS)（`twilio`）
- ベクトルデータ（`vector-data`）


---

# AIエージェント

> 元ページ: `management/ai-agent` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ai-agent/

AIエージェントでは、Kuroco 上で動作する AI エージェントの一覧の確認・追加・更新ができます。エージェントには、利用できるツール・スキル・MCP サーバーなどの「許可する行動」を設定します。

:::caution β提供中
現在、この機能はβ提供中です。エージェントの動作は各セッションにおいて隔離された環境で動作しており学習されたり外部に漏れることはありません。エージェントが実際に動作するロケーションはUSとなっております。データは東京リージョンにあります。β提供期間中はサービス向上や性能向上のために株式会社ディバータのシステム管理者が内容の確認をする場合がございます。
:::

:::note 課金について
AIエージェントの実行は従量課金の対象です。エージェントの実行時間は「AIエージェント処理時間」（コンピューティング）として集計されます。また、Amazon Bedrock 経由で実行するモデルの場合、トークン使用量が「AI処理ユニット」に加算されます。実際の利用量は[利用状況](/ja/docs/management/usage/)画面の日別利用量で確認できます。
:::

## エージェント一覧

### 確認方法

[AI] -> [AIエージェント]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed140e8d8e08836012e897a21dbf0dac.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/efaa2fd342a3476d1223b1c086fb1855.png)

|項目|説明|
|:--|:--|
|有効|エージェントが有効かどうかを示します。|
|名前|エージェントの名前を表示します。クリックするとエージェント編集画面に移動します。|
|モデル|エージェントが使用するモデルを表示します。|
|セッション|クリックするとエージェントのセッション一覧に移動します。|
|トリガーメールアドレス|自律実行が有効なエージェントに、起動用のトリガーメールアドレスを表示します。Slugが設定されている場合はSlug、未設定の場合はエージェントIDがローカル部（@より前）に表示されます。|
|更新日時|エージェントが最後に更新された日時を表示します。|

[追加]をクリックすると、新しいエージェントを作成できます。

## エージェント編集

### 確認方法

[AI] -> [AIエージェント]をクリックし、一覧から対象エージェントの名前をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8776ad3c7cd6ea2c94d6bc1b67308947.png)

### 基本情報

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6cb923a6a7174f3f72cb1ae25094f9a8.png)

|項目|説明|
|:--|:--|
|名前|エージェントの表示名を設定します。（必須）|
|モデル|使用するモデルを選択します。（必須）デフォルトは `claude-sonnet-4-6` です。選択できるモデルは実行環境のハーネス種別によって変わります。|
|システムプロンプト|エージェントの動作を制御するシステムプロンプトを入力します。|

### 実行環境・ステータス

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4258d94c07626029489db048faf15c9.png)

|項目|説明|
|:--|:--|
|環境|エージェントの実行環境を選択します。ネットワークやパッケージの設定を管理できます。[設定]をクリックすると[実行環境](/ja/docs/management/ai-environment/)の編集画面に移動します。|
|ステータス|無効にするとエージェントは利用できなくなります。|
|自律実行|有効にすると、人手の確認なしにエージェントを起動できます。連携メンバー（MCP連携メンバー）のメールアドレスが空の場合、自動的にトリガーメールアドレスに設定され、そのアドレス宛の通知メールがエージェントを起動します。実行時のツール操作はエージェントの権限ポリシー（Admin MCPの読み取り専用設定など）に従います。|
|Slug|自律実行が有効な場合に表示されます。トリガーメールアドレスのローカル部（@より前）に使用する識別子です。半角英数字・ハイフン・アンダースコアが使用できます（数字のみは不可）。大文字・小文字は区別されず、他のエージェントと重複する値は設定できません。未設定の場合はエージェントIDが使用されます。設定した場合も、エージェントID宛のアドレスは引き続き利用できます。|
|トリガーメールアドレス|自律実行が有効な場合に表示されます。このアドレス宛の通知メールがエージェントを起動します。Slugの入力内容に応じて表示が更新されます。|
|メモ|管理用のメモを入力します。|
|Anthropic Agent ID|エージェント保存後、ハーネス側のエージェントが作成されている場合に表示されます。クリックすると、このエージェントに割り当てられたIDを確認できます。|

### エージェントに許可する行動

エージェントが利用できるツールや接続先を、タブごとに設定します。

:::note
[エージェントツール]と[スキル]のタブは、[環境]に Bedrock Managed Harness の実行環境を選択している場合は表示されません。これらは Anthropic Managed Agents の機能で、Bedrock Managed Harness にはモデル・システムプロンプト・MCPツールのみが適用されるためです。
:::

ツールの実行には権限ポリシーを設定できます。

|権限ポリシー|説明|
|:--|:--|
|常に許可|ツールの実行確認をスキップします。|
|常に確認|ツールの実行前に承認を必要とします。|

#### エージェントツール

エージェントが使用できるビルトインツールを選択します。[デフォルト許可ポリシー]に加えて、ツールごとに個別の権限ポリシーを設定できます。

![Image from Gyazo](https://i.gyazo.com/2a1cb5a876fc934dffbc880de75af6a1.png)

|ツール|説明|
|:--|:--|
|bash|コンテナ内でシェルコマンドを実行|
|read|ファイルやディレクトリの内容を読み取り|
|write|ファイルの作成・上書き|
|edit|既存ファイルへの部分編集|
|glob|globパターンに一致するファイルを検索|
|grep|正規表現によるファイル内容の検索|
|web_fetch|URLからコンテンツを取得・抽出|
|web_search|Webで情報を検索|

#### スキル

このエージェントに有効にする Anthropic マネージドスキルを選択します。

|スキル|説明|
|:--|:--|
|xlsx|Excelスプレッドシートの作成・編集|
|docx|Word文書の作成・編集|
|pptx|PowerPointプレゼンテーションの作成・編集|
|pdf|PDF文書の操作・分析|

Kuroco Skills が提供されている場合は「自動追加」として表示され、常にエージェントに含まれます。

#### MCPサーバー (Kuroco API)

Kuroco API の MCP サーバーを選択します。エージェントはこの API を MCP ツールとして利用できます。

|項目|説明|
|:--|:--|
|MCPサーバー (Kuroco API)|接続する Kuroco API を選択します。動的アクセストークン (dynamic_token) のAPIのみ表示されます。保存時に target_domain=API の OAuth IdP とクライアントが自動的にプロビジョニングされます。|
|読み取り専用モード|有効にすると、この MCP サーバー (Kuroco API) の書き込み系ツール（作成・更新・削除など）が AI エージェントから利用できなくなります。|
|MCP許可ポリシー|「常に許可」はMCPツールの確認をスキップします。「常に確認」（デフォルト）は各MCPツール実行前に承認を必要とします。|

:::info
MCP サーバー対応の Kuroco API が設定されていない場合は、[APIでMCPの設定をする]から先にエンドポイントの MCP 設定を行います。設定方法は [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) を参照してください。
:::

#### Admin MCPサーバー

Kuroco管理コントローラー（topics、member等）をMCPツールとして利用します。

|項目|説明|
|:--|:--|
|読み取り専用モード|有効にすると、選択した全モジュールの書き込み系ツール（作成・更新・削除など）が AI エージェントから利用できなくなります。|
|公開モジュール|MCPツールとして利用するモジュールを選択してください。（必須）モジュールごとに利用できるツール数が表示されます。|
|MCP許可ポリシー|「常に許可」はMCPツールの確認をスキップします。「常に確認」（デフォルト）は各MCPツール実行前に承認を必要とします。|

[MCPツール]をクリックすると、公開モジュールごとのツール一覧を確認できます。

Admin MCP サーバーの仕様は [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/#admin-mcp-サーバ) を参照してください。

#### GitHubリポジトリ

サイトの GitHub リポジトリをリソースとしてマウントします。利用するには、[GitHub設定]でリポジトリ連携と PAT を設定します。

### MCP認証

|項目|説明|
|:--|:--|
|MCP認証メンバーID|MCPサーバーへのアクセス時に使用するメンバーIDを設定します。メンバーの閲覧権限がある場合は検索付きの選択欄が表示され、名前・メールアドレス・ログインID・メンバーIDで検索して選択できます。権限がない場合はメンバーIDの直接入力欄が表示されます。|
|MCP Credentialを再生成|MCP Credential のトークンを再生成します。|

:::caution
MCP認証メンバーは、そのエージェント専用のメンバーとして扱われます。他のエージェントで設定済みのメンバーは指定できません。
:::

設定後、[更新する]をクリックして保存します。

## セッション

### 確認方法

エージェント一覧の[セッション]、またはエージェント編集画面右上の[セッション]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c8dce491bc631ac478e58b76f70f7fce.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3f4650ae45745a1e28f4bc3eab3b9742.png)

### セッション一覧の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/24a723ac5df5e701640c5024fee00d8d.png)

|項目|説明|
|:--|:--|
|タイトル|セッションのタイトルを表示します。|
|Anthropic Session ID|セッションのIDを表示します。|
|作成日時|セッションが作成された日時を表示します。|

[新規セッション]をクリックすると、新しいセッションを開始できます。[詳細]をクリックすると、セッションのトランスクリプト画面に移動します。

### セッション表示

セッションのトランスクリプト（やり取りの履歴）を確認し、メッセージを送信できます。

![Image from Gyazo](https://i.gyazo.com/931c440e575900c88ad3574659a3878f.png)

- メッセージ入力欄からエージェントにメッセージを送信できます。
- 権限ポリシーが「常に確認」のツールをエージェントが実行しようとすると、承認待ち（Action Required）となり、[Allow]（許可）または[Deny]（拒否）を選択します。
- [Interrupt]をクリックすると、実行中のエージェントを中断できます。

:::note
セッション表示画面の一部の表記（Allow / Deny / Interrupt / Send など）は英語で表示されます。
:::

## 注意点

- エージェントの削除は[削除する]から行います。削除したエージェントに紐付くセッションもアーカイブされます。

## 関連ドキュメント

- [実行環境](/ja/docs/management/ai-environment/)
- [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/)
- [Model Context Protocol (MCP) と Kuroco の連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)
- [Microsoft Teams と連携する](/ja/docs/tutorials/microsoft-teams-setup/) - AIエージェントを利用した Teams ボットの構築例


---

# 環境一覧

> 元ページ: `management/ai-environment` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ai-environment/

実行環境では、[AIエージェント](/ja/docs/management/ai-agent/)が動作する環境の一覧の確認・追加・更新ができます。ハーネス種別（接続先）、ネットワーク、パッケージなどを設定します。

## 環境一覧

### 確認方法

[AI] -> [AIエージェント]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed140e8d8e08836012e897a21dbf0dac.png)

画面上部のナビゲーションから[環境一覧]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/deb491ae0e536442f2a4bd03beb16e0e.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/be4493f9ee4ba24eb3906aa03104bb96.png)

|項目|説明|
|:--|:--|
|名前|環境の名前を表示します。クリックすると環境編集画面に移動します。|
|ハーネス種別|環境のハーネス種別を表示します。|
|ネットワーク|ネットワーク設定を表示します。|
|ステータス|環境のステータスを表示します。|
|Anthropic ID|環境のIDを表示します。|
|更新日時|環境が最後に更新された日時を表示します。|

[追加]をクリックすると、新しい環境を作成できます。

## 環境編集

### 確認方法

環境一覧から対象環境の名前をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/308380e39fd3835283236ed70214cb5a.png)

### 基本項目

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3988584a3d475050ad87b01d17679c4d.png)

|項目|説明|
|:--|:--|
|名前|環境の名前を設定します。（必須）|
|ハーネス種別|エージェントの接続先を選択します。（必須）|
|メモ|管理用のメモを入力します。|

ハーネス種別は以下から選択します。

|ハーネス種別|説明|
|:--|:--|
|AWS Bedrock AgentCore Managed Harness|AWS Bedrock AgentCore Managed Harness に接続します。AWS リージョンを選択し、Kuroco がエージェントごとに Managed Harness を自動作成します。会話履歴は AWS 側で保持され、MCP は AgentCore Gateway OAuth 経由で接続します。|
|Anthropic Managed Agents|Anthropic Managed Agents API（api.anthropic.com）に接続します。エージェント・セッション・vault・MCP credential を Anthropic 側で保持します。|

### AWS Bedrock AgentCore Managed Harness の設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a910aa1a166fa62da58dc645ff4fcc81.png)

ハーネス種別で[AWS Bedrock AgentCore Managed Harness]を選択した場合に表示されます。

|項目|説明|
|:--|:--|
|AWS リージョン|Runtime が存在する AWS リージョンを選択します。（必須）Asia Pacific (Tokyo) - ap-northeast-1 / US East (N. Virginia) - us-east-1 / US West (Oregon) - us-west-2 / Europe (Frankfurt) - eu-central-1 / Asia Pacific (Sydney) - ap-southeast-2 から選択できます。|
|実行ロールARN|未入力の場合は OEM 設定の実行ロールを使用します。|

:::caution
ハーネス作成後は AWS リージョンを変更できません。
:::

### Anthropic Managed Agents の設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eac622115935a57eb39957d99d18d91.png)

ハーネス種別で[Anthropic Managed Agents]を選択した場合に表示されます。

|項目|説明|
|:--|:--|
|Anthropic APIキー|この環境の Anthropic Managed Agents 用 API キー（`sk-ant-...`）を設定します。（必須）環境ごとに保存されます。保存済みのキーを変更しない場合は空欄のままにします。|
|ネットワーク|「制限なし」（完全な外向きネットワークアクセス。安全ブロックリストを除く）または「制限あり」（許可ホストのみにアクセスを制限）を選択します。（必須）|
|パッケージ|エージェント環境にインストールするパッケージを、パッケージマネージャーごとに1行で入力します。形式: `manager:pkg1,pkg2`（例: `pip:pandas,numpy` / `npm:express` / `apt:ffmpeg`）|

ネットワークで「制限あり」を選択した場合は、制限ネットワーク設定を行います。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d212ab7cdf18ccefb9d5379105d90a22.png)

|項目|説明|
|:--|:--|
|許可ホスト|アクセスを許可するドメインを1行に1つ入力します。HTTPSのみ。（例: api.example.com）|
|MCPサーバーを許可|エージェントに設定されたMCPサーバーエンドポイントは常にアクセス可能です（常にON）。|
|パッケージマネージャーを許可|公開パッケージレジストリ（PyPI、npm等）へのアクセスを許可します。|

設定後、[更新する]をクリックして保存します。

## 関連ドキュメント

- [AIエージェント](/ja/docs/management/ai-agent/)


---

# AIモデル一覧

> 元ページ: `management/ai-models` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ai-models/

AIモデル一覧ではEmbedding modelsとCompletions modelsのそれぞれで、利用可能なモデルとその参考単価が確認できます。

## AIの確認方法
[AI] -> [AIモデル一覧]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed2cb6db8fa8ffa3ebba371bb667b26e.png)

## AIモデル一覧の項目説明
### Embedding models

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8895931540e31ed2cd80fee615463155.png)

|項目|説明|
|:--|:--|
|Model key|モデルのキーを表示します。|
|名前|モデルの名前を表示します。|
|価格/1,000 文字 | 1,000文字あたりの料金を表示します。料金は日本円とユニット数の両方で示されます。|
|最大トークン数(入力)| モデルが処理可能な最大トークン数（入力側）を表示します。|
|メモ| モデルに関する追加情報や特徴を記載します（例：利用開始時期、次元数、制限事項など）。|
|URL|モデルの公式ドキュメントや利用ガイドへのリンクを表示します。|       

### Completions models

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3ac19d59d8c3fe5ede5a648ddd360303.png)

|項目|説明|
|:--|:--|
|Model key|モデルのキーを表示します。|
|名前|モデルの名前を表示します。|
|価格/1,000 文字(入力)| 1,000文字あたりの入力コストを表示します。料金は日本円とユニット数の両方で示されます。|
|価格/1,000 文字(出力)| 1,000文字あたりの出力コストを表示します。料金は日本円とユニット数の両方で示されます。|
|最大トークン数(入力)| モデルが処理可能な最大入力トークン数を表示します。|
| 最大トークン数(出力)| モデルが生成可能な最大出力トークン数を表示します。|
|メモ|モデルに関する追加情報や特徴を記載します（例：モデルの特性や制限事項など）。|
|URL|モデルの公式ドキュメントや利用ガイドへのリンクを表示します。|

## 関連ドキュメント
- [クイックスタート](/ja/docs/management/ai-quickstart/)
- [ベクトルデータ](/ja/docs/management/vector-data/)
- [AI辞書](/ja/docs/management/ai-dictionary/)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)
- [AIによる回答を生成する](/ja/docs/tutorials/generating-ai-responses/)
- [どのようなときに従量課金として計上されますか](/ja/docs/about/how-much-does-kuroco-cost/)


---

# クイックスタート

> 元ページ: `management/ai-quickstart` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ai-quickstart/

クイックスタートではKuroco AI APIのレスポンスが確認できます。
 
## クイックスタートの確認方法
[AI] -> [クイックスタート]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4f04f9ce357ad7785693f02653dc9987.png)

## Kuroco RAG クイックスタート
### コンテンツを選ぶ
コンテンツ定義の検索設定で[ベクトルデータに変換する]が有効になったコンテンツ定義と、その埋め込みモデル、ベクトル化されたコンテンツ数が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d6bee221552b56128af9fe0362008a4.png)

### カスタムAPIを選ぶ
セキュリティを静的アクセストークンに設定したAPIに設定された以下のエンドポイントが表示されます。
- OpenAI::chat_contents_search
- OpenAI::rag_search

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5326a4b70ccaf93f1c872893e0f7c783.png)

### 質問をする
質問の内容を入力して[送信する]をクリックすると、選択したエンドポイントにリクエストを送信します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8e54ed23cd435bf82963881411cb684.png)

### 完了！レスポンスを確認しましょう
エンドポイントからのレスポンスを確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d83c585b23752e1f90f2cdf9e3809e21.png)

## 関連ドキュメント
- [AIによる回答を生成する](/ja/docs/tutorials/generating-ai-responses)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)


---

# Microsoft Teams

> 元ページ: `management/microsoft-teams` ｜ 公式ページ: https://kuroco.app/ja/docs/management/microsoft-teams/

Microsoft Teams設定では、KurocoをMicrosoft TeamsのBotと連携するための設定を行います。設定した内容は、TeamsのチャットでBotにメッセージを送るとKurocoが受信して処理する仕組みで利用します。

## Microsoft Teamsの確認方法
[チャネル] -> [メッセージング] -> [Microsoft Teams]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cc93764fc7af50dbc25f750189711c3c.png)

## Microsoft Teamsの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/59d0f2162c927596dcf727893f0596d9.png)

| 項目 | 説明 |
| :--- | :--- |
| 有効にする | Microsoft Teams連携を有効にする場合はトグルをONにします。 |
| Microsoft App ID | Azureで登録したアプリケーションの「アプリケーション（クライアント）ID」を入力します。 |
| App Password（クライアントシークレット） | Azureで作成したクライアントシークレットの値を入力します。 |
| アプリの種類 | アプリの種類を選択します（例: `SingleTenant`）。 |
| テナントID | Azureの「ディレクトリ（テナント）ID」を入力します。 |
| Messaging endpoint URL | 設定を保存すると表示される、読み取り専用のURLです。このURLをAzure BotのMessaging endpointに設定することで、TeamsからのメッセージがKurocoに届くようになります。<br/>`https://{your-site}.g.kuroco.app/direct/topics/teams/` |

「マニフェスト設定」セクションでは、Teamsアプリパッケージ用のマニフェストに反映される内容を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/85e605e8d11721d14a212af452dc1835.png)

| 項目 | 説明 |
| :--- | :--- |
| ボット名 | Teamsに表示されるBot名を入力します（例: `KurocoBot`）。 |
| ボットの説明 | Botの説明を入力します（例: `A chat bot powered by Kuroco`）。 |

[更新する]をクリックすると、入力した内容を反映します。

## テスト送信

設定画面の下部にある「テスト」セクションでは、保存済みの設定を使って、実際にTeamsへメッセージを送信し、連携が正しく設定されているかを確認できます。

:::caution
テスト送信すると、指定した会話に実際にメッセージが送信されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f4e74f3eca23cf25ddce31f230bef17e.png)

| 項目 | 説明 |
| :--- | :--- |
| Teams serviceUrl | 送信先のTeams serviceUrlを入力します。 |
| Teams 会話ID | 送信先のTeams会話ID（conversationId）を入力します。 |
| メッセージ | 送信するテキストを入力します。 |
| テストする | [テストする]をクリックすると、入力したメッセージをTeamsに送信します。 |

:::info
テスト送信に必要な`serviceUrl`と会話ID（`conversationId`）は、一度Botとメッセージのやり取りをした後、Teamsメッセージ履歴を保存するコンテンツ定義のレコードから確認できます。取得手順は[Microsoft Teams と連携する](/ja/docs/tutorials/microsoft-teams-setup/)を参照してください。
:::

## manifest.json

「manifest.json」セクションの[manifest.jsonをダウンロード]をクリックすると、Teamsアプリパッケージ用のmanifest.jsonをダウンロードできます。ダウンロードしたmanifest.jsonとアイコン画像をまとめたZIPファイルを、Teamsにアプリとしてインストールします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee85ff96faefab195950653d04140134.png)

## 関連ドキュメント
- [Microsoft Teams と連携する](/ja/docs/tutorials/microsoft-teams-setup/)


---

# reCAPTCHA

> 元ページ: `management/recaptcha` ｜ 公式ページ: https://kuroco.app/ja/docs/management/recaptcha/

ここではreCAPTCHAを利用する為のサイトキーとシークレットキーの入力ができます。

## reCAPTCHAの確認方法
[外部システム連携] -> [reCAPTCHA]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea716e1a7122aa897e7d901e969b867e.png)

## reCAPTCHAの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff9e2293455023898cdcbb3c924ed47d.png)

|項目   |説明  |
| :--- | :--- |
|reCAPTCHA site key|reCAPTCHAで取得したサイトキーの値を入力します。|
|reCAPTCHA secret key|reCAPTCHAで取得したシークレットキーの値を入力します。|
|更新する|クリックすると入力した内容を反映します。|

## 関連ドキュメント
- [reCAPTCHAを利用したフォームを作成する](/ja/docs/tutorials/using-recaptcha/)
- [reCAPTCHAを利用したパスワードリマインダーを作成する](/ja/docs/tutorials/using-recaptcha-for-password-reminders/)


---

# Slack

> 元ページ: `management/slack` ｜ 公式ページ: https://kuroco.app/ja/docs/management/slack/

SlackではSlackアプリと連携するためのBot User OAuth Tokenの入力ができます。

## Slackの確認方法
[チャネル] -> [メッセージング] -> [Slack]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/568e5421e71f00b08fa282a6b021b695.png)

## Slackの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/177d6c1ce28f91f42f471bafa7341e58.png)

|項目  |説明  |
| :--- | :--- |
|Slack|「有効にする」にチェックを入れて更新すると、Slackとの連携が有効になります。|
|Bot User OAuth Token|SlackAPIで取得した「Bot User OAuth Token」を入力します。取得手順は[SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)を参照してください。|
|更新する|クリックすると入力した内容を反映します。|

## テスト送信

Slack連携が有効で、かつBot User OAuth Tokenが設定されている場合、テスト送信フォームが表示されます。保存済みの設定を使って、実際にSlackへメッセージを送信し、連携が正しく設定されているかを確認できます。

:::caution
テスト送信すると、指定したチャンネルに実際にメッセージが送信されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/28df4c7f4cf0bae423d9cc1caad9ad21.png)

| 項目 | 説明 |
| :--- | :--- |
| チャネル | 送信先のチャンネルを入力します。チャンネルID、または「#チャンネル名」の形式で指定します（例: `#general`）。 |
| メッセージ | 送信するテキストを入力します。 |
| テストする | [テストする]をクリックすると、入力したメッセージをSlackに送信します。送信に成功すると「送信しました。」、失敗すると「メッセージの送信に失敗しました。」と表示されます。 |

## 関連ドキュメント
- [SlackアプリのBot User OAuth Tokenを取得してKurocoに設定する](/ja/docs/tutorials/create-slack-app-and-get-bot-token/)
- [Slackで定期的に確認をサポートするbotアプリ「KurocoWorkflow」のインストールと利用方法](/ja/docs/tutorials/workflow-bot/)
- [お問い合わせの受信通知をSlackで送信する](/ja/docs/tutorials/send-slack-notification-after-a-form-has-been-submitted/)


---

# WEBクローラー

> 元ページ: `management/spider-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/spider-list/

WEBクローラーでは作成したWEBクローラーの一覧の確認・追加・更新ができます。

## WEBクローラー一覧
### 確認方法
[チャネル] -> [WEB] -> [WEBクローラー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee73ffbcb6617fc401526124a65d31ba.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/eea7cd357483500d2fc9e66a7a091879.png)

|項目|説明|
|:--|:--|
|有効       | WEBクローラーが有効かどうかを示します。|
|タイトル   | WEBクローラーのタイトルを表示します。|
|クロール対象| クロールする対象を表示します。|
|履歴       | クリックするとクロールの履歴を確認できます。|
|更新日時   | WEBクローラーが最後に更新された日時を表示します。|

## WEBクローラー編集
### 確認方法
[チャネル] -> [WEB] -> [WEBクローラー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee73ffbcb6617fc401526124a65d31ba.png)

WEBクローラー一覧ページから編集をしたいWEBクローラーの[タイトル]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/86b3e72178f900aaa401938c0b44a1ae.png)

#### 基本設定

<a><img src="https://t.gyazo.com/teams/diverta/f754acc8027eb04604968ae2050c9bea.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/3714802640b8d0ebb1abeafc07c37b33.png" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目|説明|
|:--|:--|
|タイトル|WEBクローラーのタイトルを設定します。|
|ステータス|WEBクローラーの有効状態を切り替えます。|
|メモ|メモを記入します。|
|連携先コンテンツ定義|このクローラーに紐付いているコンテンツ定義の一覧を表示します（既存のWEBクローラーの編集時のみ表示されます）。紐付けはコンテンツ定義の編集画面の「連携クローラー設定」で行います。|
|クロール対象|クロールの対象を選択します。現在サポートされている対象は以下です。<ul><li>WEBページをクロール</li><li>Kuroco RAGのS3フォルダをクロール</li><li>指定したS3フォルダをクロール</li></ul>|
|S3バケット内の対象ディレクトリ|クロール対象がS3フォルダの場合に表示されます。S3バケット内の対象ディレクトリを入力します。|
|クロール数制限|クロール数の制限を設定します。0を指定すると無制限になります。|
|予定|クロールのスケジュール実行を設定します。「毎日」を有効にすると、指定した時刻にクロールが自動で実行されます。時刻を指定しない場合は`03:00`が設定されます。|
|テキストデータ収集|テキストデータの収集を有効にする場合はオンにします。クロール対象が「WEBページをクロール」の場合に表示されます。|
|ファイル収集（PDFやOfficeファイル）|PDF・Officeファイル（.pdf/.xlsx/.xls/.docx/.pptx）の収集を有効にする場合はオンにします。クロール対象が「WEBページをクロール」の場合に表示されます。|
|画像収集する|画像収集する場合は有効にします。|
|強制更新|強制更新する場合は有効にします。|

#### WEBページのクロール設定

クロール対象が「WEBページをクロール」の場合に表示されます。

##### 全般

<a><img src="https://t.gyazo.com/teams/diverta/3c7c1000897c13d40075e826570b2bab.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/d697499d03b51595cabe764b45616d7e.png" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目|説明|
|:--|:--|
|開始URL|クロールを開始するURLを入力します。改行区切りで複数入力できます。|
|許可されているURL|クロールを許可するURLを入力します。改行区切りで複数入力できます。|
|サイトマップURL|サイトマップのURLを入力します。|
|拒否されるURL|クロールの拒否をするURLを入力します。改行区切りで複数入力できます。|
|許可される次ページURL|二次リンクの追跡で許可するURLを入力します。改行区切りで複数入力できます。|
|拒否される次ページURL|二次リンクの追跡で拒否するURLを入力します。改行区切りで複数入力できます。|
|許可される言語|複数の言語がある場合、許可する言語を入力します。|
|リンクの追跡|HTMLのリンクをたどってクロールする場合は有効にします。|
|二次リンクの追跡|許可されているURLからの次のリンク先までたどる場合は有効にします。|

##### データ変換・インポート設定

このセクションはHTMLのクロールに関する設定です。管理画面では「HTML」バッジ付きの折りたたみセクションとして表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/19a8f66e740334c579c16f1df7af9aa5.png)

|項目|説明|
|:--|:--|
|メインコンテンツ識別用CSSセレクター|メインコンテンツとして識別するCSSセレクターを入力します。|
|カテゴリ識別用CSSセレクター|カテゴリを識別するためのCSSセレクターを入力します。|
|タイトルタグから除去する文字列|タイトルタグから除去する文字列を入力します。|
|メインコンテンツから除去するCSSセレクター|メインコンテンツから除去するCSSセレクターを入力します。|

### クロールデータの保存に必要なコンテンツ定義
クロールした結果をコンテンツに保存するには以下のコンテンツ定義を持っている必要があります。

|項目名(任意)|繰り返し|項目設定|Slug|注釈(任意)|
|:--|:--|:--|:--|:--|
| 日付                          | |日付<br/> 投稿時間と秒も設定する (hh:mm:ss):有効|ymd|更新された日付がセットされます。|
| Contents                      |1|HTML<br/>全てのタグを許可する:有効             |data|マークダウン形式に変換されたコンテンツが格納されます。|
| URL                           |1| テキスト         | url                  ||
| ハッシュ値                    |1| テキスト         | etag                 |コンテンツの更新状況のチェックに利用します。|
| 言語                          |1| テキスト         | lang                 ||
| メインコンテンツのCSSセレクター |1| テキスト         | selector             |ページ内の抽出するコンテンツを指定しています。|
| レスポンスステータス           |1| 数値             | response_status      ||
| コンテンツサイズ               |1| 数値             | content-length       ||
| コンテンツタイプ               |1| テキスト         | content-type         ||
| 手動調整フラグ                 |1| 単一選択<br/>0:無効:デフォルト<br/>0:有効| manual_override_flag |有効にしていると、クローラーで上書きされません。|
| domain                        |1| テキスト         | domain               ||
| description                   |1| テキスト         | description          ||
| icon_url                      |1| テキスト         | icon_url             ||
| ogp_image_url                 |1| テキスト         | ogp_image_url        ||
| 画像                          |20| 以下3項目のグループ化   | images            ||
| - 画像URL                     | |ファイル（ファイルマネージャーから）|image_url||
| - 画像src                     | | テキスト         | image_src            ||
| - altタグ                     | | テキスト       | alt                  ||
| last-modified                 |1 | 日付フォーマット<br/>時間(hh:mm)も設定する:有効 | last-modified        ||

## クロールを実行 履歴
### 確認方法
[チャネル] -> [WEB] -> [WEBクローラー]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee73ffbcb6617fc401526124a65d31ba.png)

WEBクローラー一覧ページから編集をしたいWEBクローラーの[履歴]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/73ebb0a1a7f07aa0f90cb379ddb95804.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8948ec751b534b21b7da24b00f363e89.png)

|項目|説明|
|:--|:--|
| ステータス      | 現在のクロールの状態を表示します。|
| クロール対象    | クロールする対象を表示します。|
| コンテンツ      | クロールしたページが登録されるコンテンツ定義名を表示します。|
| 開始URL        | クロールが開始されるURLを表示します。|
| 開始日時       | クロールの実行が開始された日時を表示します。|
| 終了日時       | クロールが終了した日時を表示します。|
| 処理時間       | クロールにかかった処理時間を表示します。|
| 終了理由       | クロールが終了した理由を表示します。|
| クロール数     | クロール中に処理されたページ数を表示します。|
| ログ           | クリックするとクロールに関するログを確認できます。|
| 再実行         | クリックするとクロールを再実行します。|

## 関連ドキュメント
- [ベクトルデータ](/ja/docs/management/vector-data/)
- [KurocoRAGログ](/ja/docs/management/vector-search-log-list/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)
- [あいまい検索用のベクトルテンプレートを用意する](/ja/docs/tutorials/how-to-implement-vector-search/)


---

# テキスト メッセージ(SMS)

> 元ページ: `management/twilio` ｜ 公式ページ: https://kuroco.app/ja/docs/management/twilio/

テキストメッセージ（SMS）設定ではTwilioとの接続を設定できます。  
 
## テキスト メッセージ(SMS)設定の確認方法
[チャネル] -> [メッセージング] -> [テキスト メッセージ(SMS)]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a045602f9263d0d3684fbe5138e7a6fd.png)

## テキスト メッセージ(SMS)設定の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/115c9b46ddb20ed0917a3eedd20e1444.png)

|項目   |説明  |
| :--- | :--- |
|テキストメッセージ(SMS)|テキストメッセージ(SMS)機能を有効にするかどうかを指定します。|
|Account SID|Twilio のAccount SIDを入力します。|
|Account token|Twilio のAccount tokenを入力します。|
|Twilio で取得した電話番号|Twilioで取得した電話番号を入力します。|
|更新する|[更新する]をクリックすると設定を反映します。|

## テスト送信

テキストメッセージ(SMS)機能が有効で、かつAccount SIDとTwilioで取得した電話番号が設定されている場合、テスト送信フォームが表示されます。保存済みの設定を使って、実際にSMSを送信し、連携が正しく設定されているかを確認できます。

:::caution
テスト送信すると、指定した電話番号に実際にSMSが送信されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/945ca73313327739947bcda0b9fa104e.png)

| 項目 | 説明 |
| :--- | :--- |
| 電話番号 | 送信先の電話番号を入力します（例: `09012345678`）。 |
| メッセージ | 送信するテキストを入力します。 |
| テストする | [テストする]をクリックすると、入力したメッセージをSMSとして送信します。送信に成功すると「送信しました。」、失敗すると「メッセージの送信に失敗しました。」と表示されます。 |

## 利用サンプル

テキストメッセージ(SMS)設置後、バッチ処理やカスタム処理内で下記の様に記述するとSMSメッセージが送信されます。

```php
{sendmail var=result to="(電話番号)@twilio.r-cms.jp" subject="Test" contents="This is Test"}
```

メッセージテンプレートは[オペレーション] -> [メッセージひな形] の `Twilio(SMS)` です。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6f378252f23126caec69ba9992fbf81.png)

## 関連ドキュメント
- [Twilioと連携してSMSを送信する](/ja/docs/tutorials/how-to-connect-to-twillio/)


---

# ベクトルデータ

> 元ページ: `management/vector-data` ｜ 公式ページ: https://kuroco.app/ja/docs/management/vector-data/

ベクトルデータではAIの機能の有効化と、コンテンツをベクトル化するバッチ処理のステータスを確認できます。
 
## ベクトルデータの確認方法
[AI] -> [ベクトルデータ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e47d56cef62185748d29321b79ba79d.png)

## ベクトルデータの項目説明
### ベクトルデータ

![Image from Gyazo](https://t.gyazo.com/teams/diverta/91464121a8ce489d6ae813950a1c10cf.png)

|項目   |説明  |
| :--- | :--- |
|AI|有効にするにチェックを入れるとAIによる回答を生成するAPIが利用できるようになります。|
|非公開コンテンツも送信する|AIに非公開コンテンツの利用も許可する場合はチェックを入れます。|
|API key|独自のAPIキーをセットすることもできます。セットされていない場合は、KurocoのAPIキーが利用されます。設定済みの場合は、[削除する]にチェックを入れて更新すると削除できます。|
|更新する|[更新する]をクリックすると設定を反映します。|

### バッチ処理

[ベクトルデータに変換する]が有効になったコンテンツ定義がある場合に、ベクトルデータ化のバッチ処理結果が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2644ed7a97d2761fdfae20147dd188d9.png)

|項目   |説明  |
| :--- | :--- |
|埋め込みモデル|利用した埋め込みモデルを表示します。|
|ステータス|バッチ処理のステータスを表示します。|
|モジュールタイプ|ベクトルデータ化したモジュールを表示します。|
|言語|ベクトルデータ化したコンテンツの言語を表示します。|
|文字数|ベクトルデータ化したコンテンツの文字数を表示します。|
|チャンク|ベクトルデータ化したコンテンツの件数を表示します。リンクをクリックすると詳細の確認ができます。|
|更新する|表の左端にチェックボックスにチェックを入れてクリックすると、ベクトルデータ化のバッチ処理を再実行します。|

### ベクトルデータ 一覧

バッチ処理の表で[チャンク]のリンクをクリックすると、ベクトルデータ化されたコンテンツの一覧が確認できます。

![Image from Gyazo](https://i.gyazo.com/17c7c18b7a73739f43ead265c6dc41ff.png)

キーワードと埋め込みモデルで検索できます。キーワードを入力して[検索する]をクリックすると、ベクトル検索によって類似するコンテンツが表示されます。

|項目   |説明  |
| :--- | :--- |
|タイトル|コンテンツのタイトルを表示します。リンクをクリックするとコンテンツ編集画面へ遷移します。|
|モジュールID|ベクトルデータ化したコンテンツのIDを表示します。|
|モジュールタイプ|ベクトルデータ化したモジュールを表示します。|
|言語|ベクトルデータ化したコンテンツの言語を表示します。|
|Slug|コンテンツのSlugを表示します。|
|埋め込みモデル|利用した埋め込みモデルを表示します。|
|文字数|ベクトルデータ化したコンテンツの文字数を表示します。|
|インデックス|チャンクのインデックスを表示します。|
|ベクトル距離|キーワード検索を行った場合に、検索キーワードとのベクトル距離を表示します。|
|ステータス|バッチ処理のステータスを表示します。|
|更新する|表の左端のチェックボックスにチェックを入れて[更新する]をクリックすると、選択したベクトルデータのバッチ処理を再実行します。|

## 関連ドキュメント
- [AIによる回答を生成する](/ja/docs/tutorials/generating-ai-responses)
- [Kuroco RAGの設定方法](/ja/docs/tutorials/setting-up-kurocorag/)
