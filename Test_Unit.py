import unittest

# Fungsi sederhana yang akan diuji
def add(a, b):
    return a + b

# Kelas turunan dari unittest.TestCase
class TestAddFunction(unittest.TestCase):
    
    # Fungsi pengujian untuk kasus uji pertama
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)  # Memastikan bahwa hasil sesuai dengan yang diharapkan
    
    # Fungsi pengujian untuk kasus uji kedua
    def test_add_negative_numbers(self):
        result = add(-1, 1)
        self.assertEqual(result, 0)  # Memastikan bahwa hasil sesuai dengan yang diharapkan

if __name__ == '__main__':
    unittest.main()
