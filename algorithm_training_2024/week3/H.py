# Стек с суммой
class PrefixStack:

    def __init__(self):
        self.prefix_stack = [0]

    def push_back(self, x):
        self.prefix_stack.append(x + self.prefix_stack[-1])

    def pop_back(self):
        if len(self.prefix_stack) > 1:
            self.prefix_stack.pop()

    def count_sum(self, k):
        idx = len(self.prefix_stack) - k - 1
        return self.prefix_stack[-1] - self.prefix_stack[idx]


class Stack:

    def __init__(self):
        self.stack = []

    def push_back(self, x):
        self.stack.append(x)

    def pop_back(self):
        if self.stack:
            return self.stack.pop()


def execution(string, stack, prefix_stack):
    if string[0] == '-':
        prefix_stack.pop_back()
        return stack.pop_back()

    if string[0] == '+':
        prefix_stack.push_back(int(string[1:]))
        stack.push_back(int(string[1:]))
        return

    if string[0] == '?':
        return prefix_stack.count_sum(int(string[1:]))


if __name__ == '__main__':
    n = int(input())
    ps = PrefixStack()
    s = Stack()
    for _ in range(n):
        out = execution(input(), s, ps)
        if out is not None:
            print(out)


