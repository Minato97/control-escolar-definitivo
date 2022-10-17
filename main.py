from Universidad_controladores.carrera_controlador import *
from Universidad_controladores.materia_controlador import *
from Universidad_controladores.profesor_controlador import *
import sys
import time


def main():

    print("Bienvenido al sistema de control escolar")
    print("1) Registrar carreras.")
    print("2) Registrar materias de una carrera.")
    print("3) Registrar profesor.")
    print("4) Registrar alumnos a una carrera.")
    print("5) Inscribir alumnos a una materia.")
    print("6) Asignar profesor a una materia.")
    print("7) Listar materias de una carrera.")
    print("8) Listar carreras.")
    print("9) Listar alumnos inscritos a una materia.")
    print("10) Listar alumnos de una carrera.")
    print("11) Listar materias que imparte un profesor.")
    print("12) Salir.")
    try:
        op = int(input("Elije una opcion: "))
        if op > 12 or op <= 0:
            print("Por favor ingrese una opción válida")
            os.system("pause")
            os.system("cls")
            main()
    except ValueError:
        print("Por favor ingrese una opción válida")
        os.system("pause")
        os.system("cls")
        main()
    except:
        pass

    if op == 1:  # 1) Registrar carreras.
        os.system("cls")
        print("<REGISTRAR CARRERA>")
        registrarCarreras()
        main()

    elif op == 2:  # 2) Registrar materias de una carrera.
        os.system("cls")
        print("<REGISTRAR MATERIAS A UNA CARRERA>")
        registrarMateriasCarrera()
        main()

    elif op == 3:  # 3) Registrar profesor.
        os.system("cls")
        print("<REGISTRAR PROFESOR>")
        registrarProfesor()
        main()

    elif op == 4:  # 4) Registrar alumnos a una carrera.
        os.system("cls")
        print("<REGISTRAR ALUMNOS A UNA CARRERA>")
        registrarAlumnosCarrera()
        main()

    elif op == 5:  # 5) Inscribir alumnos a una materia.
        os.system("cls")
        print("<REGISTRAR ALUMNO A UNA MATERIA")
        inscribirAlumnosMateria()
        main()

    elif op == 6:  # 6) Asignar profesor a una materia.
        os.system("cls")
        print("<ASIGNAR PROFESOR A UNA MATERIA>")
        asignarProfesorMateria()
        main()

    elif op == 7:  # 7) Listar materias de una carrera.
        os.system("cls")
        print("<LISTAR MATERIAS DE UNA CARRERA>")
        listarMateriasCarrera()
        main()

    elif op == 8:  # 8) Listar carreras.
        os.system("cls")
        print("<LISTAR CARRERAS>")
        listarCarreras()
        main()

    elif op == 9:  # 9) Listar alumnos inscritos a una materia.
        os.system("cls")
        print("<LISTAR ALUMNOS INSCRITOS A UNA MATERIA>")
        listarAlumnosMateria()
        main()

    elif op == 10:  # 10) Listar alumnos de una carrera.4
        os.system("cls")
        print("<LISTAR ALUMNOS DE UNA CARRERA>")
        listarAlumnosCarrera()
        main()

    elif op == 11:  # 11) Listar materias que imparte un profesor.
        os.system("cls")
        print("<MATERIAS QUE IMPARTE UN PROFESOR>")
        listarMateriasImpartidas()
        main()

    elif op == 12:  # 12) Salir.
        os.system("cls")
        cadena = "Gracias por usar software de calidad\n¡Hasta pronto!..."
        print(cadena)
        sys.exit()


if __name__ == "__main__":
    main()
