from Universidad.materia import Materia


class Carrera:
    __nombre = None
    __materias = None

    def __init__(self,nombre):
        self.__nombre = str(nombre)
        self.__materias = list()

    def getCarrera(self):
        return self.__nombre

    def getMaterias(self):
        return self.__materias

    def setNombre(self,nombre):
        self.__nombre = nombre

    def setMaterias(self,materias):
        self.__materias = materias

    def addMateria(self,materia):
        self.__materias.append(materia)

    def delMateria(self,materia):
        self.__materias.remove(materia)

    def listarMaterias(self, materia):
        print("""      Las materias registradas a la carrera son: """)
        for mat in materia.__materias:
            print(mat.getMateria())