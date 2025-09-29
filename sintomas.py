import pandas as pd

df = pd.read_csv('df_limpio_con_repeticiones.csv', sep=',', encoding='utf-8')

df_filtrado = df[df['signo_/_síntoma'] != "*sin dato*"]

resumen = (
    df_filtrado
    .groupby(['evento','signo_/_síntoma'])
    .agg(
        total_casos = ('signo_/_síntoma', "size"),
        internados = ('fecha_internación', lambda x:( x != "*sin dato*").sum()),
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

