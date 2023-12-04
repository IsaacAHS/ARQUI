import time
import random
from multiprocessing import Pool

def calcular_pi(muestras):
    contador=0
    for i in range(muestras):
        x= random.uniform(-1,1)
        y= random.uniform(-1,1)
        if x**2+y**2<=1:
            contador= contador+1
    
    return contador

if __name__=='__main__':
    muestras= 10_000_000
    procesos= 4
    muestras_por_proceso= muestras//procesos
    inicio= time.perf_counter()
    
    with Pool(processes=procesos) as p:
        contadores= p.map(calcular_pi, [muestras_por_proceso]*procesos)
        
    contador_total= sum(contadores)
    resultado= (contador_total/muestras)*4
    fin= time.perf_counter()
    
    print(f"El valor de pi es: {resultado}")
    print(f"EL tiempo que le tomo fue: {fin-inicio} segundos")