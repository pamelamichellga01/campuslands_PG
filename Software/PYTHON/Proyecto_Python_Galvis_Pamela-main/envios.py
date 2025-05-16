from utils import cargar_datos_json, guardar_datos_json, generar_numero_guia, obtener_fecha_hora_actual

RUTA_CLIENTES = 'data/clientes.json'
RUTA_ENVIOS = 'data/envios.json'

ESTADOS_ENVIO = [
    "Recibido",
    "En Transito",
    "En Ciudad Destino",
    "En Bodega De La Transportadora",
    "En Reparto",
    "Entregado"
]

def registrar_envio():
    clientes = cargar_datos_json(RUTA_CLIENTES)
    envios = cargar_datos_json(RUTA_ENVIOS)

    remitente_id = input("Ingrese el número de identificación del remitente: ")
    remitente = next((c for c in clientes if c['identificacion'] == remitente_id), None)

    if remitente is None:
        print("\n Remitente no registrado. Debe registrarlo primero.")
        return

    destinatario = {
        "nombre": input("Nombre del destinatario: "),
        "direccion": input("Dirección del destinatario: "),
        "telefono": input("Teléfono del destinatario: "),
        "ciudad": input("Ciudad del destinatario: "),
        "barrio": input("Barrio del destinatario: ")
    }

    fecha_envio, hora_envio = obtener_fecha_hora_actual()
    numero_guia = generar_numero_guia()

    envio = {
        "numero_guia": numero_guia,
        "fecha_envio": fecha_envio,
        "hora_envio": hora_envio,
        "destinatario": destinatario,
        "remitente_id": remitente_id,
        "estado": "Recibido"
    }

    envios.append(envio)
    guardar_datos_json(RUTA_ENVIOS, envios)
    print(f"\n Envío registrado exitosamente. Número de guía: {numero_guia}")
