#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""声线锚点统计 —— 把「锚点表」要的那些数字从作品库台词档里数出来。

用途：写某角色的声线锚点表（自称 / 第二人称 / 句尾字频 / 语气词 / 标点 / 分场景差异）时，
     不靠眼看、不靠模型，一次跑出可回查的计数。只读，不改任何档。

用法：
  python3 voice_anchor_stats.py <角色目录> [--self <自称>] [--you <第二人称候选>] \
                                [--extra <文件> ...] [--top 12] [--json]

输入：归档好的台词档 md（表格 `| 编号 | 原文 | 备注 |`；目录会递归读取，只认带编号行的档）。
  --extra 用来加「非场景档」的锚料：App 信件 md、生日贺图文案里引号内的原话 txt 等，
  单独统计、不混进分场景数字（体裁不同用词常不同，混算会把两套口气拌在一起）。

输出：合计 + 每档分列；结论都要带条号才对得上验收，故同时打印命中条号。
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROW = re.compile(r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*$')
TAIL_PUNCT = r'。！？…~～、，,.:：;；!?"\'”’」』）)]}》】\s'
DEFAULT_FEEL = ['吧', '呢', '哦', '啊', '呀', '嘛', '诶', '哼', '哎', '咦', '哈', '呵', '啦', '咯', '喂']


def read_rows(path):
    rows = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        m = ROW.match(line)
        if m:
            rows.append((int(m.group(1)), m.group(2)))
    return rows


def collect(target):
    p = Path(target)
    files = sorted(f for f in (p.rglob('*.md') if p.is_dir() else [p])
                   if f.name != 'INDEX.md')
    docs = []
    for f in files:
        rows = read_rows(f)
        if rows:
            docs.append((f.stem, rows))
    return docs


def stats(rows, self_words, you_words, feel_words, top):
    n = len(rows)
    d = collections.Counter()
    hit = collections.defaultdict(list)
    for num, t in rows:
        for w in self_words:
            d['self:' + w] += t.count(w)
            if w in t:
                hit['self:' + w].append(num)
        for w in you_words:
            d['you:' + w] += t.count(w)
            if w in t:
                hit['you:' + w].append(num)
        for mark in ('！', '？', '……', '~', '——', '"', '“'):
            d['punct:' + mark] += t.count(mark)
        tail = t.rstrip(TAIL_PUNCT)
        if tail:
            d['tail:' + tail[-1]] += 1
        for w in feel_words:
            d['feel:' + w] += t.count(w)
        if you_words and t.startswith(you_words[0]):
            d['open:' + you_words[0]] += 1
    out = {
        '条数': n,
        '平均字数': round(sum(len(t) for _, t in rows) / n, 1) if n else 0,
        '最长条': max(((len(t), num) for num, t in rows), default=(0, 0)),
        '最短条': min(((len(t), num) for num, t in rows), default=(0, 0)),
        '计数': {k: v for k, v in d.items() if not k.startswith('tail:')},
        '句尾字频': sorted(((k[5:], v) for k, v in d.items() if k.startswith('tail:')),
                          key=lambda x: -x[1])[:top],
        '条号': {k: v for k, v in hit.items() if v},
    }
    return out


def show(name, s, quiet=False):
    print('── %s ── %d 条，平均 %s 字，最长 %d 字（#%d）／最短 %d 字（#%d）'
          % (name, s['条数'], s['平均字数'], s['最长条'][0], s['最长条'][1],
             s['最短条'][0], s['最短条'][1]))
    if quiet:
        return
    for k, v in sorted(s['计数'].items()):
        kind, _, w = k.partition(':')
        label = {'self': '自称', 'you': '第二人称', 'punct': '标点', 'feel': '语气词',
                 'open': '起手'}.get(kind, kind)
        print('   %s %-6s %d' % (label, w, v))
    print('   句尾字频 ' + '／'.join('%s%d' % (w, c) for w, c in s['句尾字频']))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('--self', dest='self_words', default='我',
                    help='自称候选，逗号分隔（默认 我）')
    ap.add_argument('--you', dest='you_words', default='你',
                    help='第二人称候选，逗号分隔（默认「你」；按你的语料给，如「你,您,您老」）')
    ap.add_argument('--feel', dest='feel_words', default=','.join(DEFAULT_FEEL))
    ap.add_argument('--extra', action='append', default=[],
                    help='额外的非场景锚料文件（信件／贺图原话），单独统计；可多次')
    ap.add_argument('--top', type=int, default=10, help='句尾字频取前 N（默认 10）')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    self_w = [w for w in a.self_words.split(',') if w]
    you_w = [w for w in a.you_words.split(',') if w]
    feel_w = [w for w in a.feel_words.split(',') if w]

    docs = collect(a.target)
    if not docs and not a.extra:
        print('没有解析到编号行（档表格应为 `| 编号 | 原文 | 备注 |`）：%s' % a.target)
        return 1
    result = {}
    for name, rows in docs:
        result[name] = stats(rows, self_w, you_w, feel_w, a.top)
    allrows = [r for _, rows in docs for r in rows]
    if allrows:
        result['合计'] = stats(allrows, self_w, you_w, feel_w, a.top)
    for path in a.extra:
        rows = [(i + 1, l.strip()) for i, l in
                enumerate(Path(path).read_text(encoding='utf-8').splitlines()) if l.strip()]
        result['extra:' + Path(path).stem] = stats(rows, self_w, you_w, feel_w, a.top)

    if a.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    for name, s in result.items():
        show(name, s)
        print()
    print('提示：结论写进锚点表时逐条标条号（脚本已打印命中条号，用 --json 取）。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
