import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import BooleanVar
from tkinter import IntVar
from tkinter import DoubleVar

window = tk.Tk()
window.title("Stock System")
window.geometry("500x500")


fields = ['Product ID' ,'Product Name', 'Product Description' ,'Price' ,'Quantity' ,'Limited']

entries=[]

for i, field in enumerate(fields):
    label = ttk.Label(window, text = field , font = 'calibri 24 bold', anchor = 'w')
    label.grid(row=i+1, column=0, sticky='w', padx=10, pady=10)

text_entry= ttk.Entry(window,textvariable = StringVar, font='calibri 14')
text_entry.grid(row = 0, column=2, padx=10, pady=10)
text_entry= ttk.Entry(window,textvariable = StringVar, font='calibri 14')
text_entry.grid(row = 1, column=2, padx=10, pady=10)
text_entry= ttk.Entry(window,textvariable = StringVar, font='calibri 14')
text_entry.grid(row = 2, column=2, padx=10, pady=10)
text_entry= ttk.Entry(window,textvariable = DoubleVar, font='calibri 14')
text_entry.grid(row = 3, column=2, padx=10, pady=10)
text_entry= ttk.Entry(window,textvariable = int, font='calibri 14')
text_entry.grid(row = 4, column=2, padx=10, pady=10)
text_entry= ttk.Entry(window,textvariable = bool, font='calibri 14')
text_entry.grid(row = 5, column=2, padx=10, pady=10)



 