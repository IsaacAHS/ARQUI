# Euler
import numpy as np
import time
import statistics
import matplotlib.pyplot as plt
import ctypes

def euler (x):
    return pow((1+1/x),x)

if __name__ == '__main__':
    N = 10000
    lib = ctypes.CDLL('./lib_euler.so')
    lib.euler.argtypes = [ctypes.c_int]
    lib.euler.restype = ctypes.c_double
    iteraciones = 100
    time_python = []
    time_c = []
    for _ in range(iteraciones):
        tic2 = time.perf_counter()
        lib.euler(N)
        toc2 = time.perf_counter()
        time_c.append(1e6*(toc2-tic2))
        #print("Tiempo Pow en C",toc2-tic2)

        tic1 = time.perf_counter()
        euler(N)
        toc1 = time.perf_counter()
        time_python.append(1e6*(toc1-tic1))
        #print("Tiempo pow Python",toc1-tic1)


    plt.plot(time_python)
    plt.plot(time_c)
    plt.grid()
    plt.legend(["Time Python", "Time C"])
    plt.xlabel("Iteraciones")
    plt.ylabel("Tiempo [us]")
    plt.savefig("Euler_comparacion2.png")
    plt.close()
    