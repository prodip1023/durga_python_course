# Write a program to access each charcter of string in Forward and Backward direction by using while loop?
'''

# Method -1
s = "Learning Python is very easy !!!"
n = len(s)
i = 0
print("Forward Direction")
while i<n :
    print(s[i],end='')
    i=i+1
print("Backward Direction")
i=-1
while i>= -n :
    print(s[i],end='')
    i=i-1

'''

# Method -2 
s = "Learning Python is very easy !!!"
print("Forward Direction")
for i in s :
    print(i,end='')
print("Forward Direction")
for i in s[::] :
    print(i,end='')
print("Backward Direction")
for i in s[::-1] :
    print(i,end='')
    
