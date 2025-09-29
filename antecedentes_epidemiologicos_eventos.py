import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('antecedentes_epidemiologico_eventos.csv')

pivot_df = df.pivot_table(
    index='evento', 
    columns='antecedente_epidemiologico', 
    values='cantidad_casos', 
    aggfunc='sum', 
    fill_value=0
)

# Ordenar eventos por total de casos
pivot_df['Total'] = pivot_df.sum(axis=1)
pivot_df = pivot_df.sort_values('Total', ascending=False).drop('Total', axis=1)

# GRÁFICO: BARRAS APILADAS POR EVENTO
plt.figure(figsize=(14, 8))
colores = plt.cm.Set3(np.linspace(0, 1, len(pivot_df.columns)))

# Crear gráfico apilado
bottom = np.zeros(len(pivot_df))
for i, columna in enumerate(pivot_df.columns):
    valores = pivot_df[columna].values
    bars = plt.bar(pivot_df.index, valores, bottom=bottom, label=columna, color=colores[i], alpha=0.8, edgecolor='black')
    
    # AÑADIR NÚMEROS DENTRO DE LAS BARRAS
    for j, (valor, barra) in enumerate(zip(valores, bars)):
        if valor > 0:
            altura_texto = bottom[j] + valor / 2
            plt.text(barra.get_x() + barra.get_width()/2, altura_texto, 
                    f'{int(valor)}', 
                    ha='center', va='center', 
                    fontsize=9, fontweight='bold',
                    color='black')
    
    bottom += valores

plt.ylabel('Cantidad de Casos', fontsize=12, fontweight='bold')
plt.xlabel('Evento (Enfermedad)', fontsize=12, fontweight='bold')
plt.title('Distribución de Antecedentes Epidemiológicos por Tipo de Enfermedad', 
          fontsize=14, fontweight='bold', pad=20)
plt.xticks(rotation=15, ha='right')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()