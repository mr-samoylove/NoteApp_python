from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

import src.Data_manager


class Buttons:
    def __init__(self, frame, table):
        self.table = table

        self.note_id_selected = None
        table.tree.bind("<<TreeviewSelect>>", lambda _: self.init_selection(table))

        self.creation_button = ttk.Button(frame, text="Create new note", command=self.edit)
        self.creation_button.pack()

        self.edit_button = ttk.Button(frame, text="Edit note", state=DISABLED,
                                      command=lambda: self.edit(update=True))
        self.edit_button.pack()

        self.delete_button = ttk.Button(frame, text="Delete note", state=DISABLED,
                                        command=lambda: [
                                            src.Data_manager.update_json(self.note_id_selected, delete=True),
                                            self.edit_button.configure(state=DISABLED),
                                            self.delete_button.configure(state=DISABLED),
                                            self.table.refresh()])
        self.delete_button.pack()

        self.refresh_button = ttk.Button(frame, text="Refresh table", command=table.refresh)
        self.refresh_button.pack()

    def init_selection(self, table):
        if len(table.tree.selection()) > 0:
            self.note_id_selected = table.tree.item(table.tree.selection())['values'][0]
            self.edit_button['state'] = NORMAL
            self.delete_button['state'] = NORMAL
            print("Selected note ID is:", self.note_id_selected)
        else:
            self.note_id_selected = None
            self.edit_button['state'] = DISABLED
            self.delete_button['state'] = DISABLED

    def edit(self, update=False):
        creation_window = Tk()
        creation_window.title("Edit note")
        creation_window.geometry("800x600")

        ttk.Label(creation_window, text="Enter the name of your note", padding=8).pack()

        entry = ttk.Entry(creation_window)
        entry.pack()

        ttk.Label(creation_window, text="Below is the note body", padding=8).pack()

        word_editor = ScrolledText(creation_window, wrap="word")
        word_editor.pack(anchor=S, fill=BOTH)

        save_button = ttk.Button(creation_window, text="Save", padding=8)
        if update:
            save_button.configure(
                command=lambda: [
                    src.Data_manager.update_json(self.note_id_selected, entry.get(), word_editor.get("1.0", END)),
                    creation_window.destroy(),
                    self.edit_button.configure(state=DISABLED),
                    self.delete_button.configure(state=DISABLED),
                    self.table.refresh()])
        else:
            save_button.configure(
                command=lambda: [src.Data_manager.append_to_json(entry.get(), word_editor.get("1.0", END)),
                                 creation_window.destroy(),
                                 self.edit_button.configure(state=DISABLED),
                                 self.delete_button.configure(state=DISABLED),
                                 self.table.refresh()])
        save_button.pack()

        if update:
            name, text = src.Data_manager.update_json(self.note_id_selected, read=True)
            entry.insert(0, name)
            word_editor.insert(INSERT, text)
            word_editor.focus()

        creation_window.mainloop()
