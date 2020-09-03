from project import *
from project.xuly.xu_ly_quan_ly_cong_ty import *
from flask import request, redirect, render_template, url_for, session
from datetime import datetime
@app.route('/quan-ly-cong-ty/dang-nhap', methods = ['GET', 'POST'])
def qlct_dn():
    thong_bao = ''
    ten_dn = ''
    if request.method == 'POST':
        ten_dn = request.form.get('ten_dn')
        mat_khau = request.form.get('mat_khau')
        nv= ql_ban_hang_dn(ten_dn, mat_khau)
        if nv == None:
            thong_bao = 'Đăng nhập không thành công'
        else:
            session['quan_ly_cong_ty'] = nv
            return redirect('/quan-ly-cong-ty')
    return render_template('quan_ly_cong_ty/dang_nhap.html',ten_dn = ten_dn, thong_bao = thong_bao)

@app.route('/quan-ly-cong-ty/dang-xuat', methods = ['GET', 'POST'])
def qlct_dang_xuat():
    if session['quan_ly_cong_ty'] == None:
        return redirect('/quan-ly-cong-ty/dang-nhap')
    else:
        del session['quan_ly_ban_hang']
        return redirect('/quan-ly-cong-ty/dang-nhap')

@app.route('/quan-ly-cong-ty', methods = ['GET', 'POST'])
def qlct():
    if session['quan_ly_cong_ty'] == None:
        return redirect('/quan-ly-cong-ty/dang-nhap')
    else:
        ds_tv = doc_danh_sach_tv()
        nv = session.get('quan_ly_cong_ty')
        if request.method == 'POST':
            chuoi_tra_cuu = request.form.get('search')
            ds_tv = xu_ly_tra_cuu(chuoi_tra_cuu,ds_tv)
        return render_template('quan_ly_cong_ty/index.html', ds_tv = ds_tv, nv = nv)


@app.route('/quan-ly-cong-ty/thong-ke-so-luong-ton', methods = ['GET', 'POST'])
def qlct_tk_so_luong_ton():
    if session['quan_ly_cong_ty'] == None:
        return redirect('/quan-ly-cong-ty/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        ds_sl_ton = ds_so_luong_ton()
        
        return render_template('quan_ly_cong_ty/tk_so_luong_ton.html', ngay = ngay, ds_sl_ton = ds_sl_ton)

@app.route('/quan-ly-cong-ty/doanh-thu-theo-tivi', methods = ['GET', 'POST'])
def qlct_doanh_thu_theo_tivi():
    if session['quan_ly_cong_ty'] == None:
        return redirect('/quan-ly-cong-ty/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        dstv = doc_danh_sach_tv()
        doanh_thu, tong_tien = thong_ke_phieu_ban_ngay(ngay, dstv)
        return render_template('quan_ly_cong_ty/doanh_thu_theo_tivi.html', ngay = ngay, doanh_thu = doanh_thu, tong_tien= tong_tien)

@app.route('/quan-ly-cong-ty/doanh-thu-theo-nhan-vien', methods = ['GET', 'POST'])
def qlct_doanh_thu_theo_nhan_vien():
    if session['quan_ly_cong_ty'] == None:
        return redirect('/quan-ly-cong-ty/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        doanh_thu = doanh_thu_nvbh(ngay)
        return render_template('quan_ly_cong_ty/doanh_thu_theo_nv.html', ngay = ngay, doanh_thu = doanh_thu)
