import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictmeasure')))

import dictmeasure

class TestCountLeafs(unittest.TestCase):

    def test_count_leafs(self):
        
        dict = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}, 'key2': 'key2v'}
        expected = 3
        actual = dictmeasure.count_leafs(dict)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()