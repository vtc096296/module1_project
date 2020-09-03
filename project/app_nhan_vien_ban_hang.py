from project import *
from project.xuly.xu_ly_nhan_vien_ban_hang import *
from flask import request, redirect, render_template, url_for, session
from datetime import datetime
@app.route('/nhan-vien-ban-hang/dang-nhap', methods = ['GET', 'POST'])
def nvbh_dn():
    thong_bao = ''
    ten_dn = ''
    if request.method == 'POST':
        ten_dn = request.form.get('ten_dn')
        mat_khau = request.form.get('mat_khau')
        nv= xu_ly_dang_nhap_nvbh(ten_dn, mat_khau)
        if nv == None:
            thong_bao = 'Đăng nhập không thành công'
        else:
            session['nhan_vien_ban_hang'] = nv
            return redirect('/nhan-vien-ban-hang')
    return render_template('nhan_vien_ban_hang/dang_nhap.html',ten_dn = ten_dn, thong_bao = thong_bao)

@app.route('/nhan-vien-ban-hang', methods = ['GET', 'POST'])
def nvbh():
    if session.get('nhan_vien_ban_hang') == None:
        return redirect('/nhan-vien-ban-hang/dang-nhap')
    else:
        ds_tv = doc_danh_sach_tv()
        nv = session.get('nhan_vien_ban_hang')
        dstv_nvbh = thong_tin_tivi_nvbh(nv, ds_tv)
        # print(nv)
        if request.method == 'POST':
            search = request.form.get('search')
            dstv_nvbh = xu_ly_tra_cuu(search, dstv_nvbh)
    return render_template('nhan_vien_ban_hang/index.html', ds_tv = dstv_nvbh, nv=nv)

@app.route('/nhan-vien-ban-hang/dang-xuat', methods = ['GET', 'POST'])
def nvbh_dang_xuat():
    if session['nhan_vien_ban_hang'] == None:
        return redirect('/nhan-vien-ban-hang/dang-nhap')
    else:
        del session['nhan_vien_ban_hang']
        return redirect('/nhan-vien-ban-hang/dang-nhap')

@app.route('/nhan-vien-ban-hang/ban-hang/<string:Ma_so>', methods = ['GET', 'POST'])
def nvbh_ban_hang(Ma_so):
    if session.get('nhan_vien_ban_hang') == None:
        return redirect('/nhan-vien-ban-hang/dang-nhap')
    else:
        tv_info = thong_tin_tivi(Ma_so)
        nv = session.get('nhan_vien_ban_hang')
        thong_bao = ''
        ngay = datetime.now().strftime('%d-%m-%Y')
        if tv_info == None :
            thong_bao = Ma_so + ' không tồn tại'
        else:
            if request.method == 'POST':
                sl_ban = int(request.form.get('sl_ban'))
                sl_ton = tv_info['So_luong_Ton']
                try:
                    if sl_ton >= sl_ban:
                        
                        tv_info['So_luong_Ton'] = tv_info['So_luong_Ton'] - sl_ban
                        tv_info['Danh_sach_Phieu_Ban'].append({'Ngay':ngay, 'So_luong':sl_ban, 'Don_gia':tv_info['Don_gia_Ban'], 'Tien':tv_info['Don_gia_Ban']*sl_ban, 'Nhan_vien':{'Ho_ten': nv['Ho_ten'], 'Ma_so':nv['Ma_so']}})
                        ghi_tivi(tv_info)
                        thong_bao = 'Bán thành công'
                    elif sl_ton < sl_ban:
                        thong_bao = 'Số lượng tồn kho không đủ để bán. Xin nhập lại số lượng'
                except:
                    thong_bao = 'Số lượng không hợp lệ'

    return render_template('nhan_vien_ban_hang/ban_hang.html', tv_info = tv_info, thong_bao = thong_bao )

@app.route('/nhan-vien-ban-hang/thong-ke-phieu-ban-ngay', methods = ['GET', 'POST'])
def tk_phieu_ban_ngay():
    if session.get('nhan_vien_ban_hang') == None:
        return redirect('/nhan-vien-ban-hang/dang-nhap')
    else:
        # <--Lay ngay hien tai-->
        ngay = datetime.now().strftime('%d-%m-%Y') 
        # </--Lay ngay hien tai-->

        # <--Lấy danh sách tivi của nhân viên bán hàng-->
        ds_tv = doc_danh_sach_tv()                      
        nv = session.get('nhan_vien_ban_hang')
        dstv_nvbh = thong_tin_tivi_nvbh(nv, ds_tv)
        # </--Lấy danh sách tivi của nhân viên bán hàng-->

        # <--Thống kê phiếu bán, tổng tiền, số thứ tự-->
        tk_pb, tong_tien = thong_ke_phieu_ban_ngay(ngay, dstv_nvbh)
        # </--Thống kê phiếu bán và tổng tiền-->

    return render_template('nhan_vien_ban_hang/thong_ke_phieu_ban.html', tk_pb = tk_pb, tong_tien = tong_tien, ngay = ngay)