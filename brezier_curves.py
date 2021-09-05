#Programilla que grafica la curva de Bezier asociada a unos puntos


import matplotlib.pyplot as plt 
import numpy as np
from math import factorial
import sympy

# Antes de nada implementamos una clase para trabajar con puntos:

class punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
       return "("+ str(self.x)+","+str(self.y)+")"

    def __add__(self, v):
        return punto(self.x + v.x, self.y + v.y)

    def __mul__(self, v):
        return punto(self.x * v , self.y * v)

#Implementamos una función para introducir los puntos que deseemos

def intro_puntos():

    puntos =[]

    continuar = True

    puntos= []

    while continuar == True:
        intro_x = input("Introduce la primera coordenada del punto: ")
        intro_y = input("Introduce la segunda coordenada del punto: ")
        puntos += [punto(float(intro_x),float(intro_y))]

        decision = input("¿Desea continuar introduciendo puntos? (y/n): ")

        if decision == "n":
            continuar = False
    return puntos


puntos = intro_puntos()

#Una vez estan los puntos introducidos vamos a calcular los puntos de la curva de Bezier
#Por comodidad he utilizado calculo simbolico pero creo que se podría hacer perfectamente sin esto

num_puntos =len(puntos)

x = []
y = []

for i in puntos:
    x += [i.x]
    y += [i.y] 

coef = []

polinomio = ""

for i in range(0,len(x)):
    coef  += [factorial(len(x)-1)/(factorial(i)*factorial(len(x)-1-i))]

lista_mul = [a*b for a,b in zip(puntos,coef)]

polinomio_lista = []

t = sympy.Symbol('t')

for i in range(0,len(lista_mul)):
    polinomio_lista += [lista_mul[i]*(1- t)**(num_puntos-1-i) * t ** i]

polinomio = punto(0,0)

for i in polinomio_lista:
    polinomio += i



f = polinomio.x
g = polinomio.y 

print("El polinomio de Bézier asociado a los puntos introducidos es: ")
print(f,g)

x_curva =[]
y_curva =[]

t_int = np.linspace(0,1,50)

for i in t_int:
   x_curva += [f.subs(t,i)]
   y_curva += [g.subs(t,i)]


plt.scatter(x,y)
plt.plot(x, y, linewidth=0.5)
plt.plot(x_curva, y_curva, linewidth=2)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")




plt.title("Bézier Curve")
plt.show()
