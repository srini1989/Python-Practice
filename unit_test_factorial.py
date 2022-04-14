import unittest
import math


class TestFactorial(unittest.Testcase()):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test. Any method which starts with 'test_'
        will be considered as test case
        """
        result = math.factorial(5)
        self.assertEqual(result, 120)


if __name__ == "__main__":
    unittest.main()
