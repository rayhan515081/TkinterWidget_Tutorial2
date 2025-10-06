import tkinter as tk
from tkinter import ttk

# Create main window
window = tk.Tk()
window.geometry("400x400")
window.title("Tkinter Checkbutton Widget")

# Label to update
message_label = ttk.Label(window, text="", font='Calibri 14')
message_label.pack(pady=20)

# Function to update label based on checkbox state
def update_label():
    if bool_var.get():
        message_label.config(text="I am very HAPPY for you!")
    else:
        message_label.config(text="I am sorry, BETTER days are ahead!")

# Boolean variable for Checkbutton
bool_var = tk.BooleanVar()

# Checkbutton with on/off behavior
check_button = ttk.Checkbutton(
    window,
    text="Are you happy?",
    variable=bool_var,
    onvalue=True,
    offvalue=False,
    command=update_label
)
check_button.pack()

# Run the GUI event loop
window.mainloop()