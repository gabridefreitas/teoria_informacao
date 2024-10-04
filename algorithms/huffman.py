import heapq
from collections import defaultdict, namedtuple


class No(namedtuple("No", ["char", "freq", "esquerda", "direita"])):
    def __lt__(self, outro):
        return self.freq < outro.freq


def construir_arvore_huffman(texto):
    frequencia = defaultdict(int)
    for caractere in texto:
        frequencia[caractere] += 1

    fila_prioridade = [
        No(caractere, freq, None, None) for caractere, freq in frequencia.items()
    ]
    heapq.heapify(fila_prioridade)

    while len(fila_prioridade) > 1:
        esquerda = heapq.heappop(fila_prioridade)
        direita = heapq.heappop(fila_prioridade)
        mesclado = No(None, esquerda.freq + direita.freq, esquerda, direita)
        heapq.heappush(fila_prioridade, mesclado)

    return fila_prioridade[0]


def construir_codigos(no, prefixo="", dicionario_codigos=None):
    if dicionario_codigos is None:
        dicionario_codigos = {}

    if no.char is not None:
        dicionario_codigos[no.char] = prefixo
    else:
        construir_codigos(no.esquerda, prefixo + "0", dicionario_codigos)
        construir_codigos(no.direita, prefixo + "1", dicionario_codigos)

    return dicionario_codigos


def codificar_huffman(texto):
    raiz = construir_arvore_huffman(texto)
    codigos = construir_codigos(raiz)

    texto_codificado = "".join(codigos[caractere] for caractere in texto)
    return texto_codificado, codigos


def decodificar_huffman(codigo, codigos):
    codigos_invertidos = {v: k for k, v in codigos.items()}
    texto_decodificado = []
    codigo_atual = ""

    for bit in codigo:
        codigo_atual += bit
        if codigo_atual in codigos_invertidos:
            texto_decodificado.append(codigos_invertidos[codigo_atual])
            codigo_atual = ""

    return "".join(texto_decodificado)
