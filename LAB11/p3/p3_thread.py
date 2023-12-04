import random
import numpy as np
import time
from threading import Thread
'''t1 = Thread(target=func1)'''
def partida(p1,p2):
    if p1[0]>p2[0]:
        p1[1]+=1
    else:
        p2[1]+=1
    time.sleep(0.15)

def ronda(p1,p2,p3,p4,p5,p6):
    t1= Thread(target=partida,args=(p1,p2))
    t2= Thread(target=partida,args=(p3,p4))
    t3= Thread(target=partida,args=(p5,p6))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

def fase_rondas_sync():
    puntaje_inicial='0'

    with open("players.csv","r") as f:
        jugadores=f.read()
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

    t_a= Thread(target=ronda,args=(levon,magnus,boris,alexander,peter,vladimir))
    t_b= Thread(target=ronda,args=(magnus,vladimir,alexander,peter,levon,boris))
    t_c= Thread(target=ronda,args=(boris,magnus,peter,levon,vladimir,alexander))
    t_d= Thread(target=ronda,args=(magnus,alexander,levon,vladimir,boris,peter))
    t_e= Thread(target=ronda,args=(peter,magnus,vladimir,boris,alexander,levon))
    t_a.start()
    t_b.start()
    t_c.start()
    t_d.start()
    t_e.start()
    t_a.join()
    t_b.join()
    t_c.join()
    t_d.join()
    t_e.join()

    puntajes=np.array([levon[1],magnus[1],boris[1],alexander[1],peter[1],vladimir[1]])
    max = puntajes[0];
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

def fase_final(ganador_ronda,ganador_pasado):
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
def main():
    ganador_ronda=fase_rondas_sync()
    ganador_pasado="anand"
    winner=fase_final(ganador_ronda,ganador_pasado)
    print(f"ganador:{winner}") 

if __name__=='__main__':
    inicio=time.perf_counter()
    main()
    fin=time.perf_counter()
    print(f"tiempo de ejecucion: {fin-inicio}")
    


