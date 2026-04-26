#Kiểu dữ liệu số trong Python
#gán cho biến a giá trị là 4. Với 4 là kiểu số nguyên ( Intergers)
a = 4
print(a)
#kiểu dữ liệu của a
print(type(a))
#gán cho biến b giá trị là 1.96. Với 1.96 là kiểu số thực ( Float)
b = 1.9687348248932456456
print(b)
#kiểu dữ liệu của b
print(type(b))

#Kiểu Decimal

#lấy toàn bộ nội dung của thư viện decimal
#Từ thư viện Decimal import mọi thứ vào from
from decimal import*
# Lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 3

f = 10/3
print(f)
print(type(f))

d = (Decimal(10)/Decimal(3))
print(d)
print(type(d))