# Kuroco Skills

Kuroco の開発を支援する Agent Skills パッケージ

An Agent Skills package for Kuroco development

---

## 日本語

### 概要

このリポジトリは、[Kuroco](https://kuroco.app/) を使った開発を支援する **Agent Skills** 集です。API連携、コンテンツ管理、フロントエンド統合、バッチ処理、セキュリティ監査などのベストプラクティスを提供します。

Agent Skills は `SKILL.md` を中心としたファイルベースの標準仕様で、Claude Code をはじめ複数のAIエージェントで利用できます。エージェントは起動時に各スキルの `name` と `description` だけを読み込み、関連する依頼が来たときに本文を読み込みます（プログレッシブディスクロージャー）。そのため、インストールしただけではコンテキストをほとんど消費しません。

### 含まれるスキル

| スキル | 説明 |
|--------|------|
| **kuroco-docs** | Kuroco公式ドキュメントの検索・参照 |
| **kuroco-app-builder** | アプリ・サイトをゼロから丸ごと構築するワークフロー（フロントエンド先行のモックファースト → コンテンツ定義 → API → 実データ接続 → デプロイ） |
| **kuroco-api-content** | API設計・認証（Cookie/Token/StaticToken）、CORS、コンテンツCRUD、フィルタークエリ |
| **kuroco-frontend-integration** | Vite/Nuxt.js/Next.js統合、SPA/SSG/SSR、認証実装、公開先の決定（既定はKurocoFront）、KurocoFrontデプロイ |
| **kuroco-server-processing** | Smartyプラグイン・構文リファレンス（151プラグイン）、バッチ処理、Webhook、トリガー、外部システム連携方式の設計（直接呼び出し／プロキシ／取り込み、シークレット・トークン管理） |
| **kuroco-admin-mcp** | Admin MCP（管理MCPサーバー、AIエージェントからの管理操作の推奨手段）の接続設定、OAuth/CIMD認証、スコープ、ツール利用 |
| **kuroco-content-structure** | コンテンツ構造の設計判断（TopicsGroup分割、マスタデータ表現、分類、ext_slug方針、JSON項目によるフィールド圧縮）と、MCPツールによるコンテンツ定義（TopicsGroup）の作成・フィールドタイプリファレンス |
| **kuroco-auth-design** | 会員認証・権限の設計判断（会員グループ、登録フロー、アクセス制限スコープ、パスワードポリシー、エンタープライズSSO/SCIM連携） |
| **kuroco-security-audit** | Admin MCP経由でのセキュリティ設定チェック（読み取り専用・設定変更なし）、チェックリストとレポート形式 |
| **kuroco-api-performance-review** | Admin MCPによるAPIパフォーマンス／利用料の調査（API解析・キャッシュ設定レビュー・改善提案） |
| **kuroco-spec-writer** | 実設定からの仕様書生成（読み取り専用）。コンテンツ定義の項目表・ER図・API一覧・認証・ワークフローをMarkdown+Mermaidで出力し、OpenAPI定義とコンテンツ定義の生データを機械可読ファイルとして同梱、PDF+zip変換スクリプト付き |

### インストール方法

利用するクライアントに応じて選んでください。**スキルはクライアント間で自動同期されません。** 複数の環境で使う場合はそれぞれに導入します。

#### Codex：リポジトリスキルとして利用

Codexはプロジェクト内の `.agents/skills/` 配下からスキルを認識します。このリポジトリでは `.agents/skills/kuroco-*` が `skills/` の共有スキルを指す相対シンボリックリンクになっているため、クローンしたリポジトリをCodexで開けば利用できます。

```bash
git clone https://github.com/diverta/kuroco-skills.git
cd kuroco-skills
```

Codexで明示的に呼ぶ場合は `$kuroco-app-builder`、`$kuroco-admin-mcp` のように `$` を付けます。関連する依頼では暗黙に選択される場合もあります。Claude Codeの `/kuroco-skills:app-builder` とは呼び出し表記が異なりますが、参照する `SKILL.md` は同じです。

#### Claude Code：プラグインとして導入（推奨）

マーケットプレイスの登録とプラグインのインストールは**2ステップ**です。

```
/plugin marketplace add diverta/kuroco-skills
/plugin install kuroco-skills@diverta-kuroco-skills
```

シェルから実行する場合（対話操作なし）:

```bash
claude plugin marketplace add diverta/kuroco-skills
claude plugin install kuroco-skills@diverta-kuroco-skills
```

インストール結果に `Run /reload-plugins to activate.` と表示された場合は `/reload-plugins` を実行してください。

プラグインのスキルは `kuroco-skills:` 名前空間で提供されます（例: `/kuroco-skills:admin-mcp`）。明示的に呼ばなくても、関連する依頼があればエージェントが自動的に選択します。

#### 他のAIエージェント：skills CLI で導入

[skills.sh](https://skills.sh/) の CLI は Claude Code / GitHub Copilot / Cursor / Cline など18以上のエージェントに対応し、1コマンドで導入できます。

```bash
npx skills add diverta/kuroco-skills
```

特定のスキルだけを入れる場合:

```bash
npx skills add diverta/kuroco-skills --skill kuroco-admin-mcp
```

#### Claude Code：手動配置

このリポジトリは `.claude-plugin/plugin.json` を含むため、スキルディレクトリに直接クローンすると次回セッションから `kuroco-skills@skills-dir` として自動で読み込まれます（マーケットプレイス登録もインストール操作も不要）。

全プロジェクトで使う場合:

```bash
git clone https://github.com/diverta/kuroco-skills.git ~/.claude/skills/kuroco-skills
```

特定のプロジェクトだけで使う場合:

```bash
git clone https://github.com/diverta/kuroco-skills.git .claude/skills/kuroco-skills
```

#### claude.ai

**設定 → 機能（Settings → Features）** からスキルを zip でアップロードします。ファイル作成・コード実行が有効な Pro / Max / Team / Enterprise プランで利用できます。アップロードしたカスタムスキルはユーザー単位で、組織全体への配布や集中管理はできません。

claude.ai はGitHubリポジトリを直接参照できず、**スキルごとに zip をアップロード**する必要があります。手元で zip 化する代わりに、[Releases](https://github.com/diverta/kuroco-skills/releases/latest) から使いたいスキルの zip を直接ダウンロードしてください（`SKILL.md` が zip のルートに入っています。常に最新版）:

| スキル | ダウンロード |
|--------|------------|
| kuroco-app-builder | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-app-builder.zip) |
| kuroco-content-structure | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-content-structure.zip) |
| kuroco-auth-design | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-auth-design.zip) |
| kuroco-api-content | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-api-content.zip) |
| kuroco-frontend-integration | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-frontend-integration.zip) |
| kuroco-server-processing | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-server-processing.zip) |
| kuroco-admin-mcp | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-admin-mcp.zip) |
| kuroco-security-audit | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-security-audit.zip) |
| kuroco-api-performance-review | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-api-performance-review.zip) |
| kuroco-spec-writer | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-spec-writer.zip) |
| kuroco-docs | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-docs.zip) |

