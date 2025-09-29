import pandas as pd

df = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv")

# Internados por enfermedad
internados = df[df["fecha_internacion"] != "No disponible"]
internados_por_enfermedad = internados.groupby("evento").size().reset_index(name="cantidad_internados")

# Fallecidos por enfermedad
fallecidos = df[df["fallecido"] == "SI"]
fallecidos_por_enfermedad = fallecidos.groupby("evento").size().reset_index(name="cantidad_fallecidos")

# Merge internados y fallecidos por enfermedad
resumen = pd.merge(
    internados_por_enfermedad,
    fallecidos_por_enfermedad,
    on="evento",
    how="outer"
).fillna(0)

resumen["cantidad_internados"] = resumen["cantidad_internados"].astype(int)
resumen["cantidad_fallecidos"] = resumen["cantidad_fallecidos"].astype(int)

# Guardar CSV

print(resumen)
resumen.to_csv("internados_y_fallecidos_por_enfermedad.csv", index=False)
