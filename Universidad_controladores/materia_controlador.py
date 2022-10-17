
from Universidad_modelos.profesor_modelo import *
from Universidad_modelos.carrera_modelo import *
import os

def inscribirAlumnosMateria():
    nombre_carrera = input("Introduzca el nombre de la carrera a la que pertenece la materia: ")
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Nombre de la materia a la que desea registrar un alumno: ")
            matricula_alumno = int(input("Introduzca el número de matricula del alumno: "))
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    for alum in carr.getAlumnosC():
                        if int(alum.getMatricula()) == matricula_alumno:
                            mat.setAlumno(alum)
                            os.system("pause")
                            os.system("cls")
                            pass
                        else:
                            os.system("cls")
                            print("El alumno con dicha matricula no esta registrado en la carrera")
                            pass
                else:
                    os.system("cls")
                    print("El nombre de la materia no coincide con los registros actuales")
                    os.system("pause")
                    os.system("cls")
                    pass
        else:
            os.system("cls")
            print("El nombre de la carrera no coincide con los registros actuales")
            os.system("pause")
            os.system("cls")
            pass

def listarAlumnosMateria():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Nombre de la materia a la que desea mostrar sus alumnos: ")
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    mat.listarAlumnos(mat)
                    os.system("pause")
                    os.system("cls")
                    pass
                else:
                    print("El nombre de la materia no coincide con los registros actuales")
                    os.system("pause")
                    os.system("cls")
                    pass
        else:
            os.system("cls")
            print("La carrera no fue encontada")
            os.system("pause")
            pass

def asignarProfesorMateria():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Nombre de la materia a la que desea asignar profesor: ")
            numero_empleado = int(input("Introduzca el número de empleado del profesor que va a asignar: "))
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    for prof in profesores:
                        if int(prof.getNoempleado()) == numero_empleado:
                            mat.setTitular(prof)
                            os.system("cls")
                            print("El profesor se asigno correctamente")
                            os.system("pause")
                            os.system("cls")
                            pass
                        else:
                            os.system("cls")
                            print("El número de empleado no coincide con ningún registro")
                            os.system("pause")
                            os.system("cls")
                            pass
                else:
                    os.system("cls")
                    print("El nombre de la materia no coincide con los registros actuales")
                    os.system("pause")
                    os.system("cls")
                    pass
        else:
            os.system("cls")
            print("La carrera no fue encontada")
            os.system("pause")
            pass