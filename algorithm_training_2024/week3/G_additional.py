def slow_solution(lst, b):
    q = create_q(lst)
    total_time = 0

    for i in range(len(lst)):
        served = 0
        while q and served != b and q[0] <= i:
            total_time += i - q.pop(0) + 1
            served += 1

    for elem in q:
        total_time += len(lst) - elem + 1

    return total_time


def mid_solution(lst, b):
    res = 0
    pointer = 0
    for i in range(len(lst)):
        served = 0
        cur_res = 0
        while pointer <= i:
            while served != b and lst[pointer] > 0:
                lst[pointer] -= 1
                served += 1
                cur_res += i - pointer + 1

            if served == b:
                break

            pointer += 1

        res += cur_res

    for i, customer in enumerate(lst[pointer:], start=pointer):
        res += customer * (len(lst) - i + 1)

    return res


def solution(lst, b):
    res = 0
    pointer = 0
    for i in range(len(lst)):
        cur_cnt_customers = 0
        cur_res = 0
        while pointer <= i:
            possible_cnt_customer = min(lst[pointer], b - cur_cnt_customers)
            cur_res += possible_cnt_customer * (i - pointer + 1)
            lst[pointer] -= possible_cnt_customer
            cur_cnt_customers += possible_cnt_customer

            if lst[pointer] == 0:
                pointer += 1

            if cur_cnt_customers == b:
                break

        res += cur_res

    for i, customer in enumerate(lst[pointer:], start=pointer):
        res += customer * (len(lst) - i + 1)

    return res


def create_q(lst):
    q = []
    for i, elem in enumerate(lst):
        q += [i] * elem
    return q


if __name__ == '__main__':
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    print(slow_solution(lst, b))
    print(fast_solution(lst, b))