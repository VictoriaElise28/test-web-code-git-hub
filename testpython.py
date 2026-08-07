print(" chuyện gì đã xảy ra")
print(" ai vậy ạ")##print(" chuyện gì đã xảy ra")
##print(" ai vậy ạ")

#Bài 1
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
ky_tu_dac_biet = "!@#$%^&*()"
tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet
print("Tất cả:", tat_ca)

#Bài 2
danh_sach = ['P', 'y', 't', 'h', 'o', 'n']
chuoi = "".join(danh_sach)
print("Kết quả:", chuoi)


#Bài 3
import random

do_dai = int(input("Nhập độ dài mật khẩu: "))

kho_ky_tu = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
mat_khau = ""

for i in range(do_dai):
    mat_khau += random.choice(kho_ky_tu)

print("Mật khẩu:", mat_khau)