複数のスキルを使う場合は必要な数だけダウンロード・アップロードしてください（zip 1つ = スキル1つ）。全スキルをまとめて落としたい場合は [kuroco-skills-all.zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-skills-all.zip) をダウンロードして展開すると、上記のスキル zip が全部入っています（アップロードは展開後の zip を1つずつ）。自分で最新のソースから zip を作りたい場合は `./scripts/build-skill-zips.sh` を実行すると `dist/` に全スキル分が生成されます。

#### Claude API / Agent SDK

Skills API（`/v1/skills`）でアップロードし、[コード実行ツール](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)の `container` パラメータで `skill_id` を指定します。ベータヘッダー `skills-2025-10-02` が必要です。アップロードしたスキルはワークスペース全体で共有されます。

### 更新方法

Claude Code のプラグインとして導入した場合:

```
/plugin marketplace update diverta-kuroco-skills
```

サードパーティのマーケットプレイスは既定で自動更新が無効です。自動更新を有効にするには `/plugin` → **Marketplaces** タブ → 対象を選択 → **Enable auto-update** を選びます。

skills CLI で導入した場合は、同じコマンドを再実行します:

```bash
npx skills add diverta/kuroco-skills
```

手動配置の場合:

```bash
cd ~/.claude/skills/kuroco-skills && git pull origin main
```

