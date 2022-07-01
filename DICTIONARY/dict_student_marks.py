
n = int(input("Enter the number of Students :"))
d = {}
for i in range(n) :
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")
    d[name] = marks

while True:
    name = input("Enter Student Name to get marks: ")
    marks = d.get(name,-1)
    if marks == -1 :
        print("Student Not Found")
    else :
        print("The Marks of",name,"are",marks)
        option = input("Do you want to find another student marks[Yes|No]")
        if option == "No" :
            break
print("Thanks for using our Application")






