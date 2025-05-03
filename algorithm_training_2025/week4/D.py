# D. Переключение между окнами
class Node:
    def __init__(self, program_name):
        self.program_name = program_name
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.program_name)


class LinkedList:
    def __init__(self):
        self.head = None
        self.len_ = 0

    def run_program(self, program_name):
        program_node = Node(program_name)
        self.len_ += 1

        if self.head is None:
            program_node.next = program_node
            program_node.prev = program_node
            self.head = program_node
        else:
            tail = self.head.prev
            program_node.next = self.head
            program_node.prev = tail
            self.head.prev = program_node
            tail.next = program_node
            self.head = program_node

        return program_name

    def alt_tab(self, k):
        k = k % self.len_
        if k == 0:
            return self.head.program_name

        cur_node = self.head
        for _ in range(k):
            cur_node = cur_node.next

        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev

        tail = self.head.prev
        cur_node.next = self.head
        cur_node.prev = tail
        self.head.prev = cur_node
        tail.next = cur_node
        self.head = cur_node

        return cur_node.program_name


def solution(actions):
    ll = LinkedList()
    for act in actions:
        if act[0] == 'run':
            print(ll.run_program(act[1]))
        elif act[0] == 'alt':
            print(ll.alt_tab(int(act[1])))


if __name__ == '__main__':
    n = int(input())
    actions = []
    for _ in range(n):
        input_ = input()
        if input_[:3] == 'Run':
            actions.append(('run', input_[4:]))
        elif input_[:3] == 'Alt':
            cnt_tab = len(input_[3:]) // 4
            actions.append(('alt', cnt_tab))

    solution(actions)

