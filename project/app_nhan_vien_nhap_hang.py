from project import *
from project.xuly.xu_ly_nhan_vien_nhap_hang import *
from flask import request, redirect, render_template, url_for, session
from datetime import datetime
@app.route('/nhan-vien-nhap-hang/dang-nhap', methods = ['GET', 'POST'])
def nvnh_dn():
    thong_bao = ''
    ten_dn = ''
    if request.method == 'POST':
        ten_dn = request.form.get('ten_dn')
        mat_khau = request.form.get('mat_khau')
        nv= xu_ly_dang_nhap_nvnh(ten_dn, mat_khau)
        if nv == None:
            thong_bao = 'Đăng nhập không thành công'
        else:
            session['nhan_vien_nhap_hang'] = nv
            return redirect('/nhan-vien-nhap-hang')
    return render_template('nhan_vien_nhap_hang/dang_nhap.html',ten_dn = ten_dn, thong_bao = thong_bao)

@app.route('/nhan-vien-nhap-hang', methods = ['GET', 'POST'])
def nvnh():
    if session.get('nhan_vien_nhap_hang') == None:
        return redirect('/nhan-vien-nhap-hang/dang-nhap')
    else:
        ds_tv = doc_danh_sach_tv()
        if request.method == 'POST':
            chuoi_tra_cuu = request.form.get('search')
            ds_tv = xu_ly_tra_cuu(chuoi_tra_cuu,ds_tv)
        return render_template('nhan_vien_nhap_hang/index.html', ds_tv = ds_tv)

@app.route('/nhan-vien-nhap-hang/nhap-hang/<string:Ma_so>', methods = ['GET', 'POST'])
def nhap_hang(Ma_so):
    if session.get('nhan_vien_nhap_hang') == None:
        return redirect('/nhan-vien-nhap-hang/dang-nhap')
    else:
        thong_bao = ''
        tv_info = thong_tin_tivi(Ma_so)
        if tv_info == None:
            thong_bao = Ma_so + ' không tồn tại'
        else:
            if request.method == 'POST':
                try:
                    sl = int(request.form.get('nhap_sl'))
                    tv_info['So_luong_Ton'] = tv_info['So_luong_Ton'] + sl
                    nvnh = session.get('nhan_vien_nhap_hang')
                    
                    nv_info = {'Ho_ten':nvnh['Ho_ten'],'Ma_so':nvnh['Ma_so']}
                    ngay = datetime.now().strftime('%d-%m-%Y')
                    dspn = {'Ngay':ngay, 'So_luong':sl, 'Don_gia': tv_info['Don_gia_Nhap'], 'Tien':tv_info['Don_gia_Nhap']*sl, 'Nhan_vien':nv_info}
                    tv_info['Danh_sach_Phieu_Nhap'].append(dspn)
                    # print(dspn)
                    ghi_tivi(tv_info)
                    thong_bao = 'Da luu phieu nhap'
                except:
                    thong_bao = 'Số lượng không hợp lệ'
        return render_template('nhan_vien_nhap_hang/nhap_hang.html',tv_info = tv_info, thong_bao = thong_bao)

@app.route('/nhan-vien-nhap-hang/phieu-nhap-hang-moi-ngay', methods = ['GET', 'POST'])
def tkpn():
    if session.get('nhan_vien_nhap_hang') == None:
        return redirect('/nhan-vien-nhap-hang/dang-nhap')
    else:
        ngay = datetime.now().strftime('%d-%m-%Y')
        nvnh = session.get('nhan_vien_nhap_hang')['Ma_so']
        tk_pn, tong = thong_ke_phieu_nhap(ngay, nvnh)
        
        return render_template('nhan_vien_nhap_hang/thong_ke_phieu_nhap.html', tk_pn = tk_pn, tong_tien =tong, ngay = ngay)
    
@app.route('/nhan-vien-nhap-hang/dang-xuat', methods = ['GET', 'POST'])
def nvnh_dang_xuat():
    del session['nhan_vien_nhap_hang']
    return redirect('/nhan-vien-nhap-hang/dang-nhap')