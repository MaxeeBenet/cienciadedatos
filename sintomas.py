import pandas as pd

# Cargar el CSV
df = pd.read_csv('df_limpio.csv', encoding='utf-8')

# Filtrar filas con signos/síntomas disponibles
df_disponibles = df[df['signo_/_sintoma'] != "No disponible"]

# Agrupar por evento y signo/síntoma para contar casos
resumen_casos = (
    df_disponibles
    .groupby(['evento', 'signo_/_sintoma'], as_index=False)
    .size()
    .rename(columns={'size': 'total_casos'})
)

# Obtener los 2 signos/síntomas más frecuentes por evento
sintomas_top2 = (
    resumen_casos
    .sort_values(['evento', 'total_casos'], ascending=[True, False])
    .groupby('evento')
    .head(2)
    .reset_index(drop=True)
)

# Mostrar resultado
print(sintomas_top2)

# Guardar a CSV
sintomas_top2.to_csv("sintomas_enfermedad.csv", index=False, encoding='utf-8')
