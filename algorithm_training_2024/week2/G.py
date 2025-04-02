class CensorCount:

    def __init__(self):
        self.queue = []
        self.c = 0
        self.cnt_a = 0
        self.cnt_b = 0
        self.head = 0

    def _empty(self):
        return self.head >= len(self.queue)

    def _pop(self):
        item = self.queue[self.head]
        self.head += 1
        return item

    def add(self, sym, idx):
        if sym == 'a':
            self.cnt_a += 1

        elif sym == 'b':
            if self._empty():
                return self.c

            self.cnt_b += 1
            self.c += self.cnt_a

        else:
            return self.c

        self.queue.append((sym, idx))

        return self.c

    def pop(self):
        if self._empty():
            raise Exception("Empty queue")

        elem = self._pop()
        assert elem[0] == 'a'

        self.cnt_a -= 1
        self.c -= self.cnt_b

        while not self._empty() and self.queue[self.head][0] != 'a':
            self._pop()
            self.cnt_b -= 1

        return elem[1]


def solution(string, c_limit):
    max_len = 0
    start = 0
    cc = CensorCount()
    for i in range(len(string)):
        c = cc.add(string[i], i)

        if c > c_limit:
            max_len = max(max_len, i - start)

            while c > c_limit:
                start = cc.pop() + 1
                c = cc.c

    max_len = max(max_len, len(string) - start)

    return max_len


if __name__ == '__main__':
    n, c = map(int, input().split())
    string = input()

    print(solution(string, c))
