---
name: kuroco-admin-mcp
metadata:
  author: Diverta inc.
  version: "1.7.5"
  lastUpdated: "2026-08-28"
description: Kuroco Admin MCP（管理MCPサーバー）の接続設定・認証・ツール利用を支援する。AIエージェントからKurocoの管理操作を行う際の推奨手段で、OAuth 2.0 / CIMD認証、スコープ（mcp:admin / mcp:tools.all / mcp:tools.write / mcp:tools.read）と作業ごとに必要なレベル、whoamiによる実効権限の確認、Claude Code・Claude Web・ChatGPT・Codex CLIからの接続設定、部分更新（patch.カラム名による行単位の書き換え、base_hashによる楽観ロック）をカバー。MCP経由の管理操作、Issuer URLやprotected resource metadataの設定、大きなCSS/JS/テンプレートの一部だけの更新、MCPツールが見えない・権限不足で書き込めない等のトラブルシュートに使用。
---

# Kuroco Admin MCP Skill

## 概要

Kuroco Admin MCP は、Kuroco 管理画面の操作（admin_api と同等の管理操作）を
**MCP (Model Context Protocol) サーバー**として公開する機能。JSON-RPC 2.0 ベースで、
Claude Code / Claude Desktop / ChatGPT などの MCP クライアントから接続できる。

**AI エージェントから Kuroco の管理操作を行う際の推奨機能。** 標準の MCP プロトコルと
OAuth 2.0 に準拠しており、追加ツールのインストール不要で主要な MCP クライアントから
そのまま利用できる。

**最大の特徴:** ツールは DB に登録するのではなく、**管理画面のコントローラーと
サービスモデルが実行時に動的に MCP ツール化**される。管理画面でできる操作は
原則そのまま MCP ツールとして利用できる。

