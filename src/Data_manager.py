import json
import os
from datetime import datetime

from src.constants import date_format, data_filename, json_encoding


def update_json(note: list, new_name='default_name', new_text='default_text', delete=False, read=False):
    with open(data_filename, 'r', encoding=json_encoding) as f:
        all_notes = list(json.load(f))
    for old_note in all_notes:
        if old_note['name'] == note[0] \
                and old_note['creation_date'] == note[1] \
                and old_note['last_modified'] == note[2]:
            if read:
                return old_note['name'], old_note['text']
            elif delete:
                all_notes.remove(old_note)
                print(f"{note[0]} successfully deleted")
            else:
                old_note['name'] = new_name
                old_note['last_modified'] = datetime.now().strftime(date_format)
                old_note['text'] = new_text
                print(f"{note[0]} successfully edited")
            break
    else:
        print("No such note has been found in data while reading data")
    with open(data_filename, 'w', encoding=json_encoding) as f:
        json.dump(all_notes, f, indent=4)


def append_to_json(name, text):
    new_note = dict(name=name, creation_date=datetime.now().strftime(date_format),
                    last_modified=datetime.now().strftime(date_format), text=text)

    if os.path.isfile(data_filename) is False:
        with open(data_filename, 'w', encoding=json_encoding) as f:
            json.dump([new_note, ], f, indent=4)
        print("Data created")
    else:
        with open(data_filename, 'r', encoding=json_encoding) as f:
            all_notes = json.load(f)

        all_notes.append(new_note)

        with open(data_filename, 'w', encoding=json_encoding) as f:
            json.dump(all_notes, f, indent=4)

        print("Data appended")


def import_from_json():
    if os.path.isfile(data_filename) is False:
        print(f"There are no notes or file {data_filename} doesn't exist. Create the first note")
        return None
    else:
        with open(data_filename, 'r', encoding='utf-8') as f:
            all_notes = json.load(f)
        return all_notes

