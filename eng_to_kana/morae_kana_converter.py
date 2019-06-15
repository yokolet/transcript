class MoraeKanaConverter:
    def __init__(self):
        self.vowels = 'aeiou'
        self.mora_map = {
            'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ',
            'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ', 'ko': 'コ',
            'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
            'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ',
            'kwa': 'クァ', 'kwi': 'クィ', 'kwu': 'クゥ', 'kwe': 'クェ', 'kwo': 'クォ',
            'gya': 'ギャ', 'gyu': 'ギュ', 'gyo': 'ギョ',
            'gwa': 'グァ', 'gwi': 'グィ', 'gwu': 'グゥ', 'gwe': 'グェ', 'gwo': 'グォ',
            'sa': 'サ', 'si': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ',
            'sha': 'シャ', 'shi': 'シ', 'shu': 'シュ', 'she': 'シェ', 'sho': 'ショ',
            'ja': 'ジャ', 'ji': 'ジ', 'ju': 'ジュ', 'je': 'ジェ', 'jo': 'ジョ',
            'jya': 'ジャ', 'jyu': 'ジュ', 'jyo': 'ジョ',
            'za': 'ザ', 'zi':'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ',
            'zya': 'ジャ', 'zyu': 'ジュ', 'zyo': 'ジョ',
            'ta': 'タ', 'ti': 'ティ', 'tu': 'ツ', 'te': 'テ', 'to': 'ト',
            'cha': 'チャ', 'chi': 'チ', 'chu': 'チュ', 'che': 'チェ', 'cho': 'チョ',
            'da': 'ダ', 'di': 'ディ', 'du': 'ドゥ', 'de': 'デ', 'do': 'ド',
            'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
            'nya': 'ニャ', 'nyi': 'ニィ', 'nyu': 'ニュ', 'nye': 'ニェ', 'nyo': 'ニョ',
            'ha': 'ハ', 'hi': 'ヒ', 'hu': 'フ', 'he': 'ヘ', 'ho': 'ホ',
            'hya': 'ヒャ', 'hyu': 'ヒュ', 'hyo': 'ヒョ',
            'fa': 'ファ', 'fi': 'フィ', 'fu': 'フ', 'fe': 'フェ', 'fo': 'フォ',
            'fya': 'フャ', 'fyi': 'フィ', 'fyu': 'フュ', 'fye': 'フェ', 'fyo': 'フョ',
            'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ',
            'bya': 'ビャ', 'byi': 'ビィ', 'byu': 'ビュ', 'bye': 'ビェ', 'byo': 'ビョ',
            'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ',
            'pya': 'ピャ', 'pyu': 'ピュ', 'pyo': 'ピョ',
            'ma': 'マ', 'mi': 'ミ', 'mu': 'ム', 'me': 'メ', 'mo': 'モ',
            'mya': 'ミャ', 'myu': 'ミュ', 'myo': 'ミョ',
            'ya': 'ヤ', 'yi':'イ', 'yu': 'ユ', 'ye': 'イェ', 'yo': 'ヨ',
            'ra': 'ラ', 'ri': 'リ', 'ru': 'ル', 're': 'レ', 'ro': 'ロ',
            'rya': 'リャ', 'ryu': 'リュ', 'ryo': 'リョ',
            'wa': 'ワ', 'wi': 'ウィ', 'wu': 'ウ', 'we': 'ウェ', 'wo': 'ウォ',
            'N': 'ン'
        }
        self.doubled = 'ー'
        self.geminate = 'ッ'

    def convertMorae(self, morae):
        sounds = morae.split('.')
        result = self.mora_map[sounds[0]]
        for idx in range(1, len(sounds)):
            if sounds[idx] in self.vowels and sounds[idx-1][-1] == sounds[idx]:
                result += self.doubled
            elif sounds[idx] not in self.vowels and idx+1 < len(sounds) and \
                sounds[idx] == sounds[idx+1][0]:
                result += self.geminate
            else:
                result += self.mora_map[sounds[idx]]
        return result


