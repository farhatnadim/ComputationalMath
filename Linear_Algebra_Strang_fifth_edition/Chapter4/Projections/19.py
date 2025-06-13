import numpy as np 

# Method I  
# a) find the left nullspace to the normal vector
# b) in 3D the left nullspace will be a 3D plane since the vectors spaces are orthogonal
# c) The left nullspace will be matrix A 
A = np.array([[2,1],[0,1],[1,0]])
P1 = A@np.linalg.inv(A.T@A)@A.T
print(P1)
# Method II
# a) Get the normal vector
# b) Get the projection Matrix into that Vector
# c) since the spaces are orthogonal we can do P = I -Q

e = np.array([1,-1,-2])
Q = np.outer(e,e.T) / np.dot(e,e)
P2 = np.eye(3)-Q

print(P2)