# 参考
# (絵文字のバイト数について)
# https://www.softel.co.jp/blogs/tech/archives/596
# https://qiita.com/comware_harase/items/59c60ab1c6e1797f0821

import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictmeasure')))

import dictmeasure

class TestGetTextChars(unittest.TestCase):

    def test_ascii(self):
        actual = dictmeasure.get_text_chars('abcd')
        expected = 4
        self.assertEqual(expected, actual)

    def test_utf8_hiragana(self):
        actual = dictmeasure.get_text_chars('あいうえお')
        expected = 5
        self.assertEqual(expected, actual)

    def test_utf8_kanji(self):
        actual = dictmeasure.get_text_chars('壱弐参四伍')
        expected = 5
        self.assertEqual(expected, actual)

    def test_utf8_4bytes(self):
        actual = dictmeasure.get_text_chars('𠀋𡈽𡌛𡑮𡢽')
        expected = 5
        self.assertEqual(expected, actual)

    def test_utf8_emoji_1(self):
        actual = dictmeasure.get_text_chars('🇯🇵')
        expected = 2
        self.assertEqual(expected, actual)

    def test_utf8_emoji_2(self):
        actual = dictmeasure.get_text_chars('👨🏻‍🦱')
        expected = 4
        self.assertEqual(expected, actual)

class TestGetNumberChars(unittest.TestCase):
    
        def test_none(self):
            actual = dictmeasure.get_number_chars(None)
            expected = 0
            self.assertEqual(expected, actual)
    
        def test_zero(self):
            actual = dictmeasure.get_number_chars(0)
            expected = 1
            self.assertEqual(expected, actual)
    
        def test_positive(self):
            actual = dictmeasure.get_number_chars(12345)
            expected = 5
            self.assertEqual(expected, actual)
    
        def test_negative(self):
            actual = dictmeasure.get_number_chars(-12345)
            expected = 6
            self.assertEqual(expected, actual)
    
        def test_float(self):
            actual = dictmeasure.get_number_chars(123.45)
            expected = 6
            self.assertEqual(expected, actual)

class TestGetTextBytes(unittest.TestCase):

    def test_ascii(self):
        actual = dictmeasure.get_text_bytes('abcd')
        expected = 4
        self.assertEqual(expected, actual)

    def test_utf8_hiragana(self):
        actual = dictmeasure.get_text_bytes('あいうえお')
        expected = 15
        self.assertEqual(expected, actual)

    def test_utf8_kanji(self):
        actual = dictmeasure.get_text_bytes('壱弐参四伍')
        expected = 3*5
        self.assertEqual(expected, actual)

    def test_utf8_4bytes(self):
        actual = dictmeasure.get_text_bytes('𠀋𡈽𡌛𡑮𡢽')
        expected = 4*5
        self.assertEqual(expected, actual)

    def test_mix_1(self):
        actual = dictmeasure.get_text_bytes('壱1弐2参3四4伍5')
        expected = 15 + 5
        self.assertEqual(expected, actual)

    def test_utf8_emoji_1(self):
        actual = dictmeasure.get_text_bytes('🇯🇵')
        expected = 8
        self.assertEqual(expected, actual)

    def test_utf8_emoji_2(self):
        actual = dictmeasure.get_text_bytes('👨🏻‍🦱')
        expected = 15
        self.assertEqual(expected, actual)

class TestGetNumberBytes(unittest.TestCase):
        
    def test_none(self):
        actual = dictmeasure.get_number_bytes(None)
        expected = 0
        self.assertEqual(expected, actual)

    def test_zero(self):
        actual = dictmeasure.get_number_bytes(0)
        expected = 1
        self.assertEqual(expected, actual)

    def test_positive(self):
        actual = dictmeasure.get_number_bytes(12345)
        expected = 5
        self.assertEqual(expected, actual)

    def test_negative(self):
        actual = dictmeasure.get_number_bytes(-12345)
        expected = 6
        self.assertEqual(expected, actual)

    def test_float(self):
        actual = dictmeasure.get_number_bytes(123.45)
        expected = 6
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()