# Función para calcular cuántos litros se necesitan
def calcular_litros_necesarios(distancia, rendimiento):
    return distancia / rendimiento

# Función para calcular el costo total del combustible
def calcular_costo_combustible(litros, precio_litro):
    return litros * precio_litro

# Función para dividir el total entre personas
def dividir_total(total, personas):
    if personas > 0:
        return total / personas
    else:
        return total  # Evita división por cero

# Función para mostrar los resultados
def mostrar_resultados(litros, total, total_persona=None):
    print(f"\nLitros necesarios: {litros:.2f} L")
    print(f"Costo total del combustible: ${total:.2f}")
    if total_persona is not None:
        print(f"Cada persona debe pagar: ${total_persona:.2f}")

# Programa principal
def main():
    distancia = float(input("Ingresa la distancia total del viaje (km): "))
    rendimiento = float(input("Ingresa el rendimiento del vehículo (km/l): "))
    precio_litro = float(input("Ingresa el precio por litro de gasolina: $"))

    litros = calcular_litros_necesarios(distancia, rendimiento)
    total = calcular_costo_combustible(litros, precio_litro)

    dividir = input("¿Deseas dividir el costo entre los viajeros? (s/n): ").lower()
    if dividir == 's':
        personas = int(input("¿Cuántas personas viajarán?: "))
        total_persona = dividir_total(total, personas)
        mostrar_resultados(litros, total, total_persona)
    else:
        mostrar_resultados(litros, total)

# Ejecutar el programa
main()