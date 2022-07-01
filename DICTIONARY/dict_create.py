from weakref import proxy


d = {}
print(type(d))


d = dict()
print(type(d))

d[100] = "Prodip"
d[200] = "Rahul"
d[300] = "Basu"
d[400] = "Prodip"
print(d)

