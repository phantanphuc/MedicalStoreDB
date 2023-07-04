from tkcalendar import DateEntry

from common import loadImage

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from datetime import datetime, timedelta
import AppManager
from DataManager import getDataManager


class ReportMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=300, height=200)
        self.controller = controller

        self.font_size = 20

        self.frame1 = tk.Frame(self)
        self.frame1.pack(side="top")

        # Create the second frame
        self.frame2 = tk.Frame(self)
        self.frame2.pack(side="top")

        # Create the widgets for the first frame
        self.from_time_label = tk.Label(self.frame1, text="Ngày bắt đầu", font=("Times New Roman", self.font_size))
        self.from_time_label.grid(row=0, column=0, sticky="w")
        self.from_time_entry = DateEntry(self.frame1, width=20, font=("Times New Roman", self.font_size), date_pattern='d/m/yyyy')
        self.from_time_entry.grid(row=0, column=1)
        one_year_ago = datetime.now() - timedelta(days=365)
        self.from_time_entry.set_date(one_year_ago)
        self.to_time_label = tk.Label(self.frame1, text="Ngày kết thúc", font=("Times New Roman", self.font_size))
        self.to_time_label.grid(row=1, column=0, sticky="w")
        self.to_time_entry = DateEntry(self.frame1, width=20, font=("Times New Roman", self.font_size), date_pattern='d/m/yyyy')
        self.to_time_entry.grid(row=1, column=1)
        self.search_label = tk.Label(self.frame1, text="Bộ lọc", font=("Times New Roman", self.font_size))
        self.search_label.grid(row=2, column=0, sticky="w")
        self.search_entry = tk.Entry(self.frame1, font=("Times New Roman", self.font_size))
        self.search_entry.grid(row=2, column=1)

        # Create the widgets for the second frame
        # self.back_button = tk.Button(self.frame2, text="Back")
        # self.back_button.pack(side="left")
        # self.export_button = tk.Button(self.frame2, text="Export")
        # self.export_button.pack(side="left")

        report_prescription_img = loadImage("resources/report.png")
        report_prescription_button = tk.Button(self.frame2, image=report_prescription_img, command=self.exportData)
        report_prescription_button.image = report_prescription_img
        report_prescription_button.pack(side="left")

        back_img = loadImage("resources/backbutton.png")
        back_button = tk.Button(self.frame2, image=back_img, command=self.back)
        back_button.image = back_img
        back_button.pack(side="right")

    def back(self):
        AppManager.getAppManager().getFrame("MainmenuPage").tkraise()

    def exportData(self):
        from_date = self.from_time_entry.get()
        to_date = self.to_time_entry.get()

        getDataManager().createReport(from_date, to_date)








