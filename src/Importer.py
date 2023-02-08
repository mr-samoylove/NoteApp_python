import json
import os
from datetime import datetime

from src.constants import data_filename


def import_from_json():
    if os.path.isfile(data_filename) is False:
        print(f"There are no notes or file {data_filename} doesn't exist. Create the first note")
        return None
    else:
        with open(data_filename, 'r', encoding='utf-8') as f:
            all_notes = json.load(f)
        return all_notes

