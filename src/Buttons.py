from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

import src.Exporter


class Buttons:
    def __init__(self, frame, table):
        self.creation_button = ttk.Button(frame, text="Create new note", command=self.creation)
        self.creation_button.pack()

        self.refresh_button = ttk.Button(frame, text="Refresh table", command=table.refresh)
        self.refresh_button.pack()

    def creation(self):
        creation_window = Tk()
        creation_window.title("Create new note")
        creation_window.geometry("800x600")

        ttk.Label(creation_window, text="Enter the name of your note", padding=8).pack()

        entry = ttk.Entry(creation_window)
        entry.pack()

        ttk.Label(creation_window, text="Below is the note body", padding=8).pack()

        word_editor = ScrolledText(creation_window, wrap="word")
        word_editor.pack(anchor=S, fill=BOTH)

        save_button = ttk.Button(creation_window, text="Save", padding=8,
                                 command=lambda: [src.Exporter.export_to_json(entry.get(), word_editor.get("1.0", END)),
                                                  creation_window.destroy()])
        save_button.pack()

        creation_window.mainloop()
