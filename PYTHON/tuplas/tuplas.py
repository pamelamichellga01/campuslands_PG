# Tuplas en python
# ¿Que es una tupla?
# Una tupla es una estructura de datos similar a una lista, pero inmutable(no se puede modificar despues de su creacion). Se usa cuando queremos 
# asegurarnos de que los datos no cambie.

tupla=(1,2,3,"hola")
print(tupla)

#Acceso a elementos:
print(tupla[0])

#Convension de listas a tuplas:
lista=[1,2,3]
tupla1=tuple(lista)
print(tupla1)

#Desempaquetado
x,y,z, mensaje=tupla1
print(mensaje)
