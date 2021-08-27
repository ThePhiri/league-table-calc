import unittest
from table_generator import *
import os


class TestTableGenerator(unittest.TestCase):
    def test_readfile(self):
        r = TableGenerator()
        read = r.readFile('test-input.txt')
        self.assertDictEqual(
            read, {'Lions': 0, 'Snakes': 3})


class TestShowRanking(unittest.TestCase):
    def test_sortResults(self):
        r = ShowRanking()
        test = r.sortResults()
        self.assertEqual(
            test, [('Snakes', 3), ('Lions', 0)])

    def test_writeResults(self):
        self.assertTrue(os.path.exists('output.txt'))


if __name__ == '__main__':
    unittest.main()
