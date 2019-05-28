class TransEpentheticVowel:
    def __init__(self):
        self.vowels = 'aeiou'
        self.consym = 'bdfghkmprstz'

    def dt_rule(self, ph, p_idx):
        # d, t
        if p_idx == len(ph)-1:
            return ph[p_idx] + 'o'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] not in self.vowels:
            return ph[p_idx] + 'o'
        else:
            return ph[p_idx]

    def bfmprz_rule(self, ph, p_idx):
        # b, f, m, p, r, z
        if p_idx == len(ph)-1:
            return ph[p_idx] + 'u'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] not in self.vowels:
            return ph[p_idx] + 'u'
        else:
            return ph[p_idx]

    def kg_rule(self, ph, p_idx):
        # k, g
        if p_idx == len(ph)-1:
            return ph[p_idx] + 'u'
        elif p_idx+1 < len(ph) and ph[p_idx] != ph[p_idx+1] and \
            ph[p_idx+1] != 'y' and ph[p_idx+1] not in self.vowels:
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

    def transEpentheticVowel(self, ph):
        # 'bdfghkmprstz'
        epenthetic_map = {
            'b': self.bfmprz_rule,
            'd': self.dt_rule,
            'f': self.bfmprz_rule,
            'g': self.kg_rule,
            'h': self.h_rule,
            'k': self.kg_rule,
            'm': self.bfmprz_rule,
            'p': self.bfmprz_rule,
            'r': self.bfmprz_rule,
            's': self.s_rule,
            't': self.dt_rule,
            'z': self.bfmprz_rule
        }
        result = ''
        p_idx = 0
        while p_idx < len(ph):
            while p_idx < len(ph) and ph[p_idx] not in self.consym:
                result += ph[p_idx]
                p_idx += 1
            
            if p_idx < len(ph) and ph[p_idx] in self.consym:
                result += epenthetic_map[ph[p_idx]](ph, p_idx)
                p_idx += 1
        return result