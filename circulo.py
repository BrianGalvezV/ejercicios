class Circulo:
    def __init__(self) -> None:
        self.radio = 0
        self.__pi = 3.1416

    def area(self):
        return self.radio**2 * self.__pi

    def perimetro(self):
        return 2 * self.radio * self.__pi

calculo = Circulo()

calculo.radio = float(input("Cual es el radio del circulo"))

print(calculo.perimetro())