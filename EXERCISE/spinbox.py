import tkinter as tk
from tkinter import ttk

def update_label(*args):
    value = value_var.get()
    display_label.config(text=f"Selected Value: {value}")

#This section creates the Tkinter window and adds the required elemnts to it
window = tk.Tk()
window.title("Tkinter Spinbox Widget")
window.geometry("400x400")

value_var = tk.DoubleVar()
value_var.trace_add("write", update_label)  

number_spinbox = ttk.Spinbox(
    window,
    from_=0,
    to=100,
    increment=0.01,
    textvariable=value_var,
    font='Calibri 24 bold'
)
number_spinbox.pack(pady=20)

Number_spinbox = ttk.spinbox('Maths','English','Science','Computing','Latin','Arabic','Social Studies','Sports Science')

#This is our spinbox
int_var = tk.IntVar()
Number_Spinbox = ttk.Spinbox(window, from_=0, to=100, increment=.01, textvariable = int_var, font = 'Calibri 24 bold')

#Pack elements in frames ready to push onto form/window
Number_Spinbox.pack

#run the program to generate window with all packed elements for user interaction
window.mainloop()
