import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

def calcular_histograma(filename_npy):
    imagen = np.load(filename_npy)
    
    M= len(imagen)
    N= len(imagen[0])
    
    histograma= np.zeros(256, dtype=int)
    
    for i in range(M):
        for j in range(N):
            pixeles= imagen[i][j]
            histograma[pixeles]+=1
    
    return histograma

def graficar_histograma(histograma_lista, filename, color):
    plt.plot(range(0,len(histograma_lista)), histograma_lista, color=color)
    plt.savefig(filename,bbox_inches='tight')
    plt.close()
    
def calcular_y_graficar_histogramas(filename_npy):
    histograma= calcular_histograma(filename_npy)
    graficar_histograma(histograma, filename_npy.replace('.npy','.png'), 'green')
    
if __name__=='__main__':
    
    imagenes= ['goldhill_x2.npy', 'hong kong_x2.npy', 'lena_x2.npy', 'stonehenge_x2.npy']
    imagenes2= ['goldhill.npy', 'hong kong.npy', 'lena.npy', 'stonehenge.npy']
    
    #Parte a
    t_inicio_a= time.perf_counter()
    for imagen in imagenes:
        calcular_y_graficar_histogramas(imagen)
    t_fin_a= time.perf_counter()
    print(f"Tiempo total en serie: {t_fin_a-t_inicio_a}")
    
    #Parte b
    t_inicio_b= time.perf_counter()
    with Pool(processes=4) as p:
        p.map(calcular_y_graficar_histogramas, imagenes)
    t_fin_b=time.perf_counter()
    print(f"Tiempo de ejecucion en paralelo: {t_fin_b-t_inicio_b}")
    
    #SpeedUp imagenes sufijo _x2
    speedup1= (t_fin_a-t_inicio_a)/(t_fin_b-t_inicio_b)
    
    ##################################################################################
    #Parte C (imagenes sin sufijo x2)
    #Serial
    t_ini_ser= time.perf_counter()
    for imagen in imagenes2:
        calcular_y_graficar_histogramas(imagen)
    t_fin_ser= time.perf_counter()
    print(f"Tiempo total en serie imagenes sin sufijo _x2: {t_fin_ser-t_ini_ser}")
    
    #Procesos
    t_ini_para= time.perf_counter()
    with Pool(processes=4) as p:
        p.map(calcular_y_graficar_histogramas, imagenes2)
    t_fin_para=time.perf_counter()
    print(f"Tiempo de ejecucion en paralelo imagenes sin sufijo _x2: {t_fin_para-t_ini_para}")
    
    #SpeedUp imagenes sufijo _x2
    speedup2= (t_fin_ser-t_ini_ser)/(t_fin_para-t_ini_para)
    
    print(f"El Speedup para las imagenes con sufijo _x2 fue: {speedup1}")
    print(f"El Speedup para las imagenes sin sufijo _x2 fue: {speedup2}")
            