import unittest
from algorithmic_toolbox.week5.Dynamic_Programming.Partitioning_Souvenirs.partition_souvenirs import partition3


class PartitionSouvenirs(unittest.TestCase):
    def test(self):
        for values, answer in (
            ((20, ), 0),
            ((7, 7, 7), 1),
            ((3, 3, 3), 1),
            ((3, 3, 3, 3), 0),
        ):
            self.assertEqual(partition3(values), answer)


if __name__ == '__main__':
    unittest.main()
