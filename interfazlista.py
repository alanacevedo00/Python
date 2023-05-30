import tkinter
from tkinter import END, Tk
from tkinter import ttk

master = Tk()
elemento = tkinter.StringVar()
listbox = tkinter.Listbox(master)
for item in ["Velez", "Boca", "Estudiantes", "River", "Racing", "Independiente", "San Lorenzo"]:
 listbox.insert(END, item)
listbox.pack()

label = tkinter.Label(text="Lista de clubes argentinos")
label.pack()

master.mainloop()