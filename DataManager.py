from tinydb import TinyDB, Query, where
import os
from datetime import datetime
import time
from tkinter import messagebox

def decimal_to_base36(decimal):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base36 = ''
    sign = ''

    if decimal < 0:
        sign = '-'
        decimal = -decimal

    while decimal > 0:
        decimal, remainder = divmod(decimal, 36)
        base36 = alphabet[remainder] + base36

    return sign + base36

def getDiseaseList():
    return_value = {}
    if os.path.isfile("./../data/DanhSachBenh.csv"):
        open_path = "./../data/DanhSachBenh.csv"
    else:
        open_path = "./data/DanhSachBenh.csv"

    with open(open_path, 'r', encoding="utf-8") as fin:
        lines = fin.readlines()
        for line in lines:
            info = line.replace("\n", "").split("\t")
            return_value[info[0].lower()] = (info[2], info[3])

    return return_value


class DataManager:
    def __init__(self):
        self.db = TinyDB('Database.json')
        self.patient_table = self.db.table('benh_nhan')
        self.don_thuoc_table = self.db.table('don_thuoc')
        # self.danh_sach_thuoc_table = self.db.table('danh_sach_thuoc')
        self.thuoc_table = self.db.table('thuoc')
        self.test_contains = lambda value, search: search in value.lower()
        self.list_disease = getDiseaseList()

    def insertPatient(self, patient_data):
        qpatient = Query()
        condition = (qpatient.ho_ten_benh_nhan == patient_data['ho_ten_benh_nhan']) & \
                    (qpatient.ngay_sinh_benh_nhan == patient_data['ngay_sinh_benh_nhan'])
        results = self.patient_table.search(condition)

        patient_data['ID'] = patient_data['ho_ten_benh_nhan'] + "_" \
                             + patient_data['ngay_sinh_benh_nhan'] + "_" + str(len(results))

        self.patient_table.insert(patient_data)
        return patient_data['ID']

    def insertPrescription(self, don_thuoc_data):
        self.don_thuoc_table.insert(don_thuoc_data)

    # def insertMedicineList(self, danh_sach_thuoc_data):
    #     self.danh_sach_thuoc_table.insert(danh_sach_thuoc_data)

    def insertMedicine(self, thuoc_data):
        self.thuoc_table.insert(thuoc_data)

    def searchPatient(self, keyword):
        keyword = keyword.lower()
        Patient = Query()
        return self.patient_table.search(Patient.ho_ten_benh_nhan.test(self.test_contains, keyword) |
                                         Patient.ma_dinh_danh_cong_dan.test(self.test_contains, keyword) |
                                         Patient.ma_dinh_danh_y_te.test(self.test_contains, keyword))

    def searchMedicine(self, keyword):
        keyword = keyword.lower()
        Medicine = Query()

        return self.thuoc_table.search(Medicine.ten_thuoc.test(self.test_contains, keyword) |
                                         Medicine.biet_duoc.test(self.test_contains, keyword))

    def getMedicine(self, keyword):
        Medicine = Query()
        return self.thuoc_table.search(Medicine.ten_thuoc == keyword)

    def getMedicineByID(self, keyword):
        Medicine = Query()
        return self.thuoc_table.search(Medicine.ma_thuoc == keyword)

    def getDiseaseFromID(self, disease_id):
        if disease_id.lower() in self.list_disease:
            return self.list_disease[disease_id.lower()]
        else:
            return ""

    def searchDiseaseFromName(self, name):
        name = name.lower()
        return_value = []
        for key in self.list_disease.keys():
            node = self.list_disease[key]
            if name in node[0] or name in node[1]:
                return_value.append((key.capitalize(), node[1]))
        return return_value

    def getPrescriptionID(self, ma_co_so, loai_don_thuoc):
        current_time = int(time.time())
        current_time_encode = decimal_to_base36(current_time)
        return str(ma_co_so) + current_time_encode + str(loai_don_thuoc)

    def inserPrescription(self, data):
        prescription_ID = self.getPrescriptionID("12345", "-c")

        patient_data = {'ho_ten_benh_nhan': data['patientName'],
                        'ma_dinh_danh_y_te': data['medical_id'],
                        'ma_dinh_danh_cong_dan': data['patient_id'],
                        'ngay_sinh_benh_nhan': data['date_of_birth'],
                        'can_nang': data['weight'],
                        'gioi_tinh': data['sex_var'],
                        'ma_so_the_bao_hiem_y_te': data['insurance_id'],
                        'thong_tin_nguoi_giam_ho': data['guardian_info'],
                        'dia_chi': data['address']}

        prescription_data = {'chan_doan': [(x[0].get(), x[2].get()) for x in data['chandoan']],
                             'luu_y': data['luu_y'],
                             'hinh_thuc_dieu_tri': data['hinh_thuc_dieu_tri'],
                             'dot_dung_thuoc': data['dot_dung_thuoc'],
                             'don_thuoc': [(x[0].get(), x[4].get()) for x in data['don_thuoc']],
                             'loi_dan': data['loi_dan_entry'],
                             'ngay_tai_kham': data['ngay_tai_kham'],
                             'ngay_gio_ke_don': data['ngay_gio_ke_don'],
                             'chu_ky_so': data['chu_ky_so'],
                             'sdt_nguoi_kham': data['sdt_nguoi_kham'],
                             'prescription_ID': prescription_ID}

        # check exist
        qpatient = Query()
        condition = (qpatient.ho_ten_benh_nhan == data['patientName']) & \
                    (qpatient.ngay_sinh_benh_nhan == data['date_of_birth'])
        results = self.patient_table.search(condition)

        if len(results) > 0: # TODO Check condition if exist multiple patient
            self.patient_table.update(patient_data, condition)
            prescription_data['patient'] = results[0]['ID']
        else:
            patient_id = self.insertPatient(patient_data)
            prescription_data['patient'] = patient_id

        self.don_thuoc_table.insert(prescription_data)

    def updatePrescription(self, data):

        patient_data = {'ho_ten_benh_nhan': data['patientName'],
                        'ma_dinh_danh_y_te': data['medical_id'],
                        'ma_dinh_danh_cong_dan': data['patient_id'],
                        'ngay_sinh_benh_nhan': data['date_of_birth'],
                        'can_nang': data['weight'],
                        'gioi_tinh': data['sex_var'],
                        'ma_so_the_bao_hiem_y_te': data['insurance_id'],
                        'thong_tin_nguoi_giam_ho': data['guardian_info'],
                        'dia_chi': data['address']}

        prescription_data = {'chan_doan': [(x[0].get(), x[2].get()) for x in data['chandoan']],
                             'luu_y': data['luu_y'],
                             'hinh_thuc_dieu_tri': data['hinh_thuc_dieu_tri'],
                             'dot_dung_thuoc': data['dot_dung_thuoc'],
                             'don_thuoc': [(x[0].get(), x[4].get()) for x in data['don_thuoc']],
                             'loi_dan': data['loi_dan_entry'],
                             'ngay_tai_kham': data['ngay_tai_kham'],
                             'ngay_gio_ke_don': data['ngay_gio_ke_don'],
                             'chu_ky_so': data['chu_ky_so'],
                             'sdt_nguoi_kham': data['sdt_nguoi_kham'],
                             'prescription_ID': data['prescription_ID'],
                             'patient': data['patient']}

        # check exist
        qpatient = Query()
        condition = (qpatient.ho_ten_benh_nhan == data['patientName']) & \
                    (qpatient.ngay_sinh_benh_nhan == data['date_of_birth'])
        results = self.patient_table.search(condition)

        if len(results) > 0: # TODO Check condition if exist multiple patient
            if prescription_data['patient'] != results[0]['ID']:
                answer = messagebox.askquestion("Xác nhận dùm cái", "Bệnh nhân không khớp với đơn thuốc cũ, "
                                                           "bạn có muốn cập nhật bệnh nhân vào đơn thuốc?")
                if answer != "yes":
                    return


            # self.patient_table.update(patient_data, condition)
            # prescription_data['patient'] = results[0]['ID']
        else:
            messagebox.showerror("Lỗi", "Thông tin bệnh nhân không khớp với ai trong dữ liệu cả! Qua bên cửa sổ thêm "
                                          "bệnh nhân để thêm đơn thuốc/ bệnh nhân")
            return

        # self.don_thuoc_table.insert(prescription_data)


    def checkSuitablePrescription(self, pres, keyword):
        return keyword in pres['ho_ten_benh_nhan'].lower()

    def getAllPrescription(self):
        temp = sorted(self.don_thuoc_table.all(),
                                  key=lambda d: datetime.strptime(d['ngay_gio_ke_don'], '%d/%m/%Y'), reverse=True)

        return temp

    def setPatientInfoToPrescription(self, list_pres):
        # print(list_pres)
        return_value = []
        for pres in list_pres:
            patient_info = self.patient_table.search(Query().ID == pres['patient'])[0]
            return_value.append({**pres, **patient_info})

        return return_value

