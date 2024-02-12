def movimientos_posibles(valor, color):
    x, y = coordenadas[valor]
    movimientos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
    posiciones = []
    for nx, ny in movimientos:
        if 1 <= nx <= 4 and 1 <= ny <= 4:  # Verifica que la nueva posición esté dentro del tablero
            nuevo_valor = valores[(nx, ny)]
            if tablero[nuevo_valor] == color:  # Verifica que la nueva posición tenga el color correcto
                posiciones.append(nuevo_valor)
    return posiciones


def recorrer_tablero(secuencia, posiciones, camino):
    if not secuencia:  # Si la secuencia está vacía, hemos terminado este camino
        caminos.append(camino)
        return
    color, *resto = secuencia  # Separa el primer color de la secuencia
    nuevas_posiciones = set()
    for valor in posiciones:
        nuevas_posiciones.update(movimientos_posibles(valor, color))  # Agrega todas las nuevas posiciones posibles
    for nuevo_valor in nuevas_posiciones:
        recorrer_tablero(resto, [nuevo_valor], camino + [nuevo_valor])  # Recorre el tablero para cada nueva posición


# Define el tablero con colores
tablero = {
    1: 'r', 2: 'n', 3: 'r', 4: 'n',
    5: 'n', 6: 'r', 7: 'n', 8: 'r',
    9: 'r', 10: 'n', 11: 'r', 12: 'n',
    13: 'n', 14: 'r', 15: 'n', 16: 'r'
}

# Define las coordenadas y valores para conversiones
coordenadas = {i: ((i - 1) // 4 + 1, (i - 1) % 4 + 1) for i in range(1, 17)}
valores = {v: k for k, v in coordenadas.items()}

secuencia = list(input("Introduce la secuencia de colores (r y n): ").lower())
caminos = []

# Inicia el recorrido desde la posición 1
recorrer_tablero(secuencia, [1], [1])

# Guarda los caminos en un archivo
with open('caminos.txt', 'w') as f:
    for camino in caminos:
        f.write(', '.join(map(str, camino)) + '\n')

print("Caminos guardados en 'caminos.txt'")
