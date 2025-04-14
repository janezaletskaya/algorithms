# H. Распределение задач*

def solution(str_orders):
    odd_len_orders = []
    even_len_orders = []

    for order in str_orders:
        odd = 0
        even = 0
        for i in range(0, len(order), 2):
            if order[i] == 'S':
                even += 1

        for i in range(1, len(order), 2):
            if order[i] == 'S':
                odd += 1

        length = len(order)
        order_data = (odd, even, odd - even, length)

        if length % 2 == 1:
            odd_len_orders.append(order_data)
        else:
            even_len_orders.append(order_data)

    best_cnt = 0

    if len(odd_len_orders) == 0:
        best_cnt = sum(order[1] for order in even_len_orders)
        return best_cnt

    odd_len_orders.sort(key=lambda order: abs(order[2]), reverse=True)

    slots_even = len(odd_len_orders) // 2 + len(odd_len_orders) % 2
    slots_odd = len(odd_len_orders) // 2

    for order in odd_len_orders:
        if order[2] < 0 and slots_even > 0:
            best_cnt += order[1]
            slots_even -= 1
        elif order[2] > 0 and slots_odd > 0:
            best_cnt += order[0]
            slots_odd -= 1
        else:
            if slots_even > 0:
                best_cnt += order[1]
                slots_even -= 1
            else:
                best_cnt += order[0]
                slots_odd -= 1

    best_cnt += sum(max(order[1], order[0]) for order in even_len_orders)

    return best_cnt


if __name__ == '__main__':
    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(input())

    print(solution(orders))
