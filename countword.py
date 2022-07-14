text = 'El amor es un concepto universal relativo a la afinidad o armonía entre seres, la efinido de diversas formas según las diferentes ideologías y puntos de vista.'

def contWord(text, word):
    limpiar = text.replace(',','')
    minus = limpiar.lower()

    arrayText = minus.split()
    contar = arrayText.count(word)
    print(arrayText)
    print(contar)


def run():
    contWord(text, 'un')

if __name__ == '__main__':
    run()
