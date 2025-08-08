def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1] > pivote[1]]
    iguales = [x for x in lista if x[1] == pivote[1]]
    menores = [x for x in lista[1:] if x[1] < pivote[1]]
    return quick_sort(mayores) + iguales + quick_sort(menores)
mensajeria = {}

def ingreso_datos():
    c = int(input("Cuantos empleados desea registrar: "))
    for i in range(c):
        s = False
        while s == False:
            nombre = input("Ingrese el nombre: ")
            if nombre in mensajeria:
                print("El nombre ya esta en uso, ingrese otro")
            else:
                s = True
        s = False
        while s == False:
            cantidad = int(input("Ingrese la cantidad de paquetes entregados: "))
            if cantidad >= 0:
                s = True
            else:
                print("La cantidad debe de ser un numero entero positivo")
        zona = input("Zona del empleado: ")
        mensajeria[nombre] = {
            "paquetes": cantidad,
            "zona": zona
        }

def busqueda_secuencial(diccionario, objetivo):
    lista_nombres = list(diccionario.keys())
    for i in range(len(lista_nombres)):
        if lista_nombres[i].lower() == objetivo.lower():
            return i
    return -1

opciones = 0
a = False
while a == False:
    print("---Menu---")
    print("1. Ingreso de datos")
    print("2. Mostrar ranking")
    print("3. Busqueda")
    print("4. Estadisticas")
    print("5. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            ingreso_datos()
        case 2:
            if len(mensajeria) > 0:
                orden = quick_sort([(nombre, datos["paquetes"], datos["zona"]) for nombre, datos in mensajeria.items()])
                print("---Ranking de Empleados---")
                for nombre, paquetes, zona in orden:
                    print(f"{nombre} - {paquetes} paquetes - Zona: {zona}")
            else:
                print("No hay ningun empleado registrado")
        case 3:
            if len(mensajeria) > 0:
                buscado = input("Ingrese el nombre que desea buscar: ")
                indice = busqueda_secuencial(mensajeria, buscado)
                if indice != -1:
                    nombre = list(mensajeria.keys())[indice]
                    print(f"{nombre} entrego {mensajeria[nombre]['paquetes']} paquetes en la zona {mensajeria[nombre]['zona']}")
                else:
                    print("No hay ningun empleado con ese nombre")
            else:
                print("No hay empleados registrados")
        case 4:
            print("adsf")
        case 5:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")