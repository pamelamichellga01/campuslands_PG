capacidad_maxima=10
espacios_ocupados=0

print("Bienvenido al simulador de parqueadero !!!")
print(f"La capacidad actual es de {capacidad_maxima} autos")

while True:
    print('''1. Ingresar Autos
          2. Retirar auto
          3. Espacios disponibles
          4. salir''')
    
    opcion= int(input('Que acion desea realizar'))

    if opcion == 1:
        if espacios_ocupados < capacidad_maxima:
            espacios_ocupados +=1
            espacio=capacidad_maxima - espacios_ocupados
            print('Bienvenido al estacionamiento mala vida !!')
            print(f"AHora la capacidad esta disponible para {espacio} autos")
        else:
            print("No hay espacios disponibles")
    elif opcion == 2:
        if espacios_ocupados>0:
            espacios_ocupados-=1
            espacio=capacidad_maxima-espacios_ocupados
            print("vuelva pronto")
            print(f"Ahora la capacidad esta disponible para {espacio} autos")
        else: 
            print("No hay autos registrados ene l parqueadero")
    elif opcion == 3:
        espacio = capacidad_maxima - espacios_ocupados
        print(f"La capacidad disponible para {espacios} auto")
    elif opcion ==4:
        print("Saliendo del sistema del parqueadero mala vida.")
        break
    else:
        print("opcion no valida")