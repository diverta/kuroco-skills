# Kuroco Skills for Claude Code

Kuroco HeadlessCMS の開発を支援する Claude Code 用スキルパッケージ

A Claude Code skill package for Kuroco HeadlessCMS development

---

## 日本語

### 概要

このリポジトリは、[Kuroco HeadlessCMS](https://kuroco.app/) を使った開発を支援する Claude Code 用のスキル集です。API連携、コンテンツ管理、フロントエンド統合、バッチ処理などのベストプラクティスを提供します。

### 含まれるスキル

| スキル | 説明 |
|--------|------|
| **kuroco-docs** | Kuroco公式ドキュメントの検索・参照 |
| **kuroco-api-integration** | API設計、認証（Cookie/Token/StaticToken）、CORS、エラー処理 |
| **kuroco-content-management** | コンテンツCRUD、フィルタークエリ、ファイル操作、CSV処理 |
| **kuroco-frontend-integration** | Nuxt.js/Next.js統合、SSG/SSR、認証実装 |
| **kuroco-webhook-processing** | バッチ処理、Webhook、Smarty構文、外部連携 |

### インストール方法

#### 方法1: skills.sh からインストール（推奨）

[skills.sh](https://skills.sh/) は AI エージェント向けスキルのオープンマーケットプレイスです。

```bash
npx skills add diverta/kuroco-skills
```

#### 方法2: Claude Code コマンドで追加

Claude Code 内で以下を実行：

```
/plugin marketplace add diverta/kuroco-skills
```

#### 方法3: 手動でクローン（グローバル）

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/diverta/kuroco-skills.git ~/.claude/skills/kuroco-skills
```

#### 方法4: プロジェクトローカルに追加

```bash
mkdir -p .claude/skills
git clone https://github.com/diverta/kuroco-skills.git .claude/skills/kuroco-skills
```

### ドキュメント同期

初回使用時、またはドキュメントが古い場合は同期を実行してください：

```bash
# Claude Code 内で実行
/sync-docs
```

または手動で：

```bash
bash ~/.claude/skills/kuroco-skills/scripts/sync-docs.sh
```

### 使い方

Claude Code でKurocoに関する質問をすると、関連するスキルが自動的に呼び出されます。

**例：**
- 「KurocoのAPIでログインを実装したい」→ api-integration スキル
- 「Nuxt3でKurocoのコンテンツを表示したい」→ frontend-integration スキル
- 「バッチ処理でSlack通知を送りたい」→ webhook-processing スキル

### 更新方法

```
/plugin marketplace update kuroco-skills
```

または手動で：

```bash
cd ~/.claude/skills/kuroco-skills
git pull origin main
```

---

## English

### Overview

This repository provides Claude Code skills for [Kuroco HeadlessCMS](https://kuroco.app/) development. It includes best practices for API integration, content management, frontend integration, and batch processing.

### Included Skills

| Skill | Description |
|-------|-------------|
| **kuroco-docs** | Search and reference Kuroco official documentation |
| **kuroco-api-integration** | API design, authentication (Cookie/Token/StaticToken), CORS, error handling |
| **kuroco-content-management** | Content CRUD, filter queries, file operations, CSV processing |
| **kuroco-frontend-integration** | Nuxt.js/Next.js integration, SSG/SSR, authentication implementation |
| **kuroco-webhook-processing** | Batch processing, webhooks, Smarty syntax, external service integration |

### Installation

#### Method 1: Install from skills.sh (Recommended)

[skills.sh](https://skills.sh/) is an open marketplace for AI agent skills.

```bash
npx skills add diverta/kuroco-skills
```

#### Method 2: Add via Claude Code command

Run in Claude Code:

```
/plugin marketplace add diverta/kuroco-skills
```

#### Method 3: Manual clone (Global)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/diverta/kuroco-skills.git ~/.claude/skills/kuroco-skills
```

#### Method 4: Add to project locally

```bash
mkdir -p .claude/skills
git clone https://github.com/diverta/kuroco-skills.git .claude/skills/kuroco-skills
```

### Document Sync

On first use or when documentation is outdated, run the sync:

```bash
# Run within Claude Code
/sync-docs
```

Or manually:

```bash
bash ~/.claude/skills/kuroco-skills/scripts/sync-docs.sh
```

### Usage

When you ask Claude Code questions about Kuroco, the relevant skills will be automatically invoked.

**Examples:**
- "I want to implement login with Kuroco API" → api-integration skill
- "I want to display Kuroco content with Nuxt3" → frontend-integration skill
- "I want to send Slack notifications from batch processing" → webhook-processing skill

### Update

```
/plugin marketplace update kuroco-skills
```

Or manually:

```bash
cd ~/.claude/skills/kuroco-skills
git pull origin main
```

---

## Repository Structure

```
kuroco-skills/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── skills/
│   ├── kuroco-docs/         # Documentation search
│   ├── api-integration/     # API patterns
│   ├── content-management/  # Content CRUD
│   ├── frontend-integration/# Nuxt/Next.js integration
│   └── webhook-processing/  # Batch & webhook
├── commands/
│   └── sync-docs.md         # /sync-docs command
├── scripts/
│   └── sync-docs.sh         # Documentation sync script
├── docs/                    # Synced documentation (generated)
└── README.md
```

## License / ライセンス

### Code / コード
MIT License

This applies to all files in this repository **except** the `docs/` directory.

このリポジトリ内のファイル（`docs/` ディレクトリを**除く**）に適用されます。

### Documentation / ドキュメント
The contents of the `docs/` directory are official Kuroco documentation, copyrighted by [Diverta Inc.](https://www.diverta.co.jp/) These documents are synced from the official source for convenience and are subject to Kuroco's terms of use.

`docs/` ディレクトリの内容は[株式会社ディバータ](https://www.diverta.co.jp/)が著作権を有するKuroco公式ドキュメントです。利便性のため公式ソースから同期されており、Kurocoの利用規約に従います。

- Redistribution or modification of `docs/` content requires permission from Diverta Inc.
- `docs/` 内のコンテンツの再配布・改変には株式会社ディバータの許可が必要です。

## Links

- [Kuroco Official Site](https://kuroco.app/)
- [Kuroco Documentation](https://kuroco.app/ja/docs/)
- [Diverta Inc.](https://www.diverta.co.jp/)
