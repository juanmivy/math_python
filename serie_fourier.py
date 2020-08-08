import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import integrate
from sympy import cos,sin,pi

#Vamos a representar del desarrollo de Fourier de una función en el intervalo [-pi,pi]

x = sp.Symbol('x')

#Vamos a introducir la función de la que queremos obtener su serie de Fourier en términos de la variable x

f = x

#Con el siguiente método calculamos los coeficientes de Fourier y obtenemos la serie

def serie_fourier(f, exactitud):
    a_0 = (1/(pi)) * integrate(f,(x,-pi,pi)) 
    serie =  a_0/2
    for i in range(1, exactitud+1):
        coeficiente_a = (1/(pi)) * integrate(f * cos(i*x) ,(x,-pi,pi))
        coeficiente_b = (1/(pi)) * integrate(f * sin(i*x) ,(x,-pi,pi))
        serie = serie + coeficiente_a * cos(i *x) + coeficiente_b * sin(i*x) 
    print('La serie de Fourier de la función introducida es: ',serie)
    print()
    return(serie)
print()
exactitud = int(input("Introcude el natural donde quieres truncar la serie: "))
print()

#Para representar la graficas tomamos el intervalo [-pi,pi] con 1000 nodos equiespaciados
z = np.linspace(-math.pi,math.pi,1000)

#Declaramos dos vectores vacíos en los que vamos a ir introduciendo los valores de la serie de Fourier y los valores de la función
valores=[]
valores_reales = []
mi_serie = serie_fourier(f,exactitud)

for i in z:
    valores += [mi_serie.subs(x,i)]
    valores_reales += [f.subs(x,i)] 

#Finalmente representamos las gráficas

plt.grid()
plt.plot(z, valores, label = "Serie de Fourier")
plt.plot(z, valores_reales, label = "Funcion")
plt.legend(loc=4)   
plt.show()
    

