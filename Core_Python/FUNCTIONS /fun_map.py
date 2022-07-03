# Without Lambda function 

l = [1,2,3,4,5]
def doublelt(x) :
    return 2 * x 
l1 = list(map(doublelt,l))
print(l1)

# With Lambda function 
l = [1,2,3,4,5] 
l1 = list(map(lambda x : 2*x,l))
print(l1)

l = [1,2,3,4,5] 
l1 = list(map(lambda x : x*x,l))
print(l1)


# Multiple list 
l1 = [1,2,3,4]
l2 = [2,3,4,5]
l3 = list(map(lambda x,y:x*y,l1,l2))
print(l3)
