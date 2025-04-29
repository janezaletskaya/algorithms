# B. Миссия джедая Ивана
def solution(matrix: list[list[int]]):
    res = []
    for i in range(len(matrix)):
        num = 0
        for j in range(len(matrix)):
            if i != j:
                num |= matrix[i][j]
        res.append(num)

    return res


if __name__ == '__main__':
    n = int(input())
    input_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        input_matrix.append(row)

    print(*solution(input_matrix))
