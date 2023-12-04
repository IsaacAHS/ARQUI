import socket
from threading import Thread

SOCK_BUFFER =1024
stock = [5,3,2,4]

def cliente_handler(cliente):
    while True:
        producto = cliente.recv(SOCK_BUFFER).decode('utf-8')
        
        if producto=='lavadora':
            if stock[0] ==0:
                mensaje='0'
            else:
                stock[0]-=1
                mensaje='1'
            cliente.send(mensaje.encode('utf-8'))
        if producto=='refrigerador':
            if stock[1] ==0:
                mensaje='0'
            else:
                stock[1]-=1
                mensaje='1'
            cliente.send(mensaje.encode('utf-8'))
        if producto=='aspiradora':
            if stock[2] ==0:
                mensaje='0'
            else:
                stock[2]-=1
                mensaje='1'
            cliente.send(mensaje.encode('utf-8'))
        if producto=='licuadora':
            if stock[3] ==0:
                mensaje='0'
            else:
                stock[3]-=1
                mensaje='1'
            cliente.send(mensaje.encode('utf-8'))

if __name__=='__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 4756)
    
    sock.bind(server_address)
    
    sock.listen(1)
    
    while True:
        print("Esperando conexiones")
        connection, direccion= sock.accept()
        t= Thread(target= cliente_handler, args=(connection,))
        
        t.start()