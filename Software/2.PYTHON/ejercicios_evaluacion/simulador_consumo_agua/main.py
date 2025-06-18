from service_simulador import calcular_costo_base, calcular_impuesto,calcular_total,dividir_total,mostrar_resultados

def main():
    consumo_m3=float(input("Digite el consumo de guan en m3: "))
    tarifa_m3=float(input("Digite la tafifa fija: $"))

    costo_base=calcular_costo_base(consumo_m3, tarifa_m3)
    porcentaje=float(input("Digite el porcentaje del impuesto a pagar: "))
    
    impuesto=calcular_impuesto(costo_base,porcentaje)
    total= calcular_total(costo_base,impuesto)

    dividir = input("\n ¿Desea dividir el pago entre varias personas? (s/n)").lower()
    if dividir =="s":
        persona=int(input("\n ¿Entre cuantas personas se dividira el pago?: "))
        total_persona=dividir_total(total,persona)

        mostrar_resultados(impuesto,total,total_persona)
    else:
        mostrar_resultados(impuesto,total)

main()