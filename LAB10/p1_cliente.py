import socket

SOCK_BUFFER=1024

if __name__=='__main__':
    
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address= ('localhost', 6759)
    
    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    
    sock.connect(server_address)
    
    try:
        n= input("Ingrese el numero: ")
        
        sock.sendall(str(n).encode('utf-8'))
        
        factorial= sock.recv(SOCK_BUFFER).decode('utf-8')
        
        print(f"El factorial de {n} es {factorial}")
    finally:
        sock.close()
        print("Fin de la conexion")     