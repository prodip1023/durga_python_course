

import prodip_math
print(prodip_math.x)
prodip_math.add(20,30)
prodip_math.product(20,3)

import prodip_math as pm 
print(pm.x)
pm.add(20,60)
pm.product(20,10)


from prodip_math import x,add 
print(x)
add(10,20)
#product(30,4) # nameError


from prodip_math import * 
print(x)
add(10,20)
product(30,4) 



from prodip_math import x as y,add as sum 
print(y)
sum(33,40)



print(dir(prodip_math))