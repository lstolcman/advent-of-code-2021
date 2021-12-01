import unittest

from task_1 import calculate


class TestCalculate(unittest.TestCase):

    def test_input_1(self):
        input_file_name = 'test_input_data.txt'
        increased, decreased = calculate(input_file_name)

        self.assertEqual(increased, 7)
        self.assertEqual(decreased, 2)

if __name__ == '__main__':
    unittest.main()
