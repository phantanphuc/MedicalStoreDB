import tkinter as tk

def add_row(event=None):
    # Create new row
    row = len(medicine_list) + 1

    # Add name field
    name_label = tk.Label(form, text=f"Medicine {row} Name:")
    name_label.grid(row=row, column=0)
    name_entry = tk.Entry(form)
    name_entry.grid(row=row, column=1)

    # Add price field
    price_label = tk.Label(form, text=f"Medicine {row} Price:")
    price_label.grid(row=row, column=2)
    price_entry = tk.Entry(form)
    price_entry.grid(row=row, column=3)

    # Add type field
    type_label = tk.Label(form, text=f"Medicine {row} Type:")
    type_label.grid(row=row, column=4)
    type_entry = tk.Entry(form)
    type_entry.grid(row=row, column=5)

    # Add new medicine to list
    medicine_list.append((name_label, name_entry, price_label, price_entry, type_label, type_entry))

    # Set focus to first field of new row
    name_entry.focus()

def remove_row():
    # Remove last row
    if len(medicine_list) > 1:
        name_label, name_entry, price_label, price_entry, type_label, type_entry = medicine_list.pop()
        name_label.destroy()
        name_entry.destroy()
        price_label.destroy()
        price_entry.destroy()
        type_label.destroy()
        type_entry.destroy()

        # Set focus to last field of previous row
        last_row = len(medicine_list)
        if last_row > 0:
            medicine_list[last_row - 1][4].focus()

# Create main window
root = tk.Tk()
root.title("Medicine List")

# Create form
form = tk.Frame(root)
form.pack()

# Create initial row of fields
name_label = tk.Label(form, text="Medicine 1 Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(form)
name_entry.grid(row=1, column=1)

price_label = tk.Label(form, text="Medicine 1 Price:")
price_label.grid(row=1, column=2)
price_entry = tk.Entry(form)
price_entry.grid(row=1, column=3)

type_label = tk.Label(form, text="Medicine 1 Type:")
type_label.grid(row=1, column=4)
type_entry = tk.Entry(form)
type_entry.grid(row=1, column=5)

medicine_list = [(name_label, name_entry, price_label, price_entry, type_label, type_entry)]

# Bind tab key to add_row function when user is focused on the last field of the last row
type_entry.bind("<Tab>", add_row)

# Create button to remove last row
remove_button = tk.Button(root, text="Remove Medicine", command=remove_row)
remove_button.pack()

root.mainloop()
