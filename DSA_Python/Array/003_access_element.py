from array import *

def accessElement(array, index):
    if index >= len(array):
        print("There is no element at this index")
    else:
        print(array[index])

arr1 = array('i', [1, 2, 3, 4, 5, 6])
accessElement(arr1, 3) #4