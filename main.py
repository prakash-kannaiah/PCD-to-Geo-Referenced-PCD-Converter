import open3d as o3d
import numpy as np

# Initialize GPS and heading parameters
tx = 0  # latitude
ty = 0   # longitude
tz = 0           # altitude

# Define rotation angle (Z-axis), in radians
rz = 0
theta = np.radians(rz)

# Load the PCD file
pcd = o3d.io.read_point_cloud("pointcloud_map.pcd")

# Step 1: Rotate point cloud around Z-axis (origin)
rotation_matrix = pcd.get_rotation_matrix_from_axis_angle([0, 0, theta])
pcd.rotate(rotation_matrix, center=(0, 0, 0))  # Rotate around origin

# Step 2: Translate point cloud
translation = np.array([tx, ty, tz])
pcd.translate(translation)

# Visualize result
o3d.visualization.draw_geometries([pcd], window_name="Transformed PCD")

# Save result
o3d.io.write_point_cloud("output_transformed.pcd", pcd)
print("Transformed point cloud saved as 'output_transformed.pcd'.")
