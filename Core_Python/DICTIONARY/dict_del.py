d = {100: 'Prodip', 200: 'Rahul', 300: 'Basu', 400: 'Prodip'}
print(d)
del d[300]
print(d)

#del d[700] # KeyError


d = {100: 'Prodip', 200: 'Rahul', 300: 'Basu', 400: 'Prodip'}
print(d)
d.clear()
print(d)

# NameError
d = {100: 'Prodip', 200: 'Rahul', 300: 'Basu', 400: 'Prodip'}
print(d)
del d 
print(d)
