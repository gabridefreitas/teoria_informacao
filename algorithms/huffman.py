import heapq
from collections import defaultdict, namedtuple

global LAST_DICT


class Node(namedtuple("No", ["char", "freq", "left", "right"])):
    def __lt__(self, outro):
        return self.freq < outro.freq


def build_huffman_tree(input_string):
    frequency = defaultdict(int)

    for char in input_string:
        frequency[char] += 1

    priority_queue = [Node(char, freq, None, None) for char, freq in frequency.items()]

    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        combined = Node(None, left.freq + right.freq, left, right)

        heapq.heappush(priority_queue, combined)

    return priority_queue[0]


def generate_codes(node, prefix="", code_dictionary=None):
    if code_dictionary is None:
        code_dictionary = {}

    if node.char is not None:
        code_dictionary[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_dictionary)
        generate_codes(node.right, prefix + "1", code_dictionary)

    global LAST_DICT
    LAST_DICT = code_dictionary

    return code_dictionary


def encode_huffman(input_string):
    root = build_huffman_tree(input_string)
    codes = generate_codes(root)

    encoded_text = "".join(codes[char] for char in input_string)

    return encoded_text, codes


def decode_huffman(input_string):
    inverted_codes = {v: k for k, v in LAST_DICT.items()}
    decoded_text = []
    current_code = ""

    for bit in input_string:
        current_code += bit
        if current_code in inverted_codes:
            decoded_text.append(inverted_codes[current_code])
            current_code = ""

    return "".join(decoded_text)
