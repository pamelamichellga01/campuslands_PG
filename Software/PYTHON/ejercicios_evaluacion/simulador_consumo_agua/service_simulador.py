def calcular_costo_base(consumo_m3, tarifa_m3):
    return (consumo_m3*tarifa_m3)

def calcular_impuesto(costo_base, porcentaje):
    return (costo_base*porcentaje)/100

def calcular_total(costo_base, impuesto):
    return costo_base+impuesto

def dividir_total(total, personas):
    if personas>0:
        return total/personas
    else:
        return total

def mostrar_resultados(impuesto, total, total_persona=None):
    print("---------------------------------------------------")
    print(f"Impuesto Ambienta: ${impuesto:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    if total_persona is not None:
        print(f"Cada persona debe pagar ${total_persona:.2f}")
    print("---------------------------------------------------")