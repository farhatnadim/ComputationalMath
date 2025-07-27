# find the parabola that fits the five points below 
import numpy as np 
#input
t_vec = np.array([-2,-1,0,1,2])
#output 
b_vec= np.array([0,0,1,0,0])

A = np.zeros((t_vec.shape[0],3))
print(A.shape)

A[:,0] = 1
A[:,1] = t_vec[:]
A[:,2] = t_vec[:]**2
print(A)

# now find the C,D,E

coef = np.linalg.solve(A.T@A,A.T@b_vec)
#print(coef)
# solution from the book 
tol = 0.000001
sol_vec = np.array([34/70,0,-10/70])
#

assert(np.sum(np.abs(sol_vec-coef)) < tol)