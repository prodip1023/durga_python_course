
#  By using while loop

n = [10,20,40,'Prodip',80,[30,50,80,39]]
i = 0
while i<len(n) :
    print(n[i])
    i +=1 


# By using for loop 

n = [10,20,40,'Prodip',80,[30,50,80,39]]
for i in n :
    print(i)


# To dispaly only even numbers 


n = [0,1,2,3,4,5,6,7,8,9,10]
for i in n :
    if i%2==0 :
        print("the number is even",i) 


# To display emements by index wise 


l = ["A","B","C"]
x = len(l)
for i in range(x) :
    print(l[i],"is available at position index :",i," and at negetive index :",i-x)
    