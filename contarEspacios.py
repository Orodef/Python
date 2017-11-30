def contarEspacios(oracion):

    iteracion = 0
    cantidadPalabras = 0
    letraActual = ''

    while oracion != '':
        iteracion += 1

        letraActual = oracion[:1]
        if letraActual == ' ':
            cantidadPalabras += 1
            if iteracion == 1:
                cantidadPalabras -= 1
            iteracion = 0
        oracion = oracion [1:]
    return cantidadPalabras + 1