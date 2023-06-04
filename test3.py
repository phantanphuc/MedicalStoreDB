import tkinter as tk

class PrescriptionFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Prescription Frame")
        self.master.geometry("500x500")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # First row
        label1 = tk.Label(self, text="Prescription")
        label1.pack(side="top")

        # Second row
        second_section = tk.Frame(self, bg="white", height=300)
        second_section.pack(side="top", fill="both", expand=True)

        button1 = tk.Button(second_section, text="Button 1")
        button1.pack(side="left")

        button2 = tk.Button(second_section, text="Button 2")
        button2.pack(side="left")

        button3 = tk.Button(second_section, text="Button 3")
        button3.pack(side="left")

        # Third row
        label2 = tk.Label(self, text="Patients")
        label2.pack(side="top")

        # Fourth row
        fourth_section = tk.Frame(self, bg="white", height=300)
        fourth_section.pack(side="top", fill="both", expand=True)

        button4 = tk.Button(fourth_section, text="Button 4")
        button4.pack(side="left")

        button5 = tk.Button(fourth_section, text="Button 5")
        button5.pack(side="left")

root = tk.Tk()
app = PrescriptionFrame(master=root)
app.mainloop()