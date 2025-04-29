# A. Количество единиц
def solution(num):
    cnt_ones = 0
    while num:
        num &= (num - 1)
        cnt_ones += 1

    return cnt_ones


if __name__ == '__main__':
    x = int(input())
    print(solution(x))
