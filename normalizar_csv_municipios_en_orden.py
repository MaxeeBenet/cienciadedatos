import pandas as pd

df = pd.read_csv("df_unico_municipios_repeticiones.csv", encoding="utf-8")

df['localidad_residencia'] = df["localidad_residencia"].replace("*sin dato* (*sin dato*)", "No disponible")
df['antecedente_epidemiológico'] = df["antecedente_epidemiológico"].replace("*sin dato*", "No disponible")
df = df.replace("*sin dato*", "No disponible")


df = df.sort_values(by=['nro_doc'], ascending=True)

df = df.drop_duplicates(subset=['nro_doc', 'evento'], keep='first')
df.to_csv("df_unico_municipio_sin_repeticiones_ordenado.csv", index=False, encoding='utf-8')
print(df.head(10))