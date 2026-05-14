print( r'Haizz, \n neu mot ngay nao do ')
#Chuỗi trần sử dụng r
strA = "HowKteam"
strB = strA[:]
#Toán tử in (nhận được 1 trong 2 đáp án true hoặc false)
#Kiểm tra 1 chuỗi có nằm bên trong chuỗi khác hay không.
strC = strB in strA
print(strB)
#Cắt chuỗi
strD = strA[1:len(strA)]
print(strD)
#Cắt từ phải qua trái 
strB = strA[None:None:2]
print(strB)
#Bước không được phép đặt là 0
strA = int(6.9)
print(strA)
#Biến số thành chuỗi
strB = str(69) + "5"
print(strB)
#Thay đổi 1 chữ trong chuỗi
strA = "HowKteam.com"
strA = strA[None:1] + "0" + strA[2:None]
print(hash(strA))