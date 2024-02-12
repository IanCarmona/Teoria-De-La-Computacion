import random

def generar_cadena_binaria(bits):
    cadena = ''.join(random.choice('01') for _ in range(bits))
    return cadena

def generar_cadenas_pares_e_impares(cantidad):
    cadenas = []

    for _ in range(cantidad):
        bits = generar_cadena_binaria(10)
        cadenas.append(bits)
    return cadenas

def guardar_cadenas_en_archivo(cadenas, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for cadena in cadenas:
            archivo.write(f'{cadena}\n')


cantidad_cadenas = int(input("Ingrese la cantidad de cadenas a generar: "))
nombre_archivo = "cadenas_binarias.txt"

cadenas_generadas = generar_cadenas_pares_e_impares(cantidad_cadenas)
guardar_cadenas_en_archivo(cadenas_generadas, nombre_archivo)

print(f"{cantidad_cadenas} cadenas generadas y guardadas en {nombre_archivo}.")
