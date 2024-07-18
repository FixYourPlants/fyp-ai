import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

def main():
    # Initialize the API
    api = KaggleApi()
    api.authenticate()

    # Name of the dataset on Kaggle (e.g., 'alejandrosantiago/plant-sickness')
    dataset = 'alejandrosantiago/plant-sickness'

    # Destination directory where the dataset will be downloaded
    destination_folder = 'datasets'

    # Create the directory if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Download the dataset
    api.dataset_download_files(dataset, path=destination_folder, unzip=True, quiet=False)

    # Paths of the source and destination folders
    origin = os.path.join(destination_folder, 'mixed/mixed')
    tmp = os.path.join(destination_folder, 'tmp')
    destination = os.path.join(destination_folder, 'mixed')

    # Move the folder
    try:
        shutil.move(origin, tmp)
        if os.path.exists(destination):
            shutil.rmtree(destination)
        os.rename(tmp, destination)
        print(f"Folder moved from {origin} to {destination}")
    except Exception as e:
        print(f"An error occurred while moving the folder: {e}")

    print(f'Dataset "{dataset}" downloaded to "{destination_folder}".')

if __name__ == "__main__":
    main()



