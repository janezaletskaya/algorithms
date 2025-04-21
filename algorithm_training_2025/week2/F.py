# F. Ближайшее большее число справа
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


def execute_query(left: int, right: int, x: int, segment_tree: list[int]) -> int:
    n = (len(segment_tree) + 1) // 2

    def find_first_right_ge(node, seg_start, seg_end, qstart, qend, target_val):
        if seg_end < qstart or seg_start > qend or segment_tree[node] < target_val:
            return -1

        if seg_start == seg_end:
            if qstart <= seg_start <= qend and segment_tree[node] >= target_val:
                return seg_start
            return -1

        mid = (seg_start + seg_end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_result = find_first_right_ge(left_child, seg_start, mid,
                                          qstart, qend, target_val)

        if left_result != -1:
            return left_result

        return find_first_right_ge(right_child, mid + 1, seg_end,
                                   qstart, qend, target_val)

    ans = find_first_right_ge(0, 0, n - 1, left, right, x)
    return ans + 1 if ans != -1 else -1


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


if __name__ == '__main__':
    _, m = map(int, input().split())
    lst = list(map(int, input().split()))
    st = make_segment_tree(lst)

    for _ in range(m):
        query_type, i, x = map(int, input().split())
        if query_type == 0:
            change_element(i - 1, x, st)
        elif query_type == 1:
            print(execute_query(i - 1, len(lst) - 1, x, st))
