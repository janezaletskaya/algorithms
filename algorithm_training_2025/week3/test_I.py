from I import decode, encode
import random

import time
import tracemalloc


def glue(message_lst: list) -> str:
    return ''.join(str(bit) for bit in message_lst)


def bit_flip(encoded_message: list[int], flip_pos) -> str:
    encoded_message[flip_pos] = 1 - encoded_message[flip_pos]

    return ''.join(str(bit) for bit in encoded_message)


def random_bit_flip(encoded_message: list[int]) -> str:
    len_ = len(encoded_message)
    flip_pos = random.randint(0, len_ - 1)

    return bit_flip(encoded_message, flip_pos)


def test_random(len_query=10_000):
    for _ in range(1, len_query + 1):
        message = ''.join(random.choice('01') for _ in range(l))
        enc = encode(message)
        enc_err = random_bit_flip(enc)
        decode_message = decode(enc_err)
        assert message == glue(decode_message)


def test_all_flips(len_query=1000):
    for _ in range(1):
        message = ''.join(random.choice('01') for _ in range(len_query))
        enc = encode(message)
        for i in range(len(enc)):
            enc_err = bit_flip(enc.copy(), i)
            decode_message = decode(enc_err)
            assert message == glue(decode_message)


def test_time(len_query=10 ** 5):
    message = ''.join(['1'] * len_query)

    start_time = time.time()
    enc = encode(message)
    decode_message = decode(glue(enc))
    end_time = time.time()
    assert message == glue(decode_message)

    print(f" Время: {end_time - start_time:.4f} сек")


def test_memory(len_query=10 ** 5):
    message = ''.join(random.choice('01') for _ in range(len_query))

    tracemalloc.start()
    enc = encode(message)
    enc_error = random_bit_flip(enc)
    decode_message = decode(enc_error)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert message == glue(decode_message)

    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} MB")
