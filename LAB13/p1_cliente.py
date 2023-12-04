import socket
SOCK_BUFFER= 1024

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address= ('localhost', 4756)
    
    sock.connect(server_address)
    while True: 
        producto = input("Ingrese el nombre del producto:")
        sock.send(producto.encode('utf-8'))
        respuesta= sock.recv(SOCK_BUFFER).decode('utf-8')
        
        if respuesta=='1':
            print("Producto en stock. Pedido Procesado")
        else:
            print("Producto agotado. Pedido no procesado")
            

    
    