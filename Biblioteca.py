'''
Alejandro Hernández Lobo    2017157163
Fabián Navarro Solano    2017201089
'''

import clases

biblioteca = []
usuarios = []

def Menu():
    print("-->A continuacón se le mostrarán las opciones de las acciones que puede realizar:")
    print("\n")
    print("1. Ingresar un nuevo libro")
    print("2. Listar libros")
    print("3. Consultar disponibilidad de un libro")
    print("4. Eliminar un libro")
    print("5. Registrar un usuario")
    print("6. Listar usuarios")
    print("7. Consultar usuario")
    print("8. Retirar un Libro: ")
    print("9. Devolver Libro:" )
    print("\n")
    opción=(input("Ingrese el número de la acción que desea realizar: "))
    try:
        int(opción)
    except:
        print("-->Debe indicar un número")
        return Menu()
    if int (opción)==1:
        return ingresarLibro()
    elif int (opción) == 2:
        return listarLibros()
    elif int (opción) == 3:
        return consultarDisponibilidad()
    elif int (opción) == 4:
        return eliminarLibro()
    elif int (opción)== 5:
        return ingresarUsuario()
    elif int (opción) == 6:
        return listarUsuarios()
    elif int (opción) == 7:
        return consultarUsuario()
    elif int (opción) == 8:
        return retirarLibro()
    elif int (opción)==9:
        return devolverLibro()
    else:
        print("La opción ingresada es inválida.")
        return Menu()

