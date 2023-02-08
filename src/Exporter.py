import json
import os
from datetime import datetime

from src.constants import date_format, data_filename


def export_to_json(name, text):
    new_note = dict(name=name, creation_date=datetime.now().strftime(date_format),
                               last_modified=datetime.now().strftime(date_format), text=text)

    if os.path.isfile(data_filename) is False:
        with open(data_filename, 'w', encoding='utf-8') as f:
            json.dump([new_note, ], f, indent=4)
    else:
        with open(data_filename, 'r', encoding='utf-8') as f:
            all_notes = json.load(f)

        all_notes.append(new_note)

        with open(data_filename, 'w', encoding='utf-8') as f:
            json.dump(all_notes, f, indent=4)

