#4.​ Crea una función que calcule la potencia de un número dada una base y un exponente.

print("Digite su base: ")
base=int(input())
print("Digite su exponente: ")
expo=int(input())

def potencia(b,e):
    return f"El resultado de la potencia con base {b} y exponente {e} es {b**e}"

print(potencia(base,expo))

