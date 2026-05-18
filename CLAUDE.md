# Lifting Lab — Personal Strength & Hypertrophy Wiki

## 私について

- **トレーニング歴**: 出戻り・再開組
- **アプローチ**: エビデンスベース（研究 > 経験則）
- **言語**: 日本語メインだが、英文ソース（論文・MASS）も読む
- **目的**: 安全に・着実に・科学的根拠を持って身体を作り直す

## 出戻り組として特に注意すべき前提

出戻りトレーニーは「筋力・筋量の回復は早い」が「結合組織の回復は遅い」非対称性がある。
このWikiでは以下を常に意識する：

- **muscle memory** の文献は重要
- **detraining → retraining** の生理学
- 怪我リスクが新規より高い（自信過剰 + 結合組織未回復）
- 「昔できた重量」のアンカリングバイアスへの対策

## 3層アーキテクチャ

### Layer 1: raw/ — 不変ソース（LLMは読むだけ、書かない）

- `raw/papers/` — PubMed論文、PDF
- `raw/mass/` — MASS Research Review
- `raw/jp-sources/` — 岡田隆、山本義徳等の日本語ソース
- `raw/youtube/` — トランスクリプト（必要時のみ）
- `raw/personal/` — 自分のトレログ、体組成データ（生データ）

### Layer 2: wiki/ — LLM が完全に管理

- `wiki/entities/` — 固有名詞（人物、種目、サプリ、器具）
- `wiki/concepts/` — 抽象概念（ボリューム理論、RIR/RPE、メカニカルテンション等）
- `wiki/protocols/` — 具体的なプログラム（PPL、5x5、Upper/Lower等の比較・解説）
- `wiki/sources/` — 各ソースの構造化サマリ
- `wiki/overviews/` — テーマ横断の俯瞰（例：「胸トレの全体像」）
- `wiki/personal/` — 自分の身体データの分析・トレンド
- `wiki/index.md` — 全ページのカタログ
- `wiki/log.md` — 追記専用の活動ログ

### Layer 3: このファイル（CLAUDE.md）

## ページのフロントマター規約

```yaml
---
type: entity | concept | protocol | source | overview | personal
tags: [#hypertrophy, #strength, #nutrition, ...]
created: 2026-05-18
last_updated: 2026-05-18
sources: [[Source Page 1]], [[Source Page 2]]
confidence: high | medium | low | contested
---
```

- **confidence** が contested の場合、必ず両論併記すること
- 出戻り組に特に関係する話題には `#returning-lifter` タグを付ける

## エビデンス階層（情報の信頼度ランキング）

ソースの信頼度を以下の階層で扱う。矛盾する情報があれば上位を優先：

1. **メタアナリシス・システマティックレビュー**（特に Schoenfeld, Helms, Krieger 等）
2. **MASS Research Review**（査読論文の解説）
3. **オリジナル研究論文**（PubMed）
4. **山本義徳・岡田隆など、科学的バックグラウンドのある日本人実践家**
5. **Renaissance Periodization, Jeff Nippard など海外の evidence-based 系**
6. **Reddit, YouTube, Twitter** — 仮説や問題提起としては使うが、主張の根拠にはしない

## Wikilink 規約

- 種目名: `[[Bench Press]]`（英語名を canonical とする、`[[ベンチプレス|和名表示]]` で日本語表記可）
- 人物: `[[Brad Schoenfeld]]`, `[[山本義徳]]`
- 概念: `[[Mechanical Tension]]`, `[[Volume Landmarks]]`
- プログラム: `[[PPL Split]]`, `[[5x5 Program]]`

## オペレーション

### /ingest — 新しいソースを wiki に統合

1. raw/ にあるソースを読む
2. 以下を抽出：
   - 主要 entity（人物、種目、サプリ、器具）
   - 主要 concept（用語、理論、メカニズム）
   - 数値・推奨値（ボリューム、頻度、強度等）
3. 既存ページがあれば更新、なければ新規作成
4. **矛盾チェック**：既存の wiki と内容がぶつかる場合は、両方の主張を併記して `confidence: contested` を付ける
5. wiki/sources/ にソースサマリページを作成
6. wiki/index.md と wiki/log.md を更新
7. 出戻り組視点で特筆すべき点があれば `## 出戻り組への示唆` セクションを追加

### /query — Wiki に質問

1. wiki/index.md を読んで関連ページを特定
2. 関連ページを読んで回答を合成
3. 引用元の [[wikilink]] を必ず含める
4. 重要な query の回答は wiki/overviews/ に新規ページとして保存
5. 出戻り組の私に特に関係する論点を最後に必ず明示

### /lint — 健康診断

以下を検出：

- オーファンページ（リンクされていないページ）
- 矛盾している記述（同概念で異なる主張）
- 古いソースで上書きされるべき stale claim
- 自分のページを持つべきなのに持っていない重要概念
- 不足しているクロスリファレンス
- Web 検索で埋められそうな知識の穴
- `confidence: contested` のページで未解決のもの

### /log-workout — トレーニング記録（カスタム、後述）

## 私への原則

1. **保守的に答えること**：出戻り組の自信過剰を諫める方向で
2. **「諸説あり」を明示すること**：筋トレ界の論争は多い（高ボリューム vs 低ボリューム、頻度論等）
3. **個別最適化を意識**：論文の平均値と個人差を分けて伝える
4. **過去の自分の重量を引き合いに出さない**：アンカリングバイアスを避ける
5. **怪我リスクのある話題は必ずフラグ**：「これは怪我リスクが高い」を明示

## このCLAUDE.mdの進化

私との対話で得た学びは、このファイル自体に書き戻す。
特に「私はこういう書き方が好き」「この種目はこう呼んでほしい」等の好みは
`## 私の好み` セクションに追記すること（後日追加予定）。
