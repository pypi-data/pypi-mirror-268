import csv
import json
import os


def get_last_id_in_csv_file(file_name, column="id"):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in reader:
            # Assign the last row to the last_row variable
            last_row = row

        try:
            # Get the value you want from the last row by column name
            desired_value = last_row[column]

            return int(desired_value)
        except:
            return -1


def load_json_from_file(path):
    """
    Load json object from file.
    """
    with open(path, "r") as file:
        return json.load(file)


def write_json_to_file(path, data, indent: int = 4):
    """
    Write json object to file.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=indent)


class LyFile:
    def __init__(self, path: str = "lyfile.txt"):
        self.path = path

    def create(self):
        """
        Creates a blank file at path.
        """
        # Split path into directory and filename
        directory, _ = os.path.split(self.path)

        # If directory was included, create it if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        open(self.path, "w").close()  # Create file

    def append(self, text):
        """
        Appends text to file at path.
        """
        with open(self.path, "a") as file:
            file.write(f"{text}\n")
