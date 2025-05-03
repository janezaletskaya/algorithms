# A. Стек с защитой от ошибок
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

        return 'ok'

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return 'error'

    def back(self):
        if self.stack:
            return self.stack[-1]
        return 'error'

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

        return 'ok'

    def exit(self):
        return 'bye'


COMMANDS = {
    'push': Stack.push,
    'pop': Stack.pop,
    'back': Stack.back,
    'size': Stack.size,
    'clear': Stack.clear,
    'exit': Stack.exit
}

s = Stack()
prev_command = None
while prev_command != 'exit':
    command_name = input().split()
    if len(command_name) == 1:
        print(COMMANDS[command_name[0]](s))
        prev_command = command_name[0]

    else:
        command, num = command_name
        print(COMMANDS[command](s, num))
        prev_command = command

