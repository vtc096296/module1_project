from project import *
from project.xuly.xu_ly_quan_ly_nhap_hang import *
from flask import request, redirect, render_template, url_for, session
from datetime import datetime
@app.route('/quan-ly-nhap-hang/dang-nhap', methods = ['GET', 'POST'])
def qlnh_dn():
    thong_bao = ''
    ten_dn = ''
    if request.method == 'POST':
        ten_dn = request.form.get('ten_dn')
        mat_khau = request.form.get('mat_khau')
        nv= ql_nhap_hang_dn(ten_dn, mat_khau)
        if nv == None:
            thong_bao = 'Đăng nhập không thành công'
        else:
            session['quan_ly_nhap_hang'] = nv
            return redirect('/quan-ly-nhap-hang')
    return render_template('quan_ly_nhap_hang/dang_nhap.html',ten_dn = ten_dn, thong_bao = thong_bao)

@app.route('/quan-ly-nhap-hang', methods = ['GET', 'POST'])
def qlnh():
    if session.get('quan_ly_nhap_hang') == None:
        return redirect('/quan-ly-nhap-hang/dang-nhap')
    else:
        ds_tv = doc_danh_sach_tv()
        nv = session.get('quan_ly_nhap_hang')
        if request.method == 'POST':
            chuoi_tra_cuu = request.form.get('search')
            ds_tv = xu_ly_tra_cuu(chuoi_tra_cuu,ds_tv)
        return render_template('quan_ly_nhap_hang/index.html', ds_tv = ds_tv, nv = nv)

@app.route('/quan-ly-nhap-hang/cap-nhat-gia-nhap/<string:Ma_so>', methods = ['GET', 'POST'])
def cap_nhat_gia_nhap(Ma_so):
    if session.get('quan_ly_nhap_hang') == None:
        return redirect('/quan-ly-nhap-hang/dang-nhap')
    else:
        thong_bao = ''
        tv_info = thong_tin_tivi(Ma_so)
        if tv_info == None:
            thong_bao = Ma_so + ' không tồn tại'
        else:
            if request.method == 'POST':
                try:
                    don_gia_nhap = int(request.form.get('don_gia_nhap'))
                    tv_info['Don_gia_Nhap'] = don_gia_nhap
                    ngay = datetime.now().strftime('%d-%m-%Y')
                    ghi_tivi(tv_info)
                    thong_bao = 'Đã cập nhật đơn giá nhập mới : '+  str(don_gia_nhap)
                except:
                    thong_bao = 'Đơn giá không hợp lệ'
        return render_template('quan_ly_nhap_hang/cap_nhat_don_gia_nhap.html',tv_info = tv_info, thong_bao = thong_bao)

@app.route('/quan-ly-nhap-hang/thong-ke-so-luong-ton-ngay', methods = ['GET', 'POST'])
def tk_so_luong_ton():
    if session.get('quan_ly_nhap_hang') == None:
        return redirect('/quan-ly-nhap-hang/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        ds_sl_ton = ds_so_luong_ton()
        
        return render_template('/quan_ly_nhap_hang/tk_so_luong_ton.html', ngay = ngay, ds_sl_ton = ds_sl_ton)
    
@app.route('/quan-ly-nhap-hang/dang-xuat', methods = ['GET', 'POST'])
def qlnh_dang_xuat():
    if session['quan_ly_nhap_hang'] == None:
        return redirect('/quan-ly-nhap-hang/dang-nhap')
    else:
        del session['quan_ly_nhap_hang']
        return redirect('/quan-ly-nhap-hang/dang-nhap')