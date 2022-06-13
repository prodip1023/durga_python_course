# How to read multiple values from the keyboard in a single line :
''''a,b = [int(x)for x in input("Enter 2 numbers:").split()]
print("product is :",a*b)
'''
# write a program to read 3 float numbers from the keyboard with seperator and print sum

''''a,b,c = [float(x)for x in input("Enter 3 numbers:").split(',')]
print("The sum :",a+b+c)
'''

'''x = eval("10+20+40")
print(x)
'''
'''x = eval(input("enter the expression :"))
print(x)
'''
#Write a program to accept list from the keyboard on the display

x = eval(input("enter the Tuple :"))
print(type(x))
print(x)