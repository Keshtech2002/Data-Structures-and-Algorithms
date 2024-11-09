from array import *

def accessElement(array, index):
    if index >= len(array):
        print("There is no element at this index")
    else:
        print(array[index])


accessElement(arr1, 3) #4