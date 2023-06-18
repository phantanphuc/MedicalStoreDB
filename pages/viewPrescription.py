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

    def addViewPrescriptionWidget(self):
        prescription_listbox = tk.Listbox(self.button_frame, width=50)
        prescription_listbox.grid(row=1, column=0, columnspan=3)
        prescription_list = ['pres_1', 'pres_2', 'pres_3']

        for item in prescription_list:
            prescription_listbox.insert(tk.END, item)

        prescription_listbox.bind('<<ListboxSelect>>', self.on_prescription_select)


