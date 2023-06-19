try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image

from DataManager import getDataManager
from common import *

import pages.PrescriptionBaseClass as PrescriptionBaseClass

class ViewPrescriptionForm(PrescriptionBaseClass.PrescriptionBaseClass):
    def __init__(self, parent=None, controller=None):
        # tk.Frame.__init__(self, parent)
        super().__init__(parent, controller)
        self.addViewPrescriptionWidget()

    def on_prescription_select(self, event):
        # get selected item index
        index = event.widget.curselection()[0]
        # get selected item
        selected_item = event.widget.get(index)
        print(selected_item)
        print(index)

    def addViewPrescriptionWidget(self):

        self.list_prescription_frame = tk.LabelFrame(self)
        self.list_prescription_frame.grid(row=2, column=0, padx=10, pady=10)

        self.pres_search_entry = tk.Entry(self.list_prescription_frame, width=50)
        self.pres_search_entry.grid(row=0, column=0, columnspan=2)

        self.search_button = tk.Button(self.list_prescription_frame, text="Search")
        self.search_button.grid(row=0, column=2)


        scrollbar = tk.Scrollbar(self.list_prescription_frame)
        scrollbar.grid(row=1, column=3, sticky=tk.N+tk.S)

        prescription_listbox = tk.Listbox(self.list_prescription_frame, width=60, yscrollcommand=scrollbar.set)
        prescription_listbox.grid(row=1, column=0, columnspan=3)

        self.prescription_list = getDataManager().setPatientInfoToPrescription(getDataManager().getAllPrescription())
        self.prescription_display_list = [x['ho_ten_benh_nhan'] for x in self.prescription_list]

        # for i in range(20):
        for item in self.prescription_display_list:
            prescription_listbox.insert(tk.END, item)

        prescription_listbox.bind('<<ListboxSelect>>', self.on_prescription_select)


