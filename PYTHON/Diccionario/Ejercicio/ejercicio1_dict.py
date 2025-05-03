# Definición de funciones

def menu_sistema():
    print('----------SISTEMA USUARIOS LICORES YUSTIN----------')
    print('1. Administrador')
    print('2. Cliente')
    print('3. No tengo cuenta')
    print('4. Salir')

def menu_user():
    print('----------LICORES YUSTIN--------------')
    print('1. Comprar\n2. Salir')

def menu_admin():
    print('----------ADMIN - LICORES YUSTIN----------')
    print('1. Crear producto nuevo')
    print('2. Mostrar todos los productos')
    print('3. Actualizar un producto')
    print('4. Eliminar un producto')
    print('5. salir')

def comprar_producto(): 
    print('---------PRODUCTOS DISPONIBLES----------')
    for clave,valor in productos.items():
        print(clave,":",valor)
    nombre = input('Ingrese el producto: ').title()

    if nombre not in productos:
        print("No hay, busque a Justin para que le consiga.")
    else:
        cantidad = int(input('Ingrese la cantidad: '))

        if cantidad <= 0:
            print('Ingrese un numero mayor a cero')
        elif productos[nombre]["Cantidad"] < cantidad:
            print("No hay producto suficiente. Justin resuelve.")
        else:
            total = cantidad * productos[nombre]["Precio"]
            print(f'El valor a pagar por el producto {nombre} es de {total} pesos por la cantidad de {cantidad} unidades.')

            productos[nombre]["Cantidad"] -= cantidad

            print(f'Ahora la cantidad del producto {nombre} es {productos[nombre]["Cantidad"]}')


# Código principal

# Definicion

usuarios ={
    'Luis':{"Admin"},
    'Pamela':{"User"},
    'Natasha':{"User"}
}
productos ={
    'Poker':{"Precio":6000,"Cantidad":30},
    'Aguardiente':{"Precio":21000,"Cantidad":5},
    'Vodka':{"Precio":45000,"Cantidad":2}
    }

# Logica

while True:

    menu_sistema()
    opcion=int(input("Seleccione una opcion: "))

    if opcion== 1:
        print("hola")
    elif opcion== 2:
        while True:

            menu_user()
            opcion=int(input("Seleccione una opcion: "))

            if opcion == 1:
                edad = int(input("Que edad tienes: "))

                if edad >= 18:
                    comprar_producto()
                else:
                    print("No tienes edad para comprar bebidas alcoholicas. Yustin le vende bajo cuerda.")
                    break
            elif opcion == 2:
                print("Gracias por visitar licores Yustin")
            else:
                print("Opcion no valida.")
