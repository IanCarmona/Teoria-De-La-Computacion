import generar_jugadas as gj


secuencia = list(input("Introduce la secuencia de colores (r y n): ").lower())
caminos = []

# Inicia el recorrido desde la posición 1
gj.recorrer_tablero(secuencia, [1], [1])

# Guarda los caminos en un archivo
with open('caminos.txt', 'w') as f:
    for camino in caminos:
        f.write(', '.join(map(str, camino)) + '\n')

print("Caminos guardados en 'caminos.txt'")
