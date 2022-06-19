
#positional and keyword argument

# CASE -1 :
import imp
from turtle import width


name = "prodip"
salary = 30000
age  = 33

print("{}'s salary is {} and his age is {}".format(name,salary,age))
print("{0}'s salary is {1} and his age is {2}".format(name,salary,age) )
print("{x}'s salary is {y} and his age is {z}".format(z=age,x=name,y=salary))


# CASE - 2 :

print("The integer number is : {}".format(123))
print("The integer number is : {:d}".format(123))
print("The integer number is : {:5d}".format(123))
print("The integer number is : {:05d}".format(123))


print("The float number is : {}".format(123.4567))
print("The float number is : {:f}".format(123.4567))
print("The float number is : {:8.3f}".format(123.4567))
print("The float number is : {:08.3f}".format(123.4567))
print("The float number is : {:08.3f}".format(123.45))
print("The float number is : {:08.3f}".format(786786123.45))


print("Binary Form : {0:b}".format(153))
print("Octal Form : {0:o}".format(153))
print("Hexa Decimal Form : {0:x}".format(154))
print("Hexa Decimal Form : {0:X}".format(154))




# CASE - 3


print("int value with sign:{:+d}".format(123))
print("int value with sign:{:+d}".format(-123))
print("float value with sign:{:+f}".format(123.456))
print("float value with sign:{:+f}".format(-123.456))




# CASE - 4 

print("{:5d}".format(12))
print("{:<5d}".format(12))
print("{:<05d}".format(12))
print("{:>5d}".format(12))
print("{:>05d}".format(12))
print("{:^5d}".format(12))
print("{:=5d}".format(-12))
print("{:^10.3f}".format(12.23456))
print("{:=8.3f}".format(-12.23456))



# CASE - 5 

print("{:5d}".format(12))
print("{:5}".format("rat"))
print("{:>5}".format("rat"))
print("{:<5}".format("rat"))
print("{:^5}".format("rat"))
print("{:*^5}".format("rat")) # Instead of * we can use any character like &,$,a 



# CASE - 6 


print("{:.3}".format("prodipsarkar"))
print("{:5.3}".format("prodipsarkar"))
print("{:>5.3}".format("prodipsarkar"))
print("{:^5.3}".format("prodipsarkar"))
print("{:*^5.3}".format("prodipsarkar"))


# CASE - 7 


person = {'age':33,'name':'prodip'}
print("{p[name]}'s age is :{p[age]}".format(p=person)) # p is alias name of dictionary 



persons = {'age':19,'name':'Mou'}
print("{name}'s age is :{age}".format(**persons))




# CASE - 8 

class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
print("{p.name}'s age is :{p.age}".format(p=Person('prodip',33)))
print("{p.name}'s age is :{p.age}".format(p=Person('Mou',19)))
print("{p.name}'s age is :{p.age}".format(p=Person('Ashim',53)))
print("{p.name}'s age is :{p.age}".format(p=Person('Hasi',43)))


# CASE - 9 

string = "{:{fill}{align}{width}}"
print(string.format('cat',fill='*',align='^',width='5'))
print(string.format('cat',fill='*',align='^',width='6'))
print(string.format('cat',fill='*',align='<',width='6'))
print(string.format('cat',fill='*',align='>',width='6'))


# CASE - 10 


num = "{:{align}{width}.{precision}f}"
print(num.format( 123.236,align='<',width='8',precision=2))
print(num.format( 123.236,align='>',width='8',precision=2))



# CASE - 11 

import datetime
date = datetime.datetime.now()
#print(date)
print("It's now :{:%d/%m/%Y %H:%M:%S}".format(date))


# CASE - 12

complexNumber = 1+2j
print("Real Part:{0.real} and Imaginary Part :{0.imag}".format(complexNumber))