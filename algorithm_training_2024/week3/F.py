# Минимальная ПСП
def solution2(prefix_string, n, brackets_order):
    if n == len(prefix_string):
        return prefix_string
    dct = {
        '(': ')',
        '[': ']'
    }
    opens = {}
    closes = {}

    for i, sym in enumerate(brackets_order):
        if sym in {'(', '['}:
            opens[i] = sym
        elif sym in {')', ']'}:
            closes[sym] = i

    stack = []
    res = []
    cur_len = len(prefix_string)

    for sym in prefix_string:
        if sym in opens.values():
            stack.append(sym)
        elif sym in closes:
            stack.pop()

    open_price = min(opens.keys())
    open = opens[open_price]
    while cur_len != n:
        if cur_len + len(stack) < n:
            if stack:
                close = dct[stack[-1]]
                close_price = closes[close]

                if open_price < close_price:
                    stack.append(open)
                    res.append(open)
                else:
                    stack.pop()
                    res.append(close)
            else:
                stack.append(open)
                res.append(open)
        else:
            open = stack.pop()
            res.append(dct[open])

        cur_len += 1

    res_string = ''.join(res)
    return prefix_string + res_string


def solution(prefix_string, n, brackets_order):
    if n == len(prefix_string):
        return prefix_string
    pairs = {
        '(': ')',
        '[': ']'
    }
    opens = {}
    closes = {}

    for i, sym in enumerate(brackets_order):
        if sym in pairs.keys():
            opens[i] = sym
        else:
            closes[sym] = i

    stack = []
    res = list(prefix_string)

    for sym in prefix_string:
        if sym in opens.values():
            stack.append(sym)
        else:
            stack.pop()

    min_open_idx = min(opens.keys())
    min_open = opens[min_open_idx]

    while len(res) + len(stack) != n:
        if stack:
            close_idx = closes[pairs[stack[-1]]]
            if close_idx < min_open_idx:
                res.append(pairs[stack.pop()])
                continue

        stack.append(min_open)
        res.append(min_open)

    while stack:
        res.append(pairs[stack.pop()])

    return ''.join(res)


if __name__ == '__main__':
    n = int(input())
    brackets_order = input()
    prefix_string = input()

    print(solution(prefix_string, n, brackets_order))

