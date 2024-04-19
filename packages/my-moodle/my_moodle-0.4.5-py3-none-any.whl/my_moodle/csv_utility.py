"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
CSV utility Methods
"""

from csv import DictWriter
import logging


def save_json_list_to_csv(json_list: list[dict], filename: str) -> None:
    """Save data to a CSV file.

    Args:
        data (list): List of dictionaries containing data to be saved.
        filename (str): Name of the CSV file to save.
    """
    if not json_list:
        logging.warning("No data to save.")
        return

    fieldnames = set().union(*(json_dict.keys() for json_dict in json_list))

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        dict_writer = DictWriter(file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(json_list)


def save_json_fields_list_to_csv(
    json_list: list[dict], fieldnames: list, filename: str
) -> None:
    """Save data to a CSV file.

    Args:
        data (list): List of JSON dictionaries containing data to be saved.
        fieldnames (list): List of field names to save.
        filename (str): Name of the CSV file to save.
    """
    if not json_list:
        logging.warning("No data to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        dict_writer = DictWriter(file, fieldnames=fieldnames)
        dict_writer.writeheader()
        for json_dict in json_list:
            filtered_row = {
                key: value for key, value in json_dict.items() if key in fieldnames
            }
            dict_writer.writerow(filtered_row)
