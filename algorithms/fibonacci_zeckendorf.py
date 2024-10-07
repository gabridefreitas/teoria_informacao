def encode_fibonacci_zeckendorf(input_string):
    n = int(input_string)

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

    return "".join(result)


def decode_fibonacci_zeckendorf(input_string):
    result = 0
    fib = [0, 1]

    while len(fib) < len(input_string) + 2:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)

    for i in range(len(input_string)):
        if input_string[len(input_string) - 1 - i] == "1":
            result += fib[i + 2]

    return str(result)
