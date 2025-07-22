import numpy as np

# find the projection into columnspace of A
A = np.array([[3,6,6],[4,8,8]])
a = A[:,0].reshape(2,1)
p_c = (np.outer(a,a)/np.dot(a,a.T))
print(p_c)
# find the projection into the rowspace of A
A_rowspace = A.T
a_rowspace = A_rowspace[0,:]

p_r = (np.outer(a_rowspace,a_rowspace.T)/np.dot(a_rowspace,a_rowspace.T))
print(p_r)