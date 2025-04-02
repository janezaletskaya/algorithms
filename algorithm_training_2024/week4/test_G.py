from G import *


def test_solution():
    g1 = Graphs()
    lst1 = [
        '1 2',
        '2 3',
        '3 4'
    ]

    for s in lst1:
        idx1, idx2 = map(int, s.split())
        g1.add_edge(idx1, idx2)
    g1.make_dict_subgraphs()

    assert g1.subgraphs == {
        0: [4, 3]
    }

    g2 = Graphs()
    lst2 = [
        '1 2',
        '2 3',
        '4 3',
        '5 6'
    ]

    for s in lst2:
        idx1, idx2 = map(int, s.split())
        g2.add_edge(idx1, idx2)
    g2.make_dict_subgraphs()

    assert g2.subgraphs == {
        0: [4, 3], 1: [2, 1]
    }

    g3 = Graphs()
    lst3 = [
        '1 2',
        '2 3',
        '4 3',
        '5 6',
        '7 6'
    ]

    for s in lst3:
        idx1, idx2 = map(int, s.split())
        g3.add_edge(idx1, idx2)
    g3.make_dict_subgraphs()

    assert g3.subgraphs == {
        0: [4, 3], 1: [3, 2]
    }

    g4 = Graphs()
    lst4 = [
        '1 2',
        '2 3',
        '5 6',
        '7 6',
    ]

    for s in lst4:
        idx1, idx2 = map(int, s.split())
        g4.add_edge(idx1, idx2)
    g4.make_dict_subgraphs()

    assert g4.subgraphs == {
        0: [3, 2], 1: [3, 2]
    }

