class MoraeCreator:
    def __init__(self):
        self.vowels = 'aeiou'

    def createMorae(self, ph):
        result = ph[0]
        p_idx = 1
        while p_idx < len(ph):
            # previous char is vowel
            if ph[p_idx-1] in self.vowels:
                result += ('.' + ph[p_idx])
            # previous char is consonant
            else:
                # genimate consonant
                if ph[p_idx-1] == ph[p_idx] or ph[p_idx-1] == 'N':
                    result += ('.' + ph[p_idx])
                else:
                    result += ph[p_idx]
            p_idx += 1
        return result