libros=[("El perfue","suskind","Misterio"),
       ("La Metamorfosis","kafka","novela"),
       ("Misery","Stephen King","Misterio")]

clasificacion=input("Ingrese el genero: ").title()
resultado=[libro[0] for libro in libros if libro[2]==clasificacion]

print(resultado if resultado else "No hay libros de ese genero")

# for libro in libros:
#    if(libro[2]==clasificacion):
#         resultado=[]
#         resultado.append([libro[0]])