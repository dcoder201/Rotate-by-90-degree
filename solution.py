import numpy as np
def rotate(matrix): 
    #code here
    size = len(matrix)
    np_matrix = np.array(matrix)
    reversed_imatrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        reversed_imatrix[i, size-i-1]=1

    result=np.transpose(np.dot(np_matrix, reversed_imatrix))
    
    for i in range(size):
        for j in range(size):
            matrix[i][j]=result[i,j]
