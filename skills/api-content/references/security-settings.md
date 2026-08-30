# Kuroco APIセキュリティ設定 詳細リファレンス

このドキュメントは `kuroco-api-content` スキルのセキュリティセクションの補足資料です。
Kuroco公式ドキュメントから抽出・整理した情報に基づいています。

---

## 1. 認証方式の詳細

管理画面: [API] → [セキュリティ] で設定します。

### 選択肢一覧

| 認証方式 | 用途 | 特徴 |
|---------|------|------|
| なし | 公開データ専用API | トークンなしでアクセス可能。公開コンテンツのみを返すAPIならキャッシュと併用して選択可。非公開データ・書き込み系には使わない |
| 静的アクセストークン（StaticToken） | サーバー間通信、公開API | 固定トークン。流出リスクがあるため更新運用を想定すること |
| 動的アクセストークン（DynamicToken） | ログイン必須サイト | JWT。ログイン毎にワンタイムトークンを動的生成 |
| Cookie | ログイン必須Webサイト | セッションベース。サードパーティCookie規制への対応が必要 |
| 特権付き静的アクセストークン（PrivilegedStaticToken） | 管理ツール・サーバ間の書き込み | 固定トークンだが**発行元メンバーの権限をリクエスト毎に持つ**ため、実質「無期限のログイン済み資格情報」になる。ブラウザや公開リポジトリに置かない |

### 動的アクセストークンの前提条件

- ユーザーが1人以上登録されていること
- 必須エンドポイントの作成:
  - `Login(v1)::login_challenge` (ログイン)
  - `Login(v1)::token` (トークン取得)
- フロントエンドでのトークンマネジメント実装
- **注意**: トークン認証APIが複数ある場合、各API間で認証状態は**共有されない**

### Cookie認証の前提条件

- ユーザーが1人以上登録されていること
- 必須エンドポイント: `Login(v1)::login_challenge`
- フロントとKurocoのドメインを合わせる必要がある（ファーストパーティCookie化）
- **注意**: Cookie認証APIが複数ある場合、各API間で認証状態が**共有される**

### リクエストヘッダーの指定

```
# 静的トークン / 動的トークン共通
X-RCMS-API-ACCESS-TOKEN: {トークン値}
```

---

## 2. IPアドレス制限

管理画面: [API] → [セキュリティ] → [IPアドレス制限]

指定されたIPアドレスからのアクセスのみ許可する機能です。

### 指定形式

| 形式 | 例 | 説明 |
|------|-----|------|
| 個別IP | `192.0.2.1` | 単一IPアドレス |
| CIDR | `192.0.2.0/24` | サブネット単位（この例では192.0.2.0〜192.0.2.255） |
| 範囲指定 | `192.0.2.1-192.0.2.2` | ハイフンによるIP範囲指定 |

### IPアドレスグループ（IPSETS）

複数のIPアドレスをまとめて管理するには、定数機能を利用します。

1. 管理画面: [環境設定] → [定数] で `IPSETS_*` の名前で定数を作成
2. 改行区切りでIPアドレスを入力（`#コメント` 形式でメモ可）
3. IPアドレス制限欄に `[[IPSETS_*]]` と入力して参照

```
# 定数設定例（名前: IPSETS_OFFICE）
192.0.2.1       #東京オフィス
192.0.2.10      #大阪オフィス
10.0.0.0/8      #VPN
```

### 参考ドキュメント
- `../../kuroco-docs/docs/management-api.md`（`api-security`） - IPアドレス制限の設定画面
- `../../kuroco-docs/docs/faq-domain.md`（`is-it-possible-to-set-multiple-ip-addresses-at-once`） - IPSETS機能

---

## 3. APIリクエスト制限（エンドポイント単位）

管理画面: [API] → エンドポイント設定 → [APIリクエスト制限]

| 制限タイプ | 説明 |
|----------|------|
| None | 制限なし。認証不要のエンドポイント向け |
| GroupAuth | ログインユーザーの**グループ権限**をチェックし、合致した場合のみリクエストを許可 |
| MemberCustomSearchAuth | ログインユーザーが**カスタムメンバーフィルター**の検索条件に合致する場合のみリクエストを許可 |

### GroupAuth
- メンバーが所属するグループに基づいてアクセス制御
- グループ設定: 管理画面 → [メンバー管理] → [グループ]

### MemberCustomSearchAuth
- カスタムメンバーフィルターで定義した複合条件でアクセス制御
- 条件例: 登録日、グループ、都道府県、カスタム項目など
- フィルター設定: 管理画面 → [メンバー管理] → [カスタムメンバーフィルター]
- フィルターの「権限設定への利用」を有効にする必要がある

### 参考ドキュメント
- `../../kuroco-docs/docs/reference-api-2.md`（`endpoint-settings`） - APIリクエスト制限の項目説明
- `../../kuroco-docs/docs/tutorials-auth-member-4.md`（`using-custom-member-filters`） - カスタムメンバーフィルターの使い方

