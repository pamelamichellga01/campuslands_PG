#Listas de edades

edades =[16,17,20,22,23,25,26,28,30,50,50,50]

print(f"Lista original{edades}")

edades.append(35)

# print(f"Lista append: {edades}")

edades.insert(2,18)

# print(f"Lista insert: {edades}")

count=edades.count(50)

# print(f"conteo: {count}")

edades.remove(50)

# print(f"Lista remove: {edades}")

print(edades.index(25))

edades.pop(6)

print(f"Lista pop: {edades}")

edades.sort()
print(f"Lista creciente: {edades}")

palabras=["palabra", "palabras", "mas palabras"]
palabras.sort()
print(f"Lista creciente: {palabras}")

edades.reverse()
print(f"Lista en reversa: {edades}")

edades.sort(reverse=True)
print(f"Lista creciente: {palabras}")

# edades.clear()
# print(f"Lista limpia: {edades}")

edades_temporales=edades.copy()
print(f"Lista temporal copiada: {edades_temporales}")