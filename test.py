import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class PatientForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Patient Information Form")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Patient Name").grid(row=0, column=0)
        self.patient_name = tk.Entry(self)
        self.patient_name.grid(row=0, column=1)

        tk.Label(self, text="Medical ID").grid(row=1, column=0)
        self.medical_id = tk.Entry(self)
        self.medical_id.grid(row=1, column=1)

        tk.Label(self, text="Patient ID").grid(row=2, column=0)
        self.patient_id = tk.Entry(self)
        self.patient_id.grid(row=2, column=1)

        tk.Label(self, text="Date of Birth").grid(row=3, column=0)
        self.date_of_birth = DateEntry(self)
        self.date_of_birth.grid(row=3, column=1)

        tk.Label(self, text="Weight").grid(row=4, column=0)
        self.weight = tk.Entry(self)
        self.weight.grid(row=4, column=1)

        tk.Label(self, text="Sex").grid(row=5, column=0)

        # Create radio buttons for sex field
        self.sex_var = tk.StringVar(value="Male")

        male_radio_button = ttk.Radiobutton(
            self,
            text="Male",
            variable=self.sex_var,
            value="Male"
        )

        female_radio_button = ttk.Radiobutton(
            self,
            text="Female",
            variable=self.sex_var,
            value="Female"
        )

        male_radio_button.grid(row=5, column=1)
        female_radio_button.grid(row=5, column=2)

        tk.Label(self, text="Insurance ID").grid(row=6, column=0)
        self.insurance_id = tk.Entry(self)
        self.insurance_id.grid(row=6, column=1)

        tk.Label(self, text="Guardian Information").grid(row=7, column=0)
        self.guardian_info = tk.Entry(self)
        self.guardian_info.grid(row=7, column=1)

        tk.Label(self, text="Address").grid(row=8, column=0)
        self.address = tk.Entry(self)
        self.address.grid(row=8, column=1)

    def get_form_values(self):
        patient_name = self.patient_name.get()
        medical_id = self.medical_id.get()
        patient_id = self.patient_id.get()
        date_of_birth = str(self.date_of_birth.get_date())
        weight = self.weight.get()

        sex = str(self.sex_var.get())

        insurance_id = self.insurance_id.get()
        guardian_info = self.guardian_info.get()
        address = self.address.get()


root = tk.Tk()
app = PatientForm(master=root)
app.mainloop()

# Get form values
# patient_name = app.get_form_values()[0]
# medical_id = app.get_form_values()[1]
# patient_id = app.get_form_values()[2]
# date_of_birth = app.get_form_values()[3]
# weight = app.get_form_values()[4]
# sex = app.get_form_values()[5]
# insurance_id = app.get_form_values()[6]
# guardian_info = app.get_form_values()[7]
# address = app.get_form_values()[8]
