'''

s = input(" Enter the main String :")
subs = input( "Enter the Sub String :")
try :
    n = s.index(subs)
except ValueError :
    print("Substring not found")
else :
    print("Substring found") 
    
s = "ABCDEFGH"
print(s.index("F",3,40000))  # no ValueError ,like Slice operator  
    
      '''


mail = input("enter the mail id is :")
try :
    i = mail.index("@")
    print("mandatory symbol @ ")
except ValueError :
    print("mail id doesn't cointain @ symbol ")