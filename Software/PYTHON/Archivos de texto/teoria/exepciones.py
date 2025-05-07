while True:
    try:
        try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero"))
            resultado= num1/num2
            print("Resultado:",resultado)
        except ValueError:
            print("Error Debes ingresar solo valores numerios enteros")
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")