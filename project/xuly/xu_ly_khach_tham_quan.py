import os
import json

thu_muc_tivi = 'project/static/du_lieu/tivi/'

# Xử lý lưu trữ
def doc_danh_sach_tv():
    ds_tv = []

    for ten_tap_tin in os.listdir(thu_muc_tivi):       
        tv_path = thu_muc_tivi + ten_tap_tin
        f = open(tv_path, 'r', encoding='utf-8')
        info_tv = json.load(f)
        f.close()
        ds_tv.append(info_tv)

    return ds_tv

# Xử lý tra cứu
def xu_ly_tra_cuu(chuoi_tra_cuu, ds_tv):
    ds_tra_cuu = list(filter(lambda tv : chuoi_tra_cuu.upper() in tv['Ten'].upper(), ds_tv))
    return ds_tra_cuu