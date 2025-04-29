# C. Переупорядочивание с XOR
def solution(bit_nums):
    max_len = len(bit_nums[0])
    for i in range(max_len - 1):
        bit_sum = 0
        for j in range(n):
            bit_sum ^= bit_nums[j][i]
            if bit_sum == 1:
                flag = False
                for j in range(n):
                    if not flag and bit_nums[j][i] == 1 and bit_nums[j][-1] == 0:
                        bit_nums[j][i], bit_nums[j][-1] = bit_nums[j][-1], bit_nums[j][i]
                        flag = True

                    if not flag:
                        for j in range(n):
                            if not flag and bit_nums[j][i] == 0 and bit_nums[j][-1] == 1:
                                bit_nums[j][i], bit_nums[j][-1] = bit_nums[j][-1], bit_nums[j][i]
                                flag = True

    bit_sum = 0
    for j in range(n):
        bit_sum ^= bit_nums[j][-1]

    if bit_sum == 1:
        return ('impossible', )
    else:
        ans = []
        for i in range(n):
            s = ''.join(map(str, bit_nums[i]))
            ans.append(int(s, 2))

        return ans


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    max_len = max(nums).bit_length()
    bit_nums = []
    for i in range(n):
        bits = list(map(int, bin(nums[i])[2:])) + [0] * (max_len - nums[i].bit_length())
        bits.sort(reverse=True)
        bit_nums.append(bits)

    print(*solution(bit_nums))
