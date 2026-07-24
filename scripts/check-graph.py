#!/usr/bin/env python3
"""wiki のリンクグラフ検査: Obsidian の解決規則 (ファイル名 or aliases の
大文字小文字non区別・完全一致) で、孤立ノードと未解決リンクを検出する。
実行: リポジトリルートで python3 scripts/check-graph.py"""
import os, re, glob, sys

wiki_files = sorted(glob.glob('wiki/**/*.md', recursive=True))
raw_files = sorted(glob.glob('raw/**/*.md', recursive=True))

resolve = {}  # lowercase name -> path
for f in wiki_files + raw_files:
    stem = os.path.splitext(os.path.basename(f))[0]
    resolve[stem.lower()] = f
    c = open(f).read()
    m = re.search(r'^aliases: \[(.*)\]$', c, re.M)
    if m:
        for a in m.group(1).split(','):
            a = a.strip()
            if a:
                resolve[a.lower()] = f

incoming = {f: 0 for f in wiki_files}
unresolved = []
for f in wiki_files + raw_files:
    for l in re.findall(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]', open(f).read()):
        l = l.strip()
        t = resolve.get(l.lower()) or resolve.get(os.path.basename(l).lower().removesuffix('.md').removesuffix('.csv'))
        if t:
            if t in incoming:
                incoming[t] += 1
        elif not l.endswith('.csv') and not l.endswith('.html') and f.startswith('wiki/'):
            # raw/ は不変ソース層のため未解決リンクの修正対象外 (記法例などが含まれる)
            unresolved.append((f, l))

orphans = [f for f, c in incoming.items() if c == 0 and 'index' not in f]
print(f"nodes={len(wiki_files)} (wiki) + {len(raw_files)} (raw)")
print(f"孤立ノード (wiki 内・被リンク0): {len(orphans)}")
for f in orphans:
    print("  -", f)
print(f"未解決リンク: {len(unresolved)}")
for f, l in unresolved:
    print(f"  - {f}: [[{l}]]")
sys.exit(1 if orphans or unresolved else 0)
