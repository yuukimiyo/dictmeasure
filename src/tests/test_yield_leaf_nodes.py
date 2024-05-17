import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictmeasure')))

import dictmeasure

class TestYieldLeafNodes(unittest.TestCase):

    def test1(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v'}
        expected = ['key1-1v', 'key1-2v', 'key2v']
        actual = [x for x in dictmeasure.yield_leaf_nodes(dict)]
        self.assertEqual(expected, actual)

    def test2(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': ['key3-1v', 'key3-2v', {'key3-3': 'key3-3v'}], 'key4': 123}
        expected = ['key1-1v', 'key1-2v', 'key2v', 'key3-1v', 'key3-2v', 'key3-3v', 123]
        actual = [x for x in dictmeasure.yield_leaf_nodes(dict)]
        self.assertEqual(expected, actual)

class TestYieldLeafNodesWithPath(unittest.TestCase):

    def test1(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v'}
        expected = [('key1.key1-1', 'key1-1v'), ('key1.key1-2', 'key1-2v'), ('key2', 'key2v')]
        actual = [x for x in dictmeasure.yield_leaf_nodes_with_path(dict, sep='.')]
        self.assertEqual(expected, actual)

    def test2(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': ['key3-1v', 'key3-2v', {'key3-3': 'key3-3v'}], 'key4': 123}
        expected = [
            ('key1.key1-1', 'key1-1v'),
            ('key1.key1-2', 'key1-2v'),
            ('key2', 'key2v'),
            ('key3', 'key3-1v'),
            ('key3', 'key3-2v'),
            ('key3.key3-3', 'key3-3v'),
            ('key4', 123)
            ]
        actual = [x for x in dictmeasure.yield_leaf_nodes_with_path(dict)]
        self.assertEqual(expected, actual)

    def test3(self):
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v', 'key3': ['key3-1v', 'key3-2v', {'key3-3': 'key3-3v'}]}
        expected = [
            ('key1.key1-1', 'key1-1v'),
            ('key1.key1-2', 'key1-2v'),
            ('key2', 'key2v'),
            ('key3.[0]', 'key3-1v'),
            ('key3.[1]', 'key3-2v'),
            ('key3.[2].key3-3', 'key3-3v')
            ]
        actual = [x for x in dictmeasure.yield_leaf_nodes_with_path(dict, withListIndex=True)]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()