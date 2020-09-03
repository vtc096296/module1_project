from project import *
from project.xuly.xu_ly_quan_ly_ban_hang import *
from flask import request, redirect, render_template, url_for, session
from datetime import datetime
@app.route('/quan-ly-ban-hang/dang-nhap', methods = ['GET', 'POST'])
def qlbh_dn():
    thong_bao = ''
    ten_dn = ''
    if request.method == 'POST':
        ten_dn = request.form.get('ten_dn')
        mat_khau = request.form.get('mat_khau')
        nv= ql_ban_hang_dn(ten_dn, mat_khau)
        if nv == None:
            thong_bao = 'Đăng nhập không thành công'
        else:
            session['quan_ly_ban_hang'] = nv
            return redirect('/quan-ly-ban-hang')
    return render_template('quan_ly_ban_hang/dang_nhap.html',ten_dn = ten_dn, thong_bao = thong_bao)

@app.route('/quan-ly-ban-hang/dang-xuat', methods = ['GET', 'POST'])
def qlbh_dang_xuat():
    if session['quan_ly_ban_hang'] == None:
        return redirect('/quan-ly-ban-hang/dang-nhap')
    else:
        del session['quan_ly_ban_hang']
        return redirect('/quan-ly-ban-hang/dang-nhap')

@app.route('/quan-ly-ban-hang', methods = ['GET', 'POST'])
def qlbh():
    if session.get('quan_ly_nhap_hang') == None:
        return redirect('/quan-ly-ban-hang/dang-nhap')
    else:
        ds_tv = doc_danh_sach_tv()
        nv = session.get('quan_ly_nhap_hang')
        if request.method == 'POST':
            chuoi_tra_cuu = request.form.get('search')
            ds_tv = xu_ly_tra_cuu(chuoi_tra_cuu,ds_tv)
        return render_template('quan_ly_ban_hang/index.html', ds_tv = ds_tv, nv = nv)

@app.route('/quan-ly-ban-hang/cap-nhat-gia-ban/<string:Ma_so>', methods = ['GET', 'POST'])
def cap_nhat_gia_ban(Ma_so):
    if session.get('quan_ly_ban_hang') == None:
        return redirect('/quan-ly-ban-hang/dang-nhap')
    else:
        thong_bao = ''
        tv_info = thong_tin_tivi(Ma_so)
        if tv_info == None:
            thong_bao = Ma_so + ' không tồn tại'
        else:
            if request.method == 'POST':
                try:
                    don_gia_ban = int(request.form.get('don_gia_ban'))
                    tv_info['Don_gia_Ban'] = don_gia_ban
                    ngay = datetime.now().strftime('%d-%m-%Y')
                    ghi_tivi(tv_info)
                    thong_bao = 'Đã cập nhật đơn giá nhập mới : '+  str(don_gia_ban)
                except:
                    thong_bao = 'Đơn giá không hợp lệ'
        return render_template('quan_ly_ban_hang/cap_nhat_don_gia_ban.html',tv_info = tv_info, thong_bao = thong_bao)

@app.route('/quan-ly-ban-hang/thong-ke-so-luong-ton', methods = ['GET', 'POST'])
def qlbh_tk_so_luong_ton():
    if session.get('quan_ly_ban_hang') == None:
        return redirect('/quan-ly-ban-hang/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        ds_sl_ton = ds_so_luong_ton()
        
        return render_template('/quan_ly_ban_hang/tk_so_luong_ton.html', ngay = ngay, ds_sl_ton = ds_sl_ton)

@app.route('/quan-ly-ban-hang/doanh-thu-theo-tivi', methods = ['GET', 'POST'])
def qlbh_doanh_thu_theo_tivi():
    if session.get('quan_ly_ban_hang') == None:
        return redirect('/quan-ly-ban-hang/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        dstv = doc_danh_sach_tv()
        doanh_thu, tong_tien = thong_ke_phieu_ban_ngay(ngay, dstv)
        return render_template('/quan_ly_ban_hang/doanh_thu_theo_tivi.html', ngay = ngay, doanh_thu = doanh_thu, tong_tien= tong_tien)

@app.route('/quan-ly-ban-hang/doanh-thu-theo-nhan-vien', methods = ['GET', 'POST'])
def qlbh_doanh_thu_theo_nhan_vien():
    if session.get('quan_ly_ban_hang') == None:
        return redirect('/quan-ly-ban-hang/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        doanh_thu = doanh_thu_nvbh(ngay)
        return render_template('/quan_ly_ban_hang/doanh_thu_theo_nv.html', ngay = ngay, doanh_thu = doanh_thu)
