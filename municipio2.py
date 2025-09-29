import pandas as pd

df_unico = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv")
#filtro columna no disponible.
df_filtrado = df_unico[df_unico["municipio"] != "No disponible"]

casos_por_municipio = (
    df_filtrado.groupby("municipio")["evento"]
    .count()
    .reset_index(name="total_casos")
    .sort_values("total_casos", ascending=False)
)

#top 10 municipios
top10_municipios = casos_por_municipio.head(10)

#calcular "otros"
otros_total = casos_por_municipio["total_casos"].iloc[10:].sum()

#agregar fila "OTROS"
top10_con_otros = pd.concat(
    [top10_municipios, pd.DataFrame([{"municipio": "OTROS", "total_casos": otros_total}])]
).reset_index(drop=True)

print(top10_con_otros)

#municipios que forman el top 10
municipios_top10 = top10_municipios["municipio"]

#casos en el top 10 (detalle por evento)
detalle_eventos_top10 = (
    df_filtrado[df_filtrado["municipio"].isin(municipios_top10)]
    .groupby(["municipio", "evento"])
    .size()
    .reset_index(name="cantidad")
)

#casos de los "otros" municipios (detalle por evento)
detalle_eventos_otros = (
    df_filtrado[~df_filtrado["municipio"].isin(municipios_top10)]
    .groupby("evento")
    .size()
    .reset_index(name="cantidad")
)

#agregar columna municipio="OTROS"
detalle_eventos_otros["municipio"] = "OTROS"

#unir ambos
detalle_eventos_final = pd.concat([detalle_eventos_top10, detalle_eventos_otros], ignore_index=True)

#Solo para ver si esta haciendo bien el conteo.
print(detalle_eventos_final.head(20))
# .to_csv creo un archivo csv para poder graficar de manera mas simple con excel.

#detalle_eventos_final.to_csv("detalle_eventos_final.csv", index=False, encoding="utf-8")