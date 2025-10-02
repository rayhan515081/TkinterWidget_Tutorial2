import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Simple grading system")
window.geometry("800x700")

output_label = ttk.Title(master = window, text="Enter Student Grade:",font='Calibri 32 bold', borderwidth=1, relief='flat')


string_var = tk.StringVar()
Text_entry = ttk.Entry(master=window, textvariable=string_var, font='Calibri 24 bold')


output_label.pack()
Text_entry.pack(pady=20)

window.mainloop()
