import json
import os
import getpass
import hashlib


# -------------------- FUNCIONES DE ARCHIVOS --------------------

def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

def cargar_productos():
    if os.path.exists("inventario.json"):
        with open("inventario.json", "r") as f:
            return json.load(f)
    return {}

def guardar_productos():
    with open("inventario.json", "w") as f:
        json.dump(productos, f, indent=4)

def cargar_usuarios():
    if os.path.exists("usuarios_admin.json"):
        with open("usuarios_admin.json", "r") as f:
            return json.load(f)
    return {}

def guardar_usuarios():
    with open("usuarios_admin.json", "w") as f:
        json.dump(usuarios_admin, f, indent=4)

# -------------------- INICIALIZACIÓN DE DATOS --------------------

productos = cargar_productos()
usuarios_admin = cargar_usuarios()

if not productos:
    productos = {
        'Poker': {"Precio": 6000, "Cantidad": 30},
        'Aguardiente': {"Precio": 21000, "Cantidad": 5},
        'Vodka': {"Precio": 45000, "Cantidad": 2}
    }
    guardar_productos()

if not usuarios_admin:
    usuarios_admin = {
        "admin": "1234",
        "justin": "yustin123",
        "sofia": "sofi2024"
    }
    guardar_usuarios()

# -------------------- MENÚ PRINCIPAL --------------------

def menu_principal():
    print("------ BIENVENIDO A LICORERÍA YUSTIN ------")
    print("1. Administrador")
    print("2. Comprador")
    print("3. Salir")

# -------------------- COMPRADOR --------------------

def mostrar_menu_comprador():
    print('----------LICORES YUSTIN--------------')
    print('1. Comprar\n2. Salir')

def mostrar_productos():
    print('---------PRODUCTOS DISPONIBLES----------')
    for clave, valor in productos.items():
        print(f"{clave} : Precio: {valor['Precio']} - Cantidad: {valor['Cantidad']}")

def validar_edad():
    edad = int(input("¿Qué edad tienes?: "))
    return edad >= 18

def procesar_compra():
    mostrar_productos()
    nombre = input('Ingrese el producto: ').title()

    if nombre not in productos:
        print("No hay, busque a Justin para que le consiga.")
        return

    cantidad = int(input('Ingrese la cantidad: '))

    if cantidad <= 0:
        print('Ingrese un número mayor a cero')
    elif productos[nombre]["Cantidad"] < cantidad:
        print("No hay producto suficiente. Justin resuelve.")
    else:
        total = cantidad * productos[nombre]["Precio"]
        print(f'El valor a pagar por el producto {nombre} es de {total} pesos por la cantidad de {cantidad} unidades.')
        productos[nombre]["Cantidad"] -= cantidad
        guardar_productos()
        print(f'Ahora la cantidad del producto {nombre} es {productos[nombre]["Cantidad"]}')

def modo_comprador():
    while True:
        mostrar_menu_comprador()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            if validar_edad():
                procesar_compra()
            else:
                print("No tienes edad para comprar bebidas alcohólicas. Yustin le vende bajo cuerda.")
                break
        elif opcion == 2:
            print("Gracias por visitar licores Yustin")
            break
        else:
            print("Opción no válida.")

# -------------------- ADMINISTRADOR --------------------

def menu_administrador():
    print("\n------ MODO ADMINISTRADOR ------")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def ver_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        mostrar_productos()

def agregar_producto():
    nombre = input("Ingrese el nombre del nuevo producto: ").title()
    if nombre in productos:
        print("Ese producto ya existe.")
    else:
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        productos[nombre] = {"Precio": precio, "Cantidad": cantidad}
        guardar_productos()
        print(f"{nombre} agregado correctamente.")

def modificar_producto():
    nombre = input("Ingrese el nombre del producto a modificar: ").title()
    if nombre not in productos:
        print("Ese producto no existe.")
    else:
        precio = int(input("Nuevo precio: "))
        cantidad = int(input("Nueva cantidad: "))
        productos[nombre] = {"Precio": precio, "Cantidad": cantidad}
        guardar_productos()
        print(f"{nombre} modificado correctamente.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").title()
    if nombre in productos:
        del productos[nombre]
        guardar_productos()
        print(f"{nombre} eliminado correctamente.")
    else:
        print("Ese producto no existe.")

def autenticar_admin():
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        clave = getpass.getpass("Contraseña: ")
        clave_encriptada = encriptar_contraseña(clave)

        if usuario in usuarios_admin and usuarios_admin[usuario] == clave_encriptada:
            print(f"Bienvenido, {usuario}.\n")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    print("Acceso denegado. Demasiados intentos.")
    return False

def modo_administrador():
    if not autenticar_admin():
        return

    while True:
        menu_administrador()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            ver_productos()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            print("Saliendo del modo administrador...")
            break
        else:
            print("Opción no válida.")

# -------------------- INICIAR PROGRAMA --------------------

def iniciar_programa():
    while True:
        menu_principal()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            modo_administrador()
        elif opcion == 2:
            modo_comprador()
        elif opcion == 3:
            print("Gracias por usar el sistema de Licores Yustin.")
            break
        else:
            print("Opción no válida.")

# Ejecutar programa
iniciar_programa()
