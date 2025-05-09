import sympy as sp

A = sp.Matrix([[0,1,2,3,4],[0,0,0,1,2]])
B = sp.Matrix{}
print(A.nullspace())
