#List data type 
a = [10,20,30,40]
print(type(a))
list = [10,10.5,'prodip',True,10]
print(list)
print(list[0])
print(list[-1])
print(list[1:3])
list[0] = 100
for i in list :
    print(i)

list2 = [10,10.6,"prodip"]
list2.append(20)
print(list2)
list2.remove(10.6)
print(list2)
print(list2 * 2)

#print(dir(list))

#Tuple data type 
t = (10,20,30,40)
print(type(t))

#Range data type

r = range(10)
for i in r :
    print(i)

r = range(10,20)
for i in r :
    print(i)

r = range(20,30,2)
for i in r :
    print(i)


#set data type
s = {10,20,"prodip",True,10.3}
print(type(s))
s.add(40)
print(s)
s.remove("prodip")
print(s)

#frozenset data type
s = {10,20,"prodip",True,10.3}
s1 = frozenset(s)
print(type(s1))
for i in s1 :
    print(i)

#dict data type
d ={"name":"prodip","address" :"barasat"}
print(type(d))
for i in d :
    print(i)
d["name"]="pradip"
print(d)
for i in d :
    print(i)

d = {}
d['location'] = 88.239
d['dept'] ="IT"
print(d)
for i in d :
    print(i)

print("this  is Escape character section")
s = "prodip\nsarkar"
s1 = "prodip\tsarkar"
s2 = "prodip\rsarkar"
s3 = "prodip\bsarkar"
s4 = "prodip\fsarkar"
s5 = "prodip\vsarkar"
s6 = "prodip\'sarkar"
s7 = "prodip\''sarkar"
s8 = "prodip\\sarkar"
print(s,s1,s2,s3,s4,s5,s6,s7,s8)


#s20 = " pro\rdip is a good boy "
#s30 = "pro\bdip sarkar"
#s40 = "pro\fdip  sar\fkar"
#s50 = "pro\vdip\vsar\vkar"
#print(s50)