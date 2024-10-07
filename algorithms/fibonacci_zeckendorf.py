




def encode_fibonacci_zeckendorf(string):
    ret=""
    for char in string:
        ret+=codify_char(char)+"1" #sera adicionado o stopbit aqui entao a = 000100011
    return ret


def codify_char(char): #exemplo 10001000 = a
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
    
    return "".join(result)[::-1] #retornara 00010001


def decode_fibonacci_zeckendorf(code):
    ret=""
    current_index = 0
    
    while current_index < len(code):
        end_index = code.find('11', current_index) #acha o index do primeiro 11
    
        if end_index == -1:
            return ret;
        end_index+=1 #compensa o index pra pegar o 1 faltante
        string_code = code[current_index:end_index]
        ret+=chr(decode_char(string_code))
        current_index=end_index+1 #compensa o index para pegar o proximo codigo

    return ret





def decode_char(code):
    code = code[::-1] #reverte o codigo para poder decodar ie. 00010001 vai virar 10001000
    result = 0
    fib = [0, 1]
    while len(fib) < len(code) + 2:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    for i in range(len(code)):
        if code[len(code) - 1 - i] == "1":
            result += fib[i + 2]
    return result

