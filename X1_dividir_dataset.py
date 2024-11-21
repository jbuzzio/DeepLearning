import pandas as pd

dataset = pd.read_csv(r"C:\Users\jorge\OneDrive - UNIDAD EJECUTORA 002 INICTEL UNI\PRIVADO\UdeA\2024-2\Deep Learning\01-12\TFTP.csv")

# Crear un directorio para guardar las imágenes
#output_dir = r"C:\Users\jorge\OneDrive - UNIDAD EJECUTORA 002 INICTEL UNI\PRIVADO\UdeA\2024-2\Deep Learning\01-12\DrDos_MSSQL_img"

# Dividir el dataset en dos partes:
# 1. Filas cuya etiqueta sea 'BENIGN'
benign_data = dataset.loc[dataset[' Label'] == 'BENIGN']

# 2. Filas cuya etiqueta NO sea 'BENIGN'
non_benign_data = dataset.loc[dataset[' Label'] != 'BENIGN']

# Guardar los datasets en archivos CSV
benign_data.to_csv('TFTP_benign_data.csv', index=False)
non_benign_data.to_csv('TFTP_non_benign_data.csv', index=False)

print("Los datasets se han guardado correctamente.")
