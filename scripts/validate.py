from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def validate():
    errors=[]
    en=load('data/minimum.en.json'); lv=load('data/minimum.lv.json'); src=load('data/sources.json')
    if [x['id'] for x in en['rules']] != [x['id'] for x in lv['rules']]: errors.append('EN/LV control ID parity failed')
    if len(en['rules'])!=25 or len(lv['rules'])!=25: errors.append('expected exactly 25 rules per language')
    expected=[f'C{i:02d}' for i in range(1,26)]
    if [x['id'] for x in en['rules']]!=expected: errors.append('control IDs must be C01..C25')
    source_ids={x['id'] for x in src['sources']}
    for lang,payload in [('en',en),('lv',lv)]:
        for item in payload['rules']:
            missing=set(item.get('sources',[]))-source_ids
            if missing: errors.append(f'{lang}:{item["id"]} unknown sources: {sorted(missing)}')
    en_blob=json.dumps(en,ensure_ascii=False).lower()
    forbidden_global=['cert.lv','nic.lv','valsts polic','latvij']
    for x in forbidden_global:
        if x in en_blob: errors.append(f'global EN guidance contains Latvia-specific token: {x}')
    lv20=next(x for x in lv['rules'] if x['id']=='C20')
    lv25=next(x for x in lv['rules'] if x['id']=='C25')
    if 'cert.lv' not in lv20['guidance'].lower(): errors.append('LV C20 must contain CERT.LV localisation')
    if 'cert.lv' not in lv25['guidance'].lower(): errors.append('LV C25 must contain CERT.LV reporting localisation')
    for path in ['README.md','README.lv.md','docs/en/cybersecurity-minimum.md','docs/lv/kiberdrosibas-minimums.md']:
        text=(ROOT/path).read_text(encoding='utf-8')
        if 'http://' in text: errors.append(f'{path}: insecure URL')
        for n,line in enumerate(text.splitlines(),1):
            if line.rstrip()!=line: errors.append(f'{path}:{n}: trailing whitespace')
    return errors
if __name__=='__main__':
    e=validate()
    if e:
        print(f'Validation failed: {len(e)} error(s)'); [print('-',x) for x in e]; raise SystemExit(1)
    print('Validation passed: 25 bilingual controls, global EN boundary and Latvia localisation contracts.')
