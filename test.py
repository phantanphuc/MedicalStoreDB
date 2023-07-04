dictdata = {'chan_doan': [['A01', 'Đau'], ['B54', 'A']], 'luu_y': 'AASAS', 'hinh_thuc_dieu_tri': 'aSASAS', 'dot_dung_thuoc': 'DSASA', 'don_thuoc': [['456b', '']], 'loi_dan': 'DD', 'ngay_tai_kham': '14/6/2023', 'ngay_gio_ke_don': '27/6/2023', 'chu_ky_so': 'qwewewq', 'patient': 'Anh_5/6/2023_0', 'prescription_ID': '12345rwvdw0-c', 'sdt_nguoi_kham': '', 'synced': False, 'ho_ten_benh_nhan': 'Anh', 'ma_dinh_danh_y_te': '123123', 'ma_dinh_danh_cong_dan': '4343213123', 'ngay_sinh_benh_nhan': '5/6/2023', 'can_nang': '33', 'gioi_tinh': 'Nữ', 'ma_so_the_bao_hiem_y_te': '213', 'thong_tin_nguoi_giam_ho': 'AAA', 'dia_chi': '423332', 'ID': 'Anh_5/6/2023_0'}


import pandas as pd

print(pd.DataFrame.from_dict(dictdata))

