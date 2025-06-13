# what linear combination of (1,2,-1) and (1,0,1) is closest to b 
import numpy as np

A = np.array([[1,1],[2,0],[-1,1]])
b = np.array([2,1,1])

P = A@np.linalg.inv((A.T@A))@A.T
p = P@b
print(np.linalg.inv((A.T@A))@A.T@b)