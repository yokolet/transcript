import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from eng_to_kana.morae_kana_converter import MoraeKanaConverter

class TestMoraeKanaConverter(unittest.TestCase):
    def setUp(self):
        self.func = MoraeKanaConverter().convertMorae

    def test_1(self):
        expected_pairs = {
            'fa.za.a': 'ファザー',
            'a.a.mu': 'アーム',
            'ko.ma.N.da.a': 'コマンダー',
            'shi.i': 'シー',
            'pi.g.gu': 'ピッグ',
            'be.d.do': 'ベッド',
            'ba.a.do': 'バード',
            'ha.N.ba.a.ga.a': 'ハンバーガー',
            'kya.t.to': 'キャット',
            'gya.N.bu.ru': 'ギャンブル',
            'gya.ru': 'ギャル',
            'ka.N.to.ri.i': 'カントリー',
            'mo.N.ki.i': 'モンキー',
            'fu.ro.N.to': 'フロント',
            'ro.N.do.N': 'ロンドン',
            'bo.k.ku.su': 'ボックス',
            'su.to.ro': 'ストロ',
            'po.o.to': 'ポート',
            'bu.k.ku': 'ブック',
            'ba.ru.u.N': 'バルーン',
            'a.ba.u.to': 'アバウト',
            'pa.i.ro.t.to': 'パイロット',
            'wi.na.a': 'ウィナー',
            'ma.ma': 'ママ',
            'pu.u.ma': 'プーマ',
            'de.i': 'デイ',
            'de.i.bi.d.do': 'デイビッド',
            'ma.i': 'マイ',
            'bo.i': 'ボイ',
            'to.i': 'トイ',
            'fo.o.N': 'フォーン',
            'no.o': 'ノー',
            'na.u': 'ナウ',
            'kwi.a.a': 'クィアー',
            'he.a.a': 'ヘアー',
            'tu.a.a': 'ツアー', 
            'kyu.u.bu': 'キューブ',
            'a.ma.zo.N': 'アマゾン',
            'bo.k.ku.si.N.gu': 'ボックシング',
            'gu.u.gu.ru': 'グーグル',
            'ma.i.ku.ro.o.so.fu.to': 'マイクローソフト',
            'ne.i.sho.N': 'ネイション',
            'ro.o.ma': 'ローマ',
            'wu.d.do': 'ウッド',
            'wu.z.zu': 'ウッズ',
            'si.N': 'シン',
            're.fu.to': 'レフト',
            'mi.ru.ku': 'ミルク',
            'so.N.gu': 'ソング',
            'da.a.ri.N.gu': 'ダーリング',
            'i.i.su.to': 'イースト',
            'i.e.su': 'イエス',
            'hu.u.pu': 'フープ',
            'po.p.pu': 'ポップ',
            'ka.t.to': 'カット',
            'pa.k.ku': 'パック',
            'ki.su': 'キス',
            'pa.c.chi': 'パッチ',
            'me.s.shu': 'メッシュ'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_2(self):
        expected_pairs = {
            'wa.t.to': 'ワット',
            'ho.wa.t.to': 'ホワット',
            'wi.i.to': 'ウィート',
            'ho.wi.i.to': 'ホウィート',
            'wi.i.za.zu': 'ウィーザズ',
            'ho.wi.i.za.zu': 'ホウィーザズ',
            'wi.i.zi.zu': 'ウィージズ',
            'we.N': 'ウェン',
            'ho.we.N': 'ホウェン',
            'wi.N': 'ウィン',
            'ho.wi.N': 'ホウィン',
            'wu.u': 'ウー',
            'ho.wu.u': 'ホウー',
            'hyu.u': 'ヒュー',
            'wi.c.chi': 'ウィッチ',
            'ho.wi.c.chi': 'ホウィッチ',
            'wa.i.ti.i': 'ワイティー',
            'ho.wa.i.ti.i': 'ホワイティー',
            'wo.o': 'ウォー',
            'ho.wo.o': 'ホウォー',
            'ho.o': 'ホー',
            'wa.i': 'ワイ',
            'ho.wa.i': 'ホワイ',
            'wi.zu': 'ウィズ',
            'wi.su': 'ウィス'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_3(self):
        expected_pairs = {
            'a.jo.i.N': 'アジョイン',
            'e.ri.i.a': 'エリーア',
            'ba.N.kwe.t.to': 'バンクェット',
            'kya.ri.j.ji': 'キャリッジ',
            'ke.a.a.ji': 'ケアージ',
            'e.j.ji': 'エッジ',
            'da.i.e.t.to': 'ダイエット',
            'jya.j.ji': 'ジャッジ',
            'ma.jo.ri.ti.i': 'マジョリティー',
            'myu.u.to': 'ミュート',
            'o.ra.N.ji': 'オランジ',
            'o.ri.N.ji': 'オリンジ',
            'po.o.e.t.to': 'ポーエット',
            'kwa.k.ku': 'クァック',
            'kwe.i.ku': 'クェイク',
            'kwi.i.ri.i': 'クィーリー',
            'kwi.i.N': 'クィーン',
            'kwa.i.e.t.to': 'クァイエット',
            'kwi.p.pu': 'クィップ',
            'kwo.o.ta': 'クォータ',
            'kwo.o.to': 'クォート',
            'so.ro.o': 'ソロー',
            'wi.ji.t.to': 'ウィジット'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_4(self):
        expected_pairs = {
            'ko.ru': 'コル',
            'di.d.do': 'ディッド',
            'fi.N.ga.a': 'フィンガー',
            'hi.a.a': 'ヒアー',
            'a.i.do.ru': 'アイドル',
            're.i.di.i': 'レイディー',
            'ri.to.ru': 'リトル',
            'ma.za.a': 'マザー',
            'pu.re.ja.a': 'プレジャー',
            'pyu.a.a': 'ピュアー',
            'tu.ri.su.to': 'ツリスト',
            'bi.jo.N': 'ビジョン'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_5(self):
        expected_pairs = {
            'a.be.i.jya.a': 'アベイジャー',
            'a.kyu.a.si.i.zu': 'アキュアシーズ',
            'e.i.na.a': 'エイナー',
            'e.nye.i': 'エニェイ',
            'e.i.ku.na.a': 'エイクナー',
            'a.ki.i.ya.ma': 'アキーヤマ',
            'a.re.i.yo.o': 'アレイヨー',
            'a.u.ga.su.ti.ni.i.a.k.ku': 'アウガスティニーアック',
            'a.bi.nyo.N': 'アビニョン',
            'a.i.ya.s.shu': 'アイヤッシュ',
            'bo.o.ryu': 'ボーリュ',
            'bi.i.di.e.N.to': 'ビーディエント',
            'ka.mo.N': 'カモン',
            'cho.i.na.t.to.su.ki.i': 'チョイナットスキー',
            'do.ra.i.bu': 'ドライブ',
            'da.k.ku.ta.a': 'ダックター',
            'fi.ri.i.a.bu': 'フィリーアブ',
            'fi.ryo.o': 'フィリョー',
            'fa.i.ti.k.ku': 'ファイティック',
            'ho.re.i.ji': 'ホレイジ'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_6(self):
        expected_pairs = {
            'a.pu.ro.o.do': 'アプロード',
            'a.p.pu.ru': 'アップル',
            'a.p.pu.ru.bi.i': 'アップルビー',
            'a.pu.re.t.to': 'アプレット',
            'a.pu.ri.ke.i.sho.N': 'アプリケイション',
            'a.pu.ra.i': 'アプライ',
            'pa.i.na.p.pu.ru': 'パイナップル'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

    def test_7(self):
        expected_pairs = {
            'a.bu.ri.j.ji.do': 'アブリッジド',
            'a.bu.ri.j.ji.me.N.to': 'アブリッジメント',
            'a.byu.u.ra.z.zi.i': 'アビューラッジー',
            'a.byu.u.su': 'アビュース',
            'a.byu.u.zu': 'アビューズ',
            'ko.N.fyu.u.zu': 'コンフューズ',
            'fyu.u': 'フュー',
            'ye.i': 'イェイ'
        }
        for key, value in expected_pairs.items():
            self.assertEqual(value, self.func(key))

if __name__ == '__main__':
    unittest.main()