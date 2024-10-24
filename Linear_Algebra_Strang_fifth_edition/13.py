import sympy as sp 

A = sp.Matrix([[1, 1,0], [1, 3, 1], [3, 1, -1]])
U = sp.Matrix([[1,1,0],[0,2,1],[0,0,0]])


print("A Reduced Row Echelon form",A.rref())
tr_A = A.T




print("U Reduced Row Echelon form",U.rref())
tr_U = U.T
print(tr_U)
print(tr_A)
# True