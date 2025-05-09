import sympy as sp
# v = [1,2,3] in columnspace and nullspace 
A = sp.Matrix([[1,2,3],[2,4,5],[3,11,7]])
# v = [1,2,3] in nullspace nd columnspace
B = sp.Matrix([[1,1,-1],[2,5,-4],[3,3,-3]])
print(B.nullspace())