from datetime import datetime


class User():
    def __init__(self, name, fecha_nacimiento):
        self.name = name
        self.fecha_nacimiento = fecha_nacimiento

    def calcular_edad(self):
        fecha_actual = int(datetime.today().strftime('%Y'))
        edad = fecha_actual - self.fecha_nacimiento
        print(edad)

obj = User('Brian', 1983)
print(obj.name)
obj.calcular_edad()
