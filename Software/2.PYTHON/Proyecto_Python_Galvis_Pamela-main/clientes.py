from utils import cargar_datos_json, guardar_datos_json

RUTA_CLIENTES = 'data/clientes.json'

def registrar_cliente():
    clientes = cargar_datos_json(RUTA_CLIENTES)

    identificacion = input("Ingrese el número de identificación del cliente: ")
    for cliente in clientes:
        if cliente['identificacion'] == identificacion:
            print("\n El cliente ya está registrado.")
            return

    cliente = {
        "nombres": input("Ingrese nombres: "),
        "apellidos": input("Ingrese apellidos: "),
        "identificacion": identificacion,
        "tipo_identificacion": input("Ingrese tipo de identificación (CC, TI, CE): "),
        "direccion": input("Ingrese dirección: "),
        "telefono_fijo": input("Ingrese teléfono fijo: "),
        "celular": input("Ingrese número celular: "),
        "barrio": input("Ingrese barrio de residencia: ")
    }

    clientes.append(cliente)
    guardar_datos_json(RUTA_CLIENTES, clientes)
    print("\n Cliente registrado exitosamente.")

def actualizar_cliente():
    clientes = cargar_datos_json(RUTA_CLIENTES)
    identificacion = input("Ingrese la identificación del cliente a actualizar: ")

    for cliente in clientes:
        if cliente['identificacion'] == identificacion:
            print("\nCliente encontrado. Ingrese la nueva información:")
            cliente['direccion'] = input("Nueva dirección: ")
            cliente['telefono_fijo'] = input("Nuevo teléfono fijo: ")
            cliente['celular'] = input("Nuevo número celular: ")
            cliente['barrio'] = input("Nuevo barrio: ")
            guardar_datos_json(RUTA_CLIENTES, clientes)
            print("\n Información actualizada correctamente.")
            return

    print("\n Cliente no encontrado.")
