import numpy as np
# A is a 2-d array
def get_column_from_bottom_to_top( A, c ):
    return A[::-1,c]
def get_odd_rows( A ):
    return A[1::2]
def get_even_column_last_row( A ):
    return A[-1][::2]
def get_diagonal1( A ): # A is a square matrix
    return A.diagonal()
# # from top-left corner down to bottom-right corner
def get_diagonal2( A ): # A is a square matrix
    x = []
    a= np.fliplr(A)
    diag = a.diagonal()
    return diag
# # from top-right corner down to bottom-left corner
A=np.array([[1,2,3],[4,5,6],[7,8,9]]);print(get_diagonal2(A))