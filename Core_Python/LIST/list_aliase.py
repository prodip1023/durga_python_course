x = [10,20,30,40]
y = x 
print(id(x))
print(id(y))


x = [20,340,495,595]
y = x 
y[2] = 899
print(x)
