mesajeria = {}

def ingreso_datos():
    c = int(input("Cuantos empleados desea registrar: "))
    for i in range(c):
        nombre = input("Ingrese el nombre: ")
        cantidad = int(input("Ingrese la cantidad de paquetes entregados: "))
        zona = input("Zona del empleado: ")


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