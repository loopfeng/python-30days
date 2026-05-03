# Assign the integer value 4 to variable a.(integer)
a = 4

print(a)

#datatype of a
print(type(a))

#Assign the float value 1.96 to variable b.(float)
b = 1.96
print(b)
print(type(b))

#Import all contents from the decimal library
from decimal import*

# Get up to 30 digits for the integer and decimal parts of Decimal.
# From the decimal library, import everything (*) into the program.
getcontext().prec = 30

f = 10/3
print(f)
print(type(f))

d = 10/Decimal(3)
print(d)
print(type(d))
