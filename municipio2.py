import pandas as pd

df_unico = pd.read_csv("df_unico_municipios.csv")
#filtro columna no disponible.
df_filtrado = df_unico[df_unico["municipio"] != " NO DISPONIBLE"]

casos_por_municipio = (
    df_filtrado.groupby("municipio")["evento"]
    .count()
    .reset_index(name="total_casos")
    .sort_values("total_casos", ascending=False)
)

# Top 10 municipios
top10_municipios = casos_por_municipio.head(10)

# Calcular "otros"
otros_total = casos_por_municipio["total_casos"].iloc[10:].sum()

# Agregar fila "OTROS"
top10_con_otros = pd.concat(
    [top10_municipios, pd.DataFrame([{"municipio": "OTROS", "total_casos": otros_total}])]
).reset_index(drop=True)

print(top10_con_otros)

# Municipios que forman el top 10
municipios_top10 = top10_municipios["municipio"]

# Casos en el Top 10 (detalle por evento)
detalle_eventos_top10 = (
    df_filtrado[df_filtrado["municipio"].isin(municipios_top10)]
    .groupby(["municipio", "evento"])
    .size()
    .reset_index(name="cantidad")
)

# Casos de los "otros" municipios (detalle por evento)
detalle_eventos_otros = (
    df_filtrado[~df_filtrado["municipio"].isin(municipios_top10)]
    .groupby("evento")
    .size()
    .reset_index(name="cantidad")
)

# Agregar columna municipio="OTROS"
detalle_eventos_otros["municipio"] = "OTROS"

# Unir ambos
detalle_eventos_final = pd.concat([detalle_eventos_top10, detalle_eventos_otros], ignore_index=True)

detalle_eventos_final.to_csv("detalle_eventos_final.csv", index=False, encoding="latin-1")