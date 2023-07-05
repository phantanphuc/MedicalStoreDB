import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

frame = tk.Frame(root)
frame.pack()

row1 = tk.Frame(frame, height=50)
row1.pack(side="top", pady=10)

label1 = tk.Label(row1, text="Label 1", font=("Arial Bold", 14))
label1.pack(side="right")

button1 = tk.Button(row1, text="Button 1")
button1.pack(side="left")

row2 = tk.Frame(frame, height=50)
row2.pack(side="top", pady=10)

label2 = tk.Label(row2, text="Label 2", font=("Times New Roman", 12))
label2.pack(side="right")

button2 = tk.Button(row2, text="Button 2")
button2.pack(side="left")

row3 = tk.Frame(frame, height=50)
row3.pack(side="top", pady=10)

label3 = tk.Label(row3, text="Label 3", font=("Verdana", 10))
label3.pack(side="right")

button3 = tk.Button(row3, text="Button 3")
button3.pack(side="left")

# for row in [row1, row2, row3]:
#     row.pack_propagate(0)

root.mainloop()