### 使い方

ドキュメントはパッケージに同梱されているため、インストール後すぐに使用できます。最新のドキュメントを取得するには適宜更新してください。

Kurocoに関する質問をすると、関連するスキルが自動的に呼び出されます。

**例：**
- 「Kurocoでアプリを丸ごと作りたい」「まず動く画面を見せて」→ app-builder スキル
- 「KurocoのAPIでログインを実装したい」→ api-content スキル
- 「Nuxt3でKurocoのコンテンツを表示したい」→ frontend-integration スキル
- 「バッチ処理でSlack通知を送りたい」→ server-processing スキル
- 「Smartyのプラグインの使い方を知りたい」→ server-processing スキル
- 「KurocoFrontにサイトをデプロイしたい」→ frontend-integration スキル
- 「管理画面からコンテンツを作成したい」→ admin-mcp スキル
- 「MCPクライアントからKurocoを操作したい」「Admin MCPに接続したい」→ admin-mcp スキル
- 「Kurocoのセキュリティ設定を点検したい」→ security-audit スキル
- 「Kurocoの利用料が増えた原因を調べたい」「キャッシュヒット率を上げたい」→ api-performance-review スキル
- 「サイトの仕様書を作って」「コンテンツ定義をドキュメント化して」→ spec-writer スキル

---

## English

### Overview

