class Nhan_vien():
    def __init__(self, ho_ten, ma_so, ten_dang_nhap, mat_khau):
        self.ho_ten = ho_ten
        self.ma_so = ma_so
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau

class Nhan_vien_nhap_hang(Nhan_vien):
    def __init__(self, cong_viec, ho_ten, ma_so, ten_dang_nhap, mat_khau):
        super().__init__(self, ho_ten, ma_so, ten_dang_nhap, mat_khau)
        self.cong_viec = 'Danh_sach_Nhan_vien_Nhap_hang'
    def nhap_hang(self):
        pass

    def ds_phieu_nhap(self):
        pass

class Nhan_vien_ban_hang(Nhan_vien):
    def __init__(self, cong_viec, ho_ten, ma_so, ten_dang_nhap, mat_khau, nhom_tivi):
        super().__init__(self, ho_ten, ma_so, ten_dang_nhap, mat_khau)
        self.cong_viec = 'Danh_sach_Nhan_vien_Ban_hang'
        self.nhom_tivi = nhom_tivi

    def ban_hang(self):
        pass

    def ds_phieu_nhap(self):
        pass
    
class Quan_ly_nhap_hang(Nhan_vien):
    def __init__(self, cong_viec, ho_ten, ma_so, ten_dang_nhap, mat_khau):
        super().__init__(ho_ten, ma_so, ten_dang_nhap, mat_khau)
        self.cong_viec = 'Danh_sach_Quan_ly_Nhap_hang'
    def xem_so_luong_ton(self):
        pass

    def cap_nhat_gia_nhap(self):
        pass

class Quan_ly_ban_hang(Nhan_vien):
    def __init__(self, cong_viec, ho_ten, ma_so, ten_dang_nhap, mat_khau):
        super().__init__(ho_ten, ma_so, ten_dang_nhap, mat_khau)
        self.cong_viec = 'Danh_sach_Quan_ly_Ban_hang'
    def cap_nhat_gia_ban(self):
        pass

    def xem_so_luong_ton(self):
        pass

    def xem_doanh_thu_theo_tivi(self):
        pass

    def xem_doanh_thu_theo_nhan_vien(self):
        pass


class Quan_ly_cong_ty(Nhan_vien):
    def __init__(self, cong_viec, ho_ten, ma_so, ten_dang_nhap, mat_khau):
        super().__init__(ho_ten, ma_so, ten_dang_nhap, mat_khau)