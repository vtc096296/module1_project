import os
import json

thu_muc_tivi = 'project/static/du_lieu/tivi/'
thu_muc_cong_ty = 'project/static/du_lieu/Cong_ty/'
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


# Lấy thông tin từ file Cong_ty.json
def thong_tin_cong_ty():
    f = open(thu_muc_cong_ty + 'Cong_ty.json', 'r', encoding= 'utf-8')
    info = json.load(f)
    f.close()
    return info

# Xử lý đăng nhập quản lý nhập hàng
def ql_nhap_hang_dn(ten_dn, mk):
    info = thong_tin_cong_ty()
    for item in info['Danh_sach_Quan_ly_Nhap_hang']:
        if ten_dn == item['Ten_dang_nhap'] and mk == item['Mat_khau']:
            return item
        else:
            return None

# Lấy thông tin tivi
def thong_tin_tivi(ma_so_tv):
    if os.path.exists(thu_muc_tivi + ma_so_tv + '.json'):
        f = open(thu_muc_tivi + ma_so_tv + '.json', 'r', encoding= 'utf-8')
        noi_dung = json.load(f)
        f.close()
        return noi_dung
    else:
        return None

# Ghi thông tin tivi
def ghi_tivi(tivi):
    f= open(thu_muc_tivi + tivi['Ma_so'] + '.json', 'w', encoding= 'utf-8')
    json.dump(tivi,f, indent=4, ensure_ascii= False)
    f.close()

# Danh sách số lượng tồn
def ds_so_luong_ton():
    dstv = doc_danh_sach_tv()
    ds_nhom_tv = thong_tin_cong_ty()['Danh_sach_Nhom_Tivi']
    ds_sl_ton = []
    stt = 1
    for nhom_tv in ds_nhom_tv:
        dic = {'Nhom_Tivi' : nhom_tv['Ten'], 'So_luong_ton':0, 'STT':stt}

        for tv in dstv:
            if tv['Nhom_Tivi']['Ma_so'] == nhom_tv['Ma_so']:
                dic['So_luong_ton'] += tv['So_luong_Ton']

        ds_sl_ton.append(dic)
        stt+=1
    return ds_sl_ton
        
