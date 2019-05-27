import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from eng_to_ipa.trans_vowel import TransVowel

class TestTransVowel(unittest.TestCase):
    def setUp(self):
        self.func = TransVowel().transVowel

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
            'nation'
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
            'gæˈl': 'gyal',
            'kʌntɹi': 'kantɹi',
            'mʌŋki': 'moŋki',
            'fɹʌnt': 'fɹont',
            'lʌndʌn': 'london',
            'bɑks': 'boks',
            'stɹɔ': 'stɹoo',
            'pɔɹt': 'pooɹt',
            'bʊk': 'buk',
            'bʌlun': 'baluun',
            'ʌbawt': 'abaut',
            'pajlʌt': 'pailot',
            'wɪnɚ': 'winaa',
            'mɑmʌ': 'mama',
            'pumʌ': 'puma',
            'dej': 'dei',
            'dejvɪd': 'deivid',
            'maj': 'mai',
            'bɔj': 'booi',
            'tɔj': 'toi',
            'fown': 'foon',
            'now': 'noo',
            'naw': 'nau',
            'kwɪɹ': 'kuiaa',
            'hɛɹ': 'heaa',
            'tʊɹ': 'tuaa',
            'kjub': 'kyuub',
            'æmʌzɑˌn': 'amazon',
            'bɑksɪŋ': 'boksiŋ',
            'gugʌl': 'guugul',
            'majkɹowˌsɔft': 'maikɹosoft',
            'nejʃʌn': 'neiʃon'
        }
        print(len(words), len(trans_map))

if __name__ == '__main__':
    unittest.main()