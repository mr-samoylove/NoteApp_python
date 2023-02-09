from tkinter import *

import src

window = Tk()
window.title("NoteApp - made by mr.samoylove")
window.geometry("800x600")

table_frame = Frame(window)
table_frame.pack(anchor=N)

buttons_frame = Frame(window)
buttons_frame.pack(anchor=S)

table = src.Table(table_frame)
buttons = src.Buttons(buttons_frame, table)

window.mainloop()
