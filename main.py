from Universidad.carrera import Carrera
from Universidad.materia import Materia
from Universidad.alumno import Alumno
from datetime import date
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
                print("La carrera no fue encontada, no es posible registrar materias.")
                main()

    elif op == 3:  # 3) Inscribir alumnos a una materia.
        nombre_carrera = input("introduzca la carrera a la que desea añadir a algún alumno: ")
        for carr in carreras:
            if carr.getCarrera() == nombre_carrera:
                nombre_materia = input("Nombre de la materia a la que desea registrar un alumno: ") 
                for mat in carr.getMaterias():
                    if mat.getMateria() == nombre_materia:
                        print("Ingresa los siguientes datos del alumno: ")
                        alumno = Alumno()
                        alumno.matricula = int(input("Matricula: "))
                        alumno.name = input("Nombre: ")
                        print("\nFecha de nacimiento")
                        anio = int(input("Año: "))
                        mes = int(input("Mes: "))
                        dia = int(input("Dia: "))
                        alumno.fecha_nacimiento = date(anio, mes, dia)
                        print("\nFecha de registro")
                        anio = int(input("Año: "))
                        mes = int(input("Mes: "))
                        dia = int(input("Dia: "))
                        alumno.fecha_ingreso = date(anio, mes, dia)
                        alumno.genero = input("Genero (M/F): ")
                        alumno.ciudad = input("Ciudad de procedencia: ")
                        mat.addAlumno(alumno)
                        main()
                        
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
        nombre_carrera = input("¿De qué carrera le gustaría ingresar alumnos listar alumnos?")
        for carr in carreras:
            if carr.getCarrera() == nombre_carrera:
                carr=Materia(carr.getMateria())
                carr.listarAlumnos()
                main()
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
