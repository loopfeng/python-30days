#Sử dụng print để in ra thông tin
print("Hello World!")
a = 100
b = 200
c = 300
print (a,b,c, sep = " - ")  # In ra giá trị của a, b, c với dấu phân cách là " - "
print("Giá trị của a là:", a)  # In ra giá trị của a
print("Giá trị của b là:", b)  # In ra giá trị của b
print("Giá trị của c là:", c)  # In ra giá trị của c
print(a,b,end = " -\n ")
print(c)
#Comment
# Đây là một comment đơn dòng
"""
Đây là một comment đa dòng
Bạn có thể viết nhiều dòng comment ở đây"""
#Bài tập
"""ten = input("Nhập tên của bạn: ")
tuoi = int(input("Nhập tuổi của bạn: "))
print("Xin chào", ten + "!")
print("Bạn", tuoi, "tuổi. Năm nay bạn sinh năm", 2025 - tuoi)"""
import os
os.system('cls')# Xóa những gì đã in ra trước đó
ten = input("Nhap ten cua ban:")
tuoi = int(input("Nhap tuoi cua ban:"))
print("Xin chao", ten + "!")
print("Ban", tuoi, "tuoi.Nam nay ban sinh nam", 2026 - tuoi)

