
import numpy as np
# import sympy as sp # Not needed for this part
from fractions import Fraction # Import the Fraction class directly

b1 = np.array([1,2,2])
a1 = np.array([1,1,1])
b2 = np.array([1,3,1]) # Not used for problem #1
a2 = np.array([-1,-3,-1]) # Not used for problem #1

a_s = [a1,a2]
b_s = [b1,b2]
 
# 1. Project the vector b1 onto the line through a1.
# Calculate the scalar projection x_hat
# x_hat = (a1 . b1) / (a1 . a1)
dot_a1_b1 = np.dot(a1, b1)
dot_a1_a1 = np.dot(a1, a1)
x_hat = dot_a1_b1 / dot_a1_a1

# Calculate the projection vector p
# p = x_hat * a1
p = x_hat * a1

# Set NumPy print options to display elements as fractions
# This affects how NumPy arrays are printed.
np.set_printoptions(formatter={'all':lambda x: str(Fraction(x).limit_denominator())})

print(f"Vector a1: {a1}")
print(f"Vector b1: {b1}")

print(f"Projection vector p = x_hat * a1: {p}")
# 2. Check that e is perpendicular to a.
# Calculate the error vector e
# e = b1 - p
e = b1 - p
print(f"Error vector e = b1 - p: {e}")

# Calculate the dot product of e and a1
# If e is perpendicular to a1, then e . a1 = 0
dot_e_a1 = np.dot(e, a1)
print(f"Dot product of e and a1 (e . a1): {Fraction(dot_e_a1).limit_denominator()}")

# Check for perpendicularity (dot product close to zero)
if np.isclose(dot_e_a1, 0):
    print("The error vector e IS perpendicular to a1 (their dot product is 0).")
else:
    print("The error vector e IS NOT perpendicular to a1.")

