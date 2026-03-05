import json

ARCHIVO = "empanadas.json"
def cargar_empanadas():
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except:
        return []