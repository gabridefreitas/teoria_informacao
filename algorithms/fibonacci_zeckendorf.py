def codify_char(char):
    n = ord(char)
    result = []
    fibonacci = [1, 2]

    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]
        if next_fib > n:
            break
        fibonacci.append(next_fib)

    first_one = False

    for i in range(len(fibonacci) - 1, -1, -1):
        if n >= fibonacci[i]:
            result.append("1")
            n -= fibonacci[i]
            first_one = True
        elif first_one:
            result.append("0")

    if not result:
        return "0"

    return "".join(result)[::-1]


def encode_fibonacci_zeckendorf(input_string):
    ret = ""

    for char in input_string:
        ret += codify_char(char) + "1"

    return ret


def decode_char(code):
    code = code[::-1]

    result = 0
    fib = [0, 1]

    while len(fib) < len(code) + 2:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)

    for i in range(len(code)):
        if code[len(code) - 1 - i] == "1":
            result += fib[i + 2]

    return result


def decode_fibonacci_zeckendorf(input_string):
    ret = ""
    current_index = 0

    while current_index < len(input_string):
        end_index = input_string.find("11", current_index)

        if end_index == -1:
            return ret

        end_index += 1

        string_code = input_string[current_index:end_index]
        ret += chr(decode_char(string_code))

        current_index = end_index + 1

    return ret
