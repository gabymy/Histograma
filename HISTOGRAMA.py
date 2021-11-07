

def histograma(elementos):
    for n in elementos:
        salida = ''
        estrellas = n
        while (estrellas > 0):
            salida += '*'
            estrellas = estrellas - 1
        print(salida)


histograma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
