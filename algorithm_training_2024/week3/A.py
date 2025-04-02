# Правильная скобочная последовательность


def solution(s):
    open_brackets = []
    for sym in s:
        if sym in {'(', '{', '['}:
            open_brackets.append(sym)
        elif sym in {')', '}', ']'}:
            if not open_brackets:
                return 'no'
            last = open_brackets.pop()
            if sym == ')' and last != '(':
                return 'no'
            elif sym == ']' and last != '[':
                return 'no'
            elif sym == '}' and last != '{':
                return 'no'

    return 'no' if open_brackets else 'yes'


print(solution(input()))