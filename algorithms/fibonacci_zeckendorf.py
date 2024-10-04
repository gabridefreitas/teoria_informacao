def codificar_fibonacci_zeckendorf(num):
    n = int(num)

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


def decodificar_fibonacci_zeckendorf(codigo):
    result = 0
    fib = [0, 1]

    while len(fib) < len(codigo) + 2:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)

    for i in range(len(codigo)):
        if codigo[len(codigo) - 1 - i] == "1":
            result += fib[i + 2]

    return str(result)
