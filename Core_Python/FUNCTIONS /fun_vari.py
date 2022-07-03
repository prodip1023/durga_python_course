def sum(*n) :
    total = 0
    for n1 in n :
        total = total + n1
    print("The sum :",total)

sum()
sum(10)
sum(10,20)
sum(10,20,30,40)

# We can mix variable length arguments with positional arguments.
def f1(n1,*s) :
    print(n1)
    for s1 in s :
        print(s1)
f1(10)
f1(10,20,34,30)
f1(10,"A",20,"B")
