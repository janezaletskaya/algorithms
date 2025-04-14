# F. Рюкзак: наибольшая стоимость с восстановлением ответа

from collections import namedtuple


Cell = namedtuple('Cell', ['price', 'last_item'])


def solution(weights: list[int], prices: list[int], max_weight: int) -> list[list[Cell]]:
    dp = []

    for n, (weight, price) in enumerate(zip(weights, prices)):
        prev_row = dp[-1] if dp else [Cell(price=0, last_item=-1) for _ in range(max_weight + 1)]
        cur_row = prev_row.copy()

        for j in range(max_weight - weight, -1, -1):
            if prev_row[j].last_item != -1 or j == 0:
                cur_price = cur_row[j + weight].price
                new_price = prev_row[j].price + price
                if new_price > cur_price:
                    cur_row[j + weight] = Cell(price=new_price, last_item=n)

        dp.append(cur_row)

    return dp


def recovery_answer(dp: list[list[Cell]], weights: list[int]) -> list[int]:
    ans = []
    if not dp:
        return ans

    last_row = dp[-1]
    max_weight_index = max(range(len(last_row)), key=lambda j: last_row[j].price)
    last_item = last_row[max_weight_index].last_item

    cur_weight = max_weight_index

    while last_item != -1:
        ans.append(last_item + 1)
        cur_weight -= weights[last_item]
        if last_item == 0:
            break
        last_item = dp[last_item - 1][cur_weight].last_item

    return ans[::-1]


if __name__ == '__main__':
    _, max_weight = map(int, input().split())
    item_weights = list(map(int, input().split()))
    item_prices = list(map(int, input().split()))

    dp = solution(item_weights, item_prices, max_weight)
    print(*recovery_answer(dp, item_weights), sep='\n')
