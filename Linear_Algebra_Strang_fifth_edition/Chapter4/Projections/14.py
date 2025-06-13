# 14
# if b is 2 times the first column of A, projecting b into A keep b the same
# P is not necessarly I because A doesn;'t depend on b
import numpy as np

A = np.array([[0,1],[1,2],[2,0]])
b = 2*np.array(A[:,0])

P = A@np.linalg.inv((A.T@A))@A.T

print(f"The projection Matrix P\n {P}")
print(f"The projection p\n {P@b}")