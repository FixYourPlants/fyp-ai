import os
import shutil
import random

# Define los porcentajes para train, test, y valid
train_pct = 0.7
test_pct = 0.2
valid_pct = 0.1

# Directorio de origen y directorios de destino
source_dir = 'mixed'
train_dir = 'train'
test_dir = 'test'
valid_dir = 'valid'

def create_dirs():
    """Crea los directorios de destino si no existen"""
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)
    print(f"Directorios '{train_dir}', '{test_dir}', y '{valid_dir}' creados o existentes.")

def copy_files(files, source_subfolder_path, destination_dir, subfolder):
    """Copia archivos a las carpetas de destino"""
    dest_subfolder = os.path.join(destination_dir, subfolder)
    os.makedirs(dest_subfolder, exist_ok=True)
    for file in files:
        shutil.copy(os.path.join(source_subfolder_path, file), os.path.join(dest_subfolder, file))
    print(f"Copiados {len(files)} archivos a '{dest_subfolder}'")

def distribute_files():
    """Distribuye los archivos en los directorios de train, test y valid"""
    # Obtener todas las subcarpetas en el directorio de origen
    subfolders = [f.name for f in os.scandir(source_dir) if f.is_dir()]
    print(f"Subcarpetas encontradas en '{source_dir}': {subfolders}")

    for subfolder in subfolders:
        subfolder_path = os.path.join(source_dir, subfolder)
        print(f"\nProcesando subcarpeta '{subfolder}'")

        # Listar todos los archivos en la subcarpeta
        files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        print(f"Archivos encontrados en '{subfolder}': {len(files)}")

        # Mezclar los archivos aleatoriamente
        random.shuffle(files)

        # Calcular los tamaños para train, test y valid
        train_size = int(train_pct * len(files))
        test_size = int(test_pct * len(files))
        valid_size = len(files) - train_size - test_size

        # Obtener las listas de archivos para cada conjunto
        train_files = files[:train_size]
        test_files = files[train_size:train_size + test_size]
        valid_files = files[train_size + test_size:]

        # Copiar archivos a los directorios de train, test y valid
        copy_files(train_files, subfolder_path, train_dir, subfolder)
        copy_files(test_files, subfolder_path, test_dir, subfolder)
        copy_files(valid_files, subfolder_path, valid_dir, subfolder)

    print("\nDistribución de archivos completada.")

def main():
    print("Iniciando la distribución de archivos...")
    create_dirs()
    distribute_files()
    print("Proceso terminado.")

if __name__ == "__main__":
    main()

