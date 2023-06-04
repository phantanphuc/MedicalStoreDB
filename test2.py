import tkinter as tk
from PIL import ImageTk, Image

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Medical App")
        self.master.geometry("500x500")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add doctor button
        add_doctor_img = Image.open("resources/test.png")
        add_doctor_img = add_doctor_img.resize((100, 100), Image.ANTIALIAS)
        add_doctor_img = ImageTk.PhotoImage(add_doctor_img)
        add_doctor_button = tk.Button(self, image=add_doctor_img)
        add_doctor_button.image = add_doctor_img
        add_doctor_button.pack()

        # View prescription button
        view_prescription_img = Image.open("resources/test.png")
        view_prescription_img = view_prescription_img.resize((100, 100), Image.ANTIALIAS)
        view_prescription_img = ImageTk.PhotoImage(view_prescription_img)
        view_prescription_button = tk.Button(self, image=view_prescription_img)
        view_prescription_button.image = view_prescription_img
        view_prescription_button.pack()

root = tk.Tk()
app = MainMenu(master=root)
app.mainloop()