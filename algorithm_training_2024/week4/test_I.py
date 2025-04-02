from unittest.mock import patch
from textwrap import dedent
import random
import timeit
from functools import partial

from I_additional import slow_solution, create_tree_from_console as slow_create
from I3 import fast_solution, create_tree_from_console as fast_create


def create_tree(s, create):
    inputs = dedent(s).strip().split('\n')
    with patch("builtins.input", side_effect=inputs):
        tree = create()
    return tree


def generate_tree(n):
    if n <= 1:
        raise ValueError("The tree must have at least 2 nodes.")

    edges = [f'{n}']
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        edges.append(f"{parent} {i}")

    return '\n'.join(edges)


def test_load():
    n = 20000
    tree = create_tree(generate_tree(n), fast_create)
    execution_time = timeit.timeit(partial(fast_solution, tree), number=1)
    print(execution_time)


def test_random():
    for _ in range(1000):
        inp = generate_tree(30)
        fast_tree = create_tree(inp, fast_create)
        slow_tree = create_tree(inp, slow_create)
        assert slow_solution(slow_tree) == fast_solution(fast_tree), inp


def test_slow_solution():
    s = '''4
            1 2
            2 3
            3 4
            '''
    assert slow_solution(create_tree(s, slow_create)) == 1

    s = '''7
            1 2
            1 3
            1 4
            1 5
            1 6
            1 7
            '''
    assert slow_solution(create_tree(s, slow_create)) == 0

    s = '''6
1 2
2 3
2 4
5 4
6 4
'''
    assert slow_solution(create_tree(s, slow_create)) == 4

    s = '''17
1 2
2 3
4 5
5 6
3 7
6 7
7 8
8 9
9 10
9 11
11 12
12 13 
13 17
11 14
14 15
15 16'''

    assert slow_solution(create_tree(s, slow_create)) == 36

    s = '''15
1 2
1 3
2 4
4 8
8 12
2 5
3 6
5 9
9 13
3 7
6 10
10 14
7 11
11 15'''

    assert slow_solution(create_tree(s, slow_create)) == 36

    s = '''7
1 2
1 3
1 4
2 5
2 6
4 7'''

    assert slow_solution(create_tree(s, slow_create)) == 6

    s = '''8
1 4
2 4
3 4
5 6
7 5
8 5
5 4'''

    assert slow_solution(create_tree(s, slow_create)) == 4

    s = '''8
1 4
2 4
3 4
5 6
7 5
8 5
5 4
'''
    assert slow_solution(create_tree(s, slow_create)) == 4

    s = '''12
11 2
2 4
1 4
3 4
12 3
4 5
5 6
6 10
5 7
5 8
8 9
'''

    assert slow_solution(create_tree(s, slow_create)) == 16

    s = '''13
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1'''

    assert slow_solution(create_tree(s, slow_create)) == 12

    s = '''14
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1
11 14'''

    assert slow_solution(create_tree(s, slow_create)) == 18

    s = '''22
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1
11 14
14 15
15 16
2 17
17 18
18 19
8 20
20 21
21 22'''

    assert slow_solution(create_tree(s, slow_create)) == 40

    s = '''25
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1
11 14
14 15
15 16
2 17
17 18
18 19
8 20
20 21
21 22
5 23
23 24
24 25'''

    assert slow_solution(create_tree(s, slow_create)) == 40

    s = '''10
1 3
2 3
3 4
6 5
7 5
5 4
4 8
8 9
8 10'''

    assert slow_solution(create_tree(s, slow_create)) == 8

    s = '''14
1 3
2 3
3 4
6 5
7 5
5 4
4 8
8 9
8 10
4 11
11 12
12 13
12 14'''

    assert slow_solution(create_tree(s, slow_create)) == 10

    s = '''14
1 3
2 3
3 4
6 5
7 5
5 4
4 8
8 9
8 10
4 11
11 12
12 13
13 14'''

    assert slow_solution(create_tree(s, slow_create)) == 12

    s = '''5
1 2
2 3
2 5
3 4
'''

    assert slow_solution(create_tree(s, slow_create)) == 2

    s = '''23
1 23
1 2
2 3
3 4
1 5
5 6
6 7
7 8
8 9
9 10
10 11
8 19
12 13
13 14
14 15
12 16
16 17
17 18
18 19
19 20
20 21
21 22
    '''
    assert slow_solution(create_tree(s, slow_create)) == 100

    s = '''6
1 2
1 3
1 4
4 5
4 6
    '''

    assert slow_solution(create_tree(s, slow_create)) == 4


