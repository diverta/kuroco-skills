---
name: kuroco-content-structure
metadata:
  author: Diverta inc.
  version: "2.0.0"
  lastUpdated: "2026-08-27"
description: Kurocoのコンテンツ定義（TopicsGroup）を設計し、Admin MCPの topics_group-create で作成する。設計では TopicsGroup の分割、JSON項目によるフィールド圧縮、マスタを CSVテーブルとリレーションのどちらで持つか、カテゴリ・タグ・リレーションの使い分け、ext_slug の命名を決め、作成ではフィールド型（ext_type）ごとのプロパティ、繰り返しフィールドグループ、閲覧・編集制限、書き込み後の読み戻し検証を扱う。コンテンツ定義やカスタムフィールドの設計相談・新規作成・フィールド追加で使用。
---

# Kuroco コンテンツ構造（設計 → 作成）

コンテンツ定義（TopicsGroup）を **Part 1 で設計し、Part 2 で Admin MCP により作成する**。フィールドの追加・型変更は作成後だと投入済みデータの修正を伴いコストが高いので、**Part 1 の成果物（設計成果物テンプレート）をユーザーと合意してから Part 2 に進む。** 設計を飛ばして構文だけで作り始めない（`/kuroco-app-builder` も同じ理由でフェーズ1の画面確定後にこの設計を行う）。

依頼が「既に決まった定義を作りたい」だけなら Part 2 から入ってよいが、TopicsGroup の分割・マスタの表現方法・`ext_slug` が未決なら Part 1 で先に確定させる。逆に**設計相談だけの依頼なら、§6 の成果物を提示して終了する**（Part 2 には進まない）。

## 目次

