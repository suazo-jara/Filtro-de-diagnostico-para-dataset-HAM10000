# Filtro de diagnóstico para dataset HAM10000
Script que filtra las imágenes del [dataset HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T) por determinado diagnóstico clínico.

El script logra extraer todas las imágenes correspondientes a un diagnóstico clínico de lesión dermatológica determinado (por defecto: **mel**, de melanoma) y las guarda en una carpeta junto a un nuevo archivo de metadatos, correspondiente a los imágenes extraídas.

Instrucciones:

1. Descargue el archivo filtro.py
2. Guarde el archivo filtro.py en la misma carpeta en que se encuentran los archivos 'HAM10000_images_part_1.zip', 'HAM10000_images_part_2.zip' y 'HAM10000_metadata'.
3. Ejecute el script.