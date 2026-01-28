#!/bin/bash

# Kurocoドキュメント同期スクリプト
# ZIPファイルをダウンロードしてdocs/に全展開し、詳細なINDEXを自動生成します

set -e

ZIP_URL="https://rcms.g.kuroco-img.app/files/user/skills/current.zip"
PLUGIN_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$PLUGIN_DIR/docs"
TEMP_DIR=$(mktemp -d)
MAX_RETRIES=3
RETRY_DELAY=5

echo "=== Kurocoドキュメント同期開始 ==="
echo "ダウンロードURL: $ZIP_URL"
echo "同期先: $DOCS_DIR"
echo ""

# クリーンアップ関数
cleanup() {
  rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

# リトライ付きダウンロード関数
download_with_retry() {
  local url="$1"
  local output="$2"
  local attempt=1

  while [ $attempt -le $MAX_RETRIES ]; do
    echo "ダウンロード試行 $attempt/$MAX_RETRIES..."

    if curl -fsSL --connect-timeout 30 --max-time 300 "$url" -o "$output" 2>/dev/null; then
      # ファイルサイズチェック
      local size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null || echo "0")
      if [ "$size" -gt 1000 ]; then
        echo "ダウンロード成功 (${size} bytes)"
        return 0
      else
        echo "警告: ファイルサイズが小さすぎます (${size} bytes)"
      fi
    fi

    if [ $attempt -lt $MAX_RETRIES ]; then
      echo "ダウンロード失敗。${RETRY_DELAY}秒後にリトライします..."
      sleep $RETRY_DELAY
    fi

    attempt=$((attempt + 1))
  done

  echo "エラー: ${MAX_RETRIES}回の試行後もダウンロードに失敗しました"
  return 1
}

# ZIPファイルをダウンロード
echo "ZIPファイルをダウンロード中..."
if ! download_with_retry "$ZIP_URL" "$TEMP_DIR/current.zip"; then
  echo ""
  echo "=== エラー ==="
  echo "ドキュメントのダウンロードに失敗しました。"
  echo "以下を確認してください:"
  echo "  - インターネット接続"
  echo "  - URL: $ZIP_URL"
  exit 1
fi

# ZIPファイルの検証
echo "ZIPファイルを検証中..."
if ! unzip -t "$TEMP_DIR/current.zip" > /dev/null 2>&1; then
  echo "エラー: ZIPファイルが破損しています"
  exit 1
fi

echo "ZIPファイルを解凍中..."
unzip -q "$TEMP_DIR/current.zip" -d "$TEMP_DIR/extracted"

# 解凍したディレクトリ構造を確認
EXTRACTED_DIR="$TEMP_DIR/extracted"

# ZIPのルートにcurrentフォルダがある場合
if [ -d "$TEMP_DIR/extracted/current" ]; then
  EXTRACTED_DIR="$TEMP_DIR/extracted/current"
fi

# 既存のdocsフォルダを削除して新規作成
echo "既存のドキュメントをクリア中..."
rm -rf "$DOCS_DIR"
mkdir -p "$DOCS_DIR"

