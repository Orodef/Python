'''
Alejandro Hernández Lobo    2017157163
Grupo 6
'''

'''
Entradas: Una palabra u oración
Restircciones: Debe ser un str y no puede estar vacío
Salidas: Valor booleano que determina si es palíndromo o no
'''
def determinarPalindromo(palabra):
    if type(palabra) != str:
        return 'Debe ingresar una cadena de caracteres.'
    if palabra == '':
        return 'El parámetro ingresado está vacío.'
    else:
        return determinarInverso(palabra)

def determinarInverso(palabra):
    invertida = ''
    longitud = len(palabra) - 1

    while longitud >= 0:
        letra = palabra[longitud]
        invertida += letra
        longitud -= 1

    return compararPalindromo(palabra, invertida)

def compararPalindromo(palabra, invertida):
    if palabra == invertida:
        return True
    else:
        return False
