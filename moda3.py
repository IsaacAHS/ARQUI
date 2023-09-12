import numpy as np
import ctypes
import time
import matplotlib.pyplot as plt
import statistics


def moda_python(array, N):
    contador_global = 0
    for i in range(N):
        contador_interno = 0
        for j in range(N):
            if array[j]==array[i]:
                contador_interno = contador_interno+1
        if (contador_interno>contador_global):
            contador_global = contador_interno
            valor_retorno = array[i]
    return valor_retorno

if __name__ == '__main__':

    lib = ctypes.CDLL('./lib_moda.so')
    lib.moda_c.argtypes = [np.ctypeslib.ndpointer(dtype = np.int64), ctypes.c_int]
    lib.moda_c.restype = ctypes.c_longlong

    iteraciones = 200
    lista_t1 = []
    lista_t2 = []
    N_lista = [256,512,1024,2048,4096]
    for n in N_lista:
        time_python = []
        time_c = []
        for _ in range(iteraciones):
            array_lista = np.random.randint(0,10, n,dtype=np.int64)
            array_lista_c = np.copy(array_lista)
            t1 = time.perf_counter()
            m_py = moda_python(array_lista,n)
            t2 = time.perf_counter()
            c_py = lib.moda_c(array_lista_c,n)
            t3 = time.perf_counter()
            time_python.append(t2-t1)
            time_c.append(t3-t2)
        lista_t1.append(statistics.median(time_python))
        lista_t2.append(statistics.median(time_c))

    # plt.plot(time_python,'r')
    # plt.plot(time_c,'b')
    # plt.xlabel('Iteraciones')
    # plt.ylabel('segundos')
    # plt.legend({'Python','C'})
    # plt.grid()
    # plt.savefig('Tiempo_moda_1024_int64.png', dpi = 300)

    plt.plot(N_lista, lista_t1,'r')
    plt.plot(N_lista, lista_t2, 'b')
    plt.xlabel('Iteraciones')
    plt.ylabel('segundos')
    plt.legend({'Python','C'})
    plt.grid()
    plt.savefig('Tiempo_moda_N_int64.png', dpi = 300)