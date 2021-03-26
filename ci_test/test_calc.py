import unittest
from calc import do_calc


class TestCalc(unittest.TestCase):
    def test_calc(self):
        x, y = 9, 4
        self.assertEqual(do_calc(x, y), 6561)


if __name__ == '__main__':
    unittest.main()
