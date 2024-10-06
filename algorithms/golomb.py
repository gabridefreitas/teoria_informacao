import math


def codificar_golomb(num, m):
    n = int(num)

    q = n // m
    r = n % m

    b = math.floor(math.log2(m))
    k = 2 ** (b + 1) - m
    
    print(q)

    quociente = "0" * q + "1"

    if r < k:
        resto = bin(r)[2:]
        resto = resto.zfill(b)
    else:
        resto = bin(r + k)[2:]
        resto = resto.zfill(b + 1)

    codigo_golomb = quociente + resto

    return codigo_golomb


def decodificar_golomb(codigo, M):
    b = math.floor(math.log2(M))
    k = 2 ** (b + 1) - M

    q = 0
    while codigo[q] == "0":
        q += 1

    resto_binario = codigo[q + 1 :]

    r = int(resto_binario, 2)

    if r >= k:
        r -= k

    N = q * M + r

    return N
