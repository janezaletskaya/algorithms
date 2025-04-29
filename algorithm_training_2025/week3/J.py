# J. Упаковка и распаковка*
from collections import Counter
from collections import defaultdict

import heapq


def build_suffix_array(text: str) -> list[int]:
    n = len(text)
    k = 1
    rank = [ord(c) for c in text]
    tmp = [0] * n
    sa = list(range(n))

    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]]
            if (rank[sa[i]] != rank[sa[i - 1]] or
                    (rank[sa[i] + k] if sa[i] + k < n else -1) != (rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1)):
                tmp[sa[i]] += 1
        rank, tmp = tmp, rank

        if rank[sa[-1]] == n - 1:
            break
        k <<= 1

    return sa


def bwt_encode(text: str) -> str:
    text += '\0'
    n = len(text)
    sa = build_suffix_array(text)

    bwt = ''.join(
        text[(idx - 1) % n] for idx in sa
    )

    return bwt


def bwt_decode(bwt_text: str) -> str:
    n = len(bwt_text)

    count = defaultdict(int)
    for char in bwt_text:
        count[char] += 1

    first_occurrence = {}
    total = 0
    for char in sorted(count.keys()):
        first_occurrence[char] = total
        total += count[char]

    lf_mapping = [0] * n
    seen = defaultdict(int)
    for i, char in enumerate(bwt_text):
        lf_mapping[i] = first_occurrence[char] + seen[char]
        seen[char] += 1

    idx = bwt_text.index('\0')
    result = []

    for _ in range(n - 1):
        idx = lf_mapping[idx]
        result.append(bwt_text[idx])

    result.reverse()
    return ''.join(result)


def mtf_encode(text: str) -> list[int]:
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['\0']

    result = []

    for char in text:
        index = alphabet.index(char)
        result.append(index)

        alphabet.pop(index)
        alphabet.insert(0, char)

    return result


def mtf_decode(indices: list[int]) -> str:
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['\0']

    result = []

    for index in indices:
        char = alphabet[index]
        result.append(char)

        alphabet.pop(index)
        alphabet.insert(0, char)

    return ''.join(result)


def rle_encode(data: list[int]) -> list[tuple[int, int]]:
    if not data:
        return []

    result = []
    current_value = data[0]
    count = 1

    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = value
            count = 1

    result.append((current_value, count))

    return result


def rle_decode(data: list[tuple[int, int]]) -> list[int]:
    result = []

    for value, count in data:
        result.extend([value] * count)

    return result


