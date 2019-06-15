import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from eng_to_kana.morae_creator import MoraeCreator

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

    def test_2(self):
        expected_pairs = {
            'watto': 'wa.t.to',
            'howatto': 'ho.wa.t.to',
            'wiito': 'wi.i.to',
            'howiito': 'ho.wi.i.to',
            'wiizazu': 'wi.i.za.zu',
            'howiizazu': 'ho.wi.i.za.zu',
            'wiizizu': 'wi.i.zi.zu',
            'weN': 'we.N',
            'howeN': 'ho.we.N',
            'wiN': 'wi.N',
            'howiN': 'ho.wi.N',
            'wuu': 'wu.u',
            'howuu': 'ho.wu.u',
            'hyuu': 'hyu.u',
            'wicchi': 'wi.c.chi',
            'howicchi': 'ho.wi.c.chi',
            'waitii': 'wa.i.ti.i',
            'howaitii': 'ho.wa.i.ti.i',
            'woo': 'wo.o',
            'howoo': 'ho.wo.o',
            'hoo': 'ho.o',
            'wai': 'wa.i',
            'howai': 'ho.wa.i',
            'wizu': 'wi.zu',
            'wisu': 'wi.su'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_3(self):
        expected_pairs = {
            'ajoiN': 'a.jo.i.N',
            'eriia': 'e.ri.i.a',
            'baNkwetto': 'ba.N.kwe.t.to',
            'kyarijji': 'kya.ri.j.ji',
            'keaaji': 'ke.a.a.ji',
            'ejji': 'e.j.ji',
            'daietto': 'da.i.e.t.to',
            'jyajji': 'jya.j.ji',
            'majoritii': 'ma.jo.ri.ti.i',
            'myuuto': 'myu.u.to',
            'oraNji': 'o.ra.N.ji',
            'oriNji': 'o.ri.N.ji',
            'pooetto': 'po.o.e.t.to',
            'kwakku': 'kwa.k.ku',
            'kweiku': 'kwe.i.ku',
            'kwiirii': 'kwi.i.ri.i',
            'kwiiN': 'kwi.i.N',
            'kwaietto': 'kwa.i.e.t.to',
            'kwippu': 'kwi.p.pu',
            'kwoota': 'kwo.o.ta',
            'kwooto': 'kwo.o.to',
            'soroo': 'so.ro.o',
            'wijitto': 'wi.ji.t.to'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_4(self):
        expected_pairs = {
            'koru': 'ko.ru',
            'diddo': 'di.d.do',
            'fiNgaa': 'fi.N.ga.a',
            'hiaa': 'hi.a.a',
            'aidoru': 'a.i.do.ru',
            'reidii': 're.i.di.i',
            'ritoru': 'ri.to.ru',
            'mazaa': 'ma.za.a',
            'purejaa': 'pu.re.ja.a',
            'pyuaa': 'pyu.a.a',
            'turisuto': 'tu.ri.su.to',
            'bijoN': 'bi.jo.N'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_5(self):
        expected_pairs = {
            'abeijyaa': 'a.be.i.jya.a',
            'akyuasiizu': 'a.kyu.a.si.i.zu',
            'einaa': 'e.i.na.a',
            'enyei': 'e.nye.i',
            'eikunaa': 'e.i.ku.na.a',
            'akiiyama': 'a.ki.i.ya.ma',
            'areiyoo': 'a.re.i.yo.o',
            'augasutiniiakku': 'a.u.ga.su.ti.ni.i.a.k.ku',
            'abinyoN': 'a.bi.nyo.N',
            'aiyasshu': 'a.i.ya.s.shu',
            'booryu': 'bo.o.ryu',
            'biidieNto': 'bi.i.di.e.N.to',
            'kamoN': 'ka.mo.N',
            'choinattosukii': 'cho.i.na.t.to.su.ki.i',
            'doraibu': 'do.ra.i.bu',
            'dakkutaa': 'da.k.ku.ta.a',
            'firiiabu': 'fi.ri.i.a.bu',
            'firyoo': 'fi.ryo.o',
            'faitikku': 'fa.i.ti.k.ku',
            'horeiji': 'ho.re.i.ji'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_6(self):
        expected_pairs = {
            'apuroodo': 'a.pu.ro.o.do',
            'appuru': 'a.p.pu.ru',
            'appurubii': 'a.p.pu.ru.bi.i',
            'apuretto': 'a.pu.re.t.to',
            'apurikeishoN': 'a.pu.ri.ke.i.sho.N',
            'apurai': 'a.pu.ra.i',
            'painappuru': 'pa.i.na.p.pu.ru'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_7(self):
        expected_pairs = {
            'aburijjido': 'a.bu.ri.j.ji.do',
            'aburijjimeNto': 'a.bu.ri.j.ji.me.N.to',
            'abyuurazzii': 'a.byu.u.ra.z.zi.i',
            'abyuusu': 'a.byu.u.su',
            'abyuuzu': 'a.byu.u.zu',
            'koNfyuuzu': 'ko.N.fyu.u.zu',
            'fyuu': 'fyu.u',
            'yei': 'ye.i'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))


if __name__ == '__main__':
    unittest.main()