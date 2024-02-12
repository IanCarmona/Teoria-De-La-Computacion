import random
import time

def guardar_cadenas_en_archivo(cadenas, nombre_archivo):
    with open(nombre_archivo, "a+") as archivo:
        archivo.write(f"{cadenas}")


def e1(numero):
    transiciones = {"0": 2, "1": 3}
    return transiciones.get(numero, True)

def e2(numero):
    transiciones = {"0": 1, "1": 4}
    return transiciones.get(numero, False)

def e3(numero):
    transiciones = {"0": 4, "1": 1}
    return transiciones.get(numero, False)

def e4(numero):
    transiciones = {"0": 3, "1": 2}
    return transiciones.get(numero, False)



def automata_clasificador(cadena, ruta_par, ruta_impar):
    flag = None
    estado = 1

    for i in cadena:
        if estado == 1:
            estado = e1(i)
            flag = estado

        elif estado == 2:
            estado = e2(i)
            flag = estado

        elif estado == 3:
            estado = e3(i)
            flag = estado

        elif estado == 4:
            estado = e4(i)
            flag = estado

    if flag == True:
        guardar_cadenas_en_archivo(cadena, ruta_par)
    else:
        guardar_cadenas_en_archivo(cadena, ruta_impar)


ruta_data = "cadenas_binarias.txt"
ruta_data_impar = "cadenas_binarias_impar.txt"
ruta_data_par = "cadenas_binarias_par.txt"
ejecuciones = 0

on_off = random.choice("10")  # Con un random ve si el automata esta prendido o apagado
print(on_off)
input("¿Desea continuar?...")


while on_off == "1":
    ejecuciones = ejecuciones + 1
    with open(ruta_data, "r") as archivo:
        lineas = archivo.readlines()

    time.sleep(2)

    for linea in lineas:
        automata_clasificador(linea, ruta_data_par, ruta_data_impar)

    on_off = random.choice("10")  # Con un random ve si el automata esta prendido o apagado

    print(on_off)
    input("¿Desea continuar?...")

print(f"Se apago el automata despues de {ejecuciones} ejecuciones")
