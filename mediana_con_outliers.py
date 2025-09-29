import pandas as pd

df = pd.read_csv("df_limpio_municipio_sin_repeticiones.csv", encoding="utf-8")

df["fecha_de_consulta"] = pd.to_datetime(df["fecha_de_consulta"], errors='coerce', dayfirst=True)
df["fecha_de_inicio_de_sintomas"] = pd.to_datetime(df["fecha_de_inicio_de_sintomas"], errors='coerce', dayfirst=True)

df["Diferencia_de_dias"] = (df["fecha_de_consulta"] - df['fecha_de_inicio_de_sintomas']).dt.days

#filtro casos con dias negativos.
df =  df[df["Diferencia_de_dias"] >= 0]

eventos = df['evento'].unique()

#inicio lista vacia
resultados = []
#por cada evento en eventos (cada una de las enfermedades), hago una mediana.
for evento in eventos:
        datos_eventos = df[df["evento"] == evento]['Diferencia_de_dias']
        #.median() funcion reservada para mediana.
        mediana = round(datos_eventos.median())
        #añado a la lista en cada bucle.
        resultados.append({
                "Enfermedad": evento,
                "Mediana con outliers": mediana
        })
#lo paso a un dataframe para poder enviarlo a CSV.
df_resultados = pd.DataFrame(resultados)

print(df_resultados)
print(df["Diferencia_de_dias"].describe())
df_resultados.to_csv("mediana_con_outliers.csv", index=False, encoding='utf-8')