def test_2():
    s = '''5
        1 2
        2 5
        2 3
        3 4
        '''

    assert fast_solution(create_tree(s, fast_create)) == 2
    
    s = '''5
        1 2
        1 3
        3 4
        2 5
        '''

    assert fast_solution(create_tree(s, fast_create)) == 2


def test_fast_solution():
    s = '''4
            1 2
            2 3
            3 4
            '''
    assert fast_solution(create_tree(s, fast_create)) == 1

    s = '''7
            1 2
            1 3
            1 4
            1 5
            1 6
            1 7
            '''
    assert fast_solution(create_tree(s, fast_create)) == 0

    s = '''6
1 2
2 3
2 4
5 4
6 4
'''
    assert fast_solution(create_tree(s, fast_create)) == 4

    s = '''17
1 2
2 3
4 5
5 6
3 7
6 7
7 8
8 9
9 10
9 11
11 12
12 13 
13 17
11 14
14 15
15 16'''

    assert fast_solution(create_tree(s, fast_create)) == 36

    s = '''15
1 2
1 3
2 4
4 8
8 12
2 5
3 6
5 9
9 13
3 7
6 10
10 14
7 11
11 15'''

    assert fast_solution(create_tree(s, fast_create)) == 36

    s = '''7
1 2
1 3
1 4
2 5
2 6
4 7'''

    assert fast_solution(create_tree(s, fast_create)) == 6

    s = '''8
1 4
2 4
3 4
5 6
7 5
8 5
5 4'''

    assert fast_solution(create_tree(s, fast_create)) == 4

    s = '''8
1 4
2 4
3 4
5 6
7 5
8 5
5 4
'''
    assert fast_solution(create_tree(s, fast_create)) == 4

    s = '''12
11 2
2 4
1 4
3 4
12 3
4 5
5 6
6 10
5 7
5 8
8 9
'''

    assert fast_solution(create_tree(s, fast_create)) == 16

    s = '''13
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1'''

    assert fast_solution(create_tree(s, fast_create)) == 12

    s = '''14
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1
11 14'''

    assert fast_solution(create_tree(s, fast_create)) == 18

    s = '''22
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1
11 14
14 15
15 16
2 17
17 18
18 19
8 20
20 21
21 22'''

    assert fast_solution(create_tree(s, fast_create)) == 40

    s = '''25
13 12
12 11
4 3
3 2
10 9
9 8
7 6
6 5
8 1
2 1
5 1
11 1
11 14
14 15
15 16
2 17
17 18
18 19
8 20
20 21
21 22
5 23
23 24
24 25'''

    assert fast_solution(create_tree(s, fast_create)) == 40

    s = '''10
1 3
2 3
3 4
6 5
7 5
5 4
4 8
8 9
8 10'''

    assert fast_solution(create_tree(s, fast_create)) == 8

    s = '''14
1 3
2 3
3 4
6 5
7 5
5 4
4 8
8 9
8 10
4 11
11 12
12 13
12 14'''

    assert fast_solution(create_tree(s, fast_create)) == 10

    s = '''14
1 3
2 3
3 4
6 5
7 5
5 4
4 8
8 9
8 10
4 11
11 12
12 13
13 14'''

    assert fast_solution(create_tree(s, fast_create)) == 12

    s = '''5
1 2
2 3
2 5
3 4
'''

    assert fast_solution(create_tree(s, fast_create)) == 2
    
    s = '''6
1 2
1 3
2 4
3 5
5 6'''

    assert fast_solution(create_tree(s, fast_create)) == 4


