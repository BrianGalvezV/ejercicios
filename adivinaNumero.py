
import random

def f_nuero_adivinar():
    numero_adivinar = random.randint(1,100)
    return numero_adivinar

def run():
    numero_adivinar = f_nuero_adivinar()
    print(numero_adivinar)
    while True:
        numero = int(input('Ingrese un numero: '))
        if numero == numero_adivinar:
            print('Felicidades, adivinaste el numero')
            break
        elif numero > numero_adivinar:
            print('El numero es menor')
        else:
            print('El numero es mayor')

if __name__ == '__main__':
    run()