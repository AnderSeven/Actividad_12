def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]
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
        cantidad = int(input("Ingrese la cantidad de paquetes entregados: "))
        zona = input("Zona del empleado: ")
        mensajeria[nombre] = cantidad, zona

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
        case 3:
        case 4:
        case 5:
            print("Gracias por usar el sistema")
        case _:
            print("Opcion invalida")