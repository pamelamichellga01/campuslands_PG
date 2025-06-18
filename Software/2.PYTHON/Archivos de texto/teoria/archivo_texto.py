#-----------------------------------------------------------------------------------------------------metodo1
# archivo = open ("miArchivo.txt","r")

# contenido = archivo.read()

# print(contenido)

# archivo.close()

# archivo_lec = open ("miArchivo.txt","w") #Sobreescribir, borra lo que se tienen y escribe lo nuevo
# archivo_lec.write("Titulo\n")
# archivo_lec.write("Sub-Titulo")
# archivo_lec.close()

#--------------------------------------------------------------------------------------------------------metodo2

# with open("miArchivo.txt","r+") as archivo:
#     contenido = archivo.read()
#     print(contenido)
#     archivo.write("\nNueva liena en el archivo de texto:) ")

#--------------------------------------------------------------------------------------------------------metodo3

# with open("miArchivo.txt","r") as archivo:
#     # contenido = archivo.read()}
#     for linea in archivo:
#         print(linea.strip())
#     #archivo.write("\nNueva liena en el archivo de texto:) ")

#--------------------------------------------------------------------------------------------------------metodo2