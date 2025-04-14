import unittest
import random

from G import solution


class TestBrickWalls(unittest.TestCase):
    def run_solution(self, n, k, bricks_data):
        bricks_by_colour = {}
        all_bricks = []

        for i, (length, colour) in enumerate(bricks_data):
            all_bricks.append((length, colour))
            if colour not in bricks_by_colour:
                bricks_by_colour[colour] = []
            bricks_by_colour[colour].append(length)

        return solution(k, bricks_by_colour, all_bricks)

    def verify_solution(self, result, brick_numbers, bricks_data):
        if result == "NO":
            return True

        first_wall = [bricks_data[idx - 1] for idx in brick_numbers]
        used_indices = set(brick_numbers)
        second_wall = [bricks_data[i] for i in range(len(bricks_data)) if i + 1 not in used_indices]

        first_by_colour = {}
        second_by_colour = {}

        for length, colour in first_wall:
            if colour not in first_by_colour:
                first_by_colour[colour] = []
            first_by_colour[colour].append(length)

        for length, colour in second_wall:
            if colour not in second_by_colour:
                second_by_colour[colour] = []
            second_by_colour[colour].append(length)

        colours = set(c for _, c in bricks_data)
        for colour in colours:
            if colour not in first_by_colour or colour not in second_by_colour:
                return False

        w1 = None
        for colour, bricks_list in first_by_colour.items():
            colour_sum = sum(bricks_list)
            if w1 is None:
                w1 = colour_sum
            elif w1 != colour_sum:
                return False

        w2 = None
        for colour, bricks_list in second_by_colour.items():
            colour_sum = sum(bricks_list)
            if w2 is None:
                w2 = colour_sum
            elif w2 != colour_sum:
                return False

        return True

    def test_example_from_problem(self):
        n, k = 11, 3
        bricks_data = [(5, 1), (1, 1), (1, 1), (1, 1),  # желтые [5, 1, 1, 1]
                       (3, 2), (2, 2), (2, 2), (1, 2),  # синие [3, 2, 2, 1]
                       (4, 3), (3, 3), (1, 3)]  # зеленые [4, 3, 1]

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))

    def test_impossible_case(self):
        n, k = 7, 3
        bricks_data = [(8, 1),  # желтые [8]
                       (4, 2), (4, 2),  # синие [4, 4]
                       (2, 3), (2, 3), (2, 3), (2, 3)]  # зеленые [2, 2, 2, 2]

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "NO")

    def test_equal_split(self):
        n, k = 6, 3
        bricks_data = [(5, 1), (5, 1),  # 10
                       (5, 2), (5, 2),  # 10
                       (5, 3), (5, 3)]  # 10

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))

    def test_many_small_bricks(self):
        n, k = 30, 3
        bricks_data = [(1, 1)] * 10 + [(1, 2)] * 10 + [(1, 3)] * 10

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))

    def test_large_number_of_bricks(self):
        n, k = 300, 3
        bricks_data = []
        total_per_color = 100

        for colour in range(1, k + 1):
            remaining = total_per_color
            while remaining > 0:
                brick_length = random.randint(1, min(remaining, 50))
                bricks_data.append((brick_length, colour))
                remaining -= brick_length

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))

    def test_different_number_of_bricks_per_color(self):
        bricks_data = [(10, 1), (10, 1)] + \
                      [(5, 2), (5, 2), (5, 2), (5, 2)] + \
                      [(1, 3) for _ in range(20)]

        n, k = len(bricks_data), 3

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))

    def test_maximum_constraints(self):
        k = 100
        bricks_data = []

        for colour in range(1, k + 1):
            bricks_data.extend([(1, colour)] * 50)

        n = len(bricks_data)

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))

    def test_minimal_possible_case(self):
        n, k = 2, 1
        bricks_data = [(1, 1), (1, 1)]

        result, brick_numbers = self.run_solution(n, k, bricks_data)
        self.assertEqual(result, "YES")
        self.assertTrue(self.verify_solution(result, brick_numbers, bricks_data))


if __name__ == '__main__':
    unittest.main()
