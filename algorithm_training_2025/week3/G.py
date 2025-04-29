# G. Сумма на отрезке
def make_tree(N):
    n = 1
    while n < N:
        n *= 2

    return [0] * (2 * n - 1), n


def assign_element(tree, n, idx, new_value):
    idx -= 1
    cur_value = tree[n - 1 + idx]
    diff = new_value - cur_value
    tree[n - 1 + idx] = new_value
    parent_idx = (n - 1 + idx - 1) // 2
    while parent_idx >= 0:
        tree[parent_idx] += diff
        parent_idx = (parent_idx - 1) // 2


def execute_query(left: int, right: int, segment_tree: list[int]) -> int:
    left -= 1
    right -= 1

    def query_segment(tree: list[int], node: int, seg_start: int, seg_end: int, qstart: int, qend: int):
        if qstart <= seg_start and seg_end <= qend:
            return tree[node]

        if seg_end < qstart or qend < seg_start:
            return 0

        mid = (seg_start + seg_end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = query_segment(tree, left_child, seg_start, mid, qstart, qend)
        right_sum = query_segment(tree, right_child, mid + 1, seg_end, qstart, qend)

        return left_sum + right_sum

    return query_segment(segment_tree, 0, 0, n - 1, left, right)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    tree, n = make_tree(N)
    res = []
    for _ in range(Q):
        query_list = input().split()
        if query_list[0] == 'A':
            idx, new_value = map(int, query_list[1:])
            assign_element(tree, n, idx, new_value)
        elif query_list[0] == 'Q':
            left, right = map(int, query_list[1:])
            res.append(execute_query(left, right, tree))

    print(*res, sep='\n')

