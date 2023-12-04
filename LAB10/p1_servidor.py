import socket
SOCK_BUFFER=1024

def factorial(numero):
    prod=1
    for i in range(1, numero+1):
        prod*=i
    return prod

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addres= ('localhost', 6759)
    
    print(f"Iniciando servidor en : {server_addres[0]}:{server_addres[1]}")
    
    sock.bind(server_addres)
    
    sock.listen(1)
    
    while True:
        print("Esperando conexiones ...")
        
        conn, cliente_address= sock.accept()
        
        print(f"Conexion desde {cliente_address[0]}:{cliente_address[1]}")
        
        data= conn.recv(SOCK_BUFFER)
        n= int(data.decode('utf-8'))
        resultado= factorial(n)
        
        conn.sendall(str(resultado).encode('utf-8'))
        conn.close()
        print("Fin de la conexion GAA")