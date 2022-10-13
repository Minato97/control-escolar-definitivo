from Universidad.carrera import Carrera
from Universidad.materia import Materia
import sys
import os
import time

carreras = list()

def main():
    print("Bienvenido al sistema de control escolar")
    print("1) Registrar carreras.")
    print("2) Registrar materias de una carrera.")
    print("3) Inscribir alumnos a una materia.")
    print("4) Registrar profesor a una materia.")
    print("5) Listar materias de una carrera.")
    print("6) Listar carreras.")
    print("7) Listar alumnos inscritos a una materia.")
    print("8) Listar alumnos de una carrera.")
    print("9) Listar materias que imparte un profesor.")
    print("10) Salir.")
    op = int(input("Elije una opcion: "))


    if op == 1:  # 1) Registrar carreras.
        os.system("cls")
        nombre_carrera = input("Introduce el nombre de la carrera:")
        if len(carreras) != 0:
            for carr in carreras:
                if carr.getCarrera() == nombre_carrera:
                    print("El nombre {} ya existe, introduce uno distinto".format(nombre_carrera))
                else:
                    carrera = Carrera(nombre_carrera)
                    carreras.append(carrera)
                main()
        else:
            carrera = Carrera(nombre_carrera)
            carreras.append(carrera)
            main()

    elif op == 2:  # 2) Registrar materias de una carrera.
        nombre_carrera = input("Introduce el nombre de la carrera: ")
        for carr in carreras:
            if carr.getCarrera() == nombre_carrera:
                nombre_materia = input("Introduce el nombre de la materia: ")
                nueva_materia = Materia(nombre_materia)
                carr.addMateria(nueva_materia)
                print(carr.getMaterias())
                os.system("pause")
                main()
            else:
                print("la clave de la carrera no fue encontrada.")
                main()

    elif op == 3:  # 3) Inscribir alumnos a una materia.
        pass
    elif op == 4:  # 4) Registrar profesor a una materia.
       pass
    elif op == 5:  # 5) Listar materias de una carrera.
        nombre_carrera = input("Introduce el nombre de la carrera: ")
        for carr in carreras:
            if carr.getCarrera() == nombre_carrera:
                carr.listarMaterias(carr)
                main()
            else:
                print("la clave de la carrera no fue encontrada.")
                main()
    elif op == 6:  # 6) Listar carreras.
        if len(carreras) == 0:
            print("No se tienen carreras registradas")
            os.system("pause")
            main()
        else:
            print("""      Las carreras existentes son: """)
            for carr in carreras:
                print(carr.getCarrera())
        main()
    elif op == 7:  # 7) Listar alumnos inscritos a una materia.
        pass
    elif op == 8:  # 8) Listar alumnos de una carrera.
        pass
    elif op == 9:  # 9) Listar materias que imparte un profesor.
        pass
    elif op == 10:  # 10) Salir.
        cadena = "Gracias por usar software de calidad\n¡Hasta pronto!..."

        for i in range(0, len(cadena)):
            print(cadena[i], end="")
            time.sleep(0.1)
        sys.exit()

if __name__ == "__main__":
    main()
