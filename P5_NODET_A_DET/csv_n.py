import pandas as pd

# Lee el archivo CSV
df = pd.read_csv("tabla_final.csv")

# Crea un diccionario para mapear estados únicos a números únicos
estados_unicos = df['ESTADO'].unique()
mapeo = {estado: numero for numero, estado in enumerate(estados_unicos, start=1)}

# Aplica el mapeo a la columna 'ESTADO'
df['ESTADO'] = df['ESTADO'].map(mapeo)

# Reemplaza todos los valores en el DataFrame con sus números correspondientes
df.replace(mapeo, inplace=True)

# Guarda el DataFrame actualizado en un nuevo archivo CSV
df.to_csv("datos_actualizados.csv", index=False)
