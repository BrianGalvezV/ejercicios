


lista = [4, 5, 3, 6, 2, 1, 7]

def ordenamiento_seleccion(array):
    longitud = len(array)
    for i in range (longitud -1):
        num_comparar = i
        for j in range(i + 1, longitud):
            if lista[j] < lista[num_comparar]:
                num_comparar = j
        temportal = lista[num_comparar]
        lista[num_comparar] = lista[i]
        lista[i] = temportal

    return array


print(ordenamiento_seleccion(lista))