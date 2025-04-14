import unittest
from F import solution, recovery_answer


class TestKnapsack(unittest.TestCase):
    def test_basic_case(self):
        weights = [6, 4, 3, 5]
        prices = [7, 6, 5, 4]
        max_weight = 7
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(sorted(result), [2, 3])

    def test_single_item(self):
        weights = [5]
        prices = [10]
        max_weight = 5
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(result, [1])

    def test_no_items_fit(self):
        weights = [10, 20, 30]
        prices = [60, 100, 120]
        max_weight = 5
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(result, [])

    def test_multiple_combinations(self):
        weights = [1, 3, 4, 5]
        prices = [1, 4, 5, 7]
        max_weight = 7
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(sorted(result), [2, 3])

    def test_all_items_fit(self):
        weights = [1, 1, 1]
        prices = [1, 2, 3]
        max_weight = 3
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(sorted(result), [1, 2, 3])

    def test_equal_weights_prices(self):
        weights = [2, 2, 2]
        prices = [5, 5, 5]
        max_weight = 4
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(i in [1, 2, 3] for i in result))

    def test_zero_prices(self):
        weights = [1, 2, 3]
        prices = [0, 0, 5]
        max_weight = 3
        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)
        self.assertEqual(result, [3])

    def test_empty_case(self):
        weights = []
        prices = []
        max_weight = 10

        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)

        self.assertEqual(result, [])

    def test_same_weight_different_prices(self):
        weights = [5, 5, 5]
        prices = [10, 20, 30]
        max_weight = 10

        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)

        total_price = sum(prices[i - 1] for i in result)
        self.assertEqual(total_price, 50)

    def test_complex_case(self):
        weights = [2, 3, 4, 5, 9]
        prices = [3, 4, 5, 8, 10]
        max_weight = 20

        dp = solution(weights, prices, max_weight)
        result = recovery_answer(dp, weights)

        total_weight = sum(weights[i - 1] for i in result)
        self.assertLessEqual(total_weight, max_weight)

        total_price = sum(prices[i - 1] for i in result)
        self.assertEqual(total_price, 26)
