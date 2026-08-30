# KurocoFront

Kurocoが提供するフロントエンドホスティング（静的ホスティング + CDN）。本スキルの既定の公開先。
公開先の決め方は [SKILL.md「公開先の決定」](../SKILL.md#公開先の決定) を参照。

## 適する用途

- 継続運用する公開サイト・Webアプリ
- Kuroco API・会員認証・フォーム送信を本番接続するサイト
- 独自ドメイン、CDN、IPアドレス制限・Basic認証、継続的デプロイが必要なサイト

## 設定（kuroco_front.json）

利用するには `kuroco_front.json` をビルド出力のルートに配置する（Nuxt 3・Next.js・Viteは `public/`、Nuxt 2は `static/` 配下に置くとビルド時にルートへコピーされる）。このファイル自体は公開されない。

```json
// kuroco_front.json（SPA配信の例）
{
  "rewrites": [
    { "source": ".*", "destination": "/index.html" }
  ],
  "redirects": [],
  "basic": [],
  "ip_restrictions": []
}
```

`rewrites` のほかBasic認証・IPアドレス制限も設定可能（Basic認証のパスワードはプレーンテキストのため、公開リポジトリでは注意）。

**JSONが壊れている・ファイルが見つからない場合は `404 Not Found (CONFIG FILE NOT FOUND)`** になる。
サイト全体が404になったら、まずこのファイルの存在と構文を疑う。

### 使えるキー

**キー名を間違えてもエラーにならない。** 綴り違いや、他サービス（Vercel・Netlify 等）の設定名を
そのまま持ち込んだ場合、警告も出ずに無視されるだけなので、**設定したつもりで一切効いていない**状態になる。
キー名は下の表と突き合わせ、デプロイ前に[検査](#デプロイ前に検査するkurocofront-validate_config)する。

| キー | 内容 |
|------|------|
| `rewrites` | URLリライト（URLは変えない） |
| `redirects` | リダイレクト（URLが変わる。`status:302:` / `status:404` の指定可） |
| `redirects_by_ie` | UserAgentに `MSIE` / `Trident` を含む場合だけのリダイレクト |
| `basic` | Basic認証（`"id:password"` の配列） |
| `ip_restrictions` | IPアドレス制限（CIDR可） |
| `ip_restricted_maintenance` | 指定IP以外にメンテナンスページを表示 |
| `error_page` | エラーページ（`status404` / `status403` / `status401` / `status_ip_503`） |
| `stale_while_revalidate` | 失効済みコンテンツをCDNから配信する秒数。**数値ではなく文字列で書く**（`"86400"`） |

各キーの項目仕様は `/kuroco-docs` の FAQ「kuroco_front.jsonとは何ですか？」が正。

### デプロイ前に検査する（`kuroco_front-validate_config`）

`kuroco_front-deploy` は zip を受け取ってキューに積むだけで、**中の `kuroco_front.json` は誰も検査しない**。
そのため次の2つは無警告で起きる:

- **未知キー・型違いは黙って無視される** — 設定は効かないが signal も出ない
- **JSONとして読めないファイルをデプロイすると、そのデプロイは反映されず前バージョンが配信され続ける** — サイトは正常に見えるので気づけない

デプロイ前に `kuroco_front-validate_config`（MCP）/ `KurocoFront::validate_config`（REST v1）で検査する。

- **入力はファイルの「テキスト」**。パース済みのオブジェクトを渡すと、いちばん影響が大きい構文エラーを検出できない
- 戻り値
  - `valid` — 読めて、かつ無視される箇所が無いか
  - `error` — `json-parse-error` / `empty-content` / `content-too-large`
  - `warnings` — 無視される箇所。`<target>:<reason>` 形式で、配信側が返す `X-Kuroco-Config-Warning` ヘッダーと**同じ語彙**なので突き合わせられる
  - `notes` — 一部の配信経路でしか効かないキーへの注記。実装されている経路では正しい設定なので警告とは別扱い
  - `valid_keys` — 受け付けるキーの一覧。キー名のタイポの確認に使う
- ツールが一覧に見えない場合は annotation キャッシュのパージ（`api-annotation_cache_purge`）が必要。**全 API エンドポイントの CDN キャッシュも同時に破棄される**ので、本番サイトでは実行タイミングに注意する

検査で拾える代表的な設定ミスと、放置したときに配信時に起きること:

| 設定ミス | 配信時に起きること |
|---------|-----------------|
| 未知のキー | 無視される（設定したつもりで効いていない） |
| `source` が正規表現として不正 | `500 Please check kuroco_front.json` |
| 不正なCIDR（`ip_restrictions` 等） | レンジ判定が例外になり `500` |
| `basic` の要素にコロンが無い | **誰も認証を通れなくなる** |
| `error_page` のパスが `/` 始まりでない | エラーページが出ない |
| `stale_while_revalidate` をJSONの数値で書く | 文字列長で判定されるため**無視される** |

## SPA配信（履歴APIのクライアントルーティング）

Vue Router の `createWebHistory` / React Router の `BrowserRouter` のように History API でURLを書き換える構成では、
**リライトを設定しないとリロード・URL直打ち・共有リンクが404になる**（静的ホスティングは実ファイルを探すため）。
これに必要な設定は次の1ブロックで足りる。

```json
{
  "rewrites": [
    { "source": ".*", "destination": "/index.html" }
  ]
}
```

守るべき点:

- **`source` は必ず `.*`。** リライトが「**ファイルが存在しない場合のみ有効**」になるのは `source` が `.*` のときだけで、
  `^/app/.*` のように絞ると**ファイルの存在を確認せず常にリライトされる**。JS・CSS・画像まで `index.html` に吸われてアプリが起動しなくなる。
  「SPAは `/app` 配下だけだから」とスコープを絞るのが典型的な失敗
- **複数の `rewrites` を書くなら `.*` のフォールバックを最後に置く。** 上から順にチェックされるため、先頭に置くと後続が評価されない
- **`error_page.status404` はSPAでは発火しない。** `.*` のフォールバックがある限り未知のパスも `index.html` を 200 で返すため。
  存在しないページの表示はクライアント側ルーターの404ルートで行う。
  **URLとして本当に404を返したいパスだけ** `redirects` の `destination: "status:404"` で明示する
- リライト（URLは変えない）とリダイレクト（URLが変わる）を混同しない。SPAのフォールバックは必ず `rewrites` 側
- `stale_while_revalidate` はHTTPレスポンス200のときだけ有効。SPAは `index.html` が200で返り続けるので設定が効く。**値は文字列で書く**（`"86400"`。数値で書くと無視される）

SPAを選ぶ前に確認すること:

- **全パスが同じ `index.html` を返すので、ページ個別のOGP・metaを持てない。** 検索流入やSNSシェアが要件なら
  SSG（またはSSR）にする。判断は [SKILL.md「公開先の決定」](../SKILL.md#公開先の決定)
- hashモード（`/#/path`）ならリライトは不要だが、URL共有・SEO・OGPで不利になるので通常は選ばない
- Nuxt などで SSG に切り替えれば、そもそもこの問題は起きない（各パスの実ファイルが生成されるため）

## 非公開デフォルト（新規デプロイの既定）

新規サイトのデプロイは、ユーザーが**公開を明示するまで非公開デフォルト**で行う。プロトタイプや構築途中のサイトが `*.g.kuroco-front.app` でそのまま全公開・クロールされるのを防ぐためで、次の2つを**セットで**設定する:

1. **robots.txt**（クロール避け）: ビルド出力のルートに置く

   ```
   User-agent: *
   Disallow: /
   ```

2. **到達制限**: `kuroco_front.json` の `basic` または `ip_restrictions`。方式は**デプロイ前にユーザーに選択してもらう**:

   | 選択肢 | 設定 | 説明 |
   |--------|------|------|
   | Basic認証・PW `kuroco` | `"basic": ["kuroco:kuroco"]` | 覚えやすいが誰でも推測できるため、強度は robots.txt 相当（誤クロール防止のみ） |
   | **Basic認証・PWランダム生成（推奨）** | `"basic": ["kuroco:<ランダム8文字>"]` | 小文字+数字8文字で生成する。紛らわしい文字（`l` `1` `o` `0`）は使わない。例: `kuroco:mx7kq2ab` |
   | Basic認証・PWユーザー指定 | `"basic": ["kuroco:<指定値>"]` | ユーザーが入力した値をそのまま使う |
   | IPアドレス制限 | `"ip_restrictions": [...]` ＋ **API側のIP制限も同じ範囲で設定** | 毎回の入力が不要な代わりに、スマホ回線・外出先・共有相手のIPで詰まりやすい。許可するIP/CIDRをユーザーに確認する |

運用ルール:

- Basic認証のIDは `kuroco` に固定する（覚えることを減らすため。守りはパスワード側で担う）
- デプロイ完了時に **URL・ID・パスワードの3点セット**をユーザーに提示する（ブラウザが記憶するため入力は実質ブラウザごとに初回のみ）
- パスワードは `kuroco_front.json` に平文で入る（KurocoFrontの仕様）。公開リポジトリには置かない
- Basic認証中は OGPプレビューや Slack / LINE のリンク展開は動かない（公開前なので想定どおりの挙動）
- **IP制限を選んだ場合は、KurocoFrontとAPIの両方に同じ範囲をかける**（フロントだけ塞いでもAPIは直接叩けるため）。API側は管理画面 [API]→[セキュリティ]→[IPアドレス制限] または Admin MCP のAPI設定で行う。適用範囲は次のとおり:
  - **管理画面・Admin MCP には不要**（必ず認証が入るため）
  - **Kuroco Files（ファイル配信）のIP制限は構築時はかけない**
  - API単位のIP制限はクライアントIPごとにキャッシュが分割される点に注意（許可IPが多いとヒット率が落ちる）
- **公開時はセットで外す**: robots.txt の `Disallow: /` を削除し、`basic` / `ip_restrictions` を空に戻して再デプロイする（IP制限を選んでいた場合はAPI側のIP制限も外す）。一部だけ外すと「検索避けだけ残る」「認証だけ残る」の中途半端な状態になる

## デプロイ方法

KurocoFrontへのデプロイは2通りある:

### 方法1: GitHub連携（継続的な運用向け）

管理画面 [KurocoFront] → GitHubリポジトリ連携。push時にGitHub Actionsでビルドされ、成果物（zip）がKurocoFrontへデプロイされる。
手順の詳細は `/kuroco-docs` の `connect-to-github-with-kuroco-front` を参照。

### 方法2: Admin MCPからの直接デプロイ（AIエージェント・ワンショット向け）

GitHubリポジトリなしで、ビルド成果物のzipを直接デプロイできる。Admin MCPの `services` バンドル
（`/x/services` を含むスコープ、または `/x/all`）に以下のツールがある（正確な名前・スキーマは必ず `tools/list` で確認）:

| ツール | 用途 |
|--------|------|
| `kuroco_front-validate_config` | `kuroco_front.json` のデプロイ前検査（未知キー・型違い・無視されるルールの検出） |
| `files-create_temp_upload_url` | zipのアップロード先（プリサインドPUT URL）を発行 |
| `kuroco_front-deploy` | アップロード済みzipをデプロイ（非同期・キュー投入） |
| `kuroco_front-history` | デプロイ履歴の取得・完了確認 |
| `kuroco_front-generate_deploy_token` | CI用の短命Bearerトークン発行（デフォルト30分、最長1時間。`mcp:admin` スコープ必須） |

**デプロイ前の確認（上書き注意）**: 1つのドメインで公開されるのは**現行デプロイ1つだけ**で、
新しいデプロイは既存の公開内容を置き換える。デプロイ前に `kuroco_front-history`（`current_flg: "1"`）で
既存デプロイの有無を確認し、上書きになる場合はユーザーに確認を取る。
確認が取れない場合は `is_preview: true` のプレビューデプロイに留めること。

**手順**:

1. **ビルド**: `nuxt generate` / `vite build` 等。ビルド出力のルートに `kuroco_front.json` があることを確認。
   **`kuroco_front-validate_config` にそのファイルのテキストを渡して検査する**（`valid` が false のまま進めると、設定が黙って無視されるかデプロイが反映されない）
2. **zip化**: ビルド出力ディレクトリの**中身**をzipのルートにする（`cd dist && zip -r ../dist.zip .`）
3. **アップロード先の発行**: `files-create_temp_upload_url` を呼ぶ。`file_size`（バイト数）と `ext: "zip"` の宣言が必須。返却された `presigned_url` にzipの生バイトをPUTする
4. **デプロイ実行**: `kuroco_front-deploy` を呼ぶ。`artifact_url` に手順3のレスポンスの `url`（または `short_url`）を渡す
   - `artifact_url` は **Kuroco Filesストレージ上のURLのみ**受け付ける（第三者ホストのURLは不可）
   - `domain` 省略時はサイト設定から自動解決（`site_url` → `site_url2` → `{site_key}.g.kuroco-front.app` の順）。指定する場合もこのいずれかに一致する必要がある
   - `is_preview: true` を渡すとステージ環境へのプレビューデプロイになり、レスポンスに `stage_url` が返る。**本番反映前にプレビューで確認するのを推奨**
   - `hash` は任意（7文字以上の英数字。省略時は自動生成）
5. **完了確認**: レスポンスは `status: "accepted"`（キュー投入・非同期）。`kuroco_front-history`（`current_flg: "1"` で現行デプロイに絞り込み）で反映を確認する

**必要権限**: `kuroco_front-*` は管理メンバーの `kuroco_front/update` 権限、`files-*` は `files/update` 権限が必要。

**関連ツール**（`site` モジュールスコープ側）:

- `kuroco_front_history-list` — デプロイ履歴の一覧（読み取り）
- `kuroco_front-cdn_cache_purge` — KurocoFront CDN キャッシュのパージ（KurocoFront 配信分のみ。API / KurocoEdge のキャッシュは `api-cdn_cache_purge` / `edge-cdn_cache_purge` が別にある）
- `kuroco_front_token-list` / `kuroco_front_token-create` / `kuroco_front_token-delete` — KurocoFront APIトークン管理

同じ機能はREST APIとしても利用できる（`KurocoFront::deploy` / `KurocoFront::history` モデルをエンドポイント登録）。
CIから定常的にデプロイする場合は GitHub連携、または `client_credentials` クライアント（`/kuroco-admin-mcp` 参照）を使い、
`kuroco_front-generate_deploy_token` の都度発行は単発のデプロイに限る。

## 完了条件

- 実URLで主要経路と、読込中・空・エラー・権限不足の各状態を確認した
- CORSと認証（Cookie または動的アクセストークン）が対象ブラウザで動作する
- 公開範囲、対象Kurocoサイト、使用API、デプロイ方法、残作業を引き渡した
