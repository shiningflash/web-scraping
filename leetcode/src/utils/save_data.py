import csv
import os
from typing import Dict, Any


def save_to_csv(row_data: Dict[str, Any], csv_file_path: str) -> None:
    """
    Save a row of data to a CSV file. Creates the file and writes the header if it does not exist.
    
    Args:
        row_data (Dict[str, Any]): A dictionary containing the row data to save.
        csv_file_path (str): The file path for the CSV file.
    
    Raises:
        ValueError: If `row_data` is empty.
        IOError: If there is an error writing to the CSV file.
    """
    if not row_data:
        raise ValueError("row_data cannot be empty. Provide at least one key-value pair.")
    
    file_exists = os.path.isfile(csv_file_path)
    
    try:
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=row_data.keys())
            if not file_exists:
                # Write header only if the file does not exist
                writer.writeheader()
            writer.writerow(row_data)
    except IOError as e:
        raise IOError(f"Failed to write to the CSV file: {csv_file_path}. Error: {e}")

