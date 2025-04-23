# WHILE: Una maquina expendedora permite comprar cafe por $10. Un usuario debe ingresar dinero hasta alanzar el momento exacto.
monto_total=10
valor=0
while True:
    monto= int(input("Ingrese el dienro: "))
    valor += monto

    if valor== monto_total:
        print("Preparando su cafe")
        break
    elif valor < monto_total:
        saldo = monto_total-valor
        print(f"Siga depositando dinero. Faltan ${saldo}")
    elif valor > monto_total:
        saldo = valor-monto_total
        print(f"Te sobran ${saldo}")
        if valor>=monto_total:
            print("Preparando tu cafe")
            break
    