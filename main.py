from usuario_a import listar_empanadas, agregar_empanada
from usuario_b import editar_empanada, eliminar_empanada, salir

def menu():
    while True:
        print("\n--- MENÚ EMPANADAS DOÑA PEPA ---")
        print("1. Listar empanadas")
        print("2. Agregar empanada")
        print("3. Editar empanada")
        print("4. Eliminar empanada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_empanadas()

        elif opcion == "2":
            agregar_empanada()

        elif opcion == "3":
            editar_empanada()

        elif opcion == "4":
            eliminar_empanada()

        elif opcion == "5":
            salir()
            break

        else:
            print("Opción inválida")


menu()