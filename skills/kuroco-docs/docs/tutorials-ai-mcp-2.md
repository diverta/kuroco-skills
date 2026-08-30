# Kurocoドキュメント: チュートリアル / AI・MCP（2/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- Kuroco Skills の使い方（`kuroco-skills-overview`）
- OpenAI Playground での MCP コネクタの登録方法（`openai-playground-mcp-setup`）
- Kuroco RAGの設定方法（`setting-up-kurocorag`）


---

# Kuroco Skills の使い方

> 元ページ: `tutorials/kuroco-skills-overview` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/kuroco-skills-overview/
> 概要: AI エージェントを使った Kuroco 開発を効率化する Kuroco Skills のインストール方法と基本的な使い方を解説します。

[Kuroco Skills](https://github.com/diverta/kuroco-skills) は、Kuroco 開発を支援する Agent Skills パッケージです。
Kuroco の API 連携、コンテンツ管理、フロントエンド統合、バッチ処理などに関するベストプラクティスを AI エージェントに提供し、Kuroco 開発の生産性を向上させます。

Agent Skills は `SKILL.md` を中心としたファイルベースの標準仕様で、[Claude Code](https://code.claude.com/docs/ja/overview) をはじめ複数の AI エージェントで利用できます。エージェントは起動時に各スキルの `name` と `description` だけを読み込み、関連する依頼が来たときに本文を読み込みます（プログレッシブディスクロージャー）。そのため、インストールしただけではコンテキストをほとんど消費しません。

## Kuroco AI アーキテクチャ

Kuroco は AI 連携のために以下のインターフェースを提供しています。

| コンポーネント | 種類 | 説明 |
|--------------|------|------|
| 管理画面 | Web UI | 管理者向けの Kuroco 管理画面 |
| Admin API | REST API | API 経由の管理操作（`/direct/rcms_api/admin_api/`） |
| Admin MCP | MCP サーバ | Admin API の MCP サーバ（`/direct/rcms_api/admin_mcp/`）、Bearer トークン認証 |
| Client API | REST API | フロントエンドアプリ向けの公開 API（`/rcms-api/{id}/`） |
| Client API | MCP サーバ | Client API の MCP サーバ (`/rcms-api/{id}/mcp`) |
| Client CLI | CLI ツール | Client API のラッパー CLI（`kuroco-client`） |

AI エージェントから管理操作を行う場合は、**Admin MCP** を使用してください。MCP 対応クライアント（Claude Code、Claude Desktop など）に直接登録でき、OAuth によるスコープ／読み取り専用のアクセス制御を利用できます。

Client CLI は、独立して使用可能なスタンドアロンのコマンドラインツールです。

## Kuroco Skills とは

Kuroco Skills をインストールすると、AI エージェントが Kuroco に関する質問に対して、正確で具体的なコード例やベストプラクティスを提示できるようになります。
以下の 11 個のスキルが含まれています。

| スキル | 説明 |
|--------|------|
| **kuroco-docs** | Kuroco 公式ドキュメントの検索・参照 |
| **kuroco-app-builder** | アプリ・サイトをゼロから構築するワークフロー（モックファースト → コンテンツ定義 → API → 実データ接続 → デプロイ） |
| **kuroco-api-content** | API 設計・認証（Cookie / 動的・静的アクセストークン）、CORS、コンテンツ CRUD、フィルタークエリ |
| **kuroco-frontend-integration** | Vite / Nuxt.js / Next.js 統合、SPA/SSG/SSR、認証実装、KurocoFront へのデプロイ |
| **kuroco-server-processing** | Smarty プラグイン・構文リファレンス（210 プラグイン）、バッチ処理、Webhook、トリガー、外部システム連携方式の設計（直接呼び出し / プロキシ / 取り込み、シークレット・トークン管理） |
| **kuroco-admin-mcp** | Admin MCP（管理 MCP サーバ）への接続設定、OAuth / CIMD 認証、スコープ、ツール利用 |
| **kuroco-content-structure** | コンテンツ構造の設計判断（コンテンツ定義の分割、JSON 項目によるフィールド圧縮、マスタデータの表現、分類の持ち方、`ext_slug` の命名方針）と、MCP ツールによるコンテンツ定義（TopicsGroup）の作成・フィールドタイプリファレンス |
| **kuroco-auth-design** | 会員認証・権限の設計判断（会員グループ、登録フロー、アクセス制限のスコープ、パスワードポリシー、エンタープライズ SSO / SCIM 連携） |
| **kuroco-api-performance-review** | API パフォーマンス・利用料の調査（API 解析、キャッシュ設定レビュー、改善提案） |
| **kuroco-security-audit** | セキュリティ設定の読み取り専用診断（API セキュリティ、CORS、IP 制限、権限、トークン） |
| **kuroco-spec-writer** | 実設定からの仕様書生成（読み取り専用）。項目表・ER 図・API 一覧などを Markdown + Mermaid で出力 |

各スキルの詳細は「[Kuroco Skills リファレンス](/ja/docs/reference/kuroco-skills-detail/)」を参照してください。

## 事前準備: Claude Code のインストール

Claude Code で Kuroco Skills を使用する場合は、[Claude Code](https://code.claude.com/docs/ja/overview) をインストールします。Codex や claude.ai で使用する場合、この手順は不要です。

:::caution
Claude Code はデスクトップ版（CLI）でのみ動作確認を行っています。Web 版（claude.ai）での動作は未検証です。
:::

### macOS の場合

ネイティブインストーラー（推奨）または Homebrew でインストールします。

```bash
# ネイティブインストーラー（推奨、自動更新あり）
curl -fsSL https://claude.ai/install.sh | bash

# または Homebrew
brew install --cask claude-code
```

インストール後、ターミナルで `claude` を実行すると Claude Code が起動します。

### Windows の場合

ネイティブインストーラー（推奨）、WinGet、または WSL でインストールします。

```powershell
# PowerShell（推奨、自動更新あり）
irm https://claude.ai/install.ps1 | iex

# または WinGet
winget install Anthropic.ClaudeCode
```

インストール後、ターミナル（PowerShell またはコマンドプロンプト）で `claude` を実行すると Claude Code が起動します。

:::note
Windows ではネイティブ（[Git Bash](https://git-scm.com/downloads/win) が必要）と WSL の両方に対応しています。WSL 2 の使用が推奨されています。詳細は [Claude Code 公式ドキュメント](https://code.claude.com/docs/ja/setup#windows-setup)を参照してください。
:::

その他のインストール方法については [Claude Code セットアップガイド](https://code.claude.com/docs/ja/setup)を参照してください。

## インストール方法

利用するクライアントに応じて選んでください。

:::caution
スキルはクライアント間で自動同期されません。複数の環境で使う場合は、それぞれに導入します。
:::

### Claude Code: プラグインとして導入（推奨）

マーケットプレイスの登録とプラグインのインストールは別の操作です。Claude Code 内で以下の 2 つのコマンドを実行します。

```
/plugin marketplace add diverta/kuroco-skills
/plugin install kuroco-skills@diverta-kuroco-skills
```

シェルから実行する場合は以下のコマンドを使用します（対話操作なし）。

```bash
claude plugin marketplace add diverta/kuroco-skills
claude plugin install kuroco-skills@diverta-kuroco-skills
```

インストール結果に `Run /reload-plugins to activate.` と表示された場合は `/reload-plugins` を実行してください。

プラグインのスキルは `kuroco-skills:` 名前空間で提供されます（例: `/kuroco-skills:admin-mcp`）。明示的に呼ばなくても、関連する依頼があればエージェントが自動的に選択します。

### skills CLI で導入

[skills.sh](https://skills.sh/) の CLI は Claude Code / GitHub Copilot / Cursor / Cline など 18 以上のエージェントに対応し、1 コマンドで導入できます。

```bash
npx skills add diverta/kuroco-skills
```

:::tip
`skills.sh` でインストールすると、Kuroco Skills と一緒に `find-skills` メタスキルも自動的にインストールされます。
`find-skills` があることで、Claude Code が適切なスキルを選択して呼び出せるようになり、Kurocoに関する質問に対して、`kuroco-skills` を適切に使用します。
:::

### Claude Code: 手動配置

リポジトリには `.claude-plugin/plugin.json` が含まれるため、スキルディレクトリに直接クローンすると、次回セッションから `kuroco-skills@skills-dir` として自動で読み込まれます（マーケットプレイスの登録もインストール操作も不要です）。

すべてのプロジェクトで利用する場合:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/diverta/kuroco-skills.git ~/.claude/skills/kuroco-skills
```

特定のプロジェクトでのみ利用する場合:

```bash
mkdir -p .claude/skills
git clone https://github.com/diverta/kuroco-skills.git .claude/skills/kuroco-skills
```

### Codex: リポジトリスキルとして利用

Codex はプロジェクト内の `.agents/skills/` 配下からスキルを認識します。リポジトリの `.agents/skills/kuroco-*` は `skills/` の共有スキルを指す相対シンボリックリンクになっているため、クローンしたリポジトリを Codex で開けば利用できます。

```bash
git clone https://github.com/diverta/kuroco-skills.git
cd kuroco-skills
```

Codex で明示的に呼ぶ場合は `$kuroco-app-builder`、`$kuroco-admin-mcp` のように `$` を付けます。関連する依頼では暗黙に選択される場合もあります。Claude Code の `/kuroco-skills:app-builder` とは呼び出し表記が異なりますが、参照する `SKILL.md` は同じです。

### claude.ai: zip をアップロード

claude.ai では [設定] → [機能]（Settings → Features）からスキルを zip でアップロードします。ファイル作成・コード実行が有効な Pro / Max / Team / Enterprise プランで利用できます。アップロードしたカスタムスキルはユーザー単位で、組織全体への配布や集中管理はできません。

claude.ai は GitHub リポジトリを直接参照できないため、スキルごとに zip をアップロードします。[Releases](https://github.com/diverta/kuroco-skills/releases/latest) から使いたいスキルの zip を直接ダウンロードできます（`SKILL.md` が zip のルートに入っています）。全スキルをまとめて取得する場合は [kuroco-skills-all.zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-skills-all.zip) をダウンロードして展開すると、スキルごとの zip が全部入っています（アップロードは展開後の zip を 1 つずつ行います）。

### Claude API / Agent SDK

Skills API（`/v1/skills`）でアップロードし、[コード実行ツール](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)の `container` パラメータで `skill_id` を指定します。ベータヘッダー `skills-2025-10-02` が必要です。アップロードしたスキルはワークスペース全体で共有されます。

## 同梱ドキュメント

Kuroco Skills には、Kuroco 公式ドキュメントがカテゴリ単位の統合ファイルとしてパッケージに同梱されています。
インストール後すぐに AI エージェントがドキュメントを横断検索して、正確な回答を提供できます。

お知らせ・リリースノートは鮮度が重要なため同梱されていません。これらは公式サイトを参照してください。

ドキュメントを最新の状態に保つには、パッケージを更新してください（[更新方法](#更新方法)を参照）。

## 基本的な使い方

Kuroco Skills をインストールすると、Claude Code で Kuroco に関する質問をした際に、関連するスキルが自動的に呼び出されます。
特別なコマンドや操作は必要ありません。

### Kurocoに関する質問をする

以下のように Claude Code に質問すると、関連するスキルが自動的に使用されます。

| 質問例 | 使用されるスキル |
|--------|----------------|
| 「Kuroco の API でログインを実装したい」 | api-content |
| 「Nuxt3 で Kuroco のコンテンツを表示したい」 | frontend-integration |
| 「バッチ処理で Slack 通知を送りたい」 | server-processing |
| 「Smarty のプラグインの使い方を知りたい」 | server-processing |
| 「サイトを KurocoFront にデプロイしたい」 | frontend-integration |
| 「Kuroco でアプリを丸ごと作りたい」 | app-builder |
| 「まず動く画面（プロトタイプ）を見せて」 | app-builder |
| 「管理画面からコンテンツを作成したい」 | admin-mcp |
| 「Claude Desktop から Kuroco を操作したい」 | admin-mcp |
| 「コンテンツ構造を設計したい」「カテゴリとタグのどちらを使うべきか」「コンテンツ定義を新しく作りたい」 | content-structure |
| 「会員グループをどう分ければいいか」「あとから SSO を繋げられるようにしたい」 | auth-design |
| 「外部 API と連携したい」「API キーをどこに置くべきか」 | server-processing |
| 「Kuroco の利用料が増えた原因を調べたい」 | api-performance-review |
| 「セキュリティ設定に問題がないか確認したい」 | security-audit |
| 「サイトの仕様書を作って」「コンテンツ定義を ER 図にして」 | spec-writer |
| 「Kuroco のドキュメントでエンドポイント設定を調べたい」 | kuroco-docs |

### Claude に Kuroco の管理操作をさせる（Admin MCP）

Model Context Protocol にネイティブ対応するクライアント（Claude Code、Claude Desktop、Codex CLI など）向けに、Kuroco は Admin API を **Admin MCP サーバ**として直接公開しています。接続すれば、Claude Code に自然言語で指示するだけで管理操作を実行できます。

```
「ブログの記事を3件作成して」
「コンテンツ定義の一覧を確認したい」
「会員情報を取得してリストアップして」
```

エンドポイントは `/direct/rcms_api/admin_mcp/` にマウントされ、HTTP POST + JSON-RPC 2.0 を受け付けます。ホストに応じて 2 種類の認証方式に対応します。

| ホスト | 認証方式 |
|------|---------|
| 管理画面 URL（`ROOT_MNG_URL`） | 管理セッション Cookie（管理画面ログインと同じ） |
| API URL（`ROOT_API_URL`） | `Authorization` ヘッダの Bearer トークン |

Bearer トークンは 2 種類を受け付けます。

- **OAuth Authorization Server アクセストークン**: `/direct/login/oauth_idp/{idpid}/token` から `target_domain=AdminMCP` で発行。RFC 8707 / RFC 9728 に準拠した audience 拘束あり。エンドユーザー認可フロー向けの推奨方式です。
- **特権 static トークン**（`api_id=-1`）: 有効な管理セッションから `AdminMCPServer::generateToken()` で発行する Bearer。OAuth ハンドシェイクを張れないツール（プログラム的にトークンを取得して使うスクリプト、対話ログインを伴わない CI など）向けの経路です。

モジュールスコープ付き URL（`/x/<csv>/readonly`）の指定方法、認識される CSV エントリ、ツール名の規則などの詳細は [MCP サーバ リファレンス](/ja/docs/reference/mcp-server/#admin-mcp-サーバ) を参照してください。

#### Claude Code への登録例

```bash
# OAuth Authorization Server 認可（エンドユーザー向けの推奨）
claude mcp add --transport http kuroco-admin \
  https://example.g.kuroco.app/direct/rcms_api/admin_mcp/x/topics_group_1,member/readonly

# Static Bearer トークン（CI／無人エージェント向け）
claude mcp add --transport http kuroco-admin \
  https://example.g.kuroco.app/direct/rcms_api/admin_mcp/x/topics_group_1,member \
  --header "Authorization: Bearer <privileged-static-token>"
```

他クライアント別の設定方法や、ヘッダ受け渡しの詳細は [MCP クライアント設定](/ja/docs/reference/mcp-client-configuration/) を参照してください。

:::caution 課金について
`/direct/rcms_api/admin_mcp/` 配下のリクエストは `/direct/` 経由として **Kuroco の課金対象**となります。AI エージェントが自律的に操作を繰り返すと意図せず多数のリクエストが発生する可能性があるため、読み取り中心のエージェントには `/readonly`、CSV のモジュール指定は本当に必要な範囲に絞ることを推奨します。
:::

## 更新方法

プラグインとして導入した場合は、マーケットプレイスとプラグインの両方を更新します。

```
/plugin marketplace update diverta-kuroco-skills
/plugin update kuroco-skills
```

更新の反映には Claude Code の再起動が必要です。

サードパーティのマーケットプレイスは、既定で自動更新が無効です。自動更新を有効にする場合は、`/plugin` → [Marketplaces] タブ → 対象のマーケットプレイスを選択 → [Enable auto-update] を選びます。

:::note
`/plugin marketplace add` は登録のみを行うコマンドで、すでに登録済みのマーケットプレイスに対して実行しても最新版は取得されません（`already on disk` と表示されます）。更新には `/plugin marketplace update` を使用してください。
:::

skills CLI で導入した場合は、同じコマンドを再実行します。

```bash
npx skills add diverta/kuroco-skills
```

手動配置した場合と、Codex でリポジトリスキルとして利用している場合は、`git pull` で更新します。

```bash
cd ~/.claude/skills/kuroco-skills
git pull origin main
```

claude.ai にアップロードした場合は、新しい zip をダウンロードしてアップロードし直します。

## リポジトリ構成

```
kuroco-skills/
├── .claude-plugin/
│   ├── marketplace.json         # マーケットプレイスカタログ
│   └── plugin.json              # プラグインメタデータ
├── .agents/skills/              # Codex がスキルを認識するための skills/ へのシンボリックリンク
├── skills/
│   ├── kuroco-docs/             # ドキュメント検索 + 公式ドキュメント（同梱）
│   ├── app-builder/             # アプリ・サイトの構築ワークフロー（フロントエンド先行）
│   ├── api-content/             # API パターン + コンテンツ CRUD
│   ├── frontend-integration/    # Vite/Nuxt/Next.js 統合 + 公開先の決定 + KurocoFront デプロイ
│   ├── server-processing/       # Smarty プラグインリファレンス + バッチ & Webhook + 外部連携方式の設計
│   ├── admin-mcp/               # Admin MCP 接続、OAuth/CIMD、スコープ
│   ├── content-structure/       # コンテンツ構造の設計 → MCP による作成
│   ├── auth-design/             # 会員認証・権限の設計判断
│   ├── security-audit/          # セキュリティ設定チェック
│   ├── api-performance-review/  # API パフォーマンス・コストレビュー
│   └── spec-writer/             # 実設定からの仕様書生成
├── scripts/
│   ├── consolidate_docs.py      # 同梱ドキュメントの統合ファイル再生成（メンテナ向け）
│   └── build-skill-zips.sh      # スキルごとの zip を dist/ に生成（リリース用）
├── tests/
│   └── skill-trigger/           # スキル選択（description）のリグレッションテスト
└── README.md
```

## 関連ドキュメント

- [Kuroco Skills リファレンス](/ja/docs/reference/kuroco-skills-detail/) - 各スキルの詳細説明
- [Kuroco Skills GitHub リポジトリ](https://github.com/diverta/kuroco-skills)
- [Claude Code 公式ドキュメント](https://code.claude.com/docs/ja/overview)


---

# OpenAI Playground での MCP コネクタの登録方法

> 元ページ: `tutorials/openai-playground-mcp-setup` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/openai-playground-mcp-setup/
> 概要: OpenAI の Playground に Kuroco MCP を接続し、Kuroco のデータを Playground から参照・操作できるようにする手順を説明します。

このページでは、OpenAI の Playground に Kuroco MCP を接続する手順を説明します。

MCP を接続することで、Playground 上で「プロジェクトの一覧を取得して」「ナレッジを検索して」などと質問するだけで、Kuroco のデータをもとに回答が得られるようになります。

:::caution
OpenAI Playgroundは、MCPサーバーのOAuthクライアントとして対応していません（2026年6月時点）。そのため、このページではKurocoの**特権付き静的トークン**構成での接続手順を説明します。

本番運用をOAuth IdP（動的アクセストークン）構成で構築する場合、このページの手順は本番の認証フローを再現しません。アプリケーションのコードに組み込む場合は、[OpenAI Responses APIドキュメント](https://platform.openai.com/docs/api-reference/responses)（`Authorization: Bearer <トークン>`を自前で付与してMCPを呼び出す）を参照してください。
:::

## 用語の説明

**MCP（Model Context Protocol）とは**

AI（OpenAIのモデルなど）が外部のツールやデータに接続するための標準規格です。KurocoはMCPサーバーを提供しており、PlaygroundからKurocoのAPIを直接呼び出せるようになります。

**Playgroundとは**

OpenAI Platform（`platform.openai.com`）が提供する、ブラウザ上の動作確認UIです。モデル・ツール・プロンプトを設定して、コードを書かずに挙動を確認できます。MCPサーバーは **Hosted ツール** として登録します。

**特権付き静的トークンとは**

Kuroco APIへのアクセスに使用する認証トークンです。Kuroco管理画面のSwagger UIから発行します。

## 前提条件

- Kurocoのサイトが作成済みであること
- OpenAIのアカウントがあること

MCPサーバーが有効になったKuroco APIエンドポイント（例：`https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp`）が必要です。

MCPサーバーの設定がまだの場合は、先に[Model Context Protocol (MCP) と Kurocoの連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)を参照して設定を完了させてください。

## 手順1: Kurocoで特権付き静的トークンを取得する

1. Kuroco管理画面 → [API] → 対象のAPIグループを選択します。
2. [セキュリティ]が`特権付き静的トークン`になっていることを確認します（なっていない場合は変更します）。
3. 右上の[Swagger UI]をクリックします。
4. [特権付き静的トークン]セクションの[＋生成する]をクリックします。
5. 有効期限を設定してトークンを発行し、値を控えます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88473e15cd29131d065135cb43511737.png)

:::caution
特権付き静的トークンは外部に公開しないでください。クライアントサイドのコードやリポジトリに直接埋め込まず、環境変数やシークレットマネージャーで管理します。
:::

## 手順2: PlaygroundにMCPサーバーを追加する

1. [platform.openai.com](https://platform.openai.com/)にサインインします。最初は[Home]（ダッシュボード）が表示されます。
2. 左サイドバー（または上部ナビゲーション）の[Chat]タブをクリックします。
3. 画面中央に表示される[Create]をクリックして、新しいChatセッションを開始します。
4. 開いたセッション画面で、右側設定パネルの[Tools]セクションにある[＋Add]をクリックし、[Hosted]→[MCP server]を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1621f6bdda5b5c761d8ee25db39b0df8.png)

5. [Add MCP server]ダイアログが開くので、右上の[＋Server]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2abdb1cc5644290b4659e322c75365be.png)

6. [Connect to MCP Server]フォームに以下を入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9dd216c353a4f1cab4785bc8a583094b.png)

| 項目 | 入力内容 |
|------|---------|
| **URL** | `https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp` |
| **Label** | `kuroco`（任意の識別名） |
| **Description** | 任意（省略可） |
| **Authentication** | `Access token / API key`を選択し、手順1で取得した特権付き静的トークンを入力します |

7. [Connect]をクリックします。
8. 接続に成功すると、ツール一覧と[Approval]の設定画面が表示されるので、[Add]をクリックして完了します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/07cf6679982be9bb7d54be79d02a8a49.png)

## 手順3: 接続を確認する

MCPサーバーの接続が完了したら、Playground画面右側のチャット欄から指示を出して動作を確認します。

以下のようなプロンプトを入力します。

```text
接続したAPIに登録されているデータの一覧を取得してください
```

Playgroundが Kuroco の MCP ツールを呼び出す際は、以下の流れで処理されます。

1. Playgroundが質問の内容から適切なMCPツール（例：`knowledge_search`）を選択します。
2. デフォルト設定（毎回承認）では、ツールを実行する前に確認ダイアログが表示されます。[Approve]をクリックして実行を許可します。

![Image from Gyazo](https://diverta.gyazo.com/11504d7c7ff831581ec3c970cfc4eb62/raw)

3. PlaygroundがKuroco MCPサーバーにリクエストを送り、データを取得します。
4. 取得したデータをもとに回答が生成され、チャット画面に表示されます。

![Image from Gyazo](https://diverta.gyazo.com/9b0c4775d8f2353ed01951d488998cff/raw)

:::tip
承認なしで自動実行したい場合は、MCPサーバー追加時の[Approval]設定を[Never require approval]に変更します。ただし書き込み操作（コンテンツ作成・更新など）を含む場合は、意図しないデータ変更を防ぐため、毎回承認のままにしておくことを推奨します。
:::

接続が成功していれば、実行されたツール名が表示され、回答にKurocoから取得した内容が含まれます。

## 利用できるツール

接続後にPlaygroundに表示されるツールは、Kuroco側で各エンドポイントのMCP設定の[ツール名]に設定した名前です。表示されるツールの一覧は、MCPを有効化したエンドポイントの構成によって異なります。

たとえば、[Model Context Protocol (MCP) と Kurocoの連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/)の手順どおりに設定した場合は、以下のツールが表示されます。

| ツール名 | 操作 |
|---------|------|
| `search_topics_by_subject` | コンテンツを件名で検索する |
| `create_blog_post` | コンテンツを作成する |
| `update_blog_post` | コンテンツを更新する |

## トラブルシューティング

| 症状 | 確認箇所 |
|------|---------|
| `access forbidden`が返る | 特権付き静的トークンが正しくコピーされているか、対象APIグループでMCPサーバーが有効化されているか（手順1）、トークンに対象APIグループへのアクセス権限があるかを確認します |
| ツールが表示されない | サーバーURLが正しいか（末尾に`/mcp`が必要）を確認し、Playgroundを再読み込みして再接続を試みます |
| `OAuth Bearer token required` / `401 Unauthorized`が返る | 対象APIグループの[セキュリティ]設定が`特権付き静的トークン`になっているか確認します。`OAuth IdP`になっている場合、PlaygroundはOAuthクライアントとして未対応のため接続できません。`特権付き静的トークン`に切り替えてください |

## 関連ドキュメント

- [Model Context Protocol (MCP) と Kurocoの連携](/ja/docs/tutorials/expose-a-kuroco-api-with-mcp/) — Kuroco側のMCP設定ガイド
- [MCPクライアント設定リファレンス](/ja/docs/reference/mcp-client-configuration/) — Static Tokenを含む認証設定の詳細

## 要確認

<!-- 公開前に削除してください -->

- ソース資料（workspace-intern PR #478）にはChatGPT版ドキュメント（OAuth接続、workspace-intern PR #481でマージ済み）への相互リンクがあったが、front_kuroco_document_site側にはまだ反映されていないため、公開中のリンクとして張れない。ChatGPT版のfront側反映が完了次第、このページと相互リンクを追加することを推奨する


---

# Kuroco RAGの設定方法

> 元ページ: `tutorials/setting-up-kurocorag` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-kurocorag/
> 概要: Kuroco RAGは、外部ソースから取得した情報を使用して生成AIモデルの精度と信頼性を向上させるサービスです。Kuroco RAGで何ができるかを理解することを目的に、Kurocoに保存したコンテンツ情報を参照して回答を生成するGPTの作成をします。

## 概要
Kuroco RAGは、外部ソースから取得した情報を使用して生成AIモデルの精度と信頼性を向上させるサービスです。

このドキュメントではKuroco RAGで何ができるかを理解することを目的に、Kurocoに保存したコンテンツ情報を参照して回答を生成するGPTの作成をします。  
説明はKurocoのアカウントを使用して進めますので、Kurocoアカウントを持っていない場合は[無料トライアル](https://kuroco.app/ja/free_trial/)からアカウント登録してください。

:::info
Kuroco RAGのご利用を希望する場合は以下からお問い合わせください。
- [サポート](/ja/docs/about/support/)
:::

### 学べること
以下の手順でKurocoに保存したコンテンツ情報を参照して回答を生成する独自のGPTを作成します。

- [前提条件](#前提条件)
- [Kurocoの設定](#kurocoの設定)
  - [AIを有効にする](#aiを有効にする)
  - [コンテンツを登録する](#コンテンツを登録する)
  - [APIを設定する](#apiを設定する)
- [ChatGPTの設定](#chatgptの設定)
  - [GPTの作成](#gptの作成)

### 前提条件
以下のアカウントが必要になりますので、持っていない場合はアカウントを作成してください。

- **Kurocoアカウント**：有効なKurocoアカウントを取得している必要があります。まだアカウントをお持ちでない場合は、[無料トライアル](https://kuroco.app/ja/free_trial/)からアカウント登録してください。

- **ChatGPT Plus、Team、またはEnterpriseプラン**：GPTs(独自にカスタマイズしたChatGPTの機能)を利用するには、[ChatGPT Plus](https://openai.com/blog/chatgpt-plus)、[ChatGPT Team](https://openai.com/chatgpt/team)、または[ChatGPT Enterprise](https://openai.com/chatgpt/enterprise)プランのいずれかを取得している必要があります。  
持っていない場合はアップグレードをご検討ください。

## Kurocoの設定
### AIを有効にする
[AI] -> [ベクトルデータ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4e47d56cef62185748d29321b79ba79d.png)

AIの項目を有効にして、[更新する]をクリックします。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e166aac6a92486724a8354f73504e7d4.png)

### コンテンツを登録する
ChatGPTに参照させるコンテンツをKurocoに登録します。  
登録した内容は独自にカスタマイズしたChatGPTのみがAPIを通して取得でき、その他の外部からは参照できないように設定していきます。

#### コンテンツ定義を追加する
[コンテンツ定義一覧](/ja/docs/management/content-structure-topics-group/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/22303613bafe005dc86e92cf56be990c.png)

以下の内容で設定をします。  

**全般**

|項目|設定|
|:--|:--|
|名前|RAGデモ|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff626ed3a68cb0ee19ee26ace85daea8.png)

**項目設定**

|項目|Slug|項目名|項目設定|
|:--|:--|:--|:--|
|ext_1|なし|WYSIWYG|WYSIWYG|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ab3132fe663411dec3d1a0ac224d171.png)

**検索設定**

|項目|設定|
|:--|:--|
|ベクトルデータに変換する|有効にする|
|埋め込みモデル|text-embedding-3-small|
|キーワードテンプレート(AI/Vector)|デフォルトのまま|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21580c3a4bd28a6c172d98529cb42100.png)

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。 

#### コンテンツを追加する
OpenAIが利用する為の情報をコンテンツに登録します。    

[コンテンツ一覧](/ja/docs/management/content-structure-topics/)の画面から[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fde6a35102823dd62276880e9c072892.png)

ここでは例として以下の3コンテンツを追加しました。  

**リモートワークガイドライン**  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b53d8c1ea95d854992ffbe3ea9f093ea.png)

**福利厚生ガイドブック**  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d442635a9c6af986e7c1a5693102002f.png)

**連絡先**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbf70948f9b5c00bc80e8e363f951309.png)

:::info
例では社内向けのAIアシスタントを想定した社内文書の登録をしています。  
チュートリアルでは3コンテンツのみですが、実際の運用時には就業規則全体を保存し、大量の文章から希望する項目の検索・確認をAIに代行させるような用途で利用します。
:::

#### ベクトルデータを確認する
コンテンツを追加すると、ベクトルデータへの変換が自動で行われます。  
コンテンツ編集画面から[その他]->[ベクトルテンプレート]とクリックし、生成されたキーワードを確認してください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/32dadda620eb401354ddd83124c63ab8.png)

また、ベクトルデータ生成の進捗と結果は[外部システム連携]->[AI]のページで確認ができます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f34db47188d71f907b0a2dec623393a1.png)

### APIを設定する
次に独自にカスタマイズしたChatGPTがコンテンツ情報を取得するためのAPIを準備します。  

#### APIの追加
Kuroco管理画面のAPIより「追加」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

|項目|設定|
|:--|:--|
|タイトル|RAGデモ|
|版|1.0|
|説明|このAPIで、Kuroco RAGデモ株式会社に関する就業規則の情報が取得できます。|
|並び順|0|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7f658ed17793c03add787cb0e2c56c72.png)

:::info
こちらの設定内容は後ほどChatGPTに入力されますので、説明などは本APIが何をするためのものか分かるように書いてください。
:::

#### セキュリティの設定
次にセキュリティの設定をします。[セキュリティ] をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/13343765f26ba0b7cbc38f3ec672029e.png)

セキュリティを[静的アクセストークン]に設定して、[保存する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c84a5a31f1e82c0ac13f230b6dbb1c1d.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f1615114fde46f36accb17c533005333.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL
- `https://chatgpt.com/`

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET

CORS_ALLOW_HEADERSの [Add Header] をクリックし、下記を追加します。

- x-rcms-api-access-token

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc5b4897582b0a76e12b09c4a3fae339.png)

問題なければ [保存する] をクリックします。

#### 静的アクセストークンの発行
[Swagegr UI]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5cba3395f6e4a591ac72e4de24b38ba0.png)

静的アクセストークンの有効期限を設定して[生成する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/92d73cd0e035e4189781d1f56816781f.png)

静的アクセストークンが発行されるので値をメモします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/17088d004596c9f8b4e0164f2cd2e4d5.png) 

#### エンドポイントの作成
RAGデモのAPIから[新しいエンドポイントの追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c974e89072808dfc5014a00735b36ef4.png)

以下のエンドポイントを作成します。

|項目|設定|
|---|---|
|パス|`search`|
|カテゴリー|コンテンツ|
|モデル|Topics|
|オペレーション|list|
|topics_group_id|先ほど作成したコンテンツ定義のID|
|cnt|APIレスポンスで返されるエントリ数を制限するために`3`を設定|
|required_param|vector_search|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f335e7aa8d0f3c43cba4fa746009569d.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a1537ad24321c3d941651c2681dee316.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6fa1b5c405edab22280fb0b66c2f78f8.png)

設定ができたら[追加]をクリックしてエンドポイントを追加します。

#### OpenAPI設定ファイルのエクスポート
KurocoにはOpenAPIエクスポートの機能があり、OpenAPIの仕様に沿った形式でAPIの情報を出力できます。

エンドポイント一覧の画面から[OpenAPIエクスポートする]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/93c87525c1a6a10a458eb607897db585.png)

ダウンロード用のモーダルが表示されるので、形式をYAMLにし、対象のエンドポイントにチェックを入れて、[エクスポート]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/af0f993df1ffb9316429f76ee32a76f9.png)

