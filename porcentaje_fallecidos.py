import pandas as pd
#creo mi dataframe leyendo el csv
df = pd.read_csv('df_limpio_con_repeticiones.csv', encoding='utf-8')
#los ordeno de menor a mayor
df = df.sort_values(by='nro_doc', ascending=True)
#elimino dni duplicados considerando que no tengan mas de una enfermedad.
df = df.drop_duplicates(subset=['nro_doc', 'evento'], keep='first')
#normalizo los valores "*sin dato*"
df['resultado'] = df['resultado'].replace("*sin dato*", "No disponible")
#contar la cantidad de filas dentro del dataset
total_casos = len(df)
#casos negativos
negativos = (df['resultado'] == "Negativo").sum()
porc_negativos = round((negativos / total_casos) * 100, 2)
#casos sin informacion (NO DISPONIBLE)
sin_info = (df['resultado'] == "No disponible").sum()
porc_sin_datos = round((sin_info / total_casos) * 100, 2)
#busco el porcentaje restante.
otros = df[(df['resultado'] != "No disponible") & (df['resultado'] != "Negativo")]
total_restante = len(otros)
porc_restante = round((total_restante / total_casos) * 100, 2)
#creo un dataframe con los datos. 
df_porcentaje = pd.DataFrame(
    {
        "Categoria": ["Negativos","Sin informacion", "Resto"],
        "Porcentajes": [porc_negativos, porc_sin_datos, porc_restante]
    }
)

print(df_porcentaje)
