import asyncio
import aiofiles
import random
import numpy as np
import time

async def partida(p1,p2):
    if p1[0]>p2[0]:
        p1[1]+=1
    else:
        p2[1]+=1
    await asyncio.sleep(0.15)

async def ronda(p1,p2,p3,p4,p5,p6):
    await asyncio.gather(partida(p1,p2),partida(p3,p4),partida(p5,p6))

async def fase_rondas_async():
    puntaje_inicial='0'

    async with aiofiles.open("players.csv","r") as f:
        jugadores=await f.read()
    lista_jugadores=jugadores.split("\n")
    lista_jugadores=lista_jugadores[1:]

    p1=lista_jugadores[0].split(';')
    p1.append(puntaje_inicial)
    magnus=np.array(p1[1:]).astype(int)

    p2=lista_jugadores[1].split(';')
    p2.append(puntaje_inicial)
    vladimir=np.array(p2[1:]).astype(int)

    p3=lista_jugadores[2].split(';')
    p3.append(puntaje_inicial)
    peter=np.array(p3[1:]).astype(int)

    p4=lista_jugadores[3].split(';')
    p4.append(puntaje_inicial)
    levon=np.array(p4[1:]).astype(int)

    p5=lista_jugadores[4].split(';')
    p5.append(puntaje_inicial)
    boris=np.array(p5[1:]).astype(int)

    p6=lista_jugadores[5].split(';')
    p6.append(puntaje_inicial)
    alexander=np.array(p6[1:]).astype(int)

    await asyncio.gather(
        ronda(levon,magnus,boris,alexander,peter,vladimir),
        ronda(magnus,vladimir,alexander,peter,levon,boris),
        ronda(boris,magnus,peter,levon,vladimir,alexander),
        ronda(magnus,alexander,levon,vladimir,boris,peter),
        ronda(peter,magnus,vladimir,boris,alexander,levon))

    puntajes=np.array([levon[1],magnus[1],boris[1],alexander[1],peter[1],vladimir[1]])
    max = puntajes[0]
    for x in puntajes:
        if x > max:
            max = x
    
    if max==levon[1]:
        ganador="levon"
    elif max==magnus[1]:
        ganador="magnus"
    elif max==boris[1]:
        ganador="boris"
    elif max==alexander[1]:
        ganador="alexander"
    elif max==peter[1]:
        ganador="peter"
    else:
        ganador="vladimir"

    return ganador

async def fase_final(ganador_ronda,ganador_pasado):
    p1_inicial=0
    p2_inicial=0
    empate="empate"
    for _ in range(12):
        resultado=random.choice([1,0.5,0])
        if resultado==1:
            p1_inicial+=1
        elif resultado==0.5:
            p1_inicial+=0.5
            p2_inicial+=0.5
        else:
            p2_inicial+=1
    
    if p1_inicial>p2_inicial:
        return ganador_ronda
    elif p1_inicial<p2_inicial:
        return ganador_pasado
    else:
        return empate
    
async def main():
    ganador_ronda=await fase_rondas_async()
    ganador_pasado="anand"

    winner=await fase_final(ganador_ronda,ganador_pasado)
    print(f"ganador:{winner}")   
if __name__=='__main__':
    inicio=time.perf_counter()
    asyncio.run(main())
    fin=time.perf_counter()
    print(f"tiempo de ejecucion: {fin-inicio}")
    


