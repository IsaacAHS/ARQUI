import socket
import numpy as np

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address= ('localhost', 8721)
    
    sock.bind(server_address)
    sock.listen(1)
    
    while True:
        print("Esperando conexiones ...")
        conn, client_address= sock.accept()
        
        print(f"Conexion desde {client_address} lista.")
        
        notas= conn.recv(1024).decode('utf-8').split(',')
        notas= [float(nota) for nota in notas if nota.strip() != '']
        
        practicas = notas[:4]
        laboratorios = notas[4:14]
        tarea_academica = notas[14]

        practicas.remove(min(practicas))
        laboratorios.remove(min(laboratorios))
        laboratorios.remove(min(laboratorios))

        Pa = np.mean(practicas)
        Pb = np.mean(laboratorios)
        Ta = tarea_academica

        NF = (3*Pa + 3*Pb + 4*Ta) / 10
        conn.send(str(NF).encode('utf-8'))

        conn.close()
    