from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Alumno:

    def __init__(self, matricula, nombre, fecha_nacimiento, fecha_ingreso, genero, ciudad):
        self.__matricula = int(matricula)
        self.__nombre = str(nombre)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__genero = str(genero)
        self.__ciudad = str(ciudad)

    def getMatricula(self):
        return self.__matricula

    def getAlumno(self):
        return self.__nombre

    def getFechanacimiento(self):
        return self.__fecha_nacimiento

    def getFechaingreso(self):
        return self.__fecha_ingreso

    def getgenero(self):
        return self.__genero

    def getCiudad(self):
        return self.__ciudad

    def calcularEdad(self,alumno):
        edad = relativedelta(datetime.now(), alumno.getFechanacimiento())
        return edad.years

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setFechanacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def setFechaingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso

    def setGenero(self, genero):
        self.__genero = genero

    def setCiudad(self, ciudad):
        self.__ciudad = ciudad


# alumno = Alumno(123,"fe",date(2000,5,2),date(2000,10,5),"m","g")
#
# print(alumno.calcularEdad(alumno))

