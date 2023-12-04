import socket
SOCK_BUFFER=1024

if __name__== '__main__':
    
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address= ('localhost', 8546)
    
    print(f"Conectado al servidor:{server_address[0]}:{server_address[1]}")
    
    sock.connect(server_address)
    
    while True:
        cmd= input("Tipee lo que quiere enviar: ")
        if cmd == 'start':
            sock.send(b'start')
            palabra_recibida= sock.recv(SOCK_BUFFER)
            print(f"Mensaje recibido: {palabra_recibida}")
            print("Tienes 5 oportunidades")
        elif cmd=='stop':
            print("Desconectando del servidor. Terminamos el juego")
            sock.close()
            break
        else:
            sock.send(cmd.encode())
            palabra_recibida= sock.recv(1024)
            print(f"Mensaje Recibido: {palabra_recibida}")
        