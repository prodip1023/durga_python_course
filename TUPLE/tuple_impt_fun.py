# len() Function 


t = (10,20,40,50)
print(len(t)) 


# count() Function 

t = (10,20,90,20,40,20,50) 
print(t.count(20))


# index() Function 
t = (10,20,40,50) 
print(t.index(20))
#print(t.index(200)) # x not in tuple

# sorted() Function 
t = (10,20,90,20,40,20,50) 
t1 = sorted(t)
t2 = tuple(t1)
print(t2)


t = (10,20,90,80,40,5,50) 
t1 = sorted(t,reverse=True)
print(t1)


# min() and max() Function 
t = (10,20,90,80,40,5,50) 
print(max(t))
print(min(t))


'''
# cmp() Function 

t1 = (10,20,30)
t2 = (40,50,60)
t3 = (10,20,30)
print(cmp(t1,t2)) 
print(cmp(t1,t3))
print(cmp(t2,t3))
'''

# Reversed() Function  

t = (10,20,30,40)
t1= reversed(t)
t2 = tuple(t1)
print(t2)
