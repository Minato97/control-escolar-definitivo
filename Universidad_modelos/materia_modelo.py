from Universidad_modelos.profesor_modelo import Profesor
from Universidad_modelos.alumno_modelo import Alumno

class Materia:

    def __init__(self, nombre):
        self.__nombre = str(nombre)
        self.__titular = Profesor
        self.__alumnos = list()

    def getMateria(self):
        return self.__nombre

    def getAlumnos(self):
        return self.__alumnos

    def getTitular(self):
        return self.__titular

    # def setMateria(self, nombre):
    #     self.__nombre = nombre

    def setTitular(self,profesor):
        self.__titular = profesor

    def setAlumno(self,alumno):
        self.__alumnos.append(alumno)

    def delAlumno(self,alumno):
        self.__alumnos.remove(alumno)

    def listarAlumnos(self,materia):
        print("""      Los alumnos inscritos a la materia son: """)
        for alum in materia.__alumnos:
            print(alum.getMatricula(),"\t",alum.getAlumno(),"\t",alum.getFechanacimiento(),"\t",alum.getFechaingreso(),"\t",alum.getGenero(),"\t",alum.getCiudad())