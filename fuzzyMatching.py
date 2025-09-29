import pandas as pd
from thefuzz import process

# 1. Cargar archivos
csv_origen = "df_limpio.csv"  # CSV original
csv_localidades = "localidades_municipios.csv"  # CSV de referencia con localidades y municipios

df_unico = pd.read_csv(csv_origen)
df_localidades = pd.read_csv(csv_localidades)

# 2. Normalizar nombres de localidades
df_unico['localidad_residencia'] = df_unico['localidad_residencia'].str.strip().str.lower()
df_localidades['LOCALIDAD'] = df_localidades['LOCALIDAD'].str.strip().str.lower()

# 3. Funcion para buscar municipio usando fuzzy matching
def buscar_municipio(localidad, lista_localidades, df_ref):
    mejor_match, puntaje = process.extractOne(localidad, lista_localidades)
    if puntaje >= 80:  # solo coincidencias confiables
        municipio = df_ref.loc[df_ref['LOCALIDAD'] == mejor_match, 'MUNICIPIO'].values[0]
        return municipio
    else:
        return None

# 4. Crear lista de localidades de referencia
lista_localidades = df_localidades['LOCALIDAD'].tolist()

# 5. Aplicar la funcion a cada fila
df_unico['municipio'] = df_unico['localidad_residencia'].apply(
    lambda x: buscar_municipio(x, lista_localidades, df_localidades)
)

# 6. Localidades no encontradas
no_encontradas = df_unico[df_unico['municipio'].isna()]['localidad_residencia'].unique()
if len(no_encontradas) > 0:
    print("Las siguientes localidades NO se encontraron en el CSV de referencia:")
    for loc in no_encontradas:
        print("-", loc)
else:
    print("Todas las localidades fueron emparejadas con fuzzy matching.")

# 7. Guardar CSV final
output_path = "df_limpio_municipios_repeticiones.csv"
df_unico.to_csv(output_path, index=False)
print(f"Archivo final guardado en: {output_path}")