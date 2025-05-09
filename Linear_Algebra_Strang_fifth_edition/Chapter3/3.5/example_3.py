from sympy import Matrix , init_printing, pprint

A = Matrix([[-1,1,0,0],[-1,0,1,0],[0,-1,1,0,],[0,-1,0,1],[0,0,-1,1]])
N_A = A.nullspace()
pprint(N_A)

rref_A = A.rref()
transpose = A.transpose()

pprint(rref_A)
pprint(transpose.rref())