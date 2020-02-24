'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest

def divide_multiply(x, y, z):
    try:
        result_ = x/(y*z)
        return result_
    except ZeroDivisionError:
        return "This will cause error because either x or y is 0."

class test_divide_multiply(unittest.TestCase):
    def test_correct_results(self):
        self.assertEqual(divide_multiply(30, 5, 3), 2)

    def test_raises_division_by_zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide_multiply(20, 0, 8)

    def test_raises_argument_not_found(self):
        with self.assertRaises(TypeError):
            divide_multiply(2, 3)


if __name__ == "__main__":
    unittest.main()



