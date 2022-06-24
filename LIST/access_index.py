# By using index

a = [10,20,30,20,10]
print(a[0])
print(a[-3])
#print(a[100])
#print(a[-39])




# By using Slice Operator

n = [1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])



# MUtable 

n = [10,20,"B",40,39]
print(n)
n[2] = "C" 
print(n)