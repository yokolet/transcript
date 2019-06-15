# English to Katakana transcription

This repository has a tool to transcript English word to Japanese Katakana expression.
In Japanese, Katakana is a good sound expression for a foreign word.
This tool doesn't translate but gives a sound counterpart of English word.

This repository provides a commandline interface. Another repository, [https://github.com/yokolet/transcript-web](https://github.com/yokolet/transcript-web), provides GraphQL endpoint.
The web version is live at [https://agile-plateau-86972.herokuapp.com/graphql](https://agile-plateau-86972.herokuapp.com/graphql).

## How it is transcripted

This tool followed the method described in the document, [Japanese/Transcribing English to Japanese](https://en.wikibooks.org/wiki/Japanese/Transcribing_English_to_Japanese).

As in the document, the transcription is done in 6 steps:

1. English word to IPA phonetics representaion

    This step uses CMU-IPA Dictionary (see [cmu_dict/README.md](cmu_dict/README.md)) to get
    IPA phonetics. The dictionary has only a subset of whole English words. If the dictionary
    doesn't have the given word, this tool returns an error code E_DIC.

2. Transform vowels in IPA phonetics

    Vowel symbols in IPA phonetics will be converted to Japanese vowel counterparts.
    CMU-IPA Dictionary has a bit different set of vowel symbols compared to the document.
    Some are elaborated conversions.

    This is the most difficult and crucial part for the transcription. The result still has a lot
    of rooms to improve.

3. Transform consonants in IPA phontics

    Consonant sumbols in IPA phonetics will be converted to Japanese consonant counterparts.
    In this step, so-called, "double voiceless obstruents (geminate)" such as p, t, k was added. Examples are:
    pop -> poppu, cat -> kyatto.

4. Add epepntheic vowels

    Japanese word syllables consist of only vowel, consonant followed by vowel or (moraic or final) N.
    In this step, additional vowels are added.

5. Break into morae

    To convert to Katakana, a set of symbols will be broken into fragments, which is called "morae."
    Each mora is consist either of a consonant + single vowel, a single vowel, (moraic or final) N,
    or single consonant for a geminate one.

6. Map morae to Katakana

    Each mora will be mapped to Katakana in this step. While converting, gemimate consonant becomes
    "ッ", and double sound becomes "ー".
    Otherwise, all fragments are coverted to Katakana found in the map.


## Considerations

This tool uses American pronouciation for the easy access to the free dictionary.
However, Japanese sounds are sometime not like American English. Perhaps, British English
dictionary may give better Katakana. Often, a Katakana transcription looks not natural, for example,
twitter -> トウィター but actually it should be ツイッター.

## How to use

### Prerequisite
- Python 3

### Intallation

```bash
pip install -r requirements.txt
```

### Usage

```
eng_to_kana/eng_to_kana.py word1 word2 word3 ...
```

### Error code
- E_DIC: given word is not in CMU-IPA Dictionary
- E_KEY: an error from transcription process

### Example

```
$ eng_to_kana/eng_to_kana.py where amazon apple facebook google microsoft twitter
['where', 'amazon', 'apple', 'facebook', 'google', 'microsoft', 'twitter']
[['ウェアー', 'ホウェアー'], ['アマゾン'], ['アップル'], ['E_DIC'], ['グーグル'], ['マイクローソフト'], ['トウィター']]
```

## Contributing

Contributions are welcome!

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Credits

Yoko Harada (@yokolet)

## License

The MIT License (MIT)

Copyright (c) 2019 Yoko Harada

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.