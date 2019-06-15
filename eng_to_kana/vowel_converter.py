class VowelConverter:
    def __init__(self):
        self.vowels = 'aeiou'
        self.vowsyms = 'aɑʌɚæeɛɪijɔoʊu'
        # ʤ, ʤʌʤ

    def aj_rule(self, word, w_idx):
        # aj, ɑj
        return 'ai'
    
    def ar_rule(self, word, w_idx):
        # ɑɹ, ɑw
        return 'aa'

    def aw_rule(self, word, w_idx):
        # aw
        return 'au' # oo?

    def a_short_rule(self, word, w_idx):
        # ɑ
        if w_idx < len(word) and word[w_idx] == 'o':
            return 'o'
        else:
            return 'a'

    def a_long_rule(self, word, w_idx):
        # ɚ
        return 'aa'

    def ae_rule(self, word, w_idx):
        # æ
        if w_idx < len(word) and w_idx >= 1 and (word[w_idx-1] == 'c' or word[w_idx-1] == 'g'):
            return 'ya'
        else:
            return 'a'
    
    def hat_rule(self, word, w_idx):
        # ʌ
        if w_idx+1 < len(word) and word[w_idx] == 'o' and word[w_idx+1] == 'u':
            return 'a'
        elif w_idx+1 < len(word) and word[w_idx] == 'i' and word[w_idx+1] == 'o':
            return 'o'
        elif w_idx > 0 and w_idx < len(word) and word[w_idx] == 'e' and word[w_idx-1] == 'l':
            if w_idx-2 >=0 and word[w_idx-2] in ['d', 't']:
                return 'o'
            elif w_idx+1 < len(word) and word[w_idx+1] == "t":
                return 'e'
            else:
                return 'u'
        elif w_idx > 0 and w_idx < len(word) and word[w_idx] == 'u' and word[w_idx-1] == 'j':
            return 'ya'
        elif w_idx < len(word) and word[w_idx] == 'o' and word != 'mother':
            return 'o'
        elif w_idx < len(word) and word[w_idx] == 'e':
            return 'e'
        elif w_idx < len(word) and word[w_idx] == 'i':
            return 'i'
        else:
            return 'a'

    def ej_rule(self, word, w_idx):
        # ej
        return 'ei'

    def er_rule(self, word, w_idx):
        # ɛɹ
        return 'eaa'

    def e_rule(self, word, w_idx):
        # ɛ
        return 'e'

    def ir_rule(self, word, w_idx):
        # ɪɹ
        return 'iaa'

    def iir_long_rule(self, word, w_idx):
        # iɹ
        return 'iaa'

    def i_long_rule(self, word, w_idx):
        # i
        return 'ii'

    def i_short_rule(self, word, w_idx):
        # ɪ
        return 'i'

    def ja_rule(self, word, w_idx):
        # jʌ
        return 'yaa'

    def ja_short_rule(self, word, w_idx):
        # jɑ, jæ
        return 'ya'

    def jaw_rule(self, word, w_idx):
        # jaw
        return 'yoo'

    def ju_rule(self, word, w_idx):
        # ju
        return 'yuu'

    def ju_short_rule(self, word, e_idx):
        # jɚ, jʊ
        return 'yu'
    
    def ji_rule(self, word, w_idx):
        # ji
        return 'ii'

    def je_rule(self, word, w_idx):
        # jɛ, jɪ
        return 'ie'

    def jej_rule(self, word, w_idx):
        # jej
        return 'yei'

    def jow_rule(self, word, w_idx):
        # jow
        return 'yoo'

    def jo_rule(self, word, w_idx):
        # jɔ
        return 'yo'

    def oj_rule(self, word, w_idx):
        # ɔj, ʌj
        # TODO: sometime, it is "ooi", ex, boy
        return 'oi'

    def or_rule(self, word, w_idx):
        # ɔɹ
        return 'oo'

    def ow_rule(self, word, w_idx):
        # ow
        return 'oo'

    def o_rule(self, word, w_idx):
        # ɔ
        if w_idx+1 < len(word) and word[w_idx] == 'a' and word[w_idx+1] == 'u':
            return 'oo'
        else:
            return 'o'

    def jur_rule(self, word, w_idx):
        # jʊɹ
        return 'yuaa'

    def jsi_rule(self, word, w_idx):
        # jsi
        return 'ji'

    def ur_rule(self, word, w_idx):
        # ʊɹ
        return 'uaa'

    def u_short_rule(self, word, w_idx):
        # ʊ
        return 'u'

    def u_long_rule(self, word, w_idx):
        # u
        return 'uu'

    def j_rule(self, word, w_idx):
        # last j
        return 'ji'

    def convertVowel(self, word, ph):
        vowel_map = {
            'aj': self.aj_rule,
            'ɑj': self.aj_rule,
            'ɑɹ': self.ar_rule,
            'aw': self.aw_rule,
            'ɑw': self.ar_rule,
            'ɑ': self.a_short_rule,
            'ɚ': self.a_long_rule,
            'æ': self.ae_rule,
            'ʌ': self.hat_rule,
            'ej': self.ej_rule,
            'ɛɹ': self.er_rule,
            'ɛ': self.e_rule,
            'ɪɹ': self.ir_rule,
            'i': self.i_long_rule,
            'iɹ': self.ir_rule,
            'ɪ': self.i_short_rule,
            'jʌ': self.ja_rule,
            'jɑ': self.ja_short_rule,
            'jæ': self.ja_short_rule,
            'jaw': self.jaw_rule,
            'ju': self.ju_rule,
            'jɚ': self.ju_short_rule,
            'jʊ': self.ju_short_rule,
            'ji': self.ji_rule,
            'jɪ': self.je_rule,
            'jɛ': self.je_rule,
            'jej': self.jej_rule,
            'jow': self.jow_rule,
            'jɔ': self.jo_rule,
            'jsi': self.jsi_rule,
            'ɔj': self.oj_rule,
            'ʌj': self.oj_rule,
            'ɔɹ': self.or_rule,
            'ow': self.ow_rule,
            'ɔ': self.o_rule,
            'jʊɹ': self.jur_rule,
            'ʊɹ': self.ur_rule,
            'ʊ': self.u_short_rule,
            'u': self.u_long_rule,
            'j': self.j_rule,
        }
        result = ''
        w_idx, p_idx = 0, 0
        while p_idx < len(ph):
            # skips consonant in a word
            # in some cases, y is mapped to vowel sound
            while w_idx < len(word) and word[w_idx] not in self.vowels and \
                word[w_idx] not in ['y', "'"]:
                w_idx += 1
            
            # adds consonant phonetics to the result, but does nothing for now
            while p_idx < len(ph) and ph[p_idx] not in self.vowsyms:
                result += ph[p_idx]
                p_idx += 1

            # convert vowel phonetics
            while p_idx < len(ph) and ph[p_idx] in self.vowsyms:
                if w_idx+1 < len(word) and word[w_idx] == 'u' \
                    and word[w_idx+1] in self.vowels:
                    w_idx += 1
                if p_idx+3 <= len(ph) and ph[p_idx:p_idx+3] in vowel_map:
                    result += vowel_map[ph[p_idx:p_idx+3]](word, w_idx)
                    p_idx += 3
                    w_idx += 1
                elif p_idx+2 <= len(ph) and ph[p_idx:p_idx+2] in vowel_map and \
                    (p_idx+2 == len(ph) or ph[p_idx+1] != 'ɹ' or ph[p_idx+2] not in self.vowsyms):
                    result += vowel_map[ph[p_idx:p_idx+2]](word, w_idx)
                    p_idx += 2
                    w_idx += 1
                elif p_idx < len(ph) and ph[p_idx] in vowel_map:
                    result += vowel_map[ph[p_idx]](word, w_idx)
                    p_idx += 1
                    w_idx += 1
                elif p_idx == len(ph)-1 and ph[p_idx] == 'j':
                    result += vowel_map[ph[p_idx]](word, w_idx)
                    p_idx += 1
                    w_idx += 1

            # skips rest of vowel chars
            while w_idx < len(word) and word[w_idx] in self.vowels:
                w_idx += 1

        # adds rest of consonant symbols
        while p_idx < len(ph):
            result += ph[p_idx]
            p_idx += 1
        return result