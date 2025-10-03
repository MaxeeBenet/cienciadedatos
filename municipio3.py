import pandas as pd

df_unico = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv")
#filtro columna no disponible.
df_filtrado = df_unico[df_unico["municipio"] != " No disponible"]

#total de casos por municipio
casos_por_municipio = (
    df_filtrado.groupby("municipio")["evento"]
    .count()
    .reset_index(name="total_casos")
    .sort_values("total_casos", ascending=False)
)

#top 10 municipios
top10_municipios = casos_por_municipio.head(10)

# Calcular "otros"
otros_total = casos_por_municipio["total_casos"].iloc[10:].sum()

# Agregar fila "OTROS"
top10_con_otros = pd.concat(
    [top10_municipios, pd.DataFrame([{"municipio": "OTROS", "total_casos": otros_total}])]
).reset_index(drop=True)

print(top10_con_otros)

top10_con_otros.to_csv("top10_con_otros.csv", index=False, encoding="latin-1")