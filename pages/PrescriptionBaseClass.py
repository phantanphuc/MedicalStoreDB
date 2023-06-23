try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image

from DataManager import getDataManager
from common import *
import AppManager

class PrescriptionBaseClass(tk.Frame):
    def __init__(self, parent=None, controller=None):
        tk.Frame.__init__(self, parent)
        self.mouse_on_canvas = False
        self.entry_width = 140
        self.current_row = 0
        self.current_diagnose_count = 0
        self.current_medicine_count = 0
        self.controller = controller

        self.last_diagnose = None
        self.list_diagnose = []

        self.last_medicine = None
        self.list_medicine = []

        self.list_recommend_patient = []
        self.list_recommend_medicine = []

        self.create_widgets()

    def dianoseIDClickOut(self, event):
        input_id = event.widget.get()
        if input_id != '':
            disease_name = getDataManager().getDiseaseFromID(input_id.lower())
            self.list_diagnose[event.widget.row_index][1].delete(0, tk.END)
            self.list_diagnose[event.widget.row_index][1].insert(0, disease_name[1])

    def on_dianose_search(self, event=None):
        value = event.widget.get()
        value = value.strip().lower()

        self.list_searched_disease = getDataManager().searchDiseaseFromName(value)

        data = self.list_searched_disease[:20]

        queried_data = [x[0] + " " + x[1] for x in data]

        self.list_diagnose[event.widget.row_index][1]['values'] = sorted(queried_data, key=str.lower)

    def on_selectDianose(self, event):
        disease_code = event.widget.get().split(" ")[0]
        self.list_diagnose[event.widget.row_index][0].delete(0, tk.END)
        self.list_diagnose[event.widget.row_index][0].insert(0, disease_code)


    def add_row_diagnose(self, event=None):
        row_thres = 1

        for widget in self.prescription_info_frame.grid_slaves():
            if widget.grid_info()['row'] >= row_thres + self.current_diagnose_count:
                widget.grid(row=widget.grid_info()['row'] + 1, column=widget.grid_info()['column'])

        ma_chan_doan_entry = tk.Entry(self.prescription_info_frame)
        ma_chan_doan_entry.grid(row=row_thres + self.current_diagnose_count, column=1)
        ma_chan_doan_entry.bind("<FocusOut>", self.dianoseIDClickOut)
        ma_chan_doan_entry.row_index = self.current_diagnose_count

        # Add price field
        # ten_chan_doan_entry = tk.Entry(self.prescription_info_frame)
        # ten_chan_doan_entry.grid(row=row_thres + self.current_diagnose_count, column=2, rowspan=3)

        ten_chan_doan_entry = ttk.Combobox(self.prescription_info_frame, width=50)
        ten_chan_doan_entry.grid(row=row_thres + self.current_diagnose_count, column=2, columnspan=3)
        ten_chan_doan_entry.bind("<Button-1>", self.on_dianose_search)
        ten_chan_doan_entry.bind("<Tab>", self.on_dianose_search)
        ten_chan_doan_entry.bind("<Down>", self.on_dianose_search)
        # ten_thuoc_entry.bind('<KeyRelease>', self.on_keyreleaseMedicineName)
        ten_chan_doan_entry.row_index = self.current_diagnose_count
        ten_chan_doan_entry.bind('<<ComboboxSelected>>', self.on_selectDianose)


        # Add type field
        ket_luan_entry = tk.Entry(self.prescription_info_frame, width=50)
        ket_luan_entry.grid(row=row_thres + self.current_diagnose_count, column=5, columnspan=2)

        self.current_diagnose_count = self.current_diagnose_count + 1

        self.list_diagnose.append((ma_chan_doan_entry, ten_chan_doan_entry, ket_luan_entry))

        if self.last_diagnose != None:
            self.last_diagnose.unbind("<Tab>")

        ket_luan_entry.bind("<Tab>", self.add_row_diagnose)
        self.last_diagnose = ket_luan_entry
        ma_chan_doan_entry.focus()

        self.updateCanvasHeight()

    def remove_row_diagnose(self, event=None):
        if self.current_diagnose_count <= 1:
            [x.delete(0, tk.END) for x in self.list_diagnose[-1]]
            return
        row_thres = 1

        last_row = self.list_diagnose[-1]
        self.list_diagnose = self.list_diagnose[:-1]

        last_row[0].destroy()
        last_row[1].destroy()
        last_row[2].destroy()

        self.current_diagnose_count = self.current_diagnose_count - 1

        for widget in self.prescription_info_frame.grid_slaves():
            if widget.grid_info()['row'] >= row_thres + self.current_diagnose_count:
                widget.grid(row=widget.grid_info()['row'] - 1, column=widget.grid_info()['column'])

        self.last_diagnose = self.list_diagnose[-1][2]
        self.list_diagnose[-1][2].bind("<Tab>", self.add_row_diagnose)

        self.updateCanvasHeight()

    def on_keyreleasePatientName(self, event):

        value = event.widget.get()
        value = value.strip().lower()

        self.list_recommend_patient = getDataManager().searchPatient(value)
        data = self.list_recommend_patient[:20]

        queried_data = [x["ho_ten_benh_nhan"] + " (" + x["ma_dinh_danh_cong_dan"] + ")" for x in data]

        self.comboboxPatient['values'] = sorted(queried_data, key=str.lower)
        # self.comboboxPatient.event_generate('<<ComboboxSelected>>')

    def DEBUGSetDummyValue(self):
        print("DEBUG")
        selected_value = getDataManager().searchPatient("Sarah")
        self.setPatientInfo(selected_value[0])
        self.add_row_medicine()
        self.setMedicineInfo(0, getDataManager().getMedicine('D new Medicine')[0])
        self.setMedicineInfo(1, getDataManager().getMedicine('A new Medicine')[0])
        self.list_diagnose[0][0].insert(0, "F45.4")
        # self.list_diagnose[0][1].insert(0, "Đau Bụng")
        self.list_diagnose[0][2].insert(0, "CHECK")
        input_id = self.list_diagnose[0][0].get()
        if input_id != '':
            disease_name = getDataManager().getDiseaseFromID(input_id.lower())
            self.list_diagnose[0][1].delete(0, tk.END)
            self.list_diagnose[0][1].insert(0, disease_name[1])

        self.list_medicine[0][3].insert(0, "10")
        self.list_medicine[1][3].insert(0, "15")

        self.luu_y_entry.insert(0, "nhớ uống thuốc")
        self.hinh_thuc_dieu_tri_entry.insert(0, "uống thuốc")
        self.dot_dung_thuoc_entry.insert(0, "4")
        self.loi_dan_entry.insert(0, "nhớ uống thuốc 2")
        self.so_dien_thoai_nguoi_kham_benh_entry.insert(0, "0912121212")
        self.ngay_tai_kham_entry.insert(0, "12/06/2024")
        self.ngay_gio_ke_don_entry.insert(0, "12/06/2023")
        self.chu_ky_so_entry.insert(0, "XYR")

    def on_selectPatient(self, event):
        to_query = " ".join(self.comboboxPatient.get().split(" ")[:-1])

        selected_value = [x for x in self.list_recommend_patient if x['ho_ten_benh_nhan'] == to_query]

        if len(selected_value) > 0:
            # print("Selected value:", selected_value[0])
            self.setPatientInfo(selected_value[0])

        # combobox_update(data[:20])

    def setPatientInfo(self, data):
        self.comboboxPatient.delete(0, tk.END)
        self.medical_id.delete(0, tk.END)
        self.patient_id.delete(0, tk.END)
        self.date_of_birth.delete(0, tk.END)
        self.weight.delete(0, tk.END)
        self.insurance_id.delete(0, tk.END)
        self.guardian_info.delete(0, tk.END)
        self.address.delete(0, tk.END)

        self.comboboxPatient.set(data['ho_ten_benh_nhan'])
        self.medical_id.insert(0, data['ma_dinh_danh_y_te'])
        self.patient_id.insert(0, data['ma_dinh_danh_cong_dan'])
        self.date_of_birth.insert(0, data['ngay_sinh_benh_nhan'])
        self.weight.insert(0, data['can_nang'])
        self.sex_var.set(data['gioi_tinh'])
        self.insurance_id.insert(0, data['ma_so_the_bao_hiem_y_te'])
        self.guardian_info.insert(0, data['thong_tin_nguoi_giam_ho'])
        self.address.insert(0, data['dia_chi'])

    def back(self):
        AppManager.getAppManager().getFrame("MainmenuPage").tkraise()

    def create_widgets(self):
        # Create a frame for patient information
        patient_info_frame = tk.LabelFrame(self, text="Patient Information")
        patient_info_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(patient_info_frame, text="Tên bệnh nhân").grid(row=0, column=0)
        # self.patient_name = tk.Entry(patient_info_frame)
        # self.patient_name.grid(row=0, column=1)

        entry_var = tk.StringVar()
        self.comboboxPatient = ttk.Combobox(patient_info_frame, textvariable=entry_var)
        self.comboboxPatient.grid(row=0, column=1)
        self.comboboxPatient.bind('<KeyRelease>', self.on_keyreleasePatientName)
        self.comboboxPatient.bind('<<ComboboxSelected>>', self.on_selectPatient)

        tk.Label(patient_info_frame, text="Định danh y tế").grid(row=1, column=0)
        self.medical_id = tk.Entry(patient_info_frame)
        self.medical_id.grid(row=1, column=1)

        tk.Label(patient_info_frame, text="Định danh công dân").grid(row=2, column=0)
        self.patient_id = tk.Entry(patient_info_frame)
        self.patient_id.grid(row=2, column=1)

        tk.Label(patient_info_frame, text="Ngày sinh").grid(row=3, column=0)
        self.date_of_birth = DateEntry(patient_info_frame, date_pattern='d/m/yyyy')
        self.date_of_birth.grid(row=3, column=1)

        tk.Label(patient_info_frame, text="Cân nặng").grid(row=4, column=0)
        self.weight = tk.Entry(patient_info_frame)
        self.weight.grid(row=4, column=1)

        tk.Label(patient_info_frame, text="Giới tính").grid(row=5, column=0)

        # Create radio buttons for sex field
        self.sex_var = tk.StringVar(value="Nam")

        male_radio_button = ttk.Radiobutton(
            patient_info_frame,
            text="Nam",
            variable=self.sex_var,
            value="Nam"
        )

        female_radio_button = ttk.Radiobutton(
            patient_info_frame,
            text="Nữ",
            variable=self.sex_var,
            value="Nữ"
        )

        male_radio_button.grid(row=5, column=1)
        female_radio_button.grid(row=5, column=2)

        tk.Label(patient_info_frame, text="Số bảo hiểm").grid(row=6, column=0)
        self.insurance_id = tk.Entry(patient_info_frame)
        self.insurance_id.grid(row=6, column=1)

        tk.Label(patient_info_frame, text="Thông tin người giám hộ").grid(row=7, column=0)
        self.guardian_info = tk.Entry(patient_info_frame)
        self.guardian_info.grid(row=7, column=1)

        tk.Label(patient_info_frame, text="Địa chỉ").grid(row=8, column=0)
        self.address = tk.Entry(patient_info_frame)
        self.address.grid(row=8, column=1)

        self.button_frame = tk.LabelFrame(self)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10)

        savesync_img = loadImage("resources/savesync.png", 96)
        savesync_button = tk.Button(self.button_frame, image=savesync_img)
        savesync_button.image = savesync_img
        savesync_button.grid(row=0, column=0)

        saveonly_img = loadImage("resources/save.png", 96)
        saveonly_button = tk.Button(self.button_frame, image=saveonly_img, command=self.savePrescription)
        saveonly_button.image = saveonly_img
        saveonly_button.grid(row=0, column=1)

        debug_img = loadImage("resources/test.png", 96)
        debug_button = tk.Button(self.button_frame, image=debug_img, command=self.DEBUGSetDummyValue)
        debug_button.image = debug_img
        debug_button.grid(row=0, column=3)

        back_img = loadImage("resources/backbutton.png", 96)
        back_button = tk.Button(self.button_frame, image=back_img, command=self.back)
        back_button.image = back_img
        back_button.grid(row=0, column=4)

        # Create a frame for prescription information



        frame = tk.LabelFrame(self, text="LabelFrame", padx=5, pady=5)
        frame.grid(row=0, column=1, padx=10, pady=10, rowspan=3)

        self.canvas = tk.Canvas(frame)
        # canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        # scrollbar.grid(row=0, column=1, sticky="ns")
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.prescription_info_frame = tk.Frame(self.canvas)
        # self.bind("<Motion>", self.on_mouse_move_canvas)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.canvas.create_window((0, 0), window=self.prescription_info_frame, anchor="nw")

        self.prescription_info_frame.bind('<Enter>', self.on_enter_pres_frame)
        self.prescription_info_frame.bind('<Leave>', self.on_leave_pres_frame)

        # self.prescription_info_frame = tk.LabelFrame(self, text='Prescription Information')
        # self.prescription_info_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=3)

        tk.Label(self.prescription_info_frame, text='Chẩn đoán').grid(row=0, column=0, padx=5, pady=5)
        # chan_doan_entry = tk.Entry(self.prescription_info_frame, width=50)
        # chan_doan_entry.grid(row=0, column=1, padx=5, pady=5)

        ma_chan_doan = tk.Label(self.prescription_info_frame, text="Mã chẩn đoán")
        ma_chan_doan.grid(row=0, column=1)

        ten_chan_doan = tk.Label(self.prescription_info_frame, text="Tên chẩn đoán")
        ten_chan_doan.grid(row=0, column=2, columnspan=3)

        ket_luan = tk.Label(self.prescription_info_frame, text="Kết luận")
        ket_luan.grid(row=0, column=5, columnspan=2)

        add_button = tk.Button(self.prescription_info_frame, text="Thêm chẩn đoán", command=self.add_row_diagnose)
        add_button.grid(row=1, column=2)

        # Create button to remove last row
        remove_button = tk.Button(self.prescription_info_frame, text="Xóa chẩn đoán", command=self.remove_row_diagnose)
        remove_button.grid(row=1, column=3)

        self.current_row = 2

        tk.Label(self.prescription_info_frame, text='Lưu ý').grid(row=self.current_row, column=0, padx=5, pady=5)
        self.luu_y_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        self.luu_y_entry.grid(row=self.current_row, column=1, columnspan=7, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Hình thức điều trị').grid(row=self.current_row, column=0, padx=5,
                                                                               pady=5)
        self.hinh_thuc_dieu_tri_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        self.hinh_thuc_dieu_tri_entry.grid(row=self.current_row, column=1, columnspan=6, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Đợt dùng thuốc').grid(row=self.current_row, column=0, padx=5,
                                                                           pady=5)
        self.dot_dung_thuoc_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        self.dot_dung_thuoc_entry.grid(row=self.current_row, column=1, columnspan=6, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Thông tin đơn thuốc').grid(row=self.current_row, column=0, padx=5,
                                                                                pady=5)

        ma_thuoc = tk.Label(self.prescription_info_frame, text="Mã thuốc")
        ma_thuoc.grid(row=self.current_row, column=1)

        biet_duoc = tk.Label(self.prescription_info_frame, text="Biệt dược")
        biet_duoc.grid(row=self.current_row, column=2)

        ten_thuoc = tk.Label(self.prescription_info_frame, text="Tên thuốc")
        ten_thuoc.grid(row=self.current_row, column=3)

        don_vi_tinh = tk.Label(self.prescription_info_frame, text="Đơn vị tính")
        don_vi_tinh.grid(row=self.current_row, column=4)

        so_luong = tk.Label(self.prescription_info_frame, text="Số lượng")
        so_luong.grid(row=self.current_row, column=5)

        cach_dung = tk.Label(self.prescription_info_frame, text="Cách dùng")
        cach_dung.grid(row=self.current_row, column=6)

        self.current_row = self.current_row + 1

        add_button = tk.Button(self.prescription_info_frame, text="Thêm thuốc", command=self.add_row_medicine)
        add_button.grid(row=self.current_row, column=2)

        # Create button to remove last row
        remove_button = tk.Button(self.prescription_info_frame, text="Xóa thuốc", command=self.remove_row_medicine)
        remove_button.grid(row=self.current_row, column=3)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Lời dặn').grid(row=self.current_row, column=0, padx=5, pady=5)
        self.loi_dan_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        self.loi_dan_entry.grid(row=self.current_row, column=1, columnspan=6, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Số điện thoại người khám bệnh').grid(row=self.current_row,
                                                                                          column=0, padx=5, pady=5)
        self.so_dien_thoai_nguoi_kham_benh_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        self.so_dien_thoai_nguoi_kham_benh_entry.grid(row=self.current_row, column=1, columnspan=6, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Ngày tái khám').grid(row=self.current_row, column=0, padx=5,
                                                                          pady=5)
        self.ngay_tai_kham_entry = DateEntry(self.prescription_info_frame, width=12, date_pattern='d/m/yyyy')
        self.ngay_tai_kham_entry.grid(row=self.current_row, column=1, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Ngày giờ kê đơn').grid(row=self.current_row, column=0, padx=5,
                                                                            pady=5)
        self.ngay_gio_ke_don_entry = DateEntry(self.prescription_info_frame, width=12, date_pattern='d/m/yyyy')
        self.ngay_gio_ke_don_entry.grid(row=self.current_row, column=1, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Chữ ký số').grid(row=self.current_row, column=0, padx=5, pady=5)
        self.chu_ky_so_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        self.chu_ky_so_entry.grid(row=self.current_row, column=1, columnspan=6, padx=5, pady=5)

        self.add_row_diagnose()
        self.add_row_medicine()

        self.canvas.configure(width=self.prescription_info_frame.winfo_width())
        self.canvas.configure(height=self.prescription_info_frame.winfo_height())

        self.bind('<Configure>', self.on_resize)

    def add_row_medicine(self, event=None):
        row_thres = self.current_diagnose_count + 6

        for widget in self.prescription_info_frame.grid_slaves():
            if widget.grid_info()['row'] >= row_thres + self.current_medicine_count:
                widget.grid(row=widget.grid_info()['row'] + 1, column=widget.grid_info()['column'])

        ma_thuoc_entry = tk.Entry(self.prescription_info_frame)
        ma_thuoc_entry.grid(row=row_thres + self.current_medicine_count, column=1)

        biet_duoc_entry = tk.Entry(self.prescription_info_frame)
        biet_duoc_entry.grid(row=row_thres + self.current_medicine_count, column=2)

        ten_thuoc_entry = ttk.Combobox(self.prescription_info_frame)
        ten_thuoc_entry.grid(row=row_thres + self.current_medicine_count, column=3)
        ten_thuoc_entry.bind('<KeyRelease>', self.on_keyreleaseMedicineName)
        ten_thuoc_entry.row_index = self.current_medicine_count
        ten_thuoc_entry.bind('<<ComboboxSelected>>', self.on_selectMedicine)

        don_vi_tinh_entry = tk.Entry(self.prescription_info_frame)
        don_vi_tinh_entry.grid(row=row_thres + self.current_medicine_count, column=4)

        so_luong_entry = tk.Entry(self.prescription_info_frame)
        so_luong_entry.grid(row=row_thres + self.current_medicine_count, column=5)

        cach_dung_entry = tk.Entry(self.prescription_info_frame)
        cach_dung_entry.grid(row=row_thres + self.current_medicine_count, column=6)

        self.current_medicine_count = self.current_medicine_count + 1

        self.list_medicine.append((ma_thuoc_entry, biet_duoc_entry, ten_thuoc_entry, don_vi_tinh_entry,
                                   so_luong_entry, cach_dung_entry))

        if self.last_medicine != None:
            self.last_medicine.unbind("<Tab>")

        cach_dung_entry.bind("<Tab>", self.add_row_medicine)
        self.last_medicine = cach_dung_entry
        ma_thuoc_entry.focus()

        self.updateCanvasHeight()

    def remove_row_medicine(self, event=None):
        if self.current_medicine_count <= 1:
            [x.delete(0, tk.END) for x in self.list_medicine[-1]]
            return

        row_thres = self.current_diagnose_count + 6

        last_row = self.list_medicine[-1]
        self.list_medicine = self.list_medicine[:-1]

        [x.destroy() for x in last_row]

        self.current_medicine_count = self.current_medicine_count - 1

        for widget in self.prescription_info_frame.grid_slaves():
            if widget.grid_info()['row'] >= row_thres + self.current_medicine_count:
                widget.grid(row=widget.grid_info()['row'] - 1, column=widget.grid_info()['column'])

        self.last_medicine = self.list_medicine[-1][2]
        self.list_medicine[-1][-1].bind("<Tab>", self.add_row_medicine)

        self.updateCanvasHeight()

    def on_keyreleaseMedicineName(self, event):

        value = event.widget.get()
        value = value.strip().lower()

        self.list_recommend_medicine = getDataManager().searchMedicine(value)
        data = self.list_recommend_medicine[:20]

        queried_data = [x["ten_thuoc"] + " (" + x["ma_thuoc"] + ")" for x in data]

        event.widget['values'] = sorted(queried_data, key=str.lower)

        # self.comboboxPatient['values'] = sorted(queried_data, key=str.lower)
        # self.comboboxPatient.event_generate('<<ComboboxSelected>>')

        # self.list_recommend_medicine.

    def on_selectMedicine(self, event):
        to_query = ' '.join(event.widget.get().split(" ")[:-1])

        selected_value = getDataManager().getMedicine(to_query)

        if len(selected_value) > 0:
            self.setMedicineInfo(event.widget.row_index, selected_value[0])

    def setMedicineInfo(self, index, value):

        to_update_row = self.list_medicine[index]

        [x.delete(0, tk.END) for x in to_update_row]

        to_update_row[0].insert(0, value['ma_thuoc'])
        to_update_row[1].insert(0, value['biet_duoc'])
        to_update_row[2].insert(0, value['ten_thuoc'])
        to_update_row[3].insert(0, value['don_vi_tinh'])
        to_update_row[5].insert(0, value['cach_dung'])

    def savePrescription(self):

        data = {
            'patientName': self.comboboxPatient.get(),
            'medical_id': self.medical_id.get(),
            'patient_id': self.patient_id.get(),
            'date_of_birth': self.date_of_birth.get(),
            'weight': self.weight.get(),
            'sex_var': self.sex_var.get(),
            'insurance_id': self.insurance_id.get(),
            'guardian_info': self.guardian_info.get(),
            'address': self.address.get(),
            'chandoan': self.list_diagnose,
            'luu_y': self.luu_y_entry.get(),
            'hinh_thuc_dieu_tri': self.hinh_thuc_dieu_tri_entry.get(),
            'dot_dung_thuoc': self.dot_dung_thuoc_entry.get(),
            'don_thuoc': self.list_medicine,
            'loi_dan_entry': self.loi_dan_entry.get(),
            'ngay_tai_kham': self.ngay_tai_kham_entry.get(),
            'ngay_gio_ke_don': self.ngay_gio_ke_don_entry.get(),
            'chu_ky_so': self.chu_ky_so_entry.get(),
            'sdt_nguoi_kham': self.so_dien_thoai_nguoi_kham_benh_entry.get()
        }

        getDataManager().inserPrescription(data)

    def resetDianoseAndMedicineList(self):
        for i in range(len(self.list_medicine)):
            self.remove_row_medicine()

        for i in range(len(self.list_diagnose)):
            self.remove_row_diagnose()

    def resetAll(self):
        self.resetDianoseAndMedicineList()

        self.luu_y_entry.delete(0, tk.END)
        self.hinh_thuc_dieu_tri_entry.delete(0, tk.END)
        self.dot_dung_thuoc_entry.delete(0, tk.END)
        self.loi_dan_entry.delete(0, tk.END)
        self.so_dien_thoai_nguoi_kham_benh_entry.delete(0, tk.END)
        self.ngay_tai_kham_entry.delete(0, tk.END)
        self.ngay_gio_ke_don_entry.delete(0, tk.END)
        self.chu_ky_so_entry.delete(0, tk.END)

        self.comboboxPatient.delete(0, tk.END)
        self.medical_id.delete(0, tk.END)
        self.patient_id.delete(0, tk.END)
        self.date_of_birth.delete(0, tk.END)
        self.weight.delete(0, tk.END)
        self.insurance_id.delete(0, tk.END)
        self.guardian_info.delete(0, tk.END)
        self.address.delete(0, tk.END)

    def updateCanvasHeight(self):
        bbox = self.canvas.bbox("all")
        bbox = (bbox[0], bbox[1] , bbox[2], bbox[3] + 20)

        self.canvas.configure(scrollregion=bbox)
        pass
        # self.canvas.configure(height=self.prescription_info_frame.winfo_height())

    def on_mousewheel(self, event):
        # self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        if self.mouse_on_canvas:
            self.canvas.yview_scroll(-int(event.delta / 60), "units")

    # def on_mouse_move_canvas(self, event):
    #     items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
    #     if len(items) > 0:
    #         self.mouse_on_canvas = True
    #     else:
    #         self.mouse_on_canvas = False
        # print(self.mouse_on_canvas)

    def on_enter_pres_frame(self, event):
        self.mouse_on_canvas = True

    def on_leave_pres_frame(self, event):
        self.mouse_on_canvas = False

    def on_resize(self, event):
        self.canvas.configure(height=int(event.height * 0.75))

    def checkValidPrescription(self):
        if len(self.comboboxPatient.get()) == 0:
            messagebox.showerror("Error", "This is an error message")
            return False
        return True

