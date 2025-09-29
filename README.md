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
- Codigo por clasificación: [clasificacion.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/clasificacion.py) Analisis de cantidad de coincidencias por cada clasificacion del caso.
- Codigos por municipio: [municipio.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/municipio.py) Analisis por rangos, contar la cantidad de municipios tenian X cantidad casos en un rango.
- Codigos por municipio: [municipio2.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/municipio2.py) Analisis de eventos por municipio.
- Codigos por municipio: [municipio3.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/municipio3.py) Analisis de casos por municipio.

## 2 - Analisis clínico.
Durante este analisis se utilizo un CSV en la cual se filtraron las repeticiones de DNI con First match, first keep, chequeando que no haya otro evento en el mismo DNI, dado que esto altera las mediciones de la mediana.
Tambien se realizo un filtro de outliers y diferencias de dias mayores a 0 (Fechas de inicio de sintomas superiores posteriores a la fecha de consulta).
- Analisis de calculo de dias y mediana: [mediana_sin_outliers.py](https://github.com/MaxeeBenet/cienciadedatos/blob/main/mediana_sin_outliers.py)

## 3 - Seccion clínica.
