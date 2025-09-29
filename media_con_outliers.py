import pandas as pd

df = pd.read_csv("df_unico_municipios_normalizado.csv", encoding="latin-1")

#print(df.head())

df["fecha_de_consulta"] = pd.to_datetime(df["fecha_de_consulta"], errors='coerce', dayfirst=True)
df["fecha_de_inicio_de_sintomas"] = pd.to_datetime(df["fecha_de_inicio_de_sintomas"], errors='coerce', dayfirst=True)

df["Diferencia_de_dias"] = (df["fecha_de_consulta"] - df['fecha_de_inicio_de_sintomas']).dt.days

eventos = df['evento'].unique()

#inicio lista vacia
resultados = []

for evento in eventos:
        datos_eventos = df[df["evento"] == evento]['Diferencia_de_dias']
        media = round(datos_eventos.mean())
        resultados.append({
                "Enfermedad": evento,
                "Media con outliers": media
        })

df_resultados = pd.DataFrame(resultados)

print(df_resultados)

#df_resultados.to_csv("media_con_outliers.csv", index=False, encoding="utf-8")
