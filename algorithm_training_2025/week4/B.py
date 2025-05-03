# B. Очередь с защитой от ошибок
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, n):
        node = Node(n)
        self.size += 1
        if self.head is None:
            self.head = self.tail = node
            return 'ok'

        node.left = self.tail
        self.tail.right = node
        self.tail = node

        return 'ok'

    def pop(self):
        if self.head:
            self.size -= 1
            value = self.head.value
            self.head = self.head.right
            if self.head:
                self.head.left = None
            return value
        return 'error'

    def front(self):
        if self.head:
            return self.head.value
        return 'error'

    def get_size(self):
        return self.size

    def clear(self):
        self.head = self.tail = None
        self.size = 0
        return 'ok'

    def exit(self):
        return 'bye'


COMMANDS = {
    'push': Queue.push,
    'pop': Queue.pop,
    'front': Queue.front,
    'size': Queue.get_size,
    'clear': Queue.clear,
    'exit': Queue.exit
}

q = Queue()
prev_command = None
while prev_command != 'exit':
    command_name = input().split()
    if len(command_name) == 1:
        print(COMMANDS[command_name[0]](q))
        prev_command = command_name[0]

    else:
        command, num = command_name
        print(COMMANDS[command](q, num))
        prev_command = command

