def slow_solution(items, S):
    n = len(items)
    max_cost = 0
    best_subset = []

    for mask in range(1, 2 ** n):
        current_subset = []
        total_volume = 0
        total_cost = 0

        for i in range(n):
            if mask & (1 << i):
                current_subset.append(i)
                total_volume += items[i][0]
                total_cost += items[i][1]

        pressure = max(0, total_volume - S)

        all_items_ok = True
        for i in current_subset:
            if items[i][2] < pressure:
                all_items_ok = False
                break

        if all_items_ok and total_cost > max_cost:
            max_cost = total_cost
            best_subset = current_subset

    selected_items_1based = [idx + 1 for idx in best_subset]

    return max_cost, selected_items_1based


if __name__ == '__main__':
    n, max_volume = map(int, input().split())
    items = []
    for j in range(1, n + 1):
        item = list(map(int, input().split()))
        item.append(j)
        items.append(tuple(item))

    max_price, path = slow_solution(items, max_volume)
    print(len(path), max_price)
    print(*path)