> **公式リファレンス:** [MCP クライアント設定リファレンス](https://kuroco.app/ja/docs/reference/mcp-client-configuration/)
> 仕様は活発に更新されているため、接続手順の最終確認は公式ドキュメントを参照すること。
> 同梱の kuroco-docs スキルからも参照できる: `../kuroco-docs/docs/reference-mcp-ai.md` 内の
> `mcp-server`（MCP サーバ）/ `mcp-client-configuration`（クライアント設定）の各ページ

**類似機能との区別（混同注意）:**

| 機能 | 対象 | ツールの実体 |
|------|------|-------------|
| **Admin MCP**（本スキル） | 管理操作全般 | 管理コントローラー/サービスを動的ツール化 |
| フロント API MCP | 特定の API (`/rcms-api/{id}/...`) | 管理画面で登録した MCP ツール |
| KurocoEdge の MCP アクション | Edge ルールから MCP を呼ぶ**クライアント側** | 外部/自サイトの MCP ツール |

---

## エンドポイント

```
POST https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/<module>[,<module>][/readonly]
```

| URL | 意味 |
|-----|------|
| `.../admin_mcp/x/all` | 全モジュールの全ツール |
| `.../admin_mcp/x/all/readonly` | 全モジュール・読み取り専用 |
| `.../admin_mcp/x/topics_group_5` | 特定コンテンツ定義のレコード操作のみ |
| `.../admin_mcp/x/topics_group` | グループ定義（TopicsGroup）のCRUD |
| `.../admin_mcp/x/member,topics_group_5` | 複数モジュール（カンマ区切り） |
| `.../admin_mcp/?MODE=tools` | 利用可能モジュール一覧（REST, GET） |

**重要なルール:**

- **エンドポイントのドメインは API ドメイン（`<site_key>.g.kuroco.app`）。** 管理ドメイン
  （`.g.kuroco-mng.app`）は管理画面・Issuer URL 用であり、MCP エンドポイントには使わない。
  URL は手で組み立てず、[Admin MCP 情報ページ](#管理画面-admin-mcp-情報ページ)に
  表示される値をそのまま使うこと。
- **`/x/<スコープ>` は必須。** bare の `/direct/rcms_api/admin_mcp/` は **400** を返す
  （旧仕様の「スコープ省略＝全ツール」は廃止済み。全ツールは必ず `/x/all`）。
- **ベースパスは末尾スラッシュ必須。** ディスパッチャURL（デフォルト audience）は
  `/direct/rcms_api/admin_mcp/`（スラッシュ込み）で、`/direct/rcms_api/admin_mcp`
  （スラッシュなし）は解決されない。**スコープ付き URL（`/x/all` 等）は例示どおり
  末尾スラッシュなしで書く。** OAuth の audience はトークン発行時の URL 表記と
  厳密一致するため、登録後に URL 表記を変えない。
- モジュール識別子は小文字英数字とアンダースコアのみ（`^[a-z][a-z0-9_]*$`）。
  カンマ区切りの順序に機能上の意味はないが、URL 表記は audience として扱われるため
  一度登録した表記を固定すること。
- topics まわりは**3つの識別子を使い分ける**:
  - `topics_group_<N>` — グループNにスコープした**コンテンツ（レコード）の実操作**
  - `topics_group` — **グループ定義（TopicsGroup）自体のCRUD**（`topics_group-create` / `-list` / `-update` / `-delete`）
  - `topics` 単独指定 — **discovery専用**（グループ制約なしの同等表現）。ツールの呼び出しは拒否されるため、
    実操作には使えない。レコード操作は `topics_group_<N>`、グループ定義の操作は `topics_group` を指定する

---

## 認証

3 方式ある。**Bearer トークンが提示された場合はセッションにフォールバックしない**
（RFC 6750 準拠。無効トークンは 401）。

### 方式1: OAuth 2.0 認可コードフロー（推奨）

管理画面に **Admin MCP 用の OAuth 認可サーバー（Authorization Server）** が
自動作成される（初回に `Admin MCP (default)` がシードされる）。

- **Issuer URL**: `https://<管理ドメイン>/direct/login/oauth_idp/<idp_id>`
  - 管理画面 **[Admin MCP 情報ページ]** または OAuth Authorization Server 編集画面に表示される
- **CIMD（クライアント ID メタデータドキュメント / URL クライアント ID）** を有効化すると、
  クライアント側での client_id / secret の手動設定が不要になる
- **Dynamic Client Registration (RFC 7591) は非対応。** CIMD を使わない場合、
  クライアントは管理画面で手動登録する
- Protected Resource Metadata (RFC 9728) は認証不要で公開:
  `GET /.well-known/oauth-protected-resource/direct/rcms_api/admin_mcp/`
- **CI／無人エージェントは `client_credentials` グラント**を使う。CIMD クライアントでは
  利用できないため手動登録が必要（認可サーバー・クライアント双方の「対応するグラントタイプ」に
  `client_credentials` を含め、クライアントのトークンエンドポイント認証方式は
  `client_secret_basic` / `client_secret_post`）。トークン要求時は `resource` パラメータ
  （RFC 8707）にスコープ付き URL を指定する。リフレッシュトークンは発行されないため、
  対話的クライアントの常用には向かない（対話利用は `authorization_code` を使う）

### 方式2: 特権静的トークン

OAuth 導入前からの管理ツール向け方式。`Authorization: Bearer <特権静的トークン>` で接続。
スコープ制限はなく全権限（`mcp:admin` 相当）になるため、取り扱いに注意。

### 方式3: 管理セッション

管理画面内の UI（AI エージェント支援、ツールチェッカー等）からの呼び出し専用。
外部クライアントからは使用しない。

### IP アドレスによるアクセス制限

Admin MCP エンドポイントは**管理画面の IP アドレス制限の対象外**（送信元 IP が一定しない
クラウド型 MCP クライアントに対応するため）。接続元を限定する場合は、専用の許可 IP リストを
**[環境設定]→[管理画面] の「Admin MCPのアクセス制限(IPアドレス)」**で有効化する。

- 判定は**認証より前**。許可外 IP からはトークンの正否にかかわらず `403`
  （`Access from this IP address is not allowed.`）が返る
- 対象: Admin MCP エンドポイント（`?MODE=tools` 含む）とファイルアップロード
  （`/direct/rcms_api/mcp_upload/`）。Bearer・管理セッションの両経路に適用され、
  **管理画面内の AI エージェント機能にも適用される**
- 対象外: `?MODE=protected_resource_metadata`（RFC 9728 メタデータ配信）
- `client_credentials` によるトークン取得と発行済みトークンでの呼び出しは
  「管理画面のアクセス制限(IPアドレス)」の対象外（効くのは Admin MCP 専用リストのみ）

---

## OAuth スコープ（権限レベル）

Admin MCP 用認可サーバーの権限は個別スコープ選択ではなく**単一レベル選択**（4段階）。
**レベルはスコープ文字列で識別すること**（管理画面の日本語ラベルは似た語が並び紛らわしいため）。
`whoami` の `permissions.connection.scope` が返すのもこのスコープ文字列:

| スコープ（弱い順） | 書き込みの上限 |
|------------------|--------------|
| `mcp:tools.read` | 書き込み不可（全モジュールの `select` のみ） |
| `mcp:tools.write` | `topics` / `csvtable` / `tag` / `comment` 等の `insert`・`update` のみ。**`delete` はどのモジュールでも不可**。`rcms_api` `member` `group` `batch` は含まれない |
| `mcp:tools.all` | 全モジュール・全操作。ただし下記の例外あり |
| `mcp:admin` | 上限なし |

- `mcp:tools.write` は単独では選べず、`mcp:tools.read` と**セットで付与される**（読み取りは全モジュールに効く）
- **`auth.scopes` には上表以外の値も混じる。** ツール一覧の取得に使われる `mcp:tools.list` が併せて付与されるため、`whoami` は例えば `["mcp:admin", "mcp:tools.list"]` を返す。これは権限レベルではない。**実効的な権限レベルの判定には `auth.scopes` ではなく `permissions.connection.scope` を見る**
- `mcp:tools.all` の例外 — **グループ（権限）と汎用Smartyバッチの作成・変更・削除／メンバーへのスーパーユーザーグループ付与／特権付き静的トークンの発行**はできない（遅延実行や特権付き静的トークンには上限を安全に引き継げないため）
- `mcp:admin` は**スーパーユーザーしか承認できない**。それ以外のメンバーには同意画面で承認可能な最大レベルが提示され、そのレベルで発行される。スコープとして直接要求した場合は「`mcp:tools.all` を要求せよ」というメッセージで**拒否される**

管理画面のラベルで確認できるのは `mcp:tools.all` = **「全操作（委譲先メンバーの権限の範囲）」**。

**スコープは「上限（ceiling）」であって権限の付与ではない。** 実効権限は
**メンバー自身の権限 ∩ スコープの上限**。上限に含まれないモジュールは全操作が拒否される。
逆に、上限が広くてもメンバーに権限がなければ何もできない。

### 構築作業に必要なスコープ

サイト構築で必要なスコープは、**どのモジュールに書き込むか**で決まる:

| 作業 | 権限モジュール | 必要なスコープ |
|------|--------------|--------------|
| コンテンツ定義（TopicsGroup）の作成・更新 | `topics` | `mcp:tools.write` |
| コンテンツの投入・更新 | `topics` | `mcp:tools.write` |
| **API定義・エンドポイントの作成** | `rcms_api` | **`mcp:tools.all`** |
| 静的アクセストークンの発行 | `rcms_api` | **`mcp:tools.all`** |
| レコードの削除全般 | — | **`mcp:tools.all`** |
| 会員グループ・汎用Smartyバッチの作成・変更・削除 | `group` / `batch` | **`mcp:admin`** |
| メンバーへのスーパーユーザーグループ付与 | `member` | **`mcp:admin`** |
| 特権付き静的トークンの発行、`kuroco_front-generate_deploy_token` | — | **`mcp:admin`** |

**API エンドポイントを作る時点で `mcp:tools.write` では足りない**（`rcms_api` が
`mcp:tools.write` の上限に含まれないため、全操作が拒否される）。コンテンツ定義の作成までは
`mcp:tools.write` で進めるので、**エンドポイント作成の手前で初めて失敗する**。着手前に確認すること。

一連の構築を通しで行うなら **`mcp:tools.all`**、上表の `mcp:admin` 行に該当する作業を
含めるなら **`mcp:admin`** が必要。

リソース単位のスコープも存在する:

- `mcp:module.<mt>` — 特定モジュール（例: `mcp:module.member`）、`mcp:module.*` で全モジュール
- `mcp:topics_group.<N>` — 特定コンテンツ定義、`mcp:topics_group.*` で全定義

**enforce-if-present 方式:** スコープは **OAuth トークンにスコープが付与されている場合のみ**
強制される。スコープなしのトークン（旧来の管理エージェントトークン・特権静的トークン）は
制限されない。「スコープを設定しない＝制限なし」である点をユーザーに必ず伝えること。

**特権メタツール:**

- `kuroco_front-generate_deploy_token` は `mcp:admin` スコープ必須
- `rcms_api-generate_token` は `rcms_api/update` 権限が必要（＝`mcp:tools.all` 以上）。
  さらに `token_type: "privileged_static"` は**厳密な `mcp:admin` が必須**で、
  `mcp:tools.all` でも発行できない（発行されるトークンが接続側の上限を持たない
  常設の資格情報になるため）。`token_type: "static"` にはこの追加制約はない

**設定箇所:** 権限レベル・リソーススコープは **OAuth Authorization Server 編集画面**
（`/management/external/memberregist_sso_oauth_idp_edit/`）で設定する。設定値と Issuer URL は
[Admin MCP 情報ページ](#管理画面-admin-mcp-情報ページ)でも確認できる。

---

## クライアント接続

### 接続手順の正本は kuroco-docs

クライアント別の対応状況（CIMD / 手動クライアント登録 / ヘッダー認証）と設定手順は
`../kuroco-docs/docs/reference-mcp-ai.md` の `mcp-client-configuration` ページが正本。
Claude Code / Claude（Web・Desktop・Mobile）/ ChatGPT（Developer mode）/ Codex CLI /
Cursor / Slackbot / GitHub Copilot / カスタム実装 の対応表と手順が揃っている。

**このスキルは接続手順を複製しない。** docs は `/sync-docs` で公式サイトから再生成されるため、
複製すると再同期のたびに片方だけ更新されて乖離する。ここに置くのは、docs に無い
「Admin MCP 固有の URL の組み立て方」と「エージェントとしての振る舞い」だけ。

### Admin MCP 固有: URL がスコープであり、リソース識別子

docs の手順の URL 部分を、Admin MCP のスコープ付き URL に置き換えて使う。

```text
https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/all
https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/topics_group_5
https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/topics_group_1,member/readonly
```

**共通の前提:**

- OAuth 認可フローは Kuroco 管理画面のログイン・同意を経由するため、**接続者には
  対象サイトの管理メンバーアカウントが必要**
- **URL（スコープ）を変更した場合は再認可が必須**（audience が URL 表記と厳密一致するため）。
  クライアント UI で URL を編集できない場合は、コネクタを削除して新規追加する
- チーム利用や権限分離が必要な場合は、既定の `Admin MCP (default)` を変更せず
  用途ごとに専用の認可サーバーを作成する運用を推奨

CLI での例（OAuth の登録方式そのものは docs に従う）:

```bash
# Claude Code
claude mcp add --transport http kuroco https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/all
claude mcp login kuroco

# Codex CLI
codex mcp add kuroco --url https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/all
codex mcp login kuroco
```

接続ごとに区別できるサーバー名を付ける（`kuroco-blog` など）。画面から設定するクライアント
（Claude Web・Desktop・Mobile、ChatGPT）は、MCP URL の入力欄に上記の URL を入れる。

特権静的トークンを使う場合（OAuth を経由しない。全権限になるため取り扱い注意 →
[方式2: 特権静的トークン](#方式2-特権静的トークン)）:

```bash
claude mcp add --transport http kuroco \
  https://<site_key>.g.kuroco.app/direct/rcms_api/admin_mcp/x/all \
  --header "Authorization: Bearer <特権静的トークン>"
```

Admin MCP のヘッダー認証は `Authorization: Bearer`。コンテンツ API MCP の
`X-RCMS-API-ACCESS-TOKEN` とは別なので、docs のヘッダー認証手順をそのまま流用しない。

### 接続時の振る舞い

- **利用クライアントを識別してから手順を選ぶ。** 全クライアントで使える自動判定があると
  仮定しない。システムから示された情報かユーザーの説明で判断し、それが無く手順の選択に
  影響する場合だけ一度確認する
- **異なるクライアントの手順を混在させない。** CLI 利用者に画面操作を求めたり、
  デスクトップ利用者に理由なく CLI コマンドを求めたりしない
- **手動クライアント登録は管理画面の永続的な設定変更。** 実行前にユーザーの承認を得る。
  CIMD が使えるかどうかは docs の対応表で確認し、
  「エラーが出た」以外の理由で手動登録へ倒さない
- **Kuroco は RFC 7591 の DCR を実装していない。** DCR しか持たないクライアント
  （Cursor 等）は手動クライアント登録が唯一の経路
- **サイト全体に影響する設定変更はエージェントが確定しない。** 認可サーバーの設定変更や
  CIMD の有効化が必要な場合は、必要性を説明してユーザー自身に操作してもらう
- **接続後は新しいタスクを開始して `whoami` を実行し**、接続先ホスト・実効スコープ・
  読み書き権限・サイト固有の上限を確認してから作業に入る（[whoami による事前確認](#whoami-による事前確認)）
- 作業に必要な**最小スコープの URL** を選ぶ（[構築作業に必要なスコープ](#構築作業に必要なスコープ)）
  - **担当者の責務で決める:**

    | 担当者の責務 | スコープ |
    |---|---|
    | 構築担当 | `mcp:admin` |
    | 改修担当 | 必要に応じて `mcp:admin` も許可 |
    | 保守・運用担当 | 最小権限 |
    | その他 | 最小権限 |

---

## ツールの命名規則と使い方

`tools/list` が返すツール名は動的に生成される。コントローラー名の語尾と MODE が
**動詞に畳み込まれた** `{resource}-{verb}` 形式（1 コントローラーアクション = 1 ツール）:

**ハイフンは resource と verb を区切る1つだけ。** `{resource}` はコントローラー名から
`_api` と末尾1語（`_list` / `_edit` / `_upload`）を除いたもので、**モジュールディレクトリ名ではない**
（`topics_group_edit_api` → `topics_group`）。リソース名に含まれるアンダースコアは
ハイフンに置き換わらない。

| パターン | 例 | 意味 |
|---------|-----|------|
| `{resource}-{verb}` | `topics-list`, `topics-create`, `topics-update`, `topics-delete` | コントローラー操作（INSERT→create 等、MODE ごとに別ツール） |
| `{resource}-{verb}`（複合リソース） | `topics_group-list`, `topics_group-create` | サブエンティティ（グループ定義等）。**ハイフンは1つで、リソース名側のアンダースコアはそのまま残る** |
| 一括指定（別ツールではない） | `topics-update` / `topics-delete` の `ids` / `filter` / `set` / `rows` | 複数件は同じ update / delete ツールの引数で指定する。`dry_run` で件数を確認し `expected_cnt` でガード、200 件超は `async: true` |
| `{mt}-get` | `topics-get` | 単一レコードの ID 指定取得 |
| `{service}-{method}` | `email-send` | サービスモデル |
| メタツール | `whoami`, `topics-describe` | 実効権限の確認／topics のフィールド定義確認 |
| ステージング | `files-create_temp_upload_url` | ファイルアップロード（一時ストレージへの presigned PUT。topics バンドルにも公開される） |

**正確なツール名と入力スキーマは必ず `tools/list` で確認する（名前を推測して呼ばない）。**

- `topics_group_<N>` スコープで接続した場合も、ツール名は汎用の `topics-{verb}` のまま変わらない。
  許可グループは各ツールの `topics_group_id` 引数の enum として制約され、許可外グループの指定は拒否される
- スコープ由来の拒否は実行時に判定される。`topics_group_id` の enum に載っていない ID を
  指定して拒否された場合は、スコープ不足なのか ID が存在しないのかを読み取りツールで切り分ける

**代表的な引数**（正確な仕様は各ツールの inputSchema が正）:

- **list 系**（`{mt}-list`）: `filter`（Kuroco DSL）・`order_query`（ソート）・`cnt` / `pageID`（ページング）・
  `columns`（カラム絞り込み）。topics はさらに `topics_keyword` / `vector_query`（検索）が使える。
  **単一レコードを ID で取るときは `{mt}-get` を優先する**
- **update / delete（単一レコード系）**: ID（`topics_id` 等）が必須。topics 系ツールは動詞によらず
  `topics_group_id` を渡す

**利用フロー:**

0. **`whoami` で実効権限を確認する**（下記）。特に構築作業の着手前と、破壊的操作の前
1. `tools/list` で利用可能ツールを確認（または REST の `?MODE=tools` でモジュール一覧）
2. 読み取りツールで現状確認（親子関係: Topics には `topics_group_id`、Member には `group_id` が必要。
   親の ID は `topics_group-list` 等で先に解決する）
   - list 系ツールはデフォルトで全カラムを返す。**`columns` 引数で必要なカラムだけに絞る**
3. 書き込みツールの inputSchema を確認してから実行
   - **topics の拡張項目（ext_col）は inputSchema に列挙されない。** `topics-describe` で
     対象グループのフィールド定義を確認する:

     ```json
     // tool: topics-describe（topics_group_id は必須）
     { "topics_group_id": 5 }
     ```
   - **update 系ツールは部分更新**: 送信しなかったフィールドは変更されず既存値が保持される。
     一部のフィールドだけ変えたい場合は、ID と変更するフィールドのみを送る（既存値の再送は不要）。
     大きなテキストカラムは行単位でも部分更新できる（下記「[部分更新](#部分更新)」）
4. **INSERT / UPDATE / DELETE は実行前にユーザーに確認すること**
5. **複数レコードの書き込みは並列せず 1 件ずつ実行する。** 各書き込みはサーバー側で
   検索インデックス再構築・キャッシュ削除・トリガー処理を伴い、並列書き込みは
   レート制限（HTTP 429）の対象になる。複数件は同じ update / delete ツールの `ids` / `filter`
   （＋`set`）で 1 回の呼び出しにまとめる（`dry_run` → `expected_cnt` の順で安全に）
6. **成功レスポンスにも `errors` 配列が含まれることがある。** 常に確認する

> **lightweight_mode の注意**: topics の create/update で `lightweight_mode: true` を渡すと
> 書き込みが大幅に軽くなるが、後追いバッチで反映されるのは検索インデックスと
> ベクトル埋め込みのみ。**トリガー・外部通知（FCM/メール）・タグ集計はスキップされ
> 恒久的に実行されない**。既定動作を変えるため、使用はユーザー確認のうえで。

**ツールが見えない場合のチェックリスト:**

- 対象テーブルが **0 件のモジュールは読み取りツールが除外**される（空モジュールは INSERT のみ表示）
- URL スコープ（`/x/<module>`）にそのモジュールが含まれているか
- `readonly` 付き URL では書き込みツールが出ない
- OAuth スコープ（`mcp:module.*` / `mcp:topics_group.*`）で絞られていないか
- コンテンツ操作は `topics` ではなく `topics_group_<N>` を指定しているか

---

## 部分更新

Admin MCP の update 系ツールは 2 段階の部分更新に対応する。どちらも「変えない部分を
送らなくて済む」ための仕組みで、送受信量とコンテキスト消費を抑えられる。

### フィールド単位（すべての update 系ツール）

送信しなかったフィールドは既存値が保持される。ID と変更するフィールドだけを送る。
既存値を読み直して再送する必要はない。

### 行単位（`patch.<カラム>`）

CSS・JS・Smarty テンプレートのように長くなるカラムは、**行範囲を指定して一部だけを
書き換えられる**。カラム全体を送る代わりに、同じ update ツールへ `patch.<カラム名>` を渡す。

`patch.` は部分更新の**予約プレフィックス**。対応カラムが増えても専用ツールは追加されず、
そのリソースの `-update` に引数が 1 つ増えるだけなので、ツール一覧は膨らまない。

**対応カラム**（`tools/list` の inputSchema が正本）:

| リソース | カラム |
|---------|-------|
| `custom_function`（カスタム処理） | `contents` |
| `topics_group`（コンテンツ定義） | `custom_css` / `custom_js` / `wysiwyg_custom_css` / `search_template_keyword` / `search_template_vector` |

**手順:**

1. 読み取りツール（`custom_function-get` / `topics_group-get`）で対象カラムの
   **`<カラム名>_hash`** を取得する（保存内容の SHA-256）
2. その値を `base_hash` に渡して update を呼ぶ

```json
// tool: topics_group-update
{
  "topics_group_id": 5,
  "patch.custom_css": {
    "base_hash": "<topics_group-get が返した custom_css_hash>",
    "start_line": 2,           // 1始まり
    "delete_line_count": 1,    // 0 なら挿入（replacement は空にできない）
    "replacement": "/* 差し替え */"   // 空文字なら該当行を削除
  }
}
```

- **`base_hash` は楽観ロック**。読み取り後に他の誰かがそのカラムを変更していれば
  「changed since it was read」で拒否される。取り直して再試行する
- 更新レスポンスにも保存後の `<カラム名>_hash` が入る。続けてパッチする場合は
  **読み直さずその値を使う**
- **カラム名そのものと `patch.<カラム名>` は併用不可**（同時指定はエラー）。
  カラム名を送れば従来どおり全文置換になる
- 改行コードは元の内容（内容に改行が無ければ `replacement`）に合わせて正規化される
- 1 回の呼び出しで複数カラムを同時にパッチできる（それぞれに `base_hash` が必要）

> **ハッシュは保存内容から算出される。** サーバー側で保存時に値を正規化するカラムがあり
> （例: `search_template_*` は空だと既定テンプレート全文に置換、`custom_css` / `custom_js` は
> エディタのプレースホルダと一致すると空で保存）、**送った値と保存された値は一致しないことがある**。
> だから `base_hash` は必ず読み取りツールの `<カラム名>_hash` を使い、自分で
> ハッシュを計算しない。

---

## whoami による事前確認

`whoami` は**すべてのスコープ付きエンドポイントに常設される**メタツール（`readonly` バンドルにも出る）。
引数なしで呼べ、接続の実効コンテキストを返す。

| 返却フィールド | 内容 |
|--------------|------|
| `member` | 接続しているメンバーと所属グループ |
| `auth.method` / `auth.scopes` / `auth.expires_at` | 認証方式・付与スコープ・トークン失効時刻 |
| `permissions.granted` / `denied` | アカウント自身のモジュール権限 |
| `permissions.approval_required` | 書き込みが**承認ワークフローに回る**モジュール（直接反映されない） |
| `permissions.connection.scope` | この接続で有効な**実効スコープ**（`mcp:tools.write` / `mcp:tools.all` / `mcp:admin` 等） |
| `permissions.connection.available_scopes` | **再認可すれば取得できるスコープ**の一覧（強い順） |
| `permissions.connection.readonly` / `modules` | readonly バンドルか／エンドポイントのモジュール制限 |
| `request.client_ip` | 接続元 IP（IP 制限の切り分けに使う） |
| `site` | 接続先サイトの識別情報（**サイトの取り違え検出**）。`topics_ext_key_format` で**このサイトの拡張項目のキー命名**、`limits` で**コンテンツ構造の上限**が分かる（下記） |
| `security.ip_restrictions` | IP 制限の状態（設定内容はサイト設定を更新できる接続のみ） |

**実際に呼べるのは `permissions.granted` ∩ `permissions.connection`。** 片方だけを見て判断しない。

### 拡張項目のキー命名（`site.topics_ext_key_format`）

topics の拡張項目のキー名は**サイト設定によって2通りに分かれる**。`whoami` はそのまま使える命名文字列を返す:

| `site.topics_ext_key_format` | 意味 |
|-----------------------------|------|
| `ext_<n>` | 連番形式（例: `ext_1`）。拡張項目を JSONB で保持するサイト |
| `ext_col_<nn>` | ゼロ埋め2桁形式（例: `ext_col_01`）。レガシー形式のサイト |

- **キー名を推測しない。** 命名はサイト単位で決まるので、topics の読み書きの前に `whoami` で確認する
- 返却値は定数名ではなく命名そのものなので、`<n>` / `<nn>` を項目番号に置き換えてそのまま使える
- **グループ単位の正は `topics-describe`。** 実際のフィールド定義（どの番号がどの項目か、`ext_slug` が設定されているか）はこちらで確認する。`topics_ext_key_format` はサイト全体の命名規則を先に知るためのもの
- `ext_slug` が設定されている項目は、フロントAPIではスラッグがキーになるためこの分岐の影響を受けない
- **古いサイトでは `topics_ext_key_format` が返らないことがある。** その場合は `topics-describe` の結果を正として扱う

### コンテンツ構造の上限（`site.limits`）

`site.limits` は、コンテンツ構造に関わる4つの上限を `{current, max}` の形で返す。**`current` はこのサイトの現在の設定値、`max` はシステム上引き上げられる上限。** どちらも推測しない——設計・作成の前に必ずここで確認する。

| キー | 内容 | `max` |
|---|---|---|
| `topics_max_extension` | TopicsGroupあたりの拡張項目数 | サイトが拡張項目をJSONB形式で持つ場合は`999`、レガシー形式の場合は`99` |
| `topics_ext_group_loop` | フィールドグループ（繰り返し項目）の繰り返し回数 | `99` |
| `topics_contents_type_cnt` | TopicsGroupあたりのカテゴリ（`contents_type`）数 | `99` |
| `member_max_extension` | メンバーの拡張項目数 | `999` |

**`current`が`max`未満なら、`admin_setting-update`ツールで引き上げられる**（`tools/list`に存在するか確認してから使う。まだ見えない場合は未対応のサーバーなので、管理画面での引き上げ手順を案内する）。「拡張項目が99個までしか作れない」といった相談を受けたら、まずこの`limits`を見て、レガシー形式（`max`=99）なのかJSONB形式（`max`=999）なのか、現在値が上限に達しているだけなのかを切り分ける。

**呼ぶべきタイミング:**

1. **セッション開始時** — 接続先サイトが意図したものか、どのメンバーとして操作するかを確認
2. **構築作業の着手前** — `connection.scope` が `mcp:tools.all` または `mcp:admin` かを確認する。
   「読み書き」で始めると**コンテンツ定義までは成功し、エンドポイント作成で初めて失敗する**ため、
   途中まで作られた状態が残る。不足していれば `available_scopes` を提示して再認可を依頼する
3. **コンテンツ構造の設計前** — `site.limits`（上記）で拡張項目・フィールドグループ・カテゴリ・会員拡張項目の上限を確認する。`/kuroco-content-structure` はこの値をもとに分割・圧縮を判断する
4. **破壊的操作の前** — 対象サイトと権限を再確認

> スコープが不足している場合、**推測でツールを呼んで失敗を確かめない。**
> `available_scopes` を添えて、必要なレベルでの再認可をユーザーに依頼する。

## ファイルアップロード

バイナリを直接 MCP に送らず、**ステージング → 参照渡し**の 2 段階方式:

1. `files-create_temp_upload_url` ツールを呼ぶと、`file_id` と S3 プリサインド PUT の
   `presigned_url`（および `presigned_short_url`）が発行される。`file_size`（バイト数）と
   `ext`（拡張子）の宣言が必須:

   ```json
   // tool: files-create_temp_upload_url
   { "file_size": 1048576, "ext": "pdf" }
   ```
2. 発行された URL にファイル本体（生バイト）を PUT する（`presigned_short_url` が 307 を返す場合は
   GET で `Location` を解決してから、その URL に PUT する）
3. `topics-create` / `topics-update` のファイル/画像型フィールドの値として `file_id` を渡して消費する。
   値の形は文字列 `"files/temp/..."`、またはキャプション付きの
   `{"file_id": "files/temp/...", "desc": "キャプション"}`

### ファイルマネージャーへのアップロード（`file_manager-upload`）

topics の項目ではなくファイルマネージャーのツリー（`files/user/`・`files/ltd/`・クラウドストレージ）に置く場合は `file_manager-upload` を使う。

```json
// 16MB まで: data URI をそのまま渡す
{ "storage": "kurocofiles_public", "directory": "docs/2026", "file": "data:application/pdf;base64,...", "file_name": "report.pdf" }

// それ以上: files-create_temp_upload_url で PUT した file_id を渡す
{ "storage": "cloud_public", "directory": "videos", "file": "files/temp/kuroco/<site>/<uuid>.mp4", "file_name": "intro.mp4" }
```

- `file_name` が保存名と拡張子を決める。拡張子はサイトのアップロード許可リストにあるもの（php 等の実行系は不可）で、内容と一致していること（HTML/SVG/JS の中身を画像拡張子で置くなど、偽装は拒否される）。フォルダごとの拡張子制限も適用される
- `directory` は `file_manager-list` が返す `path` と同じ相対パスで、途中のフォルダは自動作成される（フォルダ作成ツールは無い）
- 同名ファイルは上書き（ツールは destructive 扱い）。`allow_overwrite: false` で拒否させられる
- クラウドストレージ（`cloud_public` / `cloud_private`）宛ての `file_id` はストレージ側でコピーされ、Kuroco のサーバーを経由しない。`files-create_temp_upload_url` に `storage: "S3"` を付けて発行した `file_id` ならサイズ上限なし
- ローカルストレージ（`kurocofiles_*`）宛ての `file_id` は **80MB まで**。超える場合はクラウドストレージに置く
- 応答の `path` は `file_manager-list` / `file_manager-delete` に渡す値、`content_field_value` は「ファイル（ファイルマネージャーから）」型の項目に書き込む値

> **承認ゲートとの順序**: 書き込み前のユーザー承認を得てから URL を発行し、
> 「発行 → PUT → 消費」を一続きで行うこと（承認待ちの間に発行すると期限切れのリスク）。

**制約:**

- プリサインド URL の有効期限は **10 分**。「発行 → アップロード → 消費」を 10 分以内に完了させる
- サイズ上限は `file_size` の宣言値で検査され、消費時にも再検査される（既定 100MB）
- `storage: "S3"` を付けるとサイトの S3 バケットの `files/temp/` に直接置かれる（GCS サイトでは不可）
- 小さいファイル（16MB まで）はインライン data URI でも受理される

---

## 管理画面: Admin MCP 情報ページ

`/management/rcms_api/admin_mcp_info/` に Admin MCP の設定情報が集約されている:

- エンドポイント URL 一覧（`x/all`、`x/all/readonly`、モジュール指定の例）
- OAuth 認可サーバー一覧と **Issuer URL**
- 接続クライアント一覧（client_id のみ表示。secret は表示されない）
- Admin MCP を利用する AI エージェント一覧（公開モジュール / 読み取り専用設定）
- ツールチェッカー（利用可能ツールの確認 UI）

ユーザーに Issuer URL やエンドポイントを案内するときは、まずこのページを参照させる。

---

## トラブルシューティング

| 症状 | 原因と対処 |
|------|-----------|
| 400 Bad Request | URL に `/x/<スコープ>` がない。`/x/all` 等を付ける |
| 401 + `WWW-Authenticate` | トークン無効/期限切れ。`resource_metadata` の URL から再認証。Bearer 提示時はセッションにフォールバックしないことに注意 |
| 403 `Access from this IP address is not allowed.` | Admin MCP の IP アドレス制限。[環境設定]→[管理画面]の「Admin MCPのアクセス制限(IPアドレス)」に接続元 IP を追加 |
| 接続はできるがツールが空/少ない | 上記「ツールが見えない場合のチェックリスト」を確認 |
| エンドポイント作成だけ権限エラー | `rcms_api` は `mcp:tools.write` の上限外。`whoami` で `connection.scope` を確認し、`mcp:tools.all` 以上で再認可する。**`whoami` が既に `mcp:tools.all` / `mcp:admin` を返した場合はこの行は原因ではない** — 下の「権限エラーの切り分け」へ進む |
| `privileged_static` トークンが発行できない | 厳密な `mcp:admin` が必要（`mcp:tools.all` では不可）。スーパーユーザーでの再認可が要る |
| 書き込みは成功するが反映されない | `whoami` の `permissions.approval_required` に該当モジュールがないか確認。承認ワークフロー待ちの可能性 |
| audience 不一致でトークン拒否 | エンドポイント URL の末尾スラッシュ・パス表記がトークン発行時と厳密一致しているか確認 |
| `rcms_api-generate_token` が権限エラー | `rcms_api/update` が要るため `mcp:tools.all` 以上。`privileged_static` はさらに `mcp:admin` が必要 |
| `files/temp/...` の `file_id` が解決できない | プリサインド URL の期限切れ（10 分）、PUT 前に消費した、または別サイトで発行した `file_id`。URL を再発行して PUT からやり直す |
| 認可サーバーが情報ページに出ない | 管理者が削除した認可サーバーは自動再作成されない。手動で再作成する |
| OAuth のクライアント登録が通らない | 認可サーバーで CIMD（クライアント ID メタデータドキュメント）が有効か確認する。CIMD 非対応クライアントは手動クライアント登録が必要（Kuroco は DCR を実装していない）。クライアント別の対応は `../kuroco-docs/docs/reference-mcp-ai.md` の `mcp-client-configuration` を参照 |
| Codex から接続できない | ① 認可サーバーで CIMD が有効か ② スコープ付き URL（`/x/...`）を指定しているか ③ `~/.codex/config.toml` の `[mcp_servers.<name>.oauth]` に `client_id` が残っていないか（設定済みの client_id が優先され CIMD が使われない）。CIMD を使わない場合は手動クライアント登録が必要（Kuroco は DCR を実装していない） |

### 権限エラーの切り分け

**上表の症状マッチだけで原因を確定しない。** 「書き込みが権限エラーになった」という報告は、
スコープ不足以外の原因でも同じように見える。ユーザーが「スコープ不足だと思う」と
自己診断していても、**まず事実を確認する**。

1. **HTTPステータスを確認する。** `401` は認証（トークン無効・失効）、`403` は認可
   （スコープ・権限・IP制限）。ここを取り違えると以降の切り分けが全部ずれる
2. **`whoami` を呼ぶ**（推測でツールを呼んで失敗を再現しない）
3. 返ってきた事実で分岐する:

| `whoami` の結果 | 判定 |
|----------------|------|
| `connection.scope` が `mcp:tools.write` 以下、かつ対象が `rcms_api` 等の上限外モジュール | **スコープ不足**。`available_scopes` を添えて再認可を依頼 |
| `permissions.denied` に対象モジュールがある | **メンバー自身の権限不足**。スコープを上げても解決しない。管理画面で権限を付与する |
| `permissions.approval_required` に対象モジュールがある | 権限エラーではなく**承認ワークフロー待ち**（書き込みは成功して反映されない） |
| `connection.readonly` が `true`、または `connection.modules` に対象モジュールが無い | **エンドポイントURL側の制限**。スコープではなく接続URLを変える（再認可が必要） |
| `security.ip_restrictions.admin_mcp.current_ip_allowed` が `false` | **IP制限**（403、認証より前に判定される） |
| `auth.expires_at` が失敗時刻より前 | **トークン失効**（401）。再認証 |
| 上記すべてに該当せず、スコープも権限も足りている | **スコープ問題ではない。** 入力値のバリデーションエラー（URI重複・命名規則違反等）、別の接続／別サイトでの操作、といった候補に移る。エラーメッセージ全文・使用した接続名・失敗時刻を確認する |

**`whoami` が十分な権限を示したのに「再認可してください」と案内してはいけない。**
確認した事実と矛盾する対処を提示すると、ユーザーは解決しない作業に時間を使う。

---

## セキュリティ注意事項

- **公開エンドポイント（セキュリティ=なし）での運用は非推奨。** 特に書き込みを
  認証なしで公開しない
- 特権静的トークンはスコープ制限が効かない（全権限）。可能な限り OAuth ＋
  適切な権限レベルを使う
- 読み取り用途には `x/all/readonly` や「読み取り専用」権限レベルで最小権限にする
- client_secret・トークン値をログや会話に出力しない
- Admin MCP のリクエストは管理ログに記録され、Admin API 同様**リクエスト単位で課金対象**

---

## 他スキルとの連携

| スキル | 使い分け |
|--------|----------|
| `/kuroco-security-audit` | Admin MCP の読み取り系ツールでセキュリティ設定を点検・診断する（読み取り専用） |
| `/kuroco-content-structure` | コンテンツ定義（TopicsGroup）の設計判断と、MCP ツールで作成する場合のフィールド定義リファレンス |
| `/kuroco-api-content` | エンドユーザー向けフロント API の設計・認証 |
| `/kuroco-docs` | 公式ドキュメントの横断検索 |

**使い分けの目安:** AI エージェントからの管理操作は **Admin MCP（本スキル）が推奨**。
Claude Desktop / claude.ai / ChatGPT / Claude Code いずれからも標準の MCP 接続で利用できる。
