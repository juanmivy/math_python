#Importante que polinomios y geometria2d esten en el mismo directorio para acceder a las clases

from polinomios import Polinomio
from geometria2d import Punto
import numpy as np

def get_puntos():
    seguir = True
    datos = []
    while seguir:
        eje_x =  float(input('Introduce el valor de abcisas: '))
        eje_y =  float(input('Introduce el valor de ordenadas: '))
        datos += [Punto(eje_x, eje_y)]
        letra = input('Va a introducir más datos?? (s/n)  ')
        if letra == 'n':
            seguir = False
    
    return datos 

def interpolador(datos):
    #En b vamos a almacenar el valor de las ordenadas
    b=[]
    for i in range(0, len(datos)):
        b += [datos[i].y]
    matriz = []
    for i in range(0, len(datos)):
        vector = []
        for j in range(0, len(datos)):
            vector += [datos[i].x**j]
        matriz += vector

    #Pasamos las listas a arrays para luego resolver el sistema con numpy   
    b = np.asarray(b)
    matriz = np.asarray(matriz)
    matriz = matriz.reshape(len(datos),len(datos))
    solucion = np.linalg.solve(matriz, b) 
    solucion = solucion.tolist()
    return(Polinomio(solucion))

datos = get_puntos()
print()
print('El polinomio interpolador para los datos introducidos es: ',interpolador(datos))

valores_x = []
for i in range(0, len(datos)):
    valores_x += [datos[i].x]
valores_x = sorted(valores_x)
#Ahora graficamos el polinomio
interpolador(datos).grafica(valores_x[0], valores_x[-1])

