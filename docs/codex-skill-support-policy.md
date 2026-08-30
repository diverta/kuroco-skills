# Codex 対応方針

## 目的

Kuroco Skills の既存スキルを Claude Code と Codex の双方から利用できるようにする。製品ごとに同じ内容を複製せず、`skills/` を唯一の正本として保守する。

## ディレクトリと命名

- 既存の `skills/<skill-name>/` を共有スキルの正本とする。
- Codex がリポジトリスキルを検出できるよう、`.agents/skills/kuroco-<skill-name>` から正本へ相対シンボリックリンクを張る。
- リンク名は各 `SKILL.md` の frontmatter にある `name` と一致させる。
- Codex 専用の複製スキルや、ファイル名末尾が `-codex.md` のスキルは作らない。

## Codex 用メタデータ

- 各共有スキルに `agents/openai.yaml` を置く。
- `default_prompt` では `$kuroco-<skill-name>` を明示する。
- `agents/openai.yaml` は Codex の表示・呼び出し用メタデータであり、共有の作業手順は `SKILL.md` に置く。
- Claude Code 向け ZIP には `agents/openai.yaml` を含めない。Claude Code のスキル動作は `SKILL.md` を基準に回帰確認する。

## フロントエンドの公開先

公開先の判断ルールと比較の観点は `skills/frontend-integration/SKILL.md` の「公開先の決定」を正本とし、
この方針docには複製しない（複製すると片方だけ更新されて乖離するため）。

- 既定の公開先は KurocoFront。クライアントによらず、ユーザーの指定がない限り KurocoFront を使う。
- Codex 実行時の新規構築でのみ、Codex Sites という選択肢の提示を許す。
- 公開先固有の詳細は `references/kuroco-front.md` / `references/other-hosting.md` に分離する。

## パスの可搬性

- スキル内のファイルは、その `SKILL.md` があるディレクトリからの相対位置で参照する。
- `${CLAUDE_SKILL_DIR}` など特定クライアントだけが提供する変数に依存しない。
- シンボリックリンク経由でも、単体 ZIP で展開しても同じ参照が成立する構成にする。

## 検証方針

- 全 `SKILL.md` をスキル validator で検証する。
- `.agents/skills/` の全リンクが存在し、正本を解決できることを検証する。
- 全 `agents/openai.yaml` の必須表示項目と `$skill-name` を検証する。
- Claude Code の plugin validator と ZIP 生成を検証する。
- Claude Code 向け ZIP に `agents/openai.yaml` が含まれないことを検証する。
- 「公開先の決定」の記述が `SKILL.md` にのみ存在し、この方針docや各 reference に複製されていないことを確認する。
