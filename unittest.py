import unittest

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Bilangan harus non-negatif")
    else:
        return number ** 0.5

class TestSquareRoot(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(calculate_square_root(9), 3)
        
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_square_root(-9)

if __name__ == '__main__':
    unittest.main()
