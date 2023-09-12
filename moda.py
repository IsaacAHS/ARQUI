import numpy as np
import ctypes
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
    
    
    array_lista = [2,2,1,1,3,3,3,3,3,4,4,4,2]
    
    array_np= np.asarray(array_lista).astype(np.int8)
    array_c= np.asarray(array_lista).astype(np.int8)
    print(moda_py(array_np,len(array_np)))
    print(lib.moda_c(array_c,len(array_c)))
    
