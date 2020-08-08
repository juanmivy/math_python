import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import integrate
from sympy import cos,sin,pi

#Vamos a representar del desarrollo de Fourier de una función signo en el intervalo [-pi,pi], ya que esta presenta un salto en el origen

x = sp.Symbol('x')

#Esta es la mejor forma que he probado para introducir la funcion salto
f = x-x-1
g = x-x+1
#Tambien es interesante probar con f = x+math.pi    g = math.pi-x 

#Vamos a introducir donde se encuantra la singularidad, en nuestro caso en cero
x0 = float(input('Introduce el punto de [-pi, pi] donde se encuentra la singularidad: ' ))

def serie_fourier(exactitud):
    a_0 = (1/(pi)) * (integrate(f,(x,-pi,x0))+ integrate(g,(x,x0,pi)))
    serie =  a_0/2
    for i in range(1, exactitud+1):
        coeficiente_a = (1/(pi)) * (integrate(f * cos(i*x) ,(x,-pi,x0))+integrate(g * cos(i*x) ,(x,x0,pi)))
        coeficiente_b = (1/(pi)) * (integrate(f * sin(i*x) ,(x,-pi,x0))+integrate(g * sin(i*x) ,(x,x0,pi)))
        serie = serie + coeficiente_a * cos(i *x) + coeficiente_b * sin(i*x) 
    print('La serie de Fourier de la función introducida es: ',serie)
    print()
    return(serie)

#Vamos a introducir donde queremos truncar la serie
exactitud = int(input("Introcude el natural donde quieres truncar la serie: "))

#Ahora le damos valores a la función y graficamos
z = np.linspace(-math.pi, math.pi, 1000)
valores=[]
valores_reales = []
mi_serie = serie_fourier(exactitud)

for i in z:
    valores += [mi_serie.subs(x,i)]
    if (i<=x0):
        valores_reales += [f.subs(x,i)]
    else:
        valores_reales += [g.subs(x,i)]

plt.grid()
plt.plot(z, valores, label = "Serie de Fourier")
plt.plot(z, valores_reales, label = "Funcion")
plt.legend(loc=4)   
plt.show()
    

