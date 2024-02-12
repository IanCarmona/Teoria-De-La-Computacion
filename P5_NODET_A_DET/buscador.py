import funciones_buscador as fb

archivo_leer = 'leer.txt'
archivo_resultado = 'resultado.txt'

with open(archivo_leer, 'rb') as archivo_entrada:
    contenido = archivo_entrada.read()

resultado = fb.buscador(contenido.decode('utf-8'))  # Decodificar como utf-8 si es un archivo de texto

# Abre el archivo de resultado en modo escritura ('w')
with open('resultado.txt', 'w', encoding='utf-8') as archivo_resultado:
    for clave, arreglo in resultado.items():
        # Formatea la salida con la clave, el primer elemento del arreglo y el resto de elementos
        texto_formateado = f'{clave} = {arreglo[0]} \t\t Posiciones = {arreglo[1:]}\n'
        archivo_resultado.write(texto_formateado)

letra, estado = fb.regresa_historia()

# Abre el archivo "historia.txt" en modo escritura
with open("historia.txt", "w") as archivo_historia:
    for i in range(len(letra)):
        linea = f"{letra[i]} -> {estado[i]}\n"
        archivo_historia.write(linea)



