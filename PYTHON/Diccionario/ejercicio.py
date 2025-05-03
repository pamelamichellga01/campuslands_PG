#

productos = {'Poker':{"Precio":3000,"Cantidad":30},
             'Aguardiente':{"Precio":21000,"Cantidad":5},
             'Vodka':{"Precio":45000,"Cantidad":2}
             } 

edad = int(input("Que edad tiene: "))

if edad >= 18:

    print('---------------PRODUCTOS DISPONIBLES--------------------')
    for clave,valor in productos.items():
        print(clave,":",valor)
    nombre = input('Ingrese el producto: ').title()

    if nombre not in productos:
        print("No hay, busque a justin ára que le consiga")
    else:
        cantidad = int(input('INgrese la cantidad '))

        if cantidad <= 0:
            print('Ingrese un numero mayor a cero')
        elif productos[nombre]["Cantidad"]<cantidad:
            print("No hay producto suficinte. Justin resuelve.")
        else:
            total = cantidad * productos[nombre]["Precio"]

            print(f'El valor a pagar por el producto {nombre} es de {total} peso por la cantidad de {cantidad}')

else:
    print("No tienes edad para comprar bebidas alcohol")