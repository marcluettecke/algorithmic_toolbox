import unittest
from algorithmic_toolbox.week4.Divide_and_Conquer.Binary_Search.binary_search import binary_search, linear_search


class TestBinarySearch(unittest.TestCase):
    def test_small(self):
        for (keys, query) in [
            ([1, 2, 3], 1),
            ([4, 5, 6], 7),
            ([1], 2)
        ]:
            self.assertEqual(
                linear_search(keys, query),
                binary_search(keys, query)
            )

    def test_large(self):
        for (keys, query, answer) in [
            (list(range(10 ** 4)), 10 ** 4, -1),
            (list(range(10 ** 4)), 239, 239),
            (list(range(3 * 10 ** 4)), (3 * 10 ** 4) - 1, (3 * 10 ** 4) - 1)
        ]:
            self.assertEqual(binary_search(keys, query), answer)


if __name__ == '__main__':
    unittest.main()
