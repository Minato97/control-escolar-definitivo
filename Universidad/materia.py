from Universidad.profesor import Profesor
from Universidad.alumno import Alumno

class Materia():

    def __init__(self, nombre):
        self.__nombre = str(nombre)
        self.__titular = Profesor
        self.__alumnos = list()

    def addAlumno(self,alumno):
        self.__alumnos.append(alumno)

    def delAlumno(self,alumno):
        self.__alumnos.remove(alumno)

    def listarAlumnos(self):
        print("""      Los alumnos inscritos a la carrera son: """)
        for alum in self.__alumnos:
            print(alum.getAlumno())