class HuffmanNode:
    def __init__(self, symbol=None, freq=0, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq: dict) -> HuffmanNode:
    heap = [HuffmanNode(symbol=symbol, freq=freq_val) for symbol, freq_val in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(freq=node1.freq + node2.freq, left=node1, right=node2)
        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(node: HuffmanNode, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook


def huffman_encode(data: list[int]) -> tuple[str, dict]:
    freq = Counter(data)
    root = build_huffman_tree(freq)
    codebook = build_huffman_codes(root)

    encoded_data = ''.join(codebook[symbol] for symbol in data)
    return encoded_data, codebook


def huffman_decode(encoded_data: str, codebook: dict) -> list[int]:
    inv_codebook = {v: k for k, v in codebook.items()}

    result = []
    code = ''
    for bit in encoded_data:
        code += bit
        if code in inv_codebook:
            result.append(inv_codebook[code])
            code = ''
    return result


def bits_to_bytes(bits: str):
    bytes_list = []
    padding_length = (8 - len(bits) % 8) % 8
    padded_bits = bits + '0' * padding_length

    for i in range(0, len(padded_bits), 8):
        byte = padded_bits[i:i + 8]
        bytes_list.append(int(byte, 2))

    return bytes_list, padding_length


def bytes_to_bits(bytes_list: list[int]) -> str:
    bits = ''.join(format(byte, '08b') for byte in bytes_list)
    return bits


def encode_to_bytes(text: str) -> list[int]:
    bwt_text = bwt_encode(text)
    mtf_encoded = mtf_encode(bwt_text)

    rle_encoded = rle_encode(mtf_encoded)

    values = [v for v, c in rle_encoded]
    counts = [c for v, c in rle_encoded]

    encoded_values, codebook_values = huffman_encode(values)
    encoded_counts, codebook_counts = huffman_encode(counts)

    value_bytes, value_padding = bits_to_bytes(encoded_values)
    count_bytes, count_padding = bits_to_bytes(encoded_counts)

    output = [len(codebook_values), len(codebook_counts)]

    for symbol, code in codebook_values.items():
        output.append(symbol)
        output.append(len(code))
        code_bytes, _ = bits_to_bytes(code)
        output.extend(code_bytes)

    for symbol, code in codebook_counts.items():
        if symbol < 256:
            output.append(symbol)
            output.append(0)
        else:
            output.append(symbol % 256)
            output.append(symbol // 256 + 1)
        output.append(len(code))
        code_bytes, _ = bits_to_bytes(code)
        output.extend(code_bytes)

    output.append(value_padding)
    output.append(count_padding)

    output.append(len(value_bytes) % 256)
    output.append(len(value_bytes) // 256)
    output.append(len(count_bytes) % 256)
    output.append(len(count_bytes) // 256)

    output.extend(value_bytes)
    output.extend(count_bytes)

    return output


def decode_from_bytes(bytes_list: list[int]) -> str:
    idx = 0

    num_value_symbols = bytes_list[idx]
    idx += 1
    num_count_symbols = bytes_list[idx]
    idx += 1

    codebook_values = {}
    for _ in range(num_value_symbols):
        symbol = bytes_list[idx]
        idx += 1
        code_length = bytes_list[idx]
        idx += 1
        num_code_bytes = (code_length + 7) // 8
        code_bytes = bytes_list[idx:idx + num_code_bytes]
        idx += num_code_bytes
        code_bits = bytes_to_bits(code_bytes)[:code_length]
        codebook_values[symbol] = code_bits

    codebook_counts = {}
    for _ in range(num_count_symbols):
        symbol_low = bytes_list[idx]
        idx += 1
        symbol_high = bytes_list[idx]
        idx += 1
        if symbol_high == 0:
            symbol = symbol_low
        else:
            symbol = symbol_low + (symbol_high - 1) * 256

        code_length = bytes_list[idx]
        idx += 1
        num_code_bytes = (code_length + 7) // 8
        code_bytes = bytes_list[idx:idx + num_code_bytes]
        idx += num_code_bytes
        code_bits = bytes_to_bits(code_bytes)[:code_length]
        codebook_counts[symbol] = code_bits

    value_padding = bytes_list[idx]
    idx += 1
    count_padding = bytes_list[idx]
    idx += 1

    value_size = bytes_list[idx] + bytes_list[idx + 1] * 256
    idx += 2
    count_size = bytes_list[idx] + bytes_list[idx + 1] * 256
    idx += 2

    value_bytes = bytes_list[idx:idx + value_size]
    idx += value_size
    count_bytes = bytes_list[idx:idx + count_size]

    value_bits = bytes_to_bits(value_bytes)
    if value_padding > 0:
        value_bits = value_bits[:-value_padding]

    count_bits = bytes_to_bits(count_bytes)
    if count_padding > 0:
        count_bits = count_bits[:-count_padding]

    values = huffman_decode(value_bits, codebook_values)
    counts = huffman_decode(count_bits, codebook_counts)

    rle_encoded = list(zip(values, counts))
    mtf_encoded = rle_decode(rle_encoded)
    bwt_text = mtf_decode(mtf_encoded)
    original_text = bwt_decode(bwt_text)

    return original_text


if __name__ == "__main__":
    with open('../trash/mobidick_clean_200k.txt', 'r', encoding='utf-8') as f:
        text = input().strip()
        print(f"Длина изначального текста: {len(text)} characters")

        compressed_bytes = encode_to_bytes(text)
        print(len(compressed_bytes))
        print(' '.join(str(byte) for byte in compressed_bytes))
        restored_text = decode_from_bytes(compressed_bytes)

        if restored_text == text:
            print("====SUCCESS====")
        else:
            print("!=!=!ERROR!=!=!")
