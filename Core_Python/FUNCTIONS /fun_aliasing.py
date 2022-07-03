def wish(name) :
    print("Good Morning",name)

greeting = wish
print(id(greeting))
print(id(wish))

wish("prodip")
greeting("prodip")




def wish(name) :
    print("Good Morning",name)

greeting = wish
wish("prodip")
greeting("prodip")

del wish   # NameError 
greeting("Mou")
