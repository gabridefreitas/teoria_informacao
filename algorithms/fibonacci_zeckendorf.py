




def codificar_fibonacci_zeckendorf(string):
    ret=""
    for char in string:
        ret+=codificar_char(char)+"1"
    return ret


def codificar_char(char):
    n = ord(char)
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

    string_prep="".join(result)
    
    return "".join(result)[::-1]


def decodificar_fibonacci_zeckendorf(codigo):
    ret=""
    current_index = 0
    
    while current_index < len(codigo):
        end_index = codigo.find('11', current_index)
    
        if end_index == -1:
            return ret;
        end_index+=1
        string_code = codigo[current_index:end_index]
        ret+=chr(decodificar_char(string_code))
        current_index=end_index+1

    return ret





def decodificar_char(codigo):
    codigo = codigo[::-1]
    result = 0
    fib = [0, 1]
    while len(fib) < len(codigo) + 2:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    for i in range(len(codigo)):
        if codigo[len(codigo) - 1 - i] == "1":
            result += fib[i + 2]
    return result

