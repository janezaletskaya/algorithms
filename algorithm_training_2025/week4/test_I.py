from I import Snowmen
from I_slow import NaiveSnowmen
import random


def generate_test(n, max_mass=10, seed=42):
    random.seed(seed)
    actions = [(0, random.randint(1, max_mass))]
    for i in range(1, n):
        t = random.randint(0, i - 1)
        if random.random() < 0.3 and t != 0:
            m = 0
        else:
            m = random.randint(1, max_mass)
        actions.append((t, m))

    return actions


def test_random(n_tests=16):
    for _ in range(10000):
        tests = generate_test(n_tests)
        snowmen = Snowmen()
        naive = NaiveSnowmen()

        for query in tests:
            snowmen.add_snowman(query[0], query[1])
            naive.add_snowman(query[0], query[1])

        if not snowmen.total_mass == naive.total_mass:
            print()
            print(f'{snowmen.total_mass=}, {naive.total_mass=}')
            print(len(tests))
            for test in tests:
                print(*test)

            assert False
