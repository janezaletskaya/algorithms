import random
from H import execution, PrefixStack, Stack


def generate_commands(num_commands, min_number, max_number):
    commands = []
    stack_size = 0  # отслеживаем размер стека, чтобы корректно добавлять и удалять элементы

    for _ in range(num_commands):
        operation = random.choice(['+', '-', '?'])

        if operation == '+':
            num = random.randint(min_number, max_number)
            commands.append(f'+{num}')
            stack_size += 1
        elif operation == '-' and stack_size > 0:
            commands.append('-')
            stack_size -= 1
        elif operation == '?' and stack_size > 0:
            k = random.randint(1, stack_size)
            commands.append(f'?{k}')

    # print(len(commands))
    return commands


def multi_execution(strings):
    stack = Stack()
    prefix_stack = PrefixStack()
    res = []
    for string in strings:
        out = execution(string, stack, prefix_stack)
        if out is not None:
            res.append(out)

    return res


def slow_multi_execution(strings):
    stack = []
    res = []
    for string in strings:
        if string[0] == '+':
            stack.append(int(string[1:]))

        elif string[0] == '-':
            res.append(stack.pop())

        elif string[0] == '?':
            a = int(string[1:])
            b = len(stack)

            res.append(sum(stack[b - a:]))

    return res


if __name__ == '__main__':
    print(generate_commands(30, 100))