import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictmeasure')))

import dictmeasure

class TestCountLeafNodes(unittest.TestCase):

    def test1(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v'}
        expected = 3
        actual = dictmeasure.count_leaf_nodes(dict)
        self.assertEqual(expected, actual)

class TestGetLeafChars(unittest.TestCase):

    def test_with_jpn(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': 'キー３の値'}
        expected = 24
        actual = dictmeasure.get_leaf_chars(dict)
        self.assertEqual(expected, actual)

    def test_with_num(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': 'キー３の値', 'key4': 12345}
        expected = 29
        actual = dictmeasure.get_leaf_chars(dict)
        self.assertEqual(expected, actual)

class TestGetLeafBytes(unittest.TestCase):

    def test_with_jpn(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': 'キー３の値'}
        expected = 34
        actual = dictmeasure.get_leaf_bytes(dict)
        self.assertEqual(expected, actual)

    def test_with_num(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': 'キー３の値', 'key4': 12345}
        expected = 39
        actual = dictmeasure.get_leaf_bytes(dict)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()