# J. Присваивание на отрезке, сравнение подотрезков*

p = 10 ** 9 + 7
x_ = 257


class PolyHashSegmentTree:

    def __init__(self, array):
        (self.hashes_tree, self.update_tree, self.lens_tree,
         self.x_pow, self.prefix_sum_x_pows, self.n) = self.__make_tree(array)

    @staticmethod
    def __make_tree(array):
        n = 1
        while n < len(array):
            n *= 2

        array += [0] * (n - len(array))
        x_pow = [0] * (n + 1)
        prefix_x = [0] * (n + 1)

        x_pow[0] = 1
        prefix_x[1] = 1

        hashes_tree = [0] * (n - 1) + array
        lens_tree = [1] * (2 * n - 1)
        update_tree = [0] * (2 * n - 1)

        for i in range(1, n + 1):
            x_pow[i] = (x_pow[i - 1] * x_) % p
            prefix_x[i] = (prefix_x[i - 1] + x_pow[i - 1]) % p

        for k in range(n - 2, -1, -1):
            left_idx = 2 * k + 1
            right_idx = 2 * k + 2

            left_hash = hashes_tree[left_idx]
            right_hash = hashes_tree[right_idx]

            left_len = lens_tree[left_idx]
            right_len = lens_tree[right_idx]

            hash_ = (left_hash * x_pow[right_len] + right_hash) % p
            len_ = left_len + right_len
            lens_tree[k] = len_
            hashes_tree[k] = hash_

        return hashes_tree, update_tree, lens_tree, x_pow, prefix_x, n

    def get_hash(self, qstart, qend):
        qstart -= 1
        qend -= 1

        def get_hash_rec(idx, seg_start, seg_end):
            if seg_end < qstart or qend < seg_start:
                return 0, 0

            self.apply_update_if_needed(idx)

            if qstart <= seg_start and seg_end <= qend:
                hash_ = self.hashes_tree[idx]
                len_ = self.lens_tree[idx]
                return hash_, len_

            mid = (seg_start + seg_end) // 2
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2

            left_hash, left_len = get_hash_rec(left_child, seg_start, mid)
            right_hash, right_len = get_hash_rec(right_child, mid + 1, seg_end)
            hash_ = (left_hash * self.x_pow[right_len] + right_hash) % p
            len_ = left_len + right_len

            return hash_, len_

        return get_hash_rec(0, 0, self.n - 1)

    def update_segment(self, query_start, query_end, new_val):
        query_start -= 1
        query_end -= 1

        def update_segment_rec(idx, seg_start, seg_end):
            if seg_end < query_start or query_end < seg_start:
                return
            if query_start <= seg_start and seg_end <= query_end:
                self.update_tree[idx] = new_val
                self.apply_update_if_needed(idx)
                return

            self.apply_update_if_needed(idx)

            mid = (seg_start + seg_end) // 2
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2

            update_segment_rec(left_child, seg_start, mid)
            update_segment_rec(right_child, mid + 1, seg_end)

            self.apply_update_if_needed(left_child)
            self.apply_update_if_needed(right_child)

            left_hash = self.hashes_tree[left_child]
            right_hash = self.hashes_tree[right_child]

            right_len = self.lens_tree[right_child]
            hash_ = (left_hash * self.x_pow[right_len] + right_hash) % p
            self.hashes_tree[idx] = hash_

        update_segment_rec(0, 0, self.n - 1)

    def apply_update_if_needed(self, idx):
        if self.update_tree[idx] == 0:
            return

        len_ = self.lens_tree[idx]
        if len_ == 1:
            self.hashes_tree[idx] = self.update_tree[idx]
        else:
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2

            left_len = self.lens_tree[left_child]
            right_len = self.lens_tree[right_child]

            left_hash_ = (self.update_tree[idx] * self.prefix_sum_x_pows[left_len]) % p
            right_hash_ = (self.update_tree[idx] * self.prefix_sum_x_pows[right_len]) % p
            hash_ = (left_hash_ * self.x_pow[right_len] + right_hash_) % p

            self.hashes_tree[idx] = hash_

            self.update_tree[left_child] = self.update_tree[idx]
            self.update_tree[right_child] = self.update_tree[idx]

        self.update_tree[idx] = 0

    def is_equal(self, left1, left2, length):
        hash1, _ = self.get_hash(left1, left1 + length - 1)
        hash2, _ = self.get_hash(left2, left2 + length - 1)

        return hash1 == hash2


def execute_queries(query_list, array):
    res = []
    tree = PolyHashSegmentTree(array)
    for query in query_list:
        if query[0] == 0:
            left, right, value = query[1:]
            tree.update_segment(left, right, value)

        elif query[0] == 1:
            left1, left2, length = query[1:]
            ans = tree.is_equal(left1, left2, length)
            if ans:
                res.append('+')
            else:
                res.append('-')

    return ''.join(res)


if __name__ == '__main__':
    input()
    array = list(map(int, input().split()))
    Q = int(input())
    tree = PolyHashSegmentTree(array)

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            left, right, value = query[1:]
            tree.update_segment(left, right, value)
        elif query[0] == 1:
            left1, left2, length = query[1:]
            ans = tree.is_equal(left1, left2, length)
            print('+' if ans else '-', end='')
