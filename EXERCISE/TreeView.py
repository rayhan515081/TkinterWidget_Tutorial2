import tkinter as tk
from tkinter import ttk

root = tk.Tk() 

root.title("Tkinter TreeView")
root.geometry("500x300")

treeview  = ttk.Treeview(columns=("Salary","Bonus"))

treeview.heading("#0", text="Employee")
treeview.heading("Salary", text = "Salary")
treeview.heading("Bonus", text = "Bonus")

icon_city = tk.PhotoImage(file="./assets/city.png")
icon_male = tk.PhotoImage(file="./assets/male.png")
icon_female= tk.PhotoImage(file="./assets/female.png")

level1 = treeview.insert("", tk.END, text="San Jose",image=icon_city)


treeview.insert(level1, tk.END,text="Jane Smith", values=(f"${100000: ,}", f"${8000: ,}"))
treeview.insert(level1, tk.END,text="John Doe", values=(f"${120000: ,}", f"${9000: ,}"))


treeview.pack(padx=10,pady=10, expand=True, fill=tk.BOTH)

root.mainloop()



