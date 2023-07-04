try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from PIL import ImageTk, Image
import AppManager
from common import *

class MainmenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=300, height=200)
        self.controller = controller

        # self.bg = tk.PhotoImage(file="resources/test.png")
        # self.bg_label = tk.Label(self, image=self.bg)
        # self.bg_label.place(x=0, y=0)


        # self.root = tk.Tk()
        # self.geometry("300x200")

        label1 = tk.Label(self, text="Prescription")
        label1.pack(side="top")

        # Second row
        second_section = tk.Frame(self, bg="white", height=300)
        second_section.pack(side="top", fill="both", expand=True)

        add_prescription_img = loadImage("resources/AddPres.png")
        add_prescription_button = tk.Button(second_section, image=add_prescription_img, command=self.gotoAddPrescription)
        add_prescription_button.image = add_prescription_img
        add_prescription_button.pack(side="left")

        view_prescription_img = loadImage("resources/viewPres.png")
        view_prescription_button = tk.Button(second_section, image=view_prescription_img, command=self.gotoViewPrescription)
        view_prescription_button.image = view_prescription_img
        view_prescription_button.pack(side="left")

        # sync_prescription_img = loadImage("resources/syncPres.png")
        # sync_prescription_button = tk.Button(second_section, image=sync_prescription_img)
        # sync_prescription_button.image = sync_prescription_img
        # sync_prescription_button.pack(side="left")

        report_prescription_img = loadImage("resources/report.png")
        report_prescription_button = tk.Button(second_section, image=report_prescription_img, command=self.gotoReport)
        report_prescription_button.image = report_prescription_img
        report_prescription_button.pack(side="left")

        # Third row
        # label2 = tk.Label(self, text="Patients")
        # label2.pack(side="top")
        #
        # # Fourth row
        # fourth_section = tk.Frame(self, bg="white", height=300)
        # fourth_section.pack(side="top", fill="both", expand=True)
        #
        # view_patient_img = loadImage("resources/ViewPatient.png")
        # view_patient_button = tk.Button(fourth_section, image=view_patient_img)
        # view_patient_button.image = view_patient_img
        # view_patient_button.pack(side="left")
        #
        # # Fifth row
        # # fifth_section = tk.Frame(self, bg="white", height=300)
        # # fifth_section.pack(side="top", fill="both", expand=True)
        #
        # label3 = tk.Label(self, text="Doctor")
        # label3.pack(side="top")
        #
        # # Sixth row
        #
        # sixth_section = tk.Frame(self, bg="white", height=300)
        # sixth_section.pack(side="top", fill="both", expand=True)
        #
        # add_doctor_img = loadImage("resources/AddDoctor.png")
        # add_doctor_button = tk.Button(sixth_section, image=add_doctor_img)
        # add_doctor_button.image = add_doctor_img
        # add_doctor_button.pack(side="left")
        #
        # view_doctor_img = loadImage("resources/viewDoctor.png")
        # view_doctor_button = tk.Button(sixth_section, image=view_doctor_img)
        # view_doctor_button.image = view_doctor_img
        # view_doctor_button.pack(side="left")
        #
        # sync_doctor_img = loadImage("resources/syncDoctor.png")
        # sync_doctor_button = tk.Button(sixth_section, image=sync_doctor_img)
        # sync_doctor_button.image = sync_doctor_img
        # sync_doctor_button.pack(side="left")

    def gotoAddPrescription(self):
        AppManager.getAppManager().getFrame("AddPrescriptionForm").resetAll()
        AppManager.getAppManager().getFrame("AddPrescriptionForm").tkraise()

    def gotoViewPrescription(self):
        AppManager.getAppManager().getFrame("ViewPrescriptionForm").resetAll()
        AppManager.getAppManager().getFrame("ViewPrescriptionForm").updatePrescriptionListbox()
        AppManager.getAppManager().getFrame("ViewPrescriptionForm").tkraise()

    def gotoReport(self):
        AppManager.getAppManager().getFrame("ReportMenu").tkraise()
