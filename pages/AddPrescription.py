try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from tkinter import ttk
from tkcalendar import DateEntry


class AddPrescriptionForm(tk.Frame):
    def __init__(self, parent=None, controller=None):
        tk.Frame.__init__(self, parent)
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        # Create a frame for patient information
        patient_info_frame = tk.LabelFrame(self, text="Patient Information")
        patient_info_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(patient_info_frame, text="Tên bệnh nhân").grid(row=0, column=0)
        self.patient_name = tk.Entry(patient_info_frame)
        self.patient_name.grid(row=0, column=1)

        tk.Label(patient_info_frame, text="Định danh y tế").grid(row=1, column=0)
        self.medical_id = tk.Entry(patient_info_frame)
        self.medical_id.grid(row=1, column=1)

        tk.Label(patient_info_frame, text="Định danh công dân").grid(row=2, column=0)
        self.patient_id = tk.Entry(patient_info_frame)
        self.patient_id.grid(row=2, column=1)

        tk.Label(patient_info_frame, text="Ngày sinh").grid(row=3, column=0)
        self.date_of_birth = DateEntry(patient_info_frame)
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

        # Create a frame for prescription information

        prescription_info_frame = tk.LabelFrame(self, text='Prescription Information')
        prescription_info_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(prescription_info_frame, text='Chẩn đoán').grid(row=0, column=0, padx=5, pady=5)
        chan_doan_entry = tk.Entry(prescription_info_frame, width=50)
        chan_doan_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(prescription_info_frame, text='Lưu ý').grid(row=1, column=0, padx=5, pady=5)
        luu_y_entry = tk.Entry(prescription_info_frame, width=50)
        luu_y_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(prescription_info_frame, text='Hình thức điều trị').grid(row=2, column=0, padx=5, pady=5)
        hinh_thuc_dieu_tri_entry = tk.Entry(prescription_info_frame, width=50)
        hinh_thuc_dieu_tri_entry.grid(row= 2,column = 1,padx = 5,pady = 5)

        tk.Label(prescription_info_frame,text='Đợt dùng thuốc').grid(row = 3,column = 0,padx = 5,pady = 5)
        dot_dung_thuoc_entry = tk.Entry(prescription_info_frame,width = 50)
        dot_dung_thuoc_entry.grid(row = 3,column = 1,padx = 5,pady = 5)

        tk.Label(prescription_info_frame,text='Thông tin đơn thuốc').grid(row = 4,column = 0,padx = 5,pady = 5)
        thong_tin_don_thuoc_entry = tk.Entry(prescription_info_frame,width = 50)
        thong_tin_don_thuoc_entry.grid(row = 4,column = 1,padx = 5,pady = 5)

        tk.Label(prescription_info_frame,text='Lời dặn').grid(row = 5,column = 0,padx = 5,pady = 5)
        loi_dan_entry = tk.Entry(prescription_info_frame,width = 50)
        loi_dan_entry.grid(row = 5,column = 1,padx = 5,pady = 5)

        tk.Label(prescription_info_frame,text='Số điện thoại người khám bệnh').grid(row=6,column=0,padx=5,pady=5)
        so_dien_thoai_nguoi_kham_benh_entry=tk.Entry(prescription_info_frame,width=50)
        so_dien_thoai_nguoi_kham_benh_entry.grid(row=6,column=1,padx=5,pady=5)

        tk.Label(prescription_info_frame,text='Ngày tái khám').grid(row=7,column=0,padx=5,pady=5)
        ngay_tai_kham_entry=DateEntry(prescription_info_frame,width=12,date_pattern='dd/mm/yyyy')
        ngay_tai_kham_entry.grid(row=7,column=1,padx=5,pady=5)

        tk.Label(prescription_info_frame,text='Ngày giờ kê đơn').grid(row=8,column=0,padx=5,pady=5)
        ngay_gio_ke_don_entry=DateEntry(prescription_info_frame,width=12,date_pattern='dd/mm/yyyy')
        ngay_gio_ke_don_entry.grid(row=8,column=1,padx=5,pady=5)

        tk.Label(prescription_info_frame,text='Chữ ký số').grid(row=9,column=0,padx=5,pady=5)
        chu_ky_so_entry=tk.Entry(prescription_info_frame,width=50)
        chu_ky_so_entry.grid(row=9,column=1,padx=5,pady=5)




