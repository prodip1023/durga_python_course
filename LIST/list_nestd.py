a = [[100,230,500],[200,340,50],[300,400,600],10,30,50,60]
print(a)
print(a[0])
print(a[2][1])




# In Python we can represent matrix by using nested lists. 

n = [[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Elements by Row Wise :")
for r in n :
    print(r)
print("Elements by Matrix Wise :")
for i in range(len(n)) :
    for j in range(len(n[i])) :
        print(n[i][j],end=' ')
    print()


# List comprehension 
s = [x*x for x in range(1,11)]
print(s) 

word = ["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l = [w[0] for w in word]
print(l)




words = "the quick brown fox jumps over the lazy dog".split()
print(words)
l = [[w.upper(),len(w)] for w in words]
print(l)
