# D. Забавная игра
def solution(num):
    if num == 0:
        return 0
    k = num.bit_length()
    res = []
    mask = (1 << k) - 1

    for _ in range(k):
        num = ((num << 1) | (num >> (k - 1))) & mask
        res.append(num)

    return max(res)


if __name__ == '__main__':
    num = int(input())
    print(solution(num))
