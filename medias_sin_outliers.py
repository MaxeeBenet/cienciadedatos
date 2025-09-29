import pandas as pd

df = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv", encoding="utf-8")

#print(df.head())

df["fecha_de_consulta"] = pd.to_datetime(df["fecha_de_consulta"], errors='coerce', dayfirst=True)
df["fecha_de_inicio_de_sintomas"] = pd.to_datetime(df["fecha_de_inicio_de_sintomas"], errors='coerce', dayfirst=True)

df["Diferencia_de_dias"] = (df["fecha_de_consulta"] - df['fecha_de_inicio_de_sintomas']).dt.days

#filtro fechas con dias negativos. Fechas de consulta anteriores a la fecha de inicio de sintomas.
df = df[df["Diferencia_de_dias"] >= 0]

eventos = df['evento'].unique()

#inicio lista vacia
resultados = []

for evento in eventos:
        datos_eventos = df[df["evento"] == evento]['Diferencia_de_dias']
        Q1 = datos_eventos.quantile(0.25)
        Q3 = datos_eventos.quantile(0.75)
        IQR = Q3 - Q1
        #limite inf y superior por enfermedad
        limite_inf = Q1 - 1.5 * IQR
        limite_sup = Q3 + 1.5 * IQR
        #filtrado de outliers por evento
        datos_limpios = datos_eventos[(datos_eventos >= limite_inf) & (datos_eventos <= limite_sup)]
        media = round(datos_limpios.mean())
        resultados.append({
                "Enfermedad": evento,
                "Media sin outliers": media
        })

df_resultados = pd.DataFrame(resultados)

print(df_resultados)

df_resultados.to_csv("media_sin_outliers.csv", index=False, encoding="utf-8")