# 全ファイルをコピー
echo "ドキュメントをコピー中..."
cp -r "$EXTRACTED_DIR"/* "$DOCS_DIR/"

# ファイル数をカウント
TOTAL_FILES=$(find "$DOCS_DIR" -type f \( -name "*.md" -o -name "*.mdx" \) | wc -l | tr -d ' ')

# INDEX.mdを生成
echo "INDEX.mdを生成中..."

cat > "$DOCS_DIR/INDEX.md" << 'HEADER'
# Kurocoドキュメント インデックス

このフォルダにはKuroco公式ドキュメントが格納されています。

## クイックリファレンス（目的別）

### API・エンドポイント設定
| ファイル | 説明 |
|----------|------|
| `tutorials/configure-endpoint.md` | エンドポイントの作成・設定方法 |
| `reference/endpoint-settings.md` | エンドポイント設定項目の詳細リファレンス |
| `reference/filter-query.md` | フィルタークエリの書き方 |
| `reference/api-cache.md` | APIキャッシュの設定 |
| `management/api-security.md` | APIセキュリティ（認証方式、CORS等） |
| `management/api-list.md` | API一覧画面の使い方 |

### 認証・ログイン
| ファイル | 説明 |
|----------|------|
| `tutorials/login.md` | ログイン機能の実装 |
| `tutorials/signup.md` | 会員登録の実装 |
| `tutorials/setting-up-registration-form.md` | 登録フォームの設定 |
| `tutorials/how-to-use-password-reminder.md` | パスワードリマインダー |
| `tutorials/implementing-two-step-verification-on-login-form.md` | 二段階認証 |

### フロントエンド統合
| ファイル | 説明 |
|----------|------|
| `tutorials/beginners-guide.md` | Kurocoビギナーズガイド |
| `tutorials/integrate-kuroco-with-nuxt.md` | Nuxt.js/Next.jsでコンテンツ表示 |
| `tutorials/integrate-login.md` | フロントエンドでのログイン実装 |
| `tutorials/vue-nuxt-implementation-precautions.md` | Vue/Nuxt実装の注意点 |
| `tutorials/corporate-sample-site-to-ssg.md` | SSG対応 |

### コンテンツ管理
| ファイル | 説明 |
|----------|------|
| `tutorials/adding-a-topics.md` | コンテンツ定義の作成 |
| `management/content-structure-topics.md` | コンテンツ構造の説明 |
| `management/content-structure-topics-group.md` | コンテンツ定義の設定 |
| `tutorials/bulk-upload-in-csv.md` | CSVでの一括アップロード |
| `reference/uploading-files-using-the-api.md` | APIでのファイルアップロード |

### バッチ処理・自動化
| ファイル | 説明 |
|----------|------|
| `tutorials/how-to-use-batch.md` | バッチ処理の使い方 |
| `reference/smarty-plugin.md` | Smartyプラグイン一覧 |
| `reference/trigger-variables.md` | トリガー変数 |
| `tutorials/auto-run-github-with-contents-update.md` | GitHub Actions連携 |
| `management/function.md` | カスタム処理 |

### 外部サービス連携
| ファイル | 説明 |
|----------|------|
| `tutorials/send-slack-notification-after-a-form-has-been-submitted.md` | Slack通知 |
| `tutorials/how-to-link-sendgrid.md` | SendGrid連携 |
| `tutorials/firebase.md` | Firebase連携 |
| `tutorials/how-to-connect-to-line.md` | LINE連携 |
| `management/stripe.md` | Stripe決済 |

### インフラ・セキュリティ
| ファイル | 説明 |
|----------|------|
| `kuroco_infrastructure.pdf` | Kurocoインフラ概要（GCP、セキュリティ、SLA、バックアップ） |

---

## 検索方法

### Claude CodeのGrepツールを使用（推奨）

```
# キーワードで検索（ファイルパスのみ）
Grep: pattern="エンドポイント" path="docs/"

# 内容も確認
Grep: pattern="エンドポイント" path="docs/" output_mode="content"

# 特定ディレクトリ内を検索
Grep: pattern="ログイン" path="docs/tutorials/"
```

### Bashでの検索

```bash
# キーワードで全文検索（マッチしたファイルパスを表示）
grep -rl 'キーワード' docs/

# キーワードで全文検索（マッチした行も表示）
grep -rn 'キーワード' docs/

# 特定ディレクトリ内を検索
grep -rl 'キーワード' docs/tutorials/

# 複数キーワードでAND検索
grep -rl 'キーワード1' docs/ | xargs grep -l 'キーワード2'

# 大文字小文字を区別しない
grep -rli 'api' docs/
```

---

## ディレクトリ構造

HEADER

# 各ディレクトリの説明と内容を追加
for dir in "$DOCS_DIR"/*/; do
  if [ -d "$dir" ]; then
    dirname=$(basename "$dir")

    # ディレクトリ説明
    case "$dirname" in
      "tutorials")
        echo "### tutorials/ - チュートリアル" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "Kurocoの各機能の使い方をステップバイステップで解説。実装手順、設定方法、サンプルコード付き。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "reference")
        echo "### reference/ - リファレンス" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "API設定項目、Smartyプラグイン、フィルタークエリ、エラーコードなどの技術リファレンス。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "management")
        echo "### management/ - 管理画面ガイド" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "Kuroco管理画面の各機能（コンテンツ、メンバー、API、フォーム等）の詳細説明。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "faq")
        echo "### faq/ - よくある質問" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "よくある質問と回答。トラブル解決のヒント。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "about")
        echo "### about/ - Kurocoについて" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "Kurocoの概要、料金プラン、制限事項、用語集など。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "troubleshooting")
        echo "### troubleshooting/ - トラブルシューティング" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "エラー解決、問題診断のためのガイド。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "update")
        echo "### update/ - アップデート情報" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "リリースノート、新機能、ロードマップ。" >> "$DOCS_DIR/INDEX.md"
        ;;
      "information")
        echo "### information/ - お知らせ" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        echo "Kurocoからの公式お知らせ、メンテナンス情報。" >> "$DOCS_DIR/INDEX.md"
        ;;
      *)
        echo "### $dirname/" >> "$DOCS_DIR/INDEX.md"
        echo "" >> "$DOCS_DIR/INDEX.md"
        ;;
    esac

    echo "" >> "$DOCS_DIR/INDEX.md"
    echo "<details>" >> "$DOCS_DIR/INDEX.md"
    echo "<summary>ファイル一覧を展開</summary>" >> "$DOCS_DIR/INDEX.md"
    echo "" >> "$DOCS_DIR/INDEX.md"

    # ファイル一覧を追加（全件）
    echo "| ファイル | タイトル | 説明 |" >> "$DOCS_DIR/INDEX.md"
    echo "|----------|----------|------|" >> "$DOCS_DIR/INDEX.md"

    for file in "$dir"*.md "$dir"*.mdx; do
      if [ -f "$file" ]; then
        filename=$(basename "$file")

        # タイトルを抽出
        title=$(grep -m1 "^title:" "$file" 2>/dev/null | sed 's/^title:[[:space:]]*//' | sed 's/^"//' | sed 's/"$//' || echo "")
        if [ -z "$title" ]; then
          title=$(grep -m1 "^#[[:space:]]" "$file" 2>/dev/null | sed 's/^#[[:space:]]*//' || echo "-")
        fi
        # タイトルが長すぎる場合は切り詰め
        if [ ${#title} -gt 40 ]; then
          title="${title:0:37}..."
        fi

        # descriptionを抽出
        desc=$(grep -m1 "^description:" "$file" 2>/dev/null | sed 's/^description:[[:space:]]*//' | sed 's/^"//' | sed 's/"$//' || echo "-")
        # 説明が長すぎる場合は切り詰め
        if [ ${#desc} -gt 60 ]; then
          desc="${desc:0:57}..."
        fi

        echo "| $filename | $title | $desc |" >> "$DOCS_DIR/INDEX.md"
      fi
    done

    echo "" >> "$DOCS_DIR/INDEX.md"
    echo "</details>" >> "$DOCS_DIR/INDEX.md"
    echo "" >> "$DOCS_DIR/INDEX.md"
  fi
done

# 同期日時を記録
echo "$(date '+%s')" > "$DOCS_DIR/.last_sync"
echo "$(date '+%Y-%m-%d %H:%M:%S')" >> "$DOCS_DIR/.last_sync"

# フッター追加
cat >> "$DOCS_DIR/INDEX.md" << FOOTER

---

## メタ情報

| 項目 | 値 |
|------|-----|
| 同期日時 | $(date '+%Y-%m-%d %H:%M:%S') |
| ソース | $ZIP_URL |
| 総ファイル数 | $TOTAL_FILES |

**次回同期**: 1ヶ月以上経過したら再同期を推奨
FOOTER

echo ""
echo "=== 同期完了 ==="
echo ""
echo "同期されたドキュメント: $TOTAL_FILES ファイル"
echo ""

# ディレクトリ構造を表示
echo "ディレクトリ構造:"
for dir in "$DOCS_DIR"/*/; do
  if [ -d "$dir" ]; then
    dirname=$(basename "$dir")
    count=$(find "$dir" -type f \( -name "*.md" -o -name "*.mdx" \) 2>/dev/null | wc -l | tr -d ' ')
    echo "  $dirname/: $count ファイル"
  fi
done

echo ""
echo "ソース: $ZIP_URL"
echo "同期日時: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""
echo "INDEX.md が生成されました: $DOCS_DIR/INDEX.md"
