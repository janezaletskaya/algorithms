# D. Максимум на подотрезках с изменением элемента

def make_segment_tree(array: list[int]) -> list[int]:
    n = 1
    while n < len(array):
        n *= 2

    array = array + [-1] * (n - len(array))
    segment_tree = [-1] * (2 * n - 1)
    for j in range(n):
        segment_tree[n - 1 + j] = (array[j])

    for k in range(n - 2, -1, -1):
        left_val = segment_tree[2 * k + 1]
        right_val = segment_tree[2 * k + 2]

        if left_val == right_val:
            segment_tree[k] = left_val
        elif left_val > right_val:
            segment_tree[k] = left_val
        else:
            segment_tree[k] = right_val

    return segment_tree


def query_segment(tree: list[int], node: int, seg_start: int, seg_end: int, qstart: int, qend: int):
    if qstart <= seg_start and seg_end <= qend:
        return tree[node]

    if seg_end < qstart or qend < seg_start:
        return -1

    mid = (seg_start + seg_end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_max = query_segment(tree, left_child, seg_start, mid, qstart, qend)
    right_max = query_segment(tree, right_child, mid + 1, seg_end, qstart, qend)

    left_val = left_max
    right_val = right_max

    if left_val == right_val:
        return left_val

    elif left_val > right_val:
        return left_val

    else:
        return right_val


def execute_query(left: int, right: int, segment_tree: list[int]) -> int:
    n = (len(segment_tree) + 1) // 2
    return query_segment(segment_tree, 0, 0, n - 1, left, right)


def change_element(idx: int, new_val: int, segment_tree: list[int]):
    n = (len(segment_tree) + 1) // 2

    cur_idx = n - 1 + idx
    segment_tree[cur_idx] = new_val

    while cur_idx > 0:
        parent_idx = (cur_idx - 1) // 2
        left_idx = 2 * parent_idx + 1
        right_idx = 2 * parent_idx + 2

        left_val = segment_tree[left_idx]
        right_val = segment_tree[right_idx]

        if left_val == right_val:
            segment_tree[parent_idx] = left_val
        elif left_val > right_val:
            segment_tree[parent_idx] = left_val
        else:
            segment_tree[parent_idx] = right_val

        cur_idx = parent_idx


queries = {
    's': execute_query,
    'u': change_element
}


if __name__ == '__main__':
    input()
    lst = list(map(int, input().split()))
    st = make_segment_tree(lst)

    k = int(input())
    for i in range(k):
        query_type, left_str, right_str = input().split()
        if query_type == 's':
            max_ = queries[query_type](int(left_str) - 1, int(right_str) - 1, st)
            print(max_, end=' ')
        else:
            queries[query_type](int(left_str) - 1, int(right_str), st)
