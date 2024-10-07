def string_to_ascii(input_string):
    ascii_values = [str(ord(char)) for char in input_string]
    ascii_number = "".join(ascii_values)
    return int(ascii_number)


def ascii_to_string(ascii_number):
    ascii_str = str(ascii_number)
    result = []

    i = 0
    while i < len(ascii_str):
        if i + 2 < len(ascii_str) and 32 <= int(ascii_str[i : i + 3]) <= 126:
            result.append(chr(int(ascii_str[i : i + 3])))
            i += 3
        else:
            result.append(chr(int(ascii_str[i : i + 2])))
            i += 2

    return "".join(result)
