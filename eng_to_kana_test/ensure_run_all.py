#!/usr/bin/env python

import argparse
import os
import logging
import pickledb
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'eng_to_kana'))
from vowel_converter import VowelConverter
from consonant_converter import ConsonantConverter
from epenthetic_vowel_handler import EpentheticVowelHandler
from morae_creator import MoraeCreator
from morae_kana_converter import MoraeKanaConverter

class EnsureRunAll:
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

    def main(self, start, end):
        keys = list(self.db.getall())
        start = int(start)
        if end:
            end = int(end)
        else:
            end = len(keys)
        print(start, end)
        logging.basicConfig(filename='transcript.log', level=logging.DEBUG)
        logging.debug('Startred')
        n = start
        for key in keys[start:end]:
            print(key)
            logging.debug('[{:5d}] {}: {}'.format(n, key, self.transcript(key)))
            n += 1
        logging.debug('Finished')

def process_args():
    parser = argparse.ArgumentParser(
        prog='ensure_run_all.py',
        description='Transcripts all words in the db to Katakana'
    )
    parser.add_argument('-s', '--start', default=0, help='the number of starting line')
    parser.add_argument('-e', '--end', default=None, help='the number of ending line (exclusive))')
    return parser

if __name__ == '__main__':
    parser = process_args()
    args = parser.parse_args()
    EnsureRunAll().main(args.start, args.end)