This repository provides **Agent Skills** for [Kuroco](https://kuroco.app/) development, covering API integration, content management, frontend integration, batch processing, and security auditing.

Agent Skills is a filesystem-based standard built around `SKILL.md`, supported by Claude Code and many other AI agents. Agents load only each skill's `name` and `description` at startup and read the body when a request matches (progressive disclosure), so installing skills costs almost no context until they are used.

### Included Skills

| Skill | Description |
|-------|-------------|
| **kuroco-docs** | Search and reference Kuroco official documentation |
| **kuroco-app-builder** | End-to-end app/site building workflow (frontend-first mock prototyping → content structures → API → live data → deploy) |
| **kuroco-api-content** | API design, authentication (Cookie/Token/StaticToken), CORS, content CRUD, filter queries |
| **kuroco-frontend-integration** | Vite/Nuxt.js/Next.js integration, SPA/SSG/SSR, authentication, hosting choice (KurocoFront by default), KurocoFront deployment |
| **kuroco-server-processing** | Smarty plugin & syntax reference (151 plugins), batch processing, webhooks, triggers, external-system integration design (direct call / proxy / ingestion, secret & token management) |
| **kuroco-admin-mcp** | Admin MCP server (recommended way for AI agents to perform admin operations): connection setup, OAuth/CIMD authentication, scopes, tool usage |
| **kuroco-content-structure** | Content structure design decisions (TopicsGroup splitting, master-data modeling, category/tag/relation choice, ext_slug policy, JSON-field compression) followed by Content Structure (TopicsGroup) creation via MCP tool, field type reference |
| **kuroco-auth-design** | Member authentication & authorization design decisions (member groups, registration flow, access-restriction scope, password policy, enterprise SSO/SCIM) |
| **kuroco-security-audit** | Security settings audit via Admin MCP (read-only, never modifies settings), checklist and report format |
| **kuroco-api-performance-review** | API performance & usage-cost review via Admin MCP (API analytics, cache configuration review, improvement proposals) |
| **kuroco-spec-writer** | Specification document generation from live settings (read-only): field tables, ER diagrams, API/auth/workflow pages in Markdown + Mermaid, plus machine-readable OpenAPI and content-definition dumps, with a PDF+zip build script |

### Installation

Pick the method for your client. **Skills do not sync across clients** — install separately in each environment where you want them.

#### Codex: use as repository skills

Codex discovers project skills under `.agents/skills/`. In this repository, `.agents/skills/kuroco-*` contains relative symlinks to the shared skills under `skills/`, so open the cloned repository in Codex to use them.

```bash
git clone https://github.com/diverta/kuroco-skills.git
cd kuroco-skills
```

Invoke a Codex skill explicitly as `$kuroco-app-builder` or `$kuroco-admin-mcp`. Claude Code uses plugin commands such as `/kuroco-skills:app-builder`; both clients read the same canonical `SKILL.md` files.

#### Claude Code: install as a plugin (recommended)

Adding the marketplace and installing the plugin are **two separate steps**:

```
/plugin marketplace add diverta/kuroco-skills
/plugin install kuroco-skills@diverta-kuroco-skills
```

From your shell (non-interactive):

```bash
claude plugin marketplace add diverta/kuroco-skills
claude plugin install kuroco-skills@diverta-kuroco-skills
```

If the install summary says `Run /reload-plugins to activate.`, run `/reload-plugins`.

Plugin skills are namespaced under `kuroco-skills:` (for example `/kuroco-skills:admin-mcp`). You don't need to invoke them explicitly — the agent selects them automatically when a request is relevant.

#### Other AI agents: install with the skills CLI

The [skills.sh](https://skills.sh/) CLI supports 18+ agents including Claude Code, GitHub Copilot, Cursor, and Cline, and installs in one command:

```bash
npx skills add diverta/kuroco-skills
```

To install a single skill:

```bash
npx skills add diverta/kuroco-skills --skill kuroco-admin-mcp
```

#### Claude Code: manual placement

This repository includes a `.claude-plugin/plugin.json`, so cloning it directly into a skills directory makes Claude Code load it automatically as `kuroco-skills@skills-dir` on the next session — no marketplace or install step required.

For all your projects:

```bash
git clone https://github.com/diverta/kuroco-skills.git ~/.claude/skills/kuroco-skills
```

For a single project:

```bash
git clone https://github.com/diverta/kuroco-skills.git .claude/skills/kuroco-skills
```

#### claude.ai

Upload skills as zip files under **Settings → Features**. Available on Pro, Max, Team, and Enterprise plans with file creation / code execution enabled. Uploaded custom skills are per-user; they cannot be distributed or centrally managed organization-wide.

claude.ai can't reference a GitHub repo directly — it needs **one zip per skill**. Instead of zipping it yourself, download the skill you want directly from [Releases](https://github.com/diverta/kuroco-skills/releases/latest) (`SKILL.md` sits at the zip root; always the latest version):

| Skill | Download |
|-------|----------|
| kuroco-app-builder | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-app-builder.zip) |
| kuroco-content-structure | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-content-structure.zip) |
| kuroco-auth-design | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-auth-design.zip) |
| kuroco-api-content | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-api-content.zip) |
| kuroco-frontend-integration | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-frontend-integration.zip) |
| kuroco-server-processing | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-server-processing.zip) |
| kuroco-admin-mcp | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-admin-mcp.zip) |
| kuroco-security-audit | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-security-audit.zip) |
| kuroco-api-performance-review | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-api-performance-review.zip) |
| kuroco-spec-writer | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-spec-writer.zip) |
| kuroco-docs | [zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-docs.zip) |

Download and upload as many as you need (one zip = one skill). To grab everything at once, download [kuroco-skills-all.zip](https://github.com/diverta/kuroco-skills/releases/latest/download/kuroco-skills-all.zip) — it contains all the skill zips above (extract it, then upload each inner zip individually). To build the zips yourself from source, run `./scripts/build-skill-zips.sh`, which writes all of them to `dist/`.

#### Claude API / Agent SDK

Upload through the Skills API (`/v1/skills`), then reference the `skill_id` in the `container` parameter of the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool). Requires the `skills-2025-10-02` beta header. Uploaded skills are shared workspace-wide.

### Update

Installed as a Claude Code plugin:

```
/plugin marketplace update diverta-kuroco-skills
```

Third-party marketplaces have auto-update disabled by default. To enable it, run `/plugin` → **Marketplaces** tab → select the marketplace → **Enable auto-update**.

Installed with the skills CLI — rerun the same command:

```bash
npx skills add diverta/kuroco-skills
```

Placed manually:

```bash
cd ~/.claude/skills/kuroco-skills && git pull origin main
```

