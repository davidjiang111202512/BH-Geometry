import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
M = 1.0

# Create grid in r and phi
r = np.linspace(2.1, 10, 100)  # finer grid for better resolution
phi = np.linspace(0, 2 * np.pi, 100)

# Meshgrid
R, Phi = np.meshgrid(r, phi)

# Embedding function for Flamm's paraboloid
Z = 2 * np.sqrt(2 * M * (R - 2 * M))

# Convert to Cartesian coordinates
X = R * np.cos(Phi)
Y = R * np.sin(Phi)

# Flatten arrays
R_flat = R.ravel()
Phi_flat = Phi.ravel()
X_flat = X.ravel()
Y_flat = Y.ravel()
Z_flat = Z.ravel()

# Create DataFrame with clear labels
df = pd.DataFrame({
    "r": R_flat,
    "phi": Phi_flat,
    "x": X_flat,
    "y": Y_flat,
    "z": Z_flat
})

# Save to CSV (easy to read)
file_path = "/Users/jiangdawei/Desktop/geometry/Data_Collection1/data1.csv"
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
print("Preview:")
print(df.head())

# Plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap="viridis", edgecolor="k", linewidth=0.5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Schwarzschild Metric Embedded by Flamm's Paraboloid (M=1)")

plt.show()








