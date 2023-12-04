import time
import requests
from concurrent.futures import ThreadPoolExecutor

urls = [
"https://www.wikipedia.org/",
"https://www.nytimes.com/",
"https://www.bbc.com/",
"https://www.python.org/",
"https://www.reddit.com/",
"https://www.instagram.com/",
"https://www.twitter.com/",
"https://www.cnn.com/",
"https://www.github.com/",
"https://www.spotify.com/",
]

#Item a) descarga secuencial
def descarga(url,i)-> bool:
    response =requests.get(url)
    
    if response.status_code ==200:
        with open(f'pagina{i}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
 
    
if __name__=="__main__":
    
    lista1=[]
    lista2=[]
    #Calculamos el tiempo de la descarga secuencial
    inicio_a= time.perf_counter()
    
    for i, url in enumerate(urls, 1):
        descarga(url,i)
    fin_a= time.perf_counter()
    print(f"El tiempo de descarga secuencial es: {fin_a-inicio_a} segundos ")    
    
    
    #Calculamos el tiempo de descarga con ThreadPool
    workers= 3
    inicio_b=time.perf_counter()
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i,url in enumerate(urls,1):
            executor.submit(descarga,url,i)
            
    fin_b=time.perf_counter()
    
    print(f"El tiempo de descarga con ThreadPool es: {fin_b-inicio_b} segundos ") 
    
    
    #Speed Up
    SpeedUp= (fin_a-inicio_a)/(fin_b-inicio_b)
    print(f"El SpeedUp es: {SpeedUp}")