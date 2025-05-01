"""REVIEW
Descripcion:
Se debe desarrollar un programa en python que permita gestionar un alista de 
estudiantes, almacenando su informcion en tupla y utilizando conjusnrtos para
analizar los cursos inscritos.

Objetivo:
Aplicar listas, tuplas y conjuntos en un mismo ejercicio, permitiendo realizar
operaciones basicas como agregar estudiantes, buscar informacion y analizar cursos.

Instrucciones:
1. Crea un programam en pythoin que haga lo sguiente:

2. Registrtar estudiantes:
    -Cada estudianre se representara con un atupla que almacene:(nombre,edad,curso_inscrito)
    -Los estudantes se guradaran en un alista

3. Mostrar la lista de estudiantes registrados.

4. Buscar un estudiante por nombre y mostrar su informacion.

5. Mostrar los cursos unicos a los que estan isncritos los estudiantes(sin repetir) usando un ocnjunto. 

Pista para desarrollar el ejercicio:
    -Usa un alista para almacenar los estudiantes.
    -Cada estudante debe ser una tupla con su infromacion
    -Usa un conjunto para obtener los cursos sin repetir 
    -Usa un bucle while para le menu interatvo
    -Usa condicionaeles (if) para cada operacion del menu. 
"""


estudiantes=[]

tupla=("Estudiante 1",25,"sofware")

estudiantes.append(tupla)

def registrar_estudiante():
    print("-----------------REGISTRO DE ESTUDIANTES-------------------")

    nombre = input("Ingrese el nombre del estudiante: ").title
    edad= int(input("Ingrese la edad del estudiante: "))
    curso_inscrito=input("Ingrese el curso del estudiante: ").title