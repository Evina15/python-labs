'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

import unittest

class test_simple_calculation(unittest.TestCase):
    def test_add_two_number(self):
        self.assertEqual(adding_number(2,2),4)

    def test_input_not_number(self):
        with self.assertRaises(ValueError):
            adding_number("two", "three")

if __name__ == "__main__":
    unittest.main()