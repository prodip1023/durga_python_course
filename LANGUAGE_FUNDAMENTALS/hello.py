print(" My name is prodip")


# Addition  two numbers 
a= 10
b= 20
print("sum of this two number is :",(a+b))

# reserved word


import keyword
print("the list of keywords:")
print(keyword.kwlist)


# type of variable
a = 10 
print(type(a))

# id 
print (id(a))

# complex data type
a = 10 + 15j
print(a.real) 
print(a.imag)
# sum of complex data type 
c = 10+3j
d = 15+6j
print(c+d)

# int data type 
a= 10
print(a)
print(type(a))

"""" represent int values in following forms :
    1. Decimal form (base 10)(0-9)
    2. Binary form (base 2) (0 & 1)(any base to -> bin)(0b or 0B)
    3. Octal form (base 8)(0-7) (0o or 0O)(any base to -> oct)
    4. Hexa decimal form (base 16)(0-9,a-f)(0x or 0X)(any base to -> hex)
"""
# Base conversion 
print(bin(15))
print(bin(0o11))
print(oct(10))
print(oct(0B1111))
print(hex(100))
print(hex(0B1111))