import pandas as pd


df = pd.read_csv("df_unico_municipio_sin_repeticiones_ordenado.csv", encoding='utf-8')

df_filtrado = df[(df["antecedente_epidemiológico"] != "No disponible") & (df["municipio"] != " NO DISPONIBLE")]

tabla_df_municipio = (
    df_filtrado.groupby(['municipio', 'antecedente_epidemiológico'])
    .size()
    .reset_index(name='cantidad_casos')
)

tabla_df_eventos = (
    df_filtrado.groupby(['evento', 'antecedente_epidemiológico'])
    .size()
    .reset_index(name='cant_casos')
)

tabla_df_eventos.to_csv("antecedentes_epidemiologico_eventos.csv", index=False, encoding="utf-8")

tabla_df_municipio.to_csv("antecedentes_epidemiologicos_municipios.csv", index=False, encoding="utf-8")