import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tkinter Label Widget")
window.geometry("500x500")

output_label = ttk.Label(master = window, text="Rayhan is Da Goat!",font='Calibri 24 bold',foreground= 'green', underline = 4)

output_label.pack()

window.mainloop()
