import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def get_projection_matrix(vector_in : np.array) -> np.array:
        return np.outer(vector_in,vector_in)/ np.dot(vector_in,vector_in)

def get_projections(projection_matrix : np.array, b:np.array) -> np.array:
        return projection_matrix @ b 

def draw_vector_3d(ax, origin, vector_components, color='r', label=None, arrow_length_ratio=0.1, **kwargs):
    """
    Draws a 3D vector on the given Axes3D object.

    Parameters:
    - ax: The matplotlib.axes._subplots.Axes3DSubplot object.
    - origin: A 3-element list, tuple, or numpy array representing the origin (tail) of the vector.
    - vector_components: A 3-element list, tuple, or numpy array representing the (dx, dy, dz) components.
    - color: Color of the vector.
    - label: Label for the vector (for legend).
    - arrow_length_ratio: Ratio of the arrow head to the vector length.
    - **kwargs: Additional keyword arguments passed to ax.quiver().
    """
    origin = np.asarray(origin)
    vector_components = np.asarray(vector_components)

    ax.quiver(origin[0], origin[1], origin[2],
              vector_components[0], vector_components[1], vector_components[2],
              color=color, label=label, arrow_length_ratio=arrow_length_ratio, **kwargs)

def set_axes_equal_3d(ax):
    """
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc.

    This is one way to attempt to make the aspect ratio equal.
    It sets the box aspect to match the data ranges.
    For true visual "cubeness" of the plot box itself, use ax.set_box_aspect([1,1,1]).
    """
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))

    ax.set_xlim3d([origin[0] - radius, origin[0] + radius])
    ax.set_ylim3d([origin[1] - radius, origin[1] + radius])
    ax.set_zlim3d([origin[2] - radius, origin[2] + radius])
    # For newer matplotlib versions, you might prefer:
    # ax.set_box_aspect([1,1,1]) # This makes the plot box a cube
    # Or to make data units equal:
    # ax.set_box_aspect([np.ptp(ax.get_xlim()), np.ptp(ax.get_ylim()), np.ptp(ax.get_zlim())])


# --- Main script ---
if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # --- Define vectors ---

    # Vector 1: From origin (0,0,0) to (2,3,4)
    origin1 = np.array([0, 0, 0])
    a1 = np.array([-1, 2, 2])

    # Vector 2: From origin (0,0,0) to (-1, -2, 1)
    origin2 = np.array([0, 0, 0])
    a2 = np.array([2, 2, -1])

    # Vector 3: Starting from point (1,1,1) with components (1, -2, -2)
    origin3 = np.array([0, 0, 0])
    a3 = np.array([2, -1, 2])

    # --- Draw vectors using the helper function ---
    draw_vector_3d(ax, origin1, a1, color='blue', label='a1')
    draw_vector_3d(ax, origin2, a2, color='green', label='a2')
    draw_vector_3d(ax, origin3, a3, color='red', label='a3')
    
    # Optional: Mark the origin points if they are not (0,0,0)
    ax.scatter(origin1[0], origin1[1], origin1[2], color='k', s=20) # Origin (0,0,0)
   

    # --- Set up plot appearance ---
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Vector Visualization')

    # Determine plot limits dynamically based on all points (origins and vector tips)
    all_points = np.array([
        origin1, origin1 + a1,
        origin2, origin2 + a2,
        origin3, origin3 + a3,
        [0,0,0] # Ensure origin is included for auto-scaling if all vectors are far
    ])
    
    x_min, y_min, z_min = np.min(all_points, axis=0)
    x_max, y_max, z_max = np.max(all_points, axis=0)

    # Add some padding to the limits
    padding = 1.0 
    ax.set_xlim([x_min - padding, x_max + padding])
    ax.set_ylim([y_min - padding, y_max + padding])
    ax.set_zlim([z_min - padding, z_max + padding])

    # Try to make aspect ratio equal
    # set_axes_equal_3d(ax) # Use this helper for older matplotlib
    # For newer matplotlib (>= 3.3.0), this is often better for equal data scaling:
    ax.set_box_aspect([np.ptp(ax.get_xlim()), np.ptp(ax.get_ylim()), np.ptp(ax.get_zlim())])
    # If you want the plot box itself to be a cube regardless of data scales:
    # ax.set_box_aspect([1,1,1])

    ax.legend()
    ax.grid(True)

    plt.show()

   
    
    a_vectors = [a1,a2,a3]
    projections_matrices = []
    for vector in a_vectors:
        projections_matrices.append(get_projection_matrix(vector))
    print(projections_matrices)
    # number 5 get P1 , P2 
    print(f"P1 {projections_matrices[0]}\n")
    print(f"P2 {projections_matrices[1]}\n")
    print(f"P1*P2 {projections_matrices[1]@projections_matrices[0]} \n")
    #number 6 
   
    projections =[]
    b = np.array([1,0,0])

    for projection_matrix in projections_matrices:
        print(projection_matrix)
        print(get_projections(projection_matrix,b))
        projections.append(get_projections(projection_matrix,b))
    print(f"p1+p2+p3 { projections[0] + projections[1] + projections[2] }") # which is b 

    # 7 show that P1 + P2 + P3 = I 
    print(projections_matrices[0]+projections_matrices[1]+projections_matrices[2])