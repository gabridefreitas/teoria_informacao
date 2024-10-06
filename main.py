from algorithms.elias_gamma import codificar_elias_gamma, decodificar_elias_gamma
from algorithms.fibonacci_zeckendorf import (
    codificar_fibonacci_zeckendorf,
    decodificar_fibonacci_zeckendorf,
)
from algorithms.golomb import codificar_golomb, decodificar_golomb
from algorithms.huffman import codificar_huffman, decodificar_huffman
from algorithms.tools import (
    string_para_ascii_number,
    ascii_number_para_string,
)

ENCODE = "Codificar"
DECODE = "Decodificar"
ELIAS_GAMMA = "Elias Gamma"
FIBONACCI_ZECKENDORF = "Fibonacci/Zeckendorf"
GOLOMB = "Golomb"
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
    return HUFFMAN

def resolve_algorithm(option, algorithm, secret):
    if option == ENCODE:
        if algorithm == ELIAS_GAMMA:
            conversao = string_para_ascii_number(secret)
            return codificar_elias_gamma(conversao)
        if algorithm == FIBONACCI_ZECKENDORF:
            conversao = string_para_ascii_number(secret)
            return codificar_fibonacci_zeckendorf(conversao)
        if algorithm == GOLOMB:
            conversao = string_para_ascii_number(secret)
            return codificar_golomb(conversao, 7)
        return codificar_huffman(secret)
    else:
        if algorithm == ELIAS_GAMMA:
            return ascii_number_para_string(decodificar_elias_gamma(secret))
        if algorithm == FIBONACCI_ZECKENDORF:
            return ascii_number_para_string(decodificar_fibonacci_zeckendorf(secret))
        if algorithm == GOLOMB:
            return ascii_number_para_string(decodificar_golomb(secret, 7))
        return decodificar_huffman(secret)


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
            + "4 - Huffman"
        )

        algorithm = normalize_algorithm(get_operation(["1", "2", "3", "4"]))

        secret = get_secret(option, algorithm)

        print(f"\nResultado: {resolve_algorithm(option, algorithm, secret)}")


main()
