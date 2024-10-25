import sympy as sp 

A = sp.Matrix([[1, 1,0], [1, 3, 1], [3, 1, -1]])
# Getting the columspace dimension for A
# we get the reduced row echelon form and the number of pivots 
rref_A, pivots = A.rref() 
print("Dimension of the column space of Matrix A ",len(pivots))
# Getting the rowspace dimension for A
# first we get the transpose and we get the columnspace of the transpose 
rref_transpose_A, pivots = A.T.rref()
print(f"Dimension of the rowspace of Matrix A {len(pivots)}")
# we same process for U 
U = sp.Matrix([[1,1,0],[0,2,1],[0,0,0]])
# Getting the columspace dimension for U
# we get the reduced row echelon form and the number of pivots 
rref_U, pivots = U.rref() 
print("Dimension of the column space of Matrix U ",len(pivots))
# Getting the rowspace dimension for U
# first we get the transpose and we get the columnspace of the transpose 
rref_transpose_U, pivots = U.T.rref()
print(f"Dimension of the rowspace of Matrix U {len(pivots)}")

# checking if spaces are the same , is checking if the spaces are a linear combination of each others
import numpy as np 

A_np = np.array([[1, 1,0], [1, 3, 1], [3, 1, -1]])
U_np = np.array([[1,1,0],[0,2,1],[0,0,0]])
