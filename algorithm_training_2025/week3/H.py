class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    def add_value(self, x, y, z, value):
        x += 1
        y += 1
        z += 1

        x0, y0, z0 = x, y, z
        while x0 <= self.n:
            y0 = y
            while y0 <= self.n:
                z0 = z
                while z0 <= self.n:
                    self.tree[x0][y0][z0] += value
                    z0 += z0 & -z0
                y0 += y0 & -y0
            x0 += x0 & -x0

    def sum_coord(self, x, y, z):
        x += 1
        y += 1
        z += 1

        result = 0
        cur_x, cur_y, cur_z = x, y, z
        while cur_x > 0:
            cur_y = y
            while cur_y > 0:
                cur_z = z
                while cur_z > 0:
                    result += self.tree[cur_x][cur_y][cur_z]
                    cur_z -= cur_z & -cur_z
                cur_y -= cur_y & -cur_y
            cur_x -= cur_x & -cur_x
        return result

    def execute_query(self, x1, y1, z1, x2, y2, z2):
        # формула включений-исключений
        result = self.sum_coord(x2, y2, z2)
        result -= self.sum_coord(x1 - 1, y2, z2)
        result -= self.sum_coord(x2, y1 - 1, z2)
        result -= self.sum_coord(x2, y2, z1 - 1)
        result += self.sum_coord(x1 - 1, y1 - 1, z2)
        result += self.sum_coord(x1 - 1, y2, z1 - 1)
        result += self.sum_coord(x2, y1 - 1, z1 - 1)
        result -= self.sum_coord(x1 - 1, y1 - 1, z1 - 1)
        return result


if __name__ == "__main__":
    n = int(input())
    ft = FenwickTree(n)
    string = input()
    while string != '3':
        query_list = list(map(int, string.split()))

        if query_list[0] == 1:
            x, y, z, k = query_list[1:]
            ft.add_value(x, y, z, k)

        elif query_list[0] == 2:
            x1, y1, z1, x2, y2, z2 = query_list[1:]
            result = ft.execute_query(x1, y1, z1, x2, y2, z2)
            print(result)

        string = input()
