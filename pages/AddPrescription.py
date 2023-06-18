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

class AddPrescriptionForm(PrescriptionBaseClass.PrescriptionBaseClass):
    def __init__(self, parent=None, controller=None):
        # tk.Frame.__init__(self, parent)
        super().__init__(parent, controller)

