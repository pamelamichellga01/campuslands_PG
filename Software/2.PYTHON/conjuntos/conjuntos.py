#Conjuntos(set) en python
#Un conjunto es una coleccion sin elementos duplicados y sin orden especifico. 

conjunto={1,2,3,3,4}
print(conjunto) #{1,2,3,4}

#Union de conjuntos:
A= {1,2,3}
B={3,4,5}

print(A|B) #{1,2,3,4,5}

#Interceccion de conjuntos:
print(A&B) #{3}

#Diferencia:
print(A-B) #{1,2}