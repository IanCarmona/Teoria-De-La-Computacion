import random
import matplotlib.pyplot as plt
import math

k = 0
opcion = 0
path = "binarios.txt"


def generar_secuencia_binaria(k):
    if k == 0:
        return ["∈"]
    elif k == 1:
        return ["∈", "0", "1"]
    else:
        nueva_secuencia = ["∈", "0", "1"]
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
    contador = 0  # Inicializamos el contador
    
    for caracter in cadena:
        if caracter == '1':
            contador += 1  # Incrementamos el contador si encontramos un '1'
    
    return contador

print("BIENVENIDO".center(50))
print("\n1)  ingrese k de forma manual")
print("2)  ingrese k de forma automatica\n")

while True:
    try:
        opcion = int(input("Seleccione la opción a realizar: "))
        if opcion == 1:
            print("Seleccionaste la opción manual")
            k = int(input("Ingrese la k: "))
            break
        elif opcion == 2:
            k = random.randint(0, 1000)
            print("Seleccionaste la opción random")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

opcion = None
print(f"El valor de k -> {k}")
input("Presione enter para continuar...")

# Convertir secuencia_binaria en una lista
secuencia_binaria = list(generar_secuencia_binaria(k))

posiciones = []
cantidad_unos = []

with open(path, "w", encoding="utf-8") as file:
    for item, elemento in enumerate(secuencia_binaria):
        posiciones.append(item)
        cantidad_unos.append(contar_unos(elemento))
        file.write(f"{elemento}\n")

file.close()

plt.scatter(posiciones, cantidad_unos, marker='*', s=1, color='blue')
plt.xlabel('Posición en el Array')
plt.ylabel('Cantidad de Unos')
plt.title('Cantidad de Unos en Cada Posición del Array')

plt.show()


posiciones = []
cantidad_unos_log = []

for i in range(len(cantidad_unos)):
    if cantidad_unos[i] != 0:
        posiciones.append(i)
        cantidad_unos_log.append(math.log10(cantidad_unos[i]))

plt.scatter(posiciones, cantidad_unos_log, marker='*', s=1, color='blue')
plt.xlabel('Posición en el Array')
plt.ylabel('Cantidad de Unos logaritmo 10')
plt.title('Cantidad de Unos en Cada Posición del Array 2')

plt.show()