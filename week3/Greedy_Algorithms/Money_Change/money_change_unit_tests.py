import unittest
from algorithmic_toolbox.week3.Greedy_Algorithms.Money_Change.money_change import money_change


class TestSumOfTwoDigits(unittest.TestCase):
    def test(self):
        for (money, number_of_coins) in [(1, 1), (2, 2), (28, 6)]:
            self.assertEqual(money_change(money), number_of_coins)


if __name__ == '__main__':
    unittest.main()
