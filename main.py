from Universidad.carrera import Carrera
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
        id_carrera = input("Introduce la clave de la carrera: ")
        crn = input("Introduce el crn de la materia: ")
        nombre = input("Introduce el nombre de la carrera: ")
        semestre = input("Introduce el semestre de la carrera: ")
        existe_carrera = False
        for i in carreras:
            if i.getid() == id_carrera:
                existe_carrera = True
                break
        if existe_carrera:
            if i.addMateria(crn, nombre, semestre):
                print("La materia se registro de forma correcta")
        else:
            print("la clave de la carrera no fue encontrada.")

    elif op == 3:  # 3) Inscribir alumnos a una materia.
        pass
    elif op == 4:  # 4) Registrar profesor a una materia.
        print("*************************************")
        print("se tienen {} carerras registradas.".format((len(carrera))))
        print("*************************************")
        for i in carreras:
            print("Clave de la carrera: {}".format(i.getid()))
            print("Nombre de la carrera: {}".format(i.getnombre()))
        print("*************************************")
    elif op == 5:  # 5) Listar materias de una carrera.
        pass
    elif op == 6:  # 6) Listar carreras.
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
