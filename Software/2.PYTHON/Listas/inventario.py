# EJERCICIO
# Crea un programa que gestione el inventario de una tienda con las siguientes operaciones:
# 1.Agregar un produto con nombre y cantidad.
# 2.Actualiza la cantidad de un producto.
# 3.Eliminar un producto.
# 4.Mostrar el inventario.
# 5.Salir.

productos=["manzana","pera","sandia","papaya"]
cantidad=["6","5","4","3"]
nombre_tienda = "TIENDA WICHO"

while True:
    print(f""""------------------{nombre_tienda}------------------------
    1.Agregar un produto con nombre y cantidad.
    2.Actualiza la cantidad de un producto.
    3.Eliminar un producto.
    4.Mostrar el inventario.
    0.Salir.\n""")

    opcion = int(input("Selecione una opcion: "))
    if(opcion==0):
        print(f"Gracias por utilizar el sistema de {nombre_tienda}")
        break
    elif(opcion==1):
        producto=input("Nombre del producto: ").lower()
        cantidad_producto = int(input("Cantidad del producto: "))

        productos.append(productos)
        cantidad.append(cantidad_producto)

        print("Producto agregado exitosamente!!!")

    elif(opcion==2):
        print("Lista de productos: ")
        for producto in productos:
            print(producto)

        producto_buscado = input("Que producto quiere actualizar: ").lower()
        posicion = productos.index(producto_buscado)
        actualizar_cantidad = int(input("Ingrese la nueva actidad: "))

        cantidad[posicion]=actualizar_cantidad
        print(f"la cantidad del producto {producto[posicion]} ahora es: {cantidad[posicion]}\n")
    
    elif(opcion==3):
        print("Lista de productos: ")
        for producto in productos:
            print(producto)

        producto_buscado = input("Que producto quiere eliminar: ").lower()
        posicion = productos.index(producto_buscado)
        
        productos.pop(posicion)
        cantidad.pop(posicion)

        print(f"El producto eliminado fue {producto_buscado}\n")

    elif(opcion==4):
        print("Lista de productos: ")
        count=0
        for producto in productos:
            print(f"{producto} : {cantidad[count]}")
            count+=1
    else:
        print("opcion no valida, intente de nuevo. ")
