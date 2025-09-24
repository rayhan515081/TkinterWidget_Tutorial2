import tkinter as tk
from tkinter import ttk

def submit_text():
    original_text = string_var.get()
    edited_text = original_text + "_edited"
    result_label.config(text=edited_text)

window = tk.Tk()
window.title('tkinter Text Entry Widget')
window.geometry('400x400')

string_var = tk.StringVar()
Text_entry = ttk.Entry(master=window, textvariable=string_var, font='Calibri 24 bold', show='*')
Text_entry.pack(pady=20)

Text_entry.config(justify='center')

submit_button = ttk.Button(window, text="Submit", command=submit_text)
submit_button.pack(pady=10)

result_label = ttk.Label(window, text="", font='Calibri 20')
result_label.pack(pady=20)

window.mainloop()