# J. Аскетизм*

def solution(items, D):
    items.sort()
    costs = {}
    dp = [float('inf')] * (items[-1][0] + 1)
    dp[0] = 0
    for i, (value, _) in enumerate(items):
        if value <= D:
            cur_cost = 1
        else:
            cur_cost = min(dp[value - D:value + 1]) + 1

        if cur_cost == float('inf'):
            return costs

        costs[i] = cur_cost
        right = len(dp) - 1 - value
        left = -1

        for j in range(right, left, -1):
            if dp[j] != float('inf') or j == 0:
                dp[j + value] = min(dp[j + value], dp[j] + cur_cost)

    return costs


if __name__ == '__main__':
    N, D = map(int, input().split())
    items = []
    for _ in range(N):
        item = input().split()
        items.append((int(item[1]), item[0]))

    cost_dict = solution(items, D)
    print(len(cost_dict), sum(cost_dict.values()))
    for key in sorted([items[key][1] for key in cost_dict]):
        print(key)
