from encodings.punycode import T
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Simple grading system")
window.geometry("800x700")

title_label = ttk.Label(master = window, text="Enter Student Grade:",font='Calibri 32 bold', borderwidth=1, relief='flat')
title_label.grid(row=0, column=1)
result_label=ttk.Label(master=window, text="GRADE:", font='Calibri 20 bold',foreground='green',borderwidth=5, relief='raised')
result_label.grid(row=7,column=0,pady=20)
mark_label=ttk.Label(master=window, text='Mark(%)', font='calibri 14', anchor='w')
mark_label.grid(row=4,column=0,padx=10,pady=10)
mark_entry=ttk.Entry(master=window,font='calibri 14')
mark_entry.grid(row=4,column= 1,padx=10,pady=10)

def get_button_1_text():
    if mark_entry.get().isdigit():
        mark=int(mark_entry.get())
        if mark_entry >= 90:
            print("A")
        elif mark_entry >= 80:
            print("B")
        elif mark_entry >= 70:
            print("C")
        elif mark_entry >= 60:
            print("D")
        elif mark_entry >= 50:
           print("E")
        elif mark_entry <50:
            print("F")
        else :
          print("Invalid input. Please enter a number between 0 and 100.")

button_1=ttk.Button(master=window, text ='Submit',width=10,command = get_button_1_text)
button_1.grid(row = 5, column = 2,sticky ='se',padx=10,pady=10)

fields = ['First Name', 'Last Name','Subject']

entries=[]

for i, field in enumerate(fields):
    label= ttk.Label(window, text=field, font='Calibri 14',anchor='w')
    label.grid(row=i+1, column=0, sticky='w',padx=10,pady=10)
    entry = ttk.Entry (window,font = 'Calibri 14')
    entry.grid(row=i+1,column=1,sticky= 'we', padx=10,pady=10)


entries.append(entry)

window.mainloop()