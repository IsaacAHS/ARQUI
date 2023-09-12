import numpy as np
import ctypes
import time 
import matplotlib.pyplot as plt

def moda_py(array,N):
    contador_global=0
    for i in range(N):
        contador_interno=0
        for j in range(N):
            if array[j]== array[i]:
                contador_interno =contador_interno+1
        if (contador_interno>contador_global):
            contador_global=contador_interno
            valor_retorno= array[i]
    return valor_retorno                

if __name__ == '__main__':
    
    lib = ctypes.CDLL('./lib_moda.so')
    lib.moda_c.argtypes = [np.ctypeslib.ndpointer(dtype= np.int8)]
    lib.moda_c.restype = ctypes.c_byte
    
    iteraciones= 100
    N=1024
    time_python=[]
    time_c=[]
    
    for _ in range(iteraciones):
        
        array_lista = np.random.randint(0,10,N,dtype=np.int8)
        array_lista_c= np.copy(array_lista)
        t1= time.perf_counter()
        m_py= moda_py(array_lista,N)
        t2= time.perf_counter()
        c_py= lib.moda_c(array_lista_c,N) 
        t3= time.perf_counter()
        time_python.append(t2-t1)
        time_c.append(t3-t2)
    
    plt.plot(time_python, 'r')
    plt.plot(time_c, 'b')
    plt.xlabel('íteraciones')
    plt.ylabel('segundos')
    plt.legend(('python','c'))
    plt.grid()
    plt.savefig('tiempo moda 1024.png', dpi=300)
        