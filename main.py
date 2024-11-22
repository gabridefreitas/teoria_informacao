from algorithms.bsc import encode_bsc, decode_bsc
from algorithms.elias_gamma import encode_elias_gamma, decode_elias_gamma
from algorithms.fibonacci_zeckendorf import (
    encode_fibonacci_zeckendorf,
    decode_fibonacci_zeckendorf,
)
from algorithms.golomb import encode_golomb, decodificar_golomb
from algorithms.hamming import encode_hamming, decode_hamming
from algorithms.huffman import encode_huffman, decode_huffman

BSC = "BSC"
DECODE = "Decodificar"
ELIAS_GAMMA = "Elias Gamma"
ENCODE = "Codificar"
FIBONACCI_ZECKENDORF = "Fibonacci/Zeckendorf"
GOLOMB = "Golomb"
HAMMING = "Hamming (7,4)"
HUFFMAN = "Huffman"


def normalize_operation(option):
    if option == "1":
        return ENCODE
    if option == "2":
        return DECODE
    exit()


def normalize_algorithm(algorithm):
    if algorithm == "1":
        return ELIAS_GAMMA
    if algorithm == "2":
        return FIBONACCI_ZECKENDORF
    if algorithm == "3":
        return GOLOMB
    if algorithm == "4":
        return HUFFMAN
    if algorithm == "5":
        return HAMMING
    return BSC


def resolve_algorithm(option, algorithm, secret):
    if option == ENCODE:
        if algorithm == ELIAS_GAMMA:
            return encode_elias_gamma(secret)
        if algorithm == FIBONACCI_ZECKENDORF:
            return encode_fibonacci_zeckendorf(secret)
        if algorithm == GOLOMB:
            return encode_golomb(secret, 7)
        if algorithm == HUFFMAN:
            return encode_huffman(secret)
        if algorithm == HAMMING:
            return encode_hamming(secret)
        return encode_bsc(secret, get_bsc_r())
    else:
        if algorithm == ELIAS_GAMMA:
            return decode_elias_gamma(secret)
        if algorithm == FIBONACCI_ZECKENDORF:
            return decode_fibonacci_zeckendorf(secret)
        if algorithm == GOLOMB:
            return decodificar_golomb(secret, 7)
        if algorithm == HUFFMAN:
            return decode_huffman(secret)
        if algorithm == HAMMING:
            return decode_hamming(secret)
        return decode_bsc(secret, get_bsc_r())


def get_bsc_r():
    while True:
        r = input("\nInforme o valor de r: ")

        if not r.isdigit():
            print("\nValor inválido, tente novamente.")
        else:
            return int(r)


def get_operation(values):
    while True:
        option = input("\nDigite a opção desejada: ")

        if option not in values:
            print("\nOpção inválida, tente novamente.")
        else:
            return option


def get_secret(option, algorithm):
    while True:
        secret = input(
            f"\nInforme o que deseja {option} com o algoritmo de {algorithm}: "
        )

        if option == DECODE and not all(c in "01" for c in secret):
            print("\nCódigo inválido, tente novamente.")
        else:
            return secret


def main():
    while True:
        print(
            "\nBem vindo, informe o que você deseja fazer:\n"
            + "1 - Codificar\n"
            + "2 - Decodificar\n"
            + "3 - Encerrar o programa."
        )

        option = normalize_operation(get_operation(["1", "2", "3"]))

        print(
            "\nEscolha o algoritmo desejado:\n"
            + "1 - Elias Gamma\n"
            + "2 - Fibonacci/Zeckendorf\n"
            + "3 - Golomb\n"
            + "4 - Huffman\n"
            + "5 - Hamming (7,4)\n"
            + "6 - BSC"
        )

        algorithm = normalize_algorithm(get_operation(["1", "2", "3", "4", "5", "6"]))

        secret = get_secret(option, algorithm)

        print(f"\nResultado: {resolve_algorithm(option, algorithm, secret)}")


main()
