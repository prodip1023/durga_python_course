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

# float data type 
f = 1.23 
print(type(f))
f = 1.2e3
f1= 1.2E5 
print(f)
print(f1)

# bool data 
b = True
print(type(b))

#str data type
s1 = "prodip"
print(s1)
s2 = 'prodip'
print(s2)
s3 = ''' I am 
       an Engineer '''
print(s3)
s4 = """ I am  
      a Hacker """
print(s4)

s = "prodip sarkar "
print(s[0])
print(s[4])
print(s[-1])
#print(s[40])
print(s[1:40])
print(s[1:])
print(s[:4])
print(s[:])
print(s * 3 )
print(len(s))
