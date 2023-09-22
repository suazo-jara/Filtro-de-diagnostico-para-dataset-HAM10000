import os
import pandas as pd
from zipfile import ZipFile

zip_file1 = 'HAM10000_images_part_1.zip'
zip_file2 = 'HAM10000_images_part_2.zip'
output_folder = 'imagenes_mel'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

metadata = pd.read_csv('HAM10000_metadata')

# Filtrar las filas donde dx es igual a 'mel'
mel_data = metadata[metadata['dx'] == 'mel']

# Lista para almacenar los nombres de las imágenes con 'mel'
mel_image_names = mel_data['image_id'].tolist()

# Función para extraer imágenes de los archivos ZIP
def extract_images(zip_file, image_names, output_folder):
    with ZipFile(zip_file, 'r') as zip:
        for image_name in image_names:
            image_name_with_ext = image_name + '.jpg'
            if image_name_with_ext in zip.namelist():
                with zip.open(image_name_with_ext) as file:
                    with open(os.path.join(output_folder, image_name_with_ext), 'wb') as output_file:
                        output_file.write(file.read())

# Extraer las imágenes con 'mel' en el nombre
extract_images(zip_file1, mel_image_names, output_folder)
extract_images(zip_file2, mel_image_names, output_folder)

extracted_metadata = mel_data.copy()

# Ruta para el archivo CSV de metadatos de las imágenes extraídas
output_metadata_file = os.path.join(output_folder, 'HAM10000_mel_metadata')

# Guardar los metadatos de las imágenes extraídas en un archivo CSV
extracted_metadata.to_csv(output_metadata_file, index=False)