import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 1.0 # Charge of the particle 
q = 1.0 # Mass of the particle
dt = 0.01 # Time step
steps = 1000 # Number of time steps

position = np.array([0.0, 0.0, 0.0]) # Initial position
velocity = np.array([1.0, 1.0, 1.0]) # Initial velocity

E = np.array([0.0, 0.0, 0.0]) # Electric field
B = np.array([0.0, 0.0, 1.0]) # Magnetic field

positions = [position]

# Simulation loop

for _ in range(steps):
    # Calculate Lorentz force
    force = q * (E + np.cross(velocity, B))
    
    # Acceleration
    acceleration = force / m
    
    # Update velocity
    velocity += acceleration * dt
    
    # Update position
    position += velocity * dt
    
    # Store position
    positions.append(position.copy())

positions = np.array(positions)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
ax.set_title("Particle Trajectory")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
