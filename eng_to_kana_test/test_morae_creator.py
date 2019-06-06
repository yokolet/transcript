import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'eng_to_kana'))
import unittest
from eng_to_ipa.morae_creator import MoraeCreator

class TestMoraeCreator(unittest.TestCase):
    def setUp(self):
        self.func = MoraeCreator().createMorae

    def test_1(self):
        expected_pairs = {
            'fazaa': 'fa.za.a',
            'aamu': 'a.a.mu',
            'komaNdaa': 'ko.ma.N.da.a',
            'shii': 'shi.i',
            'piggu': 'pi.g.gu',
            'beddo': 'be.d.do',
            'baado': 'ba.a.do',
            'haNbaagaa': 'ha.N.ba.a.ga.a',
            'kyatto': 'kya.t.to',
            'gyaNburu': 'gya.N.bu.ru',
            'gyaru': 'gya.ru',
            'kaNtorii': 'ka.N.to.ri.i',
            'moNkii': 'mo.N.ki.i',
            'furoNto': 'fu.ro.N.to',
            'roNdoN': 'ro.N.do.N',
            'bokkusu': 'bo.k.ku.su',
            'sutoro': 'su.to.ro',
            'pooto': 'po.o.to',
            'bukku': 'bu.k.ku',
            'baruuN': 'ba.ru.u.N',
            'abauto': 'a.ba.u.to',
            'pairotto': 'pa.i.ro.t.to',
            'winaa': 'wi.na.a',
            'mama': 'ma.ma',
            'puuma': 'pu.u.ma',
            'dei': 'de.i',
            'deibiddo': 'de.i.bi.d.do',
            'mai': 'ma.i',
            'boi': 'bo.i',
            'toi': 'to.i',
            'fooN': 'fo.o.N',
            'noo': 'no.o', 
            'nau': 'na.u',
            'kwiaa': 'kwi.a.a',
            'heaa': 'he.a.a',
            'tuaa': 'tu.a.a',
            'kyuubu': 'kyu.u.bu',
            'amazoN': 'a.ma.zo.N',
            'bokkusiNgu': 'bo.k.ku.si.N.gu',
            'guuguru': 'gu.u.gu.ru',
            'maikuroosofuto': 'ma.i.ku.ro.o.so.fu.to',
            'neishoN': 'ne.i.sho.N',
            'rooma': 'ro.o.ma',
            'wuddo': 'wu.d.do',
            'wuzzu': 'wu.z.zu',
            'siN': 'si.N',
            'refuto': 're.fu.to',
            'miruku': 'mi.ru.ku',
            'soNgu': 'so.N.gu',
            'daariNgu': 'da.a.ri.N.gu',
            'iisuto': 'i.i.su.to',
            'iesu': 'i.e.su',
            'huupu': 'hu.u.pu',
            'poppu': 'po.p.pu',
            'katto': 'ka.t.to',
            'pakku': 'pa.k.ku',
            'kisu': 'ki.su',
            'pacchi': 'pa.c.chi', 
            'messhu': 'me.s.shu'
            }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

if __name__ == '__main__':
    unittest.main()