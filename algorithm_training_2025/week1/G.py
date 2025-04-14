# G. Две стены

def solution(K: int, bricks: dict[int, list[int]], all_bricks):
    total_lengths = {}
    for colour, bricks_lengths in bricks.items():
        total_lengths[colour] = sum(bricks_lengths)

    W = total_lengths[1]

    possible_w1 = set(range(1, W))

    for colour in range(1, K + 1):
        colour_bricks = bricks[colour]

        dp = [False] * (W + 1)
        dp[0] = True

        for brick in colour_bricks:
            for j in range(W, brick - 1, -1):
                if dp[j - brick]:
                    dp[j] = True

        colour_sums = {j for j in range(1, W) if dp[j]}
        possible_w1 &= colour_sums

    if not possible_w1:
        return "NO", []

    w1 = min(possible_w1)

    def find_subset(bricks_list, target_sum, brick_indices):
        dp = [False] * (target_sum + 1)
        dp[0] = True

        parent = {}

        for i, brick in enumerate(bricks_list):
            for j in range(target_sum, brick - 1, -1):
                if dp[j - brick] and not dp[j]:
                    dp[j] = True
                    parent[j] = i

        if not dp[target_sum]:
            return []

        subset = []
        j = target_sum

        while j > 0:
            i = parent[j]
            subset.append(brick_indices[i])
            j -= bricks_list[i]

        return subset

    brick_numbers = []

    for colour in range(1, K + 1):
        colour_bricks = bricks[colour]
        brick_indices = [i for i, (_, c) in enumerate(all_bricks, 1) if c == colour]

        subset = find_subset(colour_bricks, w1, brick_indices)
        brick_numbers.extend(subset)

    return "YES", sorted(brick_numbers)


if __name__ == '__main__':
    n, k = map(int, input().split())
    bricks_by_colour = {}
    all_bricks = []

    for i in range(n):
        length, colour = map(int, input().split())
        all_bricks.append((length, colour))
        if colour not in bricks_by_colour:
            bricks_by_colour[colour] = []
        bricks_by_colour[colour].append(length)

    result, brick_numbers = solution(k, bricks_by_colour, all_bricks)
    print(result)
    if result == "YES":
        print(*brick_numbers)
