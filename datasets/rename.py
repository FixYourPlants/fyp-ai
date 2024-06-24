import os


def rename_files(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    # Sort the list of files
    files.sort()

    # Initialize the counter
    counter = 1

    # Iterate over all the files in the directory
    for file in files:
        # Get the full path of the file
        full_path = os.path.join(directory, file)

        # Check that it is a file and not a directory
        if os.path.isfile(full_path):
            # Create the new filename with two digits
            new_name = f"{counter:04d}{os.path.splitext(file)[1]}"
            new_full_path = os.path.join(directory, new_name)

            # Rename the file
            print(f"Renaming {full_path} to {new_full_path}")
            os.rename(full_path, new_full_path)

            # Increment the counter
            counter += 1


if __name__ == "__main__":
    # Specify the directory where the files are located
    directory = "./train/Tomato leaf/Yellow virus"

    # Call the function to rename the files
    rename_files(directory)
