import math
import random
import matplotlib.pyplot as plt
import numpy as np

k = 0
opcion = 0
path = "primos.txt"


def generar_secuencia_binaria(k):
    if k == 0:
        return ["0"]
    elif k == 1:
        return ["0", "0", "1"]
    else:
        nueva_secuencia = ["0", "0", "1"]
        k_aux = 2
        k_pos = 0
        
        while k_aux <= k:
            for i in range(k_pos + 1, pow(2, k_aux), 1):
                nueva_secuencia.append(nueva_secuencia[i] + "0")
                nueva_secuencia.append(nueva_secuencia[i] + "1")
    
            k_pos = pow(2, k_aux) - 1
            k_aux = k_aux + 1
        
        del nueva_secuencia[-2:]
        return nueva_secuencia

def contar_unos(cadena):
    contador = 0  
    
    for caracter in cadena:
        if caracter == '1':
            contador += 1  
    
    return contador


def binario_a_entero(cadena_binaria):
    try:
        numero_entero = int(cadena_binaria, 2)
        return numero_entero
    except ValueError:
        return None  


def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite_superior = int(math.sqrt(numero)) + 1
    for i in range(3, limite_superior, 2):
        if numero % i == 0:
            return False

    return True


print("BIENVENIDO".center(50))
print("\n1)  Ingrese la cantidad de primos de forma manual")
print("2)  Ingrese la cantidad de primos de forma automatica")
print("3)  Salir\n")

opcion = int(input("Seleccione la opción a realizar: "))


while opcion != 3:
    try:
        if opcion == 1:
            print("Seleccionaste la opción manual")
            k = int(input("Ingrese cuantos primos decea ver: "))
        
        elif opcion == 2:
            k = random.randint(0, 10000000)
            print("Seleccionaste la opción random")
            
        elif opcion == 3:
            break
        
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
            
        opcion = None
        bin_k = len(bin(k)) - 2

        print(f"El valor de primos a mostrar -> {k}")
        input("Presione enter para continuar...")

        secuencia_binaria = list(generar_secuencia_binaria(bin_k))
        secuencia_binaria_rango = [palabra for palabra in secuencia_binaria if len(palabra) == bin_k]

        secuencia_primos = []
        posiciones = []
        cantidad_unos = []
        binario_arreglo = []

        for idx, binario in enumerate(secuencia_binaria_rango):
            numero_entero = binario_a_entero(binario)
            if es_primo(numero_entero) and (numero_entero <= k):
                binario_arreglo.append(binario)
                secuencia_primos.append(numero_entero)
                posiciones.append(idx)
                cantidad_unos.append(contar_unos(binario))

        with open(path, "w", encoding="utf-8") as file:
            for i in range(len(secuencia_primos)):
                file.write(f"{secuencia_primos[i]} -> {binario_arreglo[i]}\n")
        file.close()

        plt.scatter(posiciones, cantidad_unos, marker='*', s=1, color='blue')
        plt.xlabel('Posición en el Array')
        plt.ylabel('Cantidad de Unos')
        plt.title('Cantidad de Unos en Cada Posición del Array')

        plt.show()

        cantidad_unos_log = []
        
        for i in cantidad_unos:
            cantidad_unos_log.append(math.log10(cantidad_unos[i]))

        plt.scatter(posiciones, cantidad_unos_log, marker='*', s=1, color='blue')
        plt.xlabel('Posición en el Array')
        plt.ylabel('Cantidad de Unos logaritmo 10')
        plt.title('Cantidad de Unos en Cada Posición del Array 2')

        plt.show()
        
    
        print("\n\n 1)  Ingrese la cantidad de primos de forma manual")
        print("2)  Ingrese la cantidad de primos de forma automatica")
        print("3)  Salir\n")


        opcion = int(input("Seleccione la nueva opción a realizar: "))
        
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")


