#4.​ Crea una función que calcule la potencia de un número dada una base y un exponente.

print("Digite una base: ")
base=int(input())

print("Digite un exponente: ")
exponente=int(input())

def potencia (b,e):
    pot=1
    for i in range(e):
        pot*=b
    return f"La potencia con base {b} y exponente {e} es: {pot}"

print(potencia(base,exponente))
