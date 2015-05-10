import unittest
from warm_ups import factorial
from warm_ups import fibonacci
from warm_ups import sum_of_digits
from warm_ups import sum_of_digits2
from warm_ups import fact_digits
from warm_ups import palindrome
from warm_ups import to_digits2
from warm_ups import to_digits
from warm_ups import to_number
from warm_ups import fibonacci_number
from warm_ups import count_consonants
from warm_ups import count_vowels
from warm_ups import is_increasing
from warm_ups import is_decreasing
from warm_ups import next_hack
from warm_ups import p_score
from warm_ups import char_histogram


class TestWarmUps(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(24, factorial(4))

    def test_fibbonaci(self):
        self.assertEqual([1], fibonacci(1))
        self.assertEqual([], fibonacci(0))
        self.assertEqual([1, 1], fibonacci(2))
        self.assertEqual([1, 1, 2, 3], fibonacci(4))

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123456), 21)
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(111), 3)

    def test_sum_of_digits2(self):
        self.assertEqual(sum_of_digits2(123456), 21)
        self.assertEqual(sum_of_digits2(0), 0)
        self.assertEqual(sum_of_digits2(-111), 3)

    def test_fact_digits(self):
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)
        self.assertEqual(fact_digits(0), 0)

    def test_palindrome(self):
        self.assertTrue(palindrome("kapak"))
        self.assertTrue(palindrome(0))
        self.assertTrue(palindrome(11))
        self.assertTrue(palindrome(1110111))
        self.assertFalse(palindrome("ko"))

    def test_to_digits(self):
        self.assertEqual(to_digits(112), [1, 1, 2])
        self.assertEqual(to_digits2(10002), [1, 0, 0, 0, 2])

    def test_to_number(self):
        self.assertEqual(to_number([1, 2, 3]), 123)
        self.assertEqual(to_number([1, 22, 3]), 1223)
        self.assertEqual(to_number([]), 0)

    def test_fib_number(self):
        self.assertEqual(fibonacci_number(3), 112)
        self.assertEqual(fibonacci_number(10), 11235813213455)
        self.assertEqual(fibonacci_number(0), 0)
        self.assertEqual(fibonacci_number(1), 1)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(count_vowels("grrrrgh!"), 0)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)
        self.assertEqual(count_consonants("Theistareykjarbunga"), 11)

    def test_increasing_sequence(self):
        self.assertTrue(is_increasing([]))
        self.assertTrue(is_increasing([1]))
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))
        self.assertFalse(is_increasing([5, 6, -10]))
        self.assertFalse(is_increasing([1, 1, 1, 1]))

    def test_decreasing_sequence(self):
        self.assertTrue(is_decreasing([]))
        self.assertTrue(is_decreasing([1]))
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))
        self.assertFalse(is_decreasing([1, 1, 1, 1]))

    def test_next_hack_number(self):
        self.assertEqual(next_hack(0), 1)
        self.assertEqual(next_hack(10), 21)
        self.assertEqual(next_hack(8031), 8191)

    def test_char_histogram(self):
        pass

    def test_palindrome_score(self):
        pass

if __name__ == '__main__':
    unittest.main()
