import socket

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address= ('localhost', 8721)
    
    sock.connect(server_address)
    
    with open('notas2.csv','r') as file:
        
        notas= file.readline().strip().split(',')
    sock.send(','.join(notas).encode('utf-8'))
    
    data= sock.recv(1024).decode('utf-8')
    print(f"El promedio final es {data}")
    
    sock.close()
    
        
        
    
    