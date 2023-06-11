from tinydb import TinyDB, Query

class DataManager:
    def __init__(self):
        self.db = TinyDB('Database.json')
        self.patient_table = self.db.table('benh_nhan')
        self.don_thuoc_table = self.db.table('don_thuoc')
        self.danh_sach_thuoc_table = self.db.table('danh_sach_thuoc')
        self.thuoc_table = self.db.table('thuoc')

    def insertPatient(self, patient_data):
        self.patient_table.insert(patient_data)

    def insertPrescription(self, don_thuoc_data):
        self.don_thuoc_table.insert(don_thuoc_data)

    def insertMedicineList(self, danh_sach_thuoc_data):
        self.danh_sach_thuoc_table.insert(danh_sach_thuoc_data)

    def insertMedicine(self, thuoc_data):
        self.thuoc_table.insert(thuoc_data)


data_manager = DataManager()

def getDataManager():
    return data_manager

######

patient_data = {'ho_ten_benh_nhan': 'John Doe',
                'ma_dinh_danh_y_te': '123456789',
                'ma_dinh_danh_cong_dan': '987654321',
                'ngay_sinh_benh_nhan': '01/01/2000',
                'can_nang': 70,
                'gioi_tinh': 'Male',
                'ma_so_the_bao_hiem_y_te': '1234567890',
                'thong_tin_nguoi_giam_ho': 'Jane Doe',
                'dia_chi': '123 Main St'}

patient_data_2 = {'ho_ten_benh_nhan': 'John Smith',
                  'ma_dinh_danh_y_te': '123456789',
                  'ma_dinh_danh_cong_dan': '987654321',
                  'ngay_sinh_benh_nhan': '05/20/1975',
                  'can_nang': 80,
                  'gioi_tinh': 'Male',
                  'ma_so_the_bao_hiem_y_te': '1234567890',
                  'thong_tin_nguoi_giam_ho': 'Jane Smith',
                  'dia_chi': '123 Main St'}

patient_data_3 = {'ho_ten_benh_nhan': 'Sarah Johnson',
                  'ma_dinh_danh_y_te': '111111111',
                  'ma_dinh_danh_cong_dan': '222222222',
                  'ngay_sinh_benh_nhan': '12/01/1990',
                  'can_nang': 55,
                  'gioi_tinh': 'Female',
                  'ma_so_the_bao_hiem_y_te': '12343423',
                  'thong_tin_nguoi_giam_ho': 'Mon',
                  'dia_chi': '43432 adsa'}


# data_manager.insertPatient(patient_data_2)
# data_manager.insertPatient(patient_data_3)

# Patient = Query()
# results = data_manager.patient_table.search(Patient.ho_ten_benh_nhan == 'John Doe')
# print(results)


