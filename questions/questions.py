import unittest
from functions import functions

class Questions(unittest.TestCase):
    def test_question0001(self):
        print(functions.sumMultiples([3, 5], 1000))

    def test_question0002(self):
        print(functions.sumEvenTerms(functions.fibonacci(4000000)))

    def test_question0003(self):
        print(max(functions.primeFactors(600851475143)))

    def test_question0004(self):
        print(functions.largestPalindromeProduct(3))

    def test_question0005(self):
        print(functions.smallestMultiple(20))
