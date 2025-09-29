import pandas as pd

#leo mi csv
df_unico = pd.read_csv("df_unico_municipios.csv")
#cuento la cantidad de casos por cada clasificacion
conteo_clasificacion = df_unico["clasificacion_manual_del_caso"].value_counts().reset_index()
conteo_clasificacion.columns = ["Clasificacion", "cantidad"]
print(conteo_clasificacion)
#conteo_clasificacion.to_csv("conteo_clasificacion.csv", index=False, encoding="utf-8")