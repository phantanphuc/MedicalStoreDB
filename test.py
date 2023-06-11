import tkinter as tk
from tkinter import ttk

def on_select(event):
    print("Selected value:", combobox.get())

root = tk.Tk()
entry_var = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=entry_var)
combobox.pack()
combobox.bind('<<ComboboxSelected>>', on_select)

list_recommend = ['apple', 'banana', 'cherry', 'date', 'elderberry']
combobox['values'] = list_recommend

root.mainloop()