from flask import FLask, render_template, redirect, url_for, request

@app.route('/Dang-nhap', methods = ['GET','POST'])
def dang_nhap():
    return render_template('/dang_nhap.html')