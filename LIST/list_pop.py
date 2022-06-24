n = [10,20,30,10,40]
print(n.pop())
print(n.pop())
print(n)

'''
n = []
print(n.pop()) # IndexError

'''

n = [10,20,30,40,50,60]
print(n.pop())
print(n.pop(1))
print(n.pop(10)) # IndexError