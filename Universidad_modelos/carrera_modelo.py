from Universidad_modelos.materia_modelo import Materia

carreras = list()
class Carrera:
    # __nombre = None
    # __materias = None

    def __init__(self,carrera):
        self.__nombre = carrera
        self.__materias = list()
        self.__alumnos = list()

    def getCarrera(self):
        return self.__nombre

    def getMaterias(self):
        return self.__materias

    def getAlumnosC(self):
        return self.__alumnos

    def setAlumnosC(self,alumno):
        self.__alumnos.append(alumno)

    def setNombre(self,nombre):
        self.__nombre = nombre

    def setMaterias(self,materia):
        self.__materias.append(materia)

    # def addMateria(self,materia):
    #     self.__materias.append(materia)

    def delMateria(self,materia):
        self.__materias.remove(materia)

    def listarMaterias(self, carrera):
        print("""      Las materias registradas a la carrera son: """)
        for mat in carrera.__materias:
            print(mat.getMateria())

    def listarAlumnosC(self, carrera):
        print("""      Los alumnos registradas a la carrera son: """)
        for alum in carrera.__alumnos:
            print(alum.getMatricula(),"\t",alum.getAlumno(),"\t",alum.getFechanacimiento(),"\t",alum.getFechaingreso(),"\t",alum.getGenero(),"\t",alum.getCiudad())

