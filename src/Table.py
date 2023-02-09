from tkinter import *
from tkinter import ttk

import src.Data_manager


class Table:
    def __init__(self, table_frame):
        columns = ("id", "name", "creation_date", "last_modified")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID", command=lambda: self.sort(0, False))
        self.tree.heading("name", text="Name", command=lambda: self.sort(1, False))
        self.tree.heading("creation_date", text="Сreation date", command=lambda: self.sort(2, False))
        self.tree.heading("last_modified", text="Last modified", command=lambda: self.sort(3, False))

        self.tree.column("#1", stretch=NO, width=25)
        self.tree.column("#2", stretch=NO, width=240)
        self.tree.column("#3", stretch=NO, width=120)
        self.tree.column("#4", stretch=NO, width=120)

        self.scrollbar = Scrollbar(table_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.refresh()

    def sort(self, col, reverse):
        l = sorted([(self.tree.set(k, col), k) for k in self.tree.get_children("")], reverse=reverse)
        for index, (_, k) in enumerate(l):
            self.tree.move(k, "", index)
        self.tree.heading(col, command=lambda: self.sort(col, not reverse))

    def refresh(self):
        for item in self.tree.selection():
            self.tree.selection_remove(item)
        for item in self.tree.get_children():
            self.tree.delete(item)
        notes = src.Data_manager.import_from_json()
        if notes is not None:
            for note in notes:
                self.tree.insert('', END,
                                 values=(note['id'], note['name'], note['creation_date'], note['last_modified']))
