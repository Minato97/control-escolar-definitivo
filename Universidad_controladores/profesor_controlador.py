
from Universidad_modelos.profesor_modelo import *
from Universidad_modelos.carrera_modelo import *
import os



def registrarProfesor():
    numero_empleado = int(input("Introduce el número de empleado:"))
    if len(profesores) != 0:
        for prof in profesores:
            if int(prof.getNoempleado()) == numero_empleado:
                print("El profesor {} ya existe".format(prof.getProfesor()))
                os.system("pause")
                os.system("cls")
                pass
            else:
                print("Ingresa los siguientes datos del profesor: ")
                profesor = Profesor(numero_empleado)
                # profesor.setNoempleado((input("Número de empleado: ")))
                profesor.setNombre(input("\nNombre: "))
                print("\nFecha de ingreso")
                anio = int(input("Año: "))
                mes = int(input("Mes: "))
                dia = int(input("Dia: "))
                profesor.setFechaingreso(date(anio, mes, dia))
                profesores.append(profesor)
                os.system("cls")                
                print("Profesor registrado exitosamente")
                os.system("pause")
                os.system("cls")
                pass
    else:
        print("Ingresa los siguientes datos del profesor: ")
        profesor = Profesor(numero_empleado)
        # profesor.setNoempleado((input("Número de empleado: ")))
        profesor.setNombre(input("\nNombre: "))
        print("\nFecha de ingreso")
        anio = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Dia: "))
        profesor.setFechaingreso(date(anio, mes, dia))
        profesores.append(profesor)
        os.system("cls")
        print("Profesor registrado exitosamente")
        os.system("pause")
        os.system("cls")
        pass

def listarMateriasImpartidas():
    numero_empleado = int(input("Introduzca el número de empleado del profesor que desea listar sus materias impartidas: "))
    for prof in profesores:
        if int(prof.getNoempleado()) == numero_empleado:
            os.system("cls")
            print("Las materias que imparte el profesor ",prof.getProfesor()," son: ")
            for carr in carreras:
                for mat in carr.getMaterias():
                    if mat.getTitular().getNoempleado() == numero_empleado:
                        print(mat.getMateria())
                        os.system("pause")
                        os.system("cls")
                        pass
        else:
            os.system("cls")
            print("El número de empleado no coincide con ningún registro")
            os.system("pause")
            os.system("cls")
        pass
