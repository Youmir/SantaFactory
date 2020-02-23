from __future__ import absolute_import
import unittest
from classes.factory import *
class FactoryTest(unittest.TestCase):

    def TestSum(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()