import csv

with open("archivo_de_comas.csv","w", newline="") as archivo:
    escritor =csv.writer(archivo)

    escritor.writerow(["Nombre","Edad","Ciudad"])
    escritor.writerow(["Ana",25,"Madrid"])
    escritor.writerow(["Luis",30,"Barcelona"])
    escritor.writerow(["Sofia",22,"Valencia"])

    print('Informacion modificada.\n\n')

with open("archivo_de_comas.csv","r")as archivo2:
    lector = csv.reader(archivo2)

    for linea in lector:
        print(','.join(linea))

with open("archivo_de_comas.csv","r")as archivo3:
    lector=csv.DictReader(archivo3)

    for fila in lector:
        print(f'{fila["Nombre"]}, tiene {fila["Edad"]} años y vive ne la ciudad {fila["Ciudad"]}')