# A. Каждому по компьютеру
def solution(students: list[int], computers: list[int]) -> tuple[int, list[int]]:
    rooms = [0] * len(students)
    computers = sorted([(n_comp, i) for i, n_comp in enumerate(computers)], key=lambda x: (-x[0], x[1]))
    students = sorted([(n_students, j) for j, n_students in enumerate(students)], key=lambda x: (-x[0], x[1]))
    ptr_students, ptr_computers = 0, 0

    cnt = 0
    while ptr_students < len(students) and ptr_computers < len(computers):
        n_comp, n_room = computers[ptr_computers]
        n_students, n_group = students[ptr_students]

        if n_students + 1 > n_comp:
            ptr_students += 1
        else:
            rooms[n_group] = n_room + 1
            cnt += 1
            ptr_computers += 1
            ptr_students += 1

    return cnt, rooms


if __name__ == '__main__':
    input()
    students = list(map(int, input().split()))
    computers = list(map(int, input().split()))
    n_group, rooms = solution(students, computers)
    print(n_group)
    print(*rooms)
