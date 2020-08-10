import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return('('+str(self.x)+','+str(self.y)+')')

    def a_vector(self, p):
        return Vector(p.x - self.x, p.y - self.y)

class Vector:
    def __init__(self, primera_componenente, segunda_componente):
        self.primera_componente = primera_componenente
        self.segunda_componente = segunda_componente

    def __str__(self):
        return('('+str(self.primera_componente)+','+str(self.segunda_componente)+')')

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
