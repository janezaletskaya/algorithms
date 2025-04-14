# D. Рюкзак: наибольший вес

def solution(weights: list[int], max_weight: int) -> int:
    res = [False] * (max_weight + 1)
    res[0] = True

    for weight in weights:
        for i in range(max_weight - weight, -1, -1):
            if res[i]:
                res[i + weight] = True

    for i in range(max_weight, -1, -1):
        if res[i]:
            return i


if __name__ == '__main__':
    _, max_weight = map(int, input().split())
    weights = list(map(int, input().split()))

    print(solution(weights, max_weight))
