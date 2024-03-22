# Plot radial distribution function (RDF) using matplotlib and the coordinates of the particles in the simulation.

# Read posis_010.xyz file
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

# Set current directory as default path
path = "/Users/manel/EIA-G3-1/src"

os.chdir(path)

data = np.loadtxt('posis.xyz', skiprows=2, usecols=(1, 2, 3))
# Replace first column with the number of the particle


print(len(data))

# Plot the data with matplotlib

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2])
plt.show()


# Calculate the radial distribution function

# Distance between particles
def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

distances = []

for i in range(len(data)):
    for j in range(len(data)):
        if i != j:
            distances.append(distance(data[i], data[j]))
            print(distance(data[i], data[j]))

# Normalize the distances to plot the radial distribution function
distances = np.array(distances) / np.max(distances)


# make a histogram of the distances
plt.hist(distances, bins=25, density=True)
plt.show()

