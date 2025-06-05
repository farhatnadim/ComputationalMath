import numpy as np

a1 = np.array([1, 0])
a2 = np.array([1, 2])

print(f"Constructing A , by stacking {a1} and {a2}\n")
A = np.vstack((a1,a2)).T
print(f"A becomes\n {A}")

#9 calclulcate P 
print(f"Calculating the Projection P ")
try:
    P = A@np.linalg.inv(A.T@A)@A.T
    print(f"P is\n{P}")
except np.linalg.LinAlgError:
    print(f"P doesn't have an inverse\n")


#10 
def get_projection_matrix(vector_in : np.array) -> np.array:
        return np.outer(vector_in,vector_in)/ np.dot(vector_in,vector_in)

def get_projections(projection_matrix : np.array, b:np.array) -> np.array:
        return projection_matrix @ b 

print(f"first we find the projection matrix P2\n")
P2 = get_projection_matrix(a2)
print(f"P2 is \n {P2}")
p_a1_onto_a2 = get_projections(P2,a1)
print(f"then we compute the projection {p_a1_onto_a2}")
print(f"now we need to compute the projection back to a1\n")
P1 = get_projection_matrix(a1)
print(f"P1 is \n {P1}")
p_a12_onto_a1 = get_projections(P1,p_a1_onto_a2)
print(f".. and the projection back to a1 is not giving us a1 \n {p_a12_onto_a1}")
print(f"it goes without saying that P2P1 is not the identify like in the case of orthogonal basis\n {P1@P2}" )

