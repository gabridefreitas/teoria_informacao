def codificar_elias_gamma(num):
    n = int(num)

    if n <= 0:
        raise ValueError("O número deve ser maior que zero.")

    k = n.bit_length() - 1

    prefixo = "0" * k

    numero_binario = bin(n)[2:]

    codigo = prefixo + numero_binario

    return codigo


def decodificar_elias_gamma(codigo):
    n = 0
    i = 0

    while i < len(codigo):

        contagem_zeros = 0

        while i < len(codigo) and codigo[i] == "0":
            contagem_zeros += 1
            i += 1

        if i < len(codigo):
            n = (1 << contagem_zeros) + int(codigo[i : i + contagem_zeros], 2) - 1
            i += contagem_zeros

    return n
