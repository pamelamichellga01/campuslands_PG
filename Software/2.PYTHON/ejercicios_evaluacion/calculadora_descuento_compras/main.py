from calculadora_descuento_compras.service_caluladora import calcular_descuento,calcular_total_con_descuento, dividir_total, mostrar_resultados

def main():
    precio=float(input("\n Ingrese el preico total del producto: $"))
    porcentaje=float(input("\n Ingrese el porcentaje del descuento: "))

    descuento= calcular_descuento(precio,porcentaje)
    total= calcular_total_con_descuento(precio, descuento)

    dividir = input("\n ¿Desea dividir el pago entre varias personas? (s/n)").lower()

    if dividir=="s":
        persona=int(input("\n ¿Entre cuantas personas se dividira el pago?"))
        total_persona=dividir_total(total,persona)

        mostrar_resultados(descuento, total, total_persona)
    elif dividir=="n":
        mostrar_resultados(descuento, total)
    else:
        print("opcion incorrecta")    

main()