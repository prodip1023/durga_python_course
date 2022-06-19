s = input("Please enter Strings :")
i = 0
for x in s  :
    print("The character present at Positive index {} and at negative index {} is {}".format(i,i-len(s),x))
    i=i+1
