from G import CensorCount, solution


def test_solution():
    assert solution('aabbb', 100) == 5
    assert solution('abooo', 0) == 4
    assert solution('aab', 1) == 2
    assert solution('aabcbb', 2) == 4
    assert solution('abaabb', 4) == 5
    assert solution('abaabb', 3) == 4
    assert solution('abaabb', 2) == 4
    assert solution('abaabb', 1) == 4
    assert solution('abaabb', 0) == 3
    assert solution('ababababababab', 0) == 2


def test():
    cc = CensorCount()
    out1 = cc.add('a', 0)
    assert out1 == 0
    assert cc.cnt_a == 1
    assert cc.cnt_b == 0
    # assert cc.queue == [('a', 0)]

    out2 = cc.add('b', 1)

    assert out2 == 1
    assert cc.cnt_a == 1
    assert cc.cnt_b == 1

    out3 = cc.add('a', 2)

    assert out3 == 1
    assert cc.cnt_a == 2
    assert cc.cnt_b == 1

    out4 = cc.add('a', 3)

    assert out4 == 1
    assert cc.cnt_a == 3
    assert cc.cnt_b == 1

    out5 = cc.add('b', 4)

    assert out5 == 4
    assert cc.cnt_a == 3
    assert cc.cnt_b == 2

    out6 = cc.pop()

    assert out6 == 0
    assert cc.cnt_a == 2
    assert cc.cnt_b == 1
    # assert cc.queue[0] == ('a', 2)
    assert cc.c == 2

    out7 = cc.pop()

    assert out7 == 2
    assert cc.cnt_a == 1
    assert cc.cnt_b == 1
    # assert cc.queue[0] == ('a', 3)
    assert cc.c == 1

    out8 = cc.pop()

    assert out8 == 3
    # assert cc.queue == []
    assert cc.cnt_a == 0
    assert cc.cnt_b == 0
    assert cc.c == 0
