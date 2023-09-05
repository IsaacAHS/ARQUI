# Euler
import numpy as np
def euler (x):
    return pow((1+1/x),x)
if __name__ == '__main__':
    N = 100000
    lista_numeros = np.zeros(N)
    for x in range(1,N):
        lista_numeros[x] = (euler(x))
    print(lista_numeros)