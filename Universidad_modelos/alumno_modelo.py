from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Alumno:

    def __init__(self):
        self.__matricula = int
        self.__nombre = str
        self.__fecha_nacimiento = date
        self.__fecha_ingreso = date
        self.__genero = str
        self.__ciudad = str

    def getMatricula(self):
        return self.__matricula

    def getAlumno(self):
        return self.__nombre

    def getFechanacimiento(self):
        return self.__fecha_nacimiento

    def getFechaingreso(self):
        return self.__fecha_ingreso

    def getGenero(self):
        return self.__genero

    def getCiudad(self):
        return self.__ciudad

    def calcularEdad(self,alumno):
        edad = relativedelta(datetime.now(), alumno.getFechanacimiento())
        return edad.years

    def setMatricula(self, matricula):
        self.__matricula = matricula

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