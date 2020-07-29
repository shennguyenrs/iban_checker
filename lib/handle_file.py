import csv
import os

def handle_file(file_name):
    """
    Create database for other functions

    Parameters:
    -----------
        file_name : str
            Name of the file

    Returns:
    --------
        to_data : array
            Database from file

    Raises:
    -------
        Missing Header
        Wrong Path

    """

    # Module name due to run python3 -m
    os.chdir(os.path.dirname(__file__))
    os.chdir("..")
    to_parent_dir = os.getcwd()

    # Default name of database folder
    dir_name = "resources"

    path = os.path.join(to_parent_dir, dir_name, file_name)

    # Check path
    if os.path.isfile(path):
        with open(path) as file:
            reader = csv.reader(file)
            header = next(reader)

            # Write file to array
            to_data = []
            if header is not None:
                for row in reader:
                    to_data.append(row)

                return to_data

            # Raise missing header
            else:
                print("Header of file " + file_name + " is not null")
                print("Please add header to fix")

    # Raise wrong path
    else:
        print("Check path of the file: " + file_name)
        print(path)
