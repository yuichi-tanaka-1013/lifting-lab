#!/usr/bin/env python3
"""vault 全体のリンクグラフ検査 (Obsidian の解決規則で判定)。
検出するもの:
  1. 完全孤立ノード — 次数 (被リンク + 発リンク) が 0 の md ファイル
  2. wiki/ 内の未解決リンク — リンク先が存在しない (raw/ は不変層のため対象外)
実行: リポジトリルートで python3 scripts/check-graph.py
インラインコード (バッククォート) 内の [[...]] はリンクとして数えない。"""
import os, re, glob, sys

EXCLUDE_DIRS = ('.obsidian', '.claude', '.git', 'scripts')
all_md = [f for f in glob.glob('**/*.md', recursive=True)
          if not f.startswith(EXCLUDE_DIRS)]
attachments = [f for f in glob.glob('**/*', recursive=True)
               if not f.startswith(EXCLUDE_DIRS) and os.path.isfile(f)
               and f.endswith(('.csv', '.html', '.pdf', '.png', '.jpg'))]

resolve = {}
for f in all_md + attachments:
    resolve[f.lower()] = f                                   # full path
    resolve[os.path.basename(f).lower()] = f                 # basename with ext
    stem = os.path.splitext(os.path.basename(f))[0]
    resolve.setdefault(stem.lower(), f)                      # basename stem
for f in all_md:
    c = open(f).read()
    m = re.search(r'^aliases: \[(.*)\]$', c, re.M)
    if m:
        for a in m.group(1).split(','):
            a = a.strip()
            if a:
                resolve[a.lower()] = f

def links_of(path):
    c = open(path).read()
    c = re.sub(r'```.*?```', '', c, flags=re.S)   # fenced code blocks
    c = re.sub(r'`[^`\n]*`', '', c)               # inline code
    return [l.strip() for l in re.findall(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]', c)]

degree = {f: 0 for f in all_md}
unresolved = []
for f in all_md:
    for l in links_of(f):
        t = resolve.get(l.lower()) or resolve.get((l + '.md').lower())
        if t:
            degree[f] += 1
            if t in degree:
                degree[t] += 1
        elif f.startswith('wiki/'):
            unresolved.append((f, l))

yaml_errors = []
try:
    import yaml as _yaml
    for f in all_md:
        c = open(f).read()
        if c.startswith('---') and '\n---' in c[3:]:
            fm = c[3:c.index('\n---', 3)]
            try:
                d = _yaml.safe_load(fm)
                al = d.get('aliases') if isinstance(d, dict) else None
                if al is not None and not (isinstance(al, list) and all(isinstance(a, str) for a in al)):
                    yaml_errors.append((f, f'aliases が文字列リストでない: {al!r}'))
            except Exception as e:
                yaml_errors.append((f, str(e).splitlines()[0]))
except ImportError:
    print('(PyYAML なし: frontmatter 検証はスキップ)')

isolated = [f for f, d in degree.items() if d == 0]
print(f"nodes: {len(all_md)} md + {len(attachments)} attachments")
print(f"frontmatter YAML エラー (壊れていると Obsidian が aliases/tags を無視する): {len(yaml_errors)}")
for f, e in yaml_errors:
    print(f"  - {f}: {e}")
print(f"完全孤立ノード (次数0): {len(isolated)}")
for f in sorted(isolated):
    print("  -", f)
print(f"wiki 内の未解決リンク: {len(unresolved)}")
for f, l in unresolved:
    print(f"  - {f}: [[{l}]]")
sys.exit(1 if isolated or unresolved or yaml_errors else 0)