### Usage

Documentation is bundled with the package, so it's ready to use immediately after installation. Update periodically to get the latest documentation.

When you ask about Kuroco, the relevant skills are invoked automatically.

**Examples:**
- "I want to build a whole app on Kuroco" / "Show me a working prototype first" → app-builder skill
- "I want to implement login with Kuroco API" → api-content skill
- "I want to display Kuroco content with Nuxt3" → frontend-integration skill
- "I want to send Slack notifications from batch processing" → server-processing skill
- "I want to know how to use Smarty plugins" → server-processing skill
- "I want to deploy my site to KurocoFront" → frontend-integration skill
- "I want to create content from the admin panel" → admin-mcp skill
- "I want to operate Kuroco from my MCP client" / "I want to connect to Admin MCP" → admin-mcp skill
- "I want to audit my Kuroco security settings" → security-audit skill
- "Why did my Kuroco usage cost increase?" / "I want to improve the cache hit ratio" → api-performance-review skill
- "Write a specification document for my site" / "Document my content structures" → spec-writer skill

---

## Repository Structure

```
kuroco-skills/
├── .claude-plugin/
│   ├── marketplace.json         # Marketplace catalog
│   └── plugin.json              # Plugin metadata
├── .agents/skills/              # Codex discovery links to the canonical skills
├── skills/
│   ├── kuroco-docs/             # Documentation search + official docs (bundled)
│   ├── app-builder/             # End-to-end app building workflow (frontend-first)
│   ├── api-content/             # API patterns + Content CRUD
│   ├── frontend-integration/    # Vite/Nuxt/Next.js integration + hosting choice + KurocoFront deployment
│   ├── server-processing/       # Smarty plugin reference + Batch & webhook + external integration design
│   ├── admin-mcp/               # Admin MCP connection, OAuth/CIMD, scopes
│   ├── content-structure/       # Content structure design → creation via MCP
│   ├── auth-design/             # Member auth & permission design decisions
│   ├── security-audit/          # Read-only security settings audit via Admin MCP
│   └── api-performance-review/  # API performance & cost review via Admin MCP
├── scripts/
│   ├── consolidate_docs.py      # Rebuilds kuroco-docs/docs from per-page sources
│   └── build-skill-zips.sh      # Builds per-skill zips into dist/ (used by release workflow)
├── tests/
│   └── skill-trigger/           # Skill selection (description) regression tests
├── .github/workflows/           # Release workflow (skill zips on v* tags)
└── README.md
```

## Security / セキュリティ

Agent Skills give an agent new instructions and code, so install skills only from sources you trust. Review `SKILL.md` and any bundled scripts before use.

Agent Skills はエージェントに新しい指示とコードを与えるため、**信頼できるソースからのみ**インストールしてください。利用前に `SKILL.md` と同梱スクリプトを確認することを推奨します。

## License / ライセンス

### Code / コード
MIT License

This applies to all files in this repository **except** the `skills/kuroco-docs/docs/` directory.

このリポジトリ内のファイル（`skills/kuroco-docs/docs/` ディレクトリを**除く**）に適用されます。

### Documentation / ドキュメント
The contents of the `skills/kuroco-docs/docs/` directory are official Kuroco documentation, copyrighted by [Diverta Inc.](https://www.diverta.co.jp/) These documents are bundled from the official source for convenience and are subject to Kuroco's terms of use.

`skills/kuroco-docs/docs/` ディレクトリの内容は[株式会社ディバータ](https://www.diverta.co.jp/)が著作権を有するKuroco公式ドキュメントです。利便性のためパッケージに同梱されており、Kurocoの利用規約に従います。

- Redistribution or modification of `skills/kuroco-docs/docs/` content requires permission from Diverta Inc.
- `skills/kuroco-docs/docs/` 内のコンテンツの再配布・改変には株式会社ディバータの許可が必要です。

## Links

- [Kuroco Official Site](https://kuroco.app/)
- [Kuroco Documentation](https://kuroco.app/ja/docs/)
- [Diverta Inc.](https://www.diverta.co.jp/)
- [Agent Skills (Anthropic docs)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
