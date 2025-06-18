def calcular_descuento(precio, porcentaje):
    return (precio*porcentaje)/100

def calcular_total_con_descuento(precio, descuento):
    return precio - descuento

def dividir_total(total, personas):
    if personas >0:
        return total/personas
    else:
        return total
    
def mostrar_resultados(descuento, total, total_persona=None):
    print("---------------------------------------------------")
    print(f"Monto de descuento: ${descuento:.2f}")
    print(f"Total a pagar con el decuento: ${total:.2f}")
    if total_persona is not None:
        print(f"Cada persona debe pagar ${total_persona:.2f}")
    print("---------------------------------------------------")
