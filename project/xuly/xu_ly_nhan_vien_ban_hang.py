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

# Xử lý đăng nhập nhân viên bán hàng
def xu_ly_dang_nhap_nvbh(ten_dn, mk):
    info_dn = thong_tin_cong_ty()['Danh_sach_Nhan_vien_Ban_hang']
    nv = None
    for item in info_dn:
        if item['Ten_dang_nhap'] == ten_dn and item['Mat_khau'] == mk:
            nv = item
    return nv

# Lấy thông tin nhóm tivi
def thong_tin_tivi_nvbh(nv, dstv):
    ds_tv = []
    for dsntv in nv['Danh_sach_Nhom_Tivi']:
        for tv in dstv :
            if dsntv['Ma_so'] == tv['Nhom_Tivi']['Ma_so']:
                ds_tv.append(tv)
    return ds_tv

# Lấy thông tin tv
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

# Thống kê phiếu bán ngày
def thong_ke_phieu_ban_ngay(ngay, dstv_nvbh):
    ds_phieu_ban = []
    tong_tien = 0
    stt = 1
    for tv in dstv_nvbh:
        for phieu_ban in tv['Danh_sach_Phieu_Ban']:
            if ngay == phieu_ban['Ngay']:
                tong_tien+= phieu_ban['Tien']
                ds_phieu_ban.append({'STT':stt,'Ten':tv['Ten'], 'So_luong':phieu_ban['So_luong'], 'don_gia':phieu_ban['Don_gia'], 'tien':phieu_ban['Tien']})
                stt+=1
    return ds_phieu_ban, tong_tien