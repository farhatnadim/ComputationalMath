import sympy

# Define the matrix
A = sympy.Matrix([[1, 2, -5, -4],
                  [1, 3, -6, -3],
                  [1, 2, -5, -1]])

# Calculate the nullspace basis
# The nullspace() method returns a list of basis vectors for the nullspace
null_space_basis = A.nullspace()

# Print the matrix and the result
print(f"Matrix A:\n{A}")

print(f"A basis for the nusllspace of A is: {null_space_basis}")
print(A.rref())