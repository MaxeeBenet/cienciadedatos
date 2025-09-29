import pandas as pd

#leer el archivo con pandas
df_unico_municipio = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv")

#conteo de casos por evento
conteo_eventos = df_unico_municipio["evento"].value_counts().reset_index()
conteo_eventos.columns = ["evento", "cantidad"]

conteo_eventos.to_csv("conteo_eventos.csv", index=False, encoding="utf-8")

print(conteo_eventos)