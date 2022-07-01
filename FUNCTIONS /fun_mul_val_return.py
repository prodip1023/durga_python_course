'''def sum_sub(a,b) :
    sum = a+b
    sub = a-b
    return sum,sub

x,y = sum_sub(15,10)
print("the sum is :",x)
print("the sub is :",y)


'''
# calculator 

def cal(a,b) :
    sum = a+b
    sub = a-b
    div = a/b
    mul = a*b
    return sum,sub,div,mul
t = cal(100,50)
print("the result are :" )
for i in t :
    print(i)
