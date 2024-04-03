from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
    if (self.soLuongSinhVien() > 0):
        maxId =  self.listSinhVien[0]._id
        for sv in self.listSinhVien:
            if (maxId < sv._id):
                maxId = sv._id
                maxId = maxId + 1
            return maxId
        def soLuongSinhVien(self):
            return self.listSinhVien._len_()
        
        def nhapSinhVien(self):
            svId = self.generateID()
            name = input("Nhap Ten Sinh Vien: ")
            sex = input("Nhap Gioi Tinh Sinh Vien: ")
            major = input("Nhap Chyuen Nganh Sinh Vien: ")
            diemTB = float(input("Nhap Diem Cua Sinh Vien: "))
            sv = SinhVien(svId, name, sex, major, diemTB)
            self.xepLoaiHocLuc(sv)
            self.listSinhVien.append(sv)

        def updateSinhVien(self, ID):
            
        