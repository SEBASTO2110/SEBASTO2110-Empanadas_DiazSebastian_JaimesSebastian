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

