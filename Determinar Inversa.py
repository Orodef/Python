def determinarInverso(palabra):
    invertida = ''
    longitud = len(palabra) - 1

    while longitud >= 0:
        letra = palabra[longitud]
        invertida += letra
        longitud -= 1

    return invertida
