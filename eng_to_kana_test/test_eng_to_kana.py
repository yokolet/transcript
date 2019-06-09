import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from eng_to_kana.eng_to_kana import EngToKana

class TestEngToKana(unittest.TestCase):
    def setUp(self):
        self.list_func = EngToKana().fromWordList
        self.file_func = EngToKana().fromFile

    def test_1(self):
        words = ['what', 'girl', 'cat', 'judge', 'majority']
        expected = [['ワット', 'ホワット'], ['ガール'], ['キャット'], ['ジャッジ'], ['マジョリティー']]
        self.assertEqual(expected, self.list_func(words))

    def test_2(self):
        words = ['gaga']
        self.assertEqual([['E_DIC']], self.list_func(words))