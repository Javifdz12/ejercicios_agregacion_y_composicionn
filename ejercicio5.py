class animal:
    def __init__(self,dieta):
        pass

class cuidador:
    def __init__(self,animales,vacaciones):
        pass

class stock:
    def __init__(self,comida):
        self.comida=comida
    def sacar(self,alimento,cantidad):
        while alimento in self.comida:
            if self.comida[alimento]<=cantidad:
                self.comida[alimento]=self.comida[alimento]-cantidad
            else:
                print(f'no tienes suficiente {alimento}, tienes {self.comida[alimento]}')
        else:
            print(f'no tienes {alimento} en stock')



class zoo:
    def __init__(self,stock,cuidadores,animales):
        self.stock = stock
        self.cuidadores = cuidadores
        self.animales = animales
    def cuidar(self,cuidador,animal):
        print(f'el {cuidador}, cuidara a {animal}')
    def coger_vacaciones(self,cuidador,inicio,duracion):
        pass