from E import tokenize, solution


def test_tokenize():
    assert bool(tokenize('1+(2*2 - 3)')) is True
    assert bool(tokenize('1+a+1')) is False
    assert bool(tokenize('1 1 + 2')) is False
    assert bool(tokenize('2+()-3')) is False
    assert bool(tokenize('1+2-3+4-5+6-7+8-9+ 1 0 -11+12-13')) is False
    assert bool(tokenize('1234x1234')) is False
    assert bool(tokenize('123456-7890+1234*3-(121231)+1+')) is False
    assert bool(tokenize('123+123+')) is False
    assert bool(tokenize('123+123+(-')) is False
    assert bool(tokenize('123+123()')) is False
    assert bool(tokenize('((()))5')) is False
    assert bool(tokenize('(123+123')) is False
    assert bool(tokenize('123+123)')) is False
    assert bool(tokenize(';-2')) is False
    assert bool(tokenize('1+(7+8)-(3-4*5)*(2*4)+(9)-(16728)*(123*9+2)+((2)))+((((((0-19283))))))')) is False

    assert bool(tokenize('(2)-3')) is True
    assert bool(tokenize('+5-1')) is True
    assert bool(tokenize('1000000000*2-2000000000')) is True
    assert bool(tokenize('    123   +    123   *   (   -    312  )')) is True
    assert bool(tokenize('   -   123    +    123   *   (   -    312  )')) is True
    assert bool(tokenize('-123+(-123)')) is True
    assert bool(tokenize('6 + 3 * (1 + 4 * 5) * 2')) is True
    assert bool(tokenize('(1+(7+8)-(3-4*5)*(2*4)+(9)-(16728)*(123*9+2)+((2)))+((((((0-19283))))))')) is True
    assert bool(tokenize('(9) * (2) - (4)')) is True
    assert bool(tokenize('(1+(7+8)-(3-4*5)*(2*4)+(9)-(16728)*(123*9+2)+((2)))+((((((0-19283))))))')) is True


def test_solution():
    test_cases = [
        ("6 + 3 * (1 + 4 * 5) * 2", 132),
        ("1+((((( ((((((( 2 )-3)+ 4 * 6 ) -4)*4+4))))))))", 81),
        ("1234x1234","WRONG")
    ]

    for inp, res in test_cases:
        assert solution(inp) == res
