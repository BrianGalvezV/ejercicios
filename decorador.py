def decorador(func):
    print("funcion decoradora")
    def nueva_funcion():
        print("nueva funcion")
        #func() #se ejecuta la funcion que se recibe como argumento
    return nueva_funcion #se retorna una funcion dentro del deorador

@decorador
def operacion():
    print("funcion decorada")

operacion()
