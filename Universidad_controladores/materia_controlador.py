from datetime import date, datetime
from Universidad_modelos.alumno_modelo import Alumno
from Universidad_modelos.materia_modelo import Materia
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
                            pass
                        else:
                            print("El alumno con dicha matricula no esta registrado en la carrera")
                            pass
                else:
                    print("El nombre de la materia no coincide con los registros actuales")
                    os.system("pause")
                    pass
        else:
            print("El nombre de la carrera no coincide con los registros actuales")
            os.system("pause")
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
                    pass
                else:
                    print("El nombre de la materia no coincide con los registros actuales")
                    os.system("pause")
                    pass
        else:
            print("La carrera no fue encontada")
            os.system("pause")
            pass
