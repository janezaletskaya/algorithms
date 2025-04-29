# I. Исправление одной ошибки*
def count_k(message_len):
    k = 0
    while (2 ** k) < (message_len + k + 1):
        k += 1
    return k


def encode(message: str) -> list[int]:
    k = count_k(len(message))
    encoded_message = [0] * (len(message) + k)

    index = 0
    pow_ = 1

    for pos in range(len(encoded_message)):
        if pos == pow_ - 1:
            pow_ *= 2
            continue
        encoded_message[pos] = int(message[index])
        index += 1

    set_control_bits(encoded_message)
    return encoded_message


def set_control_bits(encoded_message):
    n = len(encoded_message)
    i = 1
    while i < n:
        control_pos = i - 1
        parity = 0
        for j in range(n):
            if (j + 1) & i:
                parity ^= encoded_message[j]
        encoded_message[control_pos] = 1 - parity
        i <<= 1


def decode(message: str):
    message = [int(c) for c in message]
    n = len(message)
    error_pos = 0

    i = 0
    while (1 << i) < n:
        parity = 0
        for j in range(n):
            if (j + 1) & (1 << i):
                parity ^= message[j]
        if parity == 0:
            error_pos += (1 << i)
        i += 1

    if error_pos != 0:
        message[error_pos - 1] ^= 1

    decoded = []
    for idx in range(1, n + 1):
        if not (idx & (idx - 1)) == 0:
            decoded.append(str(message[idx - 1]))

    return decoded


if __name__ == '__main__':
    query_type = int(input())
    message = input()

    if query_type == 1:
        print(*encode(message), sep='')
    elif query_type == 2:
        print(*decode(message), sep='')


