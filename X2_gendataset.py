import os
import cv2
import numpy as np

# Directorio raíz donde están las imágenes organizadas en subcarpetas
dataset_dir = r"C:\Users\jorge\UdeA\Deep Learning\CICDDoS2019\cicddos2019_img"

# Listas para almacenar imágenes y etiquetas
imagenes = []
etiquetas = []

# Recorremos las carpetas en el directorio raíz
for etiqueta_carpeta in os.listdir(dataset_dir):
    carpeta_path = os.path.join(dataset_dir, etiqueta_carpeta)
    
    if os.path.isdir(carpeta_path):  # Verificamos si es una carpeta
        # Iterar sobre cada imagen en la subcarpeta
        for nombre_imagen in os.listdir(carpeta_path):
            imagen_path = os.path.join(carpeta_path, nombre_imagen)
            
            # Cargar la imagen usando OpenCV
            imagen = cv2.imread(imagen_path)
            
            if imagen is not None:  # Si la imagen se cargó correctamente
                
                # Guardamos la imagen y su etiqueta
                imagenes.append(imagen)
                etiquetas.append(etiqueta_carpeta)  # Usamos el nombre de la carpeta como etiqueta

# Convertir listas a arrays de NumPy para ser usados en ML/DL
X = np.array(imagenes)
y = np.array(etiquetas)

print(f"Dataset creado con {len(X)} imágenes y etiquetas.")
