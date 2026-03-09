import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    matrix = np.asarray(A)
    n,m = matrix.shape
    t_matrix = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            t_matrix[i][j] = matrix[j][i]
    return t_matrix