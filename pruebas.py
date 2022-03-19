
lista = [7, 1, 6, 2, 5, 3, 4, 8, 9]

def ordenar(array):
    longitud = len(array) - 1
    for i in range(longitud):
        for j in range(longitud):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array


print(ordenar(lista))
