'''
Alejandro Hernández Lobo       2017157163
Grupo 6
'''
def multiplicarALaRusa(a,b):
    resultado = 0
    while (a != 0):
        if (a % 2 == 1):
            resultado += b
        a = a // 2
        b = b*2
    return resultado
