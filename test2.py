import unittest
from main1 import _min, _max, _sum, _mult, read1
import time

chisla = read1("Bigfile.txt")

class Testiki2(unittest.TestCase):
    def test_min(self):
        self.assertEqual(_min(chisla), min(chisla))

    def test_max(self):
        self.assertEqual(_max(chisla), max(chisla))

    def test_sum(self):
        self.assertEqual(_sum(chisla), sum(chisla))

    def test_mult(self):
        mt = 1
        for i in chisla:
            mt = mt*i
        self.assertEqual(_mult(chisla), mt)




if __name__ == '__main__':
    unittest.main()