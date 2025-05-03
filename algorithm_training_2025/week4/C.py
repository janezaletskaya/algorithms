# C. Дек с защитой от ошибок
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deck:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, n):
        node = Node(n)
        self._size += 1
        if self.head is None:
            self.head = self.tail = node
            return 'ok'
        node.next = self.head
        self.head.prev = node
        self.head = node
        return 'ok'

    def push_back(self, n):
        node = Node(n)
        self._size += 1
        if self.tail is None:
            self.head = self.tail = node
            return 'ok'
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        return 'ok'

    def pop_front(self):
        if self.head is None:
            return 'error'
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def pop_back(self):
        if self.tail is None:
            return 'error'
        value = self.tail.value
        self.tail = self.tail.prev
        self._size -= 1
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value

    def front(self):
        return self.head.value if self.head else 'error'

    def back(self):
        return self.tail.value if self.tail else 'error'

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return 'ok'

    def exit(self):
        return 'bye'


COMMANDS = {
    'push_front': Deck.push_front,
    'push_back': Deck.push_back,
    'pop_back': Deck.pop_back,
    'pop_front': Deck.pop_front,
    'back': Deck.back,
    'front': Deck.front,
    'size': Deck.size,
    'clear': Deck.clear,
    'exit': Deck.exit
}

d = Deck()
prev_command = None
while prev_command != 'exit':
    command_name = input().split()
    if len(command_name) == 1:
        print(COMMANDS[command_name[0]](d))
        prev_command = command_name[0]

    else:
        command, num = command_name
        print(COMMANDS[command](d, num))
        prev_command = command

