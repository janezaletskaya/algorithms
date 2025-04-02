# Постфиксная запись


def solution(string):
    operations = {
        '+': int.__add__,
        '-': int.__sub__,
        '*': int.__mul__
    }

    lst = string.split()
    stack = []

    for elem in lst:
        if elem not in operations:
            stack.append(int(elem))
        else:
            last = stack.pop()
            pre_last = stack.pop()

            new = operations[elem](pre_last, last)
            stack.append(new)

    return stack.pop()


print(solution(input()))

