from H import solution
from slow_H import slow_solution

import random
import time
import tracemalloc


def generate_random_orders(n, min_len=1, max_len=6):
    orders = []
    for _ in range(n):
        length = random.randint(min_len, max_len)
        order = ''.join(random.choice('SD') for _ in range(length))
        orders.append(order)
    return orders


def test_random(num_tests=1000, max_n=7, max_order_len=6):
    for test_num in range(1, num_tests + 1):
        n = random.randint(1, max_n)
        orders = generate_random_orders(n, max_len=max_order_len)

        fast = solution(orders)
        slow = slow_solution(orders)

        assert fast == slow, f"Test #{test_num} failed\nOrders: {orders}\nExpected: {slow}\nGot: {fast}"


def test_solution_time():
    N = 100_000
    order_length = 99
    orders = generate_random_orders(N, min_len=order_length, max_len=order_length)

    times = 10
    total_time = 0
    for i in range(10):
        start_time = time.time()
        result = solution(orders)
        end_time = time.time()
        total_time += end_time - start_time

    print(f"Mean time taken: {total_time / times:.2f} seconds")


def test_solution_memory_usage():
    N = 100_000
    order_length = 100
    orders = generate_random_orders(N, min_len=order_length, max_len=order_length)

    tracemalloc.start()

    result = solution(orders)

    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Peak memory used: {peak_mem / (1024 * 1024):.2f} MB")
