import tkinter as tk
from tkinter import ttk

def on_keyrelease(event):
    value = event.widget.get()
    value = value.strip().lower()
    if value == '':
        data = list_recommend
    else:
        data = []
        for item in list_recommend:
            if value in item.lower():
                data.append(item)
    combobox_update(data)

def combobox_update(data):
    combobox['values'] = sorted(data, key=str.lower)
    combobox.event_generate('<<ComboboxSelected>>')

root = tk.Tk()
entry_var = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=entry_var)
combobox.pack()
combobox.bind('<KeyRelease>', on_keyrelease)

list_recommend = ['apple', 'banana', 'cherry', 'date', 'elderberry']
combobox_update(list_recommend)

root.mainloop()