ダウンロードしたYAMLファイルにはエンドポイントのURLや利用可能なパラメータの設定全てが含まれるので少し調整します。  
今回はChatGPTに`vector_search`のパラメータのみを利用させるので、parametersの項目から`vector_search`パラメータ以外のすべてのパラメータを削除します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5de8a3a1e2528925003ca0ad577bd22.png)

また、`vector_search`のrequiredを`true`に設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/52b368a54c283376d0e852cfdbad481d.png)

YAMLファイルの例は以下のようになります。

```yaml
openapi: 3.1.0
info:
  title: RAGデモ
  version: '1.0'
  description: 'このAPIで、Kuroco RAGデモ株式会社に関する就業規則の情報が取得できます。'
servers:
  -
    url: 'https://YOUR_SITEKEY.g.kuroco.app'
    description: 'API Backend'
paths:
  /rcms-api/8/search:
    get:
      tags:
        - コンテンツ
      summary: ''
      description: |
        
        ### **Topics::list (v1)**
        
        
        ## Controller parameters
        
        > **topics_group_id** `27`
        
        > **cnt** `3`
        
        > **required_param** `vector_search`
        
      parameters:
        -
          name: vector_search
          schema:
            type: string
            format: ''
          in: query
          required: true
          style: form
          explode: true
          description: ベクトル検索
      responses:
        '200':
          description: 'Topics data successfully fetched'
        '404':
          description: 'Topics data could not be found'
      security:
        -
          Token-Auth: []
      operationId: getRcmsApi8Search
components:
  schemas: {  }
  securitySchemes:
    Token-Auth:
      type: apiKey
      in: header
      name: X-RCMS-API-ACCESS-TOKEN
```

