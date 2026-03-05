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

    for emp in empanadas:
        print(f"{emp['nombre']} - ${emp['precio']}")

    nombre_buscar = input("Ingrese el nombre de la empanada a editar: ")

    for emp in empanadas:
        if emp["nombre"].lower() == nombre_buscar.lower():

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = input("Nuevo precio: ")

            emp["nombre"] = nuevo_nombre
            emp["precio"] = nuevo_precio

            guardar_empanadas(empanadas)

            print("Empanada actualizada.")
            return
    print("Empanada no encontrada.")

def eliminar_empanada():
    empanadas = cargar_empanadas()

    if len(empanadas) == 0:
        print("No hay empanadas registradas.")
        return

    print("\nEmpanadas disponibles:")
    for emp in empanadas:
        print(f"{emp['nombre']} - ${emp['precio']}")

    nombre_buscar = input("Ingrese el nombre de la empanada a eliminar: ")

    for emp in empanadas:
        if emp["nombre"].lower() == nombre_buscar.lower():
            empanadas.remove(emp)
            guardar_empanadas(empanadas)
            print("Empanada eliminada correctamente.")
            return

    print("Empanada no encontrada.")

def salir():
    print("Gracias por usar el sistema.")