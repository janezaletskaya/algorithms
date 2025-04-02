# Очередь в ПВЗ
def fast_solution(lst, b):
    customers_in_queue = 0
    total_time = 0

    for customers in lst:
        customers_in_queue += customers
        total_time += customers_in_queue
        customers_in_queue -= min(customers_in_queue, b)

    total_time += customers_in_queue

    return total_time


if __name__ == '__main__':
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    print(fast_solution(lst, b))
