# test_calculator.py

import unittest
from fine_calculator.calculator import calculate_fine

class TestFineCalculator(unittest.TestCase):

    def test_fine_calculation(self):
        # Test case for days overdue less than or equal to 15
        self.assertEqual(calculate_fine(10), 0)
        
        # Test case for days overdue greater than 15
        self.assertEqual(calculate_fine(20), 50)

if __name__ == '__main__':
    unittest.main()
