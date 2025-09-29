import pandas as pd


df = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv", encoding="utf-8")

df_filtrado = df[(df["antecedente_epidemiologico"] != "No disponible") & (df["municipio"] != "No disponible")]

tabla_df_municipio = (
    df_filtrado.groupby(['municipio', 'antecedente_epidemiologico'])
    .size()
    .reset_index(name='cantidad_casos')
)

tabla_df_eventos = (
    df_filtrado.groupby(['evento', 'antecedente_epidemiologico'])
    .size()
    .reset_index(name='cantidad_casos')
)

tabla_df_eventos.to_csv("antecedentes_epidemiologico_eventos.csv", index=False, encoding="utf-8")

tabla_df_municipio.to_csv("antecedentes_epidemiologicos_municipios.csv", index=False, encoding="utf-8")