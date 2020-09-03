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

# Xử lý đăng nhập nhân viên nhập hàng
def xu_ly_dang_nhap_nvnh(ten_dn, mk):
    info_dn = thong_tin_cong_ty()['Danh_sach_Nhan_vien_Nhap_hang']
    nv = None
    for item in info_dn:
        if item['Ten_dang_nhap'] == ten_dn and item['Mat_khau'] == mk:
            nv = item
    return nv

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

#Thông tin phiếu nhập hàng ngày
def thong_ke_phieu_nhap(ngay, nv):
    danh_sach_tivi = doc_danh_sach_tv()
    danh_sach_tivi_nhap = []
    tong = 0
    stt = 1
    for item in danh_sach_tivi:
        ds_phieu_nhap = item['Danh_sach_Phieu_Nhap']
        for pn in ds_phieu_nhap:
            if pn['Ngay'] == ngay and pn['Nhan_vien']['Ma_so'] == nv:
                danh_sach_tivi_nhap.append({'Ten':item['Ten'], 'So_luong': pn['So_luong'], 'don_gia':pn['Don_gia'], 'tien':pn['Tien'], 'STT':stt })
                tong+= pn['Tien']
                stt+=1
    
    return danh_sach_tivi_nhap, tong

