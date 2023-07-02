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
        self.current_prescription_ID = ''
        self.current_patient_ID = ''
        self.current_index = -1
        self.last_color = None

    def on_prescription_select(self, event):
        # get selected item index
        if len(event.widget.curselection()) == 0:
            return
        index = event.widget.curselection()[0]

        if index == self.current_index:
            return

        # get selected item
        # selected_item = event.widget.get(index)
        selected_data = self.prescription_list[index]
        self.setPrescriptionData(selected_data)
        self.current_prescription_ID = selected_data['prescription_ID']
        self.current_patient_ID = selected_data['patient']

        if self.current_index != -1:
            self.prescription_listbox.itemconfig(self.current_index, bg=self.last_color)

        self.last_color = self.prescription_listbox.itemconfig(index, 'bg')[4]
        self.prescription_listbox.itemconfig(index, bg='yellow')
        self.current_index = index



    def updatePrescriptionListbox(self, keyword=''):
        self.prescription_listbox.delete(0,tk.END)

        self.prescription_list = getDataManager()\
            .setPatientInfoToPrescription(getDataManager().getAllPrescription())

        def filterPrescription(keywordparam, data):
            keywordparam = keywordparam.lower()
            return keywordparam in data['ho_ten_benh_nhan'].lower()

        self.prescription_list = \
            [x for x in self.prescription_list if filterPrescription(keyword, x)]

        self.prescription_display_list = [x['ho_ten_benh_nhan'] for x in self.prescription_list]

        # for i in range(20):
        for item, pres_item in zip(self.prescription_display_list, self.prescription_list):
            self.prescription_listbox.insert(tk.END, item)
            if 'synced' in pres_item and pres_item['synced']:
            # if 'a' in item:
                self.prescription_listbox.itemconfig(tk.END, bg=from_rgb((196, 255, 196)))
            else:
                self.prescription_listbox.itemconfig(tk.END, bg=from_rgb((255, 196, 196)))

        # self.prescription_listbox.itemconfig(1, bg='yellow')

        self.prescription_listbox.bind('<<ListboxSelect>>', self.on_prescription_select)

    def searchPrescription(self):
        self.resetColor()
        keyword = self.pres_search_entry.get()
        self.updatePrescriptionListbox(keyword)


    def addViewPrescriptionWidget(self):

        self.list_prescription_frame = tk.LabelFrame(self)
        self.list_prescription_frame.grid(row=2, column=0, padx=10, pady=10)

        self.pres_search_entry = tk.Entry(self.list_prescription_frame, width=50)
        self.pres_search_entry.grid(row=0, column=0, columnspan=2)

        self.search_button = tk.Button(self.list_prescription_frame, text="Search", command=self.searchPrescription)
        self.search_button.grid(row=0, column=2)


        self.search_pres_scrollbar = tk.Scrollbar(self.list_prescription_frame)
        self.search_pres_scrollbar.grid(row=1, column=3, sticky=tk.N+tk.S)

        self.prescription_listbox = tk.Listbox(self.list_prescription_frame, width=45,
                                               yscrollcommand=self.search_pres_scrollbar.set,
                                               font=('Helvetica', 12, 'bold'))
        self.prescription_listbox.grid(row=1, column=0, columnspan=3)

        self.updatePrescriptionListbox()


    def setPrescriptionData(self, display_data):
        # print(display_data)
        self.resetAll()
        self.setPatientInfo(display_data)
        self.resetDianoseAndMedicineList()

        for i in range(len(display_data['chan_doan']) - 1):
            self.add_row_diagnose()

        for i in range(len(display_data['chan_doan'])):
            disease_name = getDataManager().getDiseaseFromID(display_data['chan_doan'][i][0])
            self.list_diagnose[i][1].delete(0, tk.END)
            self.list_diagnose[i][1].insert(0, disease_name[1])

            self.list_diagnose[i][0].delete(0, tk.END)
            self.list_diagnose[i][0].insert(0, display_data['chan_doan'][i][0])

            self.list_diagnose[i][2].delete(0, tk.END)
            self.list_diagnose[i][2].insert(0, display_data['chan_doan'][i][1])

        for i in range(len(display_data['don_thuoc']) - 1):
            self.add_row_medicine()

        for i in range(len(display_data['don_thuoc'])):
            self.setMedicineInfo(i, getDataManager().getMedicineByID(display_data['don_thuoc'][i][0])[0])
            self.list_medicine[i][4].delete(0, tk.END)
            self.list_medicine[i][4].insert(0, display_data['don_thuoc'][i][1])

        self.luu_y_entry.insert(0, display_data['luu_y'])
        self.hinh_thuc_dieu_tri_entry.insert(0, display_data['hinh_thuc_dieu_tri'])
        self.dot_dung_thuoc_entry.insert(0, display_data['dot_dung_thuoc'])
        self.loi_dan_entry.insert(0, display_data['loi_dan'])

        if 'sdt_nguoi_kham' in display_data:
            self.so_dien_thoai_nguoi_kham_benh_entry.insert(0, display_data['sdt_nguoi_kham'])

        self.ngay_tai_kham_entry.insert(0, display_data['ngay_tai_kham'])
        self.ngay_gio_ke_don_entry.insert(0, display_data['ngay_gio_ke_don'])
        self.chu_ky_so_entry.insert(0, display_data['chu_ky_so'])

        # self.ngay_tai_kham_entry.insert(0, "12/06/2024")
        # self.ngay_gio_ke_don_entry.insert(0, "12/06/2023")
        # self.chu_ky_so_entry.insert(0, "XYR")

    def savePrescription(self):

        if not self.checkValidPrescription():
            return

        data = self.getPrescriptionInfo()
        data['prescription_ID'] = self.current_prescription_ID
        data['patient'] = self.current_patient_ID

        getDataManager().updatePrescription(data)

        self.resetColor()


    def syncPrescription(self):
        if self.current_prescription_ID == '':
            return
        data = self.getPrescriptionInfo()
        data['prescription_ID'] = self.current_prescription_ID
        data['patient'] = self.current_patient_ID
        #TODO SYNC!
        getDataManager().updatePrescription(data)
        getDataManager().syncPrescription(data)

        self.resetColor()

        self.updatePrescriptionListbox()
        self.searchPrescription()



    def resetColor(self):
        if self.current_index == -1:
            return
        self.prescription_listbox.itemconfig(self.current_index, bg=self.last_color)
        self.current_index = -1
