import pandas as pd

df = pd.read_csv("df_limpio_municipios_repeticiones.csv", encoding="utf-8")
#elimino duplicados para poder realizar un analisis por municipio
df = df.drop_duplicates(subset=['nro_doc', 'evento'], keep='first')
#descargo csv sin repeticiones con municipios.
df.to_csv("df_limpio_municipio_sin_repeticiones.csv", index=False, encoding='utf-8')
