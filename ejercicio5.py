class animal:
    def __init__(self,dieta):
        pass

class cuidador:
    def __init__(self,nombre,apellido,animales_cuidador):
        self.nombre = nombre
        self.apellido = apellido
        self.animales_cuidador = animales_cuidador
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
        print(f'{cuidador}, cuidara a {animal}')
    def coger_vacaciones(self,cuidador,inicio,duracion):
        pass


zoo1=zoo(stock({"carne":1000,"verdura":1000,"insectos":1000}),[cuidador("pepe","galan",["girafa"]),cuidador("juan","perez",["leon"]),cuidador("javi","fdz",["sapo"])],["girafa","leon","sapo"])
