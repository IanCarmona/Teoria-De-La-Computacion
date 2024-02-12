import networkx as nx
import matplotlib.pyplot as plt
import csv

# Crea un grafo dirigido
G = nx.DiGraph()

# Lee el archivo CSV y agrega las transiciones al grafo
with open('datos_actualizados.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # El primer elemento en cada fila es el estado actual
        current_state = row[0]
        for i, next_state in enumerate(row[1:]):
            # Ignora las transiciones vacías (representadas por '1' en tu CSV)
            if next_state != '1':
                # Agrega una arista desde el estado actual al siguiente estado
                G.add_edge(current_state, str(i))

# Dibuja el grafo
pos = nx.circular_layout(G)  # Cambia la disposición a circular

plt.figure(figsize=(8, 8))  # Ajusta el tamaño total del gráfico
nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=8, font_color="black")
plt.show()
