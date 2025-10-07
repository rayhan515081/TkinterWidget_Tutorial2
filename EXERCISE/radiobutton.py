import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x400")
window.title("Tkinter Radio Button Widget")

radiobutton_frame = tk.Frame(window)

int_var = tk.IntVar()

def radio_selected():
    val = int_var.get()
    output_label.config(text=f"You selected option {val}")


Int_radiobutton_1 = ttk.Radiobutton(radiobutton_frame, value=1, variable=int_var, text="This is One", command=radio_selected)
Int_radiobutton_2 = ttk.Radiobutton(radiobutton_frame, value=2, variable=int_var, text="This is Two", command=radio_selected)

output_label = ttk.Label(window, text="Select an option above")

radiobutton_frame.pack(pady=20)
Int_radiobutton_1.pack(anchor="w")
Int_radiobutton_2.pack(anchor="w")
output_label.pack(pady=10)

window.mainloop()



