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

if __name__ == "__main__":
    unittest.main()