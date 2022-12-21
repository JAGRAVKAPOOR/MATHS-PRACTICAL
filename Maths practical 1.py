import numpy as np
import math
mat1 = np.matrix(input("write elements separated by spaces, and separate rows with semi-colon:"))
mat2 = np.matrix(input("write elements separated by spaces, and separate rows with semi-colon:"))
mat3 = mat1 * mat2
print("matrix 1 is: ", mat1,"\n")
print("Transpose of Matrix 1 is: ", mat1.T, "\n")
print("matrix 2 is: ", mat2,"\n")
