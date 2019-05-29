import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import pickledb
from eng_to_ipa.vowel_converter import VowelConverter

class TestVowelConverter(unittest.TestCase):
    def setUp(self):
        dbname = os.path.join(os.path.dirname(__file__), '..', 'cmu_ipa.pickle')
        self.db = pickledb.load(dbname, False)
        print('SYSPATH', sys.path)
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
            'wɪnɚ': 'uinaa',
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
            'kwɪɹ': 'kuiaa',
            'hɛɹ': 'heaa',
            'tʊɹ': 'tuaa',
            'kjub': 'kyuub',
            'æmʌzɑˌn': 'amazoˌn',
            'bɑksɪŋ': 'boksiŋ',
            'gugʌl': 'guugul',
            'majkɹowˌsɔft': 'maikɹooˌsoft',
            'nejʃʌn': 'neiʃon',
            'ɹowmʌ': 'ɹooma',
            'wʊd': 'ud',
            'wʊdz': 'udz',
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

if __name__ == '__main__':
    unittest.main()