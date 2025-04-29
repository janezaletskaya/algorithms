import sys

input = sys.stdin.readline

log_block = 10
bits_in_block = 1 << log_block


def solution(size, rooks):
    cnt_blocks = (size + bits_in_block - 1) >> log_block
    xy = [[False] * size for _ in range(size)]
    xz = [[0] * cnt_blocks for _ in range(size)]
    yz = [[0] * cnt_blocks for _ in range(size)]

    for rook in rooks:
        x, y, z = rook
        xy[x][y] = True
        z_block = z >> log_block
        z_pos = z & (bits_in_block - 1)
        z_set = 1 << z_pos

        xz[x][z_block] |= z_set
        yz[y][z_block] |= z_set

    last_bits = (cnt_blocks << log_block) - size
    last_block_filler = ((1 << last_bits) - 1) << (bits_in_block - last_bits)

    for i in range(size):
        xz[i][cnt_blocks - 1] |= last_block_filler
        yz[i][cnt_blocks - 1] |= last_block_filler

    filled_block = (1 << bits_in_block) - 1

    for x in range(size):
        for y in range(size):
            if not xy[x][y]:
                for block in range(cnt_blocks):
                    if xz[x][block] | yz[y][block] != filled_block:
                        cur_pos = 1
                        for i in range(bits_in_block):
                            if (xz[x][block] | yz[y][block]) & cur_pos == 0:
                                z = (block << log_block) + i
                                return x + 1, y + 1, z + 1

                            cur_pos = cur_pos << 1

    return None


if __name__ == '__main__':
    size, k = map(int, input().split())
    rooks = []
    for _ in range(k):
        x, y, z = map(int, input().split())
        rooks.append((x - 1, y - 1, z - 1))

    ans = solution(size, rooks)
    if ans is None:
        print('YES')
    else:
        print('NO')
        print(*ans)
