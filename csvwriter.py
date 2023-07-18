import csv
import logging


class CSVWriter:
    """CSVWriter is a class for writing data to a CSV file."""

    def __init__(self, file_path):
        """The constructor for CSVWriter class."""
        self.file_path = file_path

    def write(self, data, headers):
        """Writes data to the CSV file."""
        logging.info(f"Writing data to {self.file_path}")
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
