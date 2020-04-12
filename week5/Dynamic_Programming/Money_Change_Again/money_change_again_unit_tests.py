import unittest
from algorithmic_toolbox.week5.Dynamic_Programming.Money_Change_Again.money_change_again import change, change_naive


class MoneyChangeAgain(unittest.TestCase):
    def test_small(self):
        for money in range(1, 40):
            self.assertEqual(change(money), change_naive(money))

    def test_large(self):
        for money, answer in ((200, 50), (239, 60)):
            self.assertEqual(change(money), answer)


if __name__ == '__main__':
    unittest.main()