#!/usr/bin/env python

import argparse
import os
import pickledb
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from vowel_converter import VowelConverter
from consonant_converter import ConsonantConverter
from epenthetic_vowel_handler import EpentheticVowelHandler
from morae_creator import MoraeCreator
from morae_kana_converter import MoraeKanaConverter

class EngToKana:
    def __init__(self):
        dbname = os.path.join(os.path.dirname(__file__), '..', 'cmu_dict', 'cmu_ipa.pickle')
        self.db = pickledb.load(dbname, False)
        self.vowel_fn = VowelConverter().convertVowel
        self.consonant_fn = ConsonantConverter().convertConsonant
        self.epenthetic_fn = EpentheticVowelHandler().addEpentheticVowel
        self.morae_fn = MoraeCreator().createMorae
        self.kana_fn = MoraeKanaConverter().convertMorae

    def transcript(self, word):
        try:
            phs = self.db.get(word)
            if not phs:
                return ['E_DIC']
            phs1 = [self.vowel_fn(word, ph) for ph in phs]
            phs2 = [self.consonant_fn(word, ph) for ph in phs1]
            phs3 = [self.epenthetic_fn(ph) for ph in phs2]
            moraes = [self.morae_fn(ph) for ph in phs3]
            return [self.kana_fn(m) for m in moraes]
        except KeyError:
            return ['E_KEY']

    def fromFile(self, filename):
        print('[process words in {}]'.format(filename))

    def fromWordList(self, words):
        return [self.transcript(w) for w in words]

def process_args():
    parser = argparse.ArgumentParser(
        prog='eng_to_kana.py',
        description='Transcripts English word(s) to Katakana'
    )
    parser.add_argument('word',
                        nargs='*',
                        help='space separated word list to be transcripted')
    parser.add_argument('-f', '--file', help='a filename of english words. \
        if not given, reads from command line arguments')
    return parser

if __name__ == '__main__':
    parser = process_args()
    args = parser.parse_args()
    if args.file:
        EngToKana().fromFile(args.file)
    elif args.word and len(args.word) > 0:
        print(args.word)
        print(EngToKana().fromWordList(args.word))
    else:
        parser.print_help(sys.stderr)
