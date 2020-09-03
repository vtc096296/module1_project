from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

import project.app_khach_tham_quan
import project.app_nhan_vien_ban_hang
import project.app_nhan_vien_nhap_hang
import project.app_quan_ly_ban_hang
import project.app_quan_ly_nhap_hang
import project.app_quan_ly_cong_ty
