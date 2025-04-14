from I import solution, recovery_answer
from slow_I import slow_solution

import random

import tracemalloc
from memory_profiler import memory_usage

import time


def test_solution_vs_slow_solution_random():
    max_n = 20
    volume_range = (1, 50)
    cost_range = (1, 100)
    pressure_range = (0, 30)
    base_volume_range = (10, 100)

    num_tests = 100
    tests_passed = 0
    tests_failed = 0

    for test_num in range(1, num_tests + 1):
        n = random.randint(1, max_n)
        S = random.randint(base_volume_range[0], base_volume_range[1])
        items = []

        for i in range(n):
            volume = random.randint(volume_range[0], volume_range[1])
            cost = random.randint(cost_range[0], cost_range[1])
            pressure = random.randint(pressure_range[0], pressure_range[1])
            items.append((volume, cost, pressure, i))

        slow_max_cost, slow_subset = slow_solution(items, S)

        dp = solution(S, items)
        fast_max_cost, fast_subset = recovery_answer(dp, items)

        if slow_max_cost == fast_max_cost:
            tests_passed += 1

        else:
            print('Тест не пройден!')
            print(f"   {items=}, {S=}")
            print(f"   Медленное решение: стоимость={slow_max_cost}, товары={sorted(slow_subset)}")
            print(f"   Быстрое решение: стоимость={fast_max_cost}, товары={sorted(fast_subset)}")
            tests_failed += 1

    print("\n" + "=" * 50)
    print(f"Итоги тестирования:")
    print(f"Всего тестов: {num_tests}")
    print(f"Пройдено: {tests_passed}")
    print(f"Не пройдено: {tests_failed}")
    print(f"Успешность: {tests_passed / num_tests * 100:.2f}%")
    print("=" * 50)


def test_solution_memory():
    N = 100
    S = 10**9

    items = []
    for idx in range(1, N + 1):
        v = 1000
        c = 10 ** 9
        p = random.randint(10**5, 10**9)
        items.append((v, c, p, idx))

    tracemalloc.start()
    dp = solution(S, items)
    max_price, path = recovery_answer(dp, items)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Пиковое потребление памяти: {peak / (1024 * 1024):.2f} MB")


def test_solution_memory_profiler():
    N = 100
    S = 10 ** 9

    items = []
    for idx in range(1, N + 1):
        v = 1000
        c = 10 ** 9
        p = random.randint(10 ** 5, 10 ** 9)
        items.append((v, c, p, idx))

    dp = solution(S, items)
    max_price, path = recovery_answer(dp, items)

    print(memory_usage())


def test_solution_time():
    N = 100
    S = 10 ** 9

    items = []
    for idx in range(1, N + 1):
        v = 1000
        c = 10 ** 9
        p = random.randint(10 ** 5, 10 ** 9)
        items.append((v, c, p, idx))

    start = time.time()
    dp = solution(S, items)
    max_price, path = recovery_answer(dp, items)
    end = time.time()

    print(f"Время выполнения: {end - start:.3f} сек")
    print(f"Максимальная стоимость: {max_price}")
    print(f"Кол-во предметов: {len(path)}")