def encode(bits):
    t1 = int(bits[0]) ^ int(bits[1]) ^ int(bits[2])
    t2 = int(bits[1]) ^ int(bits[2]) ^ int(bits[3])
    t3 = int(bits[0]) ^ int(bits[2]) ^ int(bits[3])

    return bits + str(t1) + str(t2) + str(t3)


def encode_char(input_string):
    first_half = ord(input_string) & 0xF
    second_half = ord(input_string) >> 4 & 0xF

    first_half_bin = bin(first_half)[2:]
    missing_zeros = 4 - len(first_half_bin)
    first_half_bin = "0" * missing_zeros + first_half_bin

    second_half_bin = bin(second_half)[2:]
    missing_zeros = 4 - len(second_half_bin)
    second_half_bin = "0" * missing_zeros + second_half_bin

    return encode(first_half_bin) + encode(second_half_bin)


def encode_hamming(input_string):
    ret = ""

    for c in input_string:
        ret += encode_char(c)

    return ret


def decode(bits):
    integrity = [int(bits[4]), int(bits[5]), int(bits[6])]

    t1 = int(bits[0]) ^ int(bits[1]) ^ int(bits[2]) == integrity[0]
    t2 = int(bits[1]) ^ int(bits[2]) ^ int(bits[3]) == integrity[1]
    t3 = int(bits[0]) ^ int(bits[2]) ^ int(bits[3]) == integrity[2]

    if not t1 and not t2 and t3:
        bits = bits[:1] + str((int(bits[1]) ^ 1)) + bits[2:]
    elif t1 and not t2 and not t3:
        bits = bits[:3] + str((int(bits[3]) ^ 1)) + bits[4:]
    elif not t1 and t2 and not t3:
        bits = bits[:0] + str((int(bits[0]) ^ 1)) + bits[1:]
    elif not t1 and not t2 and not t3:
        return False
    return bits[:4]


def decode_char(char):
    first_half_bin = char[:7]
    second_half_bin = char[7:]

    return decode(second_half_bin) + decode(first_half_bin)


def decode_hamming(input_string):
    ret = ""

    for i in range(0, len(input_string), 14):
        ret += chr(int(decode_char(input_string[i : i + 14]), 2))

    return ret
