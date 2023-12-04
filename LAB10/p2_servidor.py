import random
import socket

SOCK_BUFFER=1024

dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

def funcion_carac(letra_recv, palabra_escogida, palabra_oculta):
    for i in range(0, len(palabra_escogida)):
        if palabra_escogida[i]== letra_recv:
            palabra_oculta= palabra_oculta[:i]+letra_recv+palabra_oculta[i+1:]
    return palabra_oculta

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address= ('localhost', 8546)
    sock.bind(server_address)
    sock.listen(1)
    
    while True:
        print("Esperando conexiones ...")
        conn, client_address= sock.accept()
        print(f"Conexion desde {client_address[0]}:{client_address[1]}")
        
        try:
            palabra= conn.recv(SOCK_BUFFER).decode('utf-8')
            
            if palabra=='start':
                print(f"Recibi comandando {palabra}")
                
                palabra_escogida= random.choice(dictionary)
                print(f"La palabra escogida es: {palabra_escogida}")
                
                palabra_oculta= '*'*len(palabra_escogida)
                
                conn.send(palabra_oculta.encode('utf-8'))
                
                num_intentos= 5
                while num_intentos>0:
                    data_recv_char= conn.recv(SOCK_BUFFER)
                    
                    if data_recv_char:
                        letra_recv= data_recv_char.decode('utf-8')
                        print(f"Client guess: {letra_recv}")
                        if letra_recv in palabra_escogida:
                            palabra_oculta_nueva= funcion_carac(letra_recv,palabra_escogida,palabra_oculta)
                            if palabra_oculta== palabra_escogida:
                                conn.send("Ganaste". encode('utf-8'))
                                break
                            else:
                                conn.send(palabra_oculta_nueva.encode('utf-8'))
                                
                        else:
                            print(f"Intento incorrecto")
                            conn.send(palabra_oculta.encode('utf-8'))
                            num_intentos-=1
            elif palabra == 'stop':
                print("Se acabo el juego.")
                break
            else:
                conn.send("Escribe start para jugar".encode('utf-8'))
        except:
            print("Se cerro el juego abruptamente")
        finally:
            print("Termino el juego. Escribe start para jugar")
            
            
            
            
            
            
            
            

            
