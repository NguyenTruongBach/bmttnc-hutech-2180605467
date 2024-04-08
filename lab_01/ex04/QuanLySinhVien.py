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
        sv = self.findByID(ID)
        if sv is None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv = SinhVien(id, name, sex, major, diemTB)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhvien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhvien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

def deleteById(self, ID):
    isDeleted = False
    sv = self.findByID(ID)
    if (sv is not None):
        self.listSinhvien.remove(sv)
        isDeleted = True
    return isDeleted

def xepLoaiHocLuc(self, sv: SinhVien):
    if (sv.diemTB >= 8):
        sv._hocLuc = "Gioi"
    elif (sv. diemTB >= 6.5):
        sv. hocLuc = "Kha"
    elif (sv. diemTB >= 5):
        sv. hocLuc = "Trung binh"
    else:
        sv. hocLuc = "Yeu"

def showSinhVien(self, listSV):
    print("<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
          .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
    if len(listSV) > 0: 
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} ".format(sv._id, sv._diemTB, sv._hocLuc))  
    print("\n") 

def getListSinhvien(self):
    return self.listSinhVien
        