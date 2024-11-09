from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])

print(arr1)

# Insert an element into the end of the array
arr1.insert(6, 7) #Inserts 7 at the 6th position since the array contains 0-5 index already

print(arr1)

# Insert an element into the beginning of the array
arr1.insert(0, 0)
print(arr1)

# Insert an element into the middle of the array (index 2)
arr1.insert(2, 9)
print(arr1)