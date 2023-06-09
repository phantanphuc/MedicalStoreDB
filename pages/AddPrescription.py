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
        self.entry_width = 100
        self.current_row = 0
        self.current_diagnose_count = 0
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

        self.prescription_info_frame = tk.LabelFrame(self, text='Prescription Information')
        self.prescription_info_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.prescription_info_frame, text='Chẩn đoán').grid(row=0, column=0, padx=5, pady=5)
        # chan_doan_entry = tk.Entry(self.prescription_info_frame, width=50)
        # chan_doan_entry.grid(row=0, column=1, padx=5, pady=5)

        name_label = tk.Label(self.prescription_info_frame, text="Mã chẩn đoán")
        name_label.grid(row=0, column=1)

        price_label = tk.Label(self.prescription_info_frame, text="Tên chẩn đoán")
        price_label.grid(row=0, column=2)

        type_label = tk.Label(self.prescription_info_frame, text="Kết luận")
        type_label.grid(row=0, column=3)



        def add_row():

            row_thres = 1

            check = self.prescription_info_frame.grid_slaves(column=0)[:-1]

            for widget in self.prescription_info_frame.grid_slaves():
                if widget.grid_info()['row'] >= row_thres + self.current_diagnose_count:
                    widget.grid(row=widget.grid_info()['row'] + 1, column=widget.grid_info()['column'])


            name_entry = tk.Entry(self.prescription_info_frame)
            name_entry.grid(row=row_thres + self.current_diagnose_count, column=1)

            # Add price field
            price_entry = tk.Entry(self.prescription_info_frame)
            price_entry.grid(row=row_thres + self.current_diagnose_count, column=2)

            # Add type field
            type_entry = tk.Entry(self.prescription_info_frame)
            type_entry.grid(row=row_thres + self.current_diagnose_count, column=3)

            self.current_diagnose_count = self.current_diagnose_count + 1

            # self.current_row += 1
            # [x.grid(row=x.grid_info()['row'] + 1, column=0)
            #  for x in self.prescription_info_frame.grid_slaves(column=0)[:-1]]

            # [x.grid(row=x.grid_info()['row'] + 1, column=2)
            #  for x in self.prescription_info_frame.grid_slaves(column=2)[:-1]]



        add_button = tk.Button(self.prescription_info_frame, text="Add Medicine", command=add_row)
        add_button.grid(row=1, column=2)

        # Create button to remove last row
        remove_button = tk.Button(self.prescription_info_frame, text="Remove Medicine")
        remove_button.grid(row=1, column=3)

        self.current_row = 2


        tk.Label(self.prescription_info_frame, text='Lưu ý').grid(row=self.current_row, column=0, padx=5, pady=5)
        luu_y_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        luu_y_entry.grid(row=self.current_row, column=1, columnspan=3, padx=5, pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame, text='Hình thức điều trị').grid(row=self.current_row, column=0, padx=5, pady=5)
        hinh_thuc_dieu_tri_entry = tk.Entry(self.prescription_info_frame, width=self.entry_width)
        hinh_thuc_dieu_tri_entry.grid(row= self.current_row,column = 1, columnspan=3,padx = 5,pady = 5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Đợt dùng thuốc').grid(row = self.current_row,column = 0,padx = 5,pady = 5)
        dot_dung_thuoc_entry = tk.Entry(self.prescription_info_frame,width = self.entry_width)
        dot_dung_thuoc_entry.grid(row = self.current_row,column = 1, columnspan=3,padx = 5,pady = 5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Thông tin đơn thuốc').grid(row = self.current_row,column = 0,padx = 5,pady = 5)
        thong_tin_don_thuoc_entry = tk.Entry(self.prescription_info_frame,width = self.entry_width)
        thong_tin_don_thuoc_entry.grid(row = self.current_row,column = 1, columnspan=3,padx = 5,pady = 5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Lời dặn').grid(row = self.current_row,column = 0,padx = 5,pady = 5)
        loi_dan_entry = tk.Entry(self.prescription_info_frame,width = self.entry_width)
        loi_dan_entry.grid(row = self.current_row,column = 1, columnspan=3,padx = 5,pady = 5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Số điện thoại người khám bệnh').grid(row=self.current_row,column=0,padx=5,pady=5)
        so_dien_thoai_nguoi_kham_benh_entry=tk.Entry(self.prescription_info_frame,width=self.entry_width)
        so_dien_thoai_nguoi_kham_benh_entry.grid(row=self.current_row,column=1, columnspan=3,padx=5,pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Ngày tái khám').grid(row=self.current_row,column=0,padx=5,pady=5)
        ngay_tai_kham_entry=DateEntry(self.prescription_info_frame,width=12,date_pattern='dd/mm/yyyy')
        ngay_tai_kham_entry.grid(row=self.current_row,column=1,padx=5,pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Ngày giờ kê đơn').grid(row=self.current_row,column=0,padx=5,pady=5)
        ngay_gio_ke_don_entry=DateEntry(self.prescription_info_frame,width=12,date_pattern='dd/mm/yyyy')
        ngay_gio_ke_don_entry.grid(row=self.current_row,column=1,padx=5,pady=5)

        self.current_row = self.current_row + 1

        tk.Label(self.prescription_info_frame,text='Chữ ký số').grid(row=self.current_row,column=0,padx=5,pady=5)
        chu_ky_so_entry=tk.Entry(self.prescription_info_frame,width=self.entry_width)
        chu_ky_so_entry.grid(row=self.current_row,column=1, columnspan=3,padx=5,pady=5)




