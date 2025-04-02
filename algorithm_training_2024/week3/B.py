# Великое Лайнландское переселение


def solution(lst):
    res = [-1] * len(lst)
    stack = []

    for i in range(len(lst) - 1, -1, -1):
        while stack and lst[stack[-1]] >= lst[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)

    return res


input()
lst = list(map(int, input().split()))

print(*solution(lst))