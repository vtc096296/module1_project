import json
import os
from datetime import datetime

thu_muc_cty = 'project/static/du_lieu/Cong_ty/'

def doc_thong_tin_cty():
    path = 'project/static/du_lieu/Cong_ty/' + 'Cong_ty.json'
    if os.path.exists(path):
        f = open(path, 'r', encoding='utf-8')
        info = json.load(f)
        f.close()
    return info

def doc_thong_tin_nv(cong_viec):
    dsnv = doc_thong_tin_cty()
    nv = dsnv[cong_viec]
    return nv

# def nhan_vien_ban_hang():
#     dsnv = doc_thong_tin_cty()
#     nv = dsnv['Danh_sach_Nhan_vien_Ban_hang']
#     return nv

# def nhan_vien_nhap_hang():
#     dsnv = doc_thong_tin_cty()
#     nv = dsnv['Danh_sach_Nhan_vien_Nhap_hang']
#     return nv

# def quan_ly_nhap_hang():
#     dsnv = doc_thong_tin_cty()
#     nv = dsnv['Danh_sach_Quan_ly_Nhap_hang']
#     return nv

# def quan_ly_ban_hang():
#     dsnv = doc_thong_tin_cty()
#     nv = dsnv['Danh_sach_Quan_ly_Ban_hang']
#     return nv

# def quan_ly_cong_ty():
#     dsnv = doc_thong_tin_cty()
#     nv = dsnv['Danh_sach_Quan_ly_Cong_ty']
#     return nv