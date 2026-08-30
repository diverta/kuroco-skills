# スキル自動発動（トリガー）テスト仕様

各スキルの `description` が適切に書けているか（＝代表的な質問で正しいスキルが自動発動するか）を検証するテスト。SKILL.md の `description` を変更した際は、このテストで発動挙動が壊れていないことを確認する。

## 背景

AIエージェントはセッション開始時に各スキルの `name` と `description` のみをコンテキストに読み込み、ユーザーの質問に応じてどのスキルを使うかを判断する。つまり **description の書き方がスキル選択の精度を直接決める**。

[Agent Skills公式ベストプラクティス](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)に従い、descriptionは「何をするか＋いつ使うか」を三人称の自然文で書き、そのスキル固有の識別子（ECPoint、llms.txt、CIMDなどの固有名詞）を文中に織り込む。同義語の羅列は不要。

## テスト方法

1. `skills/` 配下の全スキルを一時プロジェクト（`.work/.claude/skills/`）にインストール
2. `cases.json` の各質問をヘッドレスモードで実行:
   ```
   claude -p "<質問>" --output-format stream-json --verbose --max-turns 2 --allowedTools "Skill"
   ```
3. stream-json 出力から **最初に発動した Skill ツール呼び出し**を抽出し、期待値と比較

## 実行方法

```bash
# 全138ケース（8並列、所要15〜20分。136回のclaude呼び出しが発生する点に注意）
python3 tests/skill-trigger/run_tests.py

# 特定ケースのみ（description調整後の確認に）
python3 tests/skill-trigger/run_tests.py --only a19 c03

# 中断後の再開（実行済みケースをスキップ）
python3 tests/skill-trigger/run_tests.py --resume
```

終了コード: 全ケース成功で `0`、失敗ありで `1`。

## ケース構成（cases.json・全138問）

| IDプレフィックス | 対象スキル | 件数 |
|------------------|-----------|------|
| `a*` | api-content | 20 |
| `b*` | app-builder | 9 |
| `s*` | server-processing | 18 |
| `f*` | frontend-integration | 18 |
| `d*` | kuroco-docs | 10 |
| `m*` | admin-mcp | 10 |
| `t*` | content-structure（作成の質問） | 9 |
| `c*` | content-structure（設計の質問） | 6 |
| `u*` | auth-design | 6 |
| `e*` | server-processing（外部連携の方式設計の質問） | 6 |
| `g*` | security-audit | 6 |
| `p*` | api-performance-review | 8 |
| `n*` | 対照（Kuroco無関係の質問。**発動しないこと**が正解） | 10 |

各ケースの形式:

```json
{ "id": "a19", "prompt": "KurocoのECポイントをAPIから付与したい", "expect": ["api-content"] }
```

- `expect` は許容するスキル名（ディレクトリ名）のリスト。境界ケースは複数許容（例: `f11` は frontend-integration / api-content の両方を正解とする）
- `expect: []` は「どのスキルも発動しないこと」を意味する（対照ケース）

## 合否基準と調整方針

- **128問（スキルあり）**: 期待スキルが最初に発動すること
- **対照10問**: いずれのスキルも発動しないこと（過剰発動の検出）
- 失敗した場合は、質問に含まれる固有語が該当スキルの description に含まれているかを確認し、**固有名詞を description に追加**して該当ケースを `--only` で3回程度再実行して安定性を確認する
- 同義語の羅列を復活させるのではなく、失敗の原因になった固有語だけをピンポイントで追加すること

## 注意事項

- LLMの判断に基づくテストのため**非決定的**。単発の失敗は `--only <id>` で複数回再実行して再現性を確認する
- 実行環境のユーザー設定（`~/.claude` のスキルやCLAUDE.md）の影響を受ける可能性がある
- 新機能をスキルに追加した際は、その機能を尋ねる質問をケースに追加すること

## 実施記録

| 日付 | 結果 | 備考 |
|------|------|------|
| 2026-07-21 | 98/100 → 調整後 100/100 | description自然文化の初回検証。ECPoint / llms.txt の固有語欠落を修正（PR #28） |
| 2026-08-27 | 133/138 → 調整後 138/138（再実行3回） | 13→11スキル統合と全 description 圧縮後の回帰。a03（Cookie vs トークン）は auth-design、f15（React で SPA）は app-builder も正解に追加（境界ケース）。d03（用語集はある？）は kuroco-docs の description に「有無の確認」用途を追加。m06 は非決定的（再実行で3/3）。n02 は環境側の postgres-patterns が発動したもので本リポジトリ外 |
