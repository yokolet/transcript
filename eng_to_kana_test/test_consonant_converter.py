import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from eng_to_kana.consonant_converter import ConsonantConverter

class TestConsonantConverter(unittest.TestCase):
    def setUp(self):
        self.func = ConsonantConverter().convertConsonant

    def test_1(self):
        words = [
            'father',
            'arm',
            'commander',
            'she',
            'pig',
            'bed',
            'bird',
            'hamburger',
            'cat',
            'gamble',
            'gal',
            'country',
            'monkey',
            'front',
            'london',
            'box',
            'straw',
            'port',
            'book',
            'balloon',
            'about',
            'pilot',
            'winner',
            'mama',
            'puma',
            'day',
            'david',
            'my',
            'boy',
            'toy',
            'phone',
            'no',
            'now',
            'queer',
            'hair',
            'tour',
            'cube',
            'amazon',
            'boxing',
            'google',
            'microsoft',
            'nation',
            'roma',
            'wood',
            'woods',
            'thin',
            'left',
            'milk',
            'song',
            'darling',
            'yeast',
            'yes',
            'hoop',
            'pop',
            'cut',
            'pack',
            'kiss',
            'patch',
            'mesh'
        ]
        pairs = {
            'father': 'faðaa',
            'arm': 'aam',
            'commander': 'komandaa',
            'she': 'ʃii',
            'pig': 'pig',
            'bed': 'bed',
            'bird': 'baad',
            'hamburger': 'hambaagaa', 
            'cat': 'kyat',
            'gamble': 'gyambul',
            'gal': 'gyal',
            'country': 'kantɹii',
            'monkey': 'moŋkii',
            'front': 'fɹont',
            'london': 'london',
            'box': 'boks',
            'straw': 'stɹo',
            'port': 'poot',
            'book': 'buk',
            'balloon': 'baluun',
            'about': 'abaut',
            'pilot': 'pailot',
            'winner': 'winaa',
            'mama': 'mama',
            'puma': 'puuma',
            'day': 'dei',
            'david': 'deivid',
            'my': 'mai',
            'boy': 'boi',
            'toy': 'toi',
            'phone': 'foon',
            'no': 'noo',
            'now': 'nau',
            'queer': 'kwiaa',
            'hair': 'heaa',
            'tour': 'tuaa',
            'cube': 'kyuub',
            'amazon': 'amazon',
            'boxing': 'boksiŋ',
            'google': 'guugul',
            'microsoft': 'maikɹoosoft',
            'nation': 'neiʃon',
            'roma': 'ɹooma',
            'wood': 'wud',
            'woods': 'wudz',
            'thin': 'θin',
            'left': 'left',
            'milk': 'milk',
            'song': 'soŋ',
            'darling': 'daaliŋ',
            'yeast': 'iist',
            'yes': 'ies',
            'hoop': 'huup',
            'pop': 'pop',
            'cut': 'kat',
            'pack': 'pak',
            'kiss': 'kis',
            'patch': 'paʧ',
            'mesh': 'meʃ'
            }
        expected_pair = {
            'faðaa': 'fazaa',
            'aam': 'aam',
            'komandaa': 'komaNdaa',
            'ʃii': 'shii',
            'pig': 'pigg',
            'bed': 'bedd',
            'baad': 'baad',
            'hambaagaa': 'haNbaagaa',
            'kyat': 'kyatt',
            'gyambul': 'gyaNbur',
            'gyal': 'gyar',
            'kantɹii': 'kaNtrii',
            'moŋkii': 'moNkii',
            'fɹont': 'froNt',
            'london': 'roNdoN',
            'boks': 'bokks',
            'stɹo': 'stro',
            'poot': 'poot',
            'buk': 'bukk',
            'baluun': 'baruuN',
            'abaut': 'abaut',
            'pailot': 'pairott',
            'winaa': 'winaa',
            'mama': 'mama',
            'puuma': 'puuma',
            'dei': 'dei',
            'deivid': 'deibidd',
            'mai': 'mai',
            'boi': 'boi',
            'toi': 'toi',
            'foon': 'fooN',
            'noo': 'noo',
            'nau': 'nau',
            'kwiaa': 'kwiaa',
            'heaa': 'heaa',
            'tuaa': 'tuaa',
            'kyuub': 'kyuub',
            'amazon': 'amazoN',
            'boksiŋ': 'bokksiNg',
            'guugul': 'guugur',
            'maikɹoosoft': 'maikroosoft',
            'neiʃon': 'neishoN',
            'ɹooma': 'rooma',
            'wud': 'wudd',
            'wudz': 'wuzz',
            'θin': 'siN',
            'left': 'reft',
            'milk': 'mirk',
            'soŋ': 'soNg',
            'daaliŋ': 'daariNg',
            'iist': 'iist',
            'ies': 'ies',
            'huup': 'huup',
            'pop': 'popp',
            'kat': 'katt',
            'pak': 'pakk',
            'kis': 'kis',
            'paʧ': 'pacch',
            'meʃ': 'messh'
        }
        for w in words:
            ph = pairs[w]
            expected = expected_pair[pairs[w]]
            self.assertEqual(expected, self.func(w, ph))

    def test_2(self):
        expected_pairs = {
            'what': [('wat', 'watt'), ('hwat', 'hwatt')],
            'wheat': [('wiit', 'wiit'), ('hwiit', 'hwiit')],
            'wheezes': [('wiizaz', 'wiizaz'), ('hwiizaz', 'hwiizaz'), ('wiiziz', 'wiiziz')],
            'when': [('wen', 'weN'), ('hwen', 'hweN'), ('win', 'wiN'), ('hwin', 'hwiN')],
            'whew': [('wuu', 'wuu'), ('hwuu', 'hwuu'), ('hyuu', 'hyuu')],
            'which': [('wiʧ', 'wicch'), ('hwiʧ', 'hwicch')],
            'whitey': [('waitii', 'waitii'), ('hwaitii', 'hwaitii')],
            'whoa': [('woo', 'woo'), ('hwoo', 'hwoo'), ('hoo', 'hoo')],
            'why': [('wai', 'wai'), ('hwai', 'hwai')],
            'with': [('wið', 'wiz'), ('wiθ', 'wis')]}
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_3(self):
        expected_pairs = {
            'adjoin': [('aʤoin', 'ajoiN')],
            'area': [('eɹiia', 'eriia')],
            'banquet': [('baŋkwet', 'baNkwett')],
            'carriage': [('kyaɹiʤ', 'kyarijj'), ('keaaaʤ', 'keaaaj')],
            'edge': [('eʤ', 'ejj')],
            'diet': [('daiet', 'daiett')],
            'judge': [('ʤyaʤ', 'jyajj')],
            'majority': [('maʤoɹitii', 'majoritii')],
            'mute': [('myuut', 'myuut')],
            'orange': [('oɹanʤ', 'oraNj'), ('oɹinʤ', 'oriNj')],
            'poet': [('pooet', 'pooett')],
            'quack': [('kwak', 'kwakk')],
            'quake': [('kweik', 'kweik')],
            'query': [('kwiiɹii', 'kwiirii')],
            'queen': [('kwiin', 'kwiiN')],
            'quiet': [('kwaiet', 'kwaiett')],
            'quip': [('kwip', 'kwipp')],
            'quota': [('kwoota', 'kwoota')],
            'quote': [('kwoot', 'kwoot')],
            'sorrow': [('soɹoo', 'soroo')],
            'widget': [('wiʤit', 'wijitt')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_4(self):
        expected_pairs = {
            'call': [('kol', 'kor')],
            'did': [('did', 'didd')],
            'finger': [('fiŋgaa', 'fiNgaa')],
            'here': [('hiaa', 'hiaa')],
            'idle': [('aidol', 'aidor')],
            'lady': [('leidii', 'reidii')],
            'little': [('litol', 'ritor')],
            'mother': [('maðaa', 'mazaa')],
            'pleasure': [('pleʒaa', 'prejaa')],
            'pure': [('pyuaa', 'pyuaa')],
            'tourist': [('tuɹist', 'turist')],
            'vision': [('viʒon', 'bijoN')],
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_5(self):
        expected_pairs = {
            'abasia': [('abeiʒyaa', 'abeijyaa')],
            'accuracies': [('akyuasiiz', 'akyuasiiz')],
            'aigner': [('einaa', 'einaa'), ('enyei', 'enyei'), ('eiknaa', 'eiknaa')],
            'akiyama': [('akiiyama', 'akiiyama')],
            'alejo': [('aleiyoo', 'areiyoo')],
            'augustyniak': [('augastiniiak', 'augastiniiakk')],
            'avignon': [('avinyon', 'abinyoN')],
            'ayyash': [('aiyaʃ', 'aiyassh')],
            'beaulieu': [('boolyu', 'booryu')],
            'bedient': [('biidient', 'biidieNt')],
            "c'mon": [('kamon', 'kamoN')],
            'chojnacki': [('ʧoinatskii', 'choinattskii')],
            'dr': [('dɹaiv', 'draib'), ('daktaa', 'dakktaa')],
            'filyaw': [('filiiav', 'firiiab'), ('filyoo', 'firyoo')],
            'fojtik': [('faitik', 'faitikk')],
            'horejsi': [('hoɹeiji', 'horeiji')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_6(self):
        expected_pairs = {
            'applaud': [('aplood', 'aprood')],
            'apple': [('apul', 'appur')],
            'applebee': [('apulbii', 'appurbii')],
            'applet': [('aplet' ,'aprett')],
            'application': [('aplikeiʃon' ,'aprikeishoN')],
            'apply': [('aplai', 'aprai')],
            'pineapple': [('painapul', 'painappur')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_7(self):
        expected_pairs = {
            'abridged': [('abɹiʤd', 'abrijjd')],
            'abridgement': [('abɹiʤment', 'abrijjmeNt')],
            'abuladze': [('abyuuladzii', 'abyuurazzii')],
            'abuse': [('abyuus', 'abyuus'), ('abyuuz', 'abyuuz')],
            'confuse': [('konfyuuz', 'koNfyuuz')],
            'few': [('fyuu', 'fyuu')],
            'yay': [('yei', 'yei')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

if __name__ == '__main__':
    unittest.main()