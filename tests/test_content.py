import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from scripts.validate import validate
class Tests(unittest.TestCase):
    def test_validation(self): self.assertEqual(validate(),[])
    def test_exact_25(self):
        en=json.loads((ROOT/'data/minimum.en.json').read_text())['rules']; lv=json.loads((ROOT/'data/minimum.lv.json').read_text())['rules']
        self.assertEqual(len(en),25); self.assertEqual(len(lv),25)
    def test_parity(self):
        en=json.loads((ROOT/'data/minimum.en.json').read_text())['rules']; lv=json.loads((ROOT/'data/minimum.lv.json').read_text())['rules']
        self.assertEqual([x['id'] for x in en],[x['id'] for x in lv])
    def test_global_english_has_no_latvia_dependency(self):
        en=json.loads((ROOT/'data/minimum.en.json').read_text())
        blob=json.dumps(en,ensure_ascii=False).lower()
        self.assertNotIn('cert.lv',blob); self.assertNotIn('latvij',blob)
    def test_latvia_localisation(self):
        lv=json.loads((ROOT/'data/minimum.lv.json').read_text())['rules']
        self.assertIn('CERT.LV',next(x for x in lv if x['id']=='C20')['guidance'])
        self.assertIn('CERT.LV',next(x for x in lv if x['id']=='C25')['guidance'])
if __name__=='__main__': unittest.main()
