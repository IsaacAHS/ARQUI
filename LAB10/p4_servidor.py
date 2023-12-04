import socket

def calcular_promedio_edades(data):
    total_edad = sum(int(row[1]) for row in data)
    return total_edad/len(data)

def contar_pacientes_enfermos(data):
    return sum(1 for row in data if row[2]=='1')

def contar_pacientes_sanos(data):
    return sum(1 for row in data if row[2]=='0')

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address= ('localhost',8758)
    
    sock.bind(server_address)
    sock.listen(1)
    
    with open('base_datos.csv', 'r') as f:
        data= [line.strip().split(',') for line in f][1:]
        while True:
            print("Esperando conexiones ...")
            conn, client_address= sock.accept()
            print(f"Establenciendo conexion {client_address}. Lista")
            
            respuesta= conn.recv(1024).decode('utf-8')
            
            if respuesta =='a':
                prom= calcular_promedio_edades(data)
                conn.send(str(prom).encode('utf-8'))
            elif respuesta=='b':
                num_sick= contar_pacientes_enfermos(data)
                conn.send(str(num_sick).encode('utf-8'))
            elif respuesta=='c':
                num_healthy= contar_pacientes_sanos(data)
                conn.send(str(num_healthy).encode('utf-8'))
                
            conn.close()
                
    
    