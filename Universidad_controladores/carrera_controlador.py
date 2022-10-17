from distutils.log import error
from Universidad_modelos.carrera_modelo import *
from Universidad_modelos.materia_modelo import *
from Universidad_modelos.alumno_modelo import *
from datetime import date

import os

def registrarCarreras():
    nombre_carrera = (input("Introduce el nombre de la carrera:"))
    if len(carreras) != 0:
        flag = False
        for carr in carreras:
            if carr.getCarrera() == nombre_carrera:
                print("El nombre {} ya existe, introduce uno distinto".format(nombre_carrera))
                os.system("pause")
                os.system("cls")
                flag = True
                pass
        if flag == False:
            carrera = Carrera(nombre_carrera)
            carreras.append(carrera)
            os.system("cls")
            print("Carrera registrada correctamente")
            os.system("pause")
            os.system("cls")
            pass
    else:
        carrera = Carrera(nombre_carrera)
        carreras.append(carrera)
        os.system("cls")
        print("Carrera registrada correctamente")
        os.system("pause")
        os.system("cls")
        pass

def registrarMateriasCarrera():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    flag = 1
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            nombre_materia = input("Introduce el nombre de la materia: ")
            flag = 2
            for mat in carr.getMaterias():
                if mat.getMateria() == nombre_materia:
                    print("La materia ",nombre_materia," ya existe en la carrera ",nombre_carrera, " no es necesario registrarla de nuevo")
                    os.system("pause")
                    os.system("cls")
                    flag = 0
                    pass
            if flag == 2:
                nueva_materia = Materia(nombre_materia)
                carr.setMaterias(nueva_materia)
                os.system("cls")
                print("Materia registrada correctamente")
                os.system("pause")
                os.system("cls")
                pass

    if flag == 1:
        os.system("cls")
        print("La carrera no fue encontada, no es posible registrar materias.")
        os.system("pause")
        os.system("cls")
        pass
    else:
        pass


def listarMateriasCarrera():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    flag = False
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            carr.listarMaterias(carr)
            os.system("pause")
            os.system("cls")
            flag = True
            pass
    if flag == False:
        os.system("cls")
        print("La carrera no fue encontada, no es posible registrar materias.")
        os.system("pause")
        os.system("cls")
        pass

def listarCarreras():
    if len(carreras) == 0:
        os.system("cls")
        print("No se tienen carreras registradas")
        os.system("pause")
        os.system("cls")
        pass
    else:
        os.system("cls")
        print("""      Las carreras existentes son: """)
        for carr in carreras:
            print(carr.getCarrera())
        os.system("pause")
        os.system("cls")
        pass

def registrarAlumnosCarrera():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    flag = 1
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            matricula_alumno = int(input("Introduzca el número de matricula del alumno: "))
            flag = 2
            for alum in carr.getAlumnosC():
                if int(alum.getMatricula()) == matricula_alumno:
                    print("El alumno", alum.getAlumno(), " ya existe en la carrera ", nombre_carrera," no es necesario registrarla de nuevo")
                    os.system("pause")
                    os.system("cls")
                    flag = 0
                    pass
            if flag == 2:
                print("Ingresa los siguientes datos del alumno: ")
                alumno = Alumno()
                alumno.setMatricula(matricula_alumno)
                alumno.setNombre(input("Nombre: "))
                print("\nFecha de nacimiento")
                anio = int(input("Año: "))
                mes = int(input("Mes: "))
                dia = int(input("Dia: "))
                alumno.setFechanacimiento(date(anio, mes, dia))
                print("\nFecha de registro")
                anio = int(input("Año: "))
                mes = int(input("Mes: "))
                dia = int(input("Dia: "))
                alumno.setFechaingreso(date(anio, mes, dia))
                alumno.setGenero(input("Genero (M/F): "))
                alumno.setCiudad(input("Ciudad de procedencia: "))
                carr.setAlumnosC(alumno)
                print("\n-----Alumno registrado exitosamente-----")
                os.system("pause")
                os.system("cls")
                flag = 0
                pass

    if flag == 1:
        os.system("cls")
        print("La carrera no fue encontada, no es posible registrar materias.")
        os.system("pause")
        os.system("cls")
        pass
    else:
        pass

def listarAlumnosCarrera():
    os.system("cls")
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    flag = False
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            carr.listarAlumnosC(carr)
            os.system("pause")
            os.system("cls")
            flag = True
            pass
    if flag == False:
        os.system("cls")
        print("La carrera no fue encontada, no es posible registrar materias.")
        os.system("pause")
        os.system("cls")
        pass

