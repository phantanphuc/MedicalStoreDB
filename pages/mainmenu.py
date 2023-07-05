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

        # label1 = tk.Label(self, text="Prescription")
        # label1.pack(side="top")

        # Second row
        # second_section = tk.Frame(self, bg="white", height=300)
        # second_section.pack(side="top", fill="both", expand=True)



        # add_prescription_button.pack(side="left")

        frame = tk.Frame(self)
        frame.pack()


        row1 = tk.Frame(frame)
        row1.pack(side="top", pady=10)

        label1 = tk.Label(row1, text="Thêm đơn thuốc", font=("Times New Roman Bold Italic", 20), width=20)
        label1.pack(side="right")

        add_prescription_img = loadImage("resources/AddPres.png")
        add_prescription_button = tk.Button(row1, image=add_prescription_img, command=self.gotoAddPrescription,
                                            height=128)
        add_prescription_button.image = add_prescription_img
        add_prescription_button.pack(side="left", padx=20)

        row2 = tk.Frame(frame)
        row2.pack(side="top", pady=10)

        label2 = tk.Label(row2, text="Xem đơn thuốc", font=("Times New Roman Bold Italic", 20), width=20)
        label2.pack(side="right")

        view_prescription_img = loadImage("resources/viewPres.png")
        view_prescription_button = tk.Button(row2, image=view_prescription_img, command=self.gotoViewPrescription,
                                             height=128)
        view_prescription_button.image = view_prescription_img
        view_prescription_button.pack(side="left", padx=20)

        row3 = tk.Frame(frame)
        row3.pack(side="top", pady=10)

        label3 = tk.Label(row3, text="Báo cáo", font=("Times New Roman Bold Italic", 20), width=20)
        label3.pack(side="right")

        report_prescription_img = loadImage("resources/report.png")
        report_prescription_button = tk.Button(row3, image=report_prescription_img, command=self.gotoReport, height=128)
        report_prescription_button.image = report_prescription_img
        report_prescription_button.pack(side="left", padx=20)

        row4 = tk.Frame(frame)
        row4.pack(side="top", pady=10)

        label4 = tk.Label(row4, text="Log out", font=("Times New Roman Bold Italic", 20), width=20)
        label4.pack(side="right")

        logout__img = loadImage("resources/backbutton.png")
        logout_button = tk.Button(row4, image=logout__img, command=self.back, height=128)
        logout_button.image = logout__img
        logout_button.pack(side="left", padx=20)

    def gotoAddPrescription(self):
        AppManager.getAppManager().getFrame("AddPrescriptionForm").resetAll()
        AppManager.getAppManager().getFrame("AddPrescriptionForm").tkraise()

    def gotoViewPrescription(self):
        AppManager.getAppManager().getFrame("ViewPrescriptionForm").resetAll()
        AppManager.getAppManager().getFrame("ViewPrescriptionForm").updatePrescriptionListbox()
        AppManager.getAppManager().getFrame("ViewPrescriptionForm").tkraise()

    def gotoReport(self):
        AppManager.getAppManager().getFrame("ReportMenu").tkraise()

    def back(self):
        AppManager.getAppManager().getFrame("LoginPage").tkraise()
