from J import execute_queries
from J_slow import execute_queries as slow_execute_queries

import random

import time
import tracemalloc


def gen_update_query(n, array_length):
    queries = []

    for _ in range(n):
        left = random.randint(1, array_length)
        right = random.randint(left, array_length)
        value = random.randint(1, 10)

        queries.append([0, left, right, value])

    return queries


def gen_compare_query(n, array_length):
    queries = []

    for _ in range(n):
        k = random.randint(1, array_length // 2)
        left1 = random.randint(1, array_length - k)
        left2 = random.randint(1, array_length - k)

        queries.append([1, left1, left2, k])

    return queries


def slow_vs_fast(array_length=4, update_q=1, compare_q=1):

    arr = [random.randint(1, 9) for _ in range(array_length)]

    queries = gen_update_query(update_q, array_length)
    compare_queries = gen_compare_query(compare_q, array_length)
    queries.extend(compare_queries)
    random.shuffle(queries)

    slow = slow_execute_queries(queries, arr.copy())
    fast = execute_queries(queries, arr.copy())
    assert slow == fast


def test_slow_vs_fast():
    for _ in range(10_000):
        slow_vs_fast(15, 10, 20)


def test_solution_time(N=50_000):
    queries = []
    array_len = 100_000
    start_time = time.time()
    for _ in range(N):
        queries += gen_update_query(1, array_len)
        queries += gen_compare_query(1, array_len)

    arr = [random.randint(1, 10) for _ in range(array_len)]
    end_time = time.time()
    print(f"\n Подготовка: {end_time - start_time:.4f} сек")

    start_time = time.time()
    execute_queries(queries, arr)
    end_time = time.time()

    print(f" Время: {end_time - start_time:.4f} сек")


def test_solution_memory():
    N = 10 ** 5
    Q = 10 ** 5
    max_value = 10 ** 5

    arr = [random.randint(max_value - 100, max_value) for _ in range(N)]
    queries = gen_update_query(Q, N)

    tracemalloc.start()
    result = execute_queries(queries, arr)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} MB")
