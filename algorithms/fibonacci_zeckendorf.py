def codificar_fibonacci_zeckendorf(num):
    n = int(num)

    resultado = []

    fibonacci = [1, 2]

    while True:
        prox = fibonacci[-1] + fibonacci[-2]

        if prox > n:
            break

        fibonacci.append(prox)

    primeiro = False

    for i in range(len(fibonacci) - 1, -1, -1):
        if n >= fibonacci[i]:
            resultado.append("1")
            n -= fibonacci[i]
            primeiro = True
        elif primeiro:
            resultado.append("0")

    if not resultado:
        return "0"

    return "".join(resultado)


def decodificar_fibonacci_zeckendorf(codigo):
    resultado = 0
    fib = [0, 1]

    while len(fib) < len(codigo) + 2:
        prox = fib[-1] + fib[-2]
        fib.append(prox)

    for i in range(len(codigo)):
        if codigo[len(codigo) - 1 - i] == "1":
            resultado += fib[i + 2]

    return str(resultado)
