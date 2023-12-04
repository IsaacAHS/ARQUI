import time
import numpy as np
import random

with open("players.csv","r") as f:
    contenido= f.read()

lista_jugadores= contenido.split("\n")
lista_jugadores= lista_jugadores[1:]
print(f"{lista_jugadores}")

p1= lista_jugadores[0].split(";")
p1.append('0')
magnus= np.array(p1[1:]).astype(int)
print(f"p1{p1}")
print(f"acasas{magnus}")

#5 rondas
ronda()