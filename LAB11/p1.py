import asyncio
import random
import aiofiles

#funcion asincrona "simulador" que recibe como arguemntos 
#el nombre de la tencología ya sea sms,3g o satelital
#y la funcion que me calculara la respectiva latencia
#Agregare el arguemnto adicional para el item b
async def simulador(tecnologia,funcion_latencia, nombre_archivo):
    latencia= funcion_latencia()
    await asyncio.sleep(latencia/1000)#simula la latencia de la tecnologia, se divide entre 1000 para que sean milisegundos
    print(f"La corrutina de la tecnología {tecnologia} tuvo una latencia de {latencia} ms.")
    
    async with aiofiles.open(nombre_archivo,"a") as f:
        await f.write(f"{latencia}\n")
    
#funcion que calcula la latencia de la tecnología Sms
def latencia_sms():
    tiempo_envio= random.randint(10,100)
    tiempo_recepcion= random.randint(10,100)
    return tiempo_envio+tiempo_recepcion

#funcion que calcula la latencia de la tecnología 3G
def latencia_3g():
    t_ida_vuelta= random.randint(100,300)
    tiempo_procesamiento= random.randint(10,100)
    return 2*(t_ida_vuelta+tiempo_procesamiento)

#funcion que calcula la latencia de la tecnología satelital
def latencia_satelital():
    tiempo_propagacion= random.randint(500,700)
    t_procesamiento= random.randint(10,100)
    return 2*tiempo_propagacion+t_procesamiento    


#par ala parte B , agrego el nombre que recibira el archivo a crear y donde se guardaran las latencias respectivas
#a las tecnologias
async def main():
    await asyncio.gather(simulador("SMS", latencia_sms, "latencias_sms.csv"),simulador("3G",latencia_3g,"latencias_3g.csv"),simulador("Satelital", latencia_satelital, "latencias_satelital.csv"))

if __name__=='__main__':
    asyncio.run(main())

#Para el item b, se desea generar archivos .txt en las que se guarde los tiempos de 
#latencia para cada tecnología, se podria modificar los argumentos de la funcion "simulador" agrgando el archivo que
#se generara desde la funcion "main" 