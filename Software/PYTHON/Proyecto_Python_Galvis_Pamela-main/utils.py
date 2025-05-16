import random
import string
import datetime


def generar_numero_guia():
    
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def obtener_fecha_hora_actual():
    
    ahora = datetime.datetime.now()
    return ahora.date().isoformat(), ahora.time().strftime('%H:%M:%S')


def cargar_datos_json(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            import json
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar_datos_json(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        import json
        json.dump(datos, archivo, indent=4, ensure_ascii=False)