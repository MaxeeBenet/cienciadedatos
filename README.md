Informe 1 - Analisis de datos de subsecretaria de salud.

Objetivo:
Elaborar un informe completo sobre el análisis de los datos epidemiológicos trabajados en clase, documentando detalladamente cada paso realizado y reflexionando sobre el proceso de aprendizaje colaborativo teniendo en cuenta el documento que acompaña al dataset.
 
Actividad:
1. Sección nominal: Elaborar un resumen de la cantidad de casos por enfermedad, por
clasificación y por municipio. Elegí una variable que te interese y también incorporala
a tu resumen. Graficar.

2. Sección clínica: Calcular la diferencia de días entre la fecha de inicio de síntomas y
la fecha de consulta. Calculá la mediana de los días. ¿Qué significa esta información
para cada enfermedad?

3. Sección clínica ¿Cuál es el síntoma que más se repite en cada enfermedad?
¿Cuántos de los casos fueron internados y/o fallecieron?

4. Sección de laboratorio: ¿Qué porcentaje de casos dieron negativo al estudio de
laboratorio? ¿Qué porcentaje representan los casos de los cuales no se posee
ningún tipo de información?

5. Sección de epidemiología: Elaborar una tabla con la cantidad de casos y los
antecedentes epidemiológicos por municipio y por enfermedad. Graficar con
columnas.

6. ¿Encontrás algún dato que te haga sospechar que pueda tratarse de un error del
operador al momento de la carga?

{METODOLOGIA DE TRABAJO}

## Preparacion y normalización de datos.
Eliminar columnas vacias, normalizar index de columnas, reemplazar espacios por guiones bajos, reemplazar caracteres con tilde. Reemplazar distintas variaciaciones de "*sin dato*" como dato nulo a un solo valor "No disponible".
Ordenar por DNI de menor a mayor.
- Codigo: [normalizar_datos.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/normalizar_datos.py)

## 1 - Analisis nominal.
Eliminacion de DNI duplicados con chequeo de mas de un evento por DNI para garantizar integridad del análisis.
Dado que el dataset contiene informacion por localidad, se realizo un mapeo a municipios para el analisis, . Se utilizo fuzzy matching para maximizar las coincidencias.
- Codigo por evento: [evento.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/eventos.py) Analisis de cantidad de casos por enfermedad.
  ![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/casos_enfermedad.jpg)
- Codigo por clasificación: [clasificacion.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/clasificacion.py) Analisis de cantidad de coincidencias por cada clasificacion del caso.
  ![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/casos_clasificacion.jpg)
- Codigos por municipio: [municipio.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/municipio.py) Analisis por rangos, contar la cantidad de municipios tenian X cantidad casos en un rango.
  ![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/casos_rango.jpg)
- Codigos por municipio: [municipio2.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/municipio2.py) Analisis de eventos por municipio.
  ![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/cant_enfermedades_municipio2.jpg)
- Codigos por municipio: [municipio3.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/municipio3.py) Analisis de casos por municipio.
  ![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/top10_con_otros3.jpg)

## 2 - Analisis clínico.
Durante este analisis se utilizo un CSV en la cual se filtraron las repeticiones de DNI con First match, first keep, chequeando que no haya otro evento en el mismo DNI, dado que esto altera las mediciones de la mediana.
Tambien se realizo un filtro de outliers y diferencias de dias mayores a 0 (Fechas de inicio de sintomas posteriores a la fecha de consulta no fueron utilizados en este analisis.).
- Analisis de calculo de dias y mediana: [mediana_sin_outliers.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/mediana_sin_outliers.py)
Luego de este analisis y un filtrado se puede obtener:

|   Enfermedad    |    Mediana sin outliers |

|:---------------:|:-----------------------:|

|   Hantavirosis  |          3              |

|   Coqueluche    |          2              |

|   Lepra         |          88             |

|   Suicidio      |          0              |

## 3 - Seccion clínica.
Al realizar este analisis en vez de un TOP 1 utilice un TOP 2.
Durante este analisis utilice un CSV que sin filtrar las coincidencias de mas de un DNI.
Para el analisis de internaciones y defunciones utilice el CSV filtrando las duplicados por DNI.
- Analisis por sintomas: [sintomas.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/sintomas.py)
![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/sintomas_frecuentes.jpg)
- Cantidad de internados: [internados.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/fallecidos_internados.py#L5-L7)
- Cantidad de fallecidos: [fallecidos.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/fallecidos_internados.py#L9-L11)
 ![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/internados_fallecidos.jpg)

## 4 - Seccion laboratorio. 
Para este analisis utilice mi CSV ya normalizado y filtrando los DNI duplicados.
El resultado de este analisis es directo y de sencilla interpretación.
Pero si es un resultado que esta muy marcado por la falta de campos sin información.
- Codigo laboratorio: [resultados_laboratorio.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/porcentaje_negativos.py)
![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/porcentajes_resultados.JPG)

##5 - Seccion de epidemiologia.
Para este analisis se utilizo un primero un analisis de dataset sin repeticiones y normalizado.
De este analisis se obtuvo 2 datasets distintos, uno con los antecedentes epidemiologicos por enfermedad y otro por municipio.
- Confección de ambos CSV: [confeccion_csv](https://github.com/MaxeeBenet/cienciadedatos/blob/main/antecedentes_municipios.py)
Una vez realizado estos datasets se procedio a analizarlos.
- Codigo de analisis por municipio: [municipio.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/antecedentes_epidemiologicos_municipio.py)
Se obtuvo el siguiente grafico:
![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/dist_antecedentes_epidemiologicos.png)
Se utilizo un top 10 debido a la cantidad de municipios lo cual resulta en un gráfico poco legible.
- Codigo de analisis por enfermedad: [enfermedad.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/antecedentes_epidemiologicos_eventos.py)
Se obtuvo el siguiente grafico:
![](https://github.com/MaxeeBenet/cienciadedatos/blob/main/imagenes/Figure_1.png)
De este analisis se puede observar que Intentos de suicidio no tiene un antecedente epidemilogico para analizar.

## 6 - Analisis final.

Luego de todos los analisis se puede observar errores de carga en la poca cantidad de datos disponible, como asi los DNI con mas de 11 cifras, fechas de inicio de sintomas posteriores a la fecha de consulta de dicha enfermedad. Varios errores en localidad hizo que se dificulte la correcta asignacion del correspondiente municipio. Se encontraron luego de charla con pares, hospitales que no correspondian a la misma localidad del paciente, muchos de ellos ubicados en capital federal o provincias aledañas a la Provincia de Buenos Aires.
