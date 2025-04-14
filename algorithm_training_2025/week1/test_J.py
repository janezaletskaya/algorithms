from J import solution

import tracemalloc
import random
import time


def test_solution_memory():
    N = 10 ** 3
    D = 10 ** 4
    max_value = 10 ** 4

    items = []
    for i in range(N):
        value = i * (max_value // N) + 1
        name = f"item_{i}"
        items.append((value, name))

    tracemalloc.start()
    result = solution(items, D)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Количество выбранных элементов: {len(result)}")
    print(f"Сумма стоимостей: {sum(result.values())}")
    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} MB")


def test_solution_time():
    N = 1000
    D = 10 ** 4
    max_value = 10 ** 4
    items = []
    for i in range(N):
        value = i * (max_value // N) + 1
        name = f"item_{i}"
        items.append((value, name))

    random.shuffle(items)

    start_time = time.time()
    solution(items, D)
    end_time = time.time()

    print(f" Время: {end_time - start_time:.4f} сек")
