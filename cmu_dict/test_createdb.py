import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import unittest
import pickledb

class TestCreateDb(unittest.TestCase):
    def setUp(self):
        dbname = os.path.join(os.path.dirname(__file__), 'cmu_ipa.pickle')
        print(dbname)
        self.db = pickledb.load(dbname, False)

    def test_1(self):
        expexted_pair = {
            'father': 'fɑðɚ',
            'arm': 'ɑɹm',
            'commander': 'kʌmændɚ',
            'she': 'ʃi', 
            'pig': 'pɪg',
            'bed': 'bɛd',
            'bird': 'bɚd',
            'hamburger': 'hæmbɚgɚ',
            'cat': 'kæt',
            'gamble': 'gæmbʌl',
            'gal': 'gæl',
            'country': 'kʌntɹi',
            'monkey': 'mʌŋki',
            'front': 'fɹʌnt',
            'london': 'lʌndʌn',
            'box': 'bɑks',
            'straw': 'stɹɔ',
            'port': 'pɔɹt',
            'book': 'bʊk',
            'balloon': 'bʌlun',
            'about': 'ʌbawt',
            'pilot': 'pajlʌt',
            'winner': 'wɪnɚ',
            'mama': 'mɑmʌ',
            'puma': 'pumʌ',
            'day': 'dej',
            'david': 'dejvɪd',
            'my': 'maj',
            'boy': 'bɔj',
            'toy': 'tɔj',
            'phone': 'fown',
            'no': 'now',
            'now': 'naw',
            'queer': 'kwɪɹ',
            'hair': 'hɛɹ',
            'tour': 'tʊɹ',
            'cube': 'kjub',
            'amazon': 'æmʌzɑn',
            'boxing': 'bɑksɪŋ',
            'google': 'gugʌl',
            'microsoft': 'majkɹowsɔft',
            'nation': 'nejʃʌn',
            'roma': 'ɹowmʌ',
            'wood': 'wʊd',
            'woods': 'wʊdz',
            'thin': 'θɪn',
            'left': 'lɛft',
            'milk': 'mɪlk',
            'song': 'sɔŋ',
            'darling': 'dɑɹlɪŋ',
            'yeast': 'jist', 
            'yes': 'jɛs',
            'hoop': 'hup',
            'pop': 'pɑp',
            'cut': 'kʌt',
            'pack': 'pæk',
            'kiss': 'kɪs',
            'patch': 'pæʧ',
            'mesh': 'mɛʃ'
            }
        for key, value in expexted_pair.items():
            self.assertEqual(value, self.db.get(key)[0])

if __name__ == '__main__':
    unittest.main()