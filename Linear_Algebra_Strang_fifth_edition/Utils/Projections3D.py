import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D # For 3D plotting
matplotlib.use('qtAgg') # Or 'Qt5Agg', 'GTK3Agg', 'WXAgg'
# Define the orthogonal basis vectors for the plane (column space)
a1 = np.array([1, 0, 1])
a2 = np.array([0, 1, 0]) # a1 and a2 are orthogonal

# Ensure they are unit vectors for easier plane plotting (optional, but good practice for some methods)
# a1 = a1 / np.linalg.norm(a1)
# a2 = a2 / np.linalg.norm(a2)

# Define vector b to be projected
b = np.array([1, 2, 3])

# Calculate the projection of b onto a1
proj_a1_b = (np.dot(b, a1) / np.dot(a1, a1)) * a1

# Calculate the projection of b onto a2
proj_a2_b = (np.dot(b, a2) / np.dot(a2, a2)) * a2

# The projection p onto the plane spanned by a1 and a2 is the sum of individual projections
p = proj_a1_b + proj_a2_b

# Alternative calculation using the projection matrix P = A(A^T A)^-1 A^T
# A = np.column_stack((a1, a2))
# P = A @ np.linalg.inv(A.T @ A) @ A.T
# p_matrix_method = P @ b
# print(f"Projection using matrix method: {p_matrix_method}") # Should be same as p

# Create the 3D plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot vector a1
ax.quiver(0, 0, 0, a1[0], a1[1], a1[2], color='blue', label='Vector a1 (basis of plane)', arrow_length_ratio=0.1)
# Plot vector a2
ax.quiver(0, 0, 0, a2[0], a2[1], a2[2], color='cyan', label='Vector a2 (basis of plane)', arrow_length_ratio=0.1)
# Plot vector b
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='red', label='Vector b', arrow_length_ratio=0.1)
# Plot the projection p
ax.quiver(0, 0, 0, p[0], p[1], p[2], color='green', label='Projection of b onto plane (p)', arrow_length_ratio=0.1)

# Draw a dashed line from b to its projection p (error vector e = b - p)
ax.plot([b[0], p[0]], [b[1], p[1]], [b[2], p[2]], linestyle='--', color='gray', label='Error vector e = b - p')

# Plot the plane spanned by a1 and a2
# Create a grid of points on the plane
# We need two parameters (s, t) such that any point on the plane is s*a1 + t*a2
s_vals = np.linspace(-1.5, 1.5, 10)
t_vals = np.linspace(-1.5, 1.5, 10)
S, T = np.meshgrid(s_vals, t_vals)

X = S * a1[0] + T * a2[0]
Y = S * a1[1] + T * a2[1]
Z = S * a1[2] + T * a2[2]

ax.plot_surface(X, Y, Z, alpha=0.2, color='lightblue', rstride=1, cstride=1, label='Plane spanned by a1 and a2')


# Set plot limits and labels
ax.set_xlim([-1, 3])
ax.set_ylim([-1, 3])
ax.set_zlim([-1, 4])
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
ax.set_title("Projection of Vector b onto a Plane (Column Space)")

# Add a legend. 3D legends can be tricky, adjust as needed or place manually.
# Due to a Matplotlib bug, plot_surface doesn't directly support labels for legends.
# We create a proxy artist for the legend.
from matplotlib.patches import Patch
proxy_plane = Patch(facecolor='lightblue', alpha=0.2, label='Plane spanned by a1, a2')
handles, labels = ax.get_legend_handles_labels()
handles.append(proxy_plane)
ax.legend(handles=handles)


# Set view angle for better visualization
ax.view_init(elev=20, azim=30) # Adjust elevation and azimuth angle

plt.show()

print(f"Vector a1: {a1}")
print(f"Vector a2: {a2}")
print(f"Vector b: {b}")
print(f"Projection of b onto a1: {proj_a1_b}")
print(f"Projection of b onto a2: {proj_a2_b}")
print(f"Projection of b onto plane (p): {p}")
print(f"Error vector (e = b - p): {b - p}")
# The error vector e should be orthogonal to both a1 and a2
print(f"Dot product of e and a1 (should be close to 0): {np.dot(b - p, a1)}")
print(f"Dot product of e and a2 (should be close to 0): {np.dot(b - p, a2)}")