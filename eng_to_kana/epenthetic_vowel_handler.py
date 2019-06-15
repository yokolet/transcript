class EpentheticVowelHandler:
    def __init__(self):
        self.vowels = 'aeiou'
        self.consym = 'bdfghjkmprstz'

    def dt_rule(self, ph, p_idx):
        # d, t
        if p_idx == len(ph)-1:
            return ph[p_idx] + 'o'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] not in self.vowels:
            return ph[p_idx] + 'o'
        else:
            return ph[p_idx]

    def bfprz_rule(self, ph, p_idx):
        # b, f, p, r, z
        if p_idx == len(ph)-1:
            return ph[p_idx] + 'u'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] != 'y' and ph[p_idx+1] not in self.vowels:
            return ph[p_idx] + 'u'
        else:
            return ph[p_idx]

    def kgm_rule(self, ph, p_idx):
        # k, g, m
        if p_idx == len(ph)-1:
            return ph[p_idx] + 'u'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] != 'y' and ph[p_idx+1] != 'w' \
            and ph[p_idx+1] not in self.vowels:
            return ph[p_idx] + 'u'
        else:
            return ph[p_idx]

    def h_rule(self, ph, p_idx):
        # cch, ssh
        if p_idx >= 1 and ph[p_idx-1] == 'c' and \
            (p_idx == len(ph) - 1 or ph[p_idx+1] not in self.vowels):
            return 'hi'
        elif p_idx >= 1 and ph[p_idx-1] == 's' and \
            (p_idx == len(ph) - 1 or ph[p_idx+1] not in self.vowels):
            return 'hu'
        elif p_idx+1 < len(ph) and ph[p_idx+1] == 'w':
            return 'ho'
        else:
            return 'h'

    def s_rule(self, ph, p_idx):
        if p_idx == len(ph)-1:
            return 'su'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] != 'h' and ph[p_idx+1] not in self.vowels:
            return 'su'
        else:
            return 's'

    def j_rule(self, ph, p_idx):
        if p_idx == len(ph) - 1:
            return 'ji'
        elif p_idx+1 < len(ph) and ph[p_idx+1] not in self.vowels:
            if ph[p_idx+1] == 'j' or ph[p_idx+1] == 'y':
                return 'j'
            else:
                return 'ji'
        else:
            return 'j'

    def addEpentheticVowel(self, ph):
        # 'bdfghkmprstz'
        epenthetic_map = {
            'b': self.bfprz_rule,
            'd': self.dt_rule,
            'f': self.bfprz_rule,
            'g': self.kgm_rule,
            'h': self.h_rule,
            'j': self.j_rule,
            'k': self.kgm_rule,
            'm': self.kgm_rule,
            'p': self.bfprz_rule,
            'r': self.bfprz_rule,
            's': self.s_rule,
            't': self.dt_rule,
            'z': self.bfprz_rule
        }
        result = ''
        p_idx = 0
        while p_idx < len(ph):
            while p_idx < len(ph) and ph[p_idx] not in self.consym:
                # skip if the same vowel continues more than two
                if p_idx >= 2 and ph[p_idx] == ph[p_idx-1] and ph[p_idx] == ph[p_idx-2]:
                    pass # no-op
                else:
                    result += ph[p_idx]
                p_idx += 1
            
            if p_idx < len(ph) and ph[p_idx] in self.consym:
                result += epenthetic_map[ph[p_idx]](ph, p_idx)
                p_idx += 1
        return result