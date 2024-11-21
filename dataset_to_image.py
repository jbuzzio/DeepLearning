import numpy as np
import pandas as pd
from PIL import Image
import os

# Cargar el dataset real (reemplaza con tu archivo o método de carga)
# dataset = pd.read_csv('tu_archivo.csv')  # Cargar el dataset real

dataset = pd.read_csv(r"C:\Users\jorge\CICDDoS2019\01-12\Syn.csv")


#dataset = pd.concat([dataset], ignore_index=True)

# Crear un directorio para guardar las imágenes
output_dir = r"C:\Users\jorge\CICDDoS2019\01-12\SYN_TEST_KEVIN"
#os.makedirs(output_dir, exist_ok=True)
# Paso 1: Dividir el dataset en bloques de 180 filas
num_rows = 180
total_images = len(dataset) // num_rows  # Número de imágenes posibles

dataset = dataset[[' Destination Port', ' Flow Duration', ' Total Fwd Packets',
       ' Total Backward Packets', 'Total Length of Fwd Packets',
       ' Total Length of Bwd Packets', ' Fwd Packet Length Max',
       ' Fwd Packet Length Min', ' Fwd Packet Length Mean',
       ' Fwd Packet Length Std', 'Bwd Packet Length Max',
       ' Bwd Packet Length Min', ' Bwd Packet Length Mean',
       ' Bwd Packet Length Std', 'Flow Bytes/s', ' Flow Packets/s',
       ' Flow IAT Mean', ' Flow IAT Std', ' Flow IAT Max', ' Flow IAT Min',
       'Fwd IAT Total', ' Fwd IAT Mean', ' Fwd IAT Std', ' Fwd IAT Max',
       ' Fwd IAT Min', 'Bwd IAT Total', ' Bwd IAT Mean', ' Bwd IAT Std',
       ' Bwd IAT Max', ' Bwd IAT Min', 'Fwd PSH Flags', ' Fwd Header Length',
       ' Bwd Header Length', 'Fwd Packets/s', ' Bwd Packets/s',
       ' Min Packet Length', ' Max Packet Length', ' Packet Length Mean',
       ' Packet Length Std', ' Packet Length Variance',
       ' SYN Flag Count', ' ACK Flag Count', ' URG Flag Count', ' CWE Flag Count',
       ' Down/Up Ratio', ' Average Packet Size',
       ' Avg Fwd Segment Size', ' Avg Bwd Segment Size','Init_Win_bytes_forward',
       ' Init_Win_bytes_backward', ' act_data_pkt_fwd',
       ' min_seg_size_forward', 'Active Mean', ' Active Std', ' Active Max',
       ' Active Min', 'Idle Mean', ' Idle Std', ' Idle Max', ' Idle Min',
       ' Label']]

etiquetas = dataset[' Label']
datos = dataset.iloc[:,:-1]


datos.replace([np.inf, -np.inf], np.nan, inplace=True)
datos = datos.dropna()


# Paso 2: Iterar sobre el dataset en bloques de 180 filas
for i in range(total_images):
    # Obtener las 180 filas correspondientes al bloque actual
    block_data = datos.iloc[i*num_rows:(i+1)*num_rows]

    # Normalizar los datos entre 0 y 255
    
    block_normalized = (block_data - block_data.min(axis=0)) / (block_data.max(axis=0) - block_data.min(axis=0)) * 255
    block_normalized = block_normalized.astype(np.uint8)

    # Paso 3: Convertir el bloque en una imagen de 60x60 con 3 canales (RGB)
    image_data = block_data.values.reshape((60, 60, 3))

    # Crear la imagen
    image = Image.fromarray(image_data, 'RGB')

    # Guardar la imagen con un nombre único (por ejemplo, "image_0.png", "image_1.png", etc.)
    image_path = os.path.join(output_dir, f"syn_{i}.png")
    image.save(image_path)

    # Opción: Mostrar progreso
    if i % 100 == 0:
        print(f"{i}/{total_images} imágenes generadas...")

print("Generación de imágenes completada.")
