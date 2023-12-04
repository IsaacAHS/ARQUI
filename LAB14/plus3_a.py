import time
import random

def calcular_pi(muestras):
    contador=0
    for i in range(muestras):
        x= random.uniform(-1,1)
        y= random.uniform(-1,1)
        if x**2+y**2<=1:
            contador= contador+1
    
    return (contador/muestras)*4

if __name__=='__main__':
    muestras= 10_000_000
    inicio= time.perf_counter()
    resultado= calcular_pi(muestras)
    fin= time.perf_counter()
    
    print(f"El valor de pi es: {resultado}")
    print(f"EL tiempo que le tomo fue: {fin-inicio} segundos")