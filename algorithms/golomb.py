import math


def encode_golomb(input_string, m):
    encoded_string = []

    for char in input_string:
        ascii_val = ord(char)

        q = ascii_val // m
        r = ascii_val % m

        quotient = "1" * q + "0"

        num_bits_remainder = math.ceil(math.log2(m))
        remainder = format(r, f"0{num_bits_remainder}b")

        encoded_string.append(quotient + remainder)

    return "".join(encoded_string)


def decodificar_golomb(input_string, m):
    decoded_string = []
    remainder_bits_length = math.ceil(math.log2(m))
    current_index = 0

    while current_index < len(input_string):
        quotient = 0
        while current_index < len(input_string) and input_string[current_index] == "1":
            quotient += 1
            current_index += 1

        if current_index < len(input_string) and input_string[current_index] == "0":
            current_index += 1

        remainder_binary = input_string[
            current_index : current_index + remainder_bits_length
        ]
        remainder = int(remainder_binary, 2)
        current_index += remainder_bits_length

        ascii_val = quotient * m + remainder
        decoded_string.append(chr(ascii_val))

    return "".join(decoded_string)