---

## 4. 閲覧制限の優先順序

コンテンツを返すAPIでは、以下の順序で閲覧制限が評価されます（上位が優先）:

1. **API → セキュリティ → IPアドレス制限** (API全体)
2. **API → エンドポイント設定 → APIリクエスト制限** (エンドポイント単位)
3. **コンテンツ定義 → APIリクエスト制限** (コンテンツ定義単位)
4. **コンテンツカテゴリ → APIリクエスト制限** (カテゴリ単位)
5. **個別コンテンツ → APIリクエスト制限** (コンテンツ単位)

上位レベルで拒否されると、下位レベルの設定に関わらずアクセスは拒否されます。

### 参考ドキュメント
- `../../kuroco-docs/docs/faq-member.md`（`in-what-order-are-viewing-restrictions-applied`）

---

## 5. CORS設定

管理画面: [API] → [セキュリティ] → [CORS]

| 項目 | 対応ヘッダー | 説明 | 設定例 |
|------|------------|------|--------|
| CORS_ALLOW_ORIGINS | Access-Control-Allow-Origin | 許可するオリジン（複数設定可） | `http://localhost:3000`, `https://your-site.com` |
| CORS_ALLOW_METHODS | Access-Control-Allow-Methods | 許可するHTTPメソッド | `GET`, `POST`, `OPTIONS` |
| CORS_ALLOW_HEADERS | Access-Control-Allow-Headers | 許可するリクエストヘッダー | `*` |
| CORS_MAX_AGE | Access-Control-Max-Age | プリフライトのキャッシュ秒数 | `600` |
| CORS_ALLOW_CREDENTIALS | Access-Control-Allow-Credentials | Cookie送信の許可 | `true` |

### 重要な注意点

- **ワイルドカード(`*`)をORIGINSに使用しないこと**: CSRF攻撃への防御効果がなくなる
- CORS設定はContent-Security-Policyの`frame-ancestors`にも反映される
- CORS変更後の反映遅延: `CORS_MAX_AGE`で指定された秒数だけブラウザにキャッシュされる。即時反映するにはブラウザキャッシュクリアまたは`CORS_MAX_AGE`を`0`に設定
- Cookie認証では`CORS_ALLOW_CREDENTIALS`を有効にし、フロントエンドで`credentials: 'include'`を指定

### CSRF対策との関係

KurocoではCORS + `Content-Type: application/json` の組み合わせにより、モダンブラウザにおけるCSRF攻撃を防御:
1. `Content-Type: application/json` はブラウザのプリフライトリクエストを発生させる
2. プリフライトでCORS設定がチェックされ、未許可オリジンはブロック
3. HTMLフォームでは `application/json` を送信できないため、攻撃者はバイパス不可

### 参考ドキュメント
- `../../kuroco-docs/docs/management-api.md`（`api-list`） - CORS設定テーブル
- https://kuroco.app/ja/docs/faq/cors-and-content-type-prevent-csrf-attacks/ - CSRF対策の詳細
- `../../kuroco-docs/docs/faq-api-error.md`（`i-changed-cors-but-it-is-not-reflected`） - CORS変更の反映遅延

---

## 6. 後処理によるレスポンス制限

管理画面: [API] → エンドポイント一覧 → [後処理]

APIのレスポンスから不要なフィールドを除外し、公開情報を制限する機能です。

### 出力許可リスト（ホワイトリスト）

指定したフィールドのみレスポンスに含めるフィルター:

```
# 設定例: list内のsubjectとcontents、pageInfoのみ返す
list.subject
list.contents
pageInfo
```

- ネストはドット(`.`)区切りで指定
- 配列のインデックス指定は不要（自動処理）
- パフォーマンス向上のため、カスタム処理の前に配置することを推奨

### 出力変換リスト

フィールドの削除・名称変更・変換関数の適用:
- 利用可能関数: Truncate, Trim, Strtotime, Date Format, Uppercase, Lowercase, Sprintf, Nl2br, FileSize, ImageSize

### カスタム処理

Smartyテンプレートでのカスタムロジック適用（`$json` → `$processed_json`）

### 参考ドキュメント
- `../../kuroco-docs/docs/management-api.md`（`api-postprocessing`） - 後処理の設定画面
- `../../kuroco-docs/docs/reference-smarty-trigger-1.md`（`post-processing`） - 後処理の詳細リファレンス

---

## 7. プラットフォームセキュリティ

Kurocoプラットフォーム自体が提供するセキュリティ機能:

