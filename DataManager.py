from tinydb import TinyDB, Query

class DataManager:
    def __init__(self):
        self.db = TinyDB('Database.json')
        self.patient_table = self.db.table('benh_nhan')
        self.don_thuoc_table = self.db.table('don_thuoc')
        self.danh_sach_thuoc_table = self.db.table('danh_sach_thuoc')
        self.thuoc_table = self.db.table('thuoc')
        self.test_contains = lambda value, search: search in value.lower()

    def insertPatient(self, patient_data):
        self.patient_table.insert(patient_data)

    def insertPrescription(self, don_thuoc_data):
        self.don_thuoc_table.insert(don_thuoc_data)

    def insertMedicineList(self, danh_sach_thuoc_data):
        self.danh_sach_thuoc_table.insert(danh_sach_thuoc_data)

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


data_manager = DataManager()

def getDataManager():
    return data_manager

######

patient_data = {'ho_ten_benh_nhan': 'John Doe',
                'ma_dinh_danh_y_te': '123456789',
                'ma_dinh_danh_cong_dan': '987654321',
                'ngay_sinh_benh_nhan': '01/01/2000',
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


# data_manager.insertPatient(patient_data)
# data_manager.insertPatient(patient_data_2)
# data_manager.insertPatient(patient_data_3)

test_contains = lambda value, search: search in value.lower()


# results = data_manager.patient_table.search(Patient.ho_ten_benh_nhan == 'John')
# results = data_manager.patient_table.search(Patient.ho_ten_benh_nhan.test(test_contains, 's'))

# results = data_manager.searchPatient("123")
#
# for res in results:
#     print(res)
# print(results)

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
Medicine = Query()
results = data_manager.getMedicine('C new Medicine')

for res in results:
    print(res)




