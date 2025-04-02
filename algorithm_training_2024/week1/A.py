def solution(x1, y1, x2, y2, X, Y):
    res = []
    if Y > y2:
        res.append('N')
    elif Y < y1:
        res.append('S')

    if X > x2:
        res.append('E')
    elif X < x1:
        res.append('W')

    return ''.join(res)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
X = int(input())
Y = int(input())

print(solution(x1, y1, x2, y2, X, Y))


assert solution(-1, -2, 5, 3, -4, 6) == 'NW'
assert solution(0, 0, 2, 2, -50, 1) == 'W'
assert solution(0, 0, 2, 2, 50, 1) == 'E'

assert solution(0, 0, 2, 2, 1, 50) == 'N'
assert solution(0, 0, 2, 2, 1, -50) == 'S'

assert solution(0, 0, 2, 2, 5, 10) == 'NE'
assert solution(0, 0, 2, 2, -1, 10) == 'NW'
assert solution(0, 0, 2, 2, -1, -10) == 'SW'
assert solution(0, 0, 2, 2, 10, -10) == 'SE'


