s = 'abcdefghij'
print(s[1:6:2])
print(s[::1])
print(s[::2])
print(s[::3])
print(s[::-1]) # Reverse String
''' step value = -1
     backward direction of string
     begining = 3 
     end = end+1 = 7+1 = 8 
     can not go 3 to 8 in backward direction thats why result is empty '''
print(s[3:7:-1])
print(s[7:4:-1])
print(s[0:10000:1]) # Slice operator never raises IndexError 
''' step = -1
    begining = -4
    end = end +1 = 1+1 =2
    going to -4 to 2 in backward direction  '''
print(s[-4:1:-1])
print(s[3:1:-2])
print(s[5:0:1]) # In forward direction if end value is 0 then result is always empty
#print(s[9:0:0])   Step value can not be zero ;result will be ValueError
print(s[0:-10:-1]) 
print(s[0:-11:-1])
print(s[-5:-9:-2])
print(s[0:0:1]) # In forward direction if end value is 0 then result is always empty
print(s[0:-9:-2])
print(s[10:-1:-1])  # In backward direction if end value is -1 then result is always empty
''' step = -1
    begining = 10000
    end = end +1 = 2+1 = 3
    going to 10000 to 3 in backward direction  '''
print(s[10000:2:-1])

