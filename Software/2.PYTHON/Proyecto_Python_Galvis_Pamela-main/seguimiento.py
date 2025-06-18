from utils import cargar_datos_json
import random

RUTA_ENVIOS = 'data/envios.json'

def buscar_envio():
    numero_guia = input("Ingrese el número de guía: ")
    envios = cargar_datos_json(RUTA_ENVIOS)

    for envio in envios:
        if envio['numero_guia'] == numero_guia:
            distancia_total = 1000 
            km_recorridos = random.randint(0, distancia_total)

            if km_recorridos <= 50:
                estado = "Recibido"
            elif km_recorridos <= 200:
                estado = "En tránsito"
            elif km_recorridos <= 500:
                estado = "En ciudad destino"
            elif km_recorridos <= 700:
                estado = "En bodega de la transportadora"
            elif km_recorridos <= 999:
                estado = "En reparto"
            else:
                estado = "Entregado"

            print("\n Información del envío:")
            print(f"Estado: {estado}")
            print(f"Fecha de envío: {envio['fecha_envio']}")
            print(f"Hora de envío: {envio['hora_envio']}")
            print(f"Destino: {envio['destinatario']['ciudad']}, {envio['destinatario']['direccion']}")
            print(f"Kilómetros recorridos: {km_recorridos} km")
            return

    print("\n No se encontró ningún envío con ese número de guía.")