ここまでできたらKuroco側の準備は完了です。

## ChatGPTの設定
### GPTの作成
https://chat.openai.com/ にアクセスしてログインします。  

サイドバーの[GPTを探す]をクリックし、ページ右上の[+作成する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f5075a2631210fe401f35343333c7c90.png)

GPTの作成画面が開くので、構成タブで以下のように設定します。

|項目|内容|
|:--|:--|
|名前|Kuroco RAGデモ株式会社 社内ルールアシスタンタント|
|説明|Kuroco RAGデモ株式会社の就業規定を参照して質問に回答します。|
|指示|効率的かつ正確な対応を行うため、ユーザーとのやり取りは以下のガイドラインに従って行ってください。<br/>1. 必ず指定したエンドポイントにリクエストを送ってから回答してください。<br/>2. エンドポイントから得た情報に含まれないことを推測して回答することは禁止します。<br/>3. 業務に関係ないと思われる質問には回答しないでください。|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3eb2b32e4a156e7b1df07165e3fe486c.png)

次に、画面下までスクロールし、[新しいアクションを作成する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7305a56f5f3fa53ef90bf2689f0394aa.png)

スキーマにKurocoからエクスポートして調整したopenapi.yamlファイルの内容を張り付け、認証横の歯車マークをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0176375b95bb64f8a08deeb4f2a3c7ec.png)

