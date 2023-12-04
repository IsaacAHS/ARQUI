import time

if __name__=='__main__':
    puntaje_inicial='0'

    with open("players.csv","r") as f:
            jugadores=f.read()
    lista_jugadores=jugadores.split("\n")
    lista_jugadores=lista_jugadores[1:]

    p1=lista_jugadores[0].split(';')
    p1.append(puntaje_inicial)

    print(p1[0])