import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import pickledb
from eng_to_kana.vowel_converter import VowelConverter

class TestVowelConverter(unittest.TestCase):
    def setUp(self):
        dbname = os.path.join(os.path.dirname(__file__), '..', 'cmu_dict', 'cmu_ipa.pickle')
        self.db = pickledb.load(dbname, False)
        self.func = VowelConverter().convertVowel

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
        trans_map = {
            'fɑðɚ': 'faðaa',
            'ɑɹm': 'aam',
            'kʌmændɚ': 'komandaa',
            'ʃi': 'ʃii',
            'pɪg': 'pig',
            'bɛd': 'bed',
            'bɚd': 'baad',
            'hæmbɚgɚ': 'hambaagaa',
            'kæt': 'kyat',
            'gæmbʌl': 'gyambul',
            'gæl': 'gyal',
            'kʌntɹi': 'kantɹii',
            'mʌŋki': 'moŋkii',
            'fɹʌnt': 'fɹont',
            'lʌndʌn': 'london',
            'bɑks': 'boks',
            'stɹɔ': 'stɹo',
            'pɔɹt': 'poot',
            'bʊk': 'buk',
            'bʌlun': 'baluun',
            'ʌbawt': 'abaut',
            'pajlʌt': 'pailot',
            'wɪnɚ': 'winaa',
            'mɑmʌ': 'mama',
            'pumʌ': 'puuma',
            'dej': 'dei',
            'dejvɪd': 'deivid',
            'maj': 'mai',
            'bɔj': 'boi',
            'tɔj': 'toi',
            'fown': 'foon',
            'now': 'noo',
            'naw': 'nau',
            'kwɪɹ': 'kwiaa',
            'hɛɹ': 'heaa',
            'tʊɹ': 'tuaa',
            'kjub': 'kyuub',
            'æmʌzɑn': 'amazon',
            'bɑksɪŋ': 'boksiŋ',
            'gugʌl': 'guugul',
            'majkɹowsɔft': 'maikɹoosoft',
            'nejʃʌn': 'neiʃon',
            'ɹowmʌ': 'ɹooma',
            'wʊd': 'wud',
            'wʊdz': 'wudz',
            'θɪn': 'θin',
            'lɛft': 'left',
            'mɪlk': 'milk',
            'sɔŋ': 'soŋ',
            'dɑɹlɪŋ': 'daaliŋ',
            'jist': 'iist',
            'jɛs': 'ies',
            'hup': 'huup',
            'pɑp': 'pop',
            'kʌt': 'kat',
            'pæk': 'pak',
            'kɪs': 'kis',
            'pæʧ': 'paʧ',
            'mɛʃ': 'meʃ'
        }
        for w in words:
            ph = self.db.get(w)[0]
            print(w, ph, trans_map[ph])
            self.assertEqual(trans_map[ph], self.func(w, ph))

    def test_2(self):
        expected_pairs = {
            'what': [('wʌt', 'wat'), ('hwʌt', 'hwat')],
            'wheat': [('wit', 'wiit'), ('hwit', 'hwiit')],
            'wheezes': [('wizʌz', 'wiizez'), ('hwizʌz', 'hwiizez'), ('wizɪz', 'wiiziz')],
            'when': [('wɛn', 'wen'), ('hwɛn', 'hwen'), ('wɪn', 'win'), ('hwɪn', 'hwin')],
            'whew': [('wu', 'wuu'), ('hwu', 'hwuu'), ('hju', 'hyuu')],
            'which': [('wɪʧ', 'wiʧ'), ('hwɪʧ', 'hwiʧ')],
            'whitey': [('wajti', 'waitii'), ('hwajti', 'hwaitii')],
            'whoa': [('wow', 'woo'), ('hwow', 'hwoo'), ('how', 'hoo')],
            'why': [('waj', 'wai'), ('hwaj', 'hwai')],
            'with': [('wɪð', 'wið'), ('wɪθ', 'wiθ')]}
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_3(self):
        expected_pairs = {
            'adjoin': [('ʌʤɔjn', 'aʤoin')],
            'area': [('ɛɹiʌ', 'eɹiia')],
            'banquet': [('bæŋkwʌt', 'baŋkwet')],
            'carriage': [('kæɹɪʤ', 'kyaɹiʤ'), ('kɛɹʌʤ', 'keɹiʤ')],
            'edge': [('ɛʤ', 'eʤ')],
            'diet': [('dajʌt', 'daiet')],
            'judge': [('ʤʌʤ', 'ʤyaʤ')],
            'mute': [('mjut', 'myuut')],
            'majority': [('mʌʤɔɹʌti', 'maʤoɹitii')],
            'orange': [('ɔɹʌnʤ', 'oɹanʤ'), ('ɔɹɪnʤ', 'oɹinʤ')],
            'poet': [('powʌt', 'pooet')],
            'quack': [('kwæk', 'kwak')],
            'quake': [('kwejk', 'kweik')],
            'query': [('kwiɹi', 'kwiiɹii')],
            'queen': [('kwin', 'kwiin')],
            'quiet': [('kwajʌt', 'kwaiet')],
            'quip': [('kwɪp', 'kwip')],
            'quota': [('kwowtʌ', 'kwoota')],
            'quote': [('kwowt', 'kwoot')],
            'sorrow': [('sɑɹow', 'soɹoo')],
            'widget': [('wɪʤɪt', 'wiʤit')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_4(self):
        expected_pairs = {
            'call': [('kɔl', 'kol')],
            'did': [('dɪd', 'did')],
            'finger': [('fɪŋgɚ', 'fiŋgaa')],
            'here': [('hiɹ', 'hiaa')],
            'idle': [('ajdʌl', 'aidol')],
            'lady': [('lejdi', 'leidii')],
            'little': [('lɪtʌl', 'litol')],
            'mother': [('mʌðɚ', 'maðaa')],
            'pleasure': [('plɛʒɚ', 'pleʒaa')],
            'pure': [('pjʊɹ', 'pyuaa')],
            'tourist': [('tʊɹʌst', 'tuɹist')],
            'vision': [('vɪʒʌn', 'viʒon')],
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_5(self):
        expected_pairs = {
            'abasia': [('ʌbejʒjʌ', 'abeiʒyaa')],
            'accuracies': [('ækjɚʌsiz', 'akyuasiiz')],
            'aigner': [('ejnɚ', 'einaa'), ('ɛnjej', 'enyei'), ('ejknɚ', 'eiknaa')],
            'akiyama': [('ɑkijɑmʌ', 'akiiyama')],
            'alejo': [('ɑlejjow', 'aleiyoo')],
            'augustyniak': [('awgʌstɪniæk', 'augastiniiak')],
            'avignon': [('ævɪnjɔn', 'avinyon')],
            'ayyash': [('ajjæʃ', 'aiyaʃ')],
            'beaulieu': [('bowljʊ', 'boolyu')],
            'bedient': [('bidjɪnt', 'biidient')],
            "c'mon": [('kʌmɑn', 'kamon')],
            'chojnacki': [('ʧʌjnɑtski', 'ʧoinatskii')],
            'dr': [('dɹajv', 'dɹaiv'), ('dɑktɚ', 'daktaa')],
            'filyaw': [('fɪliɑv', 'filiiav'), ('fɪljaw', 'filyoo')],
            'fojtik': [('fɑjtɪk', 'faitik')],
            'horejsi': [('hɔɹejjsi', 'hoɹeiji')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_6(self):
        expected_pairs = {
            'applaud': [('ʌplɔd', 'aplood')],
            'apple': [('æpʌl', 'apul')],
            'applebee': [('æpʌlbi', 'apulbii')],
            'applet': [('æplʌt', 'aplet')],
            'application': [('æplʌkejʃʌn', 'aplikeiʃon')],
            'apply': [('ʌplaj', 'aplai')],
            'pineapple': [('pajnæpʌl', 'painapul')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

    def test_7(self):
        expected_pairs = {
            'abridged': [('ʌbɹɪʤd', 'abɹiʤd')],
            'abridgement': [('ʌbɹɪʤmʌnt', 'abɹiʤment')],
            'abuladze': [('æbjulædzi', 'abyuuladzii')],
            'abuse': [('ʌbjus', 'abyuus'), ('ʌbjuz', 'abyuuz')],
            'achmed': [('ɑhmɛd', 'ahmed')],
            'akao': [('ʌkejow', 'akeioo'), ('ʌkɑw', 'akaa')],
            'awb' : [('ɑwb', 'aab'), ('ejdʌbʌljubi', 'eidabalyuubii')],
            'confuse': [('kʌnfjuz', 'konfyuuz')],
            'few': [('fju', 'fyuu')],
            'yay': [('jej', 'yei')]
        }
        for w, pairs in expected_pairs.items():
            for p in pairs:
                self.assertEqual(p[1], self.func(w, p[0]))

if __name__ == '__main__':
    unittest.main()