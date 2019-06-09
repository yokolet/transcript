import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from eng_to_kana.epenthetic_vowel_handler import EpentheticVowelHandler

class TestEpentheticVowelHandler(unittest.TestCase):
    def setUp(self):
        self.func = EpentheticVowelHandler().addEpentheticVowel

    def test_1(self):
        expected_pairs = {
            'fazaa': 'fazaa',
            'aam': 'aamu',
            'komaNdaa': 'komaNdaa',
            'shii': 'shii',
            'pigg': 'piggu',
            'bedd': 'beddo',
            'baad': 'baado',
            'haNbaagaa': 'haNbaagaa',
            'kyatt': 'kyatto',
            'gyaNbur': 'gyaNburu',
            'gyar': 'gyaru',
            'kaNtrii': 'kaNtorii',
            'moNkii': 'moNkii',
            'froNt': 'furoNto',
            'roNdoN': 'roNdoN',
            'bokks': 'bokkusu',
            'stro': 'sutoro',
            'poot': 'pooto',
            'bukk': 'bukku',
            'baruuN': 'baruuN',
            'abaut': 'abauto',
            'pairott': 'pairotto',
            'winaa': 'winaa',
            'mama': 'mama',
            'puuma': 'puuma',
            'dei': 'dei',
            'deibidd': 'deibiddo',
            'mai': 'mai',
            'boi': 'boi',
            'toi': 'toi',
            'fooN': 'fooN',
            'noo': 'noo',
            'nau': 'nau',
            'kwiaa': 'kwiaa',
            'heaa': 'heaa',
            'tuaa': 'tuaa',
            'kyuub': 'kyuubu',
            'amazoN': 'amazoN',
            'bokksiNg': 'bokkusiNgu',
            'guugur': 'guuguru',
            'maikroosoft': 'maikuroosofuto',
            'neishoN': 'neishoN',
            'rooma': 'rooma', 
            'wudd': 'wuddo',
            'wuzz': 'wuzzu',
            'siN': 'siN',
            'reft': 'refuto', 
            'mirk': 'miruku',
            'soNg': 'soNgu',
            'daariNg': 'daariNgu',
            'iist': 'iisuto',
            'ies': 'iesu',
            'huup': 'huupu', 
            'popp': 'poppu',
            'katt': 'katto',
            'pakk': 'pakku',
            'kis': 'kisu', 
            'pacch': 'pacchi',
            'messh': 'messhu'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_2(self):
        expected_pairs = {
            'watt': 'watto',
            'hwatt': 'howatto',
            'wiit': 'wiito',
            'hwiit': 'howiito',
            'wiizaz': 'wiizazu',
            'hwiizaz': 'howiizazu',
            'wiiziz': 'wiizizu',
            'weN': 'weN',
            'hweN': 'howeN',
            'wiN': 'wiN',
            'hwiN': 'howiN',
            'wuu': 'wuu',
            'hwuu': 'howuu',
            'hyuu': 'hyuu',
            'wicch': 'wicchi',
            'hwicch': 'howicchi',
            'waitii': 'waitii',
            'hwaitii': 'howaitii',
            'woo': 'woo',
            'hwoo': 'howoo',
            'hoo': 'hoo',
            'wai': 'wai',
            'hwai': 'howai',
            'wiz': 'wizu',
            'wis': 'wisu'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_3(self):
        expected_pairs = {
            'ajoiN': 'ajoiN',
            'eriia': 'eriia',
            'baNkwett': 'baNkwetto',
            'kyarijj': 'kyarijji',
            'keaaaj': 'keaaji',
            'ejj': 'ejji',
            'daiett': 'daietto',
            'jyajj': 'jyajji',
            'majoritii': 'majoritii',
            'myuut': 'myuuto',
            'oraNj': 'oraNji',
            'oriNj': 'oriNji',
            'pooett': 'pooetto',
            'kwakk': 'kwakku',
            'kweik': 'kweiku',
            'kwiirii': 'kwiirii',
            'kwiiN': 'kwiiN',
            'kwaiett': 'kwaietto',
            'kwipp': 'kwippu',
            'kwoota': 'kwoota',
            'kwoot': 'kwooto',
            'soroo': 'soroo',
            'wijitt': 'wijitto'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_4(self):
        expected_pairs = {
            'kor': 'koru',
            'didd': 'diddo',
            'fiNgaa': 'fiNgaa',
            'hiaa': 'hiaa',
            'aidor': 'aidoru',
            'reidii': 'reidii',
            'ritor': 'ritoru',
            'mazaa': 'mazaa',
            'prejaa': 'purejaa',
            'pyuaa': 'pyuaa',
            'turist': 'turisuto',
            'bijoN': 'bijoN'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

if __name__ == '__main__':
    unittest.main()