data_manager = DataManager()

def getDataManager():
    return data_manager

######

patient_data = {'ho_ten_benh_nhan': 'John Doe',
                'ma_dinh_danh_y_te': '123456789',
                'ma_dinh_danh_cong_dan': '987654321',
                'ngay_sinh_benh_nhan': '1/1/2000',
                'can_nang': 70,
                'gioi_tinh': 'Nam',
                'ma_so_the_bao_hiem_y_te': '1234567890',
                'thong_tin_nguoi_giam_ho': 'Jane Doe',
                'dia_chi': '123 Main St'}

patient_data_2 = {'ho_ten_benh_nhan': 'John Smith',
                  'ma_dinh_danh_y_te': '123456789',
                  'ma_dinh_danh_cong_dan': '987654321',
                  'ngay_sinh_benh_nhan': '05/20/1975',
                  'can_nang': 80,
                  'gioi_tinh': 'Nam',
                  'ma_so_the_bao_hiem_y_te': '1234567890',
                  'thong_tin_nguoi_giam_ho': 'Jane Smith',
                  'dia_chi': '123 Main St'}

patient_data_3 = {'ho_ten_benh_nhan': 'Sarah Johnson',
                  'ma_dinh_danh_y_te': '111111111',
                  'ma_dinh_danh_cong_dan': '222222222',
                  'ngay_sinh_benh_nhan': '12/01/1990',
                  'can_nang': 55,
                  'gioi_tinh': 'Nữ',
                  'ma_so_the_bao_hiem_y_te': '12343423',
                  'thong_tin_nguoi_giam_ho': 'Mon',
                  'dia_chi': '43432 adsa'}


