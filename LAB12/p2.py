
from threading import Thread
from urllib.request import urlopen
import time

#Zfill-> numero de "n" digitos
urls= [f'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{str(i).zfill(2)}.png' for i in range(1,30)]

#funcion para descargar una imagen
def descargar_imagen(url):
    with urlopen(url) as u:
        image_data= u.read()
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(image_data)
            
if __name__=='__main__':
    inicio= time.perf_counter()
    for url in urls:
        descargar_imagen(url)
    
    fin= time.perf_counter()
    print(f"Descarga secuencial: {fin-inicio} segundos")
    
    
    lista_hilo=[]
    t1=time.perf_counter()
    for url in urls:
        t= Thread(target=descargar_imagen, args=(url,))
        t.start()
        lista_hilo.append(t)
    for t in lista_hilo:
        t.join()
        
    t2=time.perf_counter()
    print(f"Descarga con hilos: {t2-t1} segundos")
    
    
    lista_3hilos=[]
    t3=time.perf_counter()
    for i in range(0,len(urls),3):
        
        for url in urls[i:i+3]:
            tg3= Thread(target=descargar_imagen, args=(url,))
            tg3.start()
            lista_hilo.append(tg3)
        for tg3 in lista_hilo:
            tg3.join()
        
    t4=time.perf_counter()
    print(f"Descarga con 3 hilos: {t4-t3} segundos")
    