### API
| 機能 | 説明 |
|------|------|
| HTTPS | 全通信を暗号化 |
| TLS証明書 | SSL/TLS証明書の自動管理 |
| WAF | Webアプリケーションファイアウォール |
| CDN | コンテンツ配信ネットワーク |
| DDoS対策 | 分散型サービス拒否攻撃への対策 |
| Fastly DDoS Protection | オプションで高度なDDoS保護 |
| アクセスログ/監査ログ | リクエストの記録・追跡 |
| SAML/OAuth連携 | 外部IdP経由のログイン |
| クライアント証明書 | オプションでのmTLS認証 |

### データセンター
- Google Cloud Platform（東京/EU/USリージョン選択可）
- プライベートクラウド版も対応

### セキュリティ認証
- ISMS (ISO/IEC 27001:2022)
- ISMSクラウド (ISO/IEC 27017:2015)
- プライバシーマーク
- Assuredセキュリティ評価: **96.6/100**（全体上位5%）

### 脆弱性診断
- コンテナ更新毎の脆弱性スキャン（ほぼ毎日）
- VADDY連携による自動脆弱性診断（管理画面から申込可）

### 参考ドキュメント
- `../../kuroco-docs/docs/about.md`（`security`） - セキュリティ概要

---

## 8. 403 Forbiddenエラーのトラブルシューティング

APIから403エラーが返される場合のチェックリスト:

**まず切り分ける**: 認証（ログイン・トークン）が通っていても、権限が無ければ `403` になる。
ログインが成功し `X-RCMS-API-ACCESS-TOKEN` が有効なのに `403` なら、原因は認証側ではなく**権限側**。
認証方式（Cookie / 動的アクセストークン）を変えてもこの `403` は直らない。

1. **IP制限の確認**: API → セキュリティ → IPアドレス制限にアクセス元IPが含まれているか
2. **エンドポイントの認証要件**: Topics::insertなど、一部エンドポイントはログイン状態が前提
3. **APIリクエスト制限**: GroupAuthまたはMemberCustomSearchAuthで拒否されていないか
4. **コンテンツ定義（Topics Group）のグループ権限**: **操作ごとに別の設定**なので、失敗している操作に対応するものを見る
   - 参照（list / details）で403 → `secure_level` にログイン中の会員のグループが含まれているか
   - 追加・更新・削除（insert / update / delete）で403 → `writer_groups` に含まれているか
   - 参照は通るのに登録だけ403、という形で出るのが典型。`secure_level` だけ設定して `writer_groups` を忘れているケース
   - どちらも空なら制限なし（＝全体に許可）。「未設定」と「全体公開」が同じ状態になる点に注意
5. **CORS設定**: フロントエンドのオリジンが`CORS_ALLOW_ORIGINS`に登録されているか

### ログイン必須エンドポイントの回避策

セキュリティ上ログイン必須のエンドポイントをパブリックに使用したい場合:
- **api_internal プラグイン**: カスタム処理で `member_id` を指定してリクエスト
- **前処理でのログイン注入**: `{login member_id=1 overwrite=false}` をエンドポイントの前処理に設定

### 参考ドキュメント
- `../../kuroco-docs/docs/faq-api-error.md`（`the-api-returns-403-forbidden-even-though-no-restrictions-are-applied`）

---

## 9. Admin MCPによる設定変更

APIのセキュリティ設定（認証方式・IPアドレス制限・CORS）は管理画面だけでなく、**Admin MCP経由でも変更できます**。
`rcms_api` モジュールのAPI定義更新ツール（`UPSERT_API` 相当）が `security` / `ip_whitelist` / `cors` を引数に取ります。

**正確なツール名と引数は必ず `tools/list` で確認してください**（名前を推測して呼ばない）。接続手順は `/kuroco-admin-mcp` を参照。

### 変更時の副作用（実行前に必ずユーザーへ伝える）

| 変更 | 副作用 |
|------|--------|
| **セキュリティ種別の変更** | そのAPIで**発行済みのトークンがすべて無効化される**。稼働中のフロントエンド・バッチが即座に401になる |
| **`dynamic_token` への切り替え** | 動的トークンの発行には `Login::token` エンドポイントが必要。**存在しなくても警告が返るだけで変更自体は成功する**ため、切り替え前にエンドポイントを作成しておく |
| **`ip_whitelist`** | **引数を省略すると現状維持、明示的に空配列を渡すとIP制限が解除される。** 結果が空になる場合と `/0`（全開放）を含む場合は警告が返る |
| **`cors`** | 現在のCORS設定への**浅いマージ**（渡さなかったキーは変更されない）。ブラウザのプリフライトを通すには `methods` に `OPTIONS` を含める |

`static_token` / `privileged_static_token` の**トークン本体はこのツールでは発行されません**。
セキュリティ種別を設定したうえで、別途トークン生成ツール（`mcp:admin` スコープ必須）で発行します。

### 関連スキル

- `/kuroco-admin-mcp` — 接続・認証・スコープ設計、ツールの命名規則と探索方法
- `/kuroco-security-audit` — 読み取り専用スコープでの設定値の一括点検・診断
