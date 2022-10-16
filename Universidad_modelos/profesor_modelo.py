from dateutil.relativedelta import relativedelta
from datetime import date, datetime

profesores=list()

class Profesor:
    # __no_empleado = None
    # __nombre = None
    # __fecha_ingreso = None

    def __init__(self,no_empleado):
        self.__no_empleado = no_empleado
        self.__nombre = str
        self.__fecha_ingreso = date

    def getNoempleado(self):
        return self.__nombre

    def getProfesor(self):
        return self.__nombre

    def getFechaingreso(self):
        return self.__fecha_ingreso

    def calcularAntiguedad(self,profesor):
        antiguedad = relativedelta(datetime.now(), profesor.getFechaingreso())
        return antiguedad.years

    def setNoempleado(self, no_empleado):
        self.__no_empleado = no_empleado

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setFechaingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso


