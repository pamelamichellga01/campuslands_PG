import os
import json
# -------------------- FUNCIONES DE ARCHIVOS --------------------

def cargar_compras():
    if os.path.exists("Compras.json"):
        with open("Compras.json","r") as f:
            return json.load(f)
    return{}
#print(cargar_compras())

def cargar_empleados():
    if os.path.exists("Empleados.json"):
        with open("Empleados.json","r") as f:
            return json.load(f)
    return{}
#print(cargar_empleados())

def cargar_medicamentos():
    if os.path.exists("Medicamentos.json"):
        with open("Medicamentos.json","r") as f:
            return json.load(f)
    return{}
#print(cargar_medicamentos())

def cargar_paciente():
    if os.path.exists("Pacientes.json"):
        with open("Pacientes.json") as f:
            return json.load(f)
    return{}
#print(cargar_paciente())

def cargar_proveedores():
    if os.path.exists("Proveedores.json"):
        with open("Proveedores.json") as f:
            return json.load(f)
    return{}
#print(cargar_proveedores())

def cargar_ventas():
    if os.path.exists("Ventas.json"):
        with open("Ventas.json") as f:
            return json.load(f)
    return{}
#print(cargar_ventas())