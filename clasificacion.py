import pandas as pd

#leo mi csv SIN repeticiones para que no haya duplicacion de datos por persona.
df_unico = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv")
#cuento la cantidad de casos por cada clasificacion
conteo_clasificacion = df_unico["clasificacion_manual_del_caso"].value_counts().reset_index()

conteo_clasificacion.columns = ["Clasificacion", "cantidad"]

print(conteo_clasificacion)

conteo_clasificacion.to_csv("conteo_clasificacion.csv", index=False, encoding="utf-8")