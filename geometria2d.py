import math
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar_segmento(self, q):
        valores_x = [self.x, self.y]
        valores_y = [q.x, q.y]
        plt.plot(valores_x, valores_y)
    
    def __str__(self):
        return('('+str(self.x)+','+str(self.y)+')')

    def a_vector(self, p):
        return Vector(p.x - self.x, p.y - self.y)

    #Sobrecargamos el operador menor que para poder ordenar los puntos y posteriormente hacer la triangulacion de la clase polinomio
    def __lt__(self, p):
        if (self.y < p.y ):
            if (self.x > p.x):
                return True
            else:
                return False
        else:
            return False
class Vector:
    def __init__(self, primera_componenente, segunda_componente):
        self.primera_componente = primera_componenente
        self.segunda_componente = segunda_componente

    def __str__(self):
        return('('+str(self.primera_componente)+','+str(self.segunda_componente)+')')

    #Sobrecargamos operadores para trabajar con los vectores
    def __add__(self, otro):
        return(Vector(self.primera_componente + otro.primera_componente, self.segunda_componente + otro.segunda_componente))

    def __sub__(self, otro):
        return(Vector(self.primera_componente - otro.primera_componente, self.segunda_componente - otro.segunda_componente))

    def __mul__(self, otro):
        if (type(otro) == int or type(otro) == float):
            return(Vector( otro * self.primera_componente, otro * self.segunda_componente )) 
        if type(otro) == Vector:
            return (self.primera_componente * otro.primera_componente + self.segunda_componente * otro.segunda_componente )
    
    def modulo(self):
        u = self.primera_componente**2 + self.segunda_componente**2
        return(math.sqrt(u))

    def perpendicular(self):
        return (Vector(-self.segunda_componente, self.primera_componente))


class Triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        resultado  = 'Triangulo de vertices: ' + str(self.p1)+ ', ' +str(self.p2)+ ' y '+ str(self.p3) 
        return resultado

    #Implementamos el area del triangulo con la formula de Herón
    def area(self): 
        lado_1 = self.p1.a_vector(self.p2)
        lado_2 = self.p1.a_vector(self.p3)
        lado_3 = self.p2.a_vector(self.p3)

        longitud_lado_1 = lado_1.modulo()
        longitud_lado_2 = lado_2.modulo()
        longitud_lado_3 = lado_3.modulo()

        semiperimetro = (longitud_lado_1+longitud_lado_2+longitud_lado_3)/(2)

        resultado = semiperimetro*(semiperimetro- longitud_lado_1)*(semiperimetro- longitud_lado_2)*(semiperimetro- longitud_lado_3)

        return(math.sqrt(resultado))

    def baricentro(self):
        baricentro_x= (self.p1.x+self.p2.x+self.p3.x)/3.0
        baricentro_y= (self.p1.y+self.p2.y+self.p3.y)/3.0
        return(Punto(baricentro_x, baricentro_y))



class Poligono:
    def __init__(self, vector_puntos):
        self.vector_puntos = vector_puntos

    def ordenar_puntos(self):
        self.vector_puntos =  sorted(self.vector_puntos)
        return self.vector_puntos

    def dibujar_poligono(self):
        
        self.vector_puntos = sorted(self.vector_puntos)

        for i in self.vector_puntos:
            print(i)
        
        for i in range(0, len(self.vector_puntos)-1):
            valor_x = [self.vector_puntos[i].x, self.vector_puntos[i+1].x]
            valor_y = [self.vector_puntos[i].y, self.vector_puntos[i+1].y ]
            plt.plot(valor_x, valor_y)

        valor_x = [self.vector_puntos[0].x, self.vector_puntos[len(self.vector_puntos)-1].x]
        valor_y = [self.vector_puntos[0].y, self.vector_puntos[len(self.vector_puntos)-1].y ]
        plt.plot(valor_x, valor_y)
        plt.show()



       # valores_x = [self.x, self.y]
        #valores_y = [q.x, q.y]
        #plt.plot(valores_x, valores_y)

            
    #vamos a triangular el poligono:
    def triangulacion(self):
        self.vector_puntos = sorted(self.vector_puntos)
        triang =[]
        for i in range(0,len(self.vector_puntos)-2):
            triang += [Triangulo(self.vector_puntos[i], self.vector_puntos[i+1], self.vector_puntos[i+2])] 
        return triang

    #Implementamos el area del poligono sumando el area de cada triangulo
    def area(self):
        triangulos = self.triangulacion()
        area = 0
        for i in triangulos:
            area += i.area()
        return area

class Circunferencia:
    def __init__(self, centro, radio):
        self.centro = centro
        self. radio = radio
    
    def __str__(self):
        resultado = '(x'
        if (self.centro.x <0):
            resultado += '+' + str(abs(self.centro.x))+ ')**2+(y'
        if (self.centro.x == 0):
            resultado += ')**2+(y'
        if (self.centro.x >0):
            resultado += '-'+str(self.centro.x)+ ')**2+(y'
        if (self.centro.y <0):
            resultado += '+' + str(abs(self.centro.y))+')**2'
        if (self.centro.y == 0):
            resultado += ')**2'
        if (self.centro.y >0):
            resultado += '-'+str(self.centro.y)+ ')**2'
        resultado += '=' + str(self.radio**2)
        return(resultado)
