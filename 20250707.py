import pandas as pd
import numpy as np

# Load the CSV file
file_path = "/Users/jiangdawei/Desktop/Data_Collection1/visualization/data1.csv"
df = pd.read_csv(file_path)

# Extract the x, y, z coordinates
x = df['x'].values
y = df['y'].values
z = df['z'].values

# Create the grid
r_points = len(np.unique(df['r'].values))
phi_points = len(np.unique(df['phi'].values))

# Create an empty list for the OBJ file content
obj_content = []

# Write vertices (v)
for i in range(len(x)):
    obj_content.append(f"v {x[i]} {y[i]} {z[i]}")

# Write faces (f)
for i in range(r_points - 1):  # Avoid the last row for the faces
    for j in range(phi_points - 1):  # Avoid the last column for the faces
        # Current index
        idx1 = i * phi_points + j
        idx2 = (i + 1) * phi_points + j
        idx3 = (i + 1) * phi_points + (j + 1)
        idx4 = i * phi_points + (j + 1)

        # Write face (quad) in OBJ format (we're assuming the mesh is quadrilateral)
        obj_content.append(f"f {idx1 + 1} {idx2 + 1} {idx3 + 1} {idx4 + 1}")

# Save to OBJ file
output_path = "/Users/jiangdawei/Desktop/Data_Collection1/visualization/surface.obj"
with open(output_path, "w") as obj_file:
    obj_file.write("\n".join(obj_content))

print(f"OBJ file saved to {output_path}")
