import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDArray)

print("The number of rows are", len(twoDArray))
print("The number of cols are", len(twoDArray[0]))

def accessElem(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("There is no element at this index")
    else:
        print(array[rowIndex][colIndex])


accessElem(twoDArray, 3, 2) #14