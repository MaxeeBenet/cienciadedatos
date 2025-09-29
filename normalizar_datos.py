import pandas as pd

#contenia una codificacion diferente y el separador es ";" y no ","
dataFv1 = pd.read_csv('listado_sisa_base_actividad.csv', encoding='latin-1', sep=';')
#elimino todas las columnas vacias
df_limpio = dataFv1.dropna(axis=1, how="all") 
#elimino los espacios en los titulos de las columnas, reemplazo caracteres con " ´ ", pongo todas en minuscula
df_limpio.columns = df_limpio.columns.str.strip().str.replace(" ", "_").str.replace("ó","o").str.replace("í","i").str.replace("á","a").str.replace("é","e").str.replace("ú","u").str.lower()
#reemplazo valores de SIN DATO por No disponible, reemplazo caracteres con tilde
df_limpio = df_limpio.replace("*sin dato*", "No disponible").replace("*SIN DATO* (*SIN DATO*)", "No disponible").replace("no disponible", "No disponible").replace("ó","o").replace("í","i").replace("á","a").replace("é","e").replace("ú","u")
#ordeno de menor a mayor
df_limpio = df_limpio.sort_values(by=["nro_doc"], ascending=True)
#guardo en un nuevo csv una vez normalizado con codificacion utf-8 para normalizar con excel en español.
df_limpio.to_csv("df_limpio.csv", index=False, encoding='utf-8')