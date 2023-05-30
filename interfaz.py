import tkinter
from tkinter import Tk
from tkinter import ttk

def hacer_click():
    seleccionado.set(None)

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=4)

seleccionado = tkinter.IntVar()

R1 = ttk.Radiobutton(window, text="Opcion 1", value='1', variable=seleccionado)
R2 = ttk.Radiobutton(window, text="Opcion 2", value='2', variable=seleccionado)
R3 = ttk.Radiobutton(window, text="Opcion 3", value='3', variable=seleccionado)

R1.grid(column=0, row=1, pady=5, padx=5)
R2.grid(column=0, row=2, pady=5, padx=5)
R3.grid(column=0, row=3, pady=5, padx=5)

boton = ttk.Button(window, text="reiniciar", command=hacer_click)
boton.grid(column=0, row=4)

window.mainloop()


