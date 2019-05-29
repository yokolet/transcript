class VowelConverter:
    def __init__(self):
        self.vowels = 'aeiou'
        self.vowsyms = 'aɑʌɚæeɛɪijɔoʊuw'

    def wir_rule(self, word, w_idx):
        # wɪɹ
        return 'uiaa'

    def wi_rule(self, word, w_idx):
        # wɪ
        return 'ui'

    def wu_rule(self, word, w_idx):
        # wʊ
        return 'u'

    def aj_rule(self, word, w_idx):
        # aj
        return 'ai'
    
    def ar_rule(self, word, w_idx):
        # ɑɹ
        return 'aa'

    def aw_rule(self, word, w_idx):
        # aw
        return 'au'

    def a_short_rule(self, word, w_idx):
        # ɑ
        if word[w_idx] == 'o':
            return 'o'
        else:
            return 'a'

    def a_long_rule(self, word, w_idx):
        # ɚ
        return 'aa'

    def ae_rule(self, word, w_idx):
        # æ
        if w_idx >= 1 and (word[w_idx-1] == 'c' or word[w_idx-1] == 'g'):
            return 'ya'
        else:
            return 'a'
    
    def hat_rule(self, word, w_idx):
        # ʌ
        if w_idx+1 < len(word) and word[w_idx] == 'o' and word[w_idx+1] == 'u':
            return 'a'
        elif w_idx+1 < len(word) and word[w_idx] == 'i' and word[w_idx+1] == 'o':
            return 'o'
        elif w_idx > 0 and word[w_idx] == 'e' and word[w_idx-1] == 'l':
            return 'u'
        elif word[w_idx] == 'o':
            return 'o'
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

    def i_long_rule(self, word, w_idx):
        # i
        return 'ii'

    def i_short_rule(self, word, w_idx):
        # ɪ
        return 'i'

    def ju_rule(self, word, w_idx):
        # ju
        return 'yuu'
    
    def ji_rule(self, word, w_idx):
        # ji
        return 'ii'

    def je_rule(self, word, w_idx):
        # jɛ
        return 'ie'

    def oj_rule(self, word, w_idx):
        # ɔj
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
        return 'o'

    def ur_rule(self, word, w_idx):
        # ʊɹ
        return 'uaa'

    def u_short_rule(self, word, w_idx):
        # ʊ
        return 'u'

    def u_long_rule(self, word, w_idx):
        # u
        return 'uu'

    def convertVowel(self, word, ph):
        vowel_map = {
            'wɪɹ': self.wir_rule,
            'wɪ': self.wi_rule,
            'wʊ': self.wu_rule,
            'aj': self.aj_rule,
            'ɑɹ': self.ar_rule,
            'aw': self.aw_rule,
            'ɑ': self.a_short_rule,
            'ɚ': self.a_long_rule,
            'æ': self.ae_rule,
            'ʌ': self.hat_rule,
            'ej': self.ej_rule,
            'ɛɹ': self.er_rule,
            'ɛ': self.e_rule,
            'ɪɹ': self.ir_rule,
            'i': self.i_long_rule,
            'ɪ': self.i_short_rule,
            'ju': self.ju_rule,
            'ji': self.ji_rule,
            'jɛ': self.je_rule,
            'ɔj': self.oj_rule,
            'ɔɹ': self.or_rule,
            'ow': self.ow_rule,
            'ɔ': self.o_rule,
            'ʊɹ': self.ur_rule,
            'ʊ': self.u_short_rule,
            'u': self.u_long_rule
        }
        result = ''
        w_idx, p_idx = 0, 0
        while w_idx < len(word) and p_idx < len(ph):
            # skips consonant in a word
            while w_idx < len(word) and word[w_idx] not in self.vowels:
                w_idx += 1
            
            # adds consonant phonetics to the result, but does nothing for now
            while p_idx < len(ph) and ph[p_idx] not in self.vowsyms:
                result += ph[p_idx]
                p_idx += 1

            # convert vowel phonetics
            if p_idx+3 <= len(ph) and ph[p_idx:p_idx+3] in vowel_map:
                result += vowel_map[ph[p_idx:p_idx+3]](word, w_idx)
                p_idx += 3
            elif p_idx+2 <= len(ph) and ph[p_idx:p_idx+2] in vowel_map:
                result += vowel_map[ph[p_idx:p_idx+2]](word, w_idx)
                p_idx += 2
            elif p_idx < len(ph) and ph[p_idx] in vowel_map:
                result += vowel_map[ph[p_idx]](word, w_idx)
                p_idx += 1
            
            # skips vowel chars
            while w_idx < len(word) and word[w_idx] in self.vowels:
                w_idx += 1
        while p_idx < len(ph):
            result += ph[p_idx]
            p_idx += 1
        return result