- **Part 1: 設計判断**
  1. [TopicsGroupの分割](#1-topicsgroupの分割)
  2. [JSON項目によるフィールド数の圧縮](#2-json項目によるフィールド数の圧縮)
  3. [マスタデータの表現方法](#3-マスタデータの表現方法-csvテーブル-vs-リレーション別topicsgroup)
  4. [分類の持ち方（カテゴリ/タグ/リレーション）](#4-分類の持ち方-カテゴリ--タグ--リレーション)
  5. [ext_slugの命名方針](#5-ext_slugの命名方針)
  6. [設計成果物テンプレート](#6-設計成果物テンプレート)
  - [設計のアンチパターン](#設計のアンチパターン)
- **Part 2: Admin MCP での作成**
  - [Finding the MCP Tool](#finding-the-mcp-tool)
  - [Basic Structure](#basic-structure)
  - [Content Definition Parameters](#content-definition-parameters) — body field, publish scope, viewing/editing limits
  - [Verifying the result](#verifying-the-result) — mandatory read-back after every write
  - [Common Field Properties](#common-field-properties)
  - [Field Type Reference](#field-type-reference) — per-type properties and full examples: [references/field-types.md](references/field-types.md)
  - [Field Groups (Repeatable)](#field-groups-repeatable)
  - [Important Notes](#important-notes)

---

# Part 1: 設計判断

## 1. TopicsGroupの分割

拡張項目数の上限は`whoami`の`site.limits.topics_max_extension`（`{current, max}`）で確認する。`max`はサイトが拡張項目をJSONB形式で持つ場合999、レガシー形式の場合99——**推測しない**。`current`が`max`未満なら`admin_setting-update`ツールで引き上げ可能（詳細: `/kuroco-admin-mcp`）。上限に近づく、または性質の異なるデータを1つの定義に詰め込もうとしている場合は、引き上げの余地があるかを確認しつつ、分割も検討する。

| 状態 | 判断 |
|---|---|
| フィールド数が上限に近い、または増え続ける見込み | 分割する |
| 性質の異なるコンテンツ（一覧の出し方・公開設定・閲覧/編集制限が違う） | 分割する（例: 記事とお知らせ） |
| 同じ性質のデータの属性違い（例: 記事の中の「特集」区分） | 分割しない。カテゴリ・拡張項目の選択肢で表現する |

上限に近づく主な原因が「検索・一覧表示・外部連携に使わない単純な付随項目の積み重ね」であれば、分割する前に次項のJSON項目での圧縮を検討する。

## 2. JSON項目によるフィールド数の圧縮

**検索・一覧表示・外部連携（フィルタ・ソート・連携キー）に使わない、単純な付随情報**は、個別の拡張項目に分けず`json`型（ext_type 28）の1フィールドにまとめることを検討する。フィールドが増え続けがちな設定値・メタ情報の塊は、この方法で拡張項目数の上限（1.参照）を消費せずに済ませられる。

**判断基準**: 各項目について「一覧に出すか」「検索・絞り込みに使うか」「他システムとの連携キーになるか」のいずれかにYESがあれば個別の拡張項目にする。すべてNoなら、他の単純な付随項目とまとめてJSON項目に格納してよい。

例: 「表示設定（背景色・レイアウトモード・内部メモ）」のような、検索対象にも一覧表示対象にもならない設定値はJSON項目1つにまとめる。「カテゴリ」「価格」「公開日」のような絞り込み・並び替え・一覧表示に使う項目は個別の拡張項目として残す。

**制約（一次資料で確認できていない点として明記する）**: 標準の`filter`/`order`クエリでJSON項目の内部キーを直接絞り込み・並び替えできるという記載は見つかっていない。個別の拡張項目に用意されている絞り込みオペレーション（含む/=/&lt;/&gt;等）は、決まった型の値を前提にしたものであり、JSON型のような自由形式の内部構造を対象にした記載は無い。**この判断基準に反してJSON項目の内部キーで絞り込みたい要件が出た場合は、推測で進めず実際にAdmin MCPで試して確認する。**

## 3. マスタデータの表現方法: CSVテーブル vs リレーション（別TopicsGroup）

Kurocoで「マスタ（繰り返し参照される共通データ）」を持つ方法は2通りある。**呼び出す側の項目の型が、そのままAPIレスポンスの形を決める。**

| | CSVテーブル + `csvtable`/`csvtable_checkbox` | 別TopicsGroup + `relation` |
|---|---|---|
| マスタの実体 | CSVテーブル（TopicsGroup外の別リソース） | 通常のTopicsGroup（コンテンツ） |
| 呼び出し側のAPIレスポンス | マスタの値は含まれない（キーのみ）。中身は`Master::list`を別途呼んで自分で結合する必要がある | **id + ラベル（例: `subject`）がインラインで返る**（`"ext_col_11": { "topics_id": 123, "subject": "タイトル" }`） |
| マスタ側で拡張項目・カテゴリ・公開制御を持てるか | 持てない（CSVの行・列のみ） | 持てる（普通のコンテンツのため） |
| マスタ自身の属性で絞り込みたい（例:「特定カテゴリのブランドだけ」） | 不可 | 可能（`:R()`検索。下記の制約あり） |
| 向くケース | 都道府県・業種一覧など、**静的でごく単純な**キー/値の対応 | マスタ自体が管理画面で編集される、属性を持つ、絞り込みに使う場合 |

**原則: マスタを呼ぶ側の項目は`relation`型にする。** CSVテーブルは「本当に単純な固定リスト」の場合の軽量な代替として使う。どちらを選んでも作成は Part 2 の[作成ツール対応表](#part-1-で選んだ要素の作成ツール)に従う（CSVテーブル自体は `csvtable-create` で別に作る）。

**ただし`relation`は「フルジョイン」ではない。** デフォルトで返るのは**id + ラベルのみ**（`module_id`とラベル1個）。関連先コンテンツの全フィールドをレスポンスに含めたい場合は、**エンドポイントの後処理にカスタム処理を追加する**必要がある（`api_method`でモデル取得 →`append`で差し替え。`module_type`が`topics`/`member`/`inquiry`のいずれかで実装が変わる）。実装は`/kuroco-server-processing`・詳細は`/kuroco-api-content`を参照。この一手間を設計段階で成果物に書いておかないと、「`relation`にしたのにマスタの中身が取れない」という手戻りになる。

**多言語サイトの注意**: `:R()`によるリレーション先の絞り込みは**主言語に対してのみ実行可能**。多言語設定を有効にしていても紐づくコンテンツは主言語が元になる。多言語マスタで絞り込み検索を使う設計の場合はこの制約を成果物に明記する。

## 4. 分類の持ち方: カテゴリ / タグ / リレーション

> Kuroco側に「どれを使うべきか」という公式の指針は無い。以下は各機構の実際の挙動（`/kuroco-api-content`）から導いた設計判断であり、Kurocoの一次情報ではない。

| 機構 | 実体 | 多重選択 | 向くケース |
|---|---|---|---|
| カテゴリ | 単一の階層ID（APIのフィールド名は`contents_type`）。選択肢は管理者が `topics_category-*` で管理 | 既定は1コンテンツ1カテゴリ。定義の `contents_type_cnt` で 0=カテゴリ無効 / N>1=複数スロット | 排他的な分類（例: 記事種別） |
| タグ | 文字列配列。選択肢は `tag-*` で登録。定義の `tag_allow_private_flg=1` にすると管理者以外の投稿者も自分用のタグを登録できる | 可 | 横断的なラベル付け（例: キーワード） |
| リレーション | 他コンテンツ参照 | 型次第 | 分類先自体に属性がある、または分類先を管理画面で編集したい場合（実質3.の「マスタ」と同じ判断） |

カテゴリは `topics_category-create`、タグは `tag-create` で TopicsGroup 作成後に登録する（Part 2 の作成ツール対応表）。**カテゴリ数の上限**は`whoami`の`site.limits.topics_contents_type_cnt`（`{current, max}`、`max`は99）で確認する。細かく分類したい分類軸が複数ある、または選択肢が増え続ける見込みなら、カテゴリではなくタグかリレーションに寄せる。

## 5. ext_slugの命名方針

**すべての拡張項目に`ext_slug`を設定する。** 未設定の場合、キー名は`ext_1`形式と`ext_col_01`形式にサイト単位で分かれ（`whoami`の`site.topics_ext_key_format`で決まる）、フロント側のマッパーがサイトごとに変わってしまう（詳細: `/kuroco-app-builder` の `references/mock-contract.md`）。設計時点でスラッグ名（アプリ用のフィールド名と一致させる）を決め、成果物に明記する。タイトルは標準項目 `subject` に載せて拡張項目にしない（`subject` は予約語でもあり、relation のラベルとして返る）。予約語は [references/field-types.md › Reserved slug names](references/field-types.md#reserved-slug-names) を照合する（`description` / `title` / `price` は可、`subject` / `tags` / `keyword` は不可）。

## 6. 設計成果物テンプレート

Part 2 に進む前に、TopicsGroupごとにこの形式でまとめ、ユーザーの合意を得る:

```markdown
## コンテンツ定義: 記事
- 本文の持ち方: content_input_type 2（本文は WYSIWYG 拡張項目 `body` として持つ）
- 閲覧制限（secure_level）: なし（公開） ／ 編集制限（writer_groups）: 編集部
- 承認（need_application_groups）: なし ／ 自分の投稿のみ（my_topics_only_limit_groups）: なし
  （グループは名前で書き、ID は Part 2 で `group-list` から解決する）
- 多言語: 有効／無効（有効なら relation の `:R()` 絞り込みは主言語基準、CSVテーブルの表示名は言語別の列で持つ）
- タイトル: 標準項目 `subject`（拡張項目にしない）

| フィールド名(ext_slug) | 型 | 必須 | 備考 |
|---|---|---|---|
| body | wysiwyg | ✓ | 本文 |
| lead_text | text | - | |
| main_image | image | ✓ | |
| author | relation (module: member) | ✓ | 全データ取得が必要ならエンドポイント後処理を追加 |
| brand | relation (module: topics, group_id: X) | - | マスタ=別TopicsGroup |
| prefecture | csvtable (csv_master_id: Y) | - | 静的固定リストのため |
| display_settings | json | - | 背景色・レイアウトモード等、検索/一覧/連携に使わない付随設定をまとめて格納 |
| gallery（グループ, group_repetitions 5） | image + text(caption) | - | 繰り返しフィールドグループ。子フィールドは repetitions 1 |

## コンテンツ定義: ブランド（マスタ）
（別 TopicsGroup にしたマスタは、それ自体にも上と同じ定義ブロックを1つ書く。既定: 編集制限は呼び出し側と揃える／閲覧制限は呼び出し側と同じ／承認・自分の投稿のみは「なし」）

## Part 2 前にユーザーへ確認する未決事項
- 例: 給与の単位（月給/年収）、必須にする項目、画像の上限サイズ、承認者（approvalflow）の有無 — 要件文に無い属性は既定で埋めず、ここに列挙して合意を取る

## マスタ一覧
| マスタ名 | 表現方法 | 作成手段 | 理由 |
|---|---|---|---|
| ブランド | 別TopicsGroup + relation | `topics_group-create`（呼び出し側より先に作り、返る id を relation の group_id に渡す） | 属性（ロゴ画像・説明文）を持つため |
| 都道府県 | CSVテーブル | `csvtable-create`（既存なら `csvtable-list` で id） → `csv_master_id` | 固定・属性不要のため |
```

## 設計のアンチパターン

| してはいけないこと | 理由 |
|---|---|
| マスタを持たせたいだけなのに、選択肢（select）の巨大な固定リストにする | 選択肢の追加・変更のたびにコンテンツ定義自体を編集することになる。CSVテーブルかリレーションにする |
| `relation`にすれば関連データが全部返ると思い込む | デフォルトはid+ラベルのみ。全データが要るならエンドポイント後処理が必須 |
| 性質の異なるデータを1つのTopicsGroupに無理に収める | 拡張項目数の上限に早く達し、公開設定・閲覧/編集制限も細かく分けられなくなる |
| `ext_slug`を設定せず番号キーのままAPIを設計する | サイトによってキー形式（`ext_1`/`ext_col_01`）が変わり、フロントの実装がサイト依存になる |
| 検索・一覧・絞り込みに使う項目までJSON項目にまとめてしまう | JSON内部キーでの絞り込み・並び替えは標準機能での対応が未確認。個別の拡張項目に出す |
| 単純な付随情報まで律儀に個別の拡張項目にして上限に近づける | 一覧・検索・連携に使わないなら、JSON項目1つにまとめて上限を圧迫しない |

---

# Part 2: Admin MCP での作成

Part 1 で確定した設計を、Admin MCP の `topics_group-create` で作成する手順と構文。用語対応: 拡張項目 = extension field（以下 *field*）、コンテンツ定義 = content structure / TopicsGroup、閲覧・編集制限 = viewing / editing limit（`secure_level` / `writer_groups`。定義レベルの設定をまとめて *container parameters* と呼ぶ）。

## Part 1 で選んだ要素の作成ツール

| 設計で選んだもの | 作成ツール |
|---|---|
| TopicsGroup 本体と拡張項目 | `topics_group-create`。既存定義への追加は `topics_group-update`（→ [Adding fields to an existing definition](#adding-fields-to-an-existing-definition)） |
| CSVテーブル（マスタ） | `csvtable-create`（既存なら `csvtable-list` で ID を取る）。その ID を CSV テーブル型フィールドに渡す |
| カテゴリ | `topics_group-create` はグループ名と同名の最初のカテゴリを自動作成し、その ID を `topics_category_id` で返す。名前の変更・追加は `topics_category-update` / `topics_category-create` |
| タグ | `tag-create`（タグの分類は `tag_category-create`） |
| 閲覧/編集/承認のグループ ID | `group-list` で解決する。**推測しない** |

**Source of Truth**: Build each field with the property vocabulary documented in this skill (`options`, `required`, and the per-type properties in [references/field-types.md](references/field-types.md)) — these are what the write handler consumes. Use the tool's live `inputSchema` for the **top-level parameters** (see [Content Definition Parameters](#content-definition-parameters)); that object sets `additionalProperties: false`, so an undeclared top-level key is rejected.

**Verify by read-back after every write** (see [Verifying the result](#verifying-the-result)). A successful response means the call was accepted, not that every field landed as intended — check before reporting success to the user.

## Finding the MCP Tool

Content Structures are managed through the **Kuroco Admin MCP server** (`/direct/rcms_api/admin_mcp/`). Group-definition CRUD requires the `topics_group` scope in the connection URL (e.g., `/x/topics_group` or `/x/all`). See `/kuroco-admin-mcp` for connection setup, OAuth authentication, and scopes.

**How to find the correct tool:**

1. Verify the connection with the **`whoami` tool** (present on every scoped endpoint, including `readonly` ones), then run `tools/list`.
   - Group definitions live under the `topics` permission module, so **`mcp:tools.write` is enough** to create them.
   - **But that level cannot create API endpoints** (`rcms_api` is outside its ceiling). If the user's goal includes exposing this content through an API, tell them up front that the endpoint step needs `mcp:tools.all` or higher — otherwise they get a content definition they cannot serve. See `/kuroco-admin-mcp`.
   - Check `permissions.approval_required` too: if `topics` is listed, writes enter the approval workflow instead of taking effect directly.
2. Look for the group-definition tools — with the standard naming convention this is **`topics_group-create`** (list/update/delete follow the same `topics_group-{verb}` pattern). Tool names are generated dynamically, so **always confirm the exact name and `inputSchema` via `tools/list` — never guess**.
3. If no matching tool appears, check the connection scope (`topics_group` missing, or a `readonly` URL hides write tools — see the `/kuroco-admin-mcp` checklist), or **ask the user** which MCP server they have configured.
4. Build your JSON against the tool's `inputSchema` and call the tool. **Creating a content structure is a write operation — confirm with the user before executing.**

### Recommended workflow

1. **Check the tool's live `inputSchema`** (`tools/list`) for the **top-level** parameters — that object rejects undeclared keys, so this is where the schema is authoritative.
2. **Take the Part 1 §6 artifact as input** and carry its 定義レベル設定 into the container parameters; elicit only what the artifact lacks: body field (`content_input_type`) and access rules (`non_public_flg` / `secure_level` / `writer_groups`). See [Content Definition Parameters](#content-definition-parameters). Resolve any group IDs with `group-list` — never guess them.
3. **Build the `fields` array** using the property vocabulary of this skill (`options`, `required`, and the per-type properties in `references/field-types.md`) — **not** the raw `ext_option` / `ext_limit_item` columns, which are silently ignored on write.
4. **Show the final JSON and confirm once** — the design was agreed in Part 1, so this confirmation covers only the payload — then send it to the tool.
5. **Read the record back** with `topics_group-get` and verify the stored values. See [Verifying the result](#verifying-the-result).

## Basic Structure

Top-level JSON structure:

```json
{
  "name": "Content structure name (required)",
  "description": "Description of the content structure (optional)",
  "fields": [
    // Array of field definitions or field groups (at least one required)
  ]
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name of the content structure |
| `description` | string | No | Description of the content structure |
| `fields` | array | Yes | Array of field definitions or field groups (minimum 1) |

## Content Definition Parameters

`name` / `description` / `fields` are not the whole contract. The parameters below live at the **top level** of the same JSON and control the body field and the access rules for every record in this definition. **They cannot be expressed as fields, and omitting them silently accepts defaults that are often wrong for the request.**

| Parameter | Type | Description |
|-----------|------|-------------|
| `content_input_type` | number | `0`=WYSIWYG body, `1`=Textarea body, `2`=Custom. **`2` is the recommended value and is the default on API/MCP INSERT — leave it as is.** `2` means the built-in `contents` field is not used and **every item is built as an extension field** in `fields`. When the content needs a main body, declare a WYSIWYG field (`ext_type: 6`) for it instead of switching to `0`/`1` |
| `open_flg` | number | `0`=unpublished/disabled, `1`=published/enabled (default `1`). The UI label depends on `non_public_flg` |
| `non_public_flg` | number | `0`=publish-oriented (default), `1`=internal use only. **`secure_level` is required when this is `1`** |
| `secure_level` | integer[] | **Viewing limit**: group IDs allowed to view records. An empty array means publicly viewable |
| `writer_groups` | integer[] | **Editing limit**: group IDs allowed to insert/update/delete records. How administrator groups and multiple limits combine is defined in `/kuroco-api-content` (閲覧/編集制限の優先順序) — check it before promising "only group X can edit" |
| `need_application_groups` | integer[] | Group IDs whose updates require approval (`data_waiting`) before going live |
| `my_topics_only_limit_groups` | integer[] | Group IDs restricted to records they authored themselves |
| `can_save_draft_groups` | integer[] | Group IDs allowed to save drafts instead of publishing immediately |

> **Reading back the unset state**: when you omit `secure_level` / `writer_groups` / `need_application_groups` / `my_topics_only_limit_groups` / `can_save_draft_groups`, they are stored as the **string `"0"`**, not as an empty string or empty array. `"0"` means "no restriction configured" — do not read it as "group 0 is allowed".

**Mapping natural-language requests to these parameters** — a request phrased in terms of visibility is a request for these parameters, not for a field:

| The user says | Set |
|---|---|
| 「外部には公開しない」「社内向け」「internal only」 | `non_public_flg: 1` + `secure_level: [<group ids>]` |
| 「担当者だけが見られる」「会員限定」 | `secure_level: [<group ids>]` |
| 「編集できるのは編集部だけ」 | `writer_groups: [<group ids>]` |
| 「公開前に承認を通す」 | `need_application_groups: [<group ids>]` — usually the same groups as `writer_groups` (the people who can edit are the ones whose updates need approval). This only marks *whose* updates wait; **who approves** is configured separately with the `approvalflow-*` tools (outside this skill) — say so, or approvals go nowhere |
| 「自分が作成したレコードだけ見せる・編集させる」 | `my_topics_only_limit_groups: [<group ids>]`（定義レベル）。relation フィールドの `self_only` は別物で、**関連先の選択候補**を自分の作成分に絞るプロパティ |
| 「記事本文が必要」「blog / news article」 | Keep `content_input_type: 2` and declare a WYSIWYG field (`ext_type: 6`) in `fields` |

**Do not switch to `content_input_type: 0`/`1` just because the content has a body.** `2` (Custom) is the recommended shape: every piece of content is an explicit, named field. The Practical Examples in `references/field-types.md` follow this pattern — Example 1 declares its own `Article Body` WYSIWYG field while leaving `content_input_type` at its default.

**Never guess group IDs.** Resolve them with `group-list` first — group names and IDs differ per site (e.g. a site may have `Administrator`=1, `Editor`=2, `User`=104 with no contiguous numbering).

## Verifying the result

A successful `topics_group-create` response does **not** prove your fields were stored as intended: the ignored properties above fail silently. After every create/update, read the record back and check the stored values.

```json
// tool: topics_group-get
{ "topics_group_id": <returned id> }
```

Check `formData` in the response — it exposes the per-field stored state with a numeric suffix per field:

| What you intended | Field to check | Expected when it worked |
|---|---|---|
| `select` / `checkbox` choices | `options_<n>` | `{"news":"お知らせ",...}` — the key→label map. (`ext_option_<n>` holds the same data serialized as `"key::val"` lines, `"key::default::val"` when an option carries `"default": true`) |
| `required: true` | `ext_limit_item_<n>` / `limits_<n>` | `"required=1"` / `{"required":"1"}` |
| Field type | `ext_type_<n>` | The `ext_type` you sent |
| Repeatable group | `ext_group_loop_<n>`, `ext_group_parent_ext_col_<n>` | Repetition count on every member field; children point at the group's first field (e.g. `"ext_3"`) |
| Access rules | `non_public_flg`, `secure_level`, `writer_groups`, `need_application_groups`, `my_topics_only_limit_groups`, `can_save_draft_groups` | `1` for the flag; group lists as comma-separated strings (`"1,2"`), unset ones as `"0"` |
| Per-type properties (`file_type`, `true_label`, `csv_master_id`, …) | not individually documented here | Diff the whole `formData` against the before-snapshot (or the intended payload) instead of guessing key names; `topics-describe` confirms the API-facing result |

`topics-describe` is the complementary check: it reports the resulting **API-facing** shape of each field (e.g. a 5-repetition group appears as `"type": "array", "maxItems": 5`).

Report any discrepancy to the user rather than assuming the write took effect.

## Common Field Properties

Properties shared by all field types:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ext_title` | string | Yes | Display name of the field |
| `ext_type` | number | Yes | Field type identifier (see reference table below) |
| `type` | string | No | Field type name (see reference table below). **Not required** — creation succeeds without it, since `ext_type` carries the type. Kept in the examples below because it is harmless and self-documenting |
| `ext_slug` | string | No | Slug for API access. **Set this on every field.** With a slug, the front API returns the field under that name (`main_image`). Without one, the key is positional, and its form differs per site: either `ext_1` (plain counter) or `ext_col_01` (zero-padded). `whoami` reports which one this site uses in `site.topics_ext_key_format`, and `topics-describe` is authoritative for a specific group. Positional keys also break when fields are reordered, so a slug removes both problems |
| `ext_help_msg` | string | No | Help text displayed to editors (admin UI only) |
| `description` | string | No | Field description used in the generated API schema (OpenAPI / MCP tool schema) |
| `repetitions` | number | No | Number of repetitions allowed |
| `required` | boolean | No | Whether the field is required |
| `searchable` | boolean | No | Expose the field in the **management-screen** search form (`ext_limit_item.searchable=1`). Unrelated to front API filtering |
| `template` | string | No | Custom template HTML |

## Field Type Reference

> Reconciled against `topics_group-describe` on 2026-08-27. `topics_group-describe` is the live primary source for which types exist and which per-type parameters they accept — call it when in doubt.

| ext_type | type | Description |
|----------|------|-------------|
| 0 | `text` | Single-line text input |
| 1 | `textarea` | Multi-line text area |
| 2 | `select` | Select box (single choice) |
| 4 | `image` | Image upload |
| 5 | `checkbox` | Checkbox (multiple choice) |
| 6 | `wysiwyg` | WYSIWYG rich text editor |
| 7 | `link` | URL link input |
| 8 | `date` | Date/datetime picker |
| 9 | `file` | File upload |
| 10 | `table` | Table input |
| 11 | `location` | Geolocation (map) |
| 13 | `textauto` | Autocomplete text |
| 20 | `relation` | Relation (reference to other records) |
| 21 | `html` | HTML code input |
| 27 | `s3file` | Amazon S3 file upload — **not listed by `topics_group-describe`; MCP creation unverified** |
| 28 | `json` | JSON data input |
| 29 | `csvtable` | CSV table |
| 30 | `filemanager` | File manager |
| 31 | `vimeo` | Vimeo video upload — **not listed by `topics_group-describe`; MCP creation unverified** |
| 32 | `api` | External API integration |
| 33 | `gcsfile` | Google Cloud Storage file upload — **not listed by `topics_group-describe`; MCP creation unverified** |
| 34 | `counter` | Auto-increment counter |
| 35 | `number` | Numeric input |
| 36 | `bool` | Boolean (ON/OFF toggle) |
| 37 | `csvtable_checkbox` | CSV table checkbox |
| 38 | `block_editor` | Block-based content editor — **only as the first field of a field group** |

Per-type properties (`placeholder`, `options`, `module`, `csv_master_id`, …), the repeatable-group example, and three complete payloads (news / product catalog / events) are in **[references/field-types.md](references/field-types.md)** — read the section for each type you are about to use before building the `fields` array.

## Field Groups (Repeatable)

Field groups allow you to bundle multiple fields into a repeatable section.

### Group Structure

```json
{
  "group_nm": "Group Name (required)",
  "group_slug": "group-slug",
  "group_repetitions": 5,
  "fields": [
    // Fields inside the group (each field must have repetitions: 1)
  ]
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_nm` | string | Yes | Group display name |
| `group_slug` | string | No | Group slug for API |
| `group_repetitions` | number | No | Number of allowed repetitions (default: 1, minimum: 1) |
| `fields` | array | Yes | Array of fields in the group (minimum 1) |

**Important**: Fields inside a group must have `repetitions: 1`.

**Site-wide ceiling**: the maximum `group_repetitions` a site allows is reported by `whoami`'s `site.limits.topics_ext_group_loop` (`{current, max}`, `max` is 99). Don't assume a number — check `whoami` before setting a large `group_repetitions`. `current` is raisable up to `max` via `admin_setting-update` (see `/kuroco-admin-mcp`).

## Adding fields to an existing definition

Use `topics_group-update` with `topics_group_id`. Its semantics (from the tool schema):

- **Resolve the target first**: get `topics_group_id` from `topics_group-list` (`{}` — fetch all and match `group_nm` locally; check its `inputSchema` for a name filter) — never guess it; if several definitions match, list them and let the user choose. Then `topics_group-get` the definition and keep the `formData` as a before-snapshot.
- **Re-check the ceiling**: existing field count + new fields must stay within `whoami` → `site.limits.topics_max_extension.current` (raise via `admin_setting-update` if `current < max`).
- **Partial update**: any top-level column you omit is back-filled from the current row, so send only what changes (e.g. just `secure_level`, or just `fields`). To clear a value, send it explicitly empty (`""` / `0` / `[]`).
- **`fields` adds, never removes**: entries in `fields` are appended as new fields; existing fields you do not mention are preserved as-is. This endpoint cannot delete or reorder existing fields — tell the user when a request needs that.
- Before adding, call `topics_group-get` and check the existing `ext_slug`s so the new slug does not collide, then read back after the write as in [Verifying the result](#verifying-the-result). New fields get new suffixes `<n>` — find them by matching `ext_slug_<n>` to the slugs you sent, and confirm every other `<n>` is identical to the before-snapshot.
- `file_size` must be within the site's `MAX_FILE_SIZE`; that value is not exposed by `whoami`, so a too-large value surfaces as a tool error or a clamped read-back — check the read-back.
- **`required: true` on a new field affects existing records**: their next edit fails validation until the field is filled. Ask before making an added field required.
- A definition has no approval/draft workflow of its own: the update applies immediately. `need_application_groups` / `can_save_draft_groups` govern the *content records*, not the definition.

## Important Notes

- `ext_type` is what determines the field type. If you also send `type`, it must be the matching pair (see the Field Type Reference table); omitting `type` is fine
- `select` and `checkbox` types **require** `options` (at least one option)
- A request about **who can see or edit the content** is a container parameter, not a field → [Content Definition Parameters](#content-definition-parameters)
- **Read the record back after every write** and confirm the fields were stored → [Verifying the result](#verifying-the-result)
- `relation` type **requires** `module`
- `api` type **requires** `api_settings`
- Fields inside field groups must have `repetitions: 1`
- `name` (content structure name) and each field's `ext_title` cannot be empty strings
- `ext_slug` / `group_slug` may contain only `[a-zA-Z0-9_-]` and must not be a reserved name — the tool rejects them. The complete list is in [references/field-types.md › Reserved slug names](references/field-types.md#reserved-slug-names); check it before proposing slugs (e.g. `description`, `title`, `price` are fine; `subject`, `tags`, `keyword`, `contents` are not)

## 関連スキル

| スキル | 役割 |
|--------|------|
| `/kuroco-admin-mcp` | Admin MCP の接続・OAuth・スコープ、`whoami` の `site.limits` と `admin_setting-update` による上限引き上げ、ツール名の確認 |
| `/kuroco-api-content` | フィールド型別の API レスポンス形、`:R()` 検索構文、閲覧/編集制限の優先順序、コンテンツ CRUD |
| `/kuroco-server-processing` | リレーション先の全データ取得（エンドポイント後処理のカスタム関数）、外部連携 |
| `/kuroco-app-builder` | アプリ構築全体のフェーズ2で本スキルを使う |
| `/kuroco-auth-design` | 「自分の投稿だけ見せる」等のアクセススコープの設計判断（`self_only` の実装は本スキル） |
