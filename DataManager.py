from tinydb import TinyDB, Query, where
import os

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

    def inserPrescription(self, data):
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
                             'chu_ky_so': data['chu_ky_so']}

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

        # data = {
        #     'patientName': self.comboboxPatient.get(),
        #     'medical_id': self.medical_id.get(),
        #     'patient_id': self.patient_id.get(),
        #     'date_of_birth': self.date_of_birth.get(),
        #     'weight': self.weight.get(),
        #     'sex_var': self.sex_var.get(),
        #     'insurance_id': self.insurance_id.get(),
        #     'guardian_info': self.guardian_info.get(),
        #     'chandoan': [x.get() for x in self.list_diagnose],
        #     'luu_y': self.luu_y_entry.get(),
        #     'hinh_thuc_dieu_tri': self.hinh_thuc_dieu_tri_entry.get(),
        #     'dot_dung_thuoc': self.dot_dung_thuoc_entry.get(),
        #     'don_thuoc': [x.get() for x in self.list_medicine],
        #     'loi_dan_entry': self.loi_dan_entry.get(),
        #     'ngay_tai_kham': self.ngay_tai_kham_entry.get(),
        #     'ngay_gio_ke_don': self.ngay_gio_ke_don_entry.get(),
        #     'chu_ky_so': self.chu_ky_so_entry.get(),
        # }

    def getAllPrescription(self):
        return self.don_thuoc_table.all() #TODO filter and sort by time

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



# [data_manager.insertMedicine(x) for x in thuoc_data]

# results = data_manager.searchMedicine("z")
# Medicine = Query()
# results = data_manager.getMedicine('C new Medicine')
#
# for res in results:
#     print(res)

# print(data_manager.searchDiseaseFromName("flu"))

# print(data_manager.getDiseaseFromID("A03"))
# data_manager.don_thuoc_table.truncate()
