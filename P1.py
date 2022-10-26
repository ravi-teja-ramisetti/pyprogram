# Python program to find sum of elements in list
total = 0
# creating a list
l= [11,5,17,18,23]
# Iterate each element in list
# and add them in variable total
for val in range(0,len(l)):
	total =total+l[val]

# printing total value
print("Sum of all values in given list:{}".format(total))
print("===============or===============")

import math
l=[11,5,17,18,23]
result=math.fsum(l)
print("result:{}".format(result))



