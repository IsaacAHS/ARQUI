import asyncio
import aiofiles
import matplotlib.pyplot as plt
import time

lista_N = [2**i for i in range(10,20)]
tiempos_sync = []
tiempos_async = []


def generar_archivos(M,N):
    for i in range(M):
        with open(f"./ORIGINAL/archivo{i+1}.txt","w") as f:
            f.write("d"*N)
            
#generar_archivos(3,1024)    

def copia_sincronica(M,N):
    for i in range(M):
        with open(f"./ORIGINAL/archivo{i+1}.txt","r") as f_origen:  
            contenido= f_origen.read()
        with open(f"./COPIA/archivo{i+1}","w") as f_copia:
            f_copia.write(contenido)
            
#copia_sincronica(3,1024)


async def copia_asincronica(M,N):
    for i in range(M):
        async with aiofiles.open(f"./ORIGINAL/archivo{i+1}.txt","r") as f_ori:
            archivos= await f_ori.read()
        async with aiofiles.open(f"./COPIA2/archivo{i+1}.txt", "w") as f_copi:
            await f_copi.write(archivos)
            
#asyncio.run(copia_asincronica(3,1024))
            
            
if __name__=='__main__':
    for N in lista_N:
        t1= time.perf_counter()
        copia_sincronica(3,N)
        t2= time.perf_counter()
        tiempos_sync.append(t2-t1)
        
        t3=time.perf_counter()
        asyncio.run(copia_asincronica(3,N))
        t4= time.perf_counter()
        tiempos_async.append(t4-t3)
    
    plt.plot(lista_N, tiempos_sync)
    plt.plot(lista_N, tiempos_async)
    plt.xlabel('File size [bytes]')
    plt.ylabel('Copy time[ms]')
    plt.legend(['Sync', 'Async'])
    plt.savefig('SizeVsTime.png')
    plt.cla()
        
        
                    
                   
