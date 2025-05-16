from clientes import registrar_cliente, actualizar_cliente
from envios import registrar_envio
from seguimiento import buscar_envio

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar cliente")
        print("2. Actualizar cliente")
        print("3. Registrar envío")
        print("4. Consultar estado de envío")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            actualizar_cliente()
        elif opcion == '3':
            registrar_envio()
        elif opcion == '4':
            buscar_envio()
        elif opcion == '5':
            print("\n Programa finalizado.")
            break
        else:
            print("\n Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
