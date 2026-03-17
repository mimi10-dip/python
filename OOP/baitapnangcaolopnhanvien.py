class NhanVien:
    LUONG_MAX = 50000000   
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong
    def get_tenNhanVien(self):
        return self.tenNhanVien
    def get_luongCoBan(self):
        return self.luongCoBan
    def get_heSoLuong(self):
        return self.heSoLuong
    def set_tenNhanVien(self, ten):
        self.tenNhanVien = ten
    def set_luongCoBan(self, luong):
        self.luongCoBan = luong
    def set_heSoLuong(self, heSo):
        self.heSoLuong = heSo
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong
    def inTTin(self):
        print("Tên:", self.tenNhanVien)
        print("Lương cơ bản:", self.luongCoBan)
        print("Hệ số lương:", self.heSoLuong)
        print("Lương:", self.tinhLuong())
    def tangLuong(self, delta):
        new_luong = self.tinhLuong() + delta

        if new_luong > NhanVien.LUONG_MAX:
            print("Vượt quá lương tối đa!")
            return False
        else:           
            self.luongCoBan += delta / self.heSoLuong
            return True

nv = NhanVien("Diep", 5000000, 2.5)
nv.inTTin()
print("\nTăng lương 5 triệu:")
if nv.tangLuong(5000000):
    print("Tăng thành công!")
else:
    print("Tăng thất bại!")
nv.inTTin()