import numpy as np

def rotation_matrix_x(theta):
  """Creates a 3D rotation matrix around the X-axis."""
  cos_t = np.cos(theta)
  sin_t = np.sin(theta)
  return np.array([
      [1, 0,     0    ],
      [0, cos_t, -sin_t],
      [0, sin_t, cos_t ]
  ])

def rotation_matrix_y(phi):
  """Creates a 3D rotation matrix around the Y-axis."""
  cos_p = np.cos(phi)
  sin_p = np.sin(phi)
  return np.array([
      [cos_p,  0, sin_p],
      [0,      1, 0    ],
      [-sin_p, 0, cos_p]
  ])

def rotation_matrix_z(psi):
  """Creates a 3D rotation matrix around the Z-axis."""
  cos_s = np.cos(psi)
  sin_s = np.sin(psi)
  return np.array([
      [cos_s, -sin_s, 0],
      [sin_s, cos_s,  0],
      [0,     0,      1]
  ])

def check_orthogonality(matrix, tol=1e-9):
    """Checks if the columns of a matrix are mutually orthogonal."""
    cols = matrix.T # Get columns as rows
    n_cols = cols.shape[0]
    for i in range(n_cols):
        for j in range(i + 1, n_cols):
            dot_product = np.dot(cols[i], cols[j])
            if not np.isclose(dot_product, 0, atol=tol):
                print(f"Columns {i} and {j} are NOT orthogonal. Dot product: {dot_product}")
                return False
    print("All column pairs are orthogonal (within tolerance).")
    return True

def check_non_zero_entries(matrix, tol=1e-9):
    """Checks if all entries of the matrix are non-zero."""
    if np.any(np.isclose(matrix, 0, atol=tol)):
        print("Matrix contains zero (or near-zero) entries.")
        return False
    else:
        print("Matrix does not contain zero (or near-zero) entries.")
        return True

# --- Parameters ---
# Choose angles that are not multiples of pi/2 to increase chances of non-zero entries
# Using radians directly, or converting degrees
angle_x_deg = angle_y_deg = angle_z_deg =45
theta = np.radians(angle_x_deg)
phi   = np.radians(angle_y_deg)
psi   = np.radians(angle_z_deg)

# Let's use slightly less standard radians directly
#theta = np.sqrt(2)/2 # radians around X
#phi   = theta # radians around Y
#psi   = phi # radians around Z

# --- Calculation ---
print(f"Using angles (radians): theta={theta:.4f}, phi={phi:.4f}, psi={psi:.4f}\n")

# Define the rotation matrices
Rx = rotation_matrix_x(theta)
Ry = rotation_matrix_y(phi)
Rz = rotation_matrix_z(psi)

# Combine the rotations (order matters, ZYX is common for Euler angles)
# The final matrix A is the combined rotation matrix itself
A = Rz @ Ry @ Rx

print("Resulting Matrix A:")
print(np.round(A, 5)) # Print rounded for readability
print("\n--- Checks ---")

# Check 1: Orthogonality
is_orthogonal = check_orthogonality(A)

# Check 2: Non-zero entries
has_no_zeros = check_non_zero_entries(A)

print("\n--- Verification ---")
# Mathematically, A should be an orthogonal matrix. Check A^T * A = I
identity_check = A.T @ A
print("A^T @ A (should be close to Identity):")
print(np.round(identity_check, 5))
print(f"Is A^T @ A close to Identity? {np.allclose(identity_check, np.identity(3), atol=1e-9)}")

# --- Conclusion ---
print("\nConclusion on the method:")
if is_orthogonal and has_no_zeros:
    print("The method WORKED for these specific angles.")
    print("The resulting matrix has mutually orthogonal columns and non-zero entries.")
elif is_orthogonal and not has_no_zeros:
     print("The method PARTIALLY worked.")
     print("The resulting matrix has mutually orthogonal columns BUT contains zero entries.")
     print("You would need to try different angles.")
else:
     print("Something went wrong, the resulting matrix columns are not orthogonal (check code/math).")