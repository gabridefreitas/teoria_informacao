import math
from math import log
 
def codificar_elias_gamma(x):
    log2 = lambda x: log(x, 2)
 
    def Unary(x):
        return (x - 1) * '0' + '1'
   
    def Binary(x, l=1):
        s = '{0:0%db}' % l
        return s.format(x)
     
    if x == 0:  
        return '0'
 
    n = 1 + int(log2(x))
    b = x - 2**(int(log2(x)))
    l = int(log2(x))
 
    return Unary(n) + Binary(b, l)
 
def decodificar_elias_gamma(x):
    x = list(x)
    K = 0
    while True:
        if not x[K] == '0':
            break
        K = K + 1
     
    x = x[K:2*K+1]
 
    n = 0
    x.reverse()
     
    for i in range(len(x)):
        if x[i] == '1':
            n = n+math.pow(2, i)
    return int(n)
