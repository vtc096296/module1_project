from project import *
from project.xuly.xu_ly_khach_tham_quan import *
from flask import request

@app.route('/', methods = ['GET', 'POST'])
def index():
    chuoi_tim_kiem = ''
    ds_tv = doc_danh_sach_tv()

    if request.method == 'POST':
        chuoi_tim_kiem = request.form.get('search')
        ds_tv = xu_ly_tra_cuu(chuoi_tim_kiem, ds_tv)
    return render_template('khach_tham_quan/index.html',ds_tv = ds_tv, chuoi_tim_kiem = chuoi_tim_kiem)