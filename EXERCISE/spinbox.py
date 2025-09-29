import tkinter as tk
from tkinter import ttk

#This section creates the Tkinter window and adds the required elemnts to it
window = tk.Tk()
window.title("Tkinter Spinbox Widget")
window.geometry("400x400")

#This is our spinbox
int_var = tk.IntVar()
Number_Spinbox = ttk.Spinbox(window, from_=0, to=100, increment=.01, textvariable = int_var, font = 'Calibri 24 bold')

#Pack elements in frames ready to push onto form/window
Number_Spinbox.pack

#run the program to generate window with all packed elements for user interaction
window.mainloop()

