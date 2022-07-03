#  By using index


t = (10,20,30,40,50,60)
print(t[0])
print(t[4])
print(t[-2])
print(t[-5])
#print(t[100]) # tuple index out of range



# By using slice operator 

t = (10,20,30,40,50,60) 
print(t[:])
print(t[2:5])
print(t[2:100])
print(t[::2])


#'tuple' object does not support item assignment
'''
t = (10,20,30,40,50,60)  
t[2] = 100
print(t)
'''