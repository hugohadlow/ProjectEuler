import unittest
from functions import functions

class Tests(unittest.TestCase):
    def testSumMultiples(self):
        self.assertEqual(23, functions.sumMultiples([3, 5], 10))
        self.assertEqual(233168, functions.sumMultiples([3, 5], 1000))

    def testSumEvenTerms(self):
        self.assertEqual(30, functions.sumEvenTerms([1,2,3,4,5,6,7,8,9,10]))

    def testFibonacci(self):
        self.assertEqual([1,2,3,5,8,13,21], functions.fibonacci(21))

    def testNextPrime_1(self):
        self.assertEqual(2, functions.nextPrime([]))

    def testNextPrime_2(self):
        self.assertEqual(17, functions.nextPrime([2, 3, 5, 7, 11, 13]))

    def testPrimes(self):
        self.assertEqual([2, 3, 5, 7, 11, 13], functions.primes(13))

    def testPrimeFactors_1(self):
        self.assertEqual([13], functions.primeFactors(13))

    def testPrimeFactors_1(self):
        self.assertEqual([2,3], functions.primeFactors(6))

    def testPrimeFactors_2(self):
        self.assertEqual([2,2,3], functions.primeFactors(12))

    def testPalindrome(self):
        self.assertTrue(functions.palindrome(121))
        self.assertFalse(functions.palindrome(123))
        self.assertTrue(functions.palindrome(1221))
        self.assertFalse(functions.palindrome(1222))
        self.assertFalse(functions.palindrome(1231))

    def testLargestPalindromeProduct(self):
        self.assertEqual(9009, functions.largestPalindromeProduct(2))

    def testSmallestMultiple(self):
        self.assertEqual(2520, functions.smallestMultiple(10))

