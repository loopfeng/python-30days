# Chuyển về phân số 
#Fraction là kiểu dữ liệu phân số trong Python, dùng để lưu số dưới dạng tử số / mẫu số một cách chính xác
from fractions import*
#Fraction(<tử số>, <mẫu số>)
frac1 = Fraction(6,9)
frac2 = Fraction(5,10)
frac3 = frac1 + frac2

print(frac3)
