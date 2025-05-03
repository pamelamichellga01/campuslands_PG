estudiantes = []

def registrar_estudiante():
    print('--------REGISTRO DE ESTUDIANTES---------')

    nombre = input("Ingrese el nombre del estudiante: ").title()
    edad = int(input("Ingreses la edad del estudiante: "))
    curso = input("Ingrese el curso del estudiante: ").title()

    tupla = (nombre,edad,curso)

    estudiantes.append(tupla)

    print('Estudiante registrado exitosamente\n\n')

def mostrar_estudiante():
    if not estudiantes:
        print("No hay estudiantes registrados.\n\n")
    else:
        print(f"{'N°':<3} | {'NOMBRE':<10} | {'EDAD':<4} | {'CURSO':<10}")
        for i, estudiante in enumerate(estudiantes):
            print(f"{i+1:<3} | {estudiante[0]:<10} | {estudiante[1]:<4} | {estudiante[2]:<10}")
        print('\n')


def buscar_estudiante():
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ").title()
    encontrados = [est for est in estudiantes if est[0] == nombre_buscar]
    if encontrados:
        for est in encontrados:
            print(f"Encontrado: Nombre: {est[0]}, Edad: {est[1]}, Curso: {est[2]}")
    else:
        print("Estudiante no encontrado.")
    print('\n')

def mostrar_cursos_unicos():
    cursos = {est[2] for est in estudiantes}

    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("Cursos únicos inscritos:")
        for curso in cursos:
            print(f"- {curso}")
        print("\n")


def menu_principal():    
    while True:
        print('-------SISTEMA DE REGISTRO DE ESTUDIANTES------------')
        print('1. Registrar estudiante\n2. Estudiantes registrados\n3. Buscar estudiante por nombre\n4. Mostrar cursos\n0. Salir')

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 0:
            print('Gracias por utilizar el sistema de registro.')
            break
        elif opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            mostrar_estudiante()
        elif opcion == 3:
            buscar_estudiante()
        elif opcion == 4:
            mostrar_cursos_unicos()
        else:
            print(f'la opcion {opcion} no es valida. Intente de nuevo.\n')

menu_principal()