def ingresarUsuario():
    respuesta1=input("Ha seleccionado la opción de ~Ingresar un usuario~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="sí" or respuesta1.lower()=="si" :
        pNombre = input("Ingrese su primer nombre: ")
        pApellido1 = input("Ingrese su primer apellido: ")
        pApellido2 = input("Ingrese su segundo apellido: ")
        pCedula = input("Ingrese su número de cédula: ")
        try:
            int(pCedula)
        except:
            print("-->Debe ser un número"+"\n")
            return ingresarUsuario()
        for persona in usuarios:
            if int(persona.getCedula())==int(pCedula):
                print("Cédula ya registrado")
                return Menu()
        pTelefono = input("Ingrese su número de teléfono: ")
        print("Datos de su direccion")
        pPais = input("Ingrese el país en el que reside: ")
        pProvincia = input("Ingrese la provincia: ")
        pCanton = input("Ingrese el cantón: ")
        pDistrito = input("Ingrese el distrito: ")
        pDetalles = input("Ingrese los detalles de la dirección: ")
        respuesta2=input("Digite *No* si no desea cambiar ningun dato digitado: ")
        if respuesta2.lower() == "no":
            nuevaDireccion =clases.Direccion(pPais,pProvincia,pCanton,pDistrito,pDetalles)
            nuevoUsuario = clases.Persona(pNombre,pApellido1,pApellido2,pCedula,pTelefono,nuevaDireccion)
            usuarios.append(nuevoUsuario)
            print("-->Usuario registrado"+"\n")
            return Menu()
        else:
            return ingresarUsuario()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return ingresarUsuario()

def ingresarLibro():
    respuesta1=input("Ha seleccionado la opción de ~Ingresar un libro~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="sí" or respuesta1.lower()=="si" :
        pTitulo = input("Ingrese el título del libro: ")
        pEditorial= input("Ingrese la editorial del libro: ")
        pANo =(input("Ingrese el año de publicación del libro: "))
        pISBN =input("Ingrese su número de ISBN: ")
        try:
            int(pISBN)
        except:
            print("Debe indicar un número"+"\n")
            return ingresarLibro()
        for libro in biblioteca:
            if int(libro.getISBN())==int(pISBN):
                print("-->ISBN Ya registrado"+"\n")
                return Menu()
        pAutor=input("Ingrese el autor del libro: ")
        pPalabrasClave =[]
        numeroPalabras=int(input("Indique número de palabras claves que desea agregar respecto al libro: "))
        contador=0
        while (contador<numeroPalabras):
            palabra=(input("Indique palabra clave numero "+str(contador+1)+": ")).lower()
            pPalabrasClave.append(palabra)
            contador+=1
        pCopias=int(input("ingrese Número de copias disponibles: "))
        respuesta2=input("Desea modificar su repuesta(Sí o No): ")
        if respuesta2.lower() == "no":
            nuevoLibro=clases.Libro(pTitulo.lower(),pEditorial.lower(),pANo,pISBN,pAutor.lower(),pPalabrasClave,pCopias)
            biblioteca.append(nuevoLibro)
            print("-->Libro Registrado"+"\n")
        elif respuesta2.lower()=="sí" or respuesta2.lower()=="si":
            return ingresarLibro()
        else:
            print("Debe indicar sí o no")
            return ingresarLibro()
        return Menu()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return ingresarLibro()

def retirarLibro():
    respuesta1=input("Ha seleccionado la opción de ~Retirar un libro~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="si" or respuesta1.lower()=="sí":
        respuesta2=input("Para retirar un libro Usted debe estar parte del sistema, por favor indique si ya está registrado o no: ")
        if respuesta2.lower()=="si" or respuesta2.lower()=="sí":
            cedula=int(input("Indique su número de cédula: "))
            try:
                int(cedula)
            except:
                print("Numero de cedula debe ser un número"+"\n")
                return retirarLibro()
            for persona in usuarios:
                if int(persona.getCedula())==(cedula):
                    print("Esperemos que tenga buen día "+ persona.getNombre())
                    ISBN=input("Por favor indique ISBN del libro: ")
                    try:
                        int(ISBN)
                    except:
                        print("Debe indicar un nuúmero"+"\n")
                        return retirarLibro()
                    for libro in biblioteca:
                        if int(ISBN) ==int(libro.getISBN()):
                            if int(libro.getNumeroCopiasDisponibles())>0:
                                print("Ud ha solicitado el Libro: "+libro.getTitulo()+" por: "+libro.getAutor())
                                respuesta3=input("¿Este era el Libro que quería?(Sí o No): ")
                                if respuesta3.lower()=="si" or respuesta3.lower()=="sí":
                                    nuevaLista=(persona.getlistaPrestamos())+[libro.getISBN()]
                                    persona.setlistaPrestamos(nuevaLista)
                                    print("-->Retire el libro en la oficina de retiro, Gracias por preferirnos"+"\n")
                                    NumeroCopiasDisponibles=int(libro.getNumeroCopiasDisponibles())-1
                                    libro.setNumeroCopiasDisponibles(NumeroCopiasDisponibles)
                                    return Menu()
                                else:
                                    return retirarLibro()
                            else:
                                print("-->El libro no está disponible"+"\n")
                                return Menu()
                    print("El libro no lo tenemos o bien indicó mal su ISBN"+"\n")
                    return Menu()
            print("-->Ud Indicó mal su número de cédula o bien no está registrado, será devuelto al menú principal"+"\n")
            return Menu()
        elif(respuesta2.lower()=="no"):
            return Menu()
        else:
            print("-->Debe indicar un Sí o un No")
            return retirarLibro()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return retirarLibro()
            
def devolverLibro():
    respuesta1=respuesta1=input("Ha seleccionado la opción de ~Devolver un libro~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="si" or respuesta1.lower()=="sí":
        cedula=input("Digite su cédula: ")
        try:
            int(cedula)
        except:
            print("--> Digite un número")
            return devolverLibro()
        #Se revisa que la persona que entriega el libro está registrado en la biblioteca
        for persona in usuarios:
            if int(cedula)==int(persona.getCedula()):
                ISBN=input("Indique número ISBN del libro a delvolver: ")
                try:
                    int(ISBN)
                except:
                    print("Debe indicar una numero"+"/n")
                    return devolverLibro()
                for libro in biblioteca:
                    #Se revisa que el libro que se devuelva en realidad fue tomado de la biblioteca
                    if int(ISBN)==int(libro.getISBN()):
                        if int(libro.getCopias())== int(libro.getNumeroCopiasDisponibles()):
                            print("-->Ud no puede tener este libro o no es propiedad de esta Biblioteca"+"\n")
                            return Menu()
                        else:
                            NumeroCopiasDisponibles=int(libro.getNumeroCopiasDisponibles())+1
                            libro.setNumeroCopiasDisponibles(NumeroCopiasDisponibles)
                            #se revisa que el libro fue retirado por la persona
                            for libro in persona.getlistaPrestamos():
                                if int(ISBN)==int(libro):
                                    #se elimina el libro de la lista de pendientes de la persona
                                    nuevalista=[]
                                    for libro in persona.getlistaPrestamos():
                                        if int (libro)!= int (ISBN):
                                            nuevalista+=[int(libro)]
                                    persona.setlistaPrestamos(nuevalista)
                                    print("-->Muchas Gracias por Devolver el libro"+"\n")
                                    return Menu()
                            print("Ud no posee ese libro")
                            return Menu()
                print("-->El libro no está en nuestra biblioteca o ingresó mal su ISBN"+"\n")
                return Menu()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return devolverLibro()

def consultarDisponibilidad():
    respuesta1=input("Ha seleccionado la opción de ~Consultar Disponiblidad de un libro~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="si" or respuesta1.lower()=="sí":
        ISBN=input("Indique número ISBN del libro a consultar: ")
        try:
            int(ISBN)
        except:
            print("-->Debe indicar una número"+"\n")
            return consultarDisponibilidad()
        for libro in biblioteca:
            if int(ISBN)==int(libro.getISBN()):
                if int(libro.getNumeroCopiasDisponibles())==0:
                    print("-->Libro no disponible"+"\n")
                    return Menu()
                else:
                    print("-->Número de libros disponibles: " + str(libro.getNumeroCopiasDisponibles())+"\n")
                    return Menu()
        print("-->El libro no está en nuestra biblioteca o ingresó mal su ISBN"+"\n")
        return Menu()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return consultarDisponibilidad()

def listarLibros():
    respuesta1=input("Ha seleccionado la opción de ~Listar libros~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="sí" or respuesta1.lower()=="si" :
        print("A continuación se muestran las opciones de listado:\n")
        print("1. Editorial")
        print("2. Autor")
        print("3. Listar todo el catálogo")
        print("\n")
        opcionListado = int(input("Indique el número del criterio de listado que desea utilizar: "))
        print("\n")

        if opcionListado == 1:
            return listarEditorial()
        elif opcionListado == 2:
            return listarAutor()
        elif opcionListado == 3:
            return listarCatalogo()
        else:
            return "La opción ingresada es inválida."
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return listarLibros()

def listarEditorial():
    editorialBuscada = input("Ingrese la editorial que busca: ")
    print("\n")

    for libro in biblioteca:
        if (libro.getEditorial()).lower() == editorialBuscada.lower():
            print(libro)
            print("\n")
            return Menu()
    print("Editorial No encontrada")
    return Menu()

def listarAutor():
    autorBuscado = input("Ingrese el autor que busca: ")
    print("\n")

    for libro in biblioteca:
        if (libro.getAutor()).lower() == autorBuscado.lower():
            print(libro)
            print("\n")
            return Menu()
    print("Autor No encontrado")
    return Menu()

def listarCatalogo():
    print("Los libros en el catálogo son: \n")

    for libro in biblioteca:
        print(libro)
        print("\n")
    return Menu()

def listarUsuarios():
    respuesta1=input("Ha seleccionado la opción de ~Listar usuarios~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="sí" or respuesta1.lower()=="si" :
        print("A continuación se muestran las opciones de listado:\n")
        print("1. Primer Apellido")
        print("2. Todos los usuarios")
        print("\n")
        opcionListado = int(input("Indique el número del criterio de listado que desea utilizar: "))
        print("\n")

        if opcionListado == 1:
            return listarApellidos()
        elif opcionListado == 2:
            return listarTodos()
        else:
            return "La opción ingresada es inválida."
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return listarUsuarios()

def listarApellidos():
    apellidoBuscado = input("Ingrese el apellido que busca: ")
    print("\n")

    for usuario in usuarios:
        if (usuario.getApellido1()).lower() == apellidoBuscado.lower() or (usuario.getApellido2()).lower() == apellidoBuscado.lower() :
            print(usuario)
            print("\n")
            return Menu()
    print("Usuario no encontrado")
    return Menu()

def listarTodos():
    for usuario in usuarios:
        print(usuario)
        print("\n")
    return Menu()

def eliminarLibro():
    respuesta1=input("Ha seleccionado la opción de ~Listar usuarios~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="sí" or respuesta1.lower()=="si" :
        ISBNeliminar = input('Ingrese el ISBN del libro que desea eliminar del catálogo: ')
        try :
            int(ISBNeliminar)
        except:
            print("Debe Indicar un número")
            return eliminarLibro()
        print("\n")

        for libro in biblioteca:
            if int(ISBNeliminar) == libro.getISBN():
                biblioteca.remove(libro)
                print("Libro eliminado.")
                return Menu()
            else:
                print("Libro no encontrado.")
                return Menu()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return eliminarLibro()

def consultarUsuario():
    respuesta1=input("Ha seleccionado la opción de ~Consultar usuario~ ¿Esta era la acción que deseaba ingresar?"+"\n"+"Responda con Sí o No: ")
    if respuesta1.lower()=="sí" or respuesta1.lower()=="si" :
        identificacionBuscada = input("Ingrese el número de identificación de usuario que busca: ")

        try:
            int(identificacionBuscada)
        except:
            print("Debe ingresar un número.")
            return Menu()

        for usuario in usuarios:
            if usuario.getCedula() == identificacionBuscada:
                print(usuario)
                return Menu()
    elif(respuesta1.lower()=="no"):
        return Menu()
    else:
        print("-->Debe indicar un Sí o un No")
        return eliminarLibro()
