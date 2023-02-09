import json
import os
from datetime import datetime

from src.constants_and_globals import *


def update_json(target_note_id: int, new_name='default_name', new_text='default_text', delete=False, read=False):
    with open(data_filename, 'r', encoding=json_encoding) as f:
        all_notes = list(json.load(f))
    for old_note in all_notes:
        if old_note['id'] == target_note_id:
            if read:
                return old_note['name'], old_note['text']
            elif delete:
                all_notes.remove(old_note)
                print(f"Note with ID:{target_note_id} is successfully deleted")
            else:
                old_note['name'] = new_name
                old_note['last_modified'] = datetime.now().strftime(date_format)
                old_note['text'] = new_text
                print(f"Note with ID:{target_note_id} is successfully edited")
            break
    else:
        print("No such note has been found in data while reading data")
    with open(data_filename, 'w', encoding=json_encoding) as f:
        json.dump(all_notes, f, indent=4)


def append_to_json(name, text):
    global LAST_USED_MAX_ID
    LAST_USED_MAX_ID += 1
    new_note = dict(id=LAST_USED_MAX_ID, name=name, creation_date=datetime.now().strftime(date_format),
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
        global LAST_USED_MAX_ID
        LAST_USED_MAX_ID = max(note['id'] for note in all_notes)
        return all_notes
