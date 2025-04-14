from itertools import permutations


def slow_solution(str_orders):
    max_simple_for_vasya = 0

    for perm in permutations(str_orders):
        day = 0
        simple_for_vasya = 0
        for order in perm:
            for c in order:
                if day % 2 == 0 and c == 'S':
                    simple_for_vasya += 1
                day += 1
        max_simple_for_vasya = max(max_simple_for_vasya, simple_for_vasya)

    return max_simple_for_vasya


if __name__ == '__main__':
    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(input())

    print(slow_solution(orders))
