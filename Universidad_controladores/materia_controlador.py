
from Universidad_modelos.profesor_modelo import *
from Universidad_modelos.carrera_modelo import *
import os

def inscribirAlumnosMateria():
    nombre_carrera = input("Introduzca el nombre de la carrera a la que pertenece la materia: ")
    flag = 3
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Nombre de la materia a la que desea registrar un alumno: ")
            flag = 2
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    matricula_alumno = int(input("Introduzca el número de matricula del alumno: "))
                    flag = 1
                    for alum in carr.getAlumnosC():
                        if int(alum.getMatricula()) == matricula_alumno:
                            flag = 4
                            for alum in mat.getAlumnos():
                                if int(alum.getMatricula()) == matricula_alumno:
                                    print("El alumno", alum.getAlumno(), " ya existe en la materia ", nombre_materia," no es necesario registrarla de nuevo")
                                    os.system("pause")
                                    os.system("cls")
                                    flag = 0
                            if flag == 4:
                                mat.setAlumno(alum)
                                os.system("pause")
                                os.system("cls")
                                flag = 0
                                pass


    if flag == 1:
        os.system("cls")
        print("El alumno con dicha matricula no esta registrado en la carrera")
        os.system("pause")
        os.system("cls")
        pass
    elif flag == 2:
        os.system("cls")
        print("El nombre de la materia no coincide con los registros actuales")
        os.system("pause")
        os.system("cls")
        pass
    elif flag == 3:
        os.system("cls")
        print("El nombre de la carrera no coincide con los registros actuales")
        os.system("pause")
        os.system("cls")
        pass
    elif flag == 4:
        os.system("cls")
        print("El nombre de la carrera no coincide con los registros actuales")
        os.system("pause")
        os.system("cls")
    else:
        pass

def listarAlumnosMateria():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    flag = 3
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Nombre de la materia a la que desea mostrar sus alumnos: ")
            flag = 2
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    mat.listarAlumnos(mat)
                    os.system("pause")
                    os.system("cls")
                    flag = 0
                    pass
    if flag == 2:
        os.system("cls")
        print("El nombre de la materia no coincide con los registros actuales")
        os.system("pause")
        os.system("cls")
        pass
    elif flag == 3:
        os.system("cls")
        print("El nombre de la carrera no coincide con los registros actuales")
        os.system("pause")
        os.system("cls")
        pass
    else:
        pass

def asignarProfesorMateria():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    flag = 3
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Nombre de la materia a la que desea asignar profesor: ")
            flag = 2
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    numero_empleado = int(input("Introduzca el número de empleado del profesor que va a asignar: "))
                    flag = 1
                    for prof in profesores:
                        if int(prof.getNoempleado()) == numero_empleado:
                            mat.setTitular(prof)
                            os.system("cls")
                            print("El profesor se asigno correctamente")
                            os.system("pause")
                            os.system("cls")
                            flag = 0
                            pass

    if flag == 1:
        os.system("cls")
        print("El número de empleado no coincide con ningún registro")
        os.system("pause")
        os.system("cls")
        pass
    elif flag == 2:
        os.system("cls")
        print("El nombre de la materia no coincide con los registros actuales")
        os.system("pause")
        os.system("cls")
        pass
    elif flag == 3:
        os.system("cls")
        print("La carrera no fue encontada")
        os.system("pause")
        pass
    else:
        pass