espacio=4
valor=0
queda=4
while True:
    print('''--------------------ADMINISTRADOR PARQUEADERO----------------------------
          1. Ingresar auto
          2. Retirar auto
          3. Salir del programa
          ''')
    
    opcion=int(input("Que opcion desea?"))
    if valor== espacio:
        print("El parqueadero no cuenta con espacios disponibles")
        break
    if opcion == 3:
        break
    elif opcion == 1:
        valor+=1
        queda-=1
        print(f"Auto ingresado, quedan {queda} espacios")
    elif opcion == 2:
        if valor==0:
            print("El parqueadero esta vacio, no puedes sacar ningun auto")
        elif valor != 0:
            print(f"Auto retirado, quedan {queda} espacios")
        valor-=1
             
print("Saliendo del parqueadero")