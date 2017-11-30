'''
Alejandro Hernández Lobo      2017157163
Grupo 
'''

#Reto 1

def contarCaracteres(cadena):
    
    resultado = []
    usados = []
    indice1 = 0

    while (indice1 < len(cadena)):
        letra = cadena[indice1].upper()
        if (yaAparecio(letra, usados) == False):
            indice2 = 0
            cantidad = 0
            while (indice2 < len(cadena)):
                if (cadena[indice1].upper() == cadena[indice2].upper()):
                    cantidad += 1
                indice2 += 1
            resultado += [[cadena[indice1].upper(), cantidad]]
        usados += cadena[indice1].upper()
        indice1 += 1
    return resultado

def yaAparecio (letra, usados):
    
    indice = 0

    while (indice < len(usados)):
        if (letra == usados[indice].upper()):
            return True
        indice += 1
    return False

#Reto 2

def podarMatriz(matriz):

    matriz = matriz[1:]
    matriz = matriz[:len(matriz)-1]
    matriz = matriz[0][1:]
    matriz = matriz[:(len(matriz))-1]
    return matriz
