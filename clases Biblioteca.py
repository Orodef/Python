class Direccion:
    def __init__(self,pPais,pProvincia,pCanton,pDistrito,pSeñas):
        self.__pais=pPais
        self.__provincia=pProvincia
        self.__canton=pCanton
        self.__distrito=pDistrito
        self.__señas=pSeñas
    def getPais(self):
        return self.__pais
    def setPais(self,pPais):
        self.__pais=pPais
    def getProvincia(self):
        return self.__provincia
    def setProvincia(self,pProvincia):
        self.__provincia=pProvincia
    def getCanton(self):
        return self.__canton
    def setCanton(self,pCanton):
        self.__canton=pCanton
    def getDistrito(self):
        return self.__distrito
    def setDistrito(self,pDistrito):
        self.__distrito=pDistrito
    def getSeñas(self):
        return self.__señas
    def setSeñas(self,pSeñas):
        self.__señas=pSeñas
    def __str__(self):
        dirección="\n"
        dirección+="País: "+self.getPais()+ "\n"
        dirección+="Provincia: "+self.getProvincia()+ "\n"
        dirección+="Cantón: "+self.getCanton()+ "\n"
        dirección+="Distrito: "+self.getDistrito()+ "\n"
        dirección+="Detalles: "+self.getSeñas()
        return dirección
class  Persona:
    def __init__(self,pNombre,pApellido1,pApellido2,pCedula,pTelefono,pDireccion):
        self.__nombre=pNombre
        self.__apellido1=pApellido1
        self.__apellido2=pApellido2
        self.__cedula=pCedula
        self.__telefono=pTelefono
        self.__direccion=pDireccion
        self.__listaPrestamos=[]
    def getNombre(self):
        return self.__nombre
    def setNombre(self,pNombre):
        self.__nombre=pNombre
    def getApellido1(self):
        return self.__apellido1
    def setApellido1(self,pApellido1):
        self.__apellido1=pApellido1
    def getApellido2(self):
        return self.__apellido2
    def setApellido2(self,Apellido2):
        self.__apellido2=pApellido2
    def getCedula(self):
        return self.__cedula
    def setCedula(self,pCedula):
        self.__cedula=pCedula
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,pTelefono):
        self.__telefono=pTelefono
    def getDirección(self):
        return self.__direccion
    def setDirección(self,pDireccion):
        self.__direccion=pDireccion
    def getlistaPrestamos(self):
        return self.__listaPrestamos
    def setlistaPrestamos(self,pListaPrestamos):
        self.__listaPrestamos=pListaPrestamos
    def __str__(self):
        persona=""
        persona+="Nombre: "+self.getNombre()+ "\n"
        persona+="Primer Apellido: "+self.getApellido1()+ "\n"
        persona+="Segundo Apellido: "+self.getApellido2()+ "\n"
        persona+="Cédula: "+str(self.getCedula())+"\n"
        persona+="Telefono: "+str(self.getTelefono())+ "\n"
        persona+="Dirección: "+str(self.getDirección())+"\n"
        if len(self.getlistaPrestamos())==0:
            persona+="Ud no tiene libros en condición de préstamo"
        else:
            persona+="Ud tiene por pendiente de devolver(La lista será de ISBN'S):"+"\n"
            for libro in self.getlistaPrestamos():
                persona+= str(libro) + "\n"
        return persona

class  Libro:
    def __init__(self,pTitulo,pEditorial,pANo,pISBN,pAutor,pPalabrasClave,pCopias):
        self.__titulo=pTitulo
        self.__editorial=pEditorial
        self.__aNo=pANo
        self.__ISBN=pISBN
        self.__autor=pAutor
        self.__palabrasClave=pPalabrasClave
        self.__copias=pCopias
        self.__numeroCopiasDisponibles=pCopias
    def getTitulo(self):
        return self.__titulo
    def setTitulo(self,pTitulo):
        self.__titulo=pTitulo
    def getEditorial(self):
        return self.__editorial
    def setEditorial(self,pEditorial):
        self.__editorial=pEditorial
    def getANo(self):
        return self.__aNo
    def setANo(self,ANo):
        self.__apellido2=pANo
    def getNumeroCopiasDisponibles(self):
        return self.__numeroCopiasDisponibles
    def setNumeroCopiasDisponibles(self,pNumeroCopiasDisponibles):
        self.__numeroCopiasDisponibles=pNumeroCopiasDisponibles
    def getISBN(self):
        return self.__ISBN
    def setISBN(self,pISBN):
        self.__ISBN=pISBN
    def getAutor(self):
        return self.__autor
    def setAutor(self,pAutor):
        self.__autor=pAutor
    def getPalabrasClave(self):
        return self.__palabrasClave
    def setPalabrasClave(self,pPalabrasClave):
        self.__palabrasClave=pPalabrasClave
    def getCopias(self):
        return self.__copias
    def setCopias(self,pCopias):
        self.__copias=pCopias
    def __str__(self):
        libro=""
        libro+="Titulo: "+self.getTitulo()+ "\n"
        libro+="Editorial: "+self.getEditorial()+ "\n"
        libro+="Año: "+str(self.getANo())+ "\n"
        libro+="ISBN: "+str(self.getISBN())+"\n"
        libro+="Autor: "+str(self.getAutor())+ "\n"
        if len(self.getPalabrasClave())==0:
            libro+="No hay palabras Clave Relacionadas al Libro"+ "\n"
        else:
            libro+="PalabrasClave: " +"\n"
            for palabra in self.getPalabrasClave():
                libro+= palabra+"\n"
        libro+="Copias: "+str(self.getCopias())+ "\n"
        libro+="Copias disponibles: "+str(self.getNumeroCopiasDisponibles())
        return libro

