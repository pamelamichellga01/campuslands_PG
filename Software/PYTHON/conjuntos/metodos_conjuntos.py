#METODOS CONJUNTOS 

#add(valor)->Agrega un elemento al conjunto 
conjunto={1,2,3}
conjunto.add(4)
print(conjunto) #{1,2,3,4}

#remove(valor) -> Elimina un elemento (da error si no existe)

conjunto={1,2,3}
conjunto.remove(2)
print(conjunto) #{1,3}

#discard(valor)->Elimina un elemento sin error si no existe
conjunto={1,2,3}
conjunto.discard(5) #no da error

#pop()-> Elimina y devuleve un elemento aleatorio 
conjunto={1,2,3}
print(conjunto.pop()) #puede devolver 1 , 2 o 3

#crear() -> vacia el conjunto
conjunto={1,2,3}
conjunto.clear()
print(conjunto) #set()

#union(set2) -> ine dos conjuntos
A={1,2,3}
B={3,4,5}
print(A.union(B)) #{1,2,3,4,5}
#intersection(set2) -> Devuleve la interseccion
print(A.intersection(B)) #{3}

#difference(set2) -> Elementos que estan en A, pero no en B
print(A.difference(B)) #{1,2}
