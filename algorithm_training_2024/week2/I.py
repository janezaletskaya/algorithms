def solution(n, a_values, b_values, p_values):
    algorithms = [(i + 1, a_values[i], b_values[i]) for i in range(n)]
    by_a = sorted(algorithms, key=lambda x: (-x[1], -x[2], x[0]))
    by_b = sorted(algorithms, key=lambda x: (-x[2], -x[1], x[0]))

    a_pointer = 0
    b_pointer = 0

    already = set()
    res = []

    for p in p_values:
        if p == 1:
            while by_b[b_pointer][0] in already:
                b_pointer += 1
            choice = by_b[b_pointer]
        elif p == 0:
            while by_a[a_pointer][0] in already:
                a_pointer += 1
            choice = by_a[a_pointer]

        res.append(choice[0])
        already.add(choice[0])

    return res


def slow_solution(n, a_values, b_values, p_values):
    algorithms = [(i + 1, a_values[i], b_values[i]) for i in range(n)]

    by_a = sorted(algorithms, key=lambda x: (-x[1], -x[2], x[0]))
    by_b = sorted(algorithms, key=lambda x: (-x[2], -x[1], x[0]))

    already_a = set(by_a)
    already_b = set(by_b)

    res = []

    for p in p_values:
        if p == 1:
            for algo in by_b:
                if algo in already_b:
                    res.append(algo[0])
                    already_a.remove(algo)
                    already_b.remove(algo)
                    break
        else:
            for algo in by_a:
                if algo in already_a:
                    res.append(algo[0])
                    already_b.remove(algo)
                    already_a.remove(algo)
                    break

    return res


if __name__ == '__main__':
    n = int(input())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))
    p_values = list(map(int, input().split()))

    print(*solution(n, a_values, b_values, p_values))