# data_manager.patient_table.truncate()
#
# data_manager.insertPatient(patient_data)
# data_manager.insertPatient(patient_data_2)
# data_manager.insertPatient(patient_data_3)

# test_contains = lambda value, search: search in value.lower()

# Patient = Query()
# results = data_manager.don_thuoc_table\
#     .search((Query().patient_id == 'John Smith') & (Patient.ngay_sinh_benh_nhan == '05/20/1975'))
# print(results)
# data_manager.don_thuoc_table.truncate()
# print(data_manager.don_thuoc_table.all())

# data_manager.don_thuoc_table.truncate()

# results = data_manager.patient_table.search(Patient.ho_ten_benh_nhan == 'John')
# results = data_manager.patient_table.search(Patient.ho_ten_benh_nhan.test(test_contains, 's'))

# results = data_manager.searchPatient("123")
#
# for res in data_manager.patient_table.all():
#     print(res)
# print(results)

# for res in data_manager.don_thuoc_table.all():
#     print(res)

# data_manager.don_thuoc_table.truncate()

thuoc_data = [{'ma_thuoc': '123a',
               'biet_duoc': 'X medical',
               'ten_thuoc': 'A new Medicine',
               'don_vi_tinh':'Cai',
               'cach_dung':'Put in your mouth'},
              {'ma_thuoc': '456b',
               'biet_duoc': 'Y medical',
               'ten_thuoc': 'B new Medicine',
               'don_vi_tinh':'Cai',
               'cach_dung':'Put in your nose'},
              {'ma_thuoc': '789c',
               'biet_duoc': 'Z medical',
               'ten_thuoc': 'C new Medicine',
               'don_vi_tinh':'Cai',
               'cach_dung':'Put in your ear'},
              {'ma_thuoc': '101d',
               'biet_duoc': 'W medical',
               'ten_thuoc': 'D new Medicine',
               'don_vi_tinh':'Cai',
               'cach_dung':'Put in your eye'}
             ]


#
checkdata = data_manager.getAllPrescription()
#
# checkdata = sorted(checkdata, key=lambda d: datetime.strptime(d['ngay_gio_ke_don'], '%d/%m/%Y'), reverse=True)
#
# for info in checkdata:
#
#     # checktime = datetime.strptime(info['ngay_gio_ke_don'], '%d/%m/%Y')
#     # current_time_encode = decimal_to_base36(int(datetime.timestamp(checktime)))
#     #
#     # qpatient = Query()
#     # condition = qpatient.patient == info['patient']
#     #
#     # info['prescription_ID'] = "12345" + current_time_encode + "-c"
#     #
#     # data_manager.don_thuoc_table.update(info, condition)
#
#     # print('----')
#     print(info)
#     # print(current_time_encode)
#     # print("12345" + current_time_encode + "-c")
#
#     # print(info['ngay_gio_ke_don'])
#
#
# date_string = '3/2/2022'
# checktime = datetime.strptime(date_string, '%d/%m/%Y')
# print(int(datetime.timestamp(checktime)))
# #



