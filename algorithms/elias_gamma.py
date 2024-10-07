def encode_elias_gamma(input_string):
    encoded_string = []

    for char in input_string:
        ascii_val = ord(char)
        binary = bin(ascii_val)[2:]

        if ascii_val == 1:
            encoded_string.append("1")
            continue

        prefix = "0" * (len(binary) - 1)
        encoded_string.append(prefix + binary)

    return "".join(encoded_string)


def decode_elias_gamma(input_string):
    decoded_string = []
    i = 0
    input_length = len(input_string)

    while i < input_length:
        zero_count = 0

        while i < input_length and input_string[i] == "0":
            zero_count += 1
            i += 1

        if i < input_length and input_string[i] == "1":
            i += 1

        binary = "1"
        for _ in range(zero_count):
            if i < input_length:
                binary += input_string[i]
                i += 1

        ascii_val = int(binary, 2)
        decoded_string.append(chr(ascii_val))

    return "".join(decoded_string)
