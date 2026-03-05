import json

ARCHIVO = "empanadas.json"
def cargar_empanadas():
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_empanadas(empanadas):
    with open(ARCHIVO, "w") as archivo:
        json.dump(empanadas, archivo, indent=4)

def editar_empanada():
    empanadas = cargar_empanadas()

    for i, emp in enumerate(empanadas, start=1):
        print(f"{i}. {emp['nombre']} - ${emp['precio']}")

    opcion = int(input("Seleccione la empanada a editar: ")) - 1

    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_precio = input("Nuevo precio: ")

    empanadas[opcion]["nombre"] = nuevo_nombre
    empanadas[opcion]["precio"] = nuevo_precio

    guardar_empanadas(empanadas)

    print("Empanada actualizada.")

def eliminar_empanada():
    empanadas = cargar_empanadas()

    for i, emp in enumerate(empanadas, start=1):
        print(f"{i}. {emp['nombre']} - ${emp['precio']}")

    opcion = int(input("Seleccione la empanada a eliminar: ")) - 1

    empanadas.pop(opcion)

    guardar_empanadas(empanadas)

    print("Empanada eliminada.")

def salir():
    print("Gracias por usar el sistema.")