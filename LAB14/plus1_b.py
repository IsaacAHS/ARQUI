from werkzeug.security import check_password_hash
import time
from multiprocessing import Pool


contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'
vocales = ['a','e','i','o','u']
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

def funcion(vocal1):
    for vocal1 in vocales:
        for vocal2 in vocales:
            for letra in abecedario:
                password= vocal1+vocal2+letra
                validacion= comparar_con_password_correcto(password)
                if validacion:
                    return password 
                
if __name__=='__main__':
    Process= 5    
    t1= time.perf_counter()
    with Pool(processes=Process) as p:
        resultados= p.map(funcion, vocales)
    t2= time.perf_counter() 
    contra= next((r for r in resultados if r is not None), None)
    print(f"la palabra buscada es :{contra}") 
    print(f"EL tiempo que le tomo fue: {t2-t1} segudnos")
    