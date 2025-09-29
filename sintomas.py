import pandas as pd

df = pd.read_csv('df_limpio.csv', encoding='utf-8')

df_filtrado = df[df['signo_/_sintoma'] != "No disponible"]

resumen = (
    df_filtrado
    .groupby(['evento','signo_/_sintoma'])
    .agg(
        total_casos = ('signo_/_sintoma', "size"),
        internados = ('fecha_internacion', lambda x:( x != "No disponible").sum()),
        fallecidos = ('fallecido', lambda x: (x == "SI").sum())
    )
    .reset_index()
)

sintomas_top_2 = (
    resumen
    .sort_values(['evento', 'total_casos'], ascending=[True, False])
    .groupby('evento')
    .head(2)
    .reset_index(drop=True)
)

print(sintomas_top_2)

sintomas_top_2.to_csv("sintomas_enfermedad.csv", index=False, encoding='utf-8')
