#
contador = 3
while True:
    print("--------------------CAJERO AUTOMATICO--------------------------")
    print('''1. Consultar saldo
      2. Depositar dinero
      3. Retirar dinero
      4. Salir''')
    
    opcion=int(input("Que opcion desea?"))

    if opcion == 4:
        break
    elif opcion == 1:
        print("su saldo es: 5000")
    elif opcion == 2:
        print("Dinero depositado")
    elif opcion == 3:
        print("Dinero retirado")
    elif opcion < 1 or opcion > 4:
        contador -=1
        if contador == 0:
            break
        print("0pcion no valida")
             
print("Saliendo del cajero")