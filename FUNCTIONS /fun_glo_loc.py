a = 10 # Global variable
def f1() :
    a = 777 # Local variable 
    print(a)
    print(globals()['a'])

f1()
