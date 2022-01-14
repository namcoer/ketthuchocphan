ten = input(" Nhập tên đầy đủ:  ")
print(ten)
n = len(ten)
def isThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = int(input(" co thuan nghich "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
m = int(input(" khong thuan nghich "));
print("Tổng các chữ số của", m , "là", iskoThuanNghich(m));
