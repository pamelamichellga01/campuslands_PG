#Escribe una función que determine si un número es par o impar.

print("Ingresa un numero")

a=int(input())

def par_impar (num):
    
    if num%2==0:
        return (f"El numero {num} es par ")
    else:
        return (f"EL numero {num} es impar")

print(par_impar(a))