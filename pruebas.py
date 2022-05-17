lista = [8, 7, 6, 9, 5, 1, 3, 2, 4]

def ordenar_bubble(array):
    longitud = len(array) - 1
    for i in range(longitud):
        for j in range(longitud):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


def ordenar(array):
    longitud = len(array)
    for i in range(longitud - 1):
        num_compara = i
        for j in range(i + 1, longitud):
            if array[j] < array[num_compara]:
                num_compara = j
        temp = array[num_compara]
        array[num_compara] = array[i]
        array[i] = temp
    return array


def run():
    print(ordenar(lista))
    print(ordenar_bubble(lista))

if __name__ == '__main__':
    run()