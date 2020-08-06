import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt


x = sp.Symbol('x')
 
def pol_taylor(f,x0, grado_poliniomio):

    coeficientes = []

    for i in range(0,grado_poliniomio + 1):
        derivada= f.diff(x,i)
        coeficientes += [derivada.subs(x,x0)]


    potencias = [1]

    for i in range(1,grado_poliniomio+1):
        potencias += [(x-x0)**i] 

    polinomio = 0 


    for i in range(0, grado_poliniomio+1):
        polinomio = polinomio + (coeficientes[i] * potencias[i])/(math.factorial(i)) 
    return(polinomio)

print()

f = sp.cos(x) #Introducimos la función a desarrollar en serie
x0 = float(input('Introduce el punto en el que se quiere realizar el desarollo: '))
grado_poliniomio = int(input('Introduce el grado del polinomio a desarrollar: '))

polin_taylor = pol_taylor(f,x0,grado_poliniomio)
print()
print(polin_taylor)
print()

#Ahora vamos a evaluar el polonomio en un intervalo [a,b] con una exactitud indicada
print('Vamos a graficar el polinomio obtendido en un intervalo [a,b]')
print('Ten en cuenta que en dicho intervalo es mejor que no exista ninguna discontinuidad')
a = float(input('Introduce el inicio del intervalo: '))
b = float(input('Introduce el final del intervalo: '))
exactitud = int(input('Introduce la exactitud deseada: '))
z = np.linspace(a ,b , exactitud)

valores_polinomio = []
valores_funcion = []

for i in z:
    valores_polinomio += [polin_taylor.subs(x,i)]
    valores_funcion += [f.subs(x,i)]

plt.grid()
plt.plot(z, valores_polinomio)
plt.plot(z, valores_funcion,'-')
plt.show()