以下のように設定して[保存する]をクリックします。

|項目|値|
|:--|:--|
|認証タイプ|APIキー|
|APIキー|Kurocoで発行した静的アクセストークン|
|認証タイプ|カスタム|
|カスタムヘッダーの名前|X-RCMS-API-ACCESS-TOKEN|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/26a30e0473facc3781902c7cef566ef0.png)

[テストする]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fb78cec11a36c5ef48be155cd9792b05.png)

GPTがKurocoとの通信を試みますので、[許可する]をクリックし、データが取得できれば完了です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2a7ff374c76f46afbfc56bb7071fb1a.png)

[作成する]をクリックして公開範囲を指定し、GPTの作成を完了してください。

### 動作の確認
作成したGPTにアクセスして質問をすると、Kurocoに保存したコンテンツの内容を参照して回答することが確認できます。  
意図しない回答をする場合はGPTに対する指示を更新して調整します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/253c06839ae83901aec9ce93f01b1703.png)

以上でKuroco RAGを利用したGPTの作成が完了しました。  
このように、Kuroco RAGはGPTに与える情報の管理と連携を容易にする役割を担い、GPTは外部のコンテンツを参照することで生成AIの精度が向上します。

## 関連ドキュメント
- [ベクトルデータ](/ja/docs/management/vector-data/)
- [KurocoRAGログ](/ja/docs/management/vector-search-log-list/)
- [あいまい検索用のベクトルテンプレートを用意する](/ja/docs/tutorials/how-to-implement-vector-search/)
- [AIによる回答を生成する](/ja/docs/tutorials/generating-ai-responses/)
- [静的アクセストークンによるAPIアクセス制限の方法](/ja/docs/tutorials/restricting-api-access-with-statictoken/)
