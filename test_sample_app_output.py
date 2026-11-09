import unittest
from sample_app import add_numbers

class TestSampleApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(4, 8), 20)

if __name__ == '__main__':
    unittest.main()