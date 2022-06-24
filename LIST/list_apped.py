# append() Function 
'''
l = [10,20,40,49,50]
l.append("prodip")
l.append(40)
print(l)
'''



list = []
list.append("P")
list.append("R")
list.append("O")
list.append("D")
list.append("I")
list.append("P")
print(list)



# to add all elements to list upto 100 which are divisibe by 10 

list = []
for i in range(101) :
    if i % 10 == 0 :
        list.append(i)
print(list)