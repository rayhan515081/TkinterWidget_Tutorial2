import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Test Entry Widget')
window.geometry('400x400')  

output_string = tk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_string)

# Define the button command functions
def get_button1_text():
    output_string.set("You clicked Button 1")

def get_button2_text():
    output_string.set("You clicked Button 2")

# Buttons
button_1 = ttk.Button(master=window, text='BUTTON 1', command=get_button1_text)
button_2 = ttk.Button(master=window, text='BUTTON 2', command=get_button2_text)

# Pack widgets
button_1.pack()
button_2.pack()
output_label.pack()

#Label Frame 
button_frame = ttk.LabelFrame(master=window, text="Buttons Frame")
button_frame.pack(pady=20) 

button_1 = ttk.Button(master=button_frame, text='BUTTON 1', command=get_button1_text)
button_2 = ttk.Button(master=button_frame, text='BUTTON 2', command=get_button2_text)

button_1.pack(side=tk.LEFT, padx=10, pady=10)
button_2.pack(side=tk.LEFT, padx=10, pady=10)

output_label.pack(pady=10)

window.mainloop()
