# Значение арифметического выражения
def tokenize(expr):
    tokens = []
    current_token = ""

    for char in expr:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif char in {'+', '-', '*', '(', ')'}:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        elif char.isdigit():
            current_token += char
        else:
            return []

    if current_token:
        tokens.append(current_token)

    if not tokens:
        return []

    i = 0
    while i < len(tokens):
        if tokens[i] in {'+', '-'} and (i == 0 or tokens[i-1] == '('):
            tokens.insert(i, '0')
            i += 2
        else:
            i += 1

    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            if not stack:
                return []
            stack.pop()
    if stack:
        return []

    expect_number = True

    for token in tokens:
        if token in {'+', '-', '*'}:
            if expect_number:
                return []
            expect_number = True
        elif all(c.isdigit() for c in token):
            if not expect_number:
                return []
            expect_number = False
        elif token == '(':
            expect_number = True
        elif token == ')':
            if expect_number:
                return []
            expect_number = False

    res = not expect_number
    return tokens if res else []


def infix_to_postfix(lst):
    priority = {
        '+': 2,
        '-': 2,
        '*': 3
    }
    res = []
    stack = []

    for elem in lst:
        if elem.isdigit():
            res.append(elem)
        elif elem == '(':
            stack.append(elem)
        elif elem in priority:
            while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[elem]:
                res.append(stack.pop())
            stack.append(elem)
        elif elem == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()

    while stack:
        res.append(stack.pop())

    return res


def postfix_count(postfix_list):
    operations = {
        '+': int.__add__,
        '-': int.__sub__,
        '*': int.__mul__
    }
    stack = []

    for elem in postfix_list:
        if elem not in operations:
            stack.append(int(elem))
        else:
            last = stack.pop()
            pre_last = stack.pop()

            new = operations[elem](pre_last, last)
            stack.append(new)

    return stack.pop()


def solution(string):
    res = tokenize(string)

    if not res:
        return 'WRONG'

    postfix_string = infix_to_postfix(res)
    return postfix_count(postfix_string)


if __name__ == '__main__':
    string = input()
    print(solution(string))
