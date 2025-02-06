import unittest
from main import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(4)[3], "fizz")
        self.assertEqual(fizzbuzz(7)[6], "fizz")
        self.assertEqual(fizzbuzz(10)[9], "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(6)[5], "buzz")
        self.assertEqual(fizzbuzz(11)[10], "buzz")
        self.assertEqual(fizzbuzz(21)[20], "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(16)[15], "fizzbuzz")
        self.assertEqual(fizzbuzz(31)[30], "fizzbuzz")
        self.assertEqual(fizzbuzz(46)[45], "fizzbuzz")

    def test_numbers(self):
        self.assertEqual(fizzbuzz(2)[1], 1)
        self.assertEqual(fizzbuzz(3)[2], 2)
        self.assertEqual(fizzbuzz(5)[4], 4)

if __name__ == '__main__':
    unittest.main()
