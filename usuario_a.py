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

def listar_empanadas():
    empanadas = cargar_empanadas()

    if len(empanadas) == 0:
        print("No hay empanadas registradas.")
        return

        
    for i, emp in enumerate(empanadas, start=1):
        print(f"{i}. {emp['nombre']} - ${emp['precio']}")        

def agregar_empanada():
    empanadas = cargar_empanadas()

    nombre = input("Nombre de la empanada: ")
    precio = input("Precio: ")

    nueva = {
        "nombre": nombre,
        "precio": precio
    }

    empanadas.append(nueva)
    guardar_empanadas(empanadas)

    print("Empanada agregada correctamente.")
