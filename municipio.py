import pandas as pd

df_unico = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv")
#filtro columna no disponible.
df_filtrado = df_unico[df_unico["municipio"] != "No disponible"]

#agrupar cantidad de casos por municipio.
casos_por_municipio = df_filtrado.groupby("municipio")["evento"].count().reset_index()
casos_por_municipio.columns = ["municipio", "cantidad"]

#definir rangos.
bins = [0, 10, 50, 100, float("inf")]
labels = ["0-10", "11-50", "51-100", "100+"]

#crear una columna de rango.
casos_por_municipio["rango"] = pd.cut(casos_por_municipio["cantidad"], bins=bins, labels=labels, right=True)

#cantidad de municipios en cada rango.
conteo_rangos = casos_por_municipio["rango"].value_counts().reset_index()
conteo_rangos.columns = ["Rango", "Cantidad de municipios"]

#contar cantidad de municipios.
cantidad_municipios = df_unico["municipio"].nunique()

#guardo en csv para realizar graficos.
conteo_rangos.to_csv("conteo_rangos.csv", index=False, encoding="utf-8")