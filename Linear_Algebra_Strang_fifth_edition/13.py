import sympy as sp 

A = sp.Matrix([[1, 1,0], [1, 3, 1], [3, 1, -1]])
U = sp.Matrix([[1,1,0],[0,2,1],[0,0,0]])

U_A = A.copy()
U_A[1,:] = U_A[1,:] - U_A[0,:]
U_A[2,:] = U_A[2,:] - 3 * U_A[0,:]
U_A[2,:] = U_A[2,:] + U_A[1,:]
print(U_A==U)