# E. Слабое звено
def round(to_check, round_num, rem):
    losers = []
    to_check_next_round = set()

    for player in to_check:
        if not rem_indices[player]:
            continue

        left_player = left_indices[player]
        right_player = right_indices[player]

        if players[player] < players[left_player] and players[player] < players[right_player]:
            losers.append(player)

    if not losers:
        return set(), rem

    for player in losers:
        rem_indices[player] = False
        res[player] = round_num
        rem -= 1

        left_player = left_indices[player]
        right_player = right_indices[player]

        right_indices[left_player] = right_player
        left_indices[right_player] = left_player

        to_check_next_round.add(left_player)
        to_check_next_round.add(right_player)

    return {p for p in to_check_next_round if rem_indices[p]}, rem


def solution(players):
    global right_indices, left_indices, rem_indices, res

    right_indices = [(len(players) + i + 1) % len(players) for i in range(len(players))]
    left_indices = [(len(players) + i - 1) % len(players) for i in range(len(players))]
    rem_indices = [True] * len(players)
    res = [0] * len(players)

    to_check = set(range(len(players)))
    round_num = 0
    rem = len(players)

    while rem > 2:
        round_num += 1
        to_check, rem = round(to_check, round_num, rem)

        if not to_check:
            break

    return res


if __name__ == '__main__':
    n = int(input())
    players = list(map(int, input().split()))
    print(*solution(players))
