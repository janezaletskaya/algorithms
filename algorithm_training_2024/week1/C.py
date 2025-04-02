def is_I(x1, y1, x2, y2):
    return (x1 < x2 and
            y1 < y2)


def is_O(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 < x3 < x4 < x2 and
            y1 < y3 < y4 < y2)


def is_C(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 < x3 < x4 == x2 and
            y1 < y3 < y4 < y2)


def is_L(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 < x3 < x4 == x2 and
            y1 < y3 < y4 == y2)


def is_H(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (x1 < x3 == x5 < x4 == x6 < x2 and
            y1 == y3 < y4 < y5 < y6 == y2)


def is_P(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (x1 < x3 == x5 < x6 < x4 == x2 and
            y1 == y3 < y4 < y5 < y6 < y2)


def left_bottom(matrix, sym, start=(0, 0), end=None):
    n = len(matrix)
    if not end:
        end = (n, n)
    for i in range(start[1], end[1]):
        for j in range(start[0], end[0]):
            if matrix[i][j] == sym:
                return j, i
    return


def right_bottom(matrix, sym, start=(0, 0), end=None):
    n = len(matrix)
    if not end:
        end = (n, n)
    for i in range(start[1], end[1]):
        for j in range(end[0] - 1, start[0] - 1, -1):
            if matrix[i][j] == sym:
                return j + 1, i
    return


def left_top(matrix, sym, start=(0, 0), end=None):
    n = len(matrix)
    if not end:
        end = (n, n)
    for i in range(end[1] - 1, start[1] - 1, -1):
        for j in range(start[0], end[0]):
            if matrix[i][j] == sym:
                return j, i + 1
    return


def right_top(matrix, sym, start=(0, 0), end=None):
    n = len(matrix)
    if not end:
        end = (n, n)
    for i in range(end[1] - 1, start[1] - 1, -1):
        for j in range(end[0] - 1, start[0] - 1, -1):
            if matrix[i][j] == sym:
                return j + 1, i + 1
    return


def find_rect(matrix, sym, start=(0, 0), end=None):
    n = len(matrix)
    if not end:
        end = (n, n)

    minx = 11
    maxx = -1
    miny = 11
    maxy = -1
    for i in range(start[1], end[1]):
        for j in range(start[0], end[0]):
            if matrix[i][j] == sym:
                minx = min(minx, j)
                maxx = max(maxx, j)

                miny = min(miny, i)
                maxy = max(maxy, i)

    if minx > 10 or maxx < 0 or miny > 10 or maxy < 0:
        return None, None
    return (minx, miny), (maxx + 1, maxy + 1)


def find_rect_bad(matrix, sym, start=(0, 0), end=None):
    lb = left_bottom(matrix, sym, start, end)

    if lb:
        x1, y1 = left_bottom(matrix, sym, start, end)
        x2, y2 = right_bottom(matrix, sym, start, end)
        x3, y3 = right_top(matrix, sym, start, end)
        x4, y4 = left_top(matrix, sym, start, end)

        first = min(x1, x4), min(y1, y2)
        last = max(x2, x3), max(y3, y4)

        return first, last

    return None, None


def check_all_rect(matrix, sym, start, end):
    for i in range(start[1], end[1]):
        for j in range(start[0], end[0]):
            if matrix[i][j] != sym:
                return False
    return True


def read_matrix():
    n = int(input())
    tableau = [list(input()) for _ in range(n)]
    # print(*tableau, sep=',\n         ')
    tableau.reverse()

    return tableau


def change_angles(first, last):
    if not first and not last:
        return None, None

    x1, y1 = first
    x2, y2 = last

    return (x1, y2), (x2, y1)


def solution(matrix):
    first_light, last_light = find_rect(matrix, sym='#')
    if not first_light and not last_light:
        return 'X'

    x1, y1 = first_light
    x2, y2 = last_light

    first, last = find_rect(matrix, sym='.', start=(x1, y1), end=(x2, y2))

    if not first and not last:
        if is_I(x1, y1, x2, y2) and check_all_rect(matrix, '#', (x1, y1), (x2, y2)):
            return 'I'
        else:
            return 'X'

    x3, y3 = first
    x4, y4 = last

    if (is_C(x1, y1, x2, y2, x3, y3, x4, y4) and
            check_all_rect(matrix, '.', (x3, y3), (x4, y4))):
        return 'C'
    elif (is_L(x1, y1, x2, y2, x3, y3, x4, y4) and
          check_all_rect(matrix, '.', (x3, y3), (x4, y4))):
        return 'L'
    elif (is_O(x1, y1, x2, y2, x3, y3, x4, y4) and
          check_all_rect(matrix, '.', (x3, y3), (x4, y4))):
        return 'O'
    else:
        inner_light_first, inner_light_last = find_rect(matrix, sym='#', start=(x3, y3), end=(x4, y4))

        if inner_light_first and inner_light_last:
            if check_all_rect(matrix, '#', inner_light_first, inner_light_last):
                inner_light_first, inner_light_last = change_angles(inner_light_first, inner_light_last)
                x5, y5 = inner_light_first
                x6, y6 = x4, y4
                x4, y4 = inner_light_last
                if (is_H(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) and
                        check_all_rect(matrix, '.', (x3, y3), (x4, y4)) and
                        check_all_rect(matrix, '.', (x5, y5), (x6, y6))):
                    return 'H'

            else:
                _, (x4, y4) = change_angles(inner_light_first, inner_light_last)
                if check_all_rect(matrix, sym='.', start=(x3, y3), end=(x4, y4)):
                    super_inner_first, super_inner_last = find_rect(matrix, sym='.', start=inner_light_first,
                                                                    end=inner_light_last)
                    if super_inner_first and super_inner_last:
                        x5, y5 = super_inner_first
                        x6, y6 = super_inner_last

                        if (is_P(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) and
                                check_all_rect(matrix, '.', (x5, y5), (x6, y6))):
                            return 'P'

        return 'X'


if __name__ == '__main__':
    print(solution(read_matrix()))

if __name__ != '__main__':
    print(__name__)
