import numpy as np


A = np.eye(4,4)
A = A[:,:-1]

P = A@np.linalg.inv(A.T@A)@A.T
print(P@np.array([1,2,3,4]))