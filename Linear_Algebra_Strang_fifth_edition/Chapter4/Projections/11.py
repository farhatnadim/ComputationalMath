# number 11 , project b into a 2D plane in a 3D space 
# by finding by solving for x_hat first and then find the projection p 
import numpy as np


def get_x_hat(A : np.array, b :np.array) -> np.array:
    return np.linalg.inv(A.T@A)@A.T@b

def get_projection(A:np.array, b:np.array) -> np.array:
    x_hat = get_x_hat(A,b)
    return A@x_hat
# error 
def get_e(A:np.array, b:np.array) -> np.array:
    p = get_projection(A,b)
    return b - p 
# check for perpendicular e to A
def check_perpendicular(A:np.array,b:np.array)-> bool :
    for index in range(A.shape[1]):
        if np.dot(get_e(A,b),A[:,index]) == 0 :
            return True
        else :
            return False

As =[ np.array([[1,1],[0,1],[0,0]]),np.array([[1,1],[1,1],[0,1]])]
bs =[ np.array([2,3,4]), np.array([4,4,6])] 

for index in range(len(As)):
    print(f"Computing p {get_projection(As[index],bs[index])}")
    print(f"Checking e {check_perpendicular(As[index],bs[index])}")