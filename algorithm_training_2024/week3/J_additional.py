from itertools import chain, combinations, permutations


def all_subsets(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(1, len(lst) + 1)))


def my_sum_w(lst):
    cur_W = 0
    for elem in lst:
        h, w = elem
        cur_W += w

    return cur_W


def slow_count_inc(lst):
    all_perms = list(permutations(lst))

    min_inc = float('inf')
    for perm in all_perms:
        max_diff = 0
        for i in range(1, len(perm)):
            curr_diff = abs(perm[i][0] - perm[i - 1][0])
            max_diff = max(max_diff, curr_diff)

        min_inc = min(min_inc, max_diff)

    return min_inc


def slow_solution(lst, W):
    all_subs = all_subsets(lst)
    min_inc = float('inf')

    for sub_list in all_subs:
        cur_W = my_sum_w(sub_list)

        if cur_W >= W:
            sub_list = sorted(sub_list)
            cur_inc = count_inc(sub_list)
            min_inc = min(min_inc, cur_inc)

    return min_inc


def count_inc(chairs_slice):
    if len(chairs_slice) < 2:
        return 0

    max_diff = 0
    for i in range(1, len(chairs_slice)):
        curr_diff = chairs_slice[i][0] - chairs_slice[i - 1][0]
        max_diff = max(max_diff, curr_diff)

    return max_diff


def solution(chairs, W):
    if len(chairs) == 1:
        return 0

    chairs = sorted(chairs, key=lambda x: x[0])
    min_inc = float('inf')

    left = 0
    right = 0
    cur_W = chairs[right][1]

    while True:
        if cur_W < W:
            right += 1
            if right >= len(chairs):
                break
            cur_W += chairs[right][1]

        else:
            cur_inc = count_inc(chairs[left:right + 1])  # count inc
            if cur_inc == 0:
                return 0

            min_inc = min(min_inc, cur_inc)
            cur_W -= chairs[left][1]
            left += 1

    return min_inc


if __name__ == '__main__':
    n, H = map(int, input().split())
    chairs = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
    print(slow_solution(chairs, H))
