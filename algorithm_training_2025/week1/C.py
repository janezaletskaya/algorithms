# C. Интернет

def solution(target: int, array: list[int]) -> int:
    sec_by_price = [(elem, 2 ** i, elem / 2 ** i) for i, elem in enumerate(array)]
    sec_by_price.sort(key=lambda x: x[2], reverse=True)

    total_cost = 0
    min_cost = float('inf')
    rem = target

    for elem, cost, _ in sec_by_price:
        possible = rem // elem
        total_cost += possible * cost
        rem -= possible * elem

        if rem > 0:
            total_cost_plus_one = total_cost + cost
            if rem - elem <= 0:
                min_cost = min(min_cost, total_cost_plus_one)

    if rem <= 0:
        min_cost = min(min_cost, total_cost)

    return min_cost


if __name__ == '__main__':
    M = int(input())
    array = list(map(int, input().split()))
    print(solution(M, array))
