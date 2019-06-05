#!/usr/bin/env python

import argparse
import os
import pickledb
import re
import sys
from tqdm import tqdm

CMU_IPA_DIC = 'CMU.in.IPA.txt'
DEFAULT = 'cmu_ipa.pickle'
KEYPAT = re.compile(r'\(\d\)')

def printAllData(db):
    keys = db.getall()
    print([(key, db.get(key)) for key in keys])

def process_line(db, line):
    try:
        key, value = re.split(r'\t+', line.rstrip()) # removes "\n"
        key = KEYPAT.sub('', key[:-1]) # removes "," and "(1) if any"
        value = value.replace('ˈ', '') # removes accent symbol
        value = value.replace('ˌ', '') # removes ˌ symbol
        if db.exists(key):
            prev = db.get(key)
            prev.append(value)
        else:
            db.set(key, [value])
    except ValueError as err:
        print("ERROR:", line, err)

def createdb(dbname):
    print('The pickledb, "{}", will be created.'.format(dbname))
    db = pickledb.load(dbname, False)
    count, pbar = 0, tqdm(total=133290)
    with open(CMU_IPA_DIC, 'r') as f:
        while True:
            line = f.readline()
            if not line: break
            process_line(db, line)
            count += 1
            if count % 1000 == 0:
                db.dump()
                pbar.update(1000)
    pbar.close()
    db.dump()

def process_args():
    parser = argparse.ArgumentParser(
       prog='createdb.py',
       description='Creates picledb from CMU IPA dict'
    )
    parser.add_argument('-d', '--dbname', default=DEFAULT, help='pickledb file. if not given, default name will be used')
    return parser.parse_args()

if __name__ == '__main__':
    args = process_args()
    createdb(args.dbname)
