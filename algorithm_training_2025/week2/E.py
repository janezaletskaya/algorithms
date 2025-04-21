# E. K-й ноль
def make_segment_tree_cnt_min(array: list[int]) -> list[tuple[float, int]]:
    n = 1
    while n < len(array):
        n *= 2

    array = array + [float('inf')] * (n - len(array))
    segment_tree = [(float('inf'), 0)] * (2 * n - 1)
    for j in range(n):
        segment_tree[n - 1 + j] = (array[j], 1 if array[j] == 0 else 0)

    for k in range(n - 2, -1, -1):
        left_val, left_cnt = segment_tree[2 * k + 1]
        right_val, right_cnt = segment_tree[2 * k + 2]

        zero_count = 0
        if left_val == 0:
            zero_count += left_cnt
        if right_val == 0:
            zero_count += right_cnt

        if left_val == right_val:
            segment_tree[k] = (left_val, zero_count)
        elif left_val < right_val:
            segment_tree[k] = (left_val, left_cnt if left_val == 0 else 0)
        else:
            segment_tree[k] = (right_val, right_cnt if right_val == 0 else 0)

    return segment_tree


def execute_query_k_zero_idx(left: int, right: int, k: int, segment_tree: list[tuple[float, int]]) -> int:
    n = (len(segment_tree) + 1) // 2

    node = 0
    seg_start, seg_end = 0, n - 1

    val, cnt = segment_tree[node]
    left_segment = max(left, seg_start)
    right_segment = min(right, seg_end)

    if right_segment < left_segment:
        return -1

    if left <= seg_start and seg_end <= right:
        if val != 0 or k >= cnt:
            return -1

    return find_kth_zero_fast(segment_tree, node, seg_start, seg_end, left, right, k)


def find_kth_zero_fast(tree: list[tuple[float, int]], node: int, seg_start: int, seg_end: int,
                       qstart: int, qend: int, k: int) -> int:

    if seg_start == seg_end:
        val, cnt = tree[node]
        if val == 0 and qstart <= seg_start <= qend:
            return seg_start
        return -1

    mid = (seg_start + seg_end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_zeros = 0
    left_val, left_cnt = tree[left_child]
    if qstart <= mid:
        if qstart <= seg_start and mid <= qend:
            left_zeros = left_cnt if left_val == 0 else 0
        else:
            left_zeros = count_zeros_in_range(tree, left_child, seg_start, mid, qstart, qend)

    if k < left_zeros:
        return find_kth_zero_fast(tree, left_child, seg_start, mid, qstart, qend, k)

    return find_kth_zero_fast(tree, right_child, mid + 1, seg_end, qstart, qend, k - left_zeros)


def count_zeros_in_range(tree: list[tuple[float, int]], node: int, seg_start: int, seg_end: int,
                         qstart: int, qend: int) -> int:
    if qstart <= seg_start and seg_end <= qend:
        val, cnt = tree[node]
        return cnt if val == 0 else 0

    if seg_end < qstart or qend < seg_start:
        return 0

    mid = (seg_start + seg_end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_zeros = count_zeros_in_range(tree, left_child, seg_start, mid, qstart, qend)
    right_zeros = count_zeros_in_range(tree, right_child, mid + 1, seg_end, qstart, qend)

    return left_zeros + right_zeros


def change_element(idx: int, new_val: int, segment_tree: list[tuple[float, int]]):
    n = (len(segment_tree) + 1) // 2

    cur_idx = n - 1 + idx
    segment_tree[cur_idx] = (new_val, 1 if new_val == 0 else 0)

    while cur_idx > 0:
        parent_idx = (cur_idx - 1) // 2
        left_idx = 2 * parent_idx + 1
        right_idx = 2 * parent_idx + 2

        left_val, left_cnt = segment_tree[left_idx]
        right_val, right_cnt = segment_tree[right_idx]

        zero_count = 0
        if left_val == 0:
            zero_count += left_cnt
        if right_val == 0:
            zero_count += right_cnt

        if left_val == right_val:
            segment_tree[parent_idx] = (left_val, zero_count)
        elif left_val < right_val:
            segment_tree[parent_idx] = (left_val, left_cnt if left_val == 0 else 0)
        else:
            segment_tree[parent_idx] = (right_val, right_cnt if right_val == 0 else 0)

        cur_idx = parent_idx


if __name__ == '__main__':
    input()
    lst = list(map(int, input().split()))
    st = make_segment_tree_cnt_min(lst)

    k = int(input())
    for i in range(k):
        query_inp = input().split()
        if query_inp[0] == 's':
            l, r, k_val = map(int, query_inp[1:])

            kth_zero_idx = execute_query_k_zero_idx(l - 1, r - 1, k_val - 1, st)
            print(kth_zero_idx + 1 if kth_zero_idx != -1 else -1, end=' ')

        elif query_inp[0] == 'u':
            idx, val = int(query_inp[1]) - 1, int(query_inp[2])
            change_element(idx, val, st)
