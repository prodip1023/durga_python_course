# minimum values
a = int(input("enter the First number :"))
b = int(input("enter the Second number :"))
min = a if a<b else b
print("the minimum value is:",min)

# minimum of three numbers 
a = int(input("enter the First number :"))
b = int(input("enter the Second number :"))
c = int(input("enter the Third number :"))
min = a if a<b and a<c else b if b<c else c 
print("the minimum value is:",min)

