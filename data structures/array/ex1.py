from array import *

# Initalizes an array of type integer
array1 = array('i', [10,20,30,40,50])

array1.insert(0,60)  # 60,10,20,30,40,50
array1.remove(50)    # 60,10,20,30,40

value = ""
for x in array1:
   value += str(x) + " "

print(value)






