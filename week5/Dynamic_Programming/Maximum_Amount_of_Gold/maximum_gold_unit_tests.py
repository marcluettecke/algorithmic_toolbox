import unittest
from algorithmic_toolbox.week5.Dynamic_Programming.Maximum_Amount_of_Gold.maximum_gold import maximum_gold


class MaximumGold(unittest.TestCase):
    def test(self):
        for capacity, weights, answer in (
            (10, (1, 4, 8), 9),
            (20, (5, 7, 12, 18), 19),
            (10, (3, 5, 3, 3, 5), 10),
        ):
            self.assertEqual(maximum_gold(capacity, weights), answer)


if __name__ == '__main__':
    unittest.main()
