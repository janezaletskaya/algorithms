def solution(b_shirt, r_shirt, b_socks, r_socks):
    dct = {}

    if b_shirt != 0 and b_socks != 0:
        b_m = r_shirt + 1
        b_n = r_socks + 1
        dct[b_m + b_n] = (b_m, b_n)

    if r_shirt != 0 and r_socks != 0:
        r_m = b_shirt + 1
        r_n = b_socks + 1
        dct[r_m + r_n] = (r_m, r_n)

    if min(b_shirt, r_shirt) != 0:
        m1 = max(b_shirt, r_shirt) + 1
        n1 = 1
        dct[m1 + n1] = (m1, n1)

    if min(b_socks, r_socks) != 0:
        n2 = max(b_socks, r_socks) + 1
        m2 = 1
        dct[m2 + n2] = (m2, n2)

    return dct[min(dct.keys())]


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(*solution(a, b, c, d))


assert solution(100, 0, 25, 0) == (1, 1)
assert solution(0, 100, 0, 35) == (1, 1)
assert solution(0, 1, 0, 1) == (1, 1)
assert solution(100, 100, 100, 100) == (1, 101)

assert solution(1, 1, 1, 1) == (1, 2)
assert solution(1, 1, 1, 2) == (2, 1)
assert solution(1, 1, 2, 1) == (2, 1)
assert solution(2, 1, 2, 1) == (1, 3)

assert solution(2, 2, 1, 1) == (1, 2), solution(2, 2, 1, 1)

assert solution(6, 2, 7, 3) == (3, 4)
assert solution(0, 2, 5, 1) == (1, 6), solution(0, 2, 5, 1)
