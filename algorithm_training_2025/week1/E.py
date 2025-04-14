# E. Рюкзак: наибольшая стоимость

def solution(weights: list[int], prices: list[int], max_weight: int) -> int:
    res = [0] * (max_weight + 1)
    for weight, price in zip(weights, prices):
        for i in range(max_weight - weight, -1, -1):
            res[i + weight] = max(res[i + weight], res[i] + price)

    return max(res)


if __name__ == '__main__':
    _, max_weight = map(int, input().split())
    item_weights = list(map(int, input().split()))
    item_prices = list(map(int, input().split()))
    print(solution(item_weights, item_prices, max_weight))
