import unittest
from Validation import *


class Test(unittest.TestCase):
    def test_IsInteger(self):
        for i in {-10, 10}:
            result = Validation.IsNum(i)
            self.assertTrue(result)

    def test_Func(self):
        try:
            result = Validation.Validate("2+x")
            print('Passed valid func')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

        try:
            result = Validation.Validate("2*x+x^2")
            print('Passed valid func')
        except ValueError as e:
            print('Passed invalid func')

        try:
            result = Validation.Validate("2//x+x^2")
            print('Passed valid func')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')
        try:
            result = Validation.Validate("-2*x+x^2")
            self.assertTrue(result)
            print('Passed valid func')

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')

        try:
            result = Validation.Validate("x+x^2")
            self.assertTrue(result)
            print('Passed valid func')

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')

        try:
            result = Validation.Validate("x*2+x^2")
            self.assertTrue(result)
            print('Passed valid func')

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')
        try:
            result = Validation.Validate("3/x+x^2")
            self.assertTrue(result)
            print('Passed valid func')

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')
        try:
            result = Validation.Validate("3^x+x^2")
            self.assertTrue(result)
            print('Passed valid func')

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')
        try:
            result = Validation.Validate("-3/x+x^2")
            self.assertTrue(result)
            print('Passed valid func')

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')

    def test_Inequality(self):
        try:
            result = Validation.validateMaxMinValues(2, 3)

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        try:
            result = Validation.validateMaxMinValues(5, 3)
            self.assertEqual(None, result)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        try:
            result = Validation.validateMaxMinValues(3, 3)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)


if __name__ == '__main__':
    unittest.main()
