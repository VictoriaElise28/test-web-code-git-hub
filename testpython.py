
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

# Bài 4
import random


danh_sach = []


for i in range(5):
    so = random.randint(0, 9)
    danh_sach.append(so)

print("Kết quả:")
print(danh_sach)

import random

# Bài 5
do_dai = int(input("Nhập độ dài mật khẩu: "))

chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
ky_tu_dac_biet = "!@#$%^&*()"
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

print("Mật khẩu:", mat_khau)

import random

# Bài 6
do_dai = int(input("Nhập độ dài mật khẩu: "))

if do_dai < 4:
    print("Cần ít nhất 4 ký tự!")
else:
    chu_thuong = "abcdefghijklmnopqrstuvwxyz"
    chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chu_so = "0123456789"
    ky_tu_dac_biet = "!@#$%^&*()"
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

    print("Mật khẩu:", mat_khau)
    
    import random

# Bài 7
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
ky_tu_dac_biet = "!@#$%^&*()"
tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet

print("Kết quả:")

for i in range(1, 4):
    mat_khau = ""
  
    for j in range(10):
        mat_khau += random.choice(tat_ca)
    
    print(f"{i}. {mat_khau}")