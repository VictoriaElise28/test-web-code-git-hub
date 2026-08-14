##BÀI 1##
import string
chu_thuong = string.ascii_lowercase  
chu_hoa = string.ascii_uppercase      
chu_so = string.digits               
ky_tu_dac_biet = string.punctuation  
tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet
print("Tất cả:", tat_ca)

##BÀI 2##
danh_sach = ['P', 'y', 't', 'h', 'o', 'n']
chuoi = "".join(danh_sach)
print("Kết quả:", chuoi)

##BÀI 3##
import random
import string
do_dai = int(input("Nhập độ dài mật khẩu: "))
kho_ky_tu = string.ascii_letters + string.digits + string.punctuation
mat_khau = ""
for i in range(do_dai):
    mat_khau += random.choice(kho_ky_tu)
print("Mật khẩu:", mat_khau)


# Bài 4
import random

danh_sach = []

for i in range(5):
    danh_sach.append(random.randint(0, 9))

print("Kết quả (ví dụ):")
print(danh_sach)


# Bài 5
import random
import string
do_dai = int(input("Nhập: "))
chu_thuong = string.ascii_lowercase
chu_hoa = string.ascii_uppercase
chu_so = string.digits
ky_tu_dac_biet = string.punctuation
tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet
mat_khau_list = [
    random.choice(chu_thuong),
    random.choice(chu_hoa),
    random.choice(chu_so),
    random.choice(ky_tu_dac_biet)
]

for i in range(do_dai - 4):
    mat_khau_list.append(random.choice(tat_ca))
random.shuffle(mat_khau_list)
mat_khau = "".join(mat_khau_list)

print("Kết quả (ví dụ):")
print(mat_khau)