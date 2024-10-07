def generate_fibonacci_up_to(n):
    fibonacci = [1, 2]

    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]
        if next_fib > n:
            break
        fibonacci.append(next_fib)

    return fibonacci


def generate_fibonacci_for_length(length):
    fibonacci = [1, 2]

    for _ in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci


def encode_fibonacci_zeckendorf(input_string):
    encoded_string = []

    for char in input_string:
        ascii_val = ord(char)
        fibonacci = generate_fibonacci_up_to(ascii_val)

        fib_code = []

        for f in reversed(fibonacci):
            if ascii_val >= f:
                fib_code.append("1")
                ascii_val -= f
            else:
                fib_code.append("0")

        fib_code.append("11")

        encoded_string.append("".join(fib_code))

    return "".join(encoded_string)


def decode_fibonacci_zeckendorf(encoded_string):
    decoded_string = []
    current_index = 0

    while current_index < len(encoded_string):
        end_index = encoded_string.find("11", current_index)

        if end_index == -1:
            break

        encoded_char = encoded_string[current_index:end_index]

        if len(encoded_char) == 0:
            break

        fibonacci = generate_fibonacci_for_length(len(encoded_char))

        ascii_val = 0

        for i, bit in enumerate(reversed(encoded_char)):
            if bit == "1":
                ascii_val += fibonacci[i]

        decoded_string.append(chr(ascii_val))

        current_index = end_index + 2

    return "".join(decoded_string)
