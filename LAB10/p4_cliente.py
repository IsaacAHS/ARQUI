import socket

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address= ('localhost', 8758)
    
    sock.connect(server_address)
    
    respuesta= input("Enter your request (a,b or c): ")
    sock.send(respuesta.encode('utf-8'))
    
    data= sock.recv(1024).decode('utf-8')
    
    with open('base_datos','w') as file:
        file.write(respuesta +','+ data + '\n')
        
    print(f"El resultado es {data}")
    
    
    