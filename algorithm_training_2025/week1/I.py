# I. Эластичный ровер*

def solution(max_v: int, items: list[tuple[int, int, int]]):
    items.sort(key=lambda item: item[2], reverse=True)

    total_volume = sum(volume for volume, _, _, _ in items)
    max_possible_volume = min(total_volume, max_v + items[0][2])

    dp = [[(0, -1) for _ in range(max_possible_volume + 1)]]
    for num, (volume, price, P, _) in enumerate(items):
        prev_row = dp[-1]
        cur_row = prev_row.copy()

        cur_max_possible = min(max_v + P, max_possible_volume)
        for j in range(cur_max_possible - volume, -1, -1):
            if prev_row[j][1] != -1 or j == 0:
                cur_price = cur_row[j + volume][0]
                new_price = prev_row[j][0] + price
                if new_price > cur_price:
                    cur_row[j + volume] = (new_price, num + 1)

        dp.append(cur_row)

    return dp


def recovery_answer(dp, items):
    path = []
    max_price = 0
    if len(dp) == 1:
        return max_price, path

    last_row = dp[-1]
    max_price_index = max(range(len(last_row)), key=lambda j: last_row[j][0])
    max_price = last_row[max_price_index][0]
    last_item = last_row[max_price_index][1]

    cur_volume = max_price_index

    while last_item != -1:
        path.append(items[last_item - 1][3])
        cur_volume -= items[last_item - 1][0]
        last_item = dp[last_item - 1][cur_volume][1]

    return max_price, path


if __name__ == '__main__':
    n, max_volume = map(int, input().split())
    items = []
    for j in range(1, n + 1):
        item = list(map(int, input().split()))
        item.append(j)
        items.append(tuple(item))

    dp = solution(max_volume, items)

    max_price, path = recovery_answer(dp, items)
    print(len(path), max_price)
    if len(path) > 0:
        print(*path)
