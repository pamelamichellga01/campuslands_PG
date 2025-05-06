#Listas anidadas
#una lista que cintiene otra lista como elementos.

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(matriz)

# print(matriz[1][1])

# matriz[0][0]=10
# print(matriz)

#--------------------------------------------------------

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")