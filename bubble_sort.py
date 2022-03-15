
def bubbleSort(array):
    length = len(array) -1
    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array[j + 1 ]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
                print(aux)

    return array



#score = [50, 40, 34, 80, 43, 90]

score2 = [70, 90, 0, 80, 60, 85]

#print(bubbleSort(score))
print(bubbleSort(score2))