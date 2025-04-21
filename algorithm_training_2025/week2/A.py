# A. Количество максимумов на отрезке
def make_segment_tree(array: list[int]) -> list[tuple[int, int]]:
    n = 1
    while n < len(array):
        n *= 2

    array = array + [-1] * (n - len(array))
    segment_tree = [(-1, 0)] * (2 * n - 1)
    for j in range(n):
        segment_tree[n - 1 + j] = (array[j], 1)

    for k in range(n - 2, -1, -1):
        left_val, left_cnt = segment_tree[2 * k + 1]
        right_val, right_cnt = segment_tree[2 * k + 2]

        if left_val == right_val:
            segment_tree[k] = (left_val, left_cnt + right_cnt)
        elif left_val > right_val:
            segment_tree[k] = (left_val, left_cnt)
        else:
            segment_tree[k] = (right_val, right_cnt)

    return segment_tree


def query_segment(tree: list[tuple[int, int]], node: int, seg_start: int, seg_end: int, qstart: int, qend: int):
    if qstart <= seg_start and seg_end <= qend:
        return tree[node]

    if seg_end < qstart or qend < seg_start:
        return -1, 0

    mid = (seg_start + seg_end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_max = query_segment(tree, left_child, seg_start, mid, qstart, qend)
    right_max = query_segment(tree, right_child, mid + 1, seg_end, qstart, qend)

    left_val, left_cnt = left_max
    right_val, right_cnt = right_max

    if left_val == right_val:
        return left_val, left_cnt + right_cnt

    elif left_val > right_val:
        return left_max

    else:
        return right_max


def execute_query(left: int, right: int, segment_tree: list[tuple[int, int]]) -> tuple[int, int]:
    n = (len(segment_tree) + 1) // 2
    return query_segment(segment_tree, 0, 0, n - 1, left, right)


if __name__ == '__main__':
    input()
    lst = list(map(int, input().split()))
    st = make_segment_tree(lst)

    k = int(input())
    for i in range(k):
        l, r = map(int, input().split())
        print(*execute_query(l - 1, r - 1, st))

