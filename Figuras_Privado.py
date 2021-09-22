#Osvaldo Basilio Jijon
#Sergio Valdivia
class Punto:
    def __init__(self, x, y):
        self.__cordx = x
        self.__cordy = y
    
    def get_cordx(self):
        return self.__cordx

    def get_cordy(self):
        return self.__cordy
    
    def set_cordx(self, x):
        self.__cordx = x
    
    def set_cordy(self, y):
        self.__cordy = y
    
    def area (self):
        return 0
    
    def volumen (self):
        return 0
    def __str__(self):
        return 'Clase Punto: ' + str(self.get_cordx()) + ' ' + str(self.get_cordy())
###################################
class Circulo(Punto):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__radio=r

    def get_radio(self):
        return self.__radio
    
    def set_radio(self, r):
        self.__radio = r

    def area(self):
        return 3.1416*self.__radio**2

    def volumen (self):
        return 0
    
    def __str__(self):
         return 'Clase Circulo: ' + str(super().get_cordx()) + ' ' + str(super().get_cordy()) + ' ' + str(self.get_radio())
##################################
class Cilindro(Circulo):
    def __init__(self,x,y,r,h):
        super().__init__(x,y,r)
        self.__altura=h

    def get_altura(self):
        return self.__altura
    
    def set_altura(self, h):
        self.__altura = h

    def area(self):
        return (2*3.1416*self.get_radio()*self.__altura)+(2*3.1416*self.get_radio()**2)
        
    def volumen (self):
        return 3.1416*self.get_radio()**2*self.__altura
    
    def __str__(self):
         return 'Clase Circulo: ' + str(super().get_cordx()) + ' ' + str(super().get_cordy()) + ' ' + str(super().get_radio()) + ' ' + str (self.get_altura())
        
###################################
        #Comprobar clases#
p1=Punto(1,8)
print(p1)

c1=Circulo(5,3,2)
print(c1)
print(c1.area())
print(c1.volumen())

ci1=Cilindro(4,1,5,9)
print(ci1)
print(ci1.area())
print(ci1.volumen())