from dateutil.relativedelta import relativedelta
from datetime import date, datetime

class Profesor:
    __no_empleado = None
    __nombre = None
    __fecha_ingreso = None

    def __init__(self, no_empleado, nombre, fecha_ingreso):
        self.__no_empleado = int(no_empleado)
        self.__nombre = str(nombre)
        self.__fecha_ingreso = fecha_ingreso

    def getNoempleado(self):
        return self.__nombre

    def getProfesor(self):
        return self.__nombre

    def getFechaingreso(self):
        return self.__fecha_ingreso

    def calcularAntiguedad(self,profesor):
        antiguedad = relativedelta(datetime.now(), profesor.getFechaingreso())
        return edad.years

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setFechaingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso


