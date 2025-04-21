def update_segment(array, left, right, value):
    for i in range(left - 1, right):
        array[i] = value


def compare_segments(array, left1, left2, length):
    ptr1, ptr2 = left1 - 1, left2 - 1
    for _ in range(length):
        if array[ptr1] != array[ptr2]:
            return False
        ptr1 += 1
        ptr2 += 1

    return True


def execute_queries(query_list, array):
    res = []
    for query in query_list:
        if query[0] == 0:
            left, right, value = query[1:]
            update_segment(array, left, right, value)

        elif query[0] == 1:
            left1, left2, length = query[1:]
            ans = compare_segments(array, left1, left2, length)
            if ans:
                res.append('+')
            else:
                res.append('-')

    return ''.join(res)


if __name__ == '__main__':
    input()
    array = list(map(int, input().split()))
    Q = int(input())

    query_list = []
    res = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        query_list.append(query)

    print(execute_queries(query_list, array))

