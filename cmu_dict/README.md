# Create English word to IPA phonetics database 

This is a tool to create a pickle database ([https://pythonhosted.org/pickleDB/](https://pythonhosted.org/pickleDB/)) from CMU-IPA Dictionary.

The pickle database has key-value pairs of English words and phonetic transcriptions.
A single word may have multiple transcriptions. For this reason, values are arrays.

## Intallation

```bash
pip install -r requirements.txt
```

## How to Run

The code assumus the CMU-IPA Dictionary is in this top directory as `CMU.in.IPA.txt`.
The pickle database name can be given. If none is given, the default name is `cmu_ipa.pickle`.

```
$ ./createdb.py -h
usage: createdb.py [-h] [-d DBNAME]

Creates picledb from CMU IPA dict

optional arguments:
  -h, --help            show this help message and exit
  -d DBNAME, --dbname DBNAME
                        pickledb file. if not given, default name will be used
```

## CMU-IPA Dictionary

The dictionary is from [http://people.umass.edu/nconstan/CMU-IPA/](http://people.umass.edu/nconstan/CMU-IPA/). The dictionary has around 130,000 words and those American phonetic transcription.