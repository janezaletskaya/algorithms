# E. Точки на плоскости
def solution(a, b):
    return a ^ b


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(solution(x, y))
    x, c = map(int, input().split())
    print(solution(x, c))