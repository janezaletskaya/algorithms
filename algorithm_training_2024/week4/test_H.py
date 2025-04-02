from memory_profiler import memory_usage

from unittest.mock import patch
from textwrap import dedent
import random
import timeit
from functools import partial

from H_additional import solution, create_tree_from_console


def create_tree(s):
    inputs = dedent(s).strip().split('\n')
    with patch("builtins.input", side_effect=inputs):
        tree = create_tree_from_console()
    return tree


def generate_tree(n):
    if n <= 1:
        raise ValueError("The tree must have at least 2 nodes.")

    edges = [f'{n}']
    for i in range(2, n + 1):
        # Соединяем текущую вершину с одной из уже добавленных
        parent = random.randint(1, i - 1)
        edges.append(f"{parent} {i}")

    return '\n'.join(edges)


def test_load():
    n = 500000
    inp = generate_tree(n)
    val = 10 ** 9
    vals = [str(val)] * n
    inp += '\n' + ' '.join(vals)

    tree = create_tree(inp)
    execution_time = timeit.timeit(partial(solution, tree), number=1)
    print(execution_time)

