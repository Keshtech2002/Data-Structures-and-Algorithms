import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDArray)

new2DArray_row = np.delete(twoDArray, 0, axis=0) # Delete first row
print(new2DArray_row)

new2DArray_col = np.delete(twoDArray, 0, axis=1) # Delete first col
print